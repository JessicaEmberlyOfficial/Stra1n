import os
import time

def decryptor():

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
  
  os.system("clear")
  question = input("What is the name of your file?: ")
  os.system("clear")
  password = input("What is your password?: ")

  _new_password = password.replace("a", a + " ").replace("b", b + " ").replace("c", c + " ").replace("d", d + " ").replace("e", e + " ").replace("f", f + " ").replace("g", g + " ").replace("h", h + " ").replace("i", i + " ").replace("j", j + " ").replace("k", k + " ").replace("l", l + " ").replace("m", m + " ").replace("n", n + " ").replace("o", o + " ").replace("p", p + " ").replace("q", q + " ").replace("r", r + " ").replace("s", s + " ").replace("t", t + " ").replace("u", u + " ").replace("v", v + " ").replace("w", w + " ").replace("x", x + " ").replace("y", y + " ").replace("z", z + " ").replace("A", a + ".7").replace("B", b + ".7").replace("C", c + ".7").replace("D", d + ".7").replace("E", e + ".7").replace("F", f + ".7").replace("G", g + ".7").replace("H", h + ".7").replace("I", i + ".7").replace("J", j + ".7").replace("K", k + ".7").replace("L", l + ".7").replace("M", m + ".7").replace("N", n + ".7").replace("O", o + ".7").replace("P", p + ".7").replace("Q", q + ".7").replace("R", r + ".7").replace("S", s + ".7").replace("T", t + ".7").replace("U", u + ".7").replace("V", v + ".7").replace("W", w + ".7").replace("X", x + ".7").replace("Y", y + ".7").replace("Z", z + ".7").replace("@", at).replace("#", hashtag).replace("$", money).replace("&", _and).replace("*", star).replace("-", dash).replace("=", equals).replace("(", p_l).replace(")", p_r).replace("!", ep).replace('"', qm).replace("'", sqm).replace(":", colon).replace(";", semi_colon).replace("/", slash_r).replace("?", question_mark).replace(",", comma).replace("¡", upside_down_ep).replace("<", left).replace(">", right).replace("¢", cents).replace("|", vertical).replace("¿", upside_down_qm).replace("©", copyright).replace("®", reserved).replace("+", plus).replace("±", poob).replace("{", clb).replace("}", crb).replace("[", lb).replace("]", rb).replace("~", wave).replace("÷", division).replace("•", bd).replace("°", degrees).replace("`", tl).replace("´", tr).replace("¥", u).replace("£", ue).replace("€", ue2).replace("¥", odd_qm).replace("1", " 9 ").replace("2", " 8 ").replace("3", " 7 ").replace("4", " 6 ").replace("5", " ..... ").replace("6", " 4 ").replace("7", " 3 ").replace("8", " 2 ").replace("9", " 1 ")

  first_part = _new_password[:len(_new_password)//2]
  second_part = _new_password[len(_new_password)//2]
  third_part = _new_password[len(_new_password)//2]
  fourth_part = _new_password[len(_new_password)//2]
  fifth_part = _new_password[len(_new_password)//2:]
  _password_split_1 = " -start- " + first_part + " -end- "
  _password_split_2 = " --start-- " + second_part + " --end-- "
  _password_split_3 = " ---start--- " + third_part + " ---end--- "
  _password_split_4 = " ----start---- " + fourth_part + " ----end---- "
  _password_split_5 = " -----start----- " + fifth_part + " -----end----- "
  
  if len(password) == 256:
    if len(question) > 0:
      with open(os.getcwd() + "/" + question + ".txt", "r") as file:
        if _password_split_1 or _password_split_2 or _password_split_3 or _password_split_4 or _password_split_5 in file:
          if # in file:
            print(":)")
          elif # not in file:
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
    else:
      os.system("clear")
      print("Invalid file name—returning in [5].")
      time.sleep(1)
      os.system("clear")
      print("Invalid file name—returning in [4].")
      time.sleep(1)
      os.system("clear")
      print("Invalid file name—returning in [3].")
      time.sleep(1)
      os.system("clear")
      print("Invalid file name—returning in [2].")
      time.sleep(1)
      os.system("clear")
      print("Invalid file name—returning in [1].")
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
    pass