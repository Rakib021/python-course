def splitBalancedString(S):
    num_strings = 0
    balanced_strings = []
    current_string = ""

    for char in S:
        current_string += char

        if char == 'R':
            if current_string.count('L') == current_string.count('R'):
                balanced_strings.append(current_string)
                num_strings += 1
                current_string = ""

    print(num_strings)
    for string in balanced_strings:
        print(string)
S = input().strip()
splitBalancedString(S)
