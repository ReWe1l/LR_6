def remove_duplicates_and_spaces(input_string):
    result = ""
    for char in input_string:
        is_duplicate = False
        if char != " ":
            for i in range(len(result)):
                if char == result[i]:
                    is_duplicate = True
                    break
            if not is_duplicate:
                result += char
    return result

string_input = input("Введите строку: ")
processed_string = remove_duplicates_and_spaces(string_input)
print("Результат:", processed_string)