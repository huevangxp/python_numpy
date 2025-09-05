import tkinter as tk

root = tk.Tk()
root.title("Quiz")
root.geometry("400x250")

# Questions and answers
questions = [
    {"question": "ປະເທດລາວມີຈັກແຂວງ?", "answer": "18"},
    {"question": "What is the capital city of Laos?", "answer": "Vientiane"},
    {"question": "What is the official language of Laos?", "answer": "Lao"}
]

current_q = 0
entry = None
label = None

def show_question():
    global entry, label
    for widget in root.winfo_children():
        widget.destroy()

    q = questions[current_q]["question"]

    label = tk.Label(root, text=q, font=("Arial", 12))
    label.pack(pady=10)

    entry = tk.Entry(root, width=30, font=("Arial", 12))
    entry.pack(pady=5)

    tk.Button(root, text="Submit", command=check_answer, font=("Arial", 12)).pack(pady=10)


def check_answer():
    global current_q
    answer = entry.get().strip()
    correct_answer = questions[current_q]["answer"]

    for widget in root.winfo_children():
        widget.destroy()

    if answer.lower() == correct_answer.lower():
        result = tk.Label(root, text=f"Correct! ✅ ({answer})", font=("Arial", 12), fg="green")
    else:
        result = tk.Label(root, text=f"Wrong ❌ (You said: {answer}, Correct: {correct_answer})", font=("Arial", 12), fg="red")
    result.pack(pady=10)

    if current_q < len(questions) - 1:
        tk.Button(root, text="Next", command=next_question, font=("Arial", 12)).pack(pady=10)
    else:
        tk.Label(root, text="Quiz Completed 🎉", font=("Arial", 12), fg="blue").pack(pady=10)

def next_question():
    global current_q
    current_q += 1
    show_question()


# Start first question
show_question()

root.mainloop()
