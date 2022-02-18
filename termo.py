import turtle, random
lista_de_palavras = ['sagaz', 'negro', 'amago', 'exito', 'mexer', 'termo', 'senso', 'nobre', 'algoz', 'afeto',
                     'plena', 'etica', 'mutua', 'sutil', 'tenue', 'vigor', 'aquem', 'audaz', 'porem', 'fazer']
resposta = random.choice(lista_de_palavras) #para escolher uma palavra da lista acima
y = 250
print(resposta)

def draw_square(x, y, cor):   #cordenadas x e y e cores
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

def input_guess(prompt):
    chute = turtle.textinput("Palavra de 5 Letras", prompt)
    if chute == None: return "       "  #se cancelar ou se aceitar com nada
    elif len(chute) != 5: return chute[0:5]  #envia as 5 primeiras letras
    else: return chute.lower()

def check_guess(chute, resposta, y):
    count = 0
    x = -250        #localização do x
    for i in chute:
        if i == resposta[count]: draw_square(x, y, "green")     #letra certa desenha um quadrado verde
        elif i in resposta: draw_square(x, y, "yellow")
        else: draw_square(x, y, "red")
        count += 1
        x += 75     #move a coordenada 75
    turtle.penup()
    turtle.goto(x, y - 25)
    turtle.write(chute, font=("Verdana", 15, "normal"))

for i in range(6):      #onde o programa começa
    chute_prompt = 'Qual seu chute?'
    chute = input_guess(chute_prompt)
    check_guess(chute, resposta, y)
    y -= 75
    if chute == resposta:
        turtle.penup()
        turtle.goto(-400, -300)
        turtle.write("PARABÉNS, VOCE ACERTOU!!", font=("Verdana", 42, "normal"))
        break
else:
    turtle.penup()
    turtle.goto(-400, -300)
    turtle.write(resposta, font=("Verdana", 42, "normal"))
turtle.done()