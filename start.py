print("Welcome to SpeedSmart Tools!")
print("")
print("====================")
print("")
print("What would you like to do?")
menu = ["Run the tool", "Add an and-replace network", "Add a hashtag network"]
for i, item in enumerate(menu):
    print(i+1, ". ", item)
print("[Type the number of your choice.]")
choice = int(input())
if choice == 1:
    import main
elif choice == 2:
    import add_replacing_network_userinput
elif choice == 3:
    import add_hashtag_network_userinput
else:
    print("Invalid selection.")