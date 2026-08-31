import os
from encryptor import encrypt
# from decryptor import decryptor
os.system("clear")
question = input("(d)ecrypt, or (e)ncrypt?: ")
if question == "e":
  encrypt()
if question == "d":
  encrypt()