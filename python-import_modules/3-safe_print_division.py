def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

# Test the function with a = 12 and b = 0
a = 12
b = 0
result = safe_print_division(a, b)
