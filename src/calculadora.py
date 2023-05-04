peso = float(input("Qual é o seu peso? (Kg)?"))
altura = float(input("Qual é a sua altura (M)?"))

imc = peso / (altura**2)

if imc < 18.5:
    print("Voce está ABAIXO do peso ")
elif 18.5 <= imc < 25:
    print("Voce está no seu peso Ideal")
elif 25 <= imc < 30:
    print("Voce está acima do peso Indice de SOBREPESO")
elif 30 < imc < 40:
    print("Voce está com o Indice de OBESIDADE")
elif imc >= 40:
    print("Voce está na faixa de OBESIDADE MÓRBIDA")

print(f"Seu Imc é de {imc}")
