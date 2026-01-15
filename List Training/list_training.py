hat_list = [1, 2, 3, 4, 5]

user_number = int(input("Escreva um número inteiro: "))
hat_list[2] = user_number

del hat_list[-1]

print("Comprimento lista:",len(hat_list))

print(hat_list) 
