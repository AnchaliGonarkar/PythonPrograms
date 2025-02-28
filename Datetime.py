from datetime import datetime

def print_current_date_time():
    now = datetime.now()
    current_date = now.date()
    current_time = now.time()

    print(f"Today's date is: {current_date}")
    print(f"The current time is: {current_time}")

# Main program
if __name__ == "__main__":
    print_current_date_time()
