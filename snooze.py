
import tkinter as tk
from tkinter import messagebox
from time import strftime, localtime
import time

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x300")

# Digital clock display
clock = tk.Label(root, font=("Arial", 40), padx=20, pady=10)
clock.pack()

# Alarm input
tk.Label(root, text="Set Alarm (HH:MM:SS)",
         font=("Arial", 12)).pack(pady=5)

alarm_entry = tk.Entry(root, font=("Arial", 14), justify="center")
alarm_entry.pack()

alarm_status = tk.Label(root, text="No alarm set",
                        font=("Arial", 11))
alarm_status.pack(pady=5)

alarm_time = None
alarm_triggered = False
snooze_job = None


# Update the digital clock
def update_clock():
    clock.config(text=strftime("%H:%M:%S"))
    check_alarm()
    root.after(1000, update_clock)


# Set the alarm
def set_alarm():
    global alarm_time, alarm_triggered

    entered_time = alarm_entry.get().strip()

    try:
        time.strptime(entered_time, "%H:%M:%S")
    except ValueError:
        messagebox.showerror(
            "Invalid Time",
            "Enter alarm time in HH:MM:SS format."
        )
        return

    alarm_time = entered_time
    alarm_triggered = False

    alarm_status.config(text=f"Alarm set for {alarm_time}")


# Check whether the alarm time has arrived
def check_alarm():
    global alarm_triggered

    current_time = strftime("%H:%M:%S")

    if alarm_time == current_time and not alarm_triggered:
        alarm_triggered = True
        ring_alarm()


# Show alarm popup with snooze option
def ring_alarm():
    global snooze_job

    popup = tk.Toplevel(root)
    popup.title("Alarm Ringing!")
    popup.geometry("300x160")
    popup.transient(root)
    popup.grab_set()

    tk.Label(
        popup,
        text="⏰ ALARM!",
        font=("Arial", 22, "bold")
    ).pack(pady=15)

    def snooze():
        global snooze_job

        popup.destroy()
        alarm_status.config(text="Snoozed for 5 minutes")
        snooze_job = root.after(5 * 60 * 1000, ring_alarm)

    def dismiss():
        global alarm_time, snooze_job

        if snooze_job is not None:
            root.after_cancel(snooze_job)
            snooze_job = None

        alarm_time = None
        alarm_status.config(text="No alarm set")
        popup.destroy()

    buttons = tk.Frame(popup)
    buttons.pack(pady=10)

    tk.Button(
        buttons, text="Snooze 5 min",
        command=snooze
    ).pack(side="left", padx=5)

    tk.Button(
        buttons, text="Dismiss",
        command=dismiss
    ).pack(side="left", padx=5)


# Set alarm button
tk.Button(
    root,
    text="Set Alarm",
    font=("Arial", 12),
    command=set_alarm
).pack(pady=10)

update_clock()
root.mainloop()
