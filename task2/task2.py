FILE_NAME = "text_2_var_29"

with open(FILE_NAME) as file:
    lines = file.readlines()

avg_lines = list()

for line in lines:
    nums = line.split(":")
    sum_line = 0
    
    for num in nums:
        sum_line += int(num)

    if len(nums) > 0:
        avg_lines.append(sum_line / len(nums))

with open('r_text_2.txt', 'w') as result:
    for value in avg_lines:
        result.write(str(value) + "\n")