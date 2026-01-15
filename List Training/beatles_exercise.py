
beatles = []
print("Etapa 1:", beatles)


beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)



for i in range(2):
    novo_membro = input("Digite o nome do próximo membro da banda: ")
    beatles.append(novo_membro)

print("Etapa 3:", beatles)



del beatles[-1]
del beatles[-1]

print("Etapa 4:", beatles)



beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)



print("Número total de membros:", len(beatles))