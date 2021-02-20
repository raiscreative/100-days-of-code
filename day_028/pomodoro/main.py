from tkinter import *
#import winsound
#frequency = 2500  # Set Frequency To 2500 Hertz
#duration = 1000  # Set Duration To 1000 ms == 1 second
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    check_marks.config(text='')
    start_button.config(state='normal')
    reset_button.config(state='disabled')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state='disabled')
    reset_button.config(state='normal')
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps > 8:
        reset_timer()
    elif reps == 0:
        count_down(long_break_sec)
        title_label.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        #winsound.Beep(frequency, duration)
        window.bell()
        start_timer()
        marks = ''
        for _ in range(reps // 2):
            marks += '✔'
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.iconbitmap('pomodoro.ico')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


start_img = PhotoImage(file='start_button.png')
start_button = Button(image=start_img, highlightthickness=0, borderwidth=0, bg=YELLOW, command=start_timer, state='normal')
start_button.grid(column=0, row=2)

reset_img = PhotoImage(file='reset_button.png')
reset_button = Button(image=reset_img, borderwidth=0, bg=YELLOW, command=reset_timer, state='disabled')
reset_button.grid(column=2, row=2)


check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=4)


window.mainloop()
