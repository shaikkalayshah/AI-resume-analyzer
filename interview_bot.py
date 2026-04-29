# Generate questions ONLY based on detected skills
def generate_questions(skills):

    questions_bank = {
        "python": [
            "What is a list in Python?",
            "Explain OOP concepts in Python.",
            "What is a dictionary?"
        ],
        "java": [
            "What is JVM?",
            "Explain inheritance in Java.",
            "What is exception handling?"
        ],
        "javascript": [
            "What is JavaScript?",
            "Difference between var, let, and const?",
            "What is DOM?"
        ],
        "sql": [
            "What is JOIN?",
            "Difference between WHERE and HAVING?",
            "What is normalization?"
        ],
        "html": [
            "What is HTML?",
            "Difference between div and span?",
            "What is semantic HTML?"
        ],
        "css": [
            "What is CSS?",
            "What is flexbox?",
            "What is responsive design?"
        ],
        "react": [
            "What is React?",
            "What are hooks?",
            "What is virtual DOM?"
        ],
        "flask": [
            "What is Flask?",
            "What is routing in Flask?",
            "What is Jinja2?"
        ]
    }

    selected_questions = []

    # 👉 Only pick questions for detected skills
    for skill in skills:
        skill = skill.lower().strip()
        if skill in questions_bank:
            selected_questions.extend(questions_bank[skill])

    # 👉 Remove duplicates (important)
    selected_questions = list(dict.fromkeys(selected_questions))

    # 👉 If no skills found → fallback
    if not selected_questions:
        selected_questions = [
            "Tell me about yourself.",
            "What are your strengths?",
            "Why should we hire you?"
        ]

    return "\n".join(selected_questions[:5])  # limit to 5 questions


# Evaluate answer
def evaluate_answer(answer):

    if not answer.strip():
        return "⚠️ Please provide an answer."

    word_count = len(answer.split())

    if word_count > 50:
        return "✅ Excellent answer! Very detailed."
    elif word_count > 25:
        return "👍 Good answer, add examples."
    elif word_count > 10:
        return "⚠️ Average answer. Improve clarity."
    else:
        return "❌ Too short. Explain more."