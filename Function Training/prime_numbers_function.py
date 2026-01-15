def is_prime(num):
 counter = 0
 for i in range(num + 1):
     if num % (i + 1) == 0:
         counter += 1
 if counter == 2:
    return True
 else:
    return False

for i in range(1, 20):
 if is_prime(i + 1):
    print(i + 1, end=" ")
print()