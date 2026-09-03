import os
import time
from encryptor import encrypt
# from decryptor import decryptor
os.system("clear")
question = input("(d)ecrypt, or (e)ncrypt?: ")
if question == "e":
  encrypt()
elif question == "d":
  decryptor()
elif question != "e" or "d":
  os.system("clear")
  _time = 5
  while _time != 1:
    print("Invalid entry—exiting in [" + str(_time) + "].")
    time.sleep(1)
    os.system("clear")
    _time -= 1
  else:
    os.system("exit")