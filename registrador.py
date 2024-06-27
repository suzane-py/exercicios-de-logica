"""
Escreva um algoritmo que receba dados sobre 10 pessoas: nome, sexo (M ou F) e 
altura. Ao final apresente:
• A maior e a menor altura de cada grupo;
• A média de altura das mulheres;
• O número de homens;
• O nome da mulher com a menor altura.
"""

mulheres = []
num_mulheres = 0

homens = []
num_homens = 0

for i in range(1, 10+1):
    pessoa = {
        'nome': input(f"Digite o nome da {i}ª pessoa: "),
        'sexo': input("Insira o sexo (M ou F): "),
        'altura': float(input("Insira a altura: "))
    }
    pessoa['sexo'] = pessoa['sexo'].upper()

    if pessoa['sexo'] not in ['M', 'F']:
        print("Insira um sexo válido!")
        continue
    if pessoa['sexo'] in ['M']:
        homens.append(pessoa)
        num_homens += 1
    elif pessoa['sexo'] in ['F']:
        mulheres.append(pessoa)
        num_mulheres += 1

mulher_mais_baixa = min(mulheres, key=lambda mulher: mulher['altura']) # a função min() recebe uma lista e uma função lambda que retorna o valor que será comparado
menor_altura_F = mulher_mais_baixa['altura'] # a menor altura é o valor retornado pela função lambda
nome_mulher_mais_baixa = mulher_mais_baixa['nome']
media_alturas_mulheres = sum(mulher['altura'] for mulher in mulheres)/len(mulheres) 

homem_mais_baixo = min(homens, key=lambda homem: homem['altura'])
menor_altura_M = homem_mais_baixo['altura']

print(
f"""* A mulher mais baixa tem {menor_altura_F:.2f};
* O homem mais baixo tem {menor_altura_M:.2f};
* A média das alturas das mulheres é {media_alturas_mulheres:.2f};
* Existem {num_homens} homens;
* {nome_mulher_mais_baixa} é a mulher mais baixa.
"""
)

