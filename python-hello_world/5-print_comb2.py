for number in range (100):
    if number < 99:
        # print("{:02}, ".format (number), end=' ')
        print(f"{number:02},", end=' ')
    else:
        # print("{:02}" .format(number))
        print(f"{number:02}", end =' ')