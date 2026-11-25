import sys


def welcome():
  return "Grian's cat\nᓚ₍ ^. ̫ .^₎ <--- Totally Maui"


answer = input("Hello There! Would you like to see Grian's cat? ").strip().lower()

if answer == "yes":
  print(welcome())
else:
  print(f"fine alsomy name is jaden and im fat")
  sys.exit()
