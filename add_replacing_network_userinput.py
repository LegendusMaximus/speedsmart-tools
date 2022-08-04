import speedsmart_tools
truncated = input("Enter the truncated name of the network currently showing in the SpeedSmart table >")
full = input("Enter the full name of the network in question >")
print("The network name "+full+" has been truncated to "+truncated+" by SpeedSmart. Is this correct? [yes/no]")
choice = input()
if "yes" in choice or "Yes" in choice or "y" in choice or "Y" in choice:
    speedsmart_tools.add_replacing_network(truncated, full)
    print("Network added to replacing list")
else:
    print("Network addition cancelled.")