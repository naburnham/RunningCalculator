"""
Running Calculator

Calculates pace for miles and pace for kilometers
Converts mile pace to km pace and visa versa

Estimates Calories burned
Estimates VO2 max
"""

# Running MET table, key = minutes/mile, value = MET score
from collections import OrderedDict
import sys

running_met_table = {
    13: 6.0,
    12: 8.3,
    11.5: 9.0,
    10: 9.8,
    9: 10.5,
    8.5: 11.0,
    8: 11.5,
    7.5: 11.8,
    7: 12.3,
    6.5: 12.8,
    6: 14.5,
    5.5: 16,
    5: 19,
    4.6: 19.8,
    4.3: 23
}

# Standard Conversion Rates
KG_CONVERSION = 0.45356237


def find_met_score(mile_pace):
    if mile_pace > 12.5:
        return running_met_table[13]
    elif mile_pace > 11.5:
        return running_met_table[12]
    elif mile_pace > 10:
        return running_met_table[11.5]
    elif mile_pace > 9.5:
        return running_met_table[10]
    elif mile_pace > 8.5:
        return running_met_table[9.5]
    elif mile_pace > 8:
        return running_met_table[8.5]
    elif mile_pace > 7.5:
        return running_met_table[8]
    elif mile_pace > 7:
        return running_met_table[7.5]
    else:
        print("FINISH MET TABLE FUNCTION")
        print("FIXME: Find a simpler implementation that if/elif")
        return running_met_table[7]


def pounds_to_kg(weight_in_lbs):
    """ Returns weight(lbs) in kgs. """
    return weight_in_lbs * KG_CONVERSION


def convert_time_to_hours(time):
    time_list = time.split(':')

    hours = time_list[0]
    minutes = time_list[1]
    seconds = time_list[2]

    time_in_hours = int(hours) + (int(minutes) / 60) + (int(seconds) / 60 / 60)
    return time_in_hours


def pace_per_mile(time, miles):
    return time / miles


def calories_burned():
    """
    Returns the calories burned depending on age, pace per mile, and total time exercising
    using the formula kCal = MET * Weight(kg) * timePerformingHours
    """
    weight_in_lbs = float(input('Weight in Pounds: '))
    miles_ran = float(input('Total miles run: '))
    time = input('Total time (HH:MM:SS): ')

    time_in_hours = convert_time_to_hours(time)
    weight_in_kg = pounds_to_kg(weight_in_lbs)

    mile_pace = pace_per_mile(time_in_hours, miles_ran) * 60

    met = find_met_score(mile_pace)

    return 'Calories burned is: {}'.format(met * weight_in_kg * time_in_hours)


def vo2max():
    """
    Returns estimated VO2 max for men using walk_time for one mile, age, weight (in lbs), and ending heart rate.
    """
    walk_time = input('One mile walk time (MM:SS): ')
    age = int(input('Age (in years): '))
    weight = float(input('Weight (in lbs): '))
    heart_rate = int(input('Heart Rate (beats per minute): '))

    time_in_minutes = convert_time_to_hours('00:' + walk_time) * 60

    return "Estimated VO2 max is: {}".format(
        132.853 - (0.0769 * weight) - (.3877 * age) + 6.3150 - (3.2649 * time_in_minutes) - (0.1565 * heart_rate))


def main_loop():
    menu = OrderedDict({
        '\np': 'Pace per mile',
        'c': 'Calories Burned',
        'v': 'Estimated VO2 max',
        'q': 'Quit'
    })

    for menu_option, command in menu.items():
        print("{}: {}".format(menu_option, command))

    user_choice = input('Choose an option: ').strip()

    if user_choice.lower() == 'q':
        sys.exit('FIXME: CLEAN CODE, ERROR HANDLING, TESTING')
    elif user_choice.lower() == 'p':
        time = input('Total time (HH:MM:SS): ')
        miles = float(input('Total miles: '))
        time_in_hours = convert_time_to_hours(time)
        print('Pace per mile in minutes and hundredths: {}'.format(pace_per_mile(time_in_hours * 60, miles)))
    elif user_choice.lower() == 'c':
        print(calories_burned())
    elif user_choice.lower() == 'v':
        print(vo2max())


if __name__ == "__main__":
    while True:
        main_loop()
