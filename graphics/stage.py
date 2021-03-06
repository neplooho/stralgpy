import datetime
import pyglet


class Stage:

    def __init__(self, screen_width, screen_height, gen, size, window, speed=144):
        self.started = False
        self.__window = window
        self._gen = gen
        self.size = size
        self.width = screen_width / size
        self.step = 2
        self.height_mult = screen_height / size
        self.x = 5
        self.y = 5
        self.frames = []
        self.frame = 0
        self.speed = speed
        self.startTime = None

    def update(self, dt):
        try:
            self.__window.clear()
            array = next(self._gen)
            frame = self.get_draw_data(array)
            pyglet.graphics.draw(self.size * 4, pyglet.gl.GL_QUADS, frame)
        except StopIteration:
            pyglet.clock.unschedule(self.update)
            elapsed = datetime.datetime.now() - self.startTime
            print("Took {} time to finish.".format(elapsed))

    def start(self):
        pyglet.clock.schedule_interval(self.update, 1 / self.speed)
        self.started = True
        self.startTime = datetime.datetime.now()

    def get_draw_data(self, array):
        temp_list = []
        for i in range(len(array)):
            temp_list.append(self.x + (self.width * i) + self.step)
            temp_list.append(self.y)
            temp_list.append(self.x + (self.width * i) + self.width)
            temp_list.append(self.y)
            temp_list.append(self.x + (self.width * i) + self.width)
            temp_list.append(array[i] * self.height_mult + self.y)
            temp_list.append(self.x + (self.width * i) + self.step)
            temp_list.append(array[i] * self.height_mult + self.y)
        return 'v2f', tuple(temp_list)

    def multiplySpeed(self, multiplier):
        self.speed *= multiplier
        pyglet.clock.unschedule(self.update)
        pyglet.clock.schedule_interval(self.update, 1 / self.speed)
