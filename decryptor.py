import os
import time

def decryptor():

  a = "."
  b = ".."
  c = "..."
  d = "...."
  e = "....."
  f = "......"
  g = "......."
  h = "........"
  i = "........."
  j = ".........."
  k = "..........."
  l = "............"
  m = "............."
  n = ".............."
  o = "..............."
  p = "................"
  q = "................."
  r = ".................."
  s = "..................."
  t = "...................."
  u = "....................."
  v = "......................"
  w = "......................."
  x = "........................"
  y = "........................."
  z = ".........................."

  # @
  at = "999"
  # #
  hashtag = "998"
  # $
  money = "997"
  # %
  percent = "996"
  # &
  _and = "995"
  # *
  star = "994"
  # -
  dash = "993"
  # =
  equals = "992"
  # (
  p_l = "991"
  # )
  p_r = "990"
  # !
  ep = "989"
  # "
  qm = "988"
  # '
  sqm = "987"
  # :
  colon = "986"
  # ;
  semi_colon = "985"
  # /
  slash_r = "984"
  # ?
  question_mark = "983"
  # .
  period = "982"
  # ,
  comma = "981"
  # ©
  copyright = "980"
  # ®
  reserved = "979"
  # ¢
  cents = "978"
  # <
  left = "977"
  # >
  right = "976"
  # _
  underscore = "975"
  # +
  plus = "974"
  # ¿
  upside_down_qm = "973"
  # [
  lb = "972"
  # ]
  rb = "971"
  # ^
  up = "970"
  # ¡
  upside_down_ep = "969"
  # °
  degrees = "968"
  # ×
  multiply = "967"
  # {
  clb = "966"
  # }
  crb = "965"
  # ±
  poob = "964"
  # ÷
  division = "963"
  # ~
  wave = "962"
  # `
  tl = "961"
  # ´
  tr = "960"
  # •
  bd = "959"
  # £
  ue = "958"
  # |
  vertical = "957"
  # €
  ue2 = "956"
  # ¥
  odd_qm = "955"

  duuap = False
  
  os.system("clear")
  question = input("What is the name of your file?: ")
  os.system("clear")
  _question = input("Did you have a password? (y), or (n): ")
  if _question == "y":
    os.system("clear")
    password = input("What is your password?: ")
    os.system("clear")
    duuap = True
  elif _question == "n":
    duuap = False
  else:
    os.system("clear") 
    print("Invalid input—returning in [5].")
    time.sleep(1)
    os.system("clear")
    print("Invalid input—returning in [4].") 
    time.sleep(1)
    os.system("clear") 
    print("Invalid input—returning in [3].")  
    time.sleep(1) 
    os.system("clear")
    print("Invalid input—returning in [2].")  
    time.sleep(1)
    os.system("clear")
    print("Invalid input—returning in [1].")
    time.sleep(1)  
    os.system("clear")
    return decryptor

  if duuap == True:
    if len(password) == 256:
      if len(question) > 0:
        with open(os.getcwd() + "/" + question + ".txt", "r") as file:
          # missing code for reading password and message./
            else:
              os.system("clear") 
              print("Invalid file—returning in [5].")
              time.sleep(1)
              os.system("clear")
              print("Invalid file—returning in [4].") 
              time.sleep(1)
              os.system("clear") 
              print("Invalid file—returning in [3].")  
              time.sleep(1)
              os.system("clear")
              print("Invalid file—returning in [2].")  
              time.sleep(1)
              os.system("clear")
              print("Invalid file—returning in [1].")
              time.sleep(1)  
              os.system("clear")
              return decryptor
          else:
            os.system("clear")
            print("Invalid file—returning in [5].")
            time.sleep(1)
            os.system("clear")
            print("Invalid file—returning in [4].") 
            time.sleep(1)
            os.system("clear")
            print("Invalid file—returning in [3].")  
            time.sleep(1) 
            os.system("clear")
            print("Invalid file—returning in [2].")  
            time.sleep(1)
            os.system("clear")
            print("Invalid file—returning in [1].")
            time.sleep(1)  
            os.system("clear") 
            return decryptor
    elif len(password) != 256:
      os.system("clear")
      print("Invalid password—returning in [5].")
      time.sleep(1)
      os.system("clear")
      print("Invalid password—returning in [4].")
      time.sleep(1)
      os.system("clear")
      print("Invalid password—returning in [3].")
      time.sleep(1)
      os.system("clear")
      print("Invalid password—returning in [2].")
      time.sleep(1)
      os.system("clear")
      print("Invalid password—returning in [1].")
      time.sleep(1)
      os.system("clear")
      return decryptor
  if duuap == False:
    print("pass")
    time.sleep(10)
    pass