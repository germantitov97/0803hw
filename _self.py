number = 10,
print(number)

numbers = 10, 20, 30
print(numbers)

fruits = "apple", "banana", "orange"
print(fruits)

scores = (100, 95, 87)
# scores.sort()  # ERROR
print(tuple(sorted(scores)))

person = "Alice", 25, "Teacher"
print(person)

animals = "dog", "cat", "lion"
animals = ("dog", "cat", "lion")

print(animals[0])
print(animals[1])

a=1
b=2
a, b = b, a
print(a, b)

colors = ("red", "green", "blue", "yellow")
print(colors[-1])
print(colors[::1])
print(colors[::-1])
print(colors[::2])

flags = (False, False, True)
print(any(flags))
numbers = (1, 7, 5, 11, 3, 6, -1)
print(any(x % 2 == 0 for x in numbers))
print(all(x % 2 == 0 for x in numbers))
print(all(len(color) >= 3 for color in colors))
print(len(colors))

cars = ("Tesla", "Tesla", "Mitsubishi", "Honda")
print(len(cars))

animals = ("dog", "cat", "lion")
for animal in animals:
    print(animal)
for i in range(len(animals)):
    print(animals[i])
print(len(animals[2]))