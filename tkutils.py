from time import time
import tkinter
import tkinter as tk
__version__ = '1.0'
class progresbar():
    def __init__(self, x, y, width, height, canvas, base_color='green', color_progress='#00ff00', color_no_progress='#ff0000', padding=2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.padding = padding
        self.base = canvas.create_rectangle(x,y,x+width,y+height, fill=base_color)
        self.in_base = canvas.create_rectangle(x+padding,y+padding,x+width-padding,y+height-padding, fill=color_no_progress)
        self.progress_display = canvas.create_rectangle(x,y,x,y+height, fill=color_progress)
    def update_all(self, progress):
        self.canvas.coords(self.base, self.x,self.y,self.x+self.width,self.y+self.height)
        self.canvas.coords(self.in_base, self.x+self.padding,self.y+self.padding,self.x+self.width-self.padding,self.y+self.height-self.padding)
        self.update(progress)
    def update(self, progress):
        self.canvas.coords(self.progress_display, self.x+self.padding, self.y+self.padding, self.x+(self.width-self.padding)*progress, self.y+self.height-self.padding)
    def destroy(self):
        self.canvas.delete(self.base)
        self.canvas.delete(self.in_base)
        self.canvas.delete(self.progress_display)
class smotch_rect():
    counter = 0
    def __init__(self, x, y, width, height, canvas, deg=5, color='white', outline="black", id_rect=None, new_self=None, border_size=1):
        if id_rect:
            self.id = id_rect
        else:
            self.id = "smotch_rect:"+str(smotch_rect.counter)
            smotch_rect.counter += 1
        if new_self:
            self = new_self
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.deg = deg
        self.color = color
        self.outline = outline
        self.border_size = border_size

        self.in_recty = canvas.create_rectangle(x+deg, y, x+width-deg, y+height, fill = color, outline = "", tag=self.id)
        self.in_rectx = canvas.create_rectangle(x, y+deg, x+width, y+height-deg, fill = color, outline = "", tag=self.id)
        if outline:
            self.lines = [
                canvas.create_line(x, y+deg, x, y+height-deg, fill = outline, tag=self.id, width=border_size),
                canvas.create_line(x+deg, y, x+width-deg, y, fill = outline, tag=self.id, width=border_size),
                canvas.create_line(x+width, y+deg, x+width, y+height-deg, fill = outline, tag=self.id, width=border_size),
                canvas.create_line(x+deg, y+height, x+width-deg, y+height, fill = outline, tag=self.id, width=border_size),
            ]
        self.arcs = [
            canvas.create_arc(x, y+height-deg*2, x+deg*2, y+height, start = 180, extent=90, fill = color, outline = "", tag=self.id),
            canvas.create_arc(x, y+height-deg*2, x+deg*2, y+height, start = 180, extent=90, style = tkinter.ARC, outline = outline, tag=self.id, width=border_size),
            canvas.create_arc(x+width-deg*2, y, x+width, y+deg*2, start = 0, extent=90, fill = color, outline = "", tag=self.id),
            canvas.create_arc(x+width-deg*2, y, x+width, y+deg*2, start = 0, extent=90, style = tkinter.ARC, outline = outline, tag=self.id, width=border_size),
            canvas.create_arc(x+deg*2, y, x, y+deg*2, start = 90, extent=90, fill = color, outline = "", tag=self.id),
            canvas.create_arc(x+deg*2, y, x, y+deg*2, start = 90, extent=90, style = tkinter.ARC, outline = outline, tag=self.id, width=border_size),
            canvas.create_arc(x+deg*2, y, x, y+deg*2, start = 90, extent=90, fill = color, outline = "", tag=self.id),
            canvas.create_arc(x+deg*2, y, x, y+deg*2, start = 90, extent=90, style = tkinter.ARC, outline = outline, tag=self.id, width=border_size),
            canvas.create_arc(x+width-deg*2, y+height-deg*2, x+width, y+height, start = -90, extent=90, fill = color, outline = "", tag=self.id),
            canvas.create_arc(x+width-deg*2, y+height-deg*2, x+width, y+height, start = -90, extent=90, style = tkinter.ARC, outline = outline, tag=self.id, width=border_size),
        ]
    def new(self):
        return smotch_rect(self.x, self.y, self.width, self.height, self.canvas, self.deg, self.color, self.outline, self.id, self, self.border_size)
    def update(self):
        self.destroy()
        self.new()


    def destroy(self):
        self.canvas.delete(self.id)
import math

class RotateRect:
    def __init__(self, x, y, width, height, canvas, angle=0, **kwargs):
        """
        Инициализация повёрнутого прямоугольника.
        
        Параметры:
        - x, y: координаты центра
        - width, height: размеры
        - canvas: виджет Canvas
        - angle: угол поворота в градусах
        - kwargs: дополнительные параметры для create_polygon (fill, outline и т.д.)
        """
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle  # в градусах
        
        # Полуразмеры
        w2 = width / 2
        h2 = height / 2
        
        # Исходные вершины относительно центра
        vertices = [
            (-w2, -h2),  # левый верхний
            ( w2, -h2),  # правый верхний
            ( w2,  h2),  # правый нижний
            (-w2,  h2)   # левый нижний
        ]
        
        # Поворот вершин
        rotated_vertices = []
        angle_rad = math.radians(angle)
        for dx, dy in vertices:
            new_x = dx * math.cos(angle_rad) - dy * math.sin(angle_rad)
            new_y = dx * math.sin(angle_rad) + dy * math.cos(angle_rad)
            rotated_vertices.append((new_x, new_y))
        
        # Глобальные координаты
        self.points = []
        for dx, dy in rotated_vertices:
            self.points.append(x + dx)
            self.points.append(y + dy)
        
        # Рисуем
        self.polg = canvas.create_polygon(
            self.points,
            fill=kwargs.get('fill', ''),
            outline=kwargs.get('outline', 'black'),
            width=kwargs.get('width', 2),
            tags=kwargs.get('tags', '')
        )
    
    def click(self, event):
        """
        Проверяет, попал ли клик в прямоугольник.
        Возвращает True, если клик внутри, иначе False.
        """
        return self.is_point_inside(event.x, event.y)
    
    
    def is_point_inside(self, px, py):
        """
        Проверка попадания точки (px, py) внутрь многоугольника.
        Алгоритм: подсчёт пересечений луча с рёбрами.
        """
        points = self.points
        n = len(points) // 2
        inside = False
        
        p1x, p1y = points[0], points[1]
        for i in range(1, n + 1):
            p2x, p2y = points[(i % n) * 2], points[(i % n) * 2 + 1]
            if py > min(p1y, p2y):
                if py <= max(p1y, p2y):
                    if px <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (py - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or px <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        
        return inside
    
    def delete(self):
        """Удаляет прямоугольник с холста."""
        self.canvas.delete(self.polg)
    
    
    def move(self, new_x, new_y):
        """Перемещает прямоугольник в новую позицию."""
        self.x = new_x
        self.y = new_y
        self._update_position()
    
    
    def rotate(self, new_angle):
        """Изменяет угол поворота прямоугольника."""
        self.angle = new_angle
        self._recalculate_points()
        self._update_position()
    
    
    def _recalculate_points(self):
        """Пересчитывает координаты вершин с новым углом."""
        w2 = self.width / 2
        h2 = self.height / 2
        
        vertices = [
            (-w2, -h2), (w2, -h2), (w2, h2), (-w2, h2)
        ]
        
        angle_rad = math.radians(self.angle)
        rotated_vertices = []
        for dx, dy in vertices:
            new_x = dx * math.cos(angle_rad) - dy * math.sin(angle_rad)
            new_y = dx * math.sin(angle_rad) + dy * math.cos(angle_rad)
            rotated_vertices.append((new_x, new_y))
        
        self.points = []
        for dx, dy in rotated_vertices:
            self.points.append(self.x + dx)
            self.points.append(self.y + dy)
    
    
    def _update_position(self):
        """Обновляет положение прямоугольника на холсте."""
        self.canvas.coords(self.polg, self.points)
    
    
    def get_bounds(self):
        """Возвращает ограничивающий прямоугольник (x1, y1, x2, y2)."""
        xs = self.points[::2]  # все x-координаты
        ys = self.points[1::2] # все y-координаты
        return (min(xs), min(ys), max(xs), max(ys))
    
    
    def get_center(self):
        """Возвращает текущие координаты центра."""
        return (self.x, self.y)
# class Tween():
#     def __init__(self, )
class AnimateType:
    LINE = 0
    SIN = 1
    EASE_IN_QUAD = 2
    EASE_OUT_QUAD = 3
    JUMPER = 4
def get_proc(animate_type, time_need, time_right):
    # base_proc идет от 0.0 до 1.0
    base_proc = min(1.0, time_right / time_need)
    
    match animate_type:
        case AnimateType.LINE:
            return base_proc
            
        case AnimateType.SIN:
            return 1 - math.cos(base_proc * math.pi / 2)
            
        case AnimateType.EASE_IN_QUAD:
            return base_proc * base_proc
            
        case AnimateType.EASE_OUT_QUAD:
            return 1 - (1 - base_proc) * (1 - base_proc)
            
        case AnimateType.JUMPER:
            if base_proc == 0: return 0
            return 1 - math.exp(-3 * base_proc) * math.cos(base_proc * math.pi * 4)

class Animate():
    def __init__(self, tk, time_need, animate_type=AnimateType.LINE):
        self.root = tk
        self.anim_type=animate_type
        self.progres = 0
        self.time_need = time_need
        self.stop = False
    def calc(self):
        if not hasattr(self, 'start_time'):
            self.start_time = time()
            self.progres = 0
        else:
            self.progres = time()-self.start_time
        if self.progres>=self.time_need:
            self.progres = self.time_need
            self.stop = True
            return 1
        return get_proc(self.anim_type, self.time_need, self.progres)
    def handle(self, fn, seconds=1/60, handle_end=None):
        self.handle_end = handle_end
        def handlef():
            fn(self.calc())
            if not self.stop:
                self.root.after(int(seconds*1000), handlef)
            else:
                if self.handle_end is not None:
                    self.handle_end()
        handlef()
def to_black(color, k):
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)
    r = max(0, min(255, int(r * k)))
    g = max(0, min(255, int(g * k)))
    b = max(0, min(255, int(b * k)))
    return f"#{r:02x}{g:02x}{b:02x}"
class Message:
    def __init__(self, canvas, text, x, y, sx=400, sy=150, color="#3B9133", deg=20):
        self.is_deleted = False
        self.canvas = canvas
        self.text = text
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.color = color
        
        self.rect_obj = smotch_rect(
            x=self.x, y=self.y, width=self.sx, height=self.sy,
            canvas=self.canvas, color=self.color, deg=deg, border_size=5, outline=to_black(color, 0.5)
        )
        self.text_id = None
        
        # Вызываем update для первой отрисовки
        self.update(x, y, sx, sy, text)

    def update(self, x=None, y=None, sx=None, sy=None, text=None):
        if self.is_deleted:
            raise tk.TclError("object is deleted")
        # Обновляем внутренние свойства, если они переданы
        if x is not None: self.x = x
        if y is not None: self.y = y
        if sx is not None: self.sx = sx
        if sy is not None: self.sy = sy
        if text is not None: self.text = text

        self.rect_obj.x = self.x
        self.rect_obj.y = self.y
        self.rect_obj.width = self.sx
        self.rect_obj.height = self.sy
        self.rect_obj.color = self.color
        
        self.rect_obj.update()

        # Обновляем текст: удаляем старый и рисуем новый поверх
        if self.text_id:
            self.canvas.delete(self.text_id)
            
        self.text_id = self.canvas.create_text(
            self.x + self.sx / 2, 
            self.y + self.sy / 2,
            text=self.text,
            justify="center",
            width=self.sx - 20
        )

    def delete(self):
        if self.is_deleted:
            raise tk.TclError("object is deleted")
        self.rect_obj.destroy()
        if self.text_id:
            self.canvas.delete(self.text_id)
            self.text_id = None
        self.is_deleted = True

def transpose(matrix):
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)      # x
    cols = len(matrix[0])     # y
    
    # Создаём результирующую матрицу размера y × x
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    
    
    return result
class PaintCanvas:
    def __init__(self, canvas, x, y, sx=400, sy=300, width_img=50, height_img=50, 
                 more_colors=False, alpha_colors=False):
        self.canvas = canvas
        self.x, self.y = x, y
        self.sx, self.sy = sx, sy
        self.w_img, self.h_img = width_img, height_img
        
        self.more_colors = more_colors
        self.alpha_colors = alpha_colors
        self.current_color = (0, 0, 0)
        
        # Размер одного "пикселя" на экране
        self.pw = sx / width_img
        self.ph = sy / height_img
        
        # Храним цвета и ID объектов (квадратиков)
        self.pixels = [[(255, 255, 255) for _ in range(width_img)] for _ in range(height_img)]
        self.pixel_ids = [[None for _ in range(width_img)] for _ in range(height_img)]
        
        self.tag = f"paint_{id(self)}"
        self.update()

        # Привязка событий ко всему холсту, но с фильтрацией координат
        self.canvas.bind("<B1-Motion>", self._on_drag)
        self.canvas.bind("<Button-1>", self._on_drag)

    def _on_drag(self, event):
        # Вычисляем относительные координаты внутри нашего PaintCanvas
        lx = event.x - self.x
        ly = event.y - self.y
        
        ix = int(lx // self.pw)
        iy = int(ly // self.ph)
        
        if 0 <= ix < self.w_img and 0 <= iy < self.h_img:
            self._draw_pixel(ix, iy)

    def _draw_pixel(self, x, y):
        if self.more_colors:
            target = self.current_color
        else:
            target = (0, 0, 0) if self.current_color else (255, 255, 255)
        
        if self.alpha_colors and target != (255, 255, 255):
            old = self.pixels[y][x]
            new_color = tuple(int(old[i]*0.6 + target[i]*0.4) for i in range(3))
        else:
            new_row = list(self.pixels[y])
            new_color = target
            
        # 3. Обновление
        if self.pixels[y][x] != new_color:
            self.pixels[y][x] = new_color
            hex_color = "#{:02x}{:02x}{:02x}".format(*new_color)
            self.canvas.itemconfig(self.pixel_ids[y][x], fill=hex_color, outline=hex_color)
    def set_pixels(self, pxs):
        # 1. Сохраняем новые данные в матрицу (делаем копию, чтобы не связать списки)
        self.pixels = [list(row) for row in pxs]
        
        # 2. Обновляем визуальное отображение на Canvas
        for y in range(self.h_img):
            for x in range(self.w_img):
                val = self.pixels[y][x]
                
                # Приводим к формату 0/1, если в датасете вдруг RGB или наоборот
                if isinstance(val, (tuple, list)):
                    # Если пришел RGB кортеж
                    is_black = 1 if sum(val) < 500 else 0
                else:
                    # Если пришло число (0 или 1)
                    is_black = 1 if val == 1 else 0
                
                # Перезаписываем в матрицу чистое число 0 или 1
                self.pixels[y][x] = is_black
                
                # Красим квадратик
                hex_color = "#000000" if is_black == 1 else "#ffffff"
                self.canvas.itemconfig(self.pixel_ids[y][x], fill=hex_color, outline=hex_color)

    def update(self, x=None, y=None):
        if x is not None: self.x = x
        if y is not None: self.y = y
        
        self.delete()
        
        # Рисуем сетку пикселей
        for iy in range(self.h_img):
            for ix in range(self.w_img):
                color = self.pixels[iy][ix]
                hex_c = "#{:02x}{:02x}{:02x}".format(*color)
                
                x1 = self.x + ix * self.pw
                y1 = self.y + iy * self.ph
                x2 = x1 + self.pw
                y2 = y1 + self.ph
                
                pid = self.canvas.create_rectangle(
                    x1, y1, x2, y2, 
                    fill=hex_c, outline=hex_c, 
                    tags=self.tag
                )
                self.pixel_ids[iy][ix] = pid

    def get_pixels(self):
        """
        Возвращает актуальную матрицу пикселей.
        Если more_colors=False, возвращает 1 (закрашено) или 0 (пусто).
        Если more_colors=True, возвращает RGB кортежи.
        """
        if self.more_colors:
            # Возвращаем копию матрицы с RGB кортежами
            return [row[:] for row in self.pixels]
        else:
            # Считаем пиксель закрашенным (1), если он не чисто белый
            # Используем порог яркости, чтобы учитывать alpha_colors
            result = []
            for row in self.pixels:
                new_row = []
                for p in row:
                    # Если сумма RGB меньше 750 (не белый), значит там есть краска
                    if p not in [0, 1]:
                        is_painted = 1 if sum(p) < 750 else 0
                    else:
                        is_painted = p
                    new_row.append(is_painted)
                result.append(new_row)
            return result

    def clear(self):
        """Полная очистка холста и данных"""
        self.pixels = [[(255, 255, 255) for _ in range(self.w_img)] for _ in range(self.h_img)]
        for row in self.pixel_ids:
            for pid in row:
                self.canvas.itemconfig(pid, fill="#ffffff", outline="#ffffff")

    def delete(self):
        self.canvas.delete(self.tag)

    def set_color(self, rgb):
        self.current_color = rgb
def test_paint():
    root = tk.Tk()
    root.title("PaintCanvas Test")
    
    # Создаем основной холст
    canvas = tk.Canvas(root, width=600, height=500, bg="gray")
    canvas.pack(pady=20)

    # Инициализируем наш класс рисования
    # Рисуем область 400x300, но разрешение картинки внутри 50x50 пикселей для наглядности
    painter = PaintCanvas(
        canvas, 
        x=100, y=50, 
        sx=400, sy=300, 
        width_img=50, height_img=50,
        more_colors=True, 
        alpha_colors=False
    )

    # Фрейм для кнопок управления
    btn_frame = tk.Frame(root)
    btn_frame.pack(fill="x", padx=10)

    def print_data():
        pixels = painter.get_pixels()
        print(f"\n--- PIXEL DATA (Top {len(pixels)}x{len(pixels[0])}) ---")
        for row in pixels:
            print(row)
        print("----------------------------")

    def toggle_color():
        painter.more_colors = not painter.more_colors
        status = "Цветной" if painter.more_colors else "Ч/Б"
        btn_color.config(text=f"Режим: {status}")

    def set_red():
        painter.set_color((255, 0, 0))
        
    def set_blue():
        painter.set_color((0, 0, 255))
    def set_black():
        painter.set_color((0, 0, 0))
        painter.set_color(1)
    def set_white():
        painter.set_color((255, 255, 255))
        painter.set_color(0)

    # Кнопки
    btn_color = tk.Button(btn_frame, text="Режим: Цветной", command=toggle_color)
    btn_color.pack(side="left", padx=5)

    tk.Button(btn_frame, text="Красный", fg="red", command=set_red).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Синий", fg="blue", command=set_blue).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Чёрный", fg="black", command=set_black).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Белый", fg="red", command=set_white).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Получить пиксели", command=print_data).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Очистить", command=lambda: painter.clear()).pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    test_paint()
    w = tkinter.Tk()
    c = tkinter.Canvas()
    c.pack()
    rect = smotch_rect(5,5,30,30, c, 10)
    from time import time
    t = time()
    sx = 0
    sy = 0
    x = 200
    y = 50
    from math import atan2, sin, cos
    Message(c, "hello message", 200, 5, 100, 100)
    while True:
        try:
            xm = w.winfo_pointerx()
            ym = w.winfo_pointery()
            deg = atan2(xm-x, ym-y)
            sx += sin(deg)/5000
            sy += cos(deg)/5000
            x += sx
            y += sy
            rect.x = x
            rect.y = y
            rect.update()
            w.update()
        except:
            break
