#python Lists Exercises 


### 1. Creating a list 
# creating list  of 5 of my favourite fruits 
fruits=[ "Apple", "Grapes", "Orange", "Strawberries ", "Watermalone"]
#print the fruits 
print(*fruits, sep=",")

###2.Acessing Elements 
#writing the colors 
colors=["Red", "Blue", "Green", "Yellow", "Purple"]
#printing the first ,third and last colors on the list 
print(colors[0],colors[2],colors[4])

###3.Modify a List  
#making my list of numbers 
numbers=[10,20,30,40,50]
#changing the second number to 25
numbers[1]=25
#Adding 60 at the end of the list 
numbers.append(60)
print(numbers)

###4 List slicing 
#List names 
names=["Alice", "Bob", "Charlie" , "David", "Emma"]
#creating a new list subset containing only the first three names .
subset=(names[0] ,names[1],names[2] )
print(*subset,sep=",")

###5.Looping through a list 
# creating a list of numbers 
#adding a loop to the list and printing each number squared 
numbers=[1,2,3,4,5,6,7,8,9,10]
for numbers in numbers :
    print(numbers**2)

###6.List Methods :Append and Extend 
#creating my empty list 
shopping_cart=[]
#Adding milk,bread and eggs
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")

#Adding butter and cheese to the shopping_cart
shopping_cart.extend(["butter" , "cheese"])
print(*shopping_cart, sep=", ")

###7.Finding Maximum and minimum in a list 
#creating the numbers 
numbers=[45,22,88,56,92,33]
#finding the maximum number in the list 
max_value=max(numbers)
#Finding minimum numbers from the list 
min_value=min(numbers )
#printing the results 
print("Maximum_Value:",max_value)
print("Minimum_Value:",min_value)

###8. Creating a list of letters
letters = ["a", "b", "c", "b", "a", "d"]
# Counting the occurrence of the letter 'a'
count_a = letters.count("a")
# Printing results
print("The letter 'a' appears", count_a, "times.")

###9.List comprehension 
#creating a list of even numbers 
squares_of_even_numbers = [x ** 2 for x in range(11) if x % 2 == 0]
#printing the results
print(squares_of_even_numbers)

###10.Removing Duplicates
nums=[1,2,2,2,3,4,4,5,6,6,7]
#removing duplicate numbers 
unique_nums=list(set(nums))
#print the results 
print(unique_nums)







