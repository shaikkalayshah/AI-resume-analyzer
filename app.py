from flask import Flask, render_template, request
from resume_parser import extract_text, extract_skills, calculate_score, predict_job_role
from interview_bot import generate_questions, evaluate_answer

import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():
    skills = []
    score = 0
    role = ""
    questions = ""
    feedback = ""

    if request.method == "POST":

        # 🔹 Resume Upload
        if "resume" in request.files:
            file = request.files["resume"]

            if file and file.filename != "":
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)

                text = extract_text(file_path)

                # Extract skills
                skills = extract_skills(text)

                # Calculate ATS score
                score = calculate_score(skills)

                # Predict job role
                role = predict_job_role(skills)

                # Generate skill-based questions
                questions = generate_questions(skills)

        # 🔹 Answer Evaluation
        if "answer" in request.form:
            user_answer = request.form["answer"]
            feedback = evaluate_answer(user_answer)

    return render_template(
        "index.html",
        skills=skills,
        score=score,
        role=role,
        questions=questions,
        feedback=feedback,
        skills_data=skills,
        role_name=role
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)