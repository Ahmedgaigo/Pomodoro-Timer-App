import math
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
YELLOW = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
PINK = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
	window.after_cancel(time)
	timer.config(text="Timer", fg=GREEN)
	canvas.itemconfig(timer_text, text="00:00")
	check_mark.config(text="")
	global reps
	reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60
	global reps
	reps += 1

	if reps <= 8:
		if reps % 2 != 0:
			timer.config(text="Work", fg=GREEN)
			count_down(work_sec)
		elif reps == 8:
			timer.config(text="Long Break", fg=RED)
			count_down(long_break_sec)
		else:
			timer.config(text="Short Break", fg=PINK)
			count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
	count_min = math.floor(count / 60)
	count_sec = count % 60
	if count_sec < 10:
		count_sec = f"0{count_sec}"

	canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
	if count > 0:
		global time
		time = window.after(1000, count_down, count - 1)
	else:
		start_timer()
		thick = ""
		work_sessions = math.floor(reps / 2)
		for rep in range(work_sessions):
			thick += "✔️"
			check_mark.config(text=thick)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# labels
timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


# buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


# creating  canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")

# to add image
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, fill="white", text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
