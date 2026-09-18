import re
import random


def extract_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    return [
        sentence.strip()
        for sentence in sentences
        if len(sentence.strip()) > 30
    ]


def generate_mcqs(text, num_questions, difficulty):

    sentences = extract_sentences(text)

    if not sentences:
        return [{
            "question": "Not enough information provided.",
            "options": [
                "Please enter more study material",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer": "Please enter more study material",
            "explanation": "The application needs sufficient study material to generate questions."
        }]

    questions = []

    for sentence in sentences[:num_questions]:

        words = re.findall(
            r'\b[A-Za-z][A-Za-z-]+\b',
            sentence
        )

        if len(words) < 5:
            continue

        answer = random.choice(words)

        question = sentence.replace(answer, "_____")

        wrong_answers = []

        for word in words:
            if word != answer and word not in wrong_answers:
                wrong_answers.append(word)

            if len(wrong_answers) == 3:
                break

        while len(wrong_answers) < 3:
            wrong_answers.append("None of the above")

        options = [answer] + wrong_answers[:3]
        random.shuffle(options)

        questions.append({
            "question": f"Which word correctly completes the statement?\n\n{question}",
            "options": [
                f"A. {options[0]}",
                f"B. {options[1]}",
                f"C. {options[2]}",
                f"D. {options[3]}"
            ],
            "answer": answer,
            "explanation": f"The correct answer is '{answer}' because it appears in the original study material."
        })

        if len(questions) >= num_questions:
            break

    return questions