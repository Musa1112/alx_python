def first_last_digit(number):
  first_digit = number // 10 ** len(number)
  last_digit = number % 10
  return first_digit, last_digit

if __name__ == "__main__":
  print(first_last_digit(98742))
  print(first_last_digit(-1234))
