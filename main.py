import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = .1
LONG_BREAK_MIN = 20
REPS = 0
CHECK = 0
MARKS = []


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    global CHECK
    global MARKS
    REPS += 1

    short_secs = SHORT_BREAK_MIN * 60
    long_secs = LONG_BREAK_MIN * 60
    work_secs = WORK_MIN * 60

    total_marks = ""

    for mark in MARKS:
        total_marks += mark
 
    check.config(text=total_marks)
    if REPS % 2 != 0:
        countdown(work_secs)
        text.config(text="WORK")
        CHECK += 1
        if CHECK > 0:
            MARKS.append("✔")
    elif REPS % 8 == 0:
        countdown(long_secs)
        text.config(text="BREAK")
    elif REPS % 2 == 0:
        print(MARKS)
        countdown(short_secs)
        text.config(text="BREAK")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count): 
    global REPS
    mins = math.floor(count / 60)
    secs = count % 60
    if secs == 0:
        secs = "00"
    elif secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        window.after(1000, countdown, count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text = tk.Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
text.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
image= tk.PhotoImage(file="./tomato.png")
canvas.create_image(100, 115, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

btn_start = tk.Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)

check = tk.Label(text="", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=2)

btn_reset = tk.Button(text="reset")
btn_reset.grid(column=2, row=2)

window.mainloop()