

"""name = input("enter name: ")

print("length of name is", len(name)) """

"""str = "Hi, i have $99 of $299"

print(str.count ("$"))

"""



"""marks = int(input("enter student's marks :"))

if(marks >= 90):

    grade = "A"

elif(marks >= 80 and marks < 90):

    grade = "B"

elif(marks >= 70 and marks < 80):

    grade = "C"

else:

    grade = "D"

print("grade of the student ->", grade)

"""



"""number = int(input("enter the number: "))

rem = number%2

if(rem == 0):

    print("even")

else:

    print("odd")"""

"""

x = int(input("enter 1st num:" ))

y = int(input("enter 2nd num:" ))

z = int(input("enter 3rd num:" ))

if(x>=y and x>=z):

    print("1st num is greatest", x)

elif(y>=z):

    print("2nd num is greatest", y)

else:

    print("3rd num is greatest", z)

"""

""" 

#Tuples in python

tup = (87, 64,33,95)

print(tup[0])

print(tup[1])

 """

"""

#palindrome

list1 = [1,2,1]

list2 = [8,1,2]



copy_list2 = list2.copy()

copy_list2.reverse()



if(copy_list2 == list2):

    print("palindrome")

else:

    print("not palindrome")"""







# Dictionary  mutable ordered

info = {

    "name" : "shraddha",

    "topics" : ("dict", "set"),

    "age" : 20,

    #nested dictionary

    "subjects" : {

        "python" : 45,

        "C" : 40

    }



}

print(info["name"])

print(info["topics"])

print(info["subjects"])

#reassign



#print(len(list(student.keys())))





"""

#set

collection = set()

collection.add(1)

collection.add(2)

collection.add(1)

collection.remove(1)

print(collection)

#no duplicate allow immutable(unchangeable) unordered







set union 

set1 = {1,2,3}

set2 = {2,4,3}

print(set.union(set2))  

print(set.intersection(set2))



"""



"""

def calc_sum(a,b)

sum = a+b

print(sum)

return sum

"""