
lucky_numbers = [4, 8, 15, 16, 23, 42, 18]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Tom"]
friends2 = friends.copy()

print(friends)
print(friends2)

print(friends.index("Oscar"))
print(friends.count("Jim"))

friends.append("Mike")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Mike")
print(friends)

friends.pop()

friends.extend(lucky_numbers)
print(friends)

friends.clear()

print(lucky_numbers)
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)


