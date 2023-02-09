current = input("Current floor: ")
destination = input("Destination floor: ")

for floor in range(int(current), int(destination) + 1):
    print("Level ", floor)