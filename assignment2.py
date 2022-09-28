# reference
# links visted to gather info
# https://www.powerpacing.run/dew-point/
# https://iridl.ldeo.columbia.edu/dochelp/QA/Basic/dewpoint.html

import random
from playsound import playsound

while True:
    # generating temperature values
    temperature = random.uniform(-25, 45)

    # generating relative humidity values
    humidity = random.uniform(0, 100)

    # calculating the dew point temperature
    dew_point = temperature - ((100 - humidity)/5)

    if dew_point < 16:
        print("The weather is comfortable!")

    elif dew_point < 18 and dew_point >= 16:
        print("The weather is slightly uncomfortable")

    else:
        print("The weather is extremely uncomfortable")
        playsound('/Users/macbook/Desktop/IBM Project/Assignment 2/alarm.wav')
