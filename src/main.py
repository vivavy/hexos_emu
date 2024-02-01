from display import *
from wm import *


display.create()

window = Window((16, 32+48), Vector2(1920-32, 1080-160), ["inactive", "active", "inactive", "inactive"], 1,
                bg=(60,) * 3, bbg=(30,) * 3, line=(96,)*3)

window.surface.fill((60,) * 3)

window.surface.blit(window.title_font.render("Unavailable now, try `upgrade hexos_emu`", 1, (255,)*3), (32, 32))
window.surface.blit(window.title_font.render("Press [ESC] for exit",
                                             1, (255,)*3), (32, 40+window.title_font.get_height()))

panel = Panel()

bg = transform.smoothscale(image.load("images/default.png"), display.get_size())

run = 1

FPS = 114

clock = time.Clock()

while run:
    clock.tick(FPS)

    for e in event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                run = 0
    
    display.surface.blit(bg, (-1, 0))

    window.render()

    panel.render()

    display.flip()
