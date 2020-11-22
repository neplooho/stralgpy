from pyglet.window import key
from graphics import stage
import pyglet
import utils
import sort


def main():
    size = 600
    a = utils.generate_shuffled_array(size)
    window = pyglet.window.Window(width=1024, height=768)
    started = False
    # s = stage.Stage(1011, 700, sort.insertion.sort(a), size, window)
    # s = stage.Stage(1011, 700, sort.bubble.sort(a), size, window)
    # s = stage.Stage(1011, 700, sort.cocktail_shaker.sort(a), size, window)
    # s = stage.Stage(1011, 700, sort.merge.sort(a), size, window)
    s = stage.Stage(1011, 700, sort.quick.sort(a), size, window)
    # s = stage.Stage(1011, 700, sort.counting.counting_sort(a), size, window)

    @window.event
    def on_show():
        s.prepare_frames()

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.ENTER and not s.started:
            s.start()


if __name__ == '__main__':
    main()
    pyglet.app.run()
