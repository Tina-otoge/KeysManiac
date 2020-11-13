from pyglet import gl, graphics, image

image.Texture.default_min_filter = gl.GL_NEAREST
image.Texture.default_mag_filter = gl.GL_NEAREST

def percentize(s, to=1):
    if not isinstance(s, str) or s[-1] != '%':
        return False
    return to * (float(s[0:-1]) / 100)

class Grid:

    COLUMNS = 64
    ROWS = 36
    RATIO = ROWS / COLUMNS

    factor = (1, 1)

    def __init__(self):
        pass

    def __new__(self, column, row, offset_x=0, offset_y=0):
        column = percentize(column, self.COLUMNS) or column
        row = percentize(row, self.ROWS) or row
        if not (0 < column <= self.COLUMNS):
            raise IndexError('{} is not in the grid (0, {})'.format(
                column, self.COLUMNS
            ))
        if not (0 < row <= self.ROWS):
            raise IndexError('{} is not in the grid (0, {})'.format(
                row, self.ROWS
            ))
        x, y = self.factor
        return ((column * x) + offset_x, (row * y) + offset_y)

    @classmethod
    def set_factor(cls, x, y):
        cls.factor = (int(x), int(y))

    @classmethod
    def set_factor_from_resolution(cls, width, height):
        cls.set_factor(width / cls.COLUMNS, height / cls.ROWS)

    @classmethod
    def get_unit(cls, factor=1):
        x, _ = Grid(1 * factor, 1)
        return x

    @classmethod
    def draw_grid(cls):
        x, y = cls.factor
        for i in range(1, cls.COLUMNS):
            graphics.draw(2, gl.GL_LINES,
                ('v2i', (i * x, 0, i * x, y * cls.ROWS)),
                ('c3B', (0, 0, 255, 0, 255, 0))
            )
        for i in range(1, cls.ROWS):
            graphics.draw(2, gl.GL_LINES,
                ('v2i', (0, i * y, x * cls.COLUMNS, i * y)),
                ('c3B', (0, 0, 255, 0, 255, 0))
            )
