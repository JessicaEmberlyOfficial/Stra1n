import os
import random
import time
import configparser

def encrypt():

  # Increase values by...
  increase_values_by = 0
  
  # Setup config parser.
  config = configparser.ConfigParser()
  config.read(os.getcwd() + "/Stra1n.ini")
  alphabet = config["Alphabet"]
  symbols = config["Symbols"]
  bytes = config["Bytes"]
  numbers = config["Numbers"]
  dictionary = config["Dictionary"]
  message = config["Message"]

  # Increase values by x.
  increase_values_by = numbers["increase_values_by"]
    
  # Booleans.
  duwap = False

  # Strings.
  _ev = ""
  _password = ""
  _replaced = ""

  # Data segments.
  data_seg_1 = random.randbytes(int(bytes["byte_number"]))
  data_seg_2 = random.randbytes(int(bytes["byte_number"]))
  data_seg_3 = random.randbytes(int(bytes["byte_number"]))
  data_seg_4 = random.randbytes(int(bytes["byte_number"]))
  data_seg_5 = random.randbytes(int(bytes["byte_number"]))
  data_seg_6 = random.randbytes(int(bytes["byte_number"]))
  data_seg_7 = random.randbytes(int(bytes["byte_number"]))

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

  # Random number generation for extensive randomization.
  numbers = str(random.randrange(1, 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)) + str(random.randrange(int(500) + int(increase_values_by), 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)) + str(random.randrange(int(1000) + int(increase_values_by), 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)) + str(random.randrange(int(1500) + int(increase_values_by), 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)) + str(random.randrange(int(2000) + int(increase_values_by), 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)) + str(random.randrange(int(2500) + int(increase_values_by), 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)) + str(random.randrange(int(3000) + int(increase_values_by), 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)) + str(random.randrange(int(3500) + int(increase_values_by), 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)) + str(random.randrange(int(4000) + int(increase_values_by), 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)) + str(random.randrange(int(4500) + int(increase_values_by), 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)) + str(random.randrange(int(5000) + int(increase_values_by), 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111))

  # Does user want a password.
  duwap = False

  os.system("clear")
  _in = input("What do I encrypt? (Letters, and numbers only.): ")
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
    else:
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
        print("Please make sure your password has 256 or more characters—returning in [" + str(_time) + "].")
        time.sleep(1)
        os.system("clear")
        _time -= 1
      else:
        return encrypt()
  elif diuap == "n":
      duwap = False

  # Dictionary for obfuscating message.
  dictionary = {"a": dictionary["a"], "b": dictionary["b"], "c": dictionary["c"], "d": dictionary["d"], "e": dictionary["e"], "f": dictionary["f"], "g": dictionary["g"], "h": dictionary["h"], "i": dictionary["i"], "j": dictionary["j"], "k": dictionary["k"], "l": dictionary["l"], "m": dictionary["m"], "n": dictionary["n"], "o": dictionary["o"], "p": dictionary["p"], "q": dictionary["q"], "r": dictionary["r"], "s": dictionary["s"], "t": dictionary["u"], "u": dictionary["v"], "v": dictionary["w"], "w": dictionary["w"], "x": dictionary["x"], "y": dictionary["y"], "z": dictionary["z"]}

  # Make translation.
  table = str.maketrans(dictionary)

  # Translate.
  ev = _in.translate(table)

  # Set _ev.
  _ev = ev

  if duwap == True:
    # Obfuscate message once more.
    _new_message = _ev.replace("1", message["one"]).replace("2", message["two"]).replace("3", message["three"]).replace("4", message["four"]).replace("5", message["five"]).replace("6", message["six"]).replace("7", message["seven"]).replace("8", message["eight"]).replace("9", message["nine"]).replace("a", message["a"]).replace("b", message["b"]).replace("c", message["c"]).replace("d", message["d"]).replace("e", message["e"]).replace("f", message["f"]).replace("g", message["g"]).replace("h", message["h"]).replace("i", message["i"]).replace("j", message["j"]).replace("k", message["l"]).replace("l", message["l"]).replace("m", message["m"]).replace("n", message["n"]).replace("o", message["o"]).replace("p", message["p"]).replace("q", message["q"]).replace("r", message["r"]).replace("s", message["s"]).replace("t", message["t"]).replace("u", message["u"]).replace("v", message["v"]).replace("w", message["w"]).replace("x", message["x"]).replace("y", message["y"]).replace("z", message["z"]).replace("A", message["_A"]).replace("B", message["_B"]).replace("C", message["_C"]).replace("D", message["_D"]).replace("E", message["_E"]).replace("F", message["_F"]).replace("G", message["_G"]).replace("H", message["_H"]).replace("I", message["_I"]).replace("J", message["_J"]).replace("K", message["_K"]).replace("L", message["_L"]).replace("M", message["_M"]).replace("N", message["_N"]).replace("O", message["_O"]).replace("P", message["_P"]).replace("Q", message["_Q"]).replace("R", message["_R"]).replace("S", message["_S"]).replace("T", message["_T"]).replace("U", message["_U"]).replace("V", message["_V"]).replace("W", message["_W"]).replace("X", message["_X"]).replace("Y", message["_Y"]).replace("Z", message["_Z"])

    # Replacing _password in order to obfuscate it.
    _new_password = _password.replace("a", a + " ").replace("b", b + " ").replace("c", c + " ").replace("d", d + " ").replace("e", e + " ").replace("f", f + " ").replace("g", g + " ").replace("h", h + " ").replace("i", i + " ").replace("j", j + " ").replace("k", k + " ").replace("l", l + " ").replace("m", m + " ").replace("n", n + " ").replace("o", o + " ").replace("p", p + " ").replace("q", q + " ").replace("r", r + " ").replace("s", s + " ").replace("t", t + " ").replace("u", u + " ").replace("v", v + " ").replace("w", w + " ").replace("x", x + " ").replace("y", y + " ").replace("z", z + " ").replace("A", a + ".7").replace("B", b + ".7").replace("C", c + ".7").replace("D", d + ".7").replace("E", e + ".7").replace("F", f + ".7").replace("G", g + ".7").replace("H", h + ".7").replace("I", i + ".7").replace("J", j + ".7").replace("K", k + ".7").replace("L", l + ".7").replace("M", m + ".7").replace("N", n + ".7").replace("O", o + ".7").replace("P", p + ".7").replace("Q", q + ".7").replace("R", r + ".7").replace("S", s + ".7").replace("T", t + ".7").replace("U", u + ".7").replace("V", v + ".7").replace("W", w + ".7").replace("X", x + ".7").replace("Y", y + ".7").replace("Z", z + ".7").replace("@", one).replace("#", two).replace("$", three).replace("&", four).replace("*", five).replace("-", six).replace("=", seven).replace("(", eight).replace(")", nine).replace("!", ten).replace('"', eleven).replace("'", twelve).replace(":", thirteen).replace(";", nine).replace("/", ten).replace("?", eleven).replace(",", twelve).replace("¡", thirteen).replace("<", fourteen).replace(">", fifteen).replace("¢", sixteen).replace("|", seventeen).replace("¿", eighteen).replace("©", nineteen).replace("®", twenty).replace("+", twenty_one).replace("±", twenty_two).replace("{", twenty_three).replace("}", twenty_four).replace("[", twenty_five).replace("]", twenty_seven).replace("~", twenty_eight).replace("÷", twenty_nine).replace("•", thirty).replace("°", thirty_one).replace("`", thirty_two).replace("´", thirty_four).replace("¥", thirty_five).replace("£", thirty_six).replace("€", thirty_seven).replace("1", "/999/").replace("2", "/888/").replace("3", "/777/").replace("4", "/666/").replace("5", "/555/").replace("6", "/444/").replace("7", "/333/").replace("8", "/222/").replace("9", "/111/")

    # Splitting _new_password.
    first_part = _new_password[:len(_new_password)//2]
    second_part = _new_password[len(_new_password)//2]
    third_part = _new_password[len(_new_password)//2]
    fourth_part = _new_password[len(_new_password)//2]
    fifth_part = _new_password[len(_new_password)//2:]
    _password_split_1 = "/01/" + first_part + "/01/"
    _password_split_2 = "/02/" + second_part + "/02/"
    _password_split_3 = "/03/" + third_part + "/03/"
    _password_split_4 = "/04/" + fourth_part + "/04/"
    _password_split_5 = "/05/" + fifth_part + "/05/"
    _password_id = random.randrange(500, 1500)
    _new_password_id = str(_password_id).replace("1", "3").replace("2", "9").replace("3", "8").replace("4", "6").replace("5", "4").replace("6", "2").replace("7", "1").replace("8", "0").replace("9", "5").replace("0", "7")
    os.system("clear")
    input("Please write down: " + str(_password_id) + " - Once saved, press enter.")

    # Joining _password_split(s) to data segments after splitting.
    d1 = str(data_seg_1).join(_password_split_1)
    d2 = str(data_seg_2).join(_password_split_2)
    d3 = str(data_seg_3).join(_password_split_3)
    d4 = str(data_seg_4).join(_password_split_4)
    d5 = str(data_seg_5).join(_password_split_5)
    d6 = str(data_seg_6).join(_new_password_id)
    
  elif duwap == False:
    _new_message = _ev.replace("1", message["one"]).replace("2", message["two"]).replace("3", message["three"]).replace("4", message["four"]).replace("5", message["five"]).replace("6", message["six"]).replace("7", message["seven"]).replace("8", message["eight"]).replace("9", message["nine"]).replace("a", message["a"]).replace("b", message["b"]).replace("c", message["c"]).replace("d", message["d"]).replace("e", message["e"]).replace("f", message["f"]).replace("g", message["g"]).replace("h", message["h"]).replace("i", message["i"]).replace("j", message["j"]).replace("k", message["l"]).replace("l", message["l"]).replace("m", message["m"]).replace("n", message["n"]).replace("o", message["o"]).replace("p", message["p"]).replace("q", message["q"]).replace("r", message["r"]).replace("s", message["s"]).replace("t", message["t"]).replace("u", message["u"]).replace("v", message["v"]).replace("w", message["w"]).replace("x", message["x"]).replace("y", message["y"]).replace("z", message["z"]).replace("A", message["_A"]).replace("B", message["_B"]).replace("C", message["_C"]).replace("D", message["_D"]).replace("E", message["_E"]).replace("F", message["_F"]).replace("G", message["_G"]).replace("H", message["_H"]).replace("I", message["_I"]).replace("J", message["_J"]).replace("K", message["_K"]).replace("L", message["_L"]).replace("M", message["_M"]).replace("N", message["_N"]).replace("O", message["_O"]).replace("P", message["_P"]).replace("Q", message["_Q"]).replace("R", message["_R"]).replace("S", message["_S"]).replace("T", message["_T"]).replace("U", message["_U"]).replace("V", message["_V"]).replace("W", message["_W"]).replace("X", message["_X"]).replace("Y", message["_Y"]).replace("Z", message["_Z"])

  # Split _new_message into 5 parts.
  sixth_part = _new_message[:len(_new_message)//2]
  seventh_part = _new_message[len(_new_message)//2]
  eighth_part = _new_message[len(_new_message)//2]
  ninth_part = _new_message[len(_new_message)//2]
  tenth_part = _new_message[len(_new_message)//2:]
  _new_message_join_1 = " ------start------ " + sixth_part + " ------end------ "
  _new_message_join_2 = " -------start------- " + seventh_part + " -------end------- "
  _new_message_join_3 = " --------start-------- " + eighth_part + " --------end-------- "
  _new_message_join_4 = " ---------start--------- " + ninth_part + " ---------end---------"
  _new_message_join_5 = " ----------start---------- " + tenth_part + " ----------end----------"
  
  # d7 is the obfuscated message data.
  d7 = str(data_seg_7).join(_new_message_join_1 + str(random.randbytes(50)) + numbers + _new_message_join_2 + str(random.randbytes(100)) + _new_message_join_3 + numbers + str(random.randbytes(150)) + _new_message_join_4 + numbers + str(random.randbytes(200)) + _new_message_join_5 + str(random.randbytes(250)) + numbers + str(random.randbytes(300)) + str(random.randbytes(350)) + str(random.randbytes(400)) + str(random.randbytes(450)) + str(random.randbytes(500)))
  if os.path.isfile(os.getcwd() + "/data.txt") == True:
    os.system("clear")
    dfep = input("An encrypted file already exists, do you want to replace it? (y) or (n): ")
    if dfep == "y":
      os.system("clear")
      open(os.getcwd() + "/data.txt", "w")
      with open(os.getcwd() + "/data.txt", 'w') as file:
        if duwap == True:
          file.write(d1 + d2 + d3 + d4 + d5 + d6 + d7)
        elif duwap == False:
          file.write(d7)
          os.system("clear")
      if os.path.isfile(os.getcwd() + "/data.txt") == True:
            print("Encrypted file created at: " + os.getcwd() + "/data.txt")
      elif os.path.isfile(os.getcwd() + "/data.txt") == False:
        os.system("clear")
        _time = 5
        while time != 5:
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
        while time != 1:
          print("Please do not add file extensions—returning in [" + str(_time) + "].")
          time.sleep(1)
          os.system("clear")
          _time -= 1
        else:
          return encrypt()
      elif "." not in name:
        open(os.getcwd() + "/" + name + ".txt", "x")
        with open(os.getcwd() + name + ".", 'w') as file:
          if duwap == True:
            file.write(d1 + d2 + d3 + d4 + d5 + d6 + d7)
            os.system("clear")
          if duwap == False:
            file.write(d7)
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
  if os.path.isfile(os.getcwd() + "/data.txt") == False:
    open(os.getcwd() + "/data.txt", "x")
    with open(os.getcwd() + "/data.txt", 'w') as file:
      if duwap == True:
        file.write(d1 + d2 + d3 + d4 + d5 + d6 + d7)
      else:
        file.write(d7)
      os.system("clear")
      if os.path.isfile(os.getcwd() + "/data.txt") == True:
        print("Encrypted file created at: " + os.getcwd() + "/data.txt")
      elif os.path.isfile(os.getcwd() + "/data.txt") == False:
        os.system("clear")
        _time = 5
        while time != 1:
          print("There was an error creating your file—returning in [" + str(_time) + "].")
          os.system("clear")
          _time -= 1
        else:
          return encrypt()