import sys
import time 
import tkinter as tk

####* Global Variables 
user_quit = False


####* Create a GUI with a label (timer) and 2 buttons (start and stop/reset)

###* Global Variables for GUI
timer_started = False # flag if timer has been started or stopped by the user
now = 0 # int for timer at each tick
prev_time = 0 # int for reference to last "now"
running_time = 0 # int for sum of running time
saved_times_array = []



###* Create window
window = tk.Tk()
# window.geometry("450x300")

###* Create label

frame = tk.Frame( master=window )
frame.grid(row=0 , column=0,columnspan=3)



## Initalize label on GUI
timer_label = tk.Label(frame, font = ('calibri',40, 'bold'), background = '#231942',foreground = '#e0b1cb',width=11,text="Time: 0:00:0.000") 
timer_label.pack()

###* Create button 1

## Create a function for the stop button press  
def stop_btn_pressed():

    global timer_started

    timer_started=False

    start_btn.config(command=start_btn_pressed,text="Start")
    print(timer_started)

## Create a function for the start button press
def start_btn_pressed():

    global timer_started

    timer_started=True
    start_btn.config(command=stop_btn_pressed,text="Stop")
    print(timer_started)
    


frame = tk.Frame(
            master=window,
            borderwidth=2,
            background="#231942"
        )
frame.grid(row=1 , column=0)
start_btn = tk.Button(master=frame , text="Start" , command=start_btn_pressed, background="#231942")
start_btn.pack()

###* Create button 2 


## Create function for reset button pressed 
def reset_btn_pressed():
    
    global timer_started
    global running_time
    
    if timer_started: # Resets Start button if timer is reset while on 
        stop_btn_pressed()

    running_time = 0 # Reset running time
    time_elapsed_string = "Time: {:<.3f}".format(running_time) # Format label string
    timer_label.config(text=time_elapsed_string)
    


    

frame = tk.Frame(
            master=window,
            borderwidth=2,
            background="#231942"
        )
frame.grid(row=1 , column=2)
reset_btn = tk.Button(master=frame, text='Reset', command=reset_btn_pressed,background="#231942")
reset_btn.pack()

###* Create button 3

def store_btn_pressed():
    global saved_times_array
    
    temp = running_time
    saved_times_array.append(temp)
    sum_of_times_lbl.config(text="{:<.3f}s".format(max(0,sum(saved_times_array))))


    times_list.insert(0,"{:<.3f}s".format(temp))
    
    reset_btn_pressed()

frame = tk.Frame(
            master=window,
            borderwidth=2,
            background="#231942"
        )
frame.grid(row=1,column=1)
store_btn = tk.Button(master=frame,text="Store", command=store_btn_pressed)
store_btn.pack()

###* List of times Label

frame = tk.Frame(
    master = window,
)

frame.grid(row=0, column=3,rowspan=2)
times_list = tk.Listbox(frame, font = ('calibri',40, 'bold'),foreground = '#fff',width=11) 
times_list.pack()

###* Sum of times label

frame = tk.Frame(
    master=window 
)
frame.grid(row=1,column=3)
# test = sum(times_list)
sum_of_times_lbl = tk.Label(frame, font = ('calibri',40, 'bold'), background = '#231942',foreground = '#e0b1cb',width=11,text=max(0,sum(saved_times_array))) 
sum_of_times_lbl.pack()

####* Util Functions

## Create a function that updates the timer_label recursively after a set timeß
def movTime():
    global prev_time
    global now
    global running_time

    now = time.time() # Starts a timer each tick 

    print("Time {} ; Timer start flag {}".format(running_time,timer_started))
    
    if timer_started == True:
        
        running_time += (now - prev_time) # 
        hrs = running_time/3600 # 
        hrs_mod = hrs - int(hrs) # 
        mins = hrs_mod * 60 # 
        mins_mod = mins - int(mins) 
        secs = mins_mod * 60 

        print("hrs {}, hR {}, mins {} , mR {} , secs {:<.3f} ".format(hrs,hrs_mod,mins,mins_mod,secs))
        # TODO: Format time to have minutes and hours
        time_elapsed_string = "Time: {}:{:02}:{:<.3f}".format(int(hrs),int(mins),secs) # Format label string
        timer_label.config(text=time_elapsed_string) #Update timer_label 
        
    prev_time = now # Reference to previous timer for math 
    time.sleep(1*10**-8) # Wait one nanosecond
   
## Create a function to close the program
def on_close():
    global user_quit 
    user_quit = True


####* Main function

def main():
    
    window.protocol("WM_DELETE_WINDOW", on_close) # handles for close button pressed event

    while True:
        print("arr of times {} , sum: {}".format(saved_times_array,sum(saved_times_array)))
        movTime()
        if user_quit:
            
            sys.exit()
            # quit()

        window.update()
        window.update_idletasks()
            
            


if __name__ == "__main__":
    main()


