from tkinter import *
from tkinter import Button

import pygame
import random


root = Tk()
root.geometry("800x800")
root.configure(bg="gray")
bg_clr = "gray"

target_clicks = 0
alt_1 = 0
alt_2 = 0
pref_alt_1 = 0
pref_alt_2 = 0

click_pattern = []
button_order = []
points = 0
trial_points = 1
time_count = 0
stream = []
irt_1 = 0
new_interval_1 = 0

trial = 1
trial_type = 1
phase = 2


pygame.init()
pygame.mixer.init()
beep = 'ding.mp3'
pygame.mixer.music.load(beep)

fw = open('data.txt', 'w')
fw_stream = open('stream.txt', 'w')


def record_data():
    global trial
    global target_clicks
    global trial_type
    global alt_1
    global alt_2
    global pref_alt_1
    global pref_alt_2
    global points
    global phase

    fw.write('\n')
    fw.write('phase = ')
    if trial == 11:
        fw.write('4')
    else:
        fw.write(str(phase))
    fw.write('\n')
    fw.write('trial = ')
    fw.write(str(trial))
    fw.write('\n')
    fw.write('target = ')
    fw.write(str(target_clicks))
    fw.write('\n')

    if trial_type == 2:
        fw.write('Alternative 2')
        fw.write('\n')
        fw.write(str(alt_2))
        fw.write('\n')


    elif trial_type == 1:
        fw.write('Alternative 1')
        fw.write('\n')
        fw.write(str(alt_1))
        fw.write('\n')

    fw.write('points = ')
    fw.write(str(points))
    fw.write('\n')

    if trial == 21:
        button_1.grid_remove()
        button_4.grid_remove()
        button_2.grid_remove()
        button_3.grid_remove()
        lbl_end.grid(row=1, column=5)
        lbl_end2.grid(row=3, column=5)
        fw.close()
    target_clicks = 0
    alt_1 = 0
    alt_2 = 0

def record_stream():
    global time_count
    global stream
    fw_stream.write(str(time_count))
    fw_stream.write(str(stream))
    fw_stream.write('\n')
    stream = []

def bg_grey():
    root.configure(bg="gray")
    top_frame.configure(bg="gray")
    bottom_frame.configure(bg="gray")
    middle_frame.configure(bg="gray")
    lbl_points.configure(bg="gray")
    buffer.configure(bg="gray")
    global bg_clr
    bg_clr = "gray"
    if phase == 1:
            button_2.configure(highlightbackground=bg_clr)

def bg_pink():
    root.configure(bg="pink")
    top_frame.configure(bg="pink")
    bottom_frame.configure(bg="pink")
    middle_frame.configure(bg="pink")
    lbl_points.configure(bg="pink")
    buffer.configure(bg="pink")
    global bg_clr
    bg_clr = "pink"
    if phase == 1:
            button_2.configure(highlightbackground=bg_clr)


def bg_cyan():
    root.configure(bg="cyan")
    top_frame.configure(bg="cyan")
    bottom_frame.configure(bg="cyan")
    middle_frame.configure(bg="cyan")
    lbl_points.configure(bg="cyan")
    buffer.configure(bg="cyan")
    global bg_clr
    bg_clr = "cyan"
    if phase == 1:
            button_2.configure(highlightbackground=bg_clr)

def bg_white():
    root.configure(bg="white")
    top_frame.configure(bg="white")
    bottom_frame.configure(bg="white")
    middle_frame.configure(bg="white")
    lbl_points.configure(bg="white")
    buffer.configure(bg="white")
    global bg_clr
    bg_clr = "white"
    if phase == 2:
            button_2.configure(highlightbackground=bg_clr)


def set_interval_1():
    global new_interval_1
    new_interval_1 = random.randrange(1, 20)

set_interval_1()

def move_buttons():
    global button_order
    button_order = [2, 3]
    random.shuffle(button_order)
    if button_order[0] == 2:
        button_2.grid(row=0, column=1, padx=50)
    elif button_order[0] == 3:
        button_1.grid(row=0, column=1, padx=50)

    if button_order[1] == 2:
        button_2.grid(row=0, column=3, padx=50)
    elif button_order[1] == 3:
        button_1.grid(row=0, column=3, padx=50)



def remove_buttons():
    global button_order
    button_1.grid_remove()
    button_4.grid_remove()
    button_2.grid_remove()
    button_3.grid_remove()



def phase_a():
    global bg_clr
    button_2.configure(image=photo1, highlightbackground=bg_clr)
    button_2.grid(row=0, column=5, padx=10)

def phase_b():
    global phase
    phase = 2

def phase_c():
    global phase
    phase = 3

def phase_d():
    global phase
    phase = 4

def set_trial():
    global click_pattern
    global trial_type
    global trial
    global phase
    global irt_1

    if trial_type == 0:
        button_1.configure(highlightbackground=bg_clr)

    elif trial_type == 1:
        button_1.configure(highlightbackground=bg_clr)
        button_2.configure(image=photo2, highlightbackground=bg_clr)
        button_3.configure(image=photo3, highlightbackground=bg_clr)
        button_4.configure(image=photo4, highlightbackground=bg_clr)
        button_1.grid(row=0, column=1, padx=50)
        button_2.grid(row=0, column=3, padx=50)
        button_3.grid_forget()
        button_4.grid_forget()

    elif trial_type == 2:
        button_1.configure(highlightbackground=bg_clr)
        button_2.configure(image=photo3, highlightbackground=bg_clr)
        button_3.configure(image=photo2, highlightbackground=bg_clr)
        button_4.configure(image=photo4, highlightbackground=bg_clr)
        button_1.grid(row=0, column=1, padx=50)
        button_2.grid(row=0, column=3, padx=50)
        button_3.grid_forget()
        button_4.grid_forget()


    elif trial_type == 3:
        button_1.configure(highlightbackground=bg_clr)
        button_2.configure(image=photo2, highlightbackground=bg_clr)
        button_3.configure(image=photo3, highlightbackground=bg_clr)
        button_4.configure(image=photo4, highlightbackground=bg_clr)
        button_1.grid(row=0, column=3, padx=10)
        button_2.grid(row=0, column=5, padx=10)
        button_3.grid(row=0, column=7, padx=10)

    if trial == 21:
        button_1.grid_remove()
        button_4.grid_remove()
        button_2.grid_remove()
        button_3.grid_remove()
        lbl_end.grid(row=1, column=5)
        lbl_end2.grid(row=3, column=5)


def check_count():
    global bg_clr
    global time_count
    global irt_1
    global trial
    global trial_type
    global phase
    global alt_1
    global alt_2
    global pref_alt_1
    global pref_alt_2

    time_count += 1
    record_stream()
    irt_1 += 1
    '''if trial == 1:
        phase_a()'''
    if time_count == 120:
        record_data()
        if trial == 10:
            phase_d()
        trial += 1
        if phase == 1:
            bg_grey()
        elif phase == 3:
            bg_white()
            if phase >= 2:
                set_trial()
        else:
            bg_cyan()
            trial_type = 2
            if phase >= 2:
                set_trial()

    elif time_count == 240:
        record_data()
        if trial == 10:
            phase_d()
        trial += 1
        if phase == 1:
            bg_grey()
        elif phase == 3:
            bg_white()
            set_trial()
        else:
            bg_pink()
            trial_type = 1
            if phase >= 2:
                set_trial()

    elif time_count == 360:
        record_data()
        if trial == 10:
            phase_d()
        trial += 1
        if phase == 1:
            bg_grey()
        elif phase == 3:
            bg_white()
            if phase >= 2:
                set_trial()
        else:
            bg_cyan()
            trial_type = 2
            if phase >= 2:
                set_trial()
    elif time_count == 480:
        record_data()
        if trial == 10:
            phase_d()
        trial += 1
        if phase == 1:
            bg_grey()
        elif phase == 3:
            bg_white()
            if phase >= 2:
                set_trial()
        else:
            bg_pink()
            trial_type = 1
            if phase >= 2:
                set_trial()
        time_count = 0



def update_clock():
    root.after(1000, update_clock)
    root.after(1000, check_count)
update_clock()


def signal_points():
    global beep
    pygame.mixer.music.play()


def check_points_1(event):
    global phase
    global target_clicks
    global stream
    if phase == 2:
        target_clicks += 1
        stream.append(1)
    if phase == 3:
        target_clicks += 1
        stream.append(1)
    if phase == 4:
        target_clicks += 1
        stream.append(1)


def check_points_2(event):
    global click_pattern
    global points
    global irt_1
    global target_clicks
    global alt_1
    global alt_2
    global pref_alt_1
    global pref_alt_2
    global new_interval_1
    global stream
    if phase == 1:
        target_clicks += 1
        stream.append(1)
        if irt_1 >= new_interval_1:
            points += 10
            signal_points()
            lbl_actual_points.configure(text=points)
            stream.append(9)
            set_interval_1()
            irt_1 = 0
    if phase == 2:
        if trial_type == 1:
            alt_1 += 1
            stream.append(2)
            if irt_1 >= new_interval_1:
                points += 10
                signal_points()
                lbl_actual_points.configure(text=points)
                stream.append(9)
                set_interval_1()
                irt_1 = 0
                move_buttons()
        if trial_type == 2:
            alt_2 += 1
            stream.append(2)
            if irt_1 >= new_interval_1:
                points += 10
                signal_points()
                lbl_actual_points.configure(text=points)
                stream.append(9)
                set_interval_1()
                irt_1 = 0
                move_buttons()
        if trial_type == 3:
            alt_1 += 1
            stream.append(2)
            points += 10
            signal_points()
            lbl_actual_points.configure(text=points)
            stream.append(9)
    if phase == 3:
        if trial_type == 3:
            alt_1 += 1
            pref_alt_1 += 1
            stream.append(2)
            points += 10
            signal_points()
            lbl_actual_points.configure(text=points)
            stream.append(9)
        if trial_type == 4:
            alt_1 += 1
            pref_alt_1 += 1
            stream.append(2)
            points += 10
            signal_points()
            lbl_actual_points.configure(text=points)
            stream.append(9)
        if trial_type == 5:
            alt_2 += 1
            pref_alt_2 += 1
            stream.append(2)
            points += 10
            signal_points()
            lbl_actual_points.configure(text=points)
            stream.append(9)

    if phase == 4:
        if trial_type == 2:
            alt_2 += 1
            stream.append(2)
        elif trial_type == 1:
            alt_1 += 1
            stream.append(2)


def check_points_3(event):
    global click_pattern
    global points
    global trial_type
    global alt_2
    global alt_1
    global pref_alt_1
    global pref_alt_2
    global stream
    if phase == 2:
        if trial_type == 1:
            alt_1 += 1
            stream.append(3)
        if trial_type == 2:
            alt_2 += 1
            stream.append(3)
        if trial_type == 3:
            alt_2 += 1
            stream.append(3)
            points += 10
            signal_points()
            lbl_actual_points.configure(text=points)
            stream.append(9)
    if phase == 3:
        if trial_type == 3:
            alt_2 += 1
            pref_alt_2 += 1
            stream.append(3)
            points += 10
            signal_points()
            lbl_actual_points.configure(text=points)
            stream.append(9)
        if trial_type == 5:
            alt_2 += 1
            stream.append(3)
            points += 10
            signal_points()
            lbl_actual_points.configure(text=points)
            stream.append(9)

    elif phase == 4:
        if trial_type == 2:
            alt_2 += 1
            stream.append(3)
        elif trial_type == 1:
            alt_2 += 1
            stream.append(3)


def check_points_4(event):
    global click_pattern
    global points
    global phase
    global trial_type
    global stream

def add_time(event):
    global time_count
    time_count += 115

def click_start(event):
    global time_count
    fw_stream.write("START")
    fw_stream.write('\n')
    lbl_points.pack(pady=5)
    lbl_actual_points.pack(pady=5)
    btn_start.grid_forget()
    set_interval_1()
    time_count = 0
    phase_b()
    bg_pink()
    set_trial()

top_frame = Frame(root)
top_frame.pack()
top_frame.configure(bg="gray")

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)
bottom_frame.configure(bg="gray")

middle_frame = Frame(root)
middle_frame.pack(side=BOTTOM)
middle_frame.configure(bg="gray")

btn_start = Button(middle_frame, text="START", font=("Ariel", 16), bg="gray")
btn_start.bind("<Button-1>", click_start)
btn_start.configure(highlightbackground=bg_clr)
btn_start.grid(row=0, column=7, padx=350)

lbl_points = Label(top_frame, text="Points:", font=("Ariel", 16), bg="gray")
lbl_actual_points = Label(top_frame, text=points, font=("Ariel", 40), bg="white", height=2, width=6)

photo1 = PhotoImage(file="green_symbol.png")
photo2 = PhotoImage(file="red_maze.png")
photo3 = PhotoImage(file="power_button.PNG")
photo4 = PhotoImage(file="magenta_btn.gif")
photo5 = PhotoImage(file="brown_btn.gif")
photo6 = PhotoImage(file="indigo_btn.gif")
photo7 = PhotoImage(file="purple_btn.gif")
photo8 = PhotoImage(file="yellow_btn.gif")
photo9 = PhotoImage(file="pink_btn.gif")
photo10 = PhotoImage(file="teal_btn.gif")
photo11 = PhotoImage(file="maroon_btn.gif")

button_1 = Button(middle_frame, image=photo1, cursor="hand2")
button_1.bind("<Button-1>", check_points_1)

button_2 = Button(middle_frame, image=photo2, cursor="hand2")
button_2.bind("<Button-1>", check_points_2)

button_3 = Button(middle_frame, image=photo3, cursor="hand2")
button_3.bind("<Button-1>", check_points_3)

button_4: Button = Button(middle_frame, image=photo4, cursor="hand2")
button_4.bind("<Button-1>", check_points_4)



'''
button_skip = Button(middle_frame, height=10, width=10, relief=RAISED, cursor="hand2")
button_skip.grid(row=3, column=1)
button_skip.bind("<Button-1>", add_time)
'''

lbl_end = Label(middle_frame, text="Thank you for participating!", font=("Ariel", 16), bg="pink")
lbl_end2 = Label(middle_frame, text="Let the experimenter know you are finished.", font=("Ariel", 16), bg="pink")

buffer = Label(bottom_frame, text=" ", bg="gray")
buffer.grid(row=1, column=0, pady=175)

root.mainloop()
