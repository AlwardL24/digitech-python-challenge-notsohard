def check_robots():
    line = input("Input your written work:\n")

    words = line.split(" ")

    if "robot" in words:
        print("There is a small robot in the line.")
    elif "ROBOT" in words:
        print("There is a big robot in the line.")
    else:
        for word in words:
            if word.lower() == "robot":
                print("There is a medium sized robot in the line.")
                return
        print("No robots here.")

check_robots()