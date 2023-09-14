# criar um programa que calculaa quantidade de tinta necessaria para pintar um aparede
# o usuario devera fornecer as seguintes informações:
# Rendimento, largura, altura
# o programa devera mostrar na tela a mensagem
# "vc necessita de x latas de tinta"

rendimento = int(input('Qual e o rendimentoda lata? '))
altura = int(input('Qual a altura da parese? '))
largura = int(input('Qual a largura da parede? '))

# alt * larg / rendimento = qtd latas

def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'voce precisa de {total} latas de tinta')

calculo_tinta()