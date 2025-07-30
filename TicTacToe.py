import tkinter as tk
from tkinter import messagebox

current_player = "X"

def button_click(row, col):
    global current_player

    buttons[row][col].config(text=current_player, state="disabled",
                              disabledforeground="#ffffff") 

    if check_winner(current_player):
        messagebox.showinfo("Game Over", f"🌸 Player {current_player} wins! 🌸")
        disable_all_buttons()
    elif is_draw():
        messagebox.showinfo("Game Over", "It's a draw! 🐻")
        disable_all_buttons()
    else:
        current_player = "O" if current_player == "X" else "X"

def check_winner(player):
    for row in buttons:
        if all(cell["text"] == player for cell in row):
            return True
    for col in range(3):
        if all(buttons[row][col]["text"] == player for row in range(3)):
            return True
    if all(buttons[i][i]["text"] == player for i in range(3)):
        return True
    if all(buttons[i][2 - i]["text"] == player for i in range(3)):
        return True
    return False

def is_draw():
    for row in buttons:
        for cell in row:
            if cell["text"] == "":
                return False
    return True

def disable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

def restart_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn.config(text="", state="normal")

window = tk.Tk()
window.title("Tic Tac Toe")
window.configure(bg="#ffe6f0")  

buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        btn = tk.Button(window, text="", width=8, height=3,
                        font=("Comic Sans MS", 24, "bold"),
                        bg="#ffb6c1",         
                        activebackground="#ff9ac1",  
                        fg="#ffffff",         
                        command=lambda r=row, c=col: button_click(r, c))
        btn.grid(row=row, column=col, padx=5, pady=5)
        buttons[row][col] = btn

restart_btn = tk.Button(window, text="Restart Game 🔁",
                        font=("Comic Sans MS", 14, "bold"),
                        bg="#dda0dd", fg="#ffffff",
                        activebackground="#ba55d3",
                        command=restart_game)
restart_btn.grid(row=3, column=0, columnspan=3, pady=10)

window.mainloop()
