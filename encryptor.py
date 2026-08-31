import os
import random
import time

def encrypt():
  duwap = False
  
  _ev = ""
  _password = ""
  _replaced = ""

  data_seg_1 = random.randbytes(1000)
  data_seg_2 = random.randbytes(1000)
  data_seg_3 = random.randbytes(1000)
  data_seg_4 = random.randbytes(1000)
  data_seg_5 = random.randbytes(1000)
  data_seg_6 = random.randbytes(1000)

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

  at = "_"
  hashtag = "__"
  money = "___"
  percent = "____"
  _and = "_____"
  star = "______"
  dash = "_______"
  equals = "________"
  p_l = "_________"
  p_r = "__________"
  ep = "____________"
  qm = "______________"
  sqm = "_________________"
  colon = "___________________"
  semi_colon = "_________________"
  slash_r = "_______________________"
  question_mark = "____________________"
  period = "______________________________"
  comma = "_________________________________"
  
  duwap = False

  os.system("clear")
  _in = input("What do I encrypt?: ")
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
      print("Please make sure your password has 256 or more characters—returning in [5].")
      time.sleep(1)
      os.system("clear")
      print("Please make sure your password has 256 or more characters—returning in [4].")
      time.sleep(1)
      os.system("clear")
      print("Please make sure your password has 256 or more characters—returning in [4].")
      time.sleep(1)
      os.system("clear")
      print("Please make sure your password has 256 or more characters—returning in [3].")
      time.sleep(1)
      os.system("clear")
      print("Please make sure your password has 256 or more characters—returning in [2].")
      time.sleep(1)
      os.system("clear")
      print("Please make sure your password has 256 or more characters—returning in [1].")
      time.sleep(1)
      os.system("clear")
      return encrypt()
    elif diuap == "n":
      duwap = False
  dictionary = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"}

  table = str.maketrans(dictionary)

  ev = _in.translate(table)
  
  _ev = ev
  
  # Symbols (%50)
  if duwap == True:
    _new_message = _ev.replace("1", "99.01").replace("2", "88.01").replace("3", "77.01").replace("4", "66.01").replace("5", "55.01").replace("6", "44.01").replace("7", "33.01").replace("8", "22.01").replace("9", "11.01").replace("a", "00.01").replace("b", "99.02").replace("c", "88.02").replace("d", "77.02").replace("e", "66.02").replace("f", "55.02").replace("g", "44.02").replace("h", "33.02").replace("i", "22.02").replace("j", "11.02").replace("k", "00.02").replace("l", "99.03").replace("m", "88.03").replace("n", "77.03").replace("o", "66.03").replace("p", "55.03").replace("q", "44.03").replace("r", "33.03").replace("s", "22.03").replace("t", "11.03").replace("u", "00.03").replace("v", "99.04").replace("w", "88.04").replace("x", "77.04").replace("y", "66.04").replace("z", "55.04").replace("A", "44.04").replace("B", "33.04").replace("C", "22.04").replace("D", "11.04").replace("E", "00.04").replace("F", "9.05").replace("G", "88.05").replace("H", "77.05").replace("I", "66.05").replace("J", "55.05").replace("K", "44.05").replace("L", "33.05").replace("M", "22.05").replace("N", "11.05").replace("O", "00.05").replace("P", "99.06").replace("Q", "88.06").replace("R", "77.06").replace("S", "66.06").replace("T", "55.06").replace("U", "44.06").replace("V", "33.06").replace("W", "22.06").replace("X", "11.06").replace("Y", "00.06").replace("Z", "99.07")
    _new_password = _password.replace("a", a + " ").replace("b", b + " ").replace("c", c + " ").replace("d", d + " ").replace("e", e + " ").replace("f", f + " ").replace("g", g + " ").replace("h", h + " ").replace("i", i + " ").replace("j", j + " ").replace("k", k + " ").replace("l", l + " ").replace("m", m + " ").replace("n", n + " ").replace("o", o + " ").replace("p", p + " ").replace("q", q + " ").replace("r", r + " ").replace("s", s + " ").replace("t", t + " ").replace("u", u + " ").replace("v", v + " ").replace("w", w + " ").replace("x", x + " ").replace("y", y + " ").replace("z", z + " ").replace("A", a + ".7").replace("B", b + ".7").replace("C", c + ".7").replace("D", d + ".7").replace("E", e + ".7").replace("F", f + ".7").replace("G", g + ".7").replace("H", h + ".7").replace("I", i + ".7").replace("J", j + ".7").replace("K", k + ".7").replace("L", l + ".7").replace("M", m + ".7").replace("N", n + ".7").replace("O", o + ".7").replace("P", p + ".7").replace("Q", q + ".7").replace("R", r + ".7").replace("S", s + ".7").replace("T", t + ".7").replace("U", u + ".7").replace("V", v + ".7").replace("W", w + ".7").replace("X", x + ".7").replace("Y", y + ".7").replace("Z", z + ".7").replace("@", at).replace("#", hashtag).replace("$", money).replace("&", _and).replace("*", star).replace("-", dash).replace("=", equals).replace("(", p_l).replace(")", p_r).replace("!", ep).replace('"', qm).replace("'", sqm).replace(":", colon).replace(";", semi_colon).replace("/", slash_r).replace("?", question_mark).replace(",", comma).replace("1", " 9 ").replace("2", " 8 ").replace("3", " 7 ").replace("4", " 6 ").replace("5", " ..... ").replace("6", " 4 ").replace("7", " 3 ").replace("8", " 2 ").replace("9", " 1 ")
    
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
    d1 = str(data_seg_1).join(_password_split_1)
    d2 = str(data_seg_2).join(_password_split_2)
    d3 = str(data_seg_3).join(_password_split_3)
    d4 = str(data_seg_4).join(_password_split_4)
    d5 = str(data_seg_5).join(_password_split_5)
  elif duwap == False:
    _new_message = _ev.replace("1","9.1").replace("2", "8.1").replace("3", "7.1").replace("4", "6.1").replace("5", "5.1").replace("6", "4.1").replace("7","3.1").replace("8", "2.1").replace("9", "1.1").replace("a", "0.1").replace("b", "9.2").replace("c", "8.2").replace("d", "7.2").replace("e", "6.2").replace("f", "5.2").replace("g", "4.2").replace("h", "3.2").replace("i", "2.2").replace("j", "1.2").replace("k", "0.2").replace("l", "9.3").replace("m", "8.3").replace("n", "7.3").replace("o", "6.3").replace("p", "5.3").replace("q", "4.3").replace("r", "3.3").replace("s", "2.3").replace("t", "1.3").replace("u", "0.3").replace("v", "9.4").replace("w", "8.4").replace("x", "7.4").replace("y", "6.4").replace("z", "5.4").replace("A", "4.4").replace("B", "3.4").replace("C", "2.4").replace("D", "1.4").replace("E", "0.4").replace("F", "9.5").replace("G", "8.5").replace("H", "7.5").replace("I", "6.5").replace("J", "5.5").replace("K", "4.5").replace("L", "3.5").replace("M", "2.5").replace("N", "1.5").replace("O", "0.5").replace("P", "9.6").replace("Q", "8.6").replace("R", "7.6").replace("S", "6.6").replace("T", "5.6").replace("U", "4.6").replace("V", "3.6").replace("W", "2.6").replace("X", "1.6").replace("Y", "0.6").replace("Z", "9.7")
    
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
  d6 = str(data_seg_6).join(_new_message_join_1 + str(random.randbytes(50)) + _new_message_join_2 + str(random.randbytes(100)) + _new_message_join_3 + str(random.randbytes(150)) + _new_message_join_4 + str(random.randbytes(200)) + _new_message_join_5 + str(random.randbytes(250)))
  if os.path.isfile(os.getcwd() + "/data.txt") == True:
    os.system("clear")
    dfep = input("An encrypted file already exists, do you want to replace it? (y) or (n): ")
    if dfep == "y":
      os.system("clear")
      name = input("Please enter a new name for your new file? (e.g. Stra1n): ")
      if "." in name:
        os.system("clear")
        print("Please do not add file extensions—returning in [5].")
        time.sleep(1)
        os.system("clear")
        print("Please do not add file extensions—returning in [4].")
        time.sleep(1)
        os.system("clear")
        print("Please do not add file extensions—returning in [3].")
        time.sleep(1)
        os.system("clear")
        print("Please do not add file extensions—returning in [2].")
        time.sleep(1)
        os.system("clear")
        print("Please do not add file extensions—returning in [1].")
        time.sleep(1)
        os.system("clear")
        return encrypt()
      elif "." not in name:
        open(os.getcwd() + "/" + name + ".txt", "x")
        with open(os.getcwd() + name + ".", 'w') as file:
          if duwap == True:
            file.write(d1 + d2 + d3 + d4 + d5 + d6)
            os.system("clear")
          elif duwap == False:
            file.write(d6)
            os.system("clear")
            print("np")
          if os.path.isfile(os.getcwd() + name + ".txt") == True:
            print("Encrypted file created at: " + os.getcwd() + "/data.txt")
          elif os.path.isfile(os.getcwd() + name + ".txt") == False:
            os.system("clear")
            print("There was an error creating your file—returning in [5].")
            time.sleep(1)
            os.system("clear")
            print("There was an error creating your file—returning in [4].")
            time.sleep(1)
            os.system("clear")
            print("There was an error creating your file—returning in [3].")
            time.sleep(1)
            os.system("clear")
            print("There was an error creating your file—returning in [2].")
            time.sleep(1)
            os.system("clear")
            print("There was an error creating your file—returning in [1].")
            time.sleep(1)
            os.system("clear")
            return encrypt()
        if os.path.isfile(os.getcwd() + name + ".txt") == True:
          print("Encrypted file created at: " + " + os.getcwd() + /" + name + ".txt")
        if os.path.isfile(os.getcwd() + name + ".txt") == False:
          os.system("clear")
          print("There was an error creating your file—returning in [5].")
          time.sleep(1)
          os.system("clear")
          print("There was an error creating your file—returning in [4].")
          time.sleep(1)
          os.system("clear")
          print("There was an error creating your file—returning in [3].")
          time.sleep(1)
          os.system("clear")
          print("There was an error creating your file—returning in [2].")
          time.sleep(1)
          os.system("clear")
          print("There was an error creating your file—returning in [1].")
          time.sleep(1)
          os.system("clear")
          return encrypt()
    elif dfep == "n":
      os.system("clear")
      print("Exiting in [5].")
      time.sleep(1)
      os.system("clear")
      print("Exiting in [4].")
      time.sleep(1)
      os.system("clear")
      print("Exiting in [3].")
      time.sleep(1)
      os.system("clear")
      print("Exiting in [2].")
      time.sleep(1)
      os.system("clear")
      print("Exiting in [1].")
      time.sleep(1)
      os.system("clear")
      os.system("exit")
  elif os.path.isfile(os.getcwd() + "/data.txt") == False:
    open(os.getcwd() + "/data.txt", "x")
    with open(os.getcwd() + "/data.txt", 'w') as file:
      if duwap == True:
        file.write(d1 + d2 + d3 + d4 + d5 + d6)
      else:
        file.write(d6)
      os.system("clear")
      if os.path.isfile(os.getcwd() + "/data.txt") == True:
        print("Encrypted file created at: " + os.getcwd() + "/data.txt")
      elif os.path.isfile(os.getcwd() + "/data.txt") == False:
        os.system("clear")
        print("There was an error creating your file—returning in [5].")
        time.sleep(1)
        os.system("clear")
        print("There was an error creating your file—returning in [4].")
        time.sleep(1)
        os.system("clear")
        print("There was an error creating your file—returning in [3].")
        time.sleep(1)
        os.system("clear")
        print("There was an error creating your file—returning in [2].")
        time.sleep(1)
        os.system("clear")
        print("There was an error creating your file—returning in [1].")
        time.sleep(1)
        os.system("clear")
        return encrypt()