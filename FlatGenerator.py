def flat_generator(nested_list):
    cursor = 0
    iter1 = 0
    iter2 = 0
    while True:
        if cursor < len(nested_list[iter1]):
            yield nested_list[iter1][iter2]
            iter2 += 1
            cursor += 1
        else:
            iter1 += 1
            if iter1 == len(nested_list):
                break
            cursor = 0
            iter2 = 0

