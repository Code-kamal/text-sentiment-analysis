# import matplotlib.pyplot as plt
import string
import sys
import time
import datetime as dt
from csv import excel_tab
import random as rnd
import numpy as np

# grades = [10, 11 , 11, 12,14, 15, 16, 17, 18, 19, 19,19, 20]

# plt.hist(grades, 30)
# plt.show()

example_list = [1, 2, 3, 4]
# example_tuple = (1, 2, 3, 4)
# print(id(example_list))
# print(id(example_tuple))
# example_list2 = example_list.copy()
# example_list2[1] = 5
# example_list[1] = 2
# print(example_list)
# print(example_list2)
# my_list:tuple = 1, 2, 3, 4
# print(my_list)
# print(type(my_list))
# iterable = iter(my_list)
# print(iterable)
# print(next(iterable))
# print(id(my_list[0]))
# variable:int = 1
# print(id(variable))
# variable += 1
# print(id(variable))
# string:str = "hello"
# print(id(string))
# string[0] = 'a'
# print(id(string))
# Project One
#import random as rnd
#random_number = rnd.randint(1, 100)
#while True:
#    try:
#        guess:int = int(input("Enter a number: "))
#        if guess == random_number:
#            print("You found the number!")
#            break
#        elif guess > random_number:
#            print("Guessed high!")
#        else:print("Guessed low!")
#     except ValueError:
#         print("Please enter a number!")
#import string as st
#import random as rnd
#def create_strong_password(length = 8):
#    if length <= 0:
#        raise ValueError("Password length must be greater than 0")
#    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
#    chars += "*&^%$#@!"
#    password:str = "".join(rnd.choice(chars) for _ in range(length))
#    return password

#while True:
#    try:
#        length:int = int(input("How many characters would you like to be your password? "))
#        print(create_strong_password(length))
#        break

#    except ValueError:
#        print("Please enter a number")

#from datetime import datetime as dt
#now = dt.now()
#print(now.month)


# Learning Python
# data = np.array([1, 2, 3, 4])
# import numpy as np # with this line of code you can use numpy and name it np
# np.array([1, 2, 3]) # with this line of code you can create an array with just a type like just int or just string
# np.array([1, 2, 3.12]) # if you write this code your array will become all float and you have a float array type
# np.array([1, 2.14, "amir"]) # it will become a string array
# np.zeros(4) # it will create an array with just zero elements and length 4
# np.ones(3) # it will create an array with just one elements and length 3
# np.random.random(3) # it will create an array with just random elements between 0 and 1 with length 3
# np.array([1, 2, 3]) + np.array([4, 5, 6]) # it will summand these two array and it will become [5, 7, 8] you can not summand two array with different lengths
# for more you can minus(-) and multiply(*) and divide(/) array as well
# np.array([1, 2, 3, 4, 5, 6]) * 2 # 2 multiply in every elements and it will become [2, 4, 6, 8, 10, 12] and you can this method with (/) and (+) and (-)
# sum(np.array([1, 2, 3, 4, 5, 6])) and min(np.array([1, 2, 3, 4, 5, 6])) and max(np.array([1, 2, 3, 4, 5, 6])) and len(np.array([1, 2, 3, 4, 5, 6])) and you can also do this data.sum(), data.max(), data.min() but can not do this data.len()
# and also can data.mean() for average data.prod() for multiply all of the elements
# type(data), data.dtype # with the first one you can find out type of your data and that is numpy.ndarray and with second one you can find out type your elements of data
# data[1] # it returns the second element of your numpy array
# data[0:2] # you can slice your numpy array as well
# data[1:3] = 4, 5 # you can modify your numpy array and also data[2] = 3
# select = [2, 5, 8]
# data[select] # this is a trick that you can return any elements that you want and also you can modify too for example data[select] = 65
# data.size # you can return the size of you numpy array
# data.ndim # you can return the dimensional of your numpy array
# data.shape # you can return the shape of you numpy array for example if your numpy array is a matrix it will return the number of rows and number of columns
# data.mean() or np.mean(data) # you can find out the average of your numpy array
# data.max() or np.max(data), data.min() or np.min(data) # you can find the minimum and maximum of your numpy array
# data = np.array([[1, 2, 3], [4, 5, 6]])
# v = np.array([1, 0]), u = np.array([0, 1]), z= u+v
# you can plus a two dimensional numpy array with one dimensional numpy array but if rows or columns have to same.
# np.arange(0, 10, 2) # that returns a array like this [0, 2, 4, 6, 8]
# np.linspace(1, 5, 5) # that returns a array like this [1. 2. 3. 4. 5.]
# you can get mean, max, min, std and other things like one dimentional array
# data.max(axis=0) # it ignores the first parameter and find maximum in other dimension for example if your matrix is 3*2 it ignores 3 and find maximum in columns
# data.max(axis=1) # like the below one
# data.T # transpose your matrix # ماتریس ترانهاده
# data.reshape(6) # it shape your matrix into a one dimensional with six elements and you can also a one dimensional array into two dimensional with np.reshape(2, 3)
# the most important point in numpy is vectorization until you can't do something without vectorization do not use other things because it is very faster than you think the other name of it is bradcastiong
# for example if you have a matrix and want to plus every element with 5 just write matrix + 5 and don't use for each element
# and other method is faster most times for example sum method is faster

import numpy as np
import matplotlib.pyplot as plt


# 1. تعریف تابع
# def f(w0, w1):
#     return w0 ** 2 + 2 * w1 ** 2


# 2. تنظیمات اولیه الگوریتم (دقیقا مثل مثال قبل)
# w0, w1 = 10.0, 10.0
# alpha = 0.1
# epochs = 50

# لیست‌هایی برای ذخیره مسیر حرکت
# w0_history = [w0]
# w1_history = [w1]

# 3. اجرای گرادیان کاهشی و ذخیره نقاط
# for i in range(epochs):
#    dw0 = 2 * w0
#    dw1 = 4 * w1

#    w0 = w0 - (alpha * dw0)
#   w1 = w1 - (alpha * dw1)

#    w0_history.append(w0)
#    w1_history.append(w1)

# 4. آماده‌سازی صفحه برای رسم (ایجاد شبکه‌ای از نقاط)
# w0_range = np.linspace(-12, 12, 100)
# w1_range = np.linspace(-12, 12, 100)
# W0, W1 = np.meshgrid(w0_range, w1_range)
# Z = f(W0, W1)

# 5. رسم شکل
# plt.figure(figsize=(8, 6))

# رسم خطوط تراز (نقشه توپوگرافی تابع)
# contour = plt.contour(W0, W1, Z, levels=30, cmap='viridis')
# plt.clabel(contour, inline=True, fontsize=8)

# رسم مسیر گرادیان کاهشی با رنگ قرمز
# plt.plot(w0_history, w1_history, 'ro-', label='Gradient Descent Path', markersize=4, linewidth=1.5)

# علامت گذاری نقطه مینیمم (0,0) با ستاره سبز
# plt.plot(0, 0, 'g*', markersize=15, label='Minimum (0,0)')

# تنظیمات ظاهری نمودار
# plt.title("Gradient Descent on $y = w_0^2 + 2w_1^2$")
# plt.xlabel("$w_0$")
# plt.ylabel("$w_1$")
# plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
# plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
# plt.legend()
# plt.grid(True)

# نمایش تصویر
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
#
# # ۱. تعریف یک تابع موج‌دار (غیرمحدب) شبیه به تصویر شما
# # از ترکیب سینوس و کسینوس برای ایجاد تپه‌ها و دره‌ها استفاده می‌کنیم
# def J(w0, w1):
#     return 2 * np.cos(3 * np.pi * w0) * np.sin(3 * np.pi * w1) + (w0 ** 2 + w1 ** 2) * 0.1
#
#
# # ۲. محاسبه گرادیان (مشتقات جزئی) تابع بالا
# def grad_J(w0, w1):
#     dw0 = -6 * np.pi * np.sin(3 * np.pi * w0) * np.sin(3 * np.pi * w1) + 0.2 * w0
#     dw1 = 6 * np.pi * np.cos(3 * np.pi * w0) * np.cos(3 * np.pi * w1) + 0.2 * w1
#     return dw0, dw1
#
#
# # ۳. تابع اجرای گرادیان کاهشی
# def gradient_descent(start_w0, start_w1, learning_rate=0.01, epochs=15):
#     w0, w1 = start_w0, start_w1
#     history = [(w0, w1, J(w0, w1))]
#
#     for _ in range(epochs):
#         dw0, dw1 = grad_J(w0, w1)
#         w0 = w0 - (learning_rate * dw0)
#         w1 = w1 - (learning_rate * dw1)
#         history.append((w0, w1, J(w0, w1)))
#
#     return zip(*history)  # بازگرداندن مقادیر به صورت سه لیست جداگانه
#
#
# # ۴. آماده‌سازی داده‌ها برای رسم رویه (Surface)
# w0_range = np.linspace(0, 1, 100)
# w1_range = np.linspace(0, 1, 100)
# W0, W1 = np.meshgrid(w0_range, w1_range)
# Z = J(W0, W1)
#
# # اجرای الگوریتم از دو نقطه شروع متفاوت (مثل تصویر شما)
# # مسیر اول (سمت چپ): گیر افتادن در یک دره
# path1_w0, path1_w1, path1_z = gradient_descent(start_w0=0.3, start_w1=0.8, learning_rate=0.005, epochs=25)
#
# # مسیر دوم (سمت راست): حرکت در یک مسیر دیگر
# path2_w0, path2_w1, path2_z = gradient_descent(start_w0=0.8, start_w1=0.7, learning_rate=0.005, epochs=25)
#
# # ۵. رسم نمودارها
# fig = plt.figure(figsize=(14, 6))
#
# # ---- رسم تصویر سمت چپ ----
# ax1 = fig.add_subplot(121, projection='3d')
# # رسم سطح با رنگ‌بندی jet (آبی برای پایین، قرمز برای بالا) و کمی شفافیت (alpha)
# surf1 = ax1.plot_surface(W0, W1, Z, cmap='jet', alpha=0.7, edgecolor='none')
# # رسم مسیر با رنگ مشکی و علامت ستاره
# ax1.plot(path1_w0, path1_w1, path1_z, color='black', marker='*', markersize=10, linewidth=2, zorder=3)
# ax1.set_title("Path 1: Stuck in a Local Minimum")
# ax1.set_xlabel(r'$\omega_0$')
# ax1.set_ylabel(r'$\omega_1$')
# ax1.set_zlabel(r'$J(\omega_0, \omega_1)$')
#
# # ---- رسم تصویر سمت راست ----
# ax2 = fig.add_subplot(122, projection='3d')
# surf2 = ax2.plot_surface(W0, W1, Z, cmap='jet', alpha=0.7, edgecolor='none')
# ax2.plot(path2_w0, path2_w1, path2_z, color='black', marker='*', markersize=10, linewidth=2, zorder=3)
# ax2.set_title("Path 2: Different Start, Different Path")
# ax2.set_xlabel(r'$\omega_0$')
# ax2.set_ylabel(r'$\omega_1$')
# ax2.set_zlabel(r'$J(\omega_0, \omega_1)$')
#
# # تنظیم زاویه دید اولیه برای هر دو نمودار (تا شبیه عکس شما شود)
# ax1.view_init(elev=35, azim=45)
# ax2.view_init(elev=35, azim=45)
#
# plt.tight_layout()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# داده‌ها
# x = np.array([10,20,30,40,50,60,70,80])
# y = np.array([1.2,1.9,3.2,5.1,7.8,11.0,15.5,21.0])

# رسم نقاط
# plt.scatter(x, y, color='red')

# plt.xlabel("Temperature (°C)")
# plt.ylabel("Expansion (mm)")
# plt.title("Data Points")

# plt.show()

# KNN deep learning algorithm
import pandas as pd
import numpy as np
# import mglearn

# from sklearn.datasets import load_iris
# iris_dataset = load_iris()
# print(iris_dataset.keys())
# print(iris_dataset["data"].shape)
# print(iris_dataset["target_names"])
# print(iris_dataset["feature_names"])
# print(type(iris_dataset["data"]))
# print(iris_dataset["target"])

# from sklearn.model_selection import train_test_split
# X_train, X_test, Y_train, Y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0, test_size=0.2)
# iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset["feature_names"])
# print(iris_dataframe)
# pd.plotting.scatter_matrix(iris_dataframe, c=Y_train, figsize=(15, 15), marker='o', hist_kwds={"bins": 50}, s=60, alpha=0.8, cmap= mglearn.cm3)

# plt.show()

# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train, Y_train)
# x_new = np.array([[5, 2.9, 1, 0.2]])
# prediction = knn.predict(x_new)
# print("prediction: ", iris_dataset["target_names"][prediction])
# y_pred = knn.predict(X_test)

# learning sep method in print function
# print("2025", "07", "22", sep="/")
# print("2025", "07", "22", sep="-")

# learning end method in print function
# print("2025", "07", "22 ", sep="/", end="today")
# print("2025", "07", "22", sep="/", end="")

# age = input("What is your age?")
# print(age, end="")
# you can concatenate two strings
# print("Your age is " + age)
# print("hello \n \" \\")
"""
while True:
    height = input("Please Enter your height: (by meter) (if you want to exit enter one dot ")
    if height == '.':
        sys.exit("Program Ended")

    try:
        height = float(height)
        if height <= 0:
            print("Please enter a positive number")
        elif height > 3:
            print("Your height is too high")
        else:
            break
    except ValueError:
        print("Please enter a valid input")

while True:
    weight = input("Please Enter your weight: (by KG) (if you want to exit enter one dot ")
    if height == '.':
        sys.exit("Program Ended")

    try:
        weight = float(weight)
        if weight <= 0:
            print("Please enter a positive number")
        else:
            break
    except ValueError:
        print("Please enter a valid input")

BMI = (weight/(height**2))
print("Your BMI is: ", f"{BMI:.2f}")
if BMI >= 30:
    print("Obesity", end="")
elif 25 <= BMI < 30:
    print("Overweight", end="")
elif 18.5 <= BMI < 25:
    print("Healthy Weight", end="")
elif 0 < BMI < 18.5:
    print("Underweight", end="")
else:
    print("Invalid BMI", end="")  
"""

"""
year = dt.datetime.now().year
while True:
    year  = input("Please enter your year: (if you want to exit enter one dot) ")
    if year == '.':
        sys.exit("Program Ended")

    try:
        year = int(year)
        if year <= 0:
            print("Please enter a positive number")
        else:
            break
    except ValueError:
        print("Please enter a valid input")

if year%4 == 0 and (year%100 != 0 and year >= 100) or (year%400 == 0 and year >= 400):
    print("This year is a leap year", end="")
else :
    print("This year is a normal year", end="")
"""

"""
picks = ['r', 'p', 's']
while True:
    while True:
        your_pick = input("Please enter one of the following picks: (r, p, s) (if you want to exit enter one dot) ")
        if your_pick == '.':
            sys.exit("Program Ended")
        elif your_pick not in picks:
            print("Please enter a valid input")
        else:
            break

    machine_pick = rnd.choice(picks)
    if your_pick == machine_pick:
        print("DRAW", your_pick, machine_pick, sep="-")
    elif (your_pick == 'r' and machine_pick == 'p') or (your_pick == 'p' and machine_pick == 's') or (your_pick == 's' and machine_pick == 'r'):
        print("LOST", your_pick, machine_pick, sep="-")
    else:
        print("WON", your_pick, machine_pick, sep="-")
"""

# buying list management
"""
buy_list = []

while True:
    product = str(input("Please enter the product you want to buy: (If you want to exit write \"exit\") "))
    if product == "exit":
        break
    buy_list.append(product)

print(buy_list, end="")
"""

# extend method in lists
"""
list1 = ["Ali", "Sara"]
list2 = ["Reza", "Mina"]
list1.extend(list2)
print(list1, end="")
"""

# counting members of a list
"""
names = []
for i in range(0, 5):
    name = input("Please enter your name: ")
    names.append(name)

print(len(names), names[0], names[-1], end="")
"""

# finding a name in names list
"""
names = ['amir', 'ali', 'sara', 'zeinab', 'erfan', 'mahdi', 'hossein', 'fatemeh', 'alireza']
name = input("Please enter your name: ")
if name not in names:
    print("Your name does not exist", end="")
else: print("Your name was founded", end="")
"""

# iterating on a list
"""
fruits = ['banana', 'kiwi', 'apple', 'orange']
for fruit in fruits:
    print(fruit)
"""

# sum(1, 100)
"""
sum = 0
for number in range(1, 101):
    sum += number
print(sum, end="")
"""

# counting characters of a string
"""
word = "Hello"
counter = 0
for letter in word:
    counter += 1
print(counter, end="")
"""

# counting sound characters (a, e, i, o, u)
"""
text = str(input("Please enter your text: "))
counter_a, counter_e, counter_i, counter_o, counter_u = 0, 0, 0, 0, 0
for character in text:
    match character:
        case "a":
            counter_a += 1
        case "e":
            counter_e += 1
        case "i":
            counter_i += 1
        case "o":
            counter_o += 1
        case "u":
            counter_u += 1
        case _:
            pass

print("number of (a, e, i, o, u): ", counter_a, counter_e, counter_i, counter_o, counter_u, sep="-")
"""

# A simple notepad
"""
notepad = {}
while True:
    name = input("Please enter your name: (if you want to exit write \"exit\")) ")
    if name == "exit":
        break

    number = input("Please enter number of that name: (if you want to exit write \"exit\") ")
    if number == "exit":
        break

    while True:
        try:
            int(number)
            break
        except ValueError:
            number = input("Please enter a valid number: ")

    notepad[name] = number

print(notepad, end="")
"""

# search a contact
"""
contacts = {
    "Ali": "09120000000",
    "Sara": "09130000000",
    "Reza": "09140000000",
}

name = input("Please enter the name you want: ")
if name in contacts.keys():
    print(contacts[name], end="")
else: print("Name does not exist", end="")
"""

# interactive notepad
"""
class notepad:
    def __init__(self, name:str):
        self.name:str = name
        self.contacts:dict = {}

    def add(self, name:str, number:int):
        try:
            str(name)
            int(number)
        except ValueError:
            print("Please enter a valid input")
        self.contacts[name] = number

    def search(self):
        while True:
            choice = input("if you want to search by number write \"n\" \n if you want to search by name write \"N\") ")
            if choice == "n":
                while True:
                    try:
                        number = int(input("Please enter a number: "))
                        break
                    except ValueError:
                        print("Please enter a valid input")

                for name in self.contacts.keys():
                    if self.contacts[name] == number:
                        print(name, end="")
                        break
                
                print("Not found")
            
            if choice == "N":
                name = input("Please enter your name: ")
                if name not in self.contacts.keys():
                    print("Your name does not exist")
                    break
                
                print(self.contacts[name])
                
    def show(self):
        for key, value in self.contacts.items():
            print(key, end=" ", value)
            
    def exit(self):
        sys.exit("Bye bye")
"""

"""
def welcome(name:str):
    print("Welcome " + name)
"""

"""
def total_sum(number_1:int, number_2:int):
    flag:str = "even"
    if(number_2 % 2 == 1):
        flag = "odd"

    return number_1 + number_2, flag, max(number_1, number_2)

a, b, c = total_sum(4, 5)
print(a, b, c, sep="-")
"""

"""
def counter_letter(text:str):
    counter = 0
    for letter in text:
        counter += 1
    return counter

counter_letter("amir mahdi")
"""

# working with files
"""
with open("text.txt", "w") as file:
    while True:
        name = input("Please enter a name: (if you want to exit write \"exit\"))) ")
        if name == "exit":
            break

        file.write(name)
"""

# read from files
"""
with open("text.txt", "r") as file:
    print(len(file.readlines()))
    print(file.readlines())
"""


# save in different ways in files
"""
with open("text.txt", "w") as file:
    for counter in range(0, 2):
        name = input("Please enter a name:) ")
        age = int(input("Please enter your age: "))
        file.write(f"{name} - {age}\n")
"""

# strip an split method in files
# strip method removes all of spaces and split method you can seperate a line by that thing and create a list for that line
"""
with open("text.txt", "r") as file:
    for line in file.readlines():
        print(line.strip().split("-"))
"""


# average of age
"""
with open("text.txt", "r") as file:
    numbers = []
    lines = file.readlines()
    for line in lines:
        number = ""
        for char in line:
            if char.isdigit():
                number += char
            else:
                if number != "":
                    numbers.append(int(number))
                    number = ""

        if number != "":
            numbers.append(int(number))


print(numbers)
"""

# students management system
"""
class System:
    def __init__(self, name:str):
        self.name:str = name
        self.students:dict = {}
        self.last_saved = 0

    def add(self):
        full_name = input("Please enter your full name: ")
        while True:
            try:
                score = int(input("Please enter your score: "))
                break
            except ValueError:
                print("Please enter a valid score")

        self.students[full_name] = score

    def save(self):
        with open("students.txt", "w") as file:
            for key, value in self.students[self.last_saved:].items():
                file.write(f"{key} - {value}\n")

    def show(self):
        for key, value in self.students.items():
            print(f"{key} - {value}")

    def search_by_name(self, name:str):
        if name in self.students.keys():
            print(self.students[name])
        else:
            print("Name not found")

    def exit(self):
        sys.exit("Program Ended")
"""

song = np.array([0.7, 0.9, 0.6])
user_taste = np.array([0.6, 0.8, 0.5])

# print(song * user_taste) # element-wise product
# print(np.dot(user_taste, song)) # dot product
# result = "suggested" if np.dot(user_taste,song) + 0.3 > 0 else "not suggested"
# print(result)

song1 = np.array([0.9, 0.1])
song2 = np.array([0.85, 0.15])
song3 = np.array([-0.9, -0.1])

# def cosine_similarity(numpy_array1:nd.array, numpy_array2:nd.array):
#    print((numpy_array1 @ numpy_array2) / (np.linalg.norm(numpy_array1, axis=1)*np.linalg.norm(numpy_array2)))

"""
cosine_similarity(song2, song1)
cosine_similarity(song3, song1)
cosine_similarity(song2, song3)
"""

songs = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [2, 0, 1],
    [3, 3, 3],
    [1, 4, 2]
])

# cosine_similarity(songs, song)

# questions = np.array(['Q1','Q2','Q3','Q4','Q5'])
# answers = np.array(['B','D','A','C','B'])

# indices = np.random.permutation(len(questions))

# print(questions, answers, sep=":")
# print(questions[indices], answers[indices], sep=":")

# questions = np.append(questions, ["Q6", "Q7"])
# answers = np.append(answers, ["A", "D"])
# difficulty = np.array([1,2,1,3,2,2,3])

# exam = np.vstack((questions, answers, difficulty)).T
# print(exam)

# camera_frames = np.random.randint(low=0, high=5, size=(4, 6, 3, 3))
# print(camera_frames)
# print(camera_frames.reshape(6, -1))

# week_temps = np.random.randint(low=0, high=7, size=(7, 4, 3))
# print(week_temps)
# print(week_temps.T.shape)

# confidence = np.array([0.9, 0.4, 0.7, 0.95, 0.3])
# print(confidence.reshape(5, -1))

# single_command_output = np.array([[[0.1, 0.7, 0.2]]])
# print(single_command_output.reshape(3).shape)
# print(single_command_output.reshape(1, -1))

# power_readings = np.array([2.1, -0.5, 3.4, -1.1, 0, 5.6])
# power_readings[power_readings < 0] = int(0)
# print(power_readings)

logits = np.array([
    [2.5, 0.3, 0.1],
    [0.2, 0.1, 3.5],
    [1.0, 1.2, 0.9]
])

# print(np.exp(logits) / np.exp(logits).sum(axis=1).reshape(-1, 1))

"""
cart_prices = np.array([120, 45, 300, 15, 80])
discount_items = cart_prices[:2].copy()
discount_items[0] = 0
print(cart_prices)

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=0, keepdims=True))
    return exp_x / np.sum(exp_x, axis=0, keepdims=True)

x_songs = np.random.randint(low=1, high=11, size=(8, 4))

layer_1 = np.random.rand(5, 4)
layer_2 = np.random.rand(3, 5)
for song in x_songs:
    result_layer_1 = layer_1 @ song
    result_layer_1 = np.maximum(result_layer_1, 0)
    result_layer_2 = layer_2 @ result_layer_1
    result_layer_2 = softmax(result_layer_2)
    print(result_layer_2)
"""


gym_data = np.array([
    [28, 75, 175, 4],
    [34, 68, 168, 3],
    [45, 82, 180, 2],
    [22, 58, 162, 5],
    [38, 90, 0, 1],
    [29, 65, 170, 0]
])

# ستون ها به ترتیب:
# ستون 0: سن (سال)
# ستون 1: وزن (کیلوگرم)
# ستون 2: قد (سانتی متر)
# ستون 3: تعداد جلسات در هفته
member_names = np.array(["Ali", "Sara", "Reza", "Neda", "Hassan", "Maryam"])

# پر کردن عناصری که صفر بودند
gym_data[[4, 5], [2, 3]] = 178, 7
# print(gym_data)


# آرایه جدید بر اساس وزن و قد و تعداد جلسات
edited_gym_data = gym_data[:, 1:]
# print(edited_gym_data)

# حساب کردن نمره آمادگی جسمانی (BMI + training sessions*2)
bmi = gym_data[:,1]*10000 / np.square(gym_data[:,2])
# print(bmi)
fitness_scores = (bmi + gym_data[:,3]*2).reshape(-1, 1)
edited_gym_data = np.hstack((gym_data, fitness_scores))
# print(edited_gym_data)

index = np.argmax(edited_gym_data[:, 4])
# print(member_names[index])

mean = np.mean(edited_gym_data[:, 3])
z_scores = np.abs((edited_gym_data[:, 3] - mean)/np.std(edited_gym_data[:, 3]))
index = np.argmax(z_scores)
# print(member_names[index])


recipes = np.array([
    [15, 350, 2, 5],
    [45, 600, 7, 10],
    [10, 200, 0, 3],
    [30, 450, 5, 7],
    [60, 800, 8, 12]
])
recipe_names = ["Salad", "Curry", "Toast", "Pasta", "Stew"]

# Normalization
normalized_recipes = (recipes - np.min(recipes, axis= 0)) / (np.max(recipes, axis= 0) - np.min(recipes, axis= 0))
# print(min_max_slicing)

users = np.array([
    [10, 250, 1, 4],
    [50, 700, 8, 11],
    [25, 400, 4, 6]
])

normalized_users = (users - np.min(recipes, axis=0)) / (np.max(recipes, axis=0) - np.min(recipes, axis=0))
# print(normalized_users)

recipes = recipes.reshape(1, 5, 4)
users = users.reshape(3, 1 , 4)

# print(np.linalg.norm(users - recipes, axis = 2))
# print(np.linalg.norm(users - recipes, axis = 2).argmin(axis = 1))
indices = np.linalg.norm(users - recipes, axis = 2).argsort(axis = 1)
# print(indices)
recipe_names = np.array(recipe_names)[indices]
# print(recipe_names)

scores = np.array([
    [18, 15, 20],
    [12, 14, 16],
    [20, 19, 18],
    [10, 8, 15]
])

scheme_A = np.array([0.5, 0.3, 0.2])
scheme_B = np.array([0.2, 0.3, 0.5])
scheme_C = np.array([0.1, 0.2, 0.7])

weight_matrix = np.vstack((scheme_A, scheme_B, scheme_C))
# print(weight_matrix)
final_scores = scores @ weight_matrix.T
# print(final_scores)
# weighted_names = np.array(["A", "B", "C"])
# print(weighted_names[np.argmax(final_scores, axis= 1)])

# print(np.mean(final_scores, axis = 0).argmax())

# scheme_D = np.array([0.25, 0.25, 0.5])
# weight_matrix = np.vstack((weight_matrix, scheme_D))
# print(weight_matrix)


def analyze_day(arr:numpy.ndarray):
    pass

weather_data = np.random.randn(2, 8, 4) * 5 + 20
day2 = weather_data[1]
day2.reshape(4, 8)
analyze_day(day2)

# weather_data = weather_data.flatten()
# print(weather_data)

"""
day3 = np.random.randn(8, 4) * 5 + 20
weather_data = np.concatenate(
    (weather_data, day3[np.newaxis, :, :]),
    axis=0
)
print(weather_data)
"""

importance = np.array([3, 8, 1, 9, 4, 7])
# print(importance.reshape(-1, 1))
# print(importance[:,np.newaxis])

model_out = np.array([[[0.9]]])
# print(model_out[0, 0, 0])
# print(model_out.item(0))

notes = np.array([5, 10, 15, 20, 25])
pinned = notes[1:3]
pinned[0] = 999
# print(notes)


bib_numbers = np.array([101, 102, 103, 104, 105, 106])
times_5k = np.array([22.3, 25.1, 21.8, 26.4, 23.0, 24.7])

# new datas
bib_numbers_2 = np.array([107, 108])
times_5k_2 = np.array([20.5, 27.9])

bib_numbers = np.hstack((bib_numbers, bib_numbers_2))
times_5k = np.hstack((times_5k, times_5k_2))
# you can also use concatenate

indices = np.random.permutation(times_5k.shape[0])
# print(bib_numbers[indices], times_5k[indices])
# you can also use shuffle method


final_scores = np.vstack((bib_numbers[np.argsort(times_5k, axis = 0)], times_5k[np.argsort(times_5k, axis = 0)], np.arange(1,len(times_5k)+1))).T
# print(final_scores)

# print(final_scores[np.where(final_scores == 104)[0][0], 2])

X_messages = np.array([
    [12, 0, 1],
    [45, 5, 8],
    [8, 0, 0],
    [30, 3, 4]
])
w = np.array([0.1, 0.8, 0.5])
b = -2.0

output_neuron = X_messages @ w + b
# print(output_neuron)
output_neuron = np.maximum(0, output_neuron)
# print(output_neuron)
output_neuron = np.where(output_neuron > 5, 1, 0)
# print(output_neuron)

data_set = np.random.randint(low=0, high=9, size=(10000, 5))
# print(data_set[:5])
np.random.shuffle(data_set)
# print(data_set[:5])
# print(data_set.shape)

train_set_size = int(data_set.shape[0] * 0.8)
valid_set_size = int(data_set.shape[0] * 0.1)
test_set_size = int(data_set.shape[0] * 0.1)

training_set = data_set[:train_set_size, :]
validation_set = data_set[train_set_size:valid_set_size + train_set_size, :]
test_set = data_set[valid_set_size + train_set_size:, :]

# print(training_set.shape)
# print(validation_set.shape)
# print(test_set.shape)
# print(training_set[:5])
# print(validation_set[:5])
# print(test_set[:5])

data_set = np.random.randint(low=0, high=9, size=(12350, 5))
# print(data_set[:5])
np.random.shuffle(data_set)
# print(data_set[:5])
# print(data_set.shape)

train_set_size = int(data_set.shape[0] * 0.8)
valid_set_size = int(data_set.shape[0] * 0.1)
test_set_size = int(data_set.shape[0] * 0.1)

training_set = data_set[:train_set_size, :]
validation_set = data_set[train_set_size:valid_set_size + train_set_size, :]
test_set = data_set[valid_set_size + train_set_size:, :]

# print(training_set.shape)
# print(validation_set.shape)
# print(test_set.shape)
# print(training_set[:5])
# print(validation_set[:5])
# print(test_set[:5])

ground_truth = np.array([
 "Normal",
 "Urgent",
 "Normal",
 "Spam",
 "Urgent",
 "Normal",
 "Spam",
 "Normal"
])

predictions = np.array([
 "Normal",
 "Normal",
 "Normal",
 "Spam",
 "Urgent",
 "Spam",
 "Spam",
 "Normal"
])

correct_mask = ground_truth == predictions
# print(len(correct_mask[correct_mask]))
# print(predictions[correct_mask])
# print(len(correct_mask[~correct_mask]))

# print(len(correct_mask[correct_mask])/ len(correct_mask))
# print(len(correct_mask[~correct_mask])/ len(correct_mask))

y_true = ["Normal"]*950 + ["Urgent"]*50
# print(len(y_true))
y_pred = ["Normal"]*1000
# print(len(y_pred))
y_true = np.array(y_true)
y_pred = np.array(y_pred)
correct_mask1 = y_true == y_pred
# print(correct_mask1)
# print(len(correct_mask1[correct_mask1]) / len(y_true))
# print(1 - (len(correct_mask1[correct_mask1]) / len(y_true)))

patient_id = np.array([1, 2, 3, 4, 5])
ground_truth = np.array([
 "Healthy",
 "Malignant",
 "Healthy",
 "Healthy",
 "Malignant"
])

predictions = np.array([
 "Healthy",
 "Malignant",
 "Malignant",
 "Healthy",
 "Healthy"
])


mask = (ground_truth == "Healthy") & (predictions == "Malignant")
# print(len(patient_id[mask]))

mask1 = (ground_truth == "Malignant") & (predictions == "Healthy")
# print(len(patient_id[mask]))

email_id = np.array([1, 2, 3, 4, 5])

ground_truth = np.array([
 "Not Spam",
 "Spam",
 "Not Spam",
 "Not Spam",
 "Spam"
])

predictions = np.array([
 "Not Spam",
 "Spam",
 "Spam",
 "Not Spam",
 "Not Spam"
])

mask = ground_truth == predictions
# print(len(mask[mask])/ len(mask))
# print(1 - len(mask[mask])/ len(mask))

study_hours = np.array([1, 2, 3, 5, 7, 8])
gaming_hours = np.array([6, 5, 4, 3, 2, 1])
actual_scores = np.array([35, 40, 50, 68, 82, 90])
weight1 = 8
weight2 = -3
bias = 45

predicted_scores = study_hours*weight1 + gaming_hours*weight2 + bias
# print(predicted_scores)

predicted_scores = np.clip(predicted_scores, a_min=0, a_max=100)
# print(predicted_scores)

error = predicted_scores - actual_scores

absolute_error = np.abs(error)

MAE = np.mean(absolute_error)

candidate_weight1 = np.array([2, 4, 6, 8, 10, 12]).reshape(-1, 1)

predicted_scores_2 = np.clip(study_hours*candidate_weight1 + gaming_hours*weight2 + bias,0 ,100)
# print(predicted_scores_2)

MAE2 = np.mean(predicted_scores_2, axis = 0)
# print(MAE2)

min_mae2 = np.min(MAE2)
# print(min_mae2)

error_2 = predicted_scores_2 - actual_scores
# print(error_2)

best_weight = np.argmin(np.sum(np.abs(error_2), axis = 1))
# print("best_weight: ", candidate_weight1[best_weight])

emails = np.array([
 "URGENT reset my password now!!!",
 "hello I have a question about my invoice",
 "refund refund refund this is unacceptable!!!",
 "please cancel my subscription",
 "thank you for your help",
 "URGENT billing error please help!!!"
])

labels = np.array([
 "Urgent",
 "Normal",
 "Urgent",
 "Normal",
 "Normal",
 "Urgent"
])

feature_1 = np.array([])
feature_2 = np.array([])
feature_3 = np.array([])
feature_4 = np.array([])

for email in emails:

    if "urgent" in email.lower():
        feature_1 = np.append(feature_1, 1)
    else:
        feature_1 = np.append(feature_1, 0)

    if "refund" in email.lower():
        feature_2 = np.append(feature_2, 1)
    else:
        feature_2 = np.append(feature_2, 0)

    counter = email.count("!")
    feature_3 = np.append(feature_3, counter)

    feature_4 = np.append(feature_4, len(email.split()))

X_email = np.array([feature_1, feature_2, feature_3, feature_4]).T
# print(X_email)

# feature_2: shows is there refund word in every email
# feature_3: shows how many ! are there in every email
#feature_4: shows count of word in every email

predicted_labels = np.array([])
for x_email in X_email:
    if x_email[0] == 1 or x_email[1] == 1 or x_email[2] >= 3:
        predicted_labels = np.append(predicted_labels, "Urgent")
    else:
        predicted_labels = np.append(predicted_labels, "Normal")

# print(predicted_labels)

mask = predicted_labels == labels
# print(mask)

accuracy = mask.sum() / mask.size
# print(accuracy)

error = 1 - accuracy

X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 6, 9, 12, 15])

candidate_w = np.array([1, 2, 2.5, 3, 3.5, 4])

candidate_w = candidate_w.reshape(-1, 1)

predictions = X * candidate_w
# print(predictions)

MSE = np.mean((predictions - y)**2 , axis = 1)
# print(MSE)

mse_min = np.min(MSE)
# print(mse_min)

# print(candidate_w[np.argmin(MSE)])