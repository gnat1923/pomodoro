import time
import datetime

def main():
    focus_length, break_length, cycles = pomo_config()
    timer(focus_length, break_length, cycles)  
    print("Focus time complete! Enjoy a longer break :)")
    
    
    # Resume focus - after break has elapsed, notify user that focus time has begun, start new timer
    # Repeat for specified amount of periods - use a while loop

def pomo_config():
    focus_length = 25
    break_length = 5
    cycles = 4
    
    while True:
        # Ask default or custom configuration?
        default_config = str(input("Run default pomodoro configuration? Y/N: ")).lower()
            
        if default_config == "y":
            print("You have selected default configuration \n")
            return focus_length, break_length, cycles

        elif default_config == "n":
            print("You have selected custom configuration \n")
            # Custom - define focus time length, break time length, no. of cycles
            while True:
                try:
                    focus_length = int(input("Desired length of focus block (minutes): "))
                    break_length = int(input("Desired length of break block (minutes): "))
                    cycles = int(input("Desired Number of cycles: "))
                    break

                except:
                    print("Error. Values must be a whole number \n")
                    pass

            return focus_length, break_length, cycles

        else:
            print("Invalid response")    
            pass

def timer(focus_length, break_length, cycles):
    # Start - timer runs for length of focus time
    total_focus_seconds = focus_length * 60
    total_break_seconds = break_length * 60
    cycle_count = 1

    # Resume focus - after break has elapsed, notify user that focus time has begun, start new timer
    # Repeat for specified amount of periods - use a while loop
    while cycle_count <= cycles - 1:
        # Start - timer runs for length of focus time
        focus_start_time = time.ctime()
        print(f"\nFocus block {cycle_count} of {cycles} starting now! ({focus_start_time})")
        focus_seconds = total_focus_seconds

        while focus_seconds > 0:
            timer = datetime.timedelta(seconds = focus_seconds)
            print(timer, end="\r")
            time.sleep(1)
            focus_seconds -= 1 

        # Break - when focus time has elapsed, notify user, start new timer for break
        break_start_time = time.ctime()
        print(f"Take a break! ({break_start_time})")
        break_seconds = total_break_seconds

        while break_seconds > 0:
            timer = datetime.timedelta(seconds = break_seconds)
            print(timer, end="\r")
            time.sleep(1)
            break_seconds -= 1 

        cycle_count += 1

    # Final focus time (separate, so no final break)
    focus_start_time = time.ctime()
    print(f"\nFocus block {cycle_count} of {cycles} starting now! ({focus_start_time})")
    focus_seconds = total_focus_seconds

    while focus_seconds > 0:
        timer = datetime.timedelta(seconds = focus_seconds)
        print(timer, end="\r")
        time.sleep(1)
        focus_seconds -= 1 

if __name__ == "__main__":
    main()
