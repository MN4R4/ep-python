def remove_duplicates(numbers):
    new_list = []
    for x in range(len(numbers)):
        if numbers[x] not in new_list:
            new_list.append(numbers[x])
    return new_list    
print remove_duplicates([1,2,3,1,2,5,6])
