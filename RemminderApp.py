from plyer import notification
import time

def sleep_reminder():
    # Set the title and message for the notification
    title = "Sleep Reminder"
    message = "A good night's rest is important for your brain,mental health and Backache"
    app_icon = "C:\\Users\\ASUS\\PycharmProjects\\pythonProject1\\reminderapp\\sleepoico.ico"
    # Show the notification
    notification.notify(
        title=title,
        message=message,
        app_name="Sleep Reminder App",
        app_icon = app_icon,
        timeout=10  # The notification will disappear after 10 seconds
    )

if __name__ == "__main__":
    # Set the time for the reminder (in seconds)
    reminder_time = 3600 # 1 hour (you can adjust this as needed)

    while True:
        # Call the sleep reminder function
        sleep_reminder()

        # Wait for the next reminder
        time.sleep(reminder_time)


