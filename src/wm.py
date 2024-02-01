from display import *


TITLE_HEIGHT = 64
TITLE_FONT_SIZE = 28
TITLE_FONT_FAMILY = "Fira Code"


class Window:
    bg = (255,) * 3
    bbg = (0,) * 3
    line = (255,) * 3
    title_text_color = (255,) * 3

    title_font = font.SysFont(TITLE_FONT_FAMILY, TITLE_FONT_SIZE)

    def __init__(self, pos, size, tabs, active, **k):
        self.pos, self.size, self.tabs, self.active = Vector2(pos), Vector2(size), tabs, active
        self.surface = Surface(self.size).convert()
        self.surface.fill((255,)*3)
        self.update = True
        self.__dict__.update(k)
        self.tabs_cache_textures = []

        for text in self.tabs:
            self.tabs_cache_textures.append(self.title_font.render(text, 1, self.title_text_color))
    
    def render(self):
        sc = display.surface

        draw.rect(sc, self.bbg, (*self.pos, *self.size), 0, 8)
        draw.line(sc, self.line, (self.pos.x, self.pos.y + TITLE_HEIGHT),
                  (self.pos.x + self.size.x, self.pos.y + TITLE_HEIGHT), 1)

        for n, t in enumerate(self.tabs_cache_textures):
            if self.active == n:
                draw.rect(sc, self.bg,
                    (self.pos.x + n * self.size.x / len(self.tabs), self.pos.y,
                    self.size.x / len(self.tabs), TITLE_HEIGHT), 0, -1, 8, 8)
                sc.blit(t, (self.pos.x + n * self.size.x / len(self.tabs), self.pos.y) +
                        Vector2(self.size.x / len(self.tabs), TITLE_HEIGHT) / 2 - Vector2(t.get_size()) / 2)
            else:
                sc.blit(t, (self.pos.x + n * self.size.x / len(self.tabs), self.pos.y) +
                        Vector2(self.size.x / len(self.tabs), TITLE_HEIGHT) / 2 - Vector2(t.get_size()) / 2)
            
        if self.update:
            mask = Surface(self.surface.get_size(), SRCALPHA)
            draw.rect(mask, Color("white"), (0, 0, *self.size), 0, -1, -1, -1, 8, 8)
            mask.blit(self.surface, (0, 0), None, BLEND_RGBA_MULT)
            sc.blit(mask, self.pos + Vector2(0, TITLE_HEIGHT))


class Panel(object):
    def render(self):
        sc = display.surface

        draw.rect(sc, (60,) * 3, (16, 16, display.get_size().x - 32, 48), 0, 8)


class WM(object):
    def __init__(self):
        super().__init__()

        self.windows = []

    def render(self):
        for w in self.windows:
            w.render()
