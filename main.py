from scripts import roblox_checker, kaggle_checker, replit_checker
from colorama import init, Fore, Style

init()

print(Fore.BLACK + Style.BRIGHT + "Black Diamond Checker\n")
print(Fore.RED + Style.BRIGHT + "[1] Roblox (Slower CPM)\n")
print(Fore.BLUE + Style.BRIGHT + "[2] Kaggle (Fast CPM)\n")
print(Fore.MAGENTA + Style.BRIGHT + "[3] Replit (Medium CPM)\n")

done = False
while done != True:
  user_input = input(Fore.WHITE + Style.BRIGHT + "Select a checker: ")
  print()
  if user_input == "1":
    roblox_checker()
    done = True
  elif user_input == "2":
    kaggle_checker()
    done = True
  elif user_input == "3":
    replit_checker()
    done = True
  else:
    print("Please enter a valid number.")