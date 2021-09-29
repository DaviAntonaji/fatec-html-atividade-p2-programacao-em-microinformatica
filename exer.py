idades = []
olhos = []
sexos = []

idade = None
contador = 0
while idade != 0:
    idade = int(input(f"Digite a idade da {contador+1} pessoa: "))
    if idade != 0:
        sexo = input(f"Digite o sexo da {contador+1} pessoa (m/f): ")
        olho = input(f"Digite a cor dos olhos da {contador+1} pessoa (A - azuis, C - castanhos): ")
        sexosPermitidos = ["m","f"]
        olhosPermitidos = ["a", "c"]
        
        if sexo.lower() in sexosPermitidos and olho.lower() in olhosPermitidos:
            idades.append(idade)
            olhos.append(olho)
            sexos.append(sexo)
            contador+=1
        else:
            print("Algum dado errado...")
        
if len(idades) > 0:
    mediaIdades = 0
    totalIdade = 0

    femininoOlhosAzuis = 0

    for count in range(len(idades)):
        if (olhos[count] == "a") and (idades[count] > 18 and idades[count] < 35) and sexos[count] == "f":
            femininoOlhosAzuis+=1
        if olhos[count] == "c":
            mediaIdades += idades[count]
            totalIdade += 1

    mediaIdades /= totalIdade
    print("A média de idades de pessoas com olhos castanhos é ", mediaIdades)
    print("O total de pessoas entrevistadas é ", len(idades))
    print("O total de mulheres entre 18 e 35 anos com olhos azuis é " , femininoOlhosAzuis)
else:
    print("Dados coletados insuficientes")