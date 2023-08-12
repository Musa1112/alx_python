def last_digit(number):
  if number < 0:
    number = number * -1
  last_digit = number % 10
  return last_digit

if __name__ == "__main__":
  print(last_digit(98742))
  print(last_digit(-1234))
