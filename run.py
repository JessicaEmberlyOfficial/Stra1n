import os
import time
from encryptor import encrypt
from decryptor import decryptor
os.system("clear")
question = input("(d)ecrypt, or (e)ncrypt?: ")
if question == "e":
  encrypt()
elif question == "d":
  decryptor()
elif question != "e" or "d":
  os.system("clear")
  print("Invalid entry—exiting in [5].")
  time.sleep(1)
  os.system("clear")
  print("Invalid entry—exiting in [4].")
  time.sleep(1)
  os.system("clear")
  print("Invalid entry—exiting in [3].")
  time.sleep(1)
  os.system("clear")
  print("Invalid entry—exiting in [2].")
  time.sleep(1)
  os.system("clear")
  print("Invalid entry—exiting in [1].")
  time.sleep(1)
  os.system("clear")
  os.system("exit")