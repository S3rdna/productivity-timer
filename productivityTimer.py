import sys
import time 
import tkinter as tk

#### Global Variables 
user_quit = False


#### Create a GUI with a label (timer) and 2 buttons (start and stop/reset)

### Global Variables for GUI
timer_started = False # tracking if timer has been started or stopped by the user
time_at_start_press = 0 # Initalizing start variable (tracking time at button press)
time_at_pause_press = 0
first_time = True
delta_time = 0
delta_pause_time = 0



### Create window
window = tk.Tk()
# window.geometry("450x300")

### Create label

frame = tk.Frame( master=window )
frame.grid(row=0 , column=0,columnspan=3)

## Create a function that updates the timer_label recursively after a set time
# FIXME: Fix format of displayed time on label

def movTime():
    global time_at_start_press
    global time_at_pause_press
    global delta_time
    global delta_pause_time

    # FIXME: Fix running time (time when paused is being added to delta time)
    print()
    if timer_started == True:
        now = time.monotonic_ns() # Time saved at each update
        delta_time = (now - time_at_start_press)/10**8
        time_elapsed_string = "Time: {:<.3f}".format(delta_time)
        timer_label.config(text=time_elapsed_string)
    else:
        now = time.monotonic_ns()
        delta_pause_time = (now - time_at_pause_press - delta_pause_time)/10**8
    timer_label.after(10,movTime) #(wait time in miliseconds,function)
   

timer_label = tk.Label(frame, font = ('calibri',40, 'bold'), background = 'pink',foreground = 'white',width=11,text="Time 0.000")
timer_label.pack()

### Create button 1

## Create a function for the stop button press  
def stop_btn_pressed():

    global timer_started
    global time_at_pause_press

    timer_started=False
    time_at_pause_press = time.monotonic_ns()

    start_btn.config(command=start_btn_pressed,text="Start")
    print(timer_started)

## Create a function for the start button press
def start_btn_pressed():

    global timer_started
    global time_at_start_press
    global first_time

    if first_time:
        time_at_start_press = time.monotonic_ns()
        timer_started=True
        first_time = False
        start_btn.config(command=stop_btn_pressed,text="Stop")
        print(timer_started)
    else:
        timer_started=True
        start_btn.config(command=stop_btn_pressed,text="Stop")
        print(timer_started)
    


frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=2,
        )
frame.grid(row=1 , column=0)
start_btn = tk.Button(master=frame , text="Start" , command=start_btn_pressed)
start_btn.pack()

### Create button 2 


## Create function for reset button pressed 
def reset_btn_pressed():
    
    global time_at_start_press 
    

frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=2,
        )
frame.grid(row=1 , column=2)
reset_btn = tk.Button(master=frame, text='Reset', command=reset_btn_pressed)
reset_btn.pack()


## Create a function to close the program
def on_close():
    global user_quit 
    user_quit = True


#### Main function

def main():
    
    window.protocol("WM_DELETE_WINDOW", on_close) # handles for close button pressed event
    movTime()

    while True:

        if user_quit:
            sys.exit()
            break
        else:            
            window.update()
            window.update_idletasks()
            
            


if __name__ == "__main__":
    main()


