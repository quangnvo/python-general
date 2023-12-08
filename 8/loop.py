value = 1
while value <= 10:
    value = value + 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equal to " + str(value))
