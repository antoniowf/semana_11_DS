from colorama import Back, Fore

niveis = [1, 2, 3, 4, 5]
mensagem = ['Muito baixo (crítico)', 'Baixo', 'Médio', 'Alto', 'Muito alto (alerta)']

print(Fore.LIGHTWHITE_EX + 'Sensor de nível de Água')
print("-" * 27)
entrada = int(input("Insira o valor do nivel do sensor -> "))
while entrada not in range(1,6):
    print("Valor inválido, por favor entre um valor de 0 a 5")
    entrada = int(input("Insira o valor do nivel do sensor -> "))
def sensor(valor):
    print("nível do reservatório: ")
    if entrada == niveis[0]:
        print(Back.RED + mensagem[0])
        return mensagem[0]
    elif entrada == niveis[1]:
        print(Back.YELLOW + mensagem[1])
        return mensagem[1]
    elif entrada == niveis[2]:
        print(Back.GREEN + mensagem[2])
        return mensagem[2]
    elif entrada == niveis[3]:
        print(Back.CYAN + mensagem[3])
        return mensagem[3]
    elif entrada == niveis[4]:
        print(Back.BLUE + mensagem[4])
        return mensagem[2]
    return None
sensor(entrada)