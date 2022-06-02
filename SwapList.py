#Swapping first and last elements in a list of elements entered by the user
user_elements = int(input("enter number of elements you want")) #Taking the inputs from the user
list_ele = [] #creating an empty list to append elements afterwards

#The range is set to number of user_elements and we know that python extends its range from 0 to user_elements-1
for i in range(0,user_elements):
    user_enter = int(input(f"Enter element {i+1}: "))                                   #User enters his first element, second and so on
    list_ele.append(user_enter)                                                         #We append the elements as the user enters the elements
print(list_ele)                                                                         #Showing all the elements of the unswapped list

#We perform the swapping of elements namely the first and last elements
list_ele[0] = list_ele[0]+list_ele[user_elements-1]
list_ele[user_elements-1] = list_ele[0]-list_ele[user_elements-1]
list_ele[0] = list_ele[0] - list_ele[user_elements-1]

#We finally print the swapped first and last element in our list
print(list_ele)


