import tkinter
import time
import math

#constants
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
DARKBLUE = "#082032"
DARKBLUEGREY ="#2C394B"
BLUEGREY = "#334756"
BURNTORANGE ="#ff4c29"

#countdown
# define the countdown function

#define countdown
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    

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

#start work timer function

def start_timer():
    count_down(5*60)
    

#start timer button
start_button = tkinter.Button(text="Start", command=start_timer, bg=BLUEGREY, fg="white", highlightthickness=0)
start_button.grid(row=3, column=0)

#reset work timer function
def reset_timer():
    pass

#reset timer button
reset_button = tkinter.Button(text="Reset", command=reset_timer, bg=BLUEGREY, fg="white", highlightthickness=0)
reset_button.grid(row=3, column=2)


#create checkmark label
check_mark ="✅"

check_mark_label = tkinter.Label(text=check_mark, bg=DARKBLUE, fg=BURNTORANGE)
check_mark_label.grid(row=4, column=1)





window.mainloop()