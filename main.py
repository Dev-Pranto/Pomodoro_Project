import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def restart_timer():
    global reps

    button1.config(command=start_timer)
    window.after_cancel(str(timer))
    title1.config(text='Timer')
    title2.config(text='')
    canvas.itemconfig(time_text, text='00:00')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    button1.config(command=str(None))

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title1.config(text='Break', fg=RED)
        title2.config(text='✔️')
    if reps % 2 == 0:
        count_down(short_break_sec)
        title1.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        title1.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    second = count % 60
    minute = count // 60
    if second < 10:
        second = '0' + str(second)
    if minute < 10:
        minute = '0' + str(minute)
    canvas.itemconfig(time_text, text=str(minute)+':'+str(second))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += '✔️'
        title2.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Technic')
window.config(padx=200, pady=200, bg=YELLOW)

title1 = Label(text='Timer', font=(FONT_NAME, 34, 'bold'), bg=YELLOW, fg=GREEN)
title1.config(padx=10, pady=10)
title1.grid(column=1, row=0)

title2 = Label(text='', font=(FONT_NAME, 18, 'bold'), bg=YELLOW, fg=GREEN)
title2.config(padx=10, pady=10)
title2.grid(column=1, row=3)

canvas = Canvas(width=230, height=230, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(115, 115, image=img)
time_text = canvas.create_text(115, 130, text='00:00', fill='white', font=(FONT_NAME, 34, 'bold'))
canvas.grid(column=1, row=1)


button1 = Button(text='Start', bg=PINK, font=(FONT_NAME, 18, 'bold'), command=start_timer)
button1.config(padx=10, pady=10)
button1.grid(column=0, row=2)

button2 = Button(text='Reset', bg=PINK, font=(FONT_NAME, 18, 'bold'), command=restart_timer)
button2.config(padx=10, pady=10)
button2.grid(column=2, row=2)

window.mainloop()
