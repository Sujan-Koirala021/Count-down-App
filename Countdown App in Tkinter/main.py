"""
Sujan Koirala, Institute of Engineering, Pulchowk

# Stopwatch"""

from tkinter import *
import time
import sys

root = Tk()
root.title('Stopwatch')

hour, minute, second = 0, 0, 0
to_stop = False

# Function to run when start button in pressed


def start():
    startButton['state'] = DISABLED  # Disabling button after pressing it
    global hour, minute, second, to_stop, str_hour, str_minute, str_second
    second += 1
    if (second == 60):
        minute += 1
        second = 0
    if (minute == 60):
        hour += 1
        minute = 0
    if hour >= 0 and hour <= 9:
        str_hour = f'0{hour}'
    else:
        str_hour = str(hour)

    if minute >= 0 and minute <= 9:
        str_minute = f'0{minute}'
    else:
        str_minute = str(minute)

    if second >= 0 and second <= 9:
        str_second = f'0{second}'
    else:
        str_second = str(second)

    myLabel.config(text=f'{str_hour}:{str_minute}:{str_second}')
    if to_stop:
        return
    else:
        myLabel.after(1000, start)


# Function to run when stop button in pressed
def stop():
    global to_stop
    to_stop = True
    myLabel.config(text=f'{str_hour}:{str_minute}:{str_second}')


# Display Label
myLabel = Label(text='00:00:00',  font=(
    'Helvetica', 42), bg="black", fg="green")
myLabel.pack(padx=10, pady=20)

# Start Button
startButton = Button(text="Start", command=start)
startButton.pack(pady=10)

# Stop Button
stopButton = Button(text='Stop', command=stop)
stopButton.pack(pady=10)


root.mainloop()
