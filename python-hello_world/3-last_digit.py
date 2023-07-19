import random

def last_digit_info(number):
    last_digit = abs(number) % 10

    if last_digit > 5:
        return "Last digit of {} is {} and is greater than 5".format(number, last_digit)
    elif last_digit == 0:
        return "Last digit of {} is {} and is 0".format(number, last_digit)
    else:
        return "Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit)

number = random.randint(-10000, 10000)
print(last_digit_info(number))
