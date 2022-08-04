import speedsmart_tools
name = input("Enter the network name that starts with a # symbol >")
ip = input("Enter the IP address of the network, making sure not to make any mistakes >")
print("The network name "+name+" has the IP address "+ip+". Is this correct? [yes/no]")
choice = input()
if "yes" in choice or "Yes" in choice or "y" in choice or "Y" in choice:
    speedsmart_tools.add_hashtag_network(name, ip)
    print("Network added to hashtag list")
else:
    print("Network addition cancelled.")