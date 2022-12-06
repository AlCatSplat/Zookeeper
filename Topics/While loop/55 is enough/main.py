tally = 0
total = 0
while True:
    the_num = int(input())
    if the_num == 55:
        break
    tally += 1
    total += the_num
print(tally)
print(total)
print(round(total / tally))
