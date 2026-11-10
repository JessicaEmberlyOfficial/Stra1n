import os
import random
import time
import configparser
import rsa
import secrets

def encrypt():
  msgPK, msgPRK = rsa.newkeys(2048)
  spPK, spPRK = rsa.newkeys(2048)
  spPK1, spPRK1 = rsa.newkeys(2048)
  spPK2, spPRK2 = rsa.newkeys(2048)
  spPK3, spPRK3 = rsa.newkeys(2048)
  spPK4, spPRK4 = rsa.newkeys(2048)
  spPK5, spPRK5 = rsa.newkeys(2048)
  spPK6, spPRK6 = rsa.newkeys(2048)
  spPK7, spPRK7 = rsa.newkeys(2048)
  spPK8, spPRK8 = rsa.newkeys(2048)
  spPK9, spPRK9 = rsa.newkeys(2048)
  spPK10, spPRK10 = rsa.newkeys(2048)
  pidPK, pidPRK = rsa.newkeys(2048)
  
  # Setup config parser.
  config = configparser.ConfigParser()
  config.read(os.getcwd() + "/Stra1n.ini")
  alphabet = config["Alphabet"]
  symbols = config["Symbols"]
  bytes = config["Bytes"]
  numbers = config["Numbers"]
  message = config["Message_In"]

  # Increase values by x.
  increase_values_by = numbers["increase_values_by"]
    
  # Booleans.
  duwap = False

  # Strings.
  _password = ""
  _replaced = ""

  # Data segments.
  data_seg_1 = random.randbytes(int(bytes["byte_number"] + numbers["increase_values_by"]))
  data_seg_2 = random.randbytes(int(bytes["byte_number"] + numbers["increase_values_by"]))
  data_seg_3 = random.randbytes(int(bytes["byte_number"] + numbers["increase_values_by"]))
  data_seg_4 = random.randbytes(int(bytes["byte_number"] + numbers["increase_values_by"]))
  data_seg_5 = random.randbytes(int(bytes["byte_number"] + numbers["increase_values_by"]))
  data_seg_6 = random.randbytes(int(bytes["byte_number"] + numbers["increase_values_by"]))
  data_seg_7 = random.randbytes(int(bytes["byte_number"] + numbers["increase_values_by"]))

  # Data segments.
  d1 = str(data_seg_1)
  d2 = str(data_seg_2)
  d3 = str(data_seg_3)
  d4 = str(data_seg_4)
  d5 = str(data_seg_5)
  d6 = str(data_seg_6)

  # Alphabet.
  a = alphabet["a"]
  b = alphabet["b"]
  c = alphabet["c"]
  d = alphabet["d"]
  e = alphabet["e"]
  f = alphabet["f"]
  g = alphabet["g"]
  h = alphabet["h"]
  i = alphabet["i"]
  j = alphabet["j"]
  k = alphabet["k"]
  l = alphabet["l"]
  m = alphabet["m"]
  n = alphabet["n"]
  o = alphabet["o"]
  p = alphabet["p"]
  q = alphabet["q"]
  r = alphabet["r"]
  s = alphabet["s"]
  t = alphabet["t"]
  u = alphabet["u"]
  v = alphabet["v"]
  w = alphabet["w"]
  x = alphabet["x"]
  y = alphabet["y"]
  z = alphabet["z"]

  # Symbols.
  one = symbols["one"]
  two = symbols["two"]
  three = symbols["three"]
  four = symbols["four"]
  five = symbols["five"]
  six = symbols["six"]
  seven = symbols["seven"]
  eight = symbols["eight"]
  nine = symbols["nine"]
  ten = symbols["ten"]
  eleven = symbols["eleven"]
  twelve = symbols["twelve"]
  thirteen = symbols["thirteen"]
  fourteen = symbols["fourteen"]
  fifteen = symbols["fifteen"]
  sixteen = symbols["sixteen"]
  seventeen = symbols["seventeen"]
  eighteen = symbols["eighteen"]
  nineteen = symbols["nineteen"]
  twenty = symbols["twenty"]
  twenty_one = symbols["twenty_one"]
  twenty_two = symbols["twenty_two"]
  twenty_three = symbols["twenty_three"]
  twenty_four = symbols["twenty_four"]
  twenty_five = symbols["twenty_five"]
  twenty_six = symbols["twenty_six"]
  twenty_seven = symbols["twenty_seven"]
  twenty_eight = symbols["twenty_eight"]
  twenty_nine = symbols["twenty_nine"]
  thirty = symbols["thirty"]
  thirty_one = symbols["thirty_one"]
  thirty_two = symbols["thirty_two"]
  thirty_three = symbols["thirty_three"]
  thirty_four = symbols["thirty_four"]
  thirty_five = symbols["thirty_five"]
  thirty_six = symbols["thirty_six"]
  thirty_seven = symbols["thirty_seven"]
  thirty_eight= symbols["thirty_eight"]
  thirty_nine = symbols["thirty_nine"]
  fourty = symbols["fourty"]
  fourty_one = symbols["fourty_one"]
  fourty_two = symbols["fourty_two"]
  fourty_three = symbols["fourty_three"]
  fourty_four = symbols["fourty_four"]
  fourty_five = symbols["fourty_five"]

  # IN
  _in = ""
  
  # Does user want a password.
  duwap = False
  os.system("clear")
  _file = input("Do you want to use the contents of a file? (y), or (n): ")
  os.system("clear")
  if _file == "y":
    _path = input("What is the path?: ")
    if len(_path) > 0:
      pass
    else:
      _time = 5
      while _time != 1:
        print("Please make sure to add something to encrypt—returning in [" + str(_time) + "].")
        time.sleep(1)
        os.system("clear")
        _time -= 1
      return encrypt()
    if os.path.isfile(_path):
      file = open(_path, "r")
      _in = file.read()
    else:
      _time = 5
      while _time != 1:
        print("Invalid path—returning in [" + str(_time) + "].")
        time.sleep(1)
        os.system("clear")
        _time -= 1
      return encrypt()
  elif _file == "n":
    _in = input("What do I encrypt?: ")
    os.system("clear")
  else:
    os.system("clear")
    _time = 5
    while _time != 1:
      print("Please make sure to type an accepted input—returning in [" + str(_time) + "].")
      time.sleep(1)
      os.system("clear")
      _time -= 1
    return encrypt()
  if len(_in) > 0:
    pass
  else:
    os.system("clear")
    _time = 5
    while _time != 1:
      print("Please make sure to add something to encrypt—returning in [" + str(_time) + "].")
      time.sleep(1)
      os.system("clear")
      _time -= 1
    return encrypt()
  os.system("clear")
  diuap = input("Do I use a password? (y) or (n): ")

  os.system("clear")
  if diuap == "y":
    password = input("What password do I use?: ")
    duwap = True
    if len(password) == 256:
      _password = password
    elif len(password) != 256:
      os.system("clear")
      _time = 5
      while _time != 1:
        print("Please make sure your password has 256 characters—returning in [" + str(_time) + "].")
        time.sleep(1)
        os.system("clear")
        _time -= 1
      else:
        return encrypt()
  elif diuap == "n":
      duwap = False
    
  if duwap == True:
    # Obfuscate and mark message.
    _new_message = _in.replace("0", message["zero"]).replace("1", message["one"]).replace("2", message["two"]).replace("3", message["three"]).replace("4", message["four"]).replace("5", message["five"]).replace("6", message["six"]).replace("7", message["seven"]).replace("8", message["eight"]).replace("9", message["nine"]).replace("a", message["a"]).replace("b", message["b"]).replace("c", message["c"]).replace("d", message["d"]).replace("e", message["e"]).replace("f", message["f"]).replace("g", message["g"]).replace("h", message["h"]).replace("i", message["i"]).replace("j", message["j"]).replace("k", message["l"]).replace("l", message["l"]).replace("m", message["m"]).replace("n", message["n"]).replace("o", message["o"]).replace("p", message["p"]).replace("q", message["q"]).replace("r", message["r"]).replace("s", message["s"]).replace("t", message["t"]).replace("u", message["u"]).replace("v", message["v"]).replace("w", message["w"]).replace("x", message["x"]).replace("y", message["y"]).replace("z", message["z"]).replace("A", message["_A"]).replace("B", message["_B"]).replace("C", message["_C"]).replace("D", message["_D"]).replace("E", message["_E"]).replace("F", message["_F"]).replace("G", message["_G"]).replace("H", message["_H"]).replace("I", message["_I"]).replace("J", message["_J"]).replace("K", message["_K"]).replace("L", message["_L"]).replace("M", message["_M"]).replace("N", message["_N"]).replace("O", message["_O"]).replace("P", message["_P"]).replace("Q", message["_Q"]).replace("R", message["_R"]).replace("S", message["_S"]).replace("T", message["_T"]).replace("U", message["_U"]).replace("V", message["_V"]).replace("W", message["_W"]).replace("X", message["_X"]).replace("Y", message["_Y"]).replace("Z", message["_Z"])
    # Replacing _password in order to obfuscate it.
    _new_password = _password.replace("a", a + " ").replace("b", b + " ").replace("c", c + " ").replace("d", d + " ").replace("e", e + " ").replace("f", f + " ").replace("g", g + " ").replace("h", h + " ").replace("i", i + " ").replace("j", j + " ").replace("k", k + " ").replace("l", l + " ").replace("m", m + " ").replace("n", n + " ").replace("o", o + " ").replace("p", p + " ").replace("q", q + " ").replace("r", r + " ").replace("s", s + " ").replace("t", t + " ").replace("u", u + " ").replace("v", v + " ").replace("w", w + " ").replace("x", x + " ").replace("y", y + " ").replace("z", z + " ").replace("A", a + ".7").replace("B", b + ".7").replace("C", c + ".7").replace("D", d + ".7").replace("E", e + ".7").replace("F", f + ".7").replace("G", g + ".7").replace("H", h + ".7").replace("I", i + ".7").replace("J", j + ".7").replace("K", k + ".7").replace("L", l + ".7").replace("M", m + ".7").replace("N", n + ".7").replace("O", o + ".7").replace("P", p + ".7").replace("Q", q + ".7").replace("R", r + ".7").replace("S", s + ".7").replace("T", t + ".7").replace("U", u + ".7").replace("V", v + ".7").replace("W", w + ".7").replace("X", x + ".7").replace("Y", y + ".7").replace("Z", z + ".7").replace("@", one).replace("#", two).replace("$", three).replace("&", four).replace("*", five).replace("-", six).replace("=", seven).replace("(", eight).replace(")", nine).replace("!", ten).replace('"', eleven).replace("'", twelve).replace(":", thirteen).replace(";", nine).replace("/", ten).replace("?", eleven).replace(",", twelve).replace("¡", thirteen).replace("<", fourteen).replace(">", fifteen).replace("¢", sixteen).replace("|", seventeen).replace("¿", eighteen).replace("©", nineteen).replace("®", twenty).replace("+", twenty_one).replace("±", twenty_two).replace("{", twenty_three).replace("}", twenty_four).replace("[", twenty_five).replace("]", twenty_seven).replace("~", twenty_eight).replace("÷", twenty_nine).replace("•", thirty).replace("°", thirty_one).replace("`", thirty_two).replace("´", thirty_four).replace("¥", thirty_five).replace("£", thirty_six).replace("€", thirty_seven).replace("1", "/999/").replace("2", "/888/").replace("3", "/777/").replace("4", "/666/").replace("5", "/555/").replace("6", "/444/").replace("7", "/333/").replace("8", "/222/").replace("9", "/111/")
    sp = _new_password.split(" ", 11)
    _password_id = secrets.token_hex(16)
    new_message_encode = str(" - " + _new_message + " - ")
    # Encrypt message.
    encMessage = rsa.encrypt(new_message_encode.encode(), msgPK)
    # Encrypt Password
    encpwd1 = rsa.encrypt(sp[0].encode(), spPK)
    encpwd2 = rsa.encrypt(sp[1].encode(), spPK1)
    encpwd3 = rsa.encrypt(sp[2].encode(), spPK2)
    encpwd4 = rsa.encrypt(sp[3].encode(), spPK3)
    encpwd5 = rsa.encrypt(sp[4].encode(), spPK4)
    encpwd6 = rsa.encrypt(sp[5].encode(), spPK5)
    encpwd7 = rsa.encrypt(sp[6].encode(), spPK6)
    encpwd8 = rsa.encrypt(sp[7].encode(), spPK7)
    encpwd9 = rsa.encrypt(sp[8].encode(), spPK8)
    encpwd10 = rsa.encrypt(sp[9].encode(), spPK9)
    encpwd11 = rsa.encrypt(sp[10].encode(), spPK10)
    # Encrypt PID
    encPID = rsa.encrypt(_password_id.encode(), pidPK)
    os.system("clear")
    # Tell user to write down keys.
    input("\x1b[31mPlease write down:" + "\x1b[32m\nMessage Private Key: " + str(msgPRK) + "\x1b[33m\nPassword P1 Private Key:" + str(encpwd1) + "\x1b[34m\nPassword P2 Private Key: " + str(encpwd2) + "\x1b[35m\nPassword P3 Private Key: " + str(encpwd3) + "\x1b[35m\nPassword P4 Private Key: " + str(encpwd4) + "\x1b[36m\nPassword P5 Private Key: "+ str(encpwd5) + "\x1b[31m\nPassword P6 Prviate Key: " + str(encpwd6) + "\x1b[32m\nPassword P7 Private Key: " + str(encpwd7) + "\x1b[33m\nPassword P8 Private Key: " + str(encpwd8) + "\x1b[34m\nPassword P9 Private Key: " + str(encpwd9) + "\x1b[35m\nPassword P10 Private Key: " + str(encpwd10) + "\x1b[36m\n Password P11 Private Key: " + str(encpwd11) + "\x1b[32m\nPID Private Key: " + str(encPID) + "\x1b[31m\nOnce saved, press enter.")
  elif duwap == False:
    # Obfuscate and mark message.
    _new_message_encode = _in.replace("0", message["zero"]).replace("1", message["one"]).replace("2", message["two"]).replace("3", message["three"]).replace("4", message["four"]).replace("5", message["five"]).replace("6", message["six"]).replace("7", message["seven"]).replace("8", message["eight"]).replace("9", message["nine"]).replace("a", message["a"]).replace("b", message["b"]).replace("c", message["c"]).replace("d", message["d"]).replace("e", message["e"]).replace("f", message["f"]).replace("g", message["g"]).replace("h", message["h"]).replace("i", message["i"]).replace("j", message["j"]).replace("k", message["k"]).replace("l", message["l"]).replace("m", message["m"]).replace("n", message["n"]).replace("o", message["o"]).replace("p", message["p"]).replace("q", message["q"]).replace("r", message["r"]).replace("s", message["s"]).replace("t", message["t"]).replace("u", message["u"]).replace("v", message["v"]).replace("w", message["w"]).replace("x", message["x"]).replace("y", message["y"]).replace("z", message["z"]).replace("A", message["_A"]).replace("B", message["_B"]).replace("C", message["_C"]).replace("D", message["_D"]).replace("E", message["_E"]).replace("F", message["_F"]).replace("G", message["_G"]).replace("H", message["_H"]).replace("I", message["_I"]).replace("J", message["_J"]).replace("K", message["_K"]).replace("L", message["_L"]).replace("M", message["_M"]).replace("N", message["_N"]).replace("O", message["_O"]).replace("P", message["_P"]).replace("Q", message["_Q"]).replace("R", message["_R"]).replace("S", message["_S"]).replace("T", message["_T"]).replace("U", message["_U"]).replace("V", message["_V"]).replace("W", message["_W"]).replace("X", message["_X"]).replace("Y", message["_Y"]).replace("Z", message["_Z"])
    # Encrypt message.
    encMessage = rsa.encrypt(_new_message_encode.encode(), msgPK)
    # Tell user to write down keys.
    input("\x1b[31mPlease write down: " + str(msgPRK) + "\x1b[33m - Once saved, press enter.")
  if os.path.isfile(os.getcwd() + "/data.txt") == True:
    os.system("clear")
    dfep = input("An encrypted file already exists, do you want to replace it? (y) or (n): ")
    if dfep == "y":
      os.system("clear")
      with open(os.getcwd() + "/data.txt", 'w') as file:
        if duwap == True:
          file.write(d1 + d2 + d3 + "/-/0/-/" + str(encMessage) + "/-/0/-/" + "/-/1/-/" + str(encpwd1) + "/-/1/-/" + "/-/2/-/" + str(encpwd2) + "/-/2/-/" "/-/3/-/" + str(encpwd3) + "/-/3/-/" + "/-/4/-/" + str(encpwd4) + "/-/4/-/" + "/-/5/-/" + str(encpwd5) + "/-/5/-/" + "/-/6/-/" + str(encpwd6) + "/-/6/-/" + "/-/7/-/" + str(encpwd7) + "/-/7/-/" + "/-/8/-/" + str(encpwd8) + "/-/8/-/" + "/-/9/-/" + str(encpwd9) + "/-/9/-/" + "/-/10/-/" + str(encpwd10) + "/-/10/-/" + "/-/11/-/" + str(encpwd11) + "/-/11/-/" + "/-/12/-/" + str(encPID) + "/-/12/-/" + d4 + d5 + d6)
        elif duwap == False:
          file.write(d1 + d2 + d3 + "/-/0/-/" + str(encMessage) + "/-/0/-/" + d4 + d5 + d6)
          os.system("clear")
      if os.path.isfile(os.getcwd() + "/data.txt") == True:
            print("Encrypted file created at: " + os.getcwd() + "/data.txt")
      elif os.path.isfile(os.getcwd() + "/data.txt") == False:
        os.system("clear")
        _time = 5
        while _time != 1:
          print("There was an error creating your file—returning in [" + str(_time) + "].")
          time.sleep(1)
          os.system("clear")
          _time -= 1
        else:
          return encrypt()
    elif dfep == "n":
      os.system("clear")
      name = input("Please enter a new name for your new file? (e.g. Stra1n): ")
      if "." in name:
        os.system("clear")
        _time = 5
        while _time != 1:
          print("Please do not add file extensions—returning in [" + str(_time) + "].")
          time.sleep(1)
          os.system("clear")
          _time -= 1
        else:
          return encrypt()
      elif "." not in name:
        with open(os.getcwd() + name + ".", 'w') as file:
          if duwap == True:
            file.write(d1 + d2 + d3 + "/-/0/-/" + str(encMessage) + "/-/0/-/" + "/-/1/-/" + str(encpwd1) + "/-/1/-/" + "/-/2/-/" + str(encpwd2) + "/-/2/-/" "/-/3/-/" + str(encpwd3) + "/-/3/-/" + "/-/4/-/" + str(encpwd4) + "/-/4/-/" + "/-/5/-/" + str(encpwd5) + "/-/5/-/" + "/-/6/-/" + str(encpwd6) + "/-/6/-/" + "/-/7/-/" + str(encpwd7) + "/-/7/-/" + "/-/8/-/" + str(encpwd8) + "/-/8/-/" + "/-/9/-/" + str(encpwd9) + "/-/9/-/" + "/-/10/-/" + str(encpwd10) + "/-/10/-/" + "/-/11/-/" + str(encpwd11) + "/-/11/-/" + "/-/12/-/" + str(encPID) + "/-/12/-/" + d4 + d5 + d6)
            os.system("clear")
          if duwap == False:
            file.write(d1 + d2 + d3 + "/-/0/-/" + str(encMessage) + "/-/0/-/" + d4 + d5 + d6)
            os.system("clear")
          if os.path.isfile(os.getcwd() + "/" + name + ".txt") == True:
            print("Encrypted file created at: " + os.getcwd() + "/" + name + ".txt")
          if os.path.isfile(os.getcwd() + "/" + name + ".txt") == False:
            os.system("clear")
            _time = 5
            while time != 1:
              print("There was an error creating your file—returning in [" + str(_time) + "].")
              time.sleep(1)
              os.system("clear")
              _time -= 1
            else:
              return encrypt()
  elif os.path.isfile(os.getcwd() + "/data.txt") == False:
    with open(os.getcwd() + "/data.txt", 'w') as file:
      if duwap == True:
        file.write(d1 + d2 + d3 + "/-/0/-/" + str(encMessage) + "/-/0/-/" + "/-/1/-/" + str(encpwd1) + "/-/1/-/" + "/-/2/-/" + str(encpwd2) + "/-/2/-/" "/-/3/-/" + str(encpwd3) + "/-/3/-/" + "/-/4/-/" + str(encpwd4) + "/-/4/-/" + "/-/5/-/" + str(encpwd5) + "/-/5/-/" + "/-/6/-/" + str(encpwd6) + "/-/6/-/" + "/-/7/-/" + str(encpwd7) + "/-/7/-/" + "/-/8/-/" + str(encpwd8) + "/-/8/-/" + "/-/9/-/" + str(encpwd9) + "/-/9/-/" + "/-/10/-/" + str(encpwd10) + "/-/10/-/" + "/-/11/-/" + str(encpwd11) + "/-/11/-/" + "/-/12/-/" + str(encPID) + "/-/12/-/" + d4 + d5 + d6)
        os.system("clear")
      elif duwap == False:
        file.write(d1 + d2 + d3 + "/-/0/-/" + str(encMessage) + "/-/0/-/" + d4 + d5 + d6)
      os.system("clear")
      if os.path.isfile(os.getcwd() + "/data.txt") == True:
        print("Encrypted file created at: " + os.getcwd() + "/data.txt")
      elif os.path.isfile(os.getcwd() + "/data.txt") == False:
        os.system("clear")
        _time = 5
        while _time != 1:
          print("There was an error creating your file—returning in [" + str(_time) + "].")
          os.system("clear")
          _time -= 1
        else:
          return encrypt()
