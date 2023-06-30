def print_sum_of_charcacter(number):
    if int(number) < 10:
        return int(number)
    elif int(number) >= 10:
        return int(number[0]) + print_sum_of_charcacter(number[1:])


n = input()
answer = print_sum_of_charcacter(n)
print(answer)
