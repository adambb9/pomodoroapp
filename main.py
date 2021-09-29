import tkinter

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
DARKBLUE = "#082032"
DARKBLUEGREY ="#2C394B"
BLUEGREY = "#334756"
BURNTORANGE ="#ff4c29"




window =tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=DARKBLUE)

canvas = tkinter.Canvas(width=202, height=224, bg=DARKBLUE, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file=r"pomodoroapp\tomato.png")
canvas.create_image(100,112, image=tomato_image)
canvas.create_text(100,130, text="00:00", fill=BLUEGREY, font=(FONT_NAME, 50, "bold"))
canvas.grid(row=1, column=1)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=BURNTORANGE, bg=DARKBLUE)
timer_label.grid(row=0, column=1)

def start_timer():
    pass

start_button = tkinter.Button(text="Start", command=start_timer, bg=BLUEGREY, fg="white", highlightthickness=0)
start_button.grid(row=3, column=0)

def reset_timer():
    pass

reset_button = tkinter.Button(text="Reset", command=reset_timer, bg=BLUEGREY, fg="white", highlightthickness=0)
reset_button.grid(row=3, column=2)

check_mark ="✅"

check_mark_label = tkinter.Label(text=check_mark, bg=DARKBLUE, fg=BURNTORANGE)
check_mark_label.grid(row=4, column=1)











window.mainloop()