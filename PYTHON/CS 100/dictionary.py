# This program demonstrates an advanced usage of dictionaies
# It creates a list of dictionaries containing employee information
# and then prints out all the records.
# In class, we will be modifying this program to act as a "database"
# of sorts.
#
# Author: D. Palmer
#
# Date: November 28, 2022

import random

names = ["albert", "bianca", "chester", "dalia", "eugene", "fiona",
         "gilbert", "hermione", "idris", "jullietta", "kincade",
         "lipita", "manan", "naomi", "otto", "petunia", "quincy",
         "rosalita", "sean", "tyra", "uri", "viola", "walter", "xiao",
         "yul", "zendaya"]

employees = []
# create employee "database"
for name in names:
    age = random.randint(18,85)
    seniority = random.randint(0,3)
    record = {"name": name,
              "age": age,
              "seniority": seniority
              }
    employees.append(record)
    
#display all the employees"   
for record in employees:
    print(record)

print()
print("Task #1")
# Code to print out all employees with a seniority of 3
for record in employees:
    if record["seniority"] == 3:
        print(record)

#Code to print out all the employees whose names are 6 characters or more        
print()
print("Task #2")
count=0
for record in employees:
    if len(record["name"])>=6:
        print(record)
    
        
#Code to print out all the employees with a seniority of 2 or 3 who are more than 25 years old        
print()
print("Task #3")
for record in employees:
    if record["age"]>25:
        if record["seniority"]==2 or record["seniority"]==3:
            print(record)
        
        

#Code to print out all the employees who:
        # do not have a seniority of 1
        # have names that are 4 characters or fewer
print()
print("Task #4")
for record in employees:
    if len(record["name"])<=4 and record["seniority"]!=1:
        print(record)
        

#Code to print out all the employees who:
        # do have a seniority of 0 or 3
        # have names that are exactly 5 characters long
print()
print("Task #5")
for record in employees:
    if (record["seniority"]==0 or record["seniority"]==3) and len(record["name"])==5:
        print(record)
        
#Code to count how many employees who:
        # have a seniority of 1
        # -OR-
        # have are between 30 and 60 (inclusive)
print()
print("Task #6")
for record in employees:
    count=count+1
    if record["seniority"]==1 or 30<=record["age"]<=60:
        count+=1
print(count)
        

#Code to print how many employees who:
        # have a seniority of 1 or 3
        # are less than 20 or older than 55
        # have names that are between 4 and 7 characters inclusive
print()
print("Task #7")
for record in employees:
    if (record["seniority"]==1 or record["seniority"]==3) and (record["age"]<20 or record["age"]>55) and (4<=len(record["name"])<=7):
        print(record)


#Code to change all employees who have a seniority of 1 to
        # a seniority of 2
print()
print("Task #8")
for record in employees:
    if record["seniority"]==1:
        record["seniority"]=2
        print(record)


        
        
