import random
import tkinter as tk

emoji_choices = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# Game State
your_score = 0
computer_score = 0
is_dark_mode = False

def toggle_dark_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    bg_color = "#2C3E50" if is_dark_mode else "#A8E6CF"
    fg_color = "white" if is_dark_mode else "black"

    root.configure(bg=bg_color)
    label.config(bg=bg_color, fg=fg_color)
    result_label.config(bg=bg_color, fg=fg_color)
    frame.config(bg=bg_color)
    score_label.config(bg=bg_color, fg=fg_color)
    mode_button.config(bg="gray" if is_dark_mode else "white")
    for widget in frame.winfo_children():
        widget.config(bg="white", fg="black")

def play_game(choice):
    global your_score, computer_score

    computer = random.choice([-1, 0, 1])
    youDict = {"Rock": 1, "Paper": -1, "Scissors": 0}
    reverseDict = {1: "🪨 Rock", -1: "📄 Paper", 0: "✂️ Scissors"}

    you = youDict[choice]

    if computer == you:
        result = "🤝 It's a draw!"
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        result = "🎉 You win!"
        your_score += 1
    else:
        result = "😢 You lose!"
        computer_score += 1

    show_result(reverseDict[you], reverseDict[computer], result)
    update_score()

def show_result(you, computer, result):
    result_text = f"You chose {you}\nComputer chose {computer}\n\n{result}"
    animate_result(result_text)

def animate_result(text, i=0):
    result_label.config(text="")
    def update():
        nonlocal i
        if i <= len(text):
            result_label.config(text=text[:i])
            i += 1
            root.after(30, update)
    update()

def update_score():
    score_label.config(text=f"You: {your_score}    Computer: {computer_score}")

# UI Setup
root = tk.Tk()
root.title("Rock Paper Scissors 🎮")
root.geometry("450x400")
root.configure(bg="#A8E6CF")

label = tk.Label(root, text="Choose One:", font=("Arial", 16), fg="black", bg="#A8E6CF")
label.pack(pady=10)

frame = tk.Frame(root, bg="#A8E6CF")
frame.pack()

for choice in ["Rock", "Paper", "Scissors"]:
    btn = tk.Button(
        frame, text=emoji_choices[choice], font=("Arial", 20), width=5,
        command=lambda c=choice: play_game(c),
        bg="white", fg="black", relief="raised"
    )
    btn.pack(side=tk.LEFT, padx=10, pady=10)

score_label = tk.Label(root, text="You: 0    Computer: 0", font=("Arial", 14), bg="#A8E6CF")
score_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 13), wraplength=400, bg="#A8E6CF")
result_label.pack(pady=10)

mode_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode, bg="white", font=("Arial", 11))
mode_button.pack(pady=5)

root.mainloop()
