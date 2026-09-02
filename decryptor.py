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
  else:
    pass

  if duuap == True:
    if len(password) == 256:
      if len(question) > 0:
        with open(os.getcwd() + "/" + question + ".txt", "r") as file:
          if _password_split_1 or _password_split_2 or _password_split_3 or _password_split_4 or _password_split_5 in file:
            if "99.01" or "88.01" or "77.01" or "66.01" or "55.01" or "44.01" or "33.01" or "22.01" or "11.01" or "00.01" or "99.02" or "88.02" or "77.02" or "66.02" or "55.02" or "44.02" or "33.02" or "22.02" or "11.02" or "00.02" or "99.03" or "88.03" or "77.03" or "66.03" or "55.03" or "44.03" or "33.03" or "22.03" or "11.03" or "00.03" or "99.04" or "88.04" or "77.04" or "66.04" or "55.04" or "44.04" or "33.04" or "22.04" or "11.04" or "00.04" or "99.05" or "88.05" or "77.05" or "66.05" or "55.05" or "44.05" or "33.05" or "22.05" or "11.05" or "00.05" or "99.06" or "88.06" or "77.06" or "66.06" or "55.06" or "44.06" or "33.06" or "22.06" or "11.06" or "00.06" in file:
              contents = file.read()
              contents.replace("99.01", "-1-").replace("88.01", "-2-").replace("77.01", "-3-").replace("66.01", "-4-").replace("55.01", "-5-").replace("44.01", "-6-").replace("33.01", "-7-").replace("22.01", "-8-").replace("11.01", "-9-").replace("00.01", "-a-").replace("99.02", "-b-").replace("88.02", "-c-").replace("77.02", "-d-").replace("66.02", "-e-").replace("55.02", "-f-").replace("44.02", "-g-").replace("33.02", "-h-").replace("22.02", "-i-").replace("11.02", "-j-").replace("00.02", "-k-").replace("99.03", "-l-").replace("88.03", "-m-").replace("77.03", "-n-").replace("66.03", "-o-").replace("55.03", "-p-").replace("44.03", "-q-").replace("33.03", "-r-").replace("22.03", "-s-").replace("11.03", "-t-").replace("00.03", "-u-").replace("99.04", "-v-").replace("88.04", "-w-").replace("77.04", "-x-").replace("66.04", "-y-").replace("55.04", "-z-").replace("44.04", "-A-").replace("33.04", "-B-").replace("22.04", "-C-").replace("11.04", "-D-").replace("00.04", "-E-").replace("99.05", "-F-").replace("88.05", "-G-").replace("77.05", "-H-").replace("66.05", "-I-").replace("55.05", "-J-").replace("44.05", "-K-").replace("33.05", "-L-").replace("22.05", "-M-").replace("11.05", "-N-").replace("00.05", "-O-").replace("99.06", "-P-").replace("88.06", "-Q-").replace("77.06", "-R-").replace("66.06", "-S-").replace("55.06", "-T-").replace("44.06", "-U-").replace("33.06", "-V-").replace("22.06", "-W-").replace("11.06", "-X-").replace("00.06", "-Y-").replace("99.07", "-Z-")
              
            if "-1-" or "-2-" or "-3-" or "-4-" or "-5-" or "-6-" or "-7-" or "-8-" or "-9-" or "-a-" or "-b-" or "-c-" or "-d-" or "-e-" or "-f-" or "-g-" or "-h-" or "-i-" or "-j-" or "-k-" or "-l-" or "-m-" or "-n-" or "-o-" or "-p-" or "-m-" or "-n-" or "-o-" or "-p-" or "-q-" or "-r-" or "-s-" or "-t-" or "-u-" or "-v-" or "-w-" or "-x-" or "-y-" or "-z-" in contents:
              # extract words in order
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