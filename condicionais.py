# idade = 16

# if idade >= 18:
#       print("Maior de idade.")
# else:
#      print("Menor de idade.")


# temperatura_maquina = 800

# if temperatura_maquina >= 90: 
#     print("alerta critico: temperatura muito alta.")
# elif temperatura_maquina >= 75:
#     print("atenção: temperatura acima do ideial.")
# else:
#     print ("temperatura dentro do esperado.")

 

# senha_secreta = input("Digite sua senha:")

# if senha_secreta == "1234" :
#     print("acesso liberado!")
# else: 
#     print("acesso negado!")
                                    
nota = int(input("Informe a nota do aluno: "))
if nota >= 5:
    print(f"Aluno aprovado com a nota {nota}")
elif nota >= 3 and nota <= 4:
    print("Voçê está de Recuperação!")
else:
    print(f"Aluno Reprovado com a nota {nota}")
