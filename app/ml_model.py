"""
ml_model.py  –  Simple ML predictions for student performance.
No pre-saved model file needed; we train on the fly with dummy data.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# ── Dummy training data ─────────────────────────────────────────────────────
# Features: [marks, attendance]
X_train = np.array([
    [90, 95], [85, 90], [78, 85], [72, 80], [65, 75],
    [60, 70], [55, 65], [50, 60], [45, 40], [30, 30],
    [20, 25], [15, 20], [40, 50], [35, 45], [70, 55],
    [80, 85], [88, 92], [92, 98], [25, 30], [10, 15],
])

# Pass/Fail  (1 = Pass, 0 = Fail)  –  pass if marks >= 40
y_pass = np.array([1,1,1,1,1, 1,1,1,0,0, 0,0,1,0,1, 1,1,1,0,0])

# Grade: 0=C, 1=B, 2=A
y_grade = np.array([2,2,2,1,1, 1,1,0,0,0, 0,0,0,0,1, 2,2,2,0,0])

# Dropout risk  (1 = at risk)
y_dropout = np.array([0,0,0,0,0, 0,0,0,1,1, 1,1,1,1,0, 0,0,0,1,1])

# ── Train models ────────────────────────────────────────────────────────────
_pass_model    = LogisticRegression(max_iter=200).fit(X_train, y_pass)
_grade_model   = DecisionTreeClassifier().fit(X_train, y_grade)
_dropout_model = LogisticRegression(max_iter=200).fit(X_train, y_dropout)

GRADE_MAP = {2: "A", 1: "B", 0: "C"}

# ── Public API ───────────────────────────────────────────────────────────────
def predict(marks: float, attendance: float) -> dict:
    """Return pass/fail, grade and dropout risk for one student."""
    X = [[marks, attendance]]
    passed  = bool(_pass_model.predict(X)[0])
    grade   = GRADE_MAP[int(_grade_model.predict(X)[0])]
    dropout = bool(_dropout_model.predict(X)[0])

    suggestion = None
    if attendance < 50:
        suggestion = "Improve attendance to increase performance."
    elif marks < 40:
        suggestion = "Focus on studies – extra tutoring recommended."

    return {
        "pass_fail": "Pass" if passed else "Fail",
        "grade":     grade,
        "dropout_risk": "High" if dropout else "Low",
        "suggestion": suggestion,
    }
