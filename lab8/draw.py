import pygame

WIDTH, HEIGHT = 1200, 800
FPS = 90
draw = False
radius = 2
color = 'blue'
mode = 'pen'
lastPos = (0, 0)

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
screen.fill('white')
font = pygame.font.SysFont('None', 60)


def drawLine(screen, start, end, width, color):
    pygame.draw.line(screen, color, start, end, width)


def drawCircle(screen, start, end, width, color):
    x = (start[0] + end[0]) // 2
    y = (start[1] + end[1]) // 2
    radius = abs(start[0] - end[0]) // 2
    pygame.draw.circle(screen, color, (x, y), radius, width)


def drawRectangle(screen, start, end, width, color):
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                       abs(start[0] - end[0]), abs(start[1] - end[1]))
    pygame.draw.rect(screen, color, rect, width)


def drawSquare(screen, start, end, color):
    size = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], size, size)
    pygame.draw.rect(screen, color, rect)


def drawRightTriangle(screen, start, end, color):
    points = [(start[0], start[1]), (end[0], end[1]), (start[0], end[1])]
    pygame.draw.polygon(screen, color, points)


def drawEquilateralTriangle(screen, start, end, width, color):
    base = abs(end[0] - start[0])
    height = (3**0.5) * base / 2
    if end[1] > start[1]:
        points = [(start[0], end[1]), (end[0], end[1]), ((start[0] + end[0]) // 2, end[1] - height)]
    else:
        points = [(start[0], start[1]), (end[0], start[1]), ((start[0] + end[0]) // 2, start[1] - height)]
    pygame.draw.polygon(screen, color, points, width)


def drawRhombus(screen, start, end, width, color):
    points = [((start[0] + end[0]) // 2, start[1]), (start[0], (start[1] + end[1]) // 2),
              ((start[0] + end[0]) // 2, end[1]), (end[0], (start[1] + end[1]) // 2)]
    pygame.draw.polygon(screen, color, points, width)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rectangle'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_p:
                mode = 'pen'
            if event.key == pygame.K_e:
                mode = 'erase'
            if event.key == pygame.K_s:
                mode = 'square'
            if event.key == pygame.K_t:
                mode = 'right_tri'
            if event.key == pygame.K_u:
                mode = 'eq_tri'
            if event.key == pygame.K_h:
                mode = 'rhombus'
            if event.key == pygame.K_q:
                screen.fill('white')

            if event.key == pygame.K_1:
                color = 'black'
            if event.key == pygame.K_2:
                color = 'green'
            if event.key == pygame.K_3:
                color = 'red'
            if event.key == pygame.K_4:
                color = 'blue'
            if event.key == pygame.K_5:
                color = 'yellow'

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            lastPos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if mode == 'rectangle':
                drawRectangle(screen, lastPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, lastPos, event.pos, radius, color)
            elif mode == 'square':
                drawSquare(screen, lastPos, event.pos, color)
            elif mode == 'right_tri':
                drawRightTriangle(screen, lastPos, event.pos, color)
            elif mode == 'eq_tri':
                drawEquilateralTriangle(screen, lastPos, event.pos, radius, color)
            elif mode == 'rhombus':
                drawRhombus(screen, lastPos, event.pos, radius, color)
            draw = False

        if event.type == pygame.MOUSEMOTION:
            if draw and mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)
            elif draw and mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, 'white')
            lastPos = event.pos

    # Show radius
    pygame.draw.rect(screen, 'white', (5, 5, 115, 75))
    renderRadius = font.render(str(radius), True, color)
    screen.blit(renderRadius, (5, 5))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
