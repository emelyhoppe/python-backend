
from payament_times.in_time import *
from payament_times.nine_months import *
from payament_times.six_months import *
from payament_times.three_months import *
from payament_times.twelve_months import *


def credit_payament(desired_car, time_option):
    if(time_option == 1):
        return (in_time(desired_car))
    elif(time_option == 2):
        return (three_months(desired_car))
    elif(time_option == 3):
        return (six_months(desired_car))
    elif(time_option == 4):
        return (nine_months(desired_car))
    elif(time_option == 5):
        return (twelve_months(desired_car))