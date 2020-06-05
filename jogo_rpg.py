import pygame, sys
from classes_personagens import *



# Comando para iniciar o pygame.
pygame.init()

# variáveis(largura e altura) definidas de acordo com o tamanho da imagem da tela inicial.
largura = 800
altura = 600
size = (largura, altura)

#variáveis globais
jogar = True
fase = -2
contador = 0 #controla o movimento do personagem
pulo_vertical = False # variável global para saber tipo do pulo
inicio = False
game_over = False
#variáveis de controle da tela
tela_file = "imagens/telainicial.jpg"
janela = pygame.display.set_mode((size))  # Módulo que inicializa uma janela ou tela para exibição.
golem_morto = 0
pegouchave = False
feiticeiromorto = False
venceu = False


#cria os inimigos
lista_golem = []
for i in range (3):
    lista_golem.append(Inimigo())

# Essa é a lista dos sprites dos inimigos
lista_inimigo = pygame.sprite.Group()

# Adiciona os inimigos na lista de sprites
for i in range (3):
    lista_inimigo.add(lista_golem[i])

#contador de passos dos golems
cont_passos_golem = [0,0,0]

#cria o personagem heroi
heroi = Heroi()

# Essa é a lista de todos os sprites herói usados no jogo
grupo_heroi = pygame.sprite.Group()

# Adiciona o heroi na lista de objetos
grupo_heroi.add(heroi)

#cria o personagem feiticeiro
feiticeiro = Feiticeiro ()

# Essa é a lista de todos os sprites feiticeiro usados no jogo
grupo_feiticeiro = pygame.sprite.Group()

# Adiciona o feiticeiro na lista de objetos
grupo_feiticeiro.add(feiticeiro)

vida_image = pygame.image.load("imagens/vida.png")
mensagem1 = pygame.image.load("imagens/msg_icon.png")
chave = pygame.image.load ("imagens/chave.png")

#adiciona audio ao jogo
pygame.mixer.init()
pygame.mixer.music.load('bgsound.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


def display_telainicial():
    global tela_file
    pygame.display.set_caption("The Hero's Journey")  # Módulo que define uma legenda para a tela inicial.
    #Tela de Início
    gameIcon = pygame.image.load("imagens/logo_ico.ico")  # Módulo que carrega uma imagem de um arquivo - (imagem da Logotipo).
    pygame.display.set_icon(gameIcon)  # Alterando o ícone do sistema
    telainicial = pygame.image.load(tela_file)
    janela.blit(telainicial, (0, 0))  # Blit : Módulo que desenha uma imagem na outra .

def handle_events():
    global jogar
    global fase
    global heroi
    global contador
    global inicio
    global feiticeiromorto
    global venceu

    for event in pygame.event.get():  # Obtendo todos os eventos que estão acontecendo nesse exato momento.
        if event.type == pygame.QUIT:  # Quit Para fechar janela ou tela. Quando o usuário clicar no X ou qualquer outra tecla para sair do jogo, vai transformar a variável sair em False, quebrando o loop infinito.
            jogar = False
        if event.type == pygame.KEYDOWN:
            if fase == -2 and event.key == pygame.K_RETURN:
                fase = -1
            elif fase == -1 and event.key == pygame.K_RETURN:
                fase = 0
            elif fase == 0 and event.key == pygame.K_RETURN: # Saída tela inicial e início do jogo
                fase = 1
                inicio = True
                heroi.estado = "parado"
                heroi.rect.x = 710#largura - 710
                heroi.rect.y = 470#altura - 470
                for i in range(3):
                    lista_golem[i].estado = "parado"
                    lista_golem[i].movimento = "direita"
                    lista_golem[i].tempo_mov = 200
                lista_golem[0].rect.x = 50
                lista_golem[0].rect.y= 470
                lista_golem[1].rect.x = 110
                lista_golem[1].rect.y = 210
                lista_golem[2].rect.x = 430
                lista_golem[2].rect.y = 270
                if fase == 1:
                    for i in range(3):
                        lista_golem[i].inimigo1 = pygame.image.load("imagens/golemterra1_d.png").convert_alpha()
                        lista_golem[i].inimigo2 = pygame.image.load("imagens/golemterra2_d.png").convert_alpha()
                        lista_golem[i].inimigo3 = pygame.image.load("imagens/golemterra1_e.png").convert_alpha()
                        lista_golem[i].inimigo4 = pygame.image.load("imagens/golemterra2_e.png").convert_alpha()
                        lista_golem[i].lista_inimigos = [lista_golem[i].inimigo1, lista_golem[i].inimigo2, lista_golem[i].inimigo3, lista_golem[i].inimigo4]

            elif fase == 2 and event.key == pygame.K_RETURN:
                fase= 3
                feiticeiro.rect.x = 650
                feiticeiro.rect.y = 455
                for i in range(3):
                    lista_inimigo.add(lista_golem[i])
                heroi.estado = "parado"
                heroi.rect.x = 40
                heroi.rect.y = 55
                for i in range(3):
                    lista_golem[i].estado = "parado"
                    lista_golem[i].movimento = "direita"
                    lista_golem[i].tempo_mov = 200
                lista_golem[0].rect.x = 280
                lista_golem[0].rect.y= 60
                lista_golem[1].rect.x = 450
                lista_golem[1].rect.y = 265
                lista_golem[2].rect.x = 100
                lista_golem[2].rect.y = 460
                if fase == 3:
                    for i in range(3):
                        lista_golem[i].inimigo1 = pygame.image.load("imagens/golemfogo1_d.png").convert_alpha()
                        lista_golem[i].inimigo2 = pygame.image.load("imagens/golemfogo2_d.png").convert_alpha()
                        lista_golem[i].inimigo3 = pygame.image.load("imagens/golemfogo1_e.png").convert_alpha()
                        lista_golem[i].inimigo4 = pygame.image.load("imagens/golemfogo2_e.png").convert_alpha()
                        lista_golem[i].lista_inimigos = [lista_golem[i].inimigo1, lista_golem[i].inimigo2, lista_golem[i].inimigo3, lista_golem[i].inimigo4]

            elif fase >= 1 and event.key == pygame.K_LEFT:# validação para caso seja clicado a seta para esquerda
                contador += 1
                movimentacao(event.key, contador)
            elif fase >= 1 and event.key == pygame.K_RIGHT: # validação para caso seja clicado a seta para direita
                contador += 1
                movimentacao(event.key, contador)
            elif fase >= 1 and event.key == pygame.K_UP:# validação para caso seja clicado a seta para cima
                contador += 1
                movimentacao(event.key, contador)
            elif fase >= 1 and event.key == pygame.K_DOWN:# validação para caso seja clicado a seta para baixo
                contador += 1
                movimentacao(event.key, contador)
            elif fase >= 1 and event.key == pygame.K_LALT: # validação para caso seja clicado para atacar (botão ALT esquerdo)
                movimentacao(event.key)
            elif fase >=1 and event.key == pygame.K_SPACE:
                movimentacao(event.key)

def mov_tempo (dt):
    global pulo_vertical
    global cont_passos_golem
    global game_over
    global jogar
    global golem_morto
    global feiticeiromorto



    for i in range (3):
        if lista_golem[i].movimento == "morto":
            lista_golem[i].kill()

    if feiticeiromorto == True:
        feiticeiro.kill()

    if heroi.direcao == "morto" and fase ==1 :
        pygame.time.delay(1000)
        heroi.rect.x = 710
        heroi.rect.y = 470
        heroi.direcao ="esquerda"
        heroi.estado = "parado"
        heroi.image = pygame.image.load("imagens/andar1_e.png").convert_alpha()
        if heroi.vida == 0 :
            game_over = True
            jogar = False

    if heroi.direcao == "morto" and fase == 3 :
        pygame.time.delay(1000)
        heroi.rect.x = 40
        heroi.rect.y = 55
        heroi.direcao ="direita"
        heroi.estado = "parado"
        heroi.image = pygame.image.load("imagens/andar1_d.png").convert_alpha()
        if heroi.vida == 0 :
            game_over = True
            jogar = False

    for i in range (3):
        if lista_golem[i].rect.colliderect(heroi.rect):
            if heroi.movimento == "ataque" and ((heroi.direcao == "esquerda" and lista_golem[i].movimento == "direita") or\
                (heroi.direcao == "direita" and lista_golem[i].movimento == "esquerda")):
                lista_golem[i].image = pygame.image.load("imagens/golem_morto.png").convert_alpha()
                lista_golem[i].movimento = "morto"
                golem_morto += 1


            elif  lista_golem[i].movimento != "morto" and heroi.direcao != "morto":
                heroi.vida -= 1
                if heroi.direcao == "esquerda":
                    heroi.image=pygame.image.load ("imagens/morte_e.png").convert_alpha()
                else:
                    heroi.image = pygame.image.load("imagens/morte_d.png").convert_alpha()
                heroi.direcao = "morto"

    if feiticeiromorto == False and heroi.direcao != "morto" and  feiticeiro.rect.colliderect(heroi.rect):
        if heroi.movimento == "ataque":
            feiticeiromorto = True
        else:
            heroi.vida -= 1
            heroi.direcao = "morto"
            

    if (heroi.movimento == "ataque"):
        heroi.tempo_mov -= dt
        if heroi.tempo_mov <= 0:
            heroi.movimento = ""
            if heroi.direcao == "esquerda":
                heroi.image = pygame.image.load("imagens/andar1_e.png").convert_alpha()
            else:
                heroi.image = pygame.image.load("imagens/andar1_d.png").convert_alpha()
    if (heroi.movimento =="pulo"):
        heroi.tempo_mov -= dt
        if heroi.tempo_mov <= 0:
            heroi.movimento = ""
            if pulo_vertical == False :
                if heroi.direcao == "esquerda":
                    if heroi.rect.y == 370:
                        heroi.moveJumpdown_e(100)
                        heroi.image = pygame.image.load("imagens/andar1_e.png").convert_alpha()
                    elif heroi.rect.y==170:
                        heroi.moveJumpdown_e(40)
                        heroi.image = pygame.image.load("imagens/andar1_e.png").convert_alpha()
                else:
                    if heroi.rect.y==370:
                        heroi.moveJumpdown_d(100)
                        heroi.image = pygame.image.load("imagens/andar1_d.png").convert_alpha()
                    elif heroi.rect.y == 110:
                        heroi.moveJumpdown_d(160)
                        heroi.image = pygame.image.load("imagens/andar1_d.png").convert_alpha()
            else:
                heroi.moveDown(100)
                pulo_vertical = False
    for i in range(3):
        if (lista_golem[i].movimento == "direita"):
            lista_golem[i].tempo_mov -=dt
            if cont_passos_golem[i] == 8 :
                lista_golem[i].movimento = "esquerda"
                lista_golem[i].tempo_mov = 200
                cont_passos_golem[i] = 0
            if lista_golem[i].tempo_mov <= 0:
                cont_passos_golem[i] += 1
                lista_golem[i].tempo_mov = 200
                if cont_passos_golem[i] % 2 == 0 :
                    lista_golem[i].image = lista_golem[i].lista_inimigos[0]
                else:
                    lista_golem[i].image = lista_golem[i].lista_inimigos[1]
                lista_golem[i].moveRight(20)
        elif (lista_golem[i].movimento== "esquerda"):
            lista_golem[i].tempo_mov -=dt
            if cont_passos_golem[i] == 8 :
                lista_golem[i].movimento = "direita"
                lista_golem[i].tempo_mov = 200
                cont_passos_golem[i] = 0
            if lista_golem[i].tempo_mov <= 0:
                cont_passos_golem[i] += 1
                lista_golem[i].tempo_mov = 200
                if cont_passos_golem[i] % 2 == 0 :
                    lista_golem[i].image = lista_golem[i].lista_inimigos[2]
                else:
                    lista_golem[i].image = lista_golem[i].lista_inimigos[3]
                lista_golem[i].moveLeft(20)
    if pegouchave == True :
        feiticeiro.tempo_mov -= dt
        if feiticeiro.tempo_mov <= 0:
            feiticeiro.tempo_mov = 200
            if feiticeiro.estado == "1":
                feiticeiro.image = pygame.image.load("imagens/feiticeiro2.png").convert_alpha()
                feiticeiro.estado = "2"
            else:
                feiticeiro.image = pygame.image.load("imagens/feiticeiro1.png").convert_alpha()
                feiticeiro.estado = "1"




# função responsável por movimentar o heroi, onde ira receber como entrada, o evento do teclado e um contador para que seja alternado a imagem
def movimentacao(key, quantidade=0):
    global pulo_vertical
    global fase
    global pegouchave
    global venceu
    global jogar
    global feiticeiromorto


    if fase == 1:
        if key == pygame.K_LEFT:
            if heroi.rect.x > 0 :
                if heroi.rect.y == 470 or (heroi.rect.y==210  and heroi.rect.x >50 and heroi.rect.x <=290) or \
                        (heroi.rect.y==50 and heroi.rect.x>50 and heroi.rect.x<=210) or  \
                        (heroi.rect.y==270 and heroi.rect.x >370 and heroi.rect.x <= 670) or \
                        (heroi.rect.y==90 and heroi.rect.x >510 and heroi.rect.x <= 670):
                    if quantidade % 2 == 0:
                        heroi.image = pygame.image.load("imagens/andar1_e.png").convert_alpha()
                    elif quantidade % 2 == 1:
                        heroi.image = pygame.image.load("imagens/andar2_e.png").convert_alpha()
                    heroi.moveLeft(20)
                heroi.direcao = "esquerda"
        if key == pygame.K_RIGHT:
            if heroi.rect.x < 730:
                if heroi.rect.y == 470 or (heroi.rect.y==210 and heroi.rect.x >=50 and heroi.rect.x <290) or \
                        (heroi.rect.y==50 and heroi.rect.x>=50 and heroi.rect.x<210) or\
                        (heroi.rect.y==270 and heroi.rect.x >=370 and heroi.rect.x < 670) or \
                        (heroi.rect.y==90 and heroi.rect.x >=510 and heroi.rect.x < 670):
                    if quantidade % 2 == 0:
                        heroi.image = pygame.image.load("imagens/andar1_d.png").convert_alpha()
                    elif quantidade % 2 == 1:
                        heroi.image = pygame.image.load("imagens/andar2_d.png").convert_alpha()
                    heroi.moveRight(20)
                heroi.direcao = "direita"
        if key == pygame.K_UP :
            if (heroi.rect.x==50 and heroi.rect.y >50) or (heroi.rect.y==650 and heroi.rect.x==270) or\
                    ( heroi.rect.x == 670 and heroi.rect.y > 90 and heroi.rect.y <=270 ) :
                if quantidade % 2 == 0:
                    heroi.image = pygame.image.load("imagens/subida1.png").convert_alpha()
                elif quantidade % 2 == 1:
                    heroi.image = pygame.image.load("imagens/subida2.png").convert_alpha()
                heroi.moveUp(20)
        if key == pygame.K_DOWN :
            if (heroi.rect.y < 470):
                if (heroi.rect.x==50 and heroi.rect.y>=50) or (heroi.rect.y==650 and heroi.rect.x==270) or \
                        (heroi.rect.y >=90 and heroi.rect.y <270 and heroi.rect.x==670):
                    if quantidade % 2 == 0:
                        heroi.image = pygame.image.load("imagens/subida1.png").convert_alpha()
                    elif quantidade % 2 == 1:
                        heroi.image = pygame.image.load("imagens/subida2.png").convert_alpha()
                    heroi.moveDown(20)
        if key == pygame.K_LALT:
            if heroi.rect.y == 470 or heroi.rect.y ==210 or  heroi.rect.y ==270:
                if heroi.direcao == "esquerda" :
                    heroi.image = pygame.image.load("imagens/atacar_e.png").convert_alpha()
                    heroi.moveRight(-40)
                elif heroi.direcao == "direita" :
                    heroi.image = pygame.image.load("imagens/atacar_d.png").convert_alpha()
                    heroi.moveRight(40)
                heroi.movimento = "ataque"
                heroi.tempo_mov = 300

        if key == pygame.K_SPACE :
            if heroi.movimento == "":
                if (heroi.rect.y == 470) or (heroi.rect.y == 210 and heroi.rect.x >=190 and heroi.direcao == "direita") or (heroi.rect.y == 270 and heroi.rect.x <= 430 and heroi.direcao == "esquerda"):
                    if heroi.direcao == "esquerda":
                        heroi.image = pygame.image.load("imagens/pulo_e.png").convert_alpha()
                        heroi.moveJumpup_e(100)
                    elif heroi.direcao == "direita":
                        heroi.image = pygame.image.load("imagens/pulo_d.png").convert_alpha()
                        heroi.moveJumpup_d(100)
                else:
                    heroi.moveUp(100)
                    pulo_vertical = True

            heroi.movimento = "pulo"
            heroi.tempo_mov = 200

    if fase == 3:
        if key == pygame.K_LEFT:
            if heroi.rect.x > 0 :
                if heroi.rect.y == 55 or (heroi.rect.y == 255 and heroi.rect.x >= 0 and heroi.rect.x <= 730) or \
                        (heroi.rect.y == 455 and heroi.rect.x >= 0 and heroi.rect.x <= 730) :
                    if quantidade % 2 == 0:
                        heroi.image = pygame.image.load("imagens/andar1_e.png").convert_alpha()
                    elif quantidade % 2 == 1:
                        heroi.image = pygame.image.load("imagens/andar2_e.png").convert_alpha()
                    heroi.moveLeft(20)
                heroi.direcao = "esquerda"
        if key == pygame.K_RIGHT:
            if heroi.rect.x < 680:
                if heroi.rect.y == 55 or (heroi.rect.y == 255 and heroi.rect.x >= 0 and heroi.rect.x <= 730) or \
                        (heroi.rect.y == 455 and heroi.rect.x >= 0 and heroi.rect.x <= 730) :
                    if quantidade % 2 == 0:
                        heroi.image = pygame.image.load("imagens/andar1_d.png").convert_alpha()
                    elif quantidade % 2 == 1:
                        heroi.image = pygame.image.load("imagens/andar2_d.png").convert_alpha()
                    heroi.moveRight(20)
                heroi.direcao = "direita"
        if key == pygame.K_UP:
            if heroi.rect.y > 55:
                if (heroi.rect.x == 460 and heroi.rect.y <= 455 ) or (heroi.rect.y >= 55 and heroi.rect.y <= 255 and heroi.rect.x == 240):
                    if quantidade % 2 == 0:
                        heroi.image = pygame.image.load("imagens/subida1.png").convert_alpha()
                    elif quantidade % 2 == 1:
                        heroi.image = pygame.image.load("imagens/subida2.png").convert_alpha()
                    heroi.moveUp(20)
        if key == pygame.K_DOWN:
            if heroi.rect.y <= 435:
                if (heroi.rect.x == 240 and heroi.rect.y >= 55 and heroi.rect.y <= 235 ) or (heroi.rect.y >= 235 and heroi.rect.x == 460):
                    if quantidade % 2 == 0:
                        heroi.image = pygame.image.load("imagens/subida1.png").convert_alpha()
                    elif quantidade % 2 == 1:
                        heroi.image = pygame.image.load("imagens/subida2.png").convert_alpha()
                    heroi.moveDown(20)
        if key == pygame.K_LALT:
            if heroi.direcao == "esquerda":
                heroi.image = pygame.image.load("imagens/atacar_e.png").convert_alpha()
                heroi.moveRight(-40)
            elif heroi.direcao == "direita":
                heroi.image = pygame.image.load("imagens/atacar_d.png").convert_alpha()
                heroi.moveRight(40)
            heroi.movimento = "ataque"
            heroi.tempo_mov = 300

        if golem_morto == 6 and fase == 3 and heroi.rect.x <= 20 and heroi.rect.y == 455:
            pegouchave = True
            feiticeiro.image = pygame.image.load("imagens/feiticeiro1.png").convert_alpha()
            feiticeiro.tempo_mov = 200

        if feiticeiromorto == True and heroi.rect.x >= 660 and heroi.rect.y == 455:
            venceu = True
            jogar = False
            feiticeiro.estado = "1"

        heroi.tempo_mov = 200



    # Game Logic
    grupo_heroi.update()
    pygame.display.flip()

def draw_heroi():
    global grupo_heroi
    global heroi
    global janela
    if heroi.estado != "escondido":
        # desenha todos os sprites da lista de bonecos
        grupo_heroi.draw(janela)
    return

def draw_inimigo():
    global lista_inimigo
    global golem
    global janela
    global pegouchave
    if lista_golem[0].estado != "escondido":
        lista_inimigo.draw(janela)
    if pegouchave == True:
        grupo_feiticeiro.draw(janela)
#atualiza tela
def update_tela():
    global fase
    global tela_file
    if fase == -2:
        tela_file="imagens/telainicial.jpg"
    elif fase == -1:
        tela_file = "imagens/abertura1.jpg"
    elif fase == 0:
        tela_file = "imagens/abertura2.jpg"
    elif fase == 1:
        tela_file="imagens/cenario1.jpg"
    elif fase == 2:
        tela_file="imagens/msg_texto.jpg"
    elif fase == 3:
        tela_file="imagens/cenario4.jpg"
    elif fase == 4:
        tela_file="imagens/cenario4.jpg"
    elif fase == 5:
        tela_file = "imagens/gameover.jpg"
    elif fase == 6:
        tela_file = "imagens/vencedor.jpg"

    return

def draw_tela():
    global tela_file
    global janela
    global fase
    global pegouchave
    tela = pygame.image.load(tela_file)
    janela.blit(tela, (0, 0))  # Blit : Módulo que desenha uma imagem na outra .
    if fase == 1 or fase == 3:
        if heroi.vida == 3:
            janela.blit(vida_image, (300, 10))
            janela.blit(vida_image, (360, 10))
            janela.blit(vida_image, (420, 10))
        elif heroi.vida == 2:
            janela.blit(vida_image, (300, 10))
            janela.blit(vida_image, (360, 10))
        elif heroi.vida == 1:
            janela.blit(vida_image, (300, 10))
    if fase ==1:
        janela.blit(mensagem1, (550, 90))
    if heroi.rect.x == 550 and heroi.rect.y == 90:
        fase = 2
        heroi.estado = "escondido"
    if pegouchave== False and fase  == 3 :
        janela.blit(chave,(40,470))
    elif pegouchave == True and fase == 3:
        janela.blit(chave, (700, 20))

    return

def desenha_elementos():
    global grupo_heroi
    global janela
    draw_tela()
    draw_heroi()
    draw_inimigo()

#função principal do jogo
def main():
    global jogar
    global inicio
    global game_over
    global fase
    global venceu

    clock = pygame.time.Clock()
    display_telainicial()

    while jogar:
        handle_events()
        update_tela()
        desenha_elementos()
        pygame.display.update()  # Permite atualizar essa parte do código.
        dt = clock.tick(50) #define o tempo de processamento FPS
        if inicio ==  True :
            mov_tempo(dt)

    if game_over == True:
        fase = 5 # 5 = game over
        update_tela()
        draw_tela()
        pygame.display.update()
        pygame.time.delay(4000)
    elif venceu == True:
        fase = 6
        update_tela()
        draw_tela()
        pygame.display.update()
        pygame.time.delay(4000)
    else:
        pygame.quit()
        sys.exit()



#inicia o jogo, chamando a função principal
main()
