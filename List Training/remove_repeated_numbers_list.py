my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temporary_list = []
 
for i in range(len(my_list)):
    if my_list[i] not in temporary_list:
        temporary_list.append(my_list[i])
 
my_list = temporary_list   
print("A lista com os elementos exclusivos aqui")
print(my_list)