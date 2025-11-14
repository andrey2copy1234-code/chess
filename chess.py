import tkinter as tk # библиотека для GUI
import vector as v   # модуль для векторных операций
__vVector__ = v.__version__ 
#import ArrayC as v
import math as m # матиматика
from time import time,sleep # время
from tkinter import filedialog,messagebox # мини окна
import gc # отключение включение сборшика мусора (GC)
import math # матиматика
import json # json разбор
import threading as th # потоки
import contextlib # для wich window
#import neiro #потом будет использоваться для ии

def is_comp(v, v2):
    print(f'is_comp({v},{v2})')
    vglobal, vlocal = v.split('.')
    v2global, v2local = v2.split('.')
    vglobal, vlocal = int(vglobal), int(vlocal)
    v2global, v2local = int(v2global), int(v2local)
    print(f"is_comp({vglobal}.{vlocal}, {v2global}.{v2local})")
    if vglobal>=v2global:
        print('version global big or eq')
        if vglobal == v2global and vlocal<v2local:
            print('version eq but not eq')
            print('return False')
            return False
        print('return True')
        return True
    print('small version')
    print('return False')
    return False
versions_chess = {'2.1', '2.2', '2.3', '2.4', '2.5'}
#вормат vChess: (vModule, vVector)
comp_table = {
    '2.1': ('2.0', '2.0'),
    '2.2': ('2.0', '2.0'),
    '2.3': ('2.0', '2.0'),
    '2.4': ('2.0', '2.0'),
    '2.5': ('2.0', '2.0')
}
class problem_comp():
    def __init__(self, v1, v2, module):
        self.v1, self.v2 = v1, v2
        self.module = module
    def __str__(self):
        return f"игра этой версии ({__version__}) не совместима с версией {self.v2} у модуля {self.module}. нужна как минимум версия {self.v1} модуля {self.module}"
def num_ind(num):
    return ('одна' if num == 1 else 'ноль') if num<=1 else ('пару' if num == 2 else 'несколько')
class comp():
    why = 'error'
    briefly = 'error'
    def __init__(self, why=None, briefly=None):
        if why:
            self.why = why
        if briefly:
            self.briefly = briefly
    def calc(self, vChess, vModule, vVector):
        if vChess in versions_chess:
            val = comp_table.get(vChess)
            if val:
                vModule_comp, vVector_comp = val 
                problems = []
                if not is_comp(vModule, vModule_comp):
                    problems.append(problem_comp(vModule_comp, vModule, 'chess_module'))
                if not is_comp(vVector, vVector_comp):
                    problems.append(problem_comp(vVector_comp, vVector, 'vector'))
                if len(problems) != 0:
                    num_idn2 = num_ind(len(problems))
                    self.why = f"произошло {num_idn2} проблем{'a' if num_idn2[-1] == 'a' else ''}:"+''.join('\n*'+str(problem) for problem in problems)
                    self.briefly = False
                else:
                    self.why = f"потому что:\nне произошло ни одной проблеммы совместимости (минимальная версия chess_module {vModule_comp} и минимальная версия vector {vVector_comp})"
                    self.briefly = True

def get_comp():
    comp_data = comp()
    comp_data.calc(__version__, __vModule__, __vVector__)
    if comp_data.why == 'error' or comp_data.briefly == 'error':
        return "Error"
    return f"Данная версия ({__version__}) {'совместима' if comp_data.briefly else 'не совместима'} с модулями.\n {comp_data.why}"
news = """
v2.1
Появились версии, проверка совместимости и то что добавили в различных версиях.

v2.2
Улучшен бот. теперь он сначало пытается максимум зашитится а потом атаковать.
Также исправлен баг с тем что не работало 2 раза по restart.

v2.3
Теперь шахматы умеют обновляться на Control-u

v2.4
Теперь бот мыслит не "я смогу съесть эту фигуру через один ход. значит ход хороший", а он теперь с эти сьедением через 1 ход проверяет застчишишена ли фигура которую он хочет съесть. рекомендую вместе с ним скачать ещё и chess_module 2.1

v2.5
Теперь обновление шахмат более понятнее и продуманнее. появился gui интерфейс во время обновления. и новые заготовки для случаев когда в проекте будет более 60 файлов. ведь раньше это с маштабом в 60 файлов могло заблокировать по ip за превышение лимита запросов в час. также увеличенна скорость загрузки нового обновления. Также улучшена обработка ошибок. теперь вместо моментального закрытия программы или зависания показывается что за ошибка и просьба отправить её автору созданного кода. также некоторые ошибки (например при обновлении) ещё и переводятся на язык понятный всем (почти).
"""
__version__ = '2.5'
#size = 600
heightButtons = 50
from chess_module import *
from chess_module import __version__ as __vModule__

def saveF(game):
    choice = multiple_choice("сохранение", "как вы хотите сохранить?\n", ('отмена','как файл', 'как видео'))
    if choice == "как файл":
        file_path = filedialog.asksaveasfilename(
                        title="Сохраните файл",
                        defaultextension=".txt",
                        filetypes=(("Text Files", "*.txt"),)
                    )
        if file_path:
            save(game,file_path)
    elif choice == "как видео":
        file_path = filedialog.asksaveasfilename(
                        title="Сохраните файл",
                        defaultextension=".txt",
                        filetypes=(("Text Files", "*.txt"),)
                    )
        if file_path:
            saveV(game, file_path)

#update part
import urllib.request
import urllib.error
import os
import sys

URL_REPOSITOR_DOWLOAD = "https://raw.githubusercontent.com/andrey2copy1234-code/chess/main"
URL_REPOSITOR_PUBLICK = "https://github.com/andrey2copy1234-code/chess"
files_update = ['chess.py', 'chess_module.py', 'vector.py']
def fast_iter(iteration, at_time):
    for i in range(0, len(iteration), at_time):
        yield (iteration[i2] for i2 in range(i, min(i+at_time, len(iteration))))
def interpolate_color(color1_hex, color2_hex, progress):
    r1, g1, b1 = int(color1_hex[1:3], 16), int(color1_hex[3:5], 16), int(color1_hex[5:7], 16)
    r2, g2, b2 = int(color2_hex[1:3], 16), int(color2_hex[3:5], 16), int(color2_hex[5:7], 16)
    r = int(r1 + (r2 - r1) * progress)
    g = int(g1 + (g2 - g1) * progress)
    b = int(b1 + (b2 - b1) * progress)
    return f"#{r:02x}{g:02x}{b:02x}"
@contextlib.contextmanager
def the_window_all_close(window):
    try:
        yield
    finally:
        if window.winfo_exists():
            window.destroy()
col1 = "#ff0000"
col2 = "#00ff00"
is_error = 0
def paralel_for_updating(fn, colection, *args, at_time=8, **kwargs):
    global is_error
    updating_window = tk.Tk()
    with the_window_all_close(updating_window):
        updating_window.geometry("300x150")
        updating_window.title("updating chess")
        updating_window.resizable(width=False, height=False)
        canvas = tk.Canvas(updating_window, bg=col1)
        text_proces = canvas.create_text(150,int(150/2), text="files loaded: 0\navg time left: unknown\n0% is loaded")
        canvas.pack(fill = 'both',expand = True)
        updating_window.update()
        tasks = fast_iter(colection, at_time)
        t = time()
        start_time = t
        counter = 0
        for tasks_time in tasks:
            while True:
                if counter+at_time>=60:
                    if time()-t>=60*60:
                        counter = 0
                        t = time()
                    else:
                        canvas.itemconfig(text_proces, text=f"files loaded: {counter}\navg time left: {start_time/counter:.1f}\n{counter/len(colection)*100:.2f}% is loaded\n loaded: wait")
                        updating_window.update()
                        sleep(60*60-(time()-t))
                        continue
                threads = [th.Thread(target=fn, args=(task, *args), kwargs=kwargs) for task in tasks_time]
                for thr in threads:
                    thr.start()
                need_stop = False
                for thr in threads:
                    thr.join()
                    if need_stop:
                        continue
                    if is_error:
                        need_stop = True
                    counter += 1
                    canvas.itemconfig(text_proces, text=f"files loaded: {counter}\navg time left: {(time()-start_time)/counter:.1f}\n{counter/len(colection)*100:.2f}% is loaded")
                    canvas.configure(bg=interpolate_color(col1, col2, counter/len(colection)))
                    updating_window.update()
                if need_stop:
                    updating_window.destroy()
                    if is_error == 1:
                        messagebox.askokcancel("Error", "Произошла ошибка сети.")
                    else:
                        messagebox.askokcancel("Error", "Превышенно время ожидания ответа.")
                    is_error = 0
                    return 1
                break
        canvas.itemconfig(text_proces, text=f"files loaded: {counter}\navg time left: 0\n{counter/len(colection)*100:.2f}% is loaded\n loaded: successfully")

        updating_window.update()
        sleep(1)
def update_file_from_github(file_update, dir_files):
    global is_error
    global past_call
    url_to_file = f"{URL_REPOSITOR_DOWLOAD}/{file_update}"
    try:
        with urllib.request.urlopen(url_to_file, timeout=10) as response:
            code = response.read()
        past_call = time()
    except urllib.error.URLError:
        is_error = 1
    except TimeoutError:
        is_error = 2
    path_to_file = dir_files+file_update
    with open(path_to_file, 'wb') as file:
        file.write(code)
def snow_console():
    from ctypes import windll
    windll.user32.ShowWindow(windll.kernel32.GetConsoleWindow(), True)
def snow_error():
    import traceback
    traceback.print_exc()
    snow_console()
def base_snow_error():
    messagebox.askokcancel("Error", "функция которую ты вызвал вызвала ошибку. я открою консоль. отправь что в консоли автору этих шахмат")
    snow_error()
past_call = 0
def update():
    global past_call
    t = time()
    if t-past_call>90*len(files_update): #нельзя чаше чем в 1 минуту вызывать но это на всякий случай
        ot = messagebox.askyesno("Обновление", "Обновить шахматы? (но рекоминдуется способ из справки)")
        if ot:
            ot = messagebox.askyesno("Обновление", "Создать отдельную папку для новой версии шахмат?")
            if ot:
                dir_files = filedialog.askdirectory()
                name_dir = simpledialog.askstring("Создание папки", "введите имя папки")
                dir_files += "/"+name_dir+"/"
                if not dir_files:
                    return 0
                try:
                    os.makedirs(dir_files)
                except FileExistsError:
                    pass
            else:
                dir_files = "./"
            try:
                paralel_for_updating(update_file_from_github, files_update, dir_files)
            except:
                messagebox.askokcancel("Error", "новая функция вызвала ошибку. я открою консоль. отправь что в консоли автору")
                snow_error()
            # for file_update in files_update:
            #     url_to_file = f"{URL_REPOSITOR_DOWLOAD}/{file_update}"
            #     try:
            #         with urllib.request.urlopen(url_to_file) as response:
            #             code = response.read()
            #         past_call = time()
            #     except urllib.error.URLError:
            #         messagebox.askokcancel("Error", "Произошла ошибка сети.")
            #         return 1
            #     print('return:', '\n'+code.decode('utf-8'))
            #     path_to_file = dir_files+file_update
            #     with open(path_to_file, 'wb') as file:
            #         file.write(code)
            if dir_files == "./":
                os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        messagebox.askyesno("Совет", "Лучше сейчас не обновлять. так обновляя можно превысить лимиты запросов к github API")
        return 1
# update()
# exit(0)


class game():
    __slots__ = ('root','map','mode','Frames','step','label','canvas','pictures','highlighted','file','victory','steps','hist','histPos','speed','text','mode', 'modes')
    #__slots__ = ('root','map','mode','Frames','step','label','canvas','pictures','highlighted','file','victory')
    def __init__(self,mode,file,text):
        self.root = tk.Tk()
        self.pictures = {}
        for ob in figure_picture:
            image = tk.PhotoImage(file = figure_picture[ob])
            self.pictures[ob] = image
        self.root.title(f"game of chess. start file: {file}")
        self.root.resizable(width=False,height=False)
        self.root.geometry(f"{size}x{size+heightButtons}")
        self.canvas = tk.Canvas()
        self.canvas.pack(fill = 'both',expand = True)
        def destroy():
            if messagebox.askyesno("Сохранить?","Сохранить файл?"):
                file_path = filedialog.asksaveasfilename(
                    title="Сохраните файл",
                    defaultextension=".txt",
                    filetypes=(("Text Files", "*.txt"),)
                )
            else:
                file_path = False
            if file_path:
                save(self,file_path)
            self.root.destroy()
        self.root.protocol("WM_DELETE_WINDOW",destroy)
        self.root.focus_force()
        self.map = []
        self.mode = mode
        if file:
            loaded(self,file)
        elif text:
            loadedString(self,text)
        self.text = text
        self.hist = histStr(getStringSave(self))
        self.histPos = 1
        self.file = file
        self.load_modes()
    def create_figure(self,*args,**kvargs):
        self.map.append(figure(self.root,self.canvas,self.pictures,self.iscollide,*args,**kvargs))
    def move_figure(self, idF, step):
        ob = self.map[idF]
        step = v.Vector2(mas=step)
        move_to = step+ob.pos
        f = self.iscollide(move_to)
        if f:
            if f.name == "король":
                self.victory = True
                self.canvas.itemconfigure(self.label,text = ("белые победили" if self.step else "чёрные победили"))
            f.delete()
            self.map.remove(f)
        change_name = ob.step(step,choice=False)
        self.canvas.lift(self.label)
        self.step = not self.step
        if not self.victory:
            self.canvas.itemconfigure(self.label,text = ("ходят белые" if self.step else "ходят чёрные"))
    def load_modes(self):
        self.modes = load_modes()
        for mode in self.modes:
            mode.init(self)
    def iscollide(self,pos):
        for ob in self.map:
            if ob.pos == pos:
                return ob
        return False
    def iscollideMas(self,pos,mas):
        for ob in mas:
            if ob.pos == pos:
                return ob
        return False
            
    def CS(self,x,y,sx,sy,fill):
        return self.canvas.create_rectangle(x,y,x+sx,y+sy,fill=fill)
    def start(self):
        if mode == "play" or mode == "random" or mode[0] == "b":
            self.Frames = []
            for x in range(0,size,int(size//8)):
                for y in range(0,size,int(size//8)):
                    self.canvas.create_rectangle(x,y,x+size/8,y+size/8,fill=('#5e3500'if (x/(size//8)+y/(size//8))%2==1 else '#f5f5dc'))
            alphabet = "abcdefgh"[::-1]
            for x in range(0,size,int(size//8)):
                self.canvas.create_text(x+7,7,text=alphabet[int(x//(size/8))], fill="#000000", font='Helvetica 8 bold')
            for y in range(0,size,int(size//8)):
                self.canvas.create_text(7,y+7+(0 if y != 0 else 10),text=str(int(y//(size//8))+1), fill="#000000", font='Helvetica 8 bold')
            for ob in self.map:
                ob.init()
            self.victory = False
            self.label = self.canvas.create_text(size/2,25,text = ("ходят белые" if self.step else "ходят чёрные"),font = "Time 15",fill='grey')
            #restart button
            self.canvas.create_rectangle(0,size,size/4,size+heightButtons,fill='#FF8000',) #restart button
            self.canvas.create_text(size/8,size+heightButtons/2,text="restart",fill  = '#362c12',font = f"Time {int(heightButtons//1.3)}") #restart text
            #save button
            self.canvas.create_rectangle(size-size/4,size,size,size+heightButtons,fill='blue',) #save button
            self.canvas.create_text(size-size/8,size+heightButtons/2,text="save",fill  = '#1e213d',font = f"Time {int(heightButtons//1.3)}") #save text
            #open button
            self.canvas.create_rectangle(size/2-size/8,size,size/2+size/8,size+heightButtons,fill='#89ac76',) #open button
            self.canvas.create_text(size/2,size+heightButtons/2,text="open",fill  = '#16251c',font = f"Time {int(heightButtons//1.3)}") #open text
            def get_steps(ob,iscollide=None):
                if not iscollide:
                    iscollide = self.iscollide
                try:
                    mas = figure_moves[ob.name]['white' if self.step else 'black']
                except:
                    try:
                        mas = figure_moves[ob.name](ob,iscollide)
                    except Exception as err:
                        mas = figure_moves[ob.name]
                        #print(err)
                return mas
            def restart():
                self.root.unbind("<Left>")
                self.root.unbind("<Right>")
                for frame in self.Frames:
                    self.canvas.delete(frame.Frame)
                self.Frames.clear()
                for ob in self.map:
                    ob.delete()
                self.map.clear()
                if self.file:
                    try:
                        with open(self.file, encoding='utf-8') as f:
                            str_read = f.read()
                            if  str_read != self.hist[self.histPos-1]:
                                loaded(game,self.file)
                                self.histPos += self.hist.set(getStringSave(self),self.histPos)
                            else:
                                loadedString(game,self.text)
                                self.histPos += self.hist.set(getStringSave(self),self.histPos)
                                self.file = None
                    except FileNotFoundError:
                        print("not can open:", self.file)
                elif self.text:
                    loadedString(self,self.text)
                for ob in self.map:
                    ob.init()
                self.victory = False
                self.canvas.itemconfigure(self.label,text = ("ходят белые" if self.step else "ходят чёрные"))
                self.canvas.lift(self.label)
                self.histPos += self.hist.set(getStringSave(self),self.histPos)
            def open_file():
                choice = multiple_choice("открытие", "что вы пытаетесь открыть?\n", ('отмена','файл', 'видео'))
                if choice == "файл":
                    self.root.unbind("<Left>")
                    self.root.unbind("<Right>")
                    file = filedialog.askopenfilename(
                                title="Выберите файл для открытия",
                                filetypes=(("Text Files", "*.txt"),)
                            )
                    if file:
                        for frame in self.Frames:
                            self.canvas.delete(frame.Frame)
                        self.Frames.clear()
                        for ob in self.map:
                            ob.delete()
                        self.map.clear()
                        loaded(game,file)
                        for ob in self.map:
                            ob.init()
                        self.file = file
                        self.victory = False
                        self.canvas.itemconfigure(self.label,text = ("ходят белые" if self.step else "ходят чёрные"))
                        self.canvas.lift(self.label)
                        self.root.title(f"game of chess. start file: {file}")
                        self.histPos += self.hist.set(getStringSave(self),self.histPos)
                elif choice == "видео":
                    file = filedialog.askopenfilename(
                                title="Выберите файл для открытия",
                                filetypes=(("Text Files", "*.txt"),)
                            )
                    if file:
                        for frame in self.Frames:
                            self.canvas.delete(frame.Frame)
                        self.Frames.clear()
                        for ob in self.map:
                            ob.delete()
                        self.map.clear()
                        self.victory = False
                        self.canvas.itemconfigure(self.label,text = ("ходят белые" if self.step else "ходят чёрные"))
                        openV(game, file)
            def clickReal(posT):
                if not self.victory and (self.mode != "random"):
                    pos = v.Vector2(mas=posT)//(size/8)+v.Vector2(mas=(1,1))
                    #print(pos)
                    idFr = 0
                    for ob in self.Frames:
                        if ob.pos == pos:
                            #print("move")
                            for frame in self.Frames:
                                self.canvas.delete(frame.Frame)
                            self.Frames.clear()
                            f = self.iscollide(pos)
                            s = True
                            if f:
                                f.delete()
                                if f.name == "король":
                                    s = False
                                    self.canvas.itemconfigure(self.label,text = ("белые победили" if self.step else "чёрные победили"))
                                    self.victory = True
                                self.map.remove(f)
                            self.highlighted.step(ob.move)
                            self.canvas.lift(self.label)
                            if self.mode == "NN teach":
                                try:
                                    file = open("./NN_dataset.txt", 'r')
                                    text = file.read()
                                    data = json.loads(text)
                                    file.close()
                                except FileNotFoundError:
                                    data = []
                                file = open("./NN_dataset.txt", 'w')
                                idF = 0
                                for f in self.map:
                                    if f is self.highlighted:
                                        break
                                    if f.b == self.step:
                                        idF += 1
                                step_data = {'all': getStringSave(self), 'idF': idF, 'color': self.step, 'step': idFr}
                                data.append(in_nn(step_data))
                                file.write(json.dumps(data))
                                file.close()
                            if self.mode != "bot" and self.mode != "bot2":
                                self.step = not self.step
                                if s:
                                    self.canvas.itemconfigure(self.label,text = ("ходят белые" if self.step else "ходят чёрные"))
                            elif s:
                                self.canvas.itemconfigure(self.label,text = ("ходят белые" if not self.step else "ходят чёрные"))
                                def f():
                                    self.step = not self.step
                                self.root.after(200,f)
                            if self.mode[0] != 'b' or not s:
                                self.histPos += self.hist.set(getStringSave(self),self.histPos)
                            return None
                        idFr += 1
                    for ob in self.map:
                        #print(ob)
                        if ob.pos == pos:
                            #print("click")5
                            if self.step == ob.b and (self.mode=="play" or self.step == True):
                                self.highlighted = ob
                                for frame in self.Frames:
                                    self.canvas.delete(frame.Frame)
                                self.Frames.clear()
                                mas = get_steps(ob)
                                #print(mas)
                                for posP in mas:
                                    posP = v.Vector(mas=posP)
                                    ep = ob.pos+posP
                                    if ep[0] <= 8 and ep[0]>0 and ep[1]<=8 and ep[1]>0:
                                        f = self.iscollide(ob.pos+posP)
                                        if not f or f.b != self.step:
                                            newPos = posP+ob.pos-v.Vector(mas=(1,1))
                                            Frame2 = FrameC(self.CS(newPos[0]*size/8,newPos[1]*size/8,size/8,size/8,fill = 'green'),newPos+v.Vector(mas=(1,1)),posP)
                                            
                                            self.Frames.append(Frame2)
                                for ob2 in self.map:
                                    self.canvas.lift(ob2.Frame)
                                self.canvas.lift(self.label)
                                            
                                return None
                    for frame in self.Frames:
                        self.canvas.delete(frame.Frame)
                    self.Frames.clear()
                if posT.y>size:
                    if posT.x < size/4:
                        restart()
                    elif size-size/4<posT.x:
                        saveF(self)
                    elif size/2-size/8<posT.x and posT.x<size/2+size/8:
                        open_file()
                for mode in self.modes:
                    try:
                        mode.click(posT)
                    except Exception as err:
                        print(f'[{mode.name}] error in click')
                        print(f'[{mode.name}] {type(err).__name__}: {err}')
            self.canvas.bind("<ButtonPress-1>",clickReal)
            def Control_H(key):
                choice = messagebox.askquestion("помошь по шахматам №1", f"этот проект маштабен. но давайте объясню с управлением:\n  Control-H это вызвать это\n  Control-z вернуть обратно СВОЙ ход\n  Control-Shift-Z это вернуть всё как было до Control-z\n  Left (стрелочка) - проматывает видио на шаг назад.\n  Right (стрелочка) - проматывает вперёд. если видио закончилось то снимает действее с Left и себя.\n  c - стереть (необратимо) историю. рекомендуется для начала записи видио.\n  m - это переключение режима\n  s - изменяет скорость главного цикла. рекомендуется оставить значение в 20ms\n  Control-u - обновить версию шахмат (но рекумендуется заходить и обновлять по {URL_REPOSITOR_PUBLICK})\n\nтеперь перейдём к окошкам. вы наверное встретите окошки в которых в скобочках слово и через тире другие слова. если нажмёте да - вы отвечаете окошку на вопрос выделенным словом в скобочках. если ответ нет - то проматывайте (с помошью нет) до нужного слова в скобочках\nпродолжить?")
                if choice == "yes":
                    choice = messagebox.askquestion("помошь по шахматам №2", "теперь разберёмся с кнопками:\n  restart - перезапускает. если был старт с файла то перезапускает его. для того чтобы перевести в начальное состояние надо два раза нажать restart.\n  open - открывает файл или файл-видио.\n  save - сохраняет файл или файл-видио.\nпродолжить?")
                    if choice == "yes":
                        choice = messagebox.askquestion("помошь по шахматам №3", "теперь про то что есть сдесь из шахмат:\n  рокировка - можно делать рокировку.\n  взятие - фигуры могут заберать друг друга.\n  перемешение по правилом шахмат - фигуры передвегаются также как и в обычных шахматах.\n  нет взятия на проходе - не получится так взять.\nпродолжить?")
                        if choice == "yes":
                            choice = messagebox.askquestion("помошь по шахматам №4", "теперь про то что может бот и что он учитывает:\n  плохие ходы - бот никогда не сделает ход который убъёт его короля.\n  взятие - бот понимает что взять лучше чем просто сходить.\n  подставка фигур - бот понимает что подставить свою фигуру тоже самое что и убить её.\n  понимает все зашиты - он понимает что лучше ходом зашитить свою фигуру.\n  понимает что своих не убивать - бот понимает что если убить своего то это будет хуже чем просто сходить.\n  простчитывает взятие до его - бот может поставить фигуру так чтобы после хода она забрала другую.\n\nпродолжить?")
                            if choice == "yes":
                                choice = messagebox.askquestion("помошь по шахматам №5", "популярные вопросы и ответы на их:\n  можно ли как-то уменьшить и увеличить окно? - нет, нельзя. окно всегда размером 600x600.\n  можно ли цифры и буквы вынести за пределы поля? - нет, нельзя.\n  почему на видео записовоется не то что надо? - сохранение видио это beta функция. сохранение видео пока работает не очень идеально. поэтому можно нажать (в начале записи) С (англискую и маленькую) для исправления этого. также вы возможно столкнулись с багом того что при использовании Control-z не правильно записывается видео.\n  почему это 'видео' .txt файл? - под видио я имею ввиду любую запись множества ходов. если вы хотите видио .mp4 а не .txt который только эта программа прочитать может то я вам могу предложить устоновить программы или использовать сочетания клавишь на windows для записи .mp4 видио.\n  чем bot отличается от bot2? - bot может делать неверные действия но плюс минус правильные а bot2 только самые лучшие как он постчитал. также bot работает намного медленее bot2. советую использовать bot2.\n  почему сочетания клавишь перестают работать? - вы наверное стоите на руской раскладке а не на англиской.\n  как поиграть в эти шахматы онлайн? - у меня есть chess_online это отдельный проект в который вы тоже можете поиграть. покачто от сюда в chess_online перейти нельзя через режимы. надо запускать другую программу.\n  как начать запись видео? - вам не нужно её начинать. она всегда включенна. если вы хотите чтобы всё что раньше записалось удалилось то нажмите C англискую\n\nесли что-то не поняли то нажмите 'да' в этом окошке.")
                                if choice == "yes":
                                    choice = messagebox.askquestion("помошь по шахматам №6", "Расширения:\n"+''.join('- '+mode.name+'\n'+mode.discription+'\n' for mode in self.modes)+('их нет' if len(self.modes) == 0 else '')+'\nесли остались вопроссы нажмите "да"')

                                    if choice == "yes":
                                        choice = messagebox.askquestion("помошь по шахматам №7", f"Версии (сейчас версия {__version__}):{news}\nесли остались вопросы нажмите 'да'")
                                        if choice:
                                            choice = messagebox.askquestion("помошь по шахматам №8", f"Совместимость:\n{get_comp()}\nесли остались вопросы нажмите 'да'")
                                            if choice == "yes":
                                                messagebox.askquestion("помошь по шахматам №9", "как вижу у вас остались вопросы. задать вы их можете создателю.")

            self.root.bind('<Control-h>', Control_H)
            def Control_Z(key):
                if self.histPos != 1:
                    for frame in self.Frames:
                        self.canvas.delete(frame.Frame)
                    self.Frames.clear()
                    for ob in self.map:
                        ob.delete()
                    self.map.clear()
                    loadedString(self,self.hist[self.histPos-2])
                    for ob in self.map:
                        ob.init()
                    self.victory = False
                    self.histPos -= 1
                    self.canvas.itemconfigure(self.label,text = ("ходят белые" if self.step else "ходят чёрные"))
                    self.canvas.lift(self.label)
                    self.root.title(f"game of chess. start file: {file}")
                    print("loaded:",self.hist[self.histPos-1])
            self.root.bind("<Control-z>",Control_Z)
            def Control_Shift_Z(key):
                if self.histPos != len(self.hist):
                    for frame in self.Frames:
                        self.canvas.delete(frame.Frame) 
                    self.Frames.clear()
                    for ob in self.map:
                        ob.delete()
                    self.map.clear()
                    loadedString(self,self.hist[self.histPos])
                    for ob in self.map:
                        ob.init()
                    self.victory = False
                    self.canvas.itemconfigure(self.label,text = ("ходят белые" if self.step else "ходят чёрные"))
                    self.canvas.lift(self.label)
                    self.root.title(f"game of chess. start file: {file}")
                    self.histPos += 1
                    print("loaded:",self.hist[self.histPos-1])
            self.root.bind("<Control-Shift-Z>",Control_Shift_Z)
            def Control_s(key):
                saveF()
            self.root.bind("<Control-s>",Control_s)
            def Control_u(key):
                try:
                    update()
                except:
                    base_snow_error()
            self.root.bind("<Control-u>",Control_u)
            def press_m(key):
                self.mode = multiple_choice("Выбор режима","выберете режим:\n",['play','random','bot', 'bot2', 'bot2 vs bot2','bot_random']+[mode.name for mode in self.modes])
                if self.mode not in ('play','random','bot', 'bot2', 'bot2 vs bot2','bot_random'):
                    for mode in self.modes:
                        if mode.name == self.mode:
                            mode.start()
                restart()
            self.root.bind("<m>",press_m)
            def clear_hist(key):
                self.histPos -= self.hist.clear()
                self.histPos += self.hist.set(getStringSave(self))
                print(self.histPos)
            self.root.bind("<c>",clear_hist)
            #curcle
            def in_map(vec):
                return vec[0]>0 and vec[0]<=8 and vec[1]>0 and vec[1]<=8
            def attak(ob,noname=False): #возращяет отакует ли введённую фигуру
                if noname:
                    return any(True for f in self.map if f.b != ob.b and any((f.pos+v.Vector2(mas=step)==ob.pos) for step in get_steps(f)))
                else:
                    for f in self.map:
                        if f.b!=ob.b:
                            steps = get_steps(f)
                            if any(True for step in steps if (f.pos+v.Vector2(mas=step)==ob.pos)):
                                return f
                    return False
            def attak_move(ob,step): #возвращяет будет ли возможна атака фигуры после её хода
                new_pos = ob.pos+v.Vector2(mas=step)
                def MyIscollide(pos):
                    if pos != ob.pos:
                        if pos == new_pos:
                            return ob
                        else:
                            return self.iscollide(pos)
                return any(True for f in self.map if f.b !=ob.b and any(f.pos+v.Vector2(mas=step)==new_pos for step in get_steps(f,MyIscollide)))
##                    for f in self.map:
##                        if f.b!=ob.b:
##                            
##                            steps = get_steps(f,MyIscollide)
##                            if any(f.pos+v.Vector2(mas=step)==new_pos for step in steps):
##                                return True
##                    return False
            def move_can_attak(ob,step,noname=False): # возращяет есть ли возможность отаковать фигуры после хода
                # поменялось с да нет и с фигура нет на число
                st_pos = ob.pos
                new_pos = st_pos+v.Vector2(mas=step)
                ob.pos = new_pos
                steps = get_steps(ob)
                if noname:
                    movs = {tuple(ob.pos+v.Vector2(mas=stepf)) for stepf in steps}
                    best_figure = None
                    pice_best_figure = 0
                    if len(steps)!=0:
                        for f in self.map:
                            if f.b != ob.b and get_pice(f)>pice_best_figure and (tuple(f.pos) in movs):
                                ob.pos = st_pos
                                return True
                    #otvet = any((True for f in self.map if f.b != ob.b and any((True for stepMyF in steps if f.pos==new_pos+v.Vector2(mas=stepMyF)))))
                else:
                    movs = {tuple(ob.pos+v.Vector2(mas=stepf)) for stepf in steps}
                    def pice(f):
                        return get_pice(f)/(get_pice(ob) if protection(f) else 1)
                    best_figure = None
                    pice_best_figure = 0
                    if len(steps)!=0:
                        for f in self.map:
                            if f.b != ob.b and pice(f)>pice_best_figure and (tuple(f.pos) in movs):
                                best_figure = f
                                pice_best_figure = pice(ob)
                ob.pos = st_pos
                return pice_best_figure
            def can_atack(ob,step): #возвращяет атакует ли фигура данным ходом
                return self.iscollide(ob.pos+v.Vector2(mas=step))
            def path_find(ob,step=None,noname=False):
                if step is None:
                    new_pos = ob.pos
                else:
                    new_pos = ob.pos+v.Vector2(mas=step)
                def MyIscollide(pos):
                    if pos != ob.pos:
                        if pos == new_pos:
                            return ob
                        else:
                            return self.iscollide(pos)
                if noname:
                    #not_b = (f for f in self.map if f.b != ob.b)
                    #return any(True for f2 in self.map if f2.b == ob.b and (not (f2 is ob)) and any(True for f in not_b if any(True for stepf in get_steps(f,MyIscollide) if f.pos+v.Vector2(mas=stepf)==f2.pos)))
                    pos_whites = {tuple(f.pos) for f in self.map if f.b == ob.b and (f is not ob)}
                    for f2 in self.map:
                        if f2.b != ob.b and f2.pos != new_pos:
                            steps = get_steps(f2, MyIscollide)
                            for stepf in steps:
                                if tuple(f2.pos+v.Vector2(mas=stepf)) in pos_whites:
                                    return True
                    #return any(True for f2 in self.map if f2.b == ob.b and (not (f2 is ob)) and any(True for f in self.map if f.b!=ob.b and any(f.pos+v.Vector2(mas=stepf)==f2.pos for stepf in get_steps(f,MyIscollide))))
                else:
                    best_figure = None
                    best_pice = 0
##                    for f2 in self.map:
##                        if f2.b == ob.b and not (f2 is ob):
##                            if any(True for f in self.map if f.b!=ob.b and any(f.pos+v.Vector2(mas=stepf)==f2.pos for stepf in get_steps(f,MyIscollide))) and get_pice(f2)>best_pice:
##                                best_figure = f2
##                                best_pice = get_pice(f2)
                    whites_pos = {tuple(f.pos): f.name for f in self.map if f.b == ob.b and (f is not ob)}
                    for f2 in self.map:
                        if f2.b != ob.b and (f2 is not ob) and f2.pos != new_pos:
                            steps = get_steps(f2,MyIscollide)
                            for stepf in steps:
                                name = whites_pos.get(tuple(f2.pos + v.Vector2(mas=stepf)))
                                if (name is not None) and get_npice(name)>best_pice:
                                    best_figure = name
                                    best_pice = get_npice(name)
                    return best_figure
##                for f in self.map:
##                    if f.b!=ob.b:
##                        steps = get_steps(f,MyIscollide)
##                        for f2 in self.map:
##                            if f2.b == ob.b and f2 != ob:
##                                if any(f.pos+v.Vector2(mas=stepf)==f2.pos for stepf in steps):
##                                    return f2
                
                return False
            def move_protection(ob, step): #возвращяет будетли фигура засшищять после хода
                step = v.Vector2(mas=step)
                new_pos = ob.pos + step
                st_pos = ob.pos
                ob.pos = new_pos
                def MyIscollide(pos):
                    res = self.iscollide(pos)
                    if res and res.b != ob.b:
                        return res
                steps = {tuple(step) for step in get_steps(ob,MyIscollide)}
                best_pice = 0
                best_figure = None
                for f in self.map:
                    if f.b == ob.b and (f is not ob) and (tuple(f.pos) in steps) and get_pice(f)>best_pice:
                        best_pice = get_pice(f)
                        best_figure = f.name
                ob.pos = st_pos
                return best_figure
            def protection(ob,step=None):  #возвращяет зашищяет ли фигуру
                if step == None:
                    new_pos = ob.pos
                else:
                    step = v.Vector2(mas=step)
                    new_pos = ob.pos + step
                def MyIscollide(pos):
                    if pos != ob.pos:
                        if pos == new_pos:
                            return ob
                        else:
                            return self.iscollide(pos)
                return any((True for f in self.map if f.b==ob.b and f != ob and any(True for stepf in get_steps(f,MyIscollide) if (f.pos+v.Vector2(mas=stepf)==new_pos))))
##                    for f in self.map:
##                        if f.b==ob.b and f != ob:
##                            steps = get_steps(f,MyIscollide)
##                            if any((f.pos+v.Vector2(mas=stepf)==new_pos) for stepf in steps):
##                                return True
##                    return False
            def end_path(ob): #возвращяет дойдёт ли пешка до конца
                return ((((not ob.b) and ob.pos[1] == 2) or (ob.b and ob.pos[1] == 7)) if ob.name == "пешка" else False)

            figures_pices = {
                'пешка': 1,
                'конь': 2,
                'слон': 2,
                'лодья': 3,
                'ферзь': 4,
                'король': 9
            }
            def get_npice(name):
                return figures_pices[name]
            def get_pice(ob):
                return figures_pices[ob.name]
            def get_king(b):
                for f in self.map:
                    if f.b is b and f.name == "король":
                        return f
            class imit_figure():
                def __init__(self, b):
                    self.b = b
                    self.pos = (-1,-1)
            def can_attak_king(ob,step): #функция проверяет есть ли ходы полезнее (которые атакуют вражеского короля)
                print(f"can_attak_king({ob},{step})")
                attackRes = can_atack(ob,step)
                if attackRes and attackRes.name == "король":
                    print("True part can_atack_king")
                    return True
                if ob.name == "король":
                    print("ok this is king")
                    if attak_move(ob, step):
                        print("attack_move king")
                        return False
                else:
                    print('ok this is not king')
                    if (path_find(ob, step)) == "король":
                        print('bad step. path_find True')
                        return False
                return True
            def step_figure(ob, step):
                step = v.Vector2(mas=step)
                move_to = step+ob.pos
                f = self.iscollide(move_to)
                if f:
                    if f.name == "король":
                        self.victory = True
                        self.canvas.itemconfigure(self.label,text = ("белые победили" if self.step else "чёрные победили"))
                    f.delete()
                    self.map.remove(f)
                change_name = ob.step(step,choice=False)
                self.canvas.lift(self.label)
                if change_name:
                    if self.mode == "bot" or self.mode == "bot2":
                        ob.change_name(v.getRandomProcentItem( {math.log((len(self.map)**1.05)/32/10)-0.7:'ферзь',100:'конь'} ))
                    else:
                        ob.change_name(('ферзь','лодья','слон','конь')[randint(0,3)])
                self.step = not self.step
                if not self.victory:
                    self.canvas.itemconfigure(self.label,text = ("ходят белые" if self.step else "ходят чёрные"))
                self.histPos += self.hist.set(getStringSave(self),self.histPos)
                        
            from random import randint
            from tkinter import simpledialog
            self.speed = 100
            def change_speed(k):
                new_speed = simpledialog.askfloat("Изменение скорости","напишите новую скорость цикла в милесекундах (ms)")
                if new_speed and int(new_speed) > 0:
                    self.speed = int(new_speed)
            self.root.bind("<s>",change_speed)
            id_figures = {
                'слон': 1,
                'лодья': 2,
                'король': 3,
                'пешка': 4,
                'ферзь': 5,
                'конь': 6
            }
            def in_nn(step_data):
                mas = []
                all_data = step_data.data
                all_data = all_data.split()
                for i in range(32*5):
                    if i<=len(all_data):
                        mas.extend(id_figures[all_data[i]], all_data[i+1], all_data[i+2], all_data[i+3], 2 if all_data[i+4] else 1)
                    else:
                        mas.extend((-1,-1,-1,-1,-1))
                return (mas, (step_data.step+1, step_data.idF+1), 2 if step_data.color else 1)
            def give_path(ob, step):
                king = get_king(ob.b)
                steps_king = get_steps(king)
                l_steps = len(steps_king)
                if l_steps == 0 or l_steps == 1:
                    pos_ob = ob.pos
                    ob.pos += v.Vector2('i', step)
                    steps_king = get_steps(king)
                    if len(steps_king)>l_steps:
                        if l_steps == 0:
                            res = 0.8
                        elif len(steps_king)>6:
                            res = 1.5
                        else:
                            res = 1
                    elif len(steps_king)==l_steps:
                        res = 1
                    else:
                        res = 1.5
                    ob.pos = pos_ob
                    return res
                return 1
            def frame():
                try:
                    if not self.victory and self.mode != "play" and (self.mode != 'bot2' or not self.step):
                        gc.disable()
                        if self.mode.startswith('bot2'):
                            all_steps = []
                        #работа json:
                        #all - положение всех фигур
                        #step - номер шага
                        #idF - id фигуры за которую идёт ход
                        #color - кто ходит

                        #работа неиросети:
                        #arg1-32*5 - положение всех фигур (если фигуры нет то -1)
                        #arg32*5+1 - то за что ходит неиросеть

                        #выводит:
                        #arg1 - номер шага фигуры
                        #arg2 - idF номер фигуры
                        
                        # если понадобится для ИИ
                        # if self.mode == "NN":
                        #     try:
                        #         data = in_nn({'all' : getStringSave(self) ,'idF' : 0, 'step' : 0, 'color': False})
                        #         res = neiro.load('./NN.neiro').forward(data[0]+[data[2]])
                        #         idF = 0
                        #         for f in self.map:
                        #             if not f.b:
                        #                 idF += 1
                        #                 if idF == res[1]:
                        #                     steps = get_steps(f)
                        #                     step_figure(f, steps[res[0]%len(steps)])
                        #     except:
                        #         pass

                        for ob in self.map:
                            if (((self.mode == "random" or self.mode == "bot2 vs bot2") and ob.b == self.step) or ((self.mode == "bot_random" or self.mode == "bot" or self.mode == "bot2") and ob.b == False and self.step==False)) and (True if self.mode == "bot" or self.mode == "bot2" else randint(1,len(self.map)//8)==1):
                                steps = get_steps(ob)
                                steps = [step for step in steps if (not self.iscollide(v.Vector2(mas=step)+ob.pos) or self.iscollide(v.Vector2(mas=step)+ob.pos).b != self.step) and in_map(ob.pos+v.Vector2(mas=step))]
                                if len(steps) != 0:
                                    #print(f"start work: {ob}")
                                    if self.mode == "bot" or self.mode.startswith('bot2'):
                                        #print(f"start work: {ob}")
                                        steps = tuple((1*
                                                    (1.2 if ob.name == "пешка" else 1)*
                                                    (1.1 * (ob.steps+1) if ob.name == "пешка" else 1)*
                                                    (3 if ob.name == "пешка" and step[1]==2 else 1)*
                                                    (6/(abs(ob.pos[0]-4)+1) if ob.name == "пешка" or ob.name == "конь" and sum(ob.steps for ob in self.map)<=6 else 1)*
                                                    (5*give_path(ob, step))*
                                                    (((1.1 if sum(ob.steps for ob in self.map)>6 else 1.5) * get_npice(move_protection(ob, step))) if move_protection(ob, step)!=None and move_protection(ob, step) != "король" and (not attak_move(ob,step)) else 1)*
                                                    ((2 if sum(ob.steps for ob in self.map)>6 else 1.2) if ob.name != "король" and protection(ob,step) else 1)*
                                                    (3*move_can_attak(ob,step) if move_can_attak(ob,step,noname=True) and (not attak_move(ob,step)) else 1)*
                                                    (4  if end_path(ob) else 1)*                               
                                                    ((5*get_pice(can_atack(ob,step))) if can_atack(ob,step) else 1)*
                                                    ((0.5*get_pice(ob)/(get_pice(attak(ob)) if ob.name != "король" and protection(ob) else 1)) if attak(ob,noname=True) else 1)/  
                                                    (5*get_npice(path_find(ob,step)) if path_find(ob,step,noname = True) else 1)/
                                                    (5*get_pice(ob) if attak_move(ob,step) else 1)
                                                    ,step)
                                                for step in steps)
                                        if self.mode.startswith('bot2'):
                                            # best = max(step_data[0] for step_data in steps)
                                            # best_steps = get_best_steps(steps,best)
                                            # all_steps.append((ob,best_steps,best))
                                            all_steps.extend((ob, step) for step in steps)
                                        else:
                                            step = v.getRandomProcentItem(steps,0.03)
                                        
                                        #print(steps)
                                    if self.mode == "random" or self.mode == "bot_random":
                                        step = v.Vector2(mas=steps[randint(0,len(steps)-1)])
                                    #if step and (self.mode!="bot" or (can_attak_king(ob, step))):
                                    if (not self.mode.startswith("bot2")) and step and (self.mode != 'bot' or can_attak_king(ob, step)):
                                        print("this is",path_find(ob,step,noname=True))
                                        print('died:',path_find(ob,step))
                                        step_figure(ob, step)
                        if self.mode.startswith("bot2"):
                            pf = path_find(imit_figure(not ob.b))
                            if pf == "король":
                                self.histPos += self.hist.set(getStringSave(self),self.histPos)
                                self.victory = True
                                self.canvas.itemconfigure(self.label,text = ("белые победили" if self.step else "чёрные победили"))

                            if not self.victory:
                                sort_steps = sorted(all_steps, key = lambda x: x[1][0], reverse=True)
                
                                for i in range(len(sort_steps)):
                                    step = sort_steps[i][1][1]
                                    ob = sort_steps[i][0]
                                    if can_attak_king(ob, step):
                                        step_figure(ob, step)
                                        break
                                else:
                                    self.victory = True
                                    self.canvas.itemconfigure(self.label,text = ("белые победили" if not self.step else "чёрные победили"))
                        gc.enable()
                except:
                    messagebox.askokcancel("Error", "при работе основного цикла игры возникла ошибка. я открою консоль. отправь что в консоли автору шахмат и перезапусти игру что бы ошибка пропала. если хочешь продолжить и тебе неважно на ошибку то нажми Enter в консоли")
                    snow_error()
                    input()
                for mode in self.modes:
                    try:
                        mode.iteration(self.mode)
                    except:
                        messagebox.askokcancel("Error", f"при работе основного цикла игры возникла ошибка в модификации {mode.name}. я открою консоль. отправь что в консоли автору мода (или шахмат) и перезапусти игру что бы ошибка пропала. если хочешь продолжить и тебе неважно на ошибку то нажми Enter в консоли")
                        snow_error()
                        input()
                    

                self.root.after(self.speed,frame)

            frame()
        else:
            print("такого режима не сушествует.")
        self.root.mainloop()
hide_console()
def load_mode(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        
        # Инициализация пространств имён
        local_vars = {}
        global_vars = {}
        
        try:
            # Безопасное выполнение кода с ограничением доступа
            exec(text, global_vars, local_vars)
        except Exception as e:
            print(type(e).__name__+':', e)
            return
        try:
            Mode = local_vars['main']()
            Mode.name
            Mode.iteration
            Mode.click
            Mode.description
            Mode.init
            Mode.start
        except:
            print('module not found main')
            return
    return Mode
import os
def load_modes(folder='./modes'):
    try:
        modes = os.listdir(folder)
    except FileNotFoundError:
        os.mkdir(folder)
        return load_modes(folder)
    modes_exec = []
    for mode in modes:
        mode_exec = load_mode(mode)
        if mode_exec is not None:
            modes_exec.append(mode_exec)
    return modes_exec
mode = multiple_choice("Выбор режима","выберете режим:\n",('play','random','bot', 'bot2', 'bot2 vs bot2','bot_random'))
messagebox.askquestion("Помошь по шахматам","help - Control-h")
if messagebox.askyesno("Загрузить?","Загрузить файл?"):
    file = filedialog.askopenfilename(
        title="Выберите файл для открытия",
        filetypes=(("Text Files", "*.txt"),)
    )
    text = None
else:
    file = False
text = "лодья 1.0 1.0 0 True лодья 8.0 1.0 0 True пешка 1.0 2.0 0 True пешка 2.0 2.0 0 True пешка 3.0 2.0 0 True пешка 4.0 2.0 0 True пешка 5.0 2.0 0 True пешка 6.0 2.0 0 True пешка 7.0 2.0 0 True пешка 8.0 2.0 0 True конь 2.0 1.0 0 True конь 7.0 1.0 0 True слон 6.0 1.0 0 True слон 3.0 1.0 0 True ферзь 5.0 1.0 0 True король 4.0 1.0 0 True лодья 1.0 8.0 0 False лодья 8.0 8.0 0 False конь 2.0 8.0 0 False конь 7.0 8.0 0 False слон 6.0 8.0 0 False слон 3.0 8.0 0 False ферзь 5.0 8.0 0 False король 4.0 8.0 0 False пешка 1.0 7.0 0 False пешка 2.0 7.0 0 False пешка 3.0 7.0 0 False пешка 4.0 7.0 0 False пешка 5.0 7.0 0 False пешка 6.0 7.0 0 False пешка 7.0 7.0 0 False пешка 8.0 7.0 0 False True "
game = game(mode,file,text)
game.start() 
