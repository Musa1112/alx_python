combinations = ""

for i in range(10):
    for j in range(i + 1, 10):
        combinations += "{:d}{:d}, ".format(i, j)

# Remove the trailing comma and space
combinations = combinations.rstrip(", ")

print(combinations)
