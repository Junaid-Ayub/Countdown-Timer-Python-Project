import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # \r prints over the same line
        time.sleep(1)
        t -= 1

    print("Time's up!")


# Get user input for the countdown time
seconds = input("Enter the time in seconds: ")

try:
    seconds = int(seconds)
    countdown(seconds)
except ValueError:
    print("Please enter a valid number.")