# Реализация 1
ticket_num = input()
sum_first = int(ticket_num[0] + ticket_num[1] + ticket_num[2])
sum_last = int(ticket_num[3] + ticket_num[4] + ticket_num[5])

print = (f"The ticket is lucky: {sum_first == sum_last}")

ticket_number = int(input)


# Реализация 2
sum_first = 0
sum_last = 0

while ticket_number:
    digit = ticket_number % 10
    if ticket_number > 999:
        sum_first += digit
    else:
        sum_last += digit
    ticket_number //= 10

print = (f"The ticket is lucky: {sum_first == sum_last}")