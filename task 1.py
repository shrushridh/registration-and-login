

import csv

def register():
  with open("users.csv","a",newline="") as f:
    writer = csv.writer(f,delimiter=",")
    email = input("Please enter email: ")
    password = input("Please enter your password: ")
    password1 = input("Please Re-enter your password")
   
def validation(emaill):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
def isValid(email):
   if re.fullmatch(pat,email):
      print("valid email")
   else:
     print("invalid email")

     if password1==password:
      print("Password not match")
      if len(password)<5: 
        print("Password length too short or too long")
      if len(password)<16:
        print("Password length too short or too long")
        writer.writerow([email,password])
        print("Registration is successful ")
      else:
        print("Please try again")
  

def login():
    email = input("Please enter your email: ")
    password = input("please enter your password:")
    #with open("user.csv","r") as f:
   
    db = open("database.txt", "r")
    reader = csv.reader(f, delimiter=",")
    for row in reader:
          if row == [email,password]:
            print("Logged in")
            return True
          print("Please try again")
          return False
    else:
      print("please attempt login again")
