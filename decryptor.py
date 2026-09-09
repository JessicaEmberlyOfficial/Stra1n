import os
import random
import time
import configparser
import sys

def decrypt():
  
  # Setup config parser.
  config = configparser.ConfigParser()
  config.read(os.getcwd() + "/Stra1n.ini")
  alphabet = config["Alphabet"]
  symbols = config["Symbols"]
  bytes = config["Bytes"]
  numbers = config["Numbers"]
  message = config["Message_In"]
  message_out = config["Message_Out"]
  pid = config["PID"]
  marker = config["Marker"]

  # Increase values by x.
  increase_values_by = numbers["increase_values_by"]

  # Booleans.
  isPath = False
  duwap = False
  
  # Strings
  _password_id = ""
  _password = ""
  dv = ""

  # Message Detection Points.
  start = str(marker["marking_symbol"])
  end = str(marker["marking_symbol"])
  
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
  
  os.system("clear")
  _out = input("What do I decrypt? (e.g. data.txt): ")
  if os.path.isfile(os.getcwd() + "/" + _out) == True:
    isPath = True
    duwap = True
  else:
    os.system("clear")
    _time = 5
    while _time != 1:
      print("Invalid file—exiting in [" + str(_time) + "].")
      time.sleep(1)
      _time -= 1
      os.system("clear")
    else:
      sys.exit()
  os.system("clear")
  diuap = input("Did I use a password? (y) or (n): ")
  os.system("clear")
  if diuap == "y" and isPath == True:
    os.system("clear")
    _pid = input("What is your password id?: ")
    if len(_pid) > 2:
      _password_id = _pid
    else:
      os.system("clear")
      _time = 5
      while _time != 1:
        print("Invalid PID—deleting file in [" + str(_time) + "].")
        time.sleep(1)
        os.system("clear")
        _time -= 1
      else:
        os.system("rm " + os.getcwd() + "/" + _out)
        os.system("clear")
        sys.exit("File deleted. :(")
    os.system("clear")
    password = input("What password did I use?: ")
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
        return decrypt()
  elif diuap == "n" and isPath == True:
      duwap = False

  _new_password = _password.replace("a", a + " ").replace("b", b + " ").replace("c", c + " ").replace("d", d + " ").replace("e", e + " ").replace("f", f + " ").replace("g", g + " ").replace("h", h + " ").replace("i", i + " ").replace("j", j + " ").replace("k", k + " ").replace("l", l + " ").replace("m", m + " ").replace("n", n + " ").replace("o", o + " ").replace("p", p + " ").replace("q", q + " ").replace("r", r + " ").replace("s", s + " ").replace("t", t + " ").replace("u", u + " ").replace("v", v + " ").replace("w", w + " ").replace("x", x + " ").replace("y", y + " ").replace("z", z + " ").replace("A", a + ".7").replace("B", b + ".7").replace("C", c + ".7").replace("D", d + ".7").replace("E", e + ".7").replace("F", f + ".7").replace("G", g + ".7").replace("H", h + ".7").replace("I", i + ".7").replace("J", j + ".7").replace("K", k + ".7").replace("L", l + ".7").replace("M", m + ".7").replace("N", n + ".7").replace("O", o + ".7").replace("P", p + ".7").replace("Q", q + ".7").replace("R", r + ".7").replace("S", s + ".7").replace("T", t + ".7").replace("U", u + ".7").replace("V", v + ".7").replace("W", w + ".7").replace("X", x + ".7").replace("Y", y + ".7").replace("Z", z + ".7").replace("@", one).replace("#", two).replace("$", three).replace("&", four).replace("*", five).replace("-", six).replace("=", seven).replace("(", eight).replace(")", nine).replace("!", ten).replace('"', eleven).replace("'", twelve).replace(":", thirteen).replace(";", nine).replace("/", ten).replace("?", eleven).replace(",", twelve).replace("¡", thirteen).replace("<", fourteen).replace(">", fifteen).replace("¢", sixteen).replace("|", seventeen).replace("¿", eighteen).replace("©", nineteen).replace("®", twenty).replace("+", twenty_one).replace("±", twenty_two).replace("{", twenty_three).replace("}", twenty_four).replace("[", twenty_five).replace("]", twenty_seven).replace("~", twenty_eight).replace("÷", twenty_nine).replace("•", thirty).replace("°", thirty_one).replace("`", thirty_two).replace("´", thirty_four).replace("¥", thirty_five).replace("£", thirty_six).replace("€", thirty_seven).replace("1", "/999/").replace("2", "/888/").replace("3", "/777/").replace("4", "/666/").replace("5", "/555/").replace("6", "/444/").replace("7", "/333/").replace("8", "/222/").replace("9", "/111/")
    
  _new_password_id = _password_id.replace("0", pid["zero"]).replace("1", pid["one"]).replace("2", pid["two"]).replace("3", pid["three"]).replace("4", pid["four"]).replace("5", pid["five"]).replace("6", pid["six"]).replace("7", pid["seven"]).replace("8", pid["eight"]).replace("9", pid["nine"])

  file = open(os.getcwd() + "/" + _out)
  contents = file.read()
  ip = contents.find(start)
  ep = contents.find(end, ip + len(start))
  
  os.system("clear")
  if os.path.isfile(os.getcwd() + "/" + _out) == True:
    with open(os.getcwd() + "/" + _out, "r") as file:
      content = file.read()
      if duwap == True:
        if _new_password_id in content:
          if _new_password in content:
            if ip != -1 and ep != -1:
              _message = content[ip + len(marker["marking_symbol"]):ep]
              _new_message = _message.replace.replace(message["a"], message_out["a"]).replace(message["b"], message_out["b"]).replace(message["c"], message_out["c"]).replace(message["d"], message_out["d"]).replace(message["e"], message_out["e"]).replace(message["f"], message_out["f"]).replace(message["g"], message_out["g"]).replace(message["h"], message_out["h"]).replace(message["i"], message_out["i"]).replace(message["j"], message_out["j"]).replace(message["k"], message_out["k"]).replace(message["l"], message_out["l"]).replace(message["m"], message_out["m"]).replace(message["n"], message_out["n"]).replace(message["o"], message_out["o"]).replace(message["p"], message_out["p"]).replace(message["q"], message_out["q"]).replace(message["r"], message_out["r"]).replace(message["s"], message_out["s"]).replace(message["t"], message_out["t"]).replace(message["u"], message_out["u"]).replace(message["v"], message_out["v"]).replace(message["w"], message_out["w"]).replace(message["x"], message_out["x"]).replace(message["y"], message_out["y"]).replace(message["z"], message_out["z"]).replace(message["_A"], message_out["_A"]).replace(message["_B"], message_out["_B"]).replace(message["_C"], message_out["_C"]).replace(message["_D"], message_out["_D"]).replace(message["_E"], message_out["_E"]).replace(message["_F"], message_out["F"]).replace(message["_G"], message_out["_G"]).replace(message["_H"], message_out["_H"]).replace(message["_I"], message_out["_I"]).replace(message["_J"], message_out["_J"]).replace(message["_K"], message_out["_K"]).replace(message["_L"], message_out["_L"]).replace(message["_M"], message_out["_M"]).replace(message["_N"], message_out["_N"]).replace(message["_O"], message_out["_O"]).replace(message["_P"], message_out["_P"]).replace(message["_Q"], message_out["_Q"]).replace(message["_R"], message_out["_R"]).replace(message["_S"], message_out["_S"]).replace(message["_T"], message_out["_T"]).replace(message["_U"], message_out["_U"]).replace(message["_V"], message_out["_V"]).replace(message["_W"], message_out["_W"]).replace(message["_X"], message_out["_X"]).replace(message["_Y"], message_out["_Y"]).replace(message["_Z"], message_out["_Z"]).replace('"', "")
        else:
          os.system("clear")
          _time = 5
          while _time != 1:
            print("Invalid PID—deleting file in [" + str(_time) + "].")
            time.sleep(1)
            os.system("clear")
            _time -= 1
          else:
            os.system("rm " + os.getcwd() + "/" + _out)
            os.system("clear")
            sys.exit()
      else:
        if ip != -1 and ep != -1:
          _message = content[ip + len(marker["marking_symbol"]):ep]
          _new_message = _message.replace(message["a"], message_out["a"]).replace(message["b"], message_out["b"]).replace(message["c"], message_out["c"]).replace(message["d"], message_out["d"]).replace(message["e"], message_out["e"]).replace(message["f"], message_out["f"]).replace(message["g"], message_out["g"]).replace(message["h"], message_out["h"]).replace(message["i"], message_out["i"]).replace(message["j"], message_out["j"]).replace(message["k"], message_out["k"]).replace(message["l"], message_out["l"]).replace(message["m"], message_out["m"]).replace(message["n"], message_out["n"]).replace(message["o"], message_out["o"]).replace(message["p"], message_out["p"]).replace(message["q"], message_out["q"]).replace(message["r"], message_out["r"]).replace(message["s"], message_out["s"]).replace(message["t"], message_out["t"]).replace(message["u"], message_out["u"]).replace(message["v"], message_out["v"]).replace(message["w"], message_out["w"]).replace(message["x"], message_out["x"]).replace(message["y"], message_out["y"]).replace(message["z"], message_out["z"]).replace(message["_A"], message_out["_A"]).replace(message["_B"], message_out["_B"]).replace(message["_C"], message_out["_C"]).replace(message["_D"], message_out["_D"]).replace(message["_E"], message_out["_E"]).replace(message["_F"], message_out["F"]).replace(message["_G"], message_out["_G"]).replace(message["_H"], message_out["_H"]).replace(message["_I"], message_out["_I"]).replace(message["_J"], message_out["_J"]).replace(message["_K"], message_out["_K"]).replace(message["_L"], message_out["_L"]).replace(message["_M"], message_out["_M"]).replace(message["_N"], message_out["_N"]).replace(message["_O"], message_out["_O"]).replace(message["_P"], message_out["_P"]).replace(message["_Q"], message_out["_Q"]).replace(message["_R"], message_out["_R"]).replace(message["_S"], message_out["_S"]).replace(message["_T"], message_out["_T"]).replace(message["_U"], message_out["_U"]).replace(message["_V"], message_out["_V"]).replace(message["_W"], message_out["_W"]).replace(message["_X"], message_out["_X"]).replace(message["_Y"], message_out["_Y"]).replace(message["_Z"], message_out["_Z"]).replace('"', "")
          print(_new_message)
  elif os.path.isfile(os.getcwd() + "/" + _out) == False:
    os.system("clear")
    _time = 5
    while _time != 1:
      print("Invalid file—returning in [" + str(_time) + "].")
      os.system("clear")
      _time -= 1
    else:
      return decrypt()