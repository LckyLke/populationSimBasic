import random as rd

class Blop:
    def __init__(self, color, pos, speed):
        self.color = color
        self.position = pos
        self.speed = speed
        self.blockSize = speed

    def move(self, width, height):
        if self.position['x'] <= 0:
            self.position['x'] += self.speed
            return
        if self.position['y'] <= 0:
            self.position['y'] += self.speed
            return
        if self.position['x'] >= width - self.speed:
            self.position['x'] -= self.speed
            return
        if self.position['y'] >= height - self.speed:
            self.position['y'] -= self.speed
            return
        self.position['x'] += self.speed * rd.randint(-1,1)
        self.position['y'] += self.speed * rd.randint(-1,1)

class BlopG(Blop):
    def __init__(self, color, pos, speed):
        super().__init__(color, pos ,speed)



