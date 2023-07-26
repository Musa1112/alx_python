def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
# Test the function with a = 10 and b = 2
result = safe_print_division(10, 2)


