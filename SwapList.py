user_elements = int(input("enter number of elements you want"))
list_ele = []

for i in range(0,user_elements):
    user_enter = int(input(f"Enter element {i+1}: "))
    list_ele.append(user_enter)
print(list_ele)

list_ele[0] = list_ele[0]+list_ele[user_elements-1]
list_ele[user_elements-1] = list_ele[0]-list_ele[user_elements-1]
list_ele[0] = list_ele[0] - list_ele[user_elements-1]

print(list_ele)


