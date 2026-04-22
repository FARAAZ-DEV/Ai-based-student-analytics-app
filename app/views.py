import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .ml_model import predict

# Admin credentials

ADMIN_USER = "admin"
ADMIN_PASS = "admin123"

# Simple login required decorator

def login_required(view):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("logged_in"):
            return redirect("login")
        return view(request, *args, **kwargs)
    wrapper.__name__ = view.__name__
    return wrapper

# Views

def login_view(request):
    error = ""
    if request.method == "POST":
        if (request.POST.get("username") == ADMIN_USER and
                request.POST.get("password") == ADMIN_PASS):
            request.session["logged_in"] = True
            return redirect("dashboard")
        error = "Invalid credentials."
    return render(request, "login.html", {"error": error})

# No registration or user management for simplicity

def logout_view(request):
    request.session.flush()
    return redirect("login")

# Dashboard view with analytics and student list

# ── READ ────────────────────────────────────────────────────────────────────────

@login_required
def dashboard(request):
    students_qs = Student.objects.all() # SELECT * FROM app_student
    enriched = []
    for s in students_qs:
        p = predict(s.marks, s.attendance)
        enriched.append({
            "id":           s.id,
            "name":         s.name,
            "roll_no":      s.roll_no,
            "marks":        s.marks,
            "attendance":   s.attendance,
            "pass_fail":    p["pass_fail"],
            "grade":        p["grade"],
            "dropout_risk": p["dropout_risk"],
            "suggestion":   p["suggestion"],
        })

    sorted_marks  = sorted(enriched, key=lambda x: x["marks"])
    weak_students = sorted_marks[:5]
    top_students  = sorted_marks[-5:][::-1]

    pass_count = sum(1 for s in enriched if s["pass_fail"] == "Pass")
    fail_count = len(enriched) - pass_count

    # Clean JSON for Chart.js
    chart_data = json.dumps([
        {"name": s["name"], "marks": s["marks"], "attendance": s["attendance"]}
        for s in enriched
    ])

    return render(request, "dashboard.html", {
        "students":      enriched,
        "weak_students": weak_students,
        "top_students":  top_students,
        "pass_count":    pass_count,
        "fail_count":    fail_count,
        "chart_data":    chart_data,
    })

# Add/Edit/Delete student views

# ── CREATE ──────────────────────────────────────────────────────────────────────

@login_required
def add_student(request):
    error = ""
    if request.method == "POST":
        try:
            Student.objects.create(  # INSERT INTO app_student VALUES(...)
                
                name       = request.POST["name"].strip(),
                roll_no    = request.POST["roll_no"].strip(),
                marks      = float(request.POST["marks"]),
                attendance = float(request.POST["attendance"]),
            )
            return redirect("dashboard")
        except Exception as e:
            error = str(e)
    return render(request, "add_student.html", {"error": error, "action": "Add", "student": None})

# ── UPDATE ─────────────────────────────────────────────────────────────────────

@login_required
def edit_student(request, pk):
    s = get_object_or_404(Student, pk=pk)
    error = ""
    if request.method == "POST":
        try:
            
            # modifies Python object fields

            s.name       = request.POST["name"].strip()
            s.roll_no    = request.POST["roll_no"].strip()
            s.marks      = float(request.POST["marks"])
            s.attendance = float(request.POST["attendance"])

            s.save() # UPDATE app_student SET ... WHERE id=pk

            return redirect("dashboard")
        except Exception as e:
            error = str(e)
    return render(request, "add_student.html", {"error": error, "action": "Edit", "student": s})

# ── DELETE ──────────────────────────────────────────────────────────────────────

@login_required
def delete_student(request, pk):

    get_object_or_404(Student, pk=pk).delete() # DELETE FROM app_student WHERE id=pk

    return redirect("dashboard")