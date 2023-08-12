def first_last_digit(number):
  return (number // 10**len(str(number)) % 10, number % 10)

if __name__ == "__main__":
  print(first_last_digit(98742))
  print(first_last_digit(-1234))
