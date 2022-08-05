import speedsmart_tools
import speedsmart_config as config
print("Program started.")
if config.puttingtogether == 1:
    speedsmart_tools.restore_full_length(config.original, config.latest, config.fulllength)
else:
    print("Temporarily deleting the count column from your table. This will be added back later in the program if requested.")
    speedsmart_tools.delete_count(config.fulllength)

if config.andnetworks == 0:
    print("Skipping and replacing")
else:
    print("Starting and replacing")
    speedsmart_tools.and_replacing(config.fulllength)

if config.hashnetworks == 0:
    print("Skipping hashtag replacing")
else:
    print("Starting hashtag replacing")
    speedsmart_tools.hashtag_replacing(config.fulllength)

if config.count == 1:
    print("Restoring count column")
    speedsmart_tools.restore_count(config.fulllength)
print("Finished!")
