list_number = [111,13, 14, 15]

def unique_numbers(numbers):
    new_list = []
    for number in numbers:
        while str(number)[0] == str(number)[1]:
            number *= 2

        new_list.append(number)
    return new_list
        
    
result = unique_numbers(list_number)

print(result)
