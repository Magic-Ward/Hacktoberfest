import random
import time

# --- Game data ---
questions = [
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
    },
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "lambda"],
        "answer": "def"
    },
    {
        "question": "What data type is the value: [1, 2, 3]?",
        "options": ["tuple", "set", "list", "dict"],
        "answer": "list"
    },
    {
        "question": "Which operator is used for floor division?",
        "options": ["/", "//", "%", "**"],
        "answer": "//"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pt", ".pyth", ".py", ".p"],
        "answer": ".py"
    }
]

# --- Game intro ---
def intro():
    print("🧙‍♂️ Welcome to Code Quest! 🧩")
    print("Test your Python powers and collect XP by answering correctly.")
    print("Let’s begin your coding adventure...\n")
    time.sleep(2)

# --- Game logic ---
def play_game():
    score = 0
    random.shuffle(questions)
    for q in questions:
        print(f"\n💡 {q['question']}")
        for i, opt in enumerate(q["options"], start=1):
            print(f"{i}. {opt}")
        try:
            choice = int(input("\nYour answer (1-4): "))
            if q["options"][choice - 1] == q["answer"]:
                print("✅ Correct! +10 XP")
                score += 10
            else:
                print(f"❌ Oops! The correct answer was: {q['answer']}")
        except (ValueError, IndexError):
            print("⚠️ Invalid choice! You lost this round.")

        time.sleep(1)

    print("\n🏁 Game Over!")
    print(f"Your total XP: {score}")

    if score >= 40:
        print("🔥 You’re a Python Master!")
    elif score >= 20:
        print("💻 Great job, Python Apprentice!")
    else:
        print("🐍 Keep practicing, young coder!")

# --- Run the game ---
if __name__ == "__main__":
    intro()
    play_game()
