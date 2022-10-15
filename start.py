# This program lets users select which part of the tool they would like to use from a menu

try:
    import speedsmart_secrets
except:
    print("Warning: Please rename speedsmart_secrets_example.py to speedsmart_secrets.py before using this tool. Failing to do this will give you problems down the line.")

import speedsmart_tools
import speedsmart_config as config

print("Welcome to SpeedSmart Tools!")
print("")
print("====================")
print("")
print("What would you like to do?")
menu = ["Run the tool", "Add an and-replace network", "Add a hashtag network", "Sort your table by Download speed", "Sort your table by upload speed", "Combine multiple tables defined in the config file", "Search your table"]
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
elif choice == 4:
    print("Starting sorting...")
    speedsmart_tools.sort_by_speed(0)
    print("Your sorted table is named \"speed.csv\" and is located in the \"sorting\" directory.")
elif choice == 5:
    print("Starting sorting...")
    speedsmart_tools.sort_by_speed(1)
    print("Your sorted table is named \"speed.csv\" and is located in the \"sorting\" directory.")
elif choice == 6:
    print("Combining tables, please wait...")
    speedsmart_tools.combine(config.multipletables)
    print("Finished.")
elif choice == 7:
    import speedsmart_search
    print("Find your results file in the Results directory")
else:
    print("Invalid selection.")