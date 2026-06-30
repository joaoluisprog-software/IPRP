import turtle as t
import functools
import random

LARGURA_JANELA = 1024
ALTURA_JANELA = 600
DEFAULT_TURTLE_SIZE = 40
DEFAULT_TURTLE_SCALE = 3
RAIO_JOGADOR = DEFAULT_TURTLE_SIZE / DEFAULT_TURTLE_SCALE
RAIO_BOLA = DEFAULT_TURTLE_SIZE / 2
PIXEIS_MOVIMENTO = 90
LADO_MAIOR_AREA = ALTURA_JANELA / 3
LADO_MENOR_AREA = 50
RAIO_MEIO_CAMPO = LADO_MAIOR_AREA / 4
START_POS_BALIZAS = ALTURA_JANELA / 4
BOLA_START_POS = (0,0)
VELOCIDADE_BOLA = 2


# Funções responsáveis pelo movimento dos jogadores no ambiente. 
# O número de unidades que o jogador se pode movimentar é definida pela constante 
# PIXEIS_MOVIMENTO. As funções recebem um dicionário que contém o estado 
# do jogo e o jogador que se está a movimentar. 

def jogador_cima(estado_jogo, jogador):
    obj = estado_jogo[jogador]
    novo_y = min((obj.ycor() + PIXEIS_MOVIMENTO), ALTURA_JANELA/2 - RAIO_JOGADOR)
    # novo_y = obj.ycor() + PIXEIS_MOVIMENTO 
    obj.goto(obj.xcor(), novo_y)
    

def jogador_baixo(estado_jogo, jogador):
    obj = estado_jogo[jogador]
    novo_y = max((obj.ycor() - PIXEIS_MOVIMENTO), -ALTURA_JANELA/2 + RAIO_JOGADOR)
    # novo_y = obj.ycor() - PIXEIS_MOVIMENTO 
    obj.goto(obj.xcor(), novo_y)
    
def jogador_direita(estado_jogo, jogador):
    obj = estado_jogo[jogador]
    novo_x = min((obj.xcor() + PIXEIS_MOVIMENTO), LARGURA_JANELA/2 - RAIO_JOGADOR)
    # novo_x = obj.xcor() + PIXEIS_MOVIMENTO 
    obj.goto(novo_x, obj.ycor())

def jogador_esquerda(estado_jogo, jogador):
    obj = estado_jogo[jogador]
    novo_x = max((obj.xcor() - PIXEIS_MOVIMENTO), -LARGURA_JANELA/2 + RAIO_JOGADOR)
    # novo_x = obj.xcor() - PIXEIS_MOVIMENTO 
    obj.goto(novo_x, obj.ycor())

def desenha_linhas_campo():
    ''' Função responsável por desenhar as linhas do campo, 
    nomeadamente a linha de meio campo, o círculo central, e as balizas. '''
    t.color('white')
    t.pensize(10)

    # Linha do meio campo
    t.up()
    t.goto(0, ALTURA_JANELA/2)
    t.setheading(-90)
    t.down()
    t.forward(ALTURA_JANELA)

    # Circulo central
    t.up()
    t.goto(-RAIO_MEIO_CAMPO*2, 0)
    t.down()
    t.circle(RAIO_MEIO_CAMPO*2)

    # Baliza Player A 
    t.up()
    t.goto(-(LARGURA_JANELA/2), LADO_MAIOR_AREA/2)
    t.setheading(0)
    t.down()
    t.forward(LADO_MENOR_AREA)
    t.right(90)
    t.forward(LADO_MAIOR_AREA)
    t.right(90)
    t.forward(LADO_MENOR_AREA)

    # Baliza Player B
    t.up()
    t.goto(LARGURA_JANELA/2, LADO_MAIOR_AREA/2)
    t.setheading(180)
    t.down()
    t.forward(LADO_MENOR_AREA)
    t.left(90)
    t.forward(LADO_MAIOR_AREA)
    t.left(90)
    t.forward(LADO_MENOR_AREA)

def criar_bola():
    '''
    Função responsável pela criação da bola. 
    Deverá considerar que esta tem uma forma redonda, é de cor preta, 
    começa na posição BOLA_START_POS com uma direção aleatória. 
    Deverá ter em conta que a velocidade da bola deverá ser superior à dos jogadores. 
    A função deverá devolver um dicionário contendo 4 elementos: o objeto bola, 
    a sua direção no eixo dos xx, a sua direção no eixo dos yy, 
    e um elemento inicialmente a None que corresponde à posição anterior da mesma.
    '''
    bola = t.Turtle()
    bola.shape('circle')
    bola.shapesize(RAIO_BOLA/10)
    bola.color('black')
    bola.penup()
    bola.goto(BOLA_START_POS)
    # bola.pendown()

    dir_x = random.choice([-1, 1])
    dir_y = random.choice([-1, 1])

    return {
        'objeto' : bola,
        'dir_x' : dir_x * VELOCIDADE_BOLA,
        'dir_y' : dir_y * VELOCIDADE_BOLA,
        'pos_anterior' : None
    }

def cria_jogador(x_pos_inicial, y_pos_inicial, cor):
    ''' Função responsável por criar e devolver o objeto que corresponde a um jogador (um objecto Turtle). 
    A função recebe 3 argumentos que correspondem às coordenadas da posição inicial 
    em xx e yy, e a cor do jogador. A forma dos jogadores deverá ser um círculo, 
    cujo seu tamanho deverá ser definido através da função shapesize
    do módulo \texttt{turtle}, usando os seguintes parâmetros: 
    stretch_wid=DEFAULT_TURTLE_SCALE, stretch_len=DEFAULT_TURTLE_SCALE. '''
    jogador = t.Turtle()
    jogador.shape('circle')
    jogador.shapesize(stretch_wid=DEFAULT_TURTLE_SCALE, stretch_len=DEFAULT_TURTLE_SCALE)
    jogador.color(cor)
    jogador.penup()
    jogador.goto(x_pos_inicial, y_pos_inicial)
    # jogador.pendown()
    return jogador


def init_state():
    estado_jogo = {}
    estado_jogo['bola'] = None
    estado_jogo['jogador_vermelho'] = None
    estado_jogo['jogador_azul'] = None
    estado_jogo['var'] = {
        'bola' : [],
        'jogador_vermelho' : [],
        'jogador_azul' : [],
    }
    estado_jogo['pontuacao_jogador_vermelho'] = 0
    estado_jogo['pontuacao_jogador_azul'] = 0
    return estado_jogo

def cria_janela():
    #create a window and declare a variable called window and call the screen()
    window=t.Screen()
    window.title("Foosball Game")
    window.bgcolor("green")
    window.setup(width = LARGURA_JANELA,height = ALTURA_JANELA)
    window.tracer(0)
    return window

def cria_quadro_resultados():
    #Code for creating pen for scorecard update
    quadro=t.Turtle()
    quadro.speed(0)
    quadro.color("Blue")
    quadro.penup()
    quadro.hideturtle()
    quadro.goto(0,260)
    quadro.write("Player A: 0\t\tPlayer B: 0 ", align="center", font=('Monaco',24,"normal"))
    return quadro


def terminar_jogo(estado_jogo):
    '''
     Função responsável por terminar o jogo. Nesta função, deverá atualizar o ficheiro 
     ''historico_resultados.csv'' com o número total de jogos até ao momento, 
     e o resultado final do jogo. Caso o ficheiro não exista, 
     ele deverá ser criado com o seguinte cabeçalho: 
     NJogo,JogadorVermelho,JogadorAzul.
    '''
    ficheiro = 'histórico_resultados.csv'

    try:
        with open(ficheiro, 'r') as f:
            linhas = f.readlines()
        jogos_existentes = [l for l in linhas[1:] if l.strip()]
        n_jogo = len(jogos_existentes) + 1
    except FileNotFoundError:
        with open(ficheiro, 'w') as f:
            f.write('NJogo,JogadorVermelho,JogadorAzul\n')
        n_jogo = 1

    with open(ficheiro, 'a') as f:
        f.write(f'{n_jogo},{estado_jogo["pontuacao_jogador_vermelho"]},{estado_jogo["pontuacao_jogador_azul"]}\n')

    estado_jogo['janela'].bye()

def setup(estado_jogo, jogar):
    janela = cria_janela()
    #Assign keys to play
    janela.listen()
    if jogar:
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_vermelho') ,'w')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_vermelho') ,'s')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_vermelho') ,'a')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_vermelho') ,'d')
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_azul') ,'Up')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_azul') ,'Down')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_azul') ,'Left')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_azul') ,'Right')
        janela.onkeypress(functools.partial(terminar_jogo, estado_jogo) ,'Escape')
        quadro = cria_quadro_resultados()
        estado_jogo['quadro'] = quadro
    desenha_linhas_campo()
    bola = criar_bola()
    jogador_vermelho = cria_jogador(-((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "red")
    jogador_azul = cria_jogador(((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "blue")
    estado_jogo['janela'] = janela
    estado_jogo['bola'] = bola
    estado_jogo['jogador_vermelho'] = jogador_vermelho
    estado_jogo['jogador_azul'] = jogador_azul


def update_board(estado_jogo):
    estado_jogo['quadro'].clear()
    estado_jogo['quadro'].write("Player A: {}\t\tPlayer B: {} ".format(estado_jogo['pontuacao_jogador_vermelho'], estado_jogo['pontuacao_jogador_azul']),align="center",font=('Monaco',24,"normal"))

def movimenta_bola(estado_jogo):
    '''
    Função responsável pelo movimento da bola que deverá ser feito tendo em conta a
    posição atual da bola e a direção em xx e yy.
    '''
    obj_bola = estado_jogo['bola']
    novo_x = obj_bola['objeto'].xcor() + obj_bola['dir_x']
    novo_y = obj_bola['objeto'].ycor() + obj_bola['dir_y']
    
    obj_bola['objeto'].goto(novo_x, novo_y)
   

def verifica_colisoes_ambiente(estado_jogo):
    '''
    Função responsável por verificar se há colisões com os limites do ambiente,
    atualizando a direção da bola. Não se esqueça de considerar que nas laterais,
    fora da zona das balizas, a bola deverá inverter a direção onde atingiu o limite.
    '''
    if estado_jogo['bola'] is None:
        return

    obj_bola = estado_jogo['bola']
    bola = obj_bola['objeto']
    x = bola.xcor()
    y = bola.ycor()

    # Paredes de cima e baixo
    if y + RAIO_BOLA >= ALTURA_JANELA / 2:
        obj_bola['dir_y'] *= -1
        bola.goto(x, ALTURA_JANELA / 2 - RAIO_BOLA)
    elif y - RAIO_BOLA <= -ALTURA_JANELA / 2:
        obj_bola['dir_y'] *= -1
        bola.goto(x, -ALTURA_JANELA / 2 + RAIO_BOLA)

    # Parede esquerda (fora da zona da baliza)
    if x - RAIO_BOLA <= -LARGURA_JANELA / 2 and abs(y) > LADO_MAIOR_AREA / 2:
        obj_bola['dir_x'] *= -1
        bola.goto(-LARGURA_JANELA / 2 + RAIO_BOLA, bola.ycor())

    # Parede direita (fora da zona da baliza)
    if x + RAIO_BOLA >= LARGURA_JANELA / 2 and abs(y) > LADO_MAIOR_AREA / 2:
        obj_bola['dir_x'] *= -1
        bola.goto(LARGURA_JANELA / 2 - RAIO_BOLA, bola.ycor())


def verifica_golo_jogador_vermelho(estado_jogo):
    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]_ja_[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma
    ',', e cada coordenada é separada por um ';'.
    '''
    if estado_jogo['bola'] is None:
        return

    obj_bola = estado_jogo['bola']
    bola = obj_bola['objeto']
    x = bola.xcor()
    y = bola.ycor()

    # Bola entrou na baliza direita (jogador vermelho marca golo)
    if x + RAIO_BOLA >= LARGURA_JANELA / 2 - LADO_MENOR_AREA and abs(y) <= START_POS_BALIZAS:
        estado_jogo['pontuacao_jogador_vermelho'] += 1

        nome = (f'replay_golo_jv_{estado_jogo["pontuacao_jogador_vermelho"]}'
                f'_ja_{estado_jogo["pontuacao_jogador_azul"]}.txt')
        with open(nome, 'w') as f:
            f.write(';'.join(f'{p[0]:.3f},{p[1]:.3f}' for p in estado_jogo['var']['bola']) + '\n')
            f.write(';'.join(f'{p[0]:.3f},{p[1]:.3f}' for p in estado_jogo['var']['jogador_vermelho']) + '\n')
            f.write(';'.join(f'{p[0]:.3f},{p[1]:.3f}' for p in estado_jogo['var']['jogador_azul']) + '\n')

        estado_jogo['var']['bola'] = []
        estado_jogo['var']['jogador_vermelho'] = []
        estado_jogo['var']['jogador_azul'] = []

        update_board(estado_jogo)

        bola.goto(BOLA_START_POS)
        obj_bola['dir_x'] = random.choice([-1, 1]) * VELOCIDADE_BOLA
        obj_bola['dir_y'] = random.choice([-1, 1]) * VELOCIDADE_BOLA

def verifica_golo_jogador_azul(estado_jogo):
    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]_ja_[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.
    '''
    if estado_jogo['bola'] is None:
        return

    obj_bola = estado_jogo['bola']
    bola = obj_bola['objeto']
    x = bola.xcor()
    y = bola.ycor()

    # Bola entrou na baliza esquerda (jogador azul marca golo)
    if x - RAIO_BOLA <= -LARGURA_JANELA / 2 + LADO_MENOR_AREA and abs(y) <= START_POS_BALIZAS:
        estado_jogo['pontuacao_jogador_azul'] += 1

        nome = (f'replay_golo_jv_{estado_jogo["pontuacao_jogador_vermelho"]}'
                f'_ja_{estado_jogo["pontuacao_jogador_azul"]}.txt')
        with open(nome, 'w') as f:
            f.write(';'.join(f'{p[0]:.3f},{p[1]:.3f}' for p in estado_jogo['var']['bola']) + '\n')
            f.write(';'.join(f'{p[0]:.3f},{p[1]:.3f}' for p in estado_jogo['var']['jogador_vermelho']) + '\n')
            f.write(';'.join(f'{p[0]:.3f},{p[1]:.3f}' for p in estado_jogo['var']['jogador_azul']) + '\n')

        estado_jogo['var']['bola'] = []
        estado_jogo['var']['jogador_azul'] = []
        estado_jogo['var']['jogador_vermelho'] = []

        update_board(estado_jogo)

        bola.goto(BOLA_START_POS)
        obj_bola['dir_x'] = random.choice([-1, 1]) * VELOCIDADE_BOLA
        obj_bola['dir_y'] = random.choice([-1, 1]) * VELOCIDADE_BOLA


def verifica_golos(estado_jogo):
    verifica_golo_jogador_vermelho(estado_jogo)
    verifica_golo_jogador_azul(estado_jogo)


def verifica_toque_jogador_azul(estado_jogo):
    '''
    Função responsável por verificar se o jogador tocou na bola.
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    if estado_jogo['bola'] is None:
        return

    obj_bola = estado_jogo['bola']
    bola = obj_bola['objeto']
    jogador = estado_jogo['jogador_azul']

    if bola.distance(jogador) < RAIO_BOLA + RAIO_JOGADOR:
        dx = bola.xcor() - jogador.xcor()
        dy = bola.ycor() - jogador.ycor()
        if abs(dx) >= abs(dy):
            obj_bola['dir_x'] *= -1
        else:
            obj_bola['dir_y'] *= -1


def verifica_toque_jogador_vermelho(estado_jogo):
    '''
    Função responsável por verificar se o jogador tocou na bola.
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    if estado_jogo['bola'] is None:
        return

    obj_bola = estado_jogo['bola']
    bola = obj_bola['objeto']
    jogador = estado_jogo['jogador_vermelho']

    if bola.distance(jogador) < RAIO_BOLA + RAIO_JOGADOR:
        dx = bola.xcor() - jogador.xcor()
        dy = bola.ycor() - jogador.ycor()
        if abs(dx) >= abs(dy):
            obj_bola['dir_x'] *= -1
        else:
            obj_bola['dir_y'] *= -1

def guarda_posicoes_para_var(estado_jogo):
    estado_jogo['var']['bola'].append(estado_jogo['bola']['objeto'].pos())
    estado_jogo['var']['jogador_vermelho'].append(estado_jogo['jogador_vermelho'].pos())
    estado_jogo['var']['jogador_azul'].append(estado_jogo['jogador_azul'].pos())


def main():
    estado_jogo = init_state()
    setup(estado_jogo, True)
    while True:
        estado_jogo['janela'].update()
        if estado_jogo['bola'] is not None:
            movimenta_bola(estado_jogo)
        verifica_colisoes_ambiente(estado_jogo)
        guarda_posicoes_para_var(estado_jogo)
        verifica_golos(estado_jogo)
        if estado_jogo['jogador_vermelho'] is not None:
            verifica_toque_jogador_azul(estado_jogo)
        if estado_jogo['jogador_azul'] is not None:
            verifica_toque_jogador_vermelho(estado_jogo)

if __name__ == '__main__':
    main()