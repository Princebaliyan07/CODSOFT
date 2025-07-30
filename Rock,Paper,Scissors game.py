import tkinter as tk
import random
# Function for handling the game logic when a button is clicked
def play(user_choice):
    global user_score, computer_score
#Random choice for the computer
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = ""
# Determine the result so using operations
    if user_choice == computer_choice:
        result = "Match TIE!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "Yeah! YOU WIN! Well played buddy"
        user_score += 10
    else:
        result = "Oh! COMPUTER WIN! Better luck next time"
        computer_score += 10

    result_label.config(text=f"You: {user_choice}\nComputer: {computer_choice}\n{result}")
    score_label.config(text=f"Score => You: {user_score} | Computer: {computer_score}")

# Creating main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("550x400")

user_score = 0
computer_score = 0

# Labels
title = tk.Label(window, text="Rock Paper Scissors Game", font=("Arial", 16))
title.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)

score_label = tk.Label(window, text="Score => You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

#Creating the Buttons on window
btn_frame = tk.Frame(window)
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="ROCK", width=10, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0)

paper_btn = tk.Button(btn_frame, text="PAPER", width=10, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1)

scissors_btn = tk.Button(btn_frame, text="SCISSORS  ", width=10, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2)

window.mainloop()
