import pygame
pygame.init()
branco = (255,255,255)
tamanho = (400,291)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("icone.png")
pygame.display.set_icon( icone )
fundo  = pygame.image.load("fundo.jpg")
mario = pygame.image.load("mario.png")
casquinha = pygame.image.load("shell.png")
pygame.display.set_caption("Jogo do Mario")
running = True
eixoXMario = 200
movimentoXMario = 0
pygame.mixer.music.load("trilha.mp3")
pygame.mixer.music.play(-1)
pular = False
gravidade = False
eixoYMario = 211
eixoXCasquinha = 410
direcaoCasquina = True
velocidadeCasquinha = 5
font = pygame.font.Font(None, 36)
pontos = 0
alturaCasquina = 40
larguraCasquina = 46
alturaMario = 48
larguraMario = 48
dificuldade = 20
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            movimentoXMario = -5
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            movimentoXMario = 0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            movimentoXMario = 5
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            movimentoXMario = 0
        elif event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pular = True


    tela.fill(branco)
    tela.blit( fundo, (0,0) )

    if eixoXMario > 355:
        eixoXMario = 355
    elif eixoXMario < 0:
        eixoXMario = 0 


    eixoXMario = eixoXMario + movimentoXMario
    if pular:
        if eixoYMario < 140:
            gravidade = True

        if gravidade :
            eixoYMario = eixoYMario + 5 
            if eixoYMario >= 211:
                pular = False
                gravidade = False
        else:
            eixoYMario = eixoYMario - 5 
    tela.blit( mario, (eixoXMario, eixoYMario) )
    tela.blit( casquinha, (eixoXCasquinha, 235) )
    if direcaoCasquina:
        eixoXCasquinha = eixoXCasquinha - velocidadeCasquinha
    else:
        eixoXCasquinha = eixoXCasquinha + velocidadeCasquinha

    if eixoXCasquinha < 0:
        direcaoCasquina = False
        #velocidadeCasquinha = velocidadeCasquinha + 1
        pontos  = pontos + 1
    elif eixoXCasquinha > 400:
        direcaoCasquina = True
        #velocidadeCasquinha = velocidadeCasquinha + 1
        pontos  = pontos + 1
    

    texto = font.render("Pontos: "+str(pontos), True, (0,0,0))
    tela.blit( texto, (10, 10) )

    pixelsYMario = list(
                range(eixoYMario, eixoYMario + alturaMario+1))
    pixelsXMario = list(
        range(eixoXMario, eixoXMario + larguraMario+1))

    pixelsYCasquina = list(range(235, 235+alturaCasquina+1))
    pixelsXCasquina = list(range(eixoXCasquinha, eixoXCasquinha+larguraMario+1))
    if len(list(set(pixelsYMario) & set(pixelsYCasquina))) > dificuldade:
        if len(list(set(pixelsXMario) & set(pixelsXCasquina))) > dificuldade:
            running = False
            print("Morreu!")

    pygame.display.update()
    clock.tick(40)
    
pygame.quit()
