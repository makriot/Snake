import pygame

pygame.init()

class Snake:

    def __init__(self, sur, color, size, z, control, step):
        self.all_positions = [z]
        self.flag_to_draw = False
        self.flag_tail = False
        self.sur = sur
        self.color = color
        self.size = size
        self.head_x = z[0]
        self.head_y = z[1]
        self.k =int(control/step)
        self.k_1 = self.k
        self.count = 1

    def move(self, delta_x, delta_y, flag=False):
        if flag:
            self.flag_tail = True
            self.flag_to_draw = True
        if len(self.all_positions) == 1:
            self.flag_tail = True

        if self.flag_to_draw or self.flag_tail:
            self.count += 1
            z = self.all_positions[0]
            self.all_positions = [[z[0]+delta_x, z[1]+delta_y]] + self.all_positions

            self.k_1 -= 1
            if self.flag_to_draw:
                self.flag_to_draw = False
            else:
                if self.flag_tail and self.k_1==0:
                    self.flag_tail = False
                    self.k_1 = self.k

        else:
            z = self.all_positions[0]
            self.all_positions = [[z[0] + delta_x, z[1] + delta_y]] + self.all_positions[:-1]
        self.head_x = self.all_positions[0][0]
        self.head_y = self.all_positions[0][1]
        self.count += 1

    def draw(self):
        if self.flag_to_draw:
            l = self.count
            l -= l%self.k
            for n,i in enumerate(self.all_positions):
                if n<=l:
                    x = i[0]
                    y = i[1]
                    pygame.draw.polygon(self.sur, self.color,
                                        ((x - self.size, y - self.size), (x + self.size, y - self.size),
                                         (x + self.size, y + self.size), (x - self.size, y + self.size)))
        elif len(self.all_positions)<=self.k:
            x = self.head_x
            y = self.head_y
            pygame.draw.polygon(self.sur, self.color,
                                ((x - self.size, y - self.size), (x + self.size, y - self.size),
                                 (x + self.size, y + self.size), (x - self.size, y + self.size)))
        else:
            l = len(self.all_positions[:-self.k])
            l -= l%self.k
            for n,i in enumerate(self.all_positions[:-self.k]):
                if n<=l:
                    x = i[0]
                    y = i[1]
                    pygame.draw.polygon(self.sur, self.color,
                                        ((x - self.size, y - self.size), (x + self.size, y - self.size),
                                         (x + self.size, y + self.size), (x - self.size, y + self.size)))
        pygame.display.update()