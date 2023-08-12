import random

def last_digit(number):
  number = random.randint(-10000, 10000)
  last_digit = number % 10
  if number < 0:
    last_digit = -last_digit
  if last_digit > 5:
    return (f"Last digit of {number} is {last_digit} and is greater than 5")
  elif last_digit == 0:
    return (f"Last digit of {number} is {last_digit} and is 0")
  else:
    return(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

if __name__ == "__main__":
  number = random.randint(-10000, 10000)
  print(last_digit(number))
