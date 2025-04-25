input_array = [1, 2, 3, 4, 5]

# 1. New array containing products
output_array = []

# 2. Loop over input array
for i in input_array:

    # 3. For each item, create a new array excluding the current item
    current_items = input_array
    del current_items[i]

    # 4. Loop over the new array and multiply all the items together
    product = 0
    j = 0
    while j < len(current_items):
        if j == 0:
            product = current_items[j]
            continue

        product = product * current_items[j]

    # 5. Add the result to a new output array
    output_array.append(product)

print(output_array)
