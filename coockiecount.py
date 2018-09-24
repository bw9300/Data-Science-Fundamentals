#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 10:57:31 2018

@author: bob
"""

# Coockie values
calories = int(200)
fat = float(3.1)
carbs = float(3.4)
suger = float(22.3)

#ask question
coockiecount = input("How many coockies did you eat?: ")

# convert input to int for calculation
tot_coockies = float(coockiecount)

# Calculate total
tot_calories = calories * tot_coockies
tot_fat = fat * tot_coockies
tot_carbs = carbs * tot_coockies
tot_sugar = suger * tot_coockies


# Check if user is serious
check = input("Are you sure? y/n: ")

# if yes than show calculated values
if check == "y":
    #output
    print("total calories = " + str(tot_calories) + " || "
          "total fat = " + str(tot_fat) + " || "
          "total carbs = " + str(tot_carbs) + " || "
          "total sugar = " + str(tot_sugar) + " || "
          )

# if no than call the user a liar and quit
else:
    print("Liar!")


#if tot_calories > 800:
#    print("FATTY! Eat less")
#else:
#    print("Youre amazing!")
