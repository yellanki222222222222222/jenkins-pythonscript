import datetime

def get_current_time():
    """A function to return the current date and time."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    print(f"Current time is: {get_current_time()}")
