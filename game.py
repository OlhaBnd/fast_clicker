import pygame
import time

pygame.init()
back = (204, 255, 255)

mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

class Area():
    def __init__(self, x = 0, y=0, width=10, height=10, color =None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)



class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    
    def draw(self, shift_x=0, shift_y =0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


YELLOW = (255, 255, 102)
DARK_BLUE = (0, 0, 153)
BLUE =(153, 204, 255)

cards = []
num_cards = 4
x = 70

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('Click', 26)
    cards.append(new_card)
    x += 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for card in cards:
        card.draw(10,30)

    pygame.display.update()
    clock.tick(40)





