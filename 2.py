def change_case(input_string):
    result = ""
    for char in input_string:
        if "a" <= char <= "z":
            result += chr(ord(char) - 32)
        elif "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        elif "а" <= char <= "я":
            result += chr(ord(char) - 32)
        elif "А" <= char <= "Я":
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

string_input = input("Введите строку: ")
processed_string = change_case(string_input)
print("Результат:", processed_string)
