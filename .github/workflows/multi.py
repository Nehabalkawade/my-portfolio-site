numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Lowest number:", min(numbers))
print("Highest number:", max(numbers))
print("Average:", sum(numbers) / len(numbers))
