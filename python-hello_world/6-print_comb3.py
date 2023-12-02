for two_digit in range(10):
    for single_digit in range(two_digit + 1, 10):
        if single_digit == 9 and two_digit == 8:
            # print("{}{}".format(two_digit, single_digit), end=' ')
            print(f"{two_digit}{single_digit}", end= '')
        else:
            print("{}{},".format(two_digit, single_digit), end=' ')
            
        # print(f"{two_digit}{single_digit}," , end=' ')

