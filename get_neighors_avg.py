# До того, как посмотрел лекцию, написал эту ф-ю для вычисления среднего при значении NA. Обрабатывая и граничные, и соседние случаи
def get_neighboring_avg(nums: list, index: int):
    left_neighbors = list()
    right_neighbors = list()
    left_index = index
    right_index = index

    while left_index > 0:
        left_index -= 1
        if nums[left_index] == "NA":
            continue
        else:
            left_neighbors.append(int(nums[left_index]))
            if len(left_neighbors) == 2:
                break

    while right_index < len(nums) - 2:
        right_index += 1
        if nums[right_index] == "NA":
            continue
        else:
            right_neighbors.append(int(nums[right_index]))
            if len(right_neighbors) == 2:
                break

    if len(left_neighbors) > 0 and len(right_neighbors) > 0:
        return (left_neighbors[0] + right_neighbors[0]) / 2
    elif len(left_neighbors) == 0:
        return sum(right_neighbors) / len(right_neighbors)
    elif len(right_neighbors) == 0:
        return sum(left_neighbors) / len(left_neighbors)
    
    return 0