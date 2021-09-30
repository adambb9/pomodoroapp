import tkinter
import time
import math

#constants
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
DARKBLUE = "#082032"
DARKBLUEGREY ="#2C394B"
BLUEGREY = "#334756"
BURNTORANGE ="#ff4c29"

reps = 0
timer = None

#countdown
# define the countdown function
#reset work timer function
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    marks = ""
    check_mark_label.config(text=marks)


#start work timer function

def start_timer():
    global reps
    reps += 1 
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    break_text = "Break"
    work_text = "Work"

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text=break_text)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text=break_text)
    else:
        count_down(work_sec)
        timer_label.config(text=work_text)


#define countdown
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_mark_label.config(text=marks)
    

#create window
window =tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=DARKBLUE)



#create canvas
canvas = tkinter.Canvas(width=202, height=224, bg=DARKBLUE, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file=r"pomodoroapp\tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill=BLUEGREY, font=(FONT_NAME, 50, "bold"))
canvas.grid(row=1, column=1)





#label to hold working time
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=BURNTORANGE, bg=DARKBLUE)
timer_label.grid(row=0, column=1)

   

#start timer button
start_button = tkinter.Button(text="Start", command=start_timer, bg=BLUEGREY, fg="white", highlightthickness=0)
start_button.grid(row=3, column=0)



#reset timer button
reset_button = tkinter.Button(text="Reset", command=reset_timer, bg=BLUEGREY, fg="white", highlightthickness=0)
reset_button.grid(row=3, column=2)


#create checkmark label
check_mark ="✅"

check_mark_label = tkinter.Label(bg=DARKBLUE, fg=BURNTORANGE)
check_mark_label.grid(row=4, column=1)





window.mainloop()