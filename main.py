import speedsmart_tools
import speedsmart_config as config
print("Program started.")
speedsmart_tools.restore_full_length(config.original, config.latest, config.fulllength)
print("Starting hashtag replacing")
speedsmart_tools.hashtag_replacing(config.fulllength)