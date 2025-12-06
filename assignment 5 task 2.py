#Task 2: Demonstrate List Slicing 

list = [1,2,3,4,5,6,7,8,9,10]
print("originel list:",list)

new_list = list[0:5:1]
print("extracted first five element:" , new_list)

new_list.reverse()
print("reversed list :",new_list)