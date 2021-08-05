import os
import shutil

path1 = input ("Please enter the file path (make sure it is a txt file): ")
name = input ("please enter your name: ")
date = input ("please enter today's date: ")
grade = input ("please enter your grade/class number: ")

path = open (path1,"a")
path.write("name date grade: ")
path.write ("{}  {}  {}\n".format(name, date, grade))
path.close()

print ("Yay! added the headers now you can submit it!!! 🤩 🤩 🤩")