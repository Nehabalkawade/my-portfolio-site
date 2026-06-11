numbers = [12, 45, 7, 89, 23, 56,5,7,4,2,8,2,8,32,42,3,7,4,1,14]

lowest = numbers[0]
highest = numbers[0]
total = 0

for num in numbers:
    if num < lowest:
        lowest = num

    if num > highest:
        highest = num

    total = total + num

average = total / len(numbers)

print("Numbers:", numbers)
print("Lowest number:", lowest)
print("Highest number:", highest)
print("Average:", average)
