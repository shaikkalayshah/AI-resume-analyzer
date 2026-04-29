import fitz  # PyMuPDF
import re

# 🔹 Skills list (no C, C++)
skills_list = [
    "python", "java", "javascript", "react", "sql",
    "html", "css", "node", "flask", "django", "testing"
]

# 🔹 Extract text from PDF
def extract_text(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# 🔹 Extract skills using regex (accurate matching)
def extract_skills(text):
    found = []
    text = text.lower()

    for skill in skills_list:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found.append(skill)

    return found


# 🔹 Calculate ATS score
def calculate_score(found_skills):
    return min(len(found_skills) * 10, 100)


# 🔹 Predict job role based on skills
def predict_job_role(skills):

    roles = {
        "Data Analyst": ["python", "sql"],
        "Web Developer": ["html", "css", "javascript", "react"],
        "Backend Developer": ["python", "flask", "django", "node"],
        "Software Engineer": ["java"],
        "QA Engineer": ["testing"]
    }

    role_scores = {}

    for role, required_skills in roles.items():
        score = 0
        for skill in skills:
            if skill in required_skills:
                score += 1
        role_scores[role] = score

    # Get best matching role
    best_role = max(role_scores, key=role_scores.get)

    # If no match
    if role_scores[best_role] == 0:
        return "General IT Role"

    return best_role