from colorama import init, Fore, Style
import pandas as pd
import requests
init()

def roblox_checker():
  print(Fore.RED + Style.BRIGHT + 'Roblox Username Checker')
  print(Fore.WHITE + Style.BRIGHT + 'Created by: Brennan & Drew')
  
  start = input("\nPress any key.\n")
  
  data = pd.read_csv("NamesToCheck.txt")
  
  names_to_check = list(data["Usernames"])
  hits = open('Available.txt', 'a')
  
  invalid_names = []
  taken_names = []
  available_names = []
  
  for word in names_to_check:
    url = "https://rblx.trade/u/" + word
    check = requests.get(url)
    if int(check.status_code) == 400 and len(word) >= 3 and len(word) < 21:
      hits.write(f'{word}\n')
      print(Fore.GREEN + Style.BRIGHT + f"[AVAILABLE] {word}")
      available_names.append(word)
    elif len(word) < 3:
      print(Fore.YELLOW + Style.BRIGHT + f"[INVALID] {word}")
      invalid_names.append(word)
    elif len(word) > 20:
      print(Fore.YELLOW + Style.BRIGHT + f"[INVALID] {word}")
      invalid_names.append(word)
    else:
      print(Fore.RED + Style.BRIGHT + f"[TAKEN] {word}")
      taken_names.append(word)
  
  hits.close()
  invalid = len(invalid_names)
  taken = len(taken_names)
  available = len(available_names)
  print(Fore.RED + Style.BRIGHT + "\nStats:\n")
  print(Fore.GREEN + Style.BRIGHT + f"Available: {available}\n")
  print(Fore.RED + Style.BRIGHT + f"Taken: {taken}\n")
  print(Fore.YELLOW + Style.BRIGHT + f"Invalid: {invalid}\n")
  total = invalid + taken + available
  print(Fore.WHITE + Style.BRIGHT + f"Total: {total}")

def kaggle_checker():
  print(Fore.BLUE + Style.BRIGHT + 'Kaggle Username Checker')
  print(Fore.WHITE + Style.BRIGHT + 'Created by: Brennan & Drew')
  
  start = input("\nPress any key.")
  
  data = pd.read_csv("NamesToCheck.txt")
  
  names_to_check = list(data["Usernames"])
  hits = open('Available.txt', 'a')
  
  invalid_names = []
  taken_names = []
  available_names = []
  for word in names_to_check:
    url = "https://www.kaggle.com/" + word
    check = requests.get(url)
    if int(check.status_code) == 404 and len(word) >= 6 and len(word) < 21:
      hits.write(f'{word}\n')
      print(Fore.GREEN + Style.BRIGHT + f"[AVAILABLE] {word}")
      available_names.append(word)
    elif len(word) < 6:
      print(Fore.YELLOW + Style.BRIGHT + f"[INVALID] {word}")
      invalid_names.append(word)
    elif len(word) > 20:
      print(Fore.YELLOW + Style.BRIGHT + f"[INVALID] {word}")
      invalid_names.append(word)
    else:
      print(Fore.RED + Style.BRIGHT + f"[TAKEN] {word}")
      taken_names.append(word)
  
  hits.close()    
  invalid = len(invalid_names)
  taken = len(taken_names)
  available = len(available_names)
  print(Fore.BLUE + Style.BRIGHT + "\nStats:\n")
  print(Fore.GREEN + Style.BRIGHT + f"Available: {available}\n")
  print(Fore.RED + Style.BRIGHT + f"Taken: {taken}\n")
  print(Fore.YELLOW + Style.BRIGHT + f"Invalid: {invalid}\n")
  total = invalid + taken + available
  print(Fore.WHITE + Style.BRIGHT + f"Total: {total}")

def replit_checker():
  print(Fore.MAGENTA + Style.BRIGHT + 'Replit Username Checker')
  print(Fore.WHITE + Style.BRIGHT + 'Created by: Brennan & Drew')
  
  start = input("\nPress any key.\n")
  
  data = pd.read_csv("NamesToCheck.txt")
  
  names_to_check = list(data["Usernames"])
  hits = open('Available.txt', 'a')
  
  invalid_names = []
  taken_names = []
  available_names = []
  
  for word in names_to_check:
    url = "https://replit.com/@" + word
    check = requests.get(url)
    if int(check.status_code) == 404 and len(word) >= 2 and len(word) < 16:
      hits.write(f'{word}\n')
      print(Fore.GREEN + Style.BRIGHT + f"[AVAILABLE] {word}")
      available_names.append(word)
    elif len(word) < 2:
      print(Fore.YELLOW + Style.BRIGHT + f"[INVALID] {word}")
      invalid_names.append(word)
    elif len(word) > 15:
      print(Fore.YELLOW + Style.BRIGHT + f"[INVALID] {word}")
      invalid_names.append(word)
    else:
      print(Fore.RED + Style.BRIGHT + f"[TAKEN] {word}")
      taken_names.append(word)
  
  hits.close()
  invalid = len(invalid_names)
  taken = len(taken_names)
  available = len(available_names)
  print(Fore.MAGENTA + Style.BRIGHT + "\nStats:\n")
  print(Fore.GREEN + Style.BRIGHT + f"Available: {available}\n")
  print(Fore.RED + Style.BRIGHT + f"Taken: {taken}\n")
  print(Fore.YELLOW + Style.BRIGHT + f"Invalid: {invalid}\n")
  total = invalid + taken + available
  print(Fore.WHITE + Style.BRIGHT + f"Total: {total}")