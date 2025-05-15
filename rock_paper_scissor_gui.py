import random
import tkinter as tk
from tkinter import messagebox

# Mapping choices to emojis
emoji_choices = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# Function to play game
def play_game(choice):
    computer = random.choice([-1, 0, 1])
    youDict = {"Rock": 1, "Paper": -1, "Scissors": 0}
    reverseDict = {1: "🪨 Rock", -1: "📄 Paper", 0: "✂️ Scissors"}

    you = youDict[choice]

    result = ""
    if computer == you:
        result = "🤝 It's a draw!"
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        result = "🎉 You win!"
    else:
        result = "😢 You lose!"

    messagebox.showinfo("Result", f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}\n\n{result}")

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors 🎮")
root.geometry("400x300")
root.configure(bg="#A8E6CF")  # Light Green Background

label = tk.Label(root, text="Choose One:", font=("Arial", 16), fg="black", bg="#A8E6CF")
label.pack(pady=15)

frame = tk.Frame(root, bg="#A8E6CF")
frame.pack()

# Creating buttons with emojis
for choice in ["Rock", "Paper", "Scissors"]:
    btn = tk.Button(
        frame, text=emoji_choices[choice], font=("Arial", 20), width=5, 
        command=lambda c=choice: play_game(c),
        bg="white", fg="black", relief="raised"
    )
    btn.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()