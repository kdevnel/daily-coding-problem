numbers_to_check = [10,15,3,7]
k = 17
count = 0;
result = "false"

# get the first number to check
for x in numbers_to_check:
    # get the second number to check
    for y in numbers_to_check:
        # Optimisation: skip this check if the second number is the same index as the first
        if numbers_to_check.index(y) == count:
            continue

        if x + y == k:
            result = "true"
            break
    count += 1
    # Optimisation: if the result is true, break the loop
    if result == "true":
        break

print(result)