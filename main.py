from tkinter import *
import math
from tkinter import messagebox
import pygame


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOGGLE_LOCK = False
reps = 0
timer = None

pygame.mixer.init()
def play_sound():
    pygame.mixer.music.load("davidgoggins.mp3")
    pygame.mixer.music.play(loops=0)




# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    play_sound()
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = f"00:00 ")
    timer_label.config(text="Timer")
    check_labels.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8 == 0:
        timer_label.config(text = "Break", fg= RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        timer_label.config(text="Short-Break", fg= PINK)
        count_down(short_break)

    else:
        timer_label.config(text="WORK", fg= GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

        minute = math.floor(count / 60)
        seconds = count % 60



        if seconds < 10:
            seconds = f"0{seconds}"

        canvas.itemconfig(timer_text, text = f"{minute}:{seconds} ")
        if count > 0:
            global timer
            timer = window.after(1000, count_down, count -  1)
        else:
            start_timer()
            play_sound()
            mark = ""
            messagebox.showerror(title= "Break Time",message= "TIME TO TAKE A BREAK")
            for _ in range(math.floor(reps/2)):
                mark += "✔"

            check_labels.config(text = mark)






# ---------------------------- UI SETUP ------------------------------- #

 # sets up window and title and padding
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50 , bg= YELLOW )




 # create canvas
canvas = Canvas(width = 200 , height= 224 , bg = YELLOW, highlightthickness= False)
tmt_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tmt_image)
timer_text = canvas.create_text(100, 130, text = "00:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1, sticky='nesw')
 


# buttons and labels

timer_label = Label(text= "Timer", font= (FONT_NAME, 35, "bold"), fg = GREEN, bg = YELLOW)
timer_label.grid(row = 0, column =1)

start_button = Button(text = "Start", fg = "black", bg = "RoyalBlue1", width= 5, command= start_timer)

start_button.grid(row = 2, column = 0)


reset_button = Button(text = "Reset", fg = "black", bg = "RoyalBlue1", width= 5, command= reset_timer)

reset_button.grid(row = 2, column =2)

check_labels = Label( font= (FONT_NAME, 15, "bold"), fg = GREEN, bg = YELLOW)
check_labels.grid(row = 3, column =1)










window.mainloop()
