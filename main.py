import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
DARKBLUE = "#082032"
DARKBLUEGREY ="#2C394B"
BLUEGREY = "#334756"
BURNTORANGE ="#ff4c29"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #



window =tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=DARKBLUE)

canvas = tkinter.Canvas(width=202, height=224, bg=DARKBLUE, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file=r"pomodoroapp\tomato.png")
canvas.create_image(100,112, image=tomato_image)
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=BURNTORANGE, bg=DARKBLUE)
timer_label.grid(row=0, column=1)












window.mainloop()