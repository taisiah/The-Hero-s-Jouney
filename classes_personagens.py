import pygame

class Heroi(pygame.sprite.Sprite):
    # Essa classe representa o personagem e deriva da classe "Sprite" do Pygame.
    def __init__(self):
        # Chama o construtor do "Sprite"
        super().__init__()
        #estados do boneco: escondido, andando_dir, andando_esq, pulando, parado etc
        self.estado = "escondido"

        self.direcao = "esquerda" #direção que o personagem está"

        self.movimento = "" #movimento que o personagem realizou

        self.tempo_mov = 0

        self.vida  = 3

        # carrega a figura do personagem
        self.image = pygame.image.load("imagens/andar1_e.png").convert_alpha()

        # Obtem o retângulo que possui as dimensões da imagem .
        self.rect = self.image.get_rect()
    # Criação de metodos para a movimentação do boneco
    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def moveJumpup_d(self, pixels):
        self.rect.y -= pixels
        self.rect.x += pixels

    def moveJumpdown_d(self,pixels):
        self.rect.y += pixels
        self.rect.x += pixels

    def moveJumpup_e (self,pixels):
        self.rect.y -= pixels
        self.rect.x -= pixels

    def moveJumpdown_e(self,pixels):
        self.rect.y += pixels
        self.rect.x -= pixels

class Inimigo(pygame.sprite.Sprite):
    # Essa classe representa o personagem e deriva da classe "Sprite" do Pygame.
    def __init__(self):
        # Chama o construtor do "Sprite"
        super().__init__()

        #estados do boneco: escondido, andando_dir, andando_esq, pulando, parado etc
        self.estado = "escondido"

        self.lista_inimigos = []

        self.indiceInimigo = 0  #indice do vetor Inimigo
        self.lista_inimigos = [pygame.image.load("imagens/golemterra1_d.png").convert_alpha()]

        self.movimento =""

        self.tempo_mov = 0

        self.image = self.lista_inimigos[self.indiceInimigo]

        # Obtem o retângulo que possui as dimensões da imagem .
        self.rect = self.image.get_rect()

    # Criação de metodos para a movimentação do boneco
    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

class Feiticeiro(pygame.sprite.Sprite):
    # Essa classe representa o personagem e deriva da classe "Sprite" do Pygame.
    def __init__(self):
        # Chama o construtor do "Sprite"
        super().__init__()

        # estados do boneco: escondido, andando_dir, andando_esq, pulando, parado etc
        self.estado = "escondido"

        self.movimento = ""

        self.tempo_mov = 0

        self.image = pygame.image.load ("imagens/andar1_e.png").convert_alpha()

        # Obtem o retângulo que possui as dimensões da imagem .
        self.rect = self.image.get_rect()

    # Criação de metodos para a movimentação do boneco
    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels
