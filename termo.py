import turtle, random
lista_de_palavras = ['sagaz', 'negro', 'amago', 'exito', 'mexer', 'termo', 'senso', 'nobre', 'algoz', 'afeto',
                     'plena', 'etica', 'mutua', 'sutil', 'tenue', 'vigor', 'aquem', 'audaz', 'porem', 'fazer',
                     'sanar', 'inato', 'assim', 'cerne', 'desde', 'ideia', 'fosse', 'poder', 'moral', 'torpe',
                     'honra', 'justo', 'muito', 'vasco', 'anexo', 'gozar', 'futil', 'razao', 'quiça', 'icone',
                     'etnia', 'sobre', 'tange', 'egide', 'lapso', 'mutuo', 'sonho', 'expor', 'haver', 'habil',
                     'casal', 'amigo', 'posse', 'pesar', 'tempo', 'avido', 'ardil', 'entao', 'boçal', 'corja',
                     'genro', 'coser', 'seara', 'dengo', 'prole', 'detem', 'causa', 'dizer', 'tenaz', 'digno',
                     'dever', 'crivo', 'obice', 'apice', 'saber', 'porra', 'ansia', 'brado', 'ceder', 'gleba',
                     'animo', 'paria', 'assaz', 'atroz', 'comum', 'graça', 'culto', 'temor', 'orgia', 'sendo',
                     'censo', 'mundo', 'denso', 'pauta', 'fugaz', 'valha', 'cozer', 'nenem', 'ainda', 'vicio',
                     'reves', 'forte', 'vulgo', 'pudor', 'ester', 'regra', 'dogma', 'louco', 'banal', 'criar',
                     'pifio', 'tenro', 'impor', 'desse', 'apraz', 'reaça', 'jeito', 'ordem', 'atras', 'pedir',
                     'round', 'clava', 'saude', 'viril', 'usura', 'merce', 'manso', 'juizo', 'sabio', 'ontem',
                     'servo', 'prosa', 'presa', 'feliz', 'afago', 'fluir', 'coisa', 'falar', 'cunho', 'forma',
                     'devir', 'meiga', 'vendo', 'serio', 'plato', 'homem', 'guisa', 'pleno', 'temer', 'visar',
                     'bruma', 'cisma', 'limbo', 'mesmo', 'magoa', 'xibiu', 'acaso', 'puder', 'gerar', 'exodo',
                     'heroi', 'obvio', 'afins', 'obter', 'valor', 'impio', 'lugar', 'matiz', 'praxe', 'crise',
                     'senil', 'havia', 'venia', 'fluxo', 'enfim', 'certo', 'alibi', 'tedio', 'ritmo', 'reter',
                     'tomar', 'posso', 'grato', 'uniao', 'vital', 'valia', 'visao', 'favor', 'abrir', 'bravo',
                     'todos', 'laico', 'ameno', 'facil', 'genio', 'reles', 'obito', 'possa', 'olhar', 'falso',
                     'levar', 'tesao', 'burro', 'selar', 'fator', 'festa', 'sexta', 'judeu', 'monge', 'rumor',
                     'piada', 'roupa', 'chefe', 'nuvem', 'ambar', 'bença', 'clero', 'amiga', 'demao', 'natal',
                     'nessa', 'sigla', 'firma', 'rente', 'enjoo', 'zumbi', 'ousar', 'santo', 'lutar', 'baixo',
                     'coroa', 'forro', 'macho', 'farto', 'ultra', 'lento', 'harem', 'caixa', 'russo']
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
    if chute == None:
        return "       "  #se cancelar ou se aceitar com nada
    elif len(chute) != 5:
        return chute[0:5]  #envia as 5 primeiras letras
    else:
        return chute.lower()

def check_guess(chute, resposta, y):
    count = 0
    x = -250        #localização do x
    for i in chute:
        if i == resposta[count]:
            draw_square(x, y, "green")     #letra certa desenha um quadrado verde
        elif i in resposta:
            draw_square(x, y, "yellow")      #letra certa em lugar errado desenha quadrado amarelo
        else:
            draw_square(x, y, "red")     #letra errada
        count += 1
        x += 75     #move a coordenada 75
    turtle.penup()      #penup desativa a caneta
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
        turtle.write("PARABÉNS, VOCE ACERTOU!!", font=("Verdana", 41, "normal"))
        break
else:
    turtle.penup()
    turtle.goto(-400, -300)
    turtle.write(resposta, font=("Verdana", 41, "normal"))
turtle.done()