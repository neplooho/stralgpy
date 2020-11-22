import pyglet


class Stage:

    def __init__(self, screen_width, screen_height, gen, size, window):
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
        self.speed = 144

    def update(self, dt):
        if self.frame < len(self.frames):
            self.__window.clear()
            pyglet.graphics.draw(self.size * 4, pyglet.gl.GL_QUADS, self.frames[self.frame])
            self.frame += 1
        else:
            pyglet.clock.unschedule(self.update)

    def prepare_frames(self):
        for array in self._gen:
            self.frames.append(self.get_draw_data(array))
        # duplicate last frame to ensure that engine won't redraw last two screens when idling (SwapBuffers)
        self.frames.append(self.frames[-1])

    def start(self):
        pyglet.clock.schedule_interval(self.update, 1 / self.speed)

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
