# -----------------------------------------------------------
# Temperature Monitoring System
# Name: Rajat Gupta
# Roll No: 202501100700114
# Branch: ECE-B
# -----------------------------------------------------------

# Import required modules
from random import uniform as temp
import time


# Take minimum and maximum temperature limits from user
min_temp, max_temp = map(
    int,
    input("Enter the min and max limits of temperature respectively: ").split()
)

time.sleep(0.5)
print("-------------------------------")


# Continuous monitoring loop
while True:
    print("Acquiring the temperature value...")
    time.sleep(1)

    # Generate random temperature between 0 and 100
    temperature = round(temp(0, 100), 2)

    print("Temperature Acquired:", temperature)
    time.sleep(1)

    # Check temperature conditions
    if temperature > max_temp:
        message = "Alert: Temperature is too high"

    elif temperature > min_temp:
        message = "Temperature is within acceptable limit"

    else:
        message = "Alert: Temperature is too low"

    # Print message character by character (animation effect)
    for char in message:
        print(char, end="")
        time.sleep(0.05)

    print("\n-------------------------------")

    # Wait before next reading
    time.sleep(2)
