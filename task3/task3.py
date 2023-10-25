import math

FILE_NAME = "text_3_var_29"

with open(FILE_NAME) as file:
    lines = file.readlines()

matrix = list()

for line in lines:
    nums = line.strip().split(",")
    for i in range(len(nums)):
        if nums[i] == "NA":
            nums[i] = str((int(nums[i-1])+int(nums[i+1])) / 2)
    
    filtered = list()
    for item in nums:
        num = float(item)
        if math.sqrt(num) < 50 + 29:
            filtered.append(num)

    matrix.append(filtered)

with open('r_text_3.txt', 'w') as result:
    for row in matrix:
        for num in row:
            result.write(str(num) + ',')
        result.write("\n")