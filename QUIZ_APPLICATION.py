def ask_question(question, options, correct_answer):
    print("\n" + question)
    for option in options:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").upper()
    if answer == correct_answer:
        print("Correct! ✅")
        return 1
    else:
        print("Wrong! ❌")
        print("Correct answer is:", correct_answer)
        return 0
def main():
    print("=" * 40)
    print("        QUIZ APPLICATION")
    print("=" * 40)
    name = input("Enter your name: ")
    questions = [
        {
            "question": "Q1. Which language is mainly used for Python programming?",
            "options": [
                "A. English",
                "B. Python",
                "C. HTML",
                "D. SQL"
            ],
            "answer": "B"
        },
        {
            "question": "Q2. Which keyword is used to define a function in Python?",
            "options": [
                "A. function",
                "B. define",
                "C. def",
                "D. fun"
            ],
            "answer": "C"
        },
        {
            "question": "Q3. Which data type is used to store multiple values in Python?",
            "options": [
                "A. List",
                "B. Integer",
                "C. Boolean",
                "D. Float"
            ],
            "answer": "A"
        },
        {
            "question": "Q4. Which symbol is used for comments in Python?",
            "options": [
                "A. //",
                "B. /* */",
                "C. #",
                "D. <!-- -->"
            ],
            "answer": "C"
        },
        {
            "question": "Q5. Which function is used to display output in Python?",
            "options": [
                "A. input()",
                "B. print()",
                "C. output()",
                "D. display()"
            ],
            "answer": "B"
        }
    ]
    score = 0
    print("\nHello", name + "!")
    print("Let's start the quiz.")
    for q in questions:
        score += ask_question(
            q["question"],
            q["options"],
            q["answer"]
        )
    total = len(questions)
    percentage = (score / total) * 100
    print("\n" + "=" * 40)
    print("             QUIZ RESULT")
    print("=" * 40)
    print("Name       :", name)
    print("Total      :", total)
    print("Correct    :", score)
    print("Wrong      :", total - score)
    print("Percentage :", percentage, "%")
    if percentage >= 80:
        print("Grade      : A")
    elif percentage >= 60:
        print("Grade      : B")
    elif percentage >= 40:
        print("Grade      : C")
    else:
        print("Grade      : Fail")
    print("=" * 40)
    print("Thank you for playing!")
main()