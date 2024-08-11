import datetime

def get_greeting(hour):
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"

def main():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    # Display the time
    print(f"Current time: {hour:02}:{minute:02}:{second:02}")

    # Display the appropriate greeting
    print(get_greeting(hour))

if __name__ == "__main__":
    main()




     
     

 