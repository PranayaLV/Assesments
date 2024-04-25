# -*- coding: utf-8 -*-
"""LVADSUSR_python_IA1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xsd0QQk1HEEGsdI83Ts7MnvNuAO9YPt0
"""

#1
len = int(input("Enter Length of the Area: "))
wid = int(input("Enter width of the Area: "))

size = "large"
area = len*wid
if area < 2000:
  size = "medium"
elif area<1000:
  size = "small"
print(f"Area is: {area} and size is {size}")

#2

h = float(input("Enter Height in M: "))
w = float(input("Enter Weight in Kg: "))

size = "large"
diet_plan = ""
fitness_plan = ""
bmi = w/h**2
print(bmi)
if bmi < 20:
  diet_plan = "Protein plan"
  fitness_plan = "weights"
elif bmi<30:
  diet_plan = "normal"
  fitness_plan = "normal"
else:
  diet_plan = "veggies"
  fitness_plan = "shred"
print(f"BMI is: {bmi} and diet plan is {diet_plan} and fitness plan is {fitness_plan}")

# 3
grades = {
    'roll1': {
        'math': 8,
        'science': 7,
        'english': 9
    } ,
    'roll2': {
        'math': 6,
        'science': 7,
        'english': 8
    },
    'roll3': {
        'math': 6,
        'science': 10,
        'english': 8
    }
}

def update_grade(roll , subject , new_score):
  grades[roll][subject] = new_score
  return grades
def get_score(roll , subject):
  return grades[roll][subject]
def add_student(roll, subjects):
  grades[roll] = subjects
  return grades
def print_student_Rec(roll):
  for key , value in grades[roll].items():
    print("Subject: ", key , "Grade: ", value)


print("Update grade",update_grade('roll1','math',10))
print("Score: ", get_score('roll2','english'))
print("add student", add_student('roll5' , {'math': 6,
        'science': 10,
        'english': 8}))
print_student_Rec('roll1')

#4
age = int(input("Age: "))

category = "sr citizen"
if age<12:
  category = "Child"

elif age<20:
  category = "teen"
elif age<55:
  category = "adult"

print("Your category is: ", category)

#5
sub_ids = [1,2,3,4,5,7,23,44,45,46,50]
target_ids = []
for i in sub_ids:
  if i % 2 == 0:
    target_ids.append(i)
print(target_ids)

#6
password = "gta654*"

while True:
  entered = input("Enter password: ")
  if entered == password:
    print("Logged in succesfully")
    break
  else:
    print("Wrong password, try again")

#7

import math
feedback_scores = {
    'customer_service' : [2,3,4,2,3,1,1,2,3],
    'hygeine' : [3,4,1,0,1,1,2,3,3],
    'quality_product' : [4,5,4,5,4,4,3,5,4] ,
    'pricing': [3,4,2,3,5,4,3,5,4]
}
new_dict = {}
for key , value in feedback_scores.items():
  new_dict[key] = int(sum(value) /9 )
print(new_dict)
print("Best kpi: Product Quality")
print("Improvement required on customer service and hygeine")

#8
vow = ['a','e','i','o','u']
def vowel(s):
  c = 0
  for i in s:
    if i in vow:
      c= c+1
  return c
vowel("hello world it is nice")

9
import datetime

now = datetime.datetime.now()
date_ = datetime.datetime.date(2024/4/22)
while True:
  if date_ == now:
    print("ALERT:", )
    break

#10
try:
  amount = float(input("Enter amount to put in savings account: "))
  print("Amount is: ", amount)

except ValueError:
  print("Enter correct number")

#11
try:
  num = int(input("Enter account number: "))
  print("ACC is: ", num)

except ValueError:
  print("Enter correct number")

#12
def add(a,b):
  if isinstance(a,float) and isinstance(b,float):
    return a+b
  else:
    return "wrong values"
def sub(a,b):
  if isinstance(a,float) and isinstance(b,float):
    return a-b
  else:
    return "wrong values"
def mult(a,b):
  if isinstance(a,float) and isinstance(b,float):
    return a*b
  else:
    return "wrong values"
def div(a,b):
  try:
    print(a/b)
  except ZeroDivisionError:
    print("Cant divide by zero")
div(5,0)

#13
with open('/content/test.txt','w') as my_f:
  hours = 8
  h = "today hours = " + str(8)
  my_f.write(h)
with open('/content/test.txt','r') as my_r:
  print(my_r.read())

#14
with open('/content/test.txt','r') as my_r:
  print(my_r.read())

#15
with open('/content/test.txt','a') as my_a:
  now = datetime.datetime.now()
  h = f'\nNews is all good, sensex is all time high, date is {now}'
  my_a.write(h)
with open('/content/test.txt','r') as my_r:
  print(my_r.read())
