import turtle, random
lista_de_palavras = ['sagaz', 'negro', 'amago', 'exito', 'mexer', 'termo', 'senso', 'nobre', 'algoz', 'afeto',
                     'plena', 'etica', 'mutua', 'sutil', 'tenue', 'vigor', 'aquem', 'audaz', 'porem', 'fazer']
reposta = random.choice(lista_de_palavras) #para escolher uma palavra da lista acima
y = 250
print(reposta)

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




