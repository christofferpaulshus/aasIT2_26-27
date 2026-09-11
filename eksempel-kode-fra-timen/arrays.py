import array as arr

numbers = arr.array('i', [10, 20, 30, 40])

print(numbers[2])

numbers.insert(1, 15)
print(numbers)

numbers.pop(1)
print(numbers)

print(numbers.index(30))

print(type(list(numbers)))

partall = [tall + 2 for tall in range(20) if not tall % 2]
print(partall)