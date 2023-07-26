import sys

if __name__ == "__main__":
    n = len(sys.argv) - 1
    s = "s" if n != 1 else ""
    print(f"{n} argument{s}: {', '.join(f'{i}: {arg}' for i, arg in enumerate(sys.argv[1:], 1))}." if n else "No arguments.")
