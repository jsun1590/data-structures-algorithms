def search(target_list, target_val):
    lower = 0
    upper = len(target_list) 
    while lower <= upper:
        avg = (lower + upper) // 2

        if target_val > target_list[avg]:
            lower = avg + 1
        elif target_val < target_list[avg]:
            upper = avg - 1
        else:
            break
    return avg if target_val == target_list[avg] else -1