import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text = tk.Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
text.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
image= tk.PhotoImage(file="./tomato.png")
canvas.create_image(100, 115, image=image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

btn_start = tk.Button(text="Start")
btn_start.grid(column=0, row=2)

btn_reset = tk.Button(text="reset")
btn_reset.grid(column=2, row=2)

check = tk.Label(text="✔", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=2)

window.mainloop()