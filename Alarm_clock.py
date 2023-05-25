from tkinter import *
import datetime
import time
import winsound
from threading import Thread

root = Tk()
root.geometry("400x200")

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        if current_time == set_alarm_time:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break  # Add break statement to exit the loop

Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica", 15, "bold")).pack()

frame = Frame(root)
frame.pack()

hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour = StringVar(root)
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minutes = tuple("{:02d}".format(i) for i in range(61))
minute = StringVar(root)
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

seconds = tuple("{:02d}".format(i) for i in range(61))
second = StringVar(root)
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica", 15), command=Threading).pack(pady=20)

root.mainloop()