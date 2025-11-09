import vector as v
#import ArrayC as v
from tkinter import messagebox
import tkinter as tk
from time import time
import threading as th
__version__ = '2.1'

item_select = None
def old_multiple_choice(title,suppl,items,select_val=True,break_val=None,dialogType="askyesno",dialogFn=None):
    i = -1
    ot = None
    if dialogFn == None:
        dialogFn = getattr(messagebox,dialogType)
    while ot != select_val:
        i += 1
        if i == len(items):
            i = 0
        ot = dialogFn(title,f"{suppl}{''.join([('(' if i == ii else '')+items[ii]+(')' if i == ii else '')+('-' if ii != len(items)-1 else '') for ii in range(len(items))])}")
        if ot == break_val:
            return None
        
    return items[i]
def multiple_choice(title,suppl,items,images=None, padding=2):
    global item_select
    if images is None:
        images = [None for i in range(len(items))]
    w = tk.Tk()
    w.title(title)
    w.geometry("300x100")
    tk.Label(w, text=suppl, font=("Arial", 12, "normal")).pack()
    item_select = None
    def select(item):
        global item_select
        item_select = item
        print("destroy window")
        print(item_select)
        w.destroy()
    def create_f(item):
        def comd():
            select(item)
        return comd
    for item, img_path in zip(items, images):
        if img_path is not None:
            img = tk.PhotoImage(img_path)
            tk.Button(w, text=item, command=create_f(item), image=img).pack(pady=padding)
        else:
            tk.Button(w, text=item, command=create_f(item)).pack(pady=padding)
    w.update()
    w.geometry(f"300x{int(w.winfo_height()+12*1.5*len(suppl)/6+25*len(items)+padding)}")
        
    w.protocol("WM_DELETE_WINDOW", create_f(False))
    while not item_select:
        w.update()
        th.Event().wait(1/30)
    print('return:', item_select)
    return item_select
size = 600

figure_picture = {
    'конь w': "C:/Users/Azerty/Desktop/шахматы/белые-конь.png",
    'конь b': "C:/Users/Azerty/Desktop/шахматы/черные-конь.png",
    'лодья w': "C:/Users/Azerty/Desktop/шахматы/белые-ладья.png",
    'лодья b': "C:/Users/Azerty/Desktop/шахматы/черные-ладья.png",
    'король w': "C:/Users/Azerty/Desktop/шахматы/белые-король.png",
    'король b': "C:/Users/Azerty/Desktop/шахматы/черные-король.png",
    'слон w': "C:/Users/Azerty/Desktop/шахматы/белые-слон.png",
    'слон b': "C:/Users/Azerty/Desktop/шахматы/черные-слон.png",
    'ферзь w': "C:/Users/Azerty/Desktop/шахматы/белые-дамка.png",
    'ферзь b': "C:/Users/Azerty/Desktop/шахматы/черные-дамка.png",
    'пешка w':"C:/Users/Azerty/Desktop/шахматы/белые-пешка.png",
    'пешка b':"C:/Users/Azerty/Desktop/шахматы/черные-пешка.png"
}

class LoadedError(Exception):
    __slots__ = ('message')
    def __init__(self,m):
        self.message = m
    def __str__(self):
        return self.message
class NaF_Error(Exception):
    __slots__ = ('message')
    def __init__(self,m):
        self.message = m
    def __str__(self):
        return self.message

def FPinC(posT):
    return v.Vector2(mas=posT)//(size/8)+v.Vector2(mas=(1,1))
def FCinP(posT):
    return (v.Vector2(mas=posT)-v.Vector2(mas=(1,1)))*(size/8)
def slon(ob,iscollide):
    pos = ob.pos
    step = ob.b
    mas = []
    for i in range(4):
        for i2 in range(1,8):
            if i == 0:
                move = v.Vector('f',(-i2,-i2))
            if i == 1:
                move = v.Vector('f',(-i2,i2))
            if i == 2:
                move = v.Vector('f',(i2,i2))
            if i == 3:
                move = v.Vector('f',(i2,-i2))
            c = iscollide(pos+move)
            if c:
                if c.b != step:
                    mas.append(move)
                break
            else:
                mas.append(move)
    return mas
def ferz(ob,iscollide):
    pos = ob.pos
    step = ob.b
    mas = []
    for i in range(4):
        for i2 in range(1,8):
            if i == 0:
                move = v.Vector('f',(-i2,0))
            if i == 1:
                move = v.Vector('f',(0,-i2))
            if i == 2:
                move = v.Vector('f',(i2,0))
            if i == 3:
                move = v.Vector('f',(0,i2))
            c = iscollide(pos+move)
            if c:
                if c.b != step:
                    mas.append(move)
                break
            else:
                mas.append(move)

    for i in range(4):
        for i2 in range(1,8):
            if i == 0:
                move = v.Vector('f',(-i2,-i2))
            if i == 1:
                move = v.Vector('f',(-i2,i2))
            if i == 2:
                move = v.Vector('f',(i2,i2))
            if i == 3:
                move = v.Vector('f',(i2,-i2))
            c = iscollide(pos+move)
            if c:
                if c.b != step:
                    mas.append(move)
                break
            else:
                mas.append(move)
    return mas
def loda(ob,iscollide):
    pos = ob.pos
    step = ob.b
    mas = []
    for i in range(4):
        for i2 in range(1,8):
            if i == 0:
                move = v.Vector('f',(-i2,0))
            if i == 1:
                move = v.Vector('f',(0,-i2))
            if i == 2:
                move = v.Vector('f',(i2,0))
            if i == 3:
                move = v.Vector('f',(0,i2))
            c = iscollide(pos+move)
            if c:
                if c.b != step:
                    mas.append(move)
                break
            else:
                mas.append(move)
    return mas

def peshka(ob,iscollide):
    c = iscollide(ob.pos+v.Vector(mas=(0,1))) if ob.b else iscollide(ob.pos-v.Vector(mas=(0,1)))
    c2 = iscollide(ob.pos+v.Vector(mas=(0,2))) if ob.b else iscollide(ob.pos-v.Vector(mas=(0,2)))
    if ob.steps == 0 and (not c) and (not c2):
        if ob.b:
            mas = [(0,1),(0,2)]
        else:
            mas = [(0,-1),(0,-2)]
    elif not c:
        if ob.b:
            mas = [(0,1),]
        else:
            mas = [(0,-1),]
    else:
        mas = []
    l = iscollide(ob.pos+v.Vector2(mas=(-1,(1 if ob.b else -1))))
    r = iscollide(ob.pos+v.Vector2(mas=(1,(1 if ob.b else -1))))
    if l and l.b != ob.b:
        if ob.b:
            mas.append((-1,1))
        else:
            mas.append((-1,-1))
    if r and r.b != ob.b:
        if ob.b:
            mas.append((1,1))
        else:
            mas.append((1,-1))
    return mas
def king(ob,iscollide):
    mas = [
            (1,0),
            (-1,0),
            (1,1),
            (-1,1),
            (1,-1),
            (-1,-1),
            (0,1),
            (0,-1)
        ]
    if ob.steps==0:
        l = iscollide(ob.pos - v.Vector2(mas=(3,0)))
        r = iscollide(ob.pos + v.Vector2(mas=(4,0)))
        if l and l.name == "лодья" and l.steps == 0 and (not iscollide(ob.pos-v.Vector2(mas=(1,0)))):
            mas.append((-2,0))
        if r and r.name == "лодья" and r.steps == 0 and (not iscollide(ob.pos+v.Vector2(mas=(1,0)))):
            mas.append((2,0))
    return mas
figure_moves = {
    'конь': (
        (1,-2),
        (2,-1),
        (2,1),
        (1,2),
        (-1,2),
        (-2,-1),
        (-2,1),
        (-1,-2)
    ),
    'пешка': peshka,
    'король': king,
    'ферзь': ferz,
    'слон': slon,
    'лодья': loda
}

def setSize(value):
    global size
    size = value

class Tween():
    __slots__ = ('canvas','root','Frame','pos','close','delayFrame','tf','ff','sp','startTime','inThread')
    def __init__(self,root,canvas,Frame,sp,pos,delayFrame = 16,tf=1,inThread=False):
        self.root = root
        self.canvas = canvas
        self.Frame = Frame
        self.pos = pos
        self.close = False
        self.delayFrame = delayFrame
        self.tf = tf
        self.ff = False
        self.sp = sp
        self.inThread = inThread
    def play(self):
        self.startTime = time()
        if self.inThread:
            while not self.close:
                self.step()
        else:
            self.step()
    def stop(self):
        self.close = True
    def step(self):
        if time()-self.startTime<self.tf and not self.close:
            newPos = self.sp+((self.pos-self.sp)*(time()-self.startTime)/self.tf)
            self.canvas.coords(self.Frame,newPos[0],newPos[1])
            if not self.inThread:
                self.root.after(self.delayFrame,self.step)
        else:
            self.canvas.coords(self.Frame,self.pos[0],self.pos[1])
            self.close = True
            if self.ff:
                self.ff()
    def callFunctionOnCompletion(self,f):
        self.ff = f
class figure():
    __slots__ = ('root','canvas','pictures','name','pos','b','Frame','steps','posP','iscollide')
    def __init__(self,root,canvas,pictures,iscollide,name,pos,b,steps=0):
        self.root = root
        self.canvas = canvas
        self.pictures = pictures
        self.iscollide = iscollide
        self.name = name
        self.pos = v.Vector2('f',pos)
        self.posP = (self.pos-v.Vector2(mas=(1,1)))*size/8+v.Vector2(mas=(size/16,size/16))
        self.b = b
        self.steps = steps
    def __str__(self):
        return f"{self.name} {self.pos[0]} {self.pos[1]} {self.steps} {self.b} "
    def __repr__(self):
        return f"figure(name = {self.name},pos = ({self.pos[0]},{self.pos[1]}),isWhile = {self.b})"
    def init(self):
        newPos = (self.pos-v.Vector2(mas=(1,1)))/8*size+v.Vector2(mas=(size/16,size/16))
        self.Frame = self.canvas.create_image(newPos[0],newPos[1],image = self.pictures[f"{self.name} {'w' if self.b else 'b'}"])
        return self.Frame
    def change_name(self,new_name):
        self.name = new_name
        self.canvas.itemconfigure(self.Frame,image = self.pictures[f"{self.name} {'w' if self.b else 'b'}"])
    def move(self,pos,inThread=False):
        newPos = (pos-v.Vector2(mas=(1,1)))*size/8+v.Vector2(mas=(size/16,size/16))
        t = Tween(self.root,self.canvas,self.Frame,self.posP.copy(),newPos,tf=0.2,inThread=inThread)
        t.play()
        self.posP = newPos
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        print('newPos:',self.pos)
        return t
    def step(self,step,new_name=None,choice=True):
        self.steps += 1
        self.canvas.lift(self.Frame)
        if self.name == "пешка" and ((self.pos[1] == 7) if self.b else (self.pos[1] == 2)):
            self.move(self.pos+step)
            if new_name == None:
                if choice:
                    self.change_name(multiple_choice("Выбор",f"Ваша пешка дошла до конца.\nвыберете фигуру в которую вы хотеле бы её превратить.\n",("ферзь","лодья","слон","конь")))
                    return self.name
                else:
                    return True
            else:
                self.change_name(new_name)
        elif self.name == "король":
            if step == v.Vector2(mas=(-2,0)) or step == v.Vector2(mas=(2,0)):
                print("рокировка")
                t = self.move(self.pos+step)
                def f():
                    print("call")
                    if step == v.Vector2(mas=(-2,0)):
                        self.iscollide(self.pos - v.Vector2(mas=(1,0))).step(v.Vector2(mas=(2,0)))
                    elif step == v.Vector2(mas=(2,0)):
                        self.iscollide(self.pos+v.Vector2(mas=(2,0))).step(v.Vector2(mas=(-3,0)))
                    else:
                        print("рокировка но не рокировка")
                t.ff = f
            else:
                self.move(self.pos+step)
        else:
            self.move(self.pos+step)

    def getInfo(self,infoName,arg1=None):
        if infoName == "isCastling":
            return self.steps == 0 and self.name == "лодья" and arg1.steps == 0 and arg1.name == "король"
        elif infoName == "isWhite":
            return self.b
        elif infoName == "isBlack":
            return not self.b
    def delete(self):
        self.canvas.delete(self.Frame)
        
def loaded(game,file,snowError=True):
    try: 
        file = open(file, 'r', encoding='utf-8')
    except:
        raise NaF_Error("file '{file}' not found")
    loadedString(game,file.read(),snowError)
    file.close()
def loadedString(game,str,snowError=True):
    if str.count('\n') == 0:
        string = ""
        p = 0
        name = ""
        x = 0
        y = 0
        for char in str:
            if char == " " and string != "":
                p +=1
                if p == 6:
                    p = 1
                    if string == "True":
                        game.step = True
                    elif string == "False":
                        game.step = False
                    else:
                        name = string
                elif p == 1:
                    name = string
                elif p == 2:
                    x = float(string)
                elif p == 3:
                    y = float(string)
                elif p == 4:
                    try:
                        steps_figure = float(string)
                    except:
                        if snowError:
                            action = multiple_choice("Error",f"""Вы видимо используете файл старой версии шахмат\n""",("ок","продолжить"))
                            if action == "ок":
                                game.root.destroy()
                                exit()
                        else:
                            raise LoadedError("old version chess")
                elif p == 5:
                    try:
                        game.create_figure(name,v.Vector('f',(x,y)),string == "True",steps=steps_figure)
                    except Exception as err:
                        if snowError:
                            action = multiple_choice("Error",f"""the file is corrupted or you have entered the wrong file.
        Error: {err}\n""",('ок','продолжить'))
                            if action == "ок":
                                game.root.destroy()
                                exit()
                        else:
                            raise LoadedError(f"Type: {type(err).__name__} | Message: {err}")
                string = ""
            else:
                string += char
        if p != 1:
            if snowError:
                action = multiple_choice("Error",f"""the file is corrupted or you have entered the wrong file.
        Error: there is not end\n""",('ок','продолжить'))
                if action == "ок":
                    game.root.destroy()
                    exit()
            else:
                raise LoadedError("not start figure")
        try:game.step
        except:
            if snowError:
                action = multiple_choice("Error",f"""the file is corrupted or you have entered the wrong file.
        Error: not saving step\n""",('ок','продолжить'))
                if action == "ок":
                    game.root.destroy()
                    exit()
            else:
                raise LoadedError("not step")
    else:
        if snowError:
            messagebox.askquestion("Error", "это файл видео")
            game.root.destroy()
            exit()
        else:
            raise LoadedError("not can loaded vidio")

def save(game,file):
    string = ""
    for ob in game.map:
        string += str(ob)
    file = open(file,'w', encoding='utf-8')
    file.write(f"{string}{game.step} ")
    file.close()
def getStringSave(game):
    string = ""
    for ob in game.map:
        string += str(ob)
    return f"{string}{game.step} "

class histStr():
    __slots__ = ('str')
    def __init__(self,string):
        self.str = [string]
    def set(self,string,i=None):
        if i==None:
            i = len(self.str)-1
        self.str.insert(i,string)
        return 1
    def get(self,i=None):
        if i==None:
            i=len(self.str)-1
        return self.str[i]
    def clear(self):
        l = len(self)
        self.str = []
        return l
    def __getitem__(self,i):
        return self.get(i)
    def __len__(self):
        return len(self.str)
def openV(game, path ):
    file = open(path, 'r', encoding='utf-8')
    text = file.read()
    file.close()
    lines = text.split('\n')
    loadedString(game, lines[0])
    for ob in game.map:
        ob.init()
    game.canvas.lift(game.label)
    class step_function():
        def __call__(self, *args, **kwds):
            try:
                self.step(*args, **kwds)
            except AttributeError:
                del self
        def step(self, _):
            if self.counter < len(lines):
                line = lines[self.counter]
                for ob in game.map:
                    ob.delete()
                game.map.clear()
                loadedString(game, line)
                for ob in game.map:
                    ob.init()
                game.canvas.lift(game.label)
                # parse_line = line.split()
                # instr = parse_line[0]
                # args = parse_line[1:]
                # if instr == "move":
                #     idF = int(args[0])
                #     new_x = int(args[1][0])
                #     new_y = int(args[1][1])
                #     move = v.Vector2(mas=(new_x, new_y))-game.map[idF].pos
                #     game.move_figure(idF, move)
                # elif instr == "change":
                #     idF = int(args[0])
                #     new_name = args[1]
                #     game.map[idF].change_name(new_name)

                    
                self.counter += 1
                # if instr == "move":
                #     game.root.after(speed, step)
                # # else:
                # #     step()
            else:
                game.root.unbind('<Right>')
                game.root.unbind('<Left>')
        def back_step(self, _):
            if self.counter > 0:
                self.counter -= 1
                line = lines[self.counter]
                for ob in game.map:
                    ob.delete()
                game.map.clear()
                loadedString(game, line)
                for ob in game.map:
                    ob.init()
                game.canvas.lift(game.label)
    sfi = step_function()
    sfi.counter = 1
    game.root.bind('<Right>', sfi)
    game.root.bind('<Left>', sfi.back_step)
def saveV(game, path):
    text = ""
    for i in range(game.histPos):
        if i == 0:
            text = game.hist[0]
            parse_pos_do = text.split()
        else:
            histPos = game.hist[i]
            text += '\n'+histPos
            # parse_pos = histPos.split()
            # for j in range(len(parse_pos)):
            #     data = parse_pos[j]
            #     if data != parse_pos_do[j] and data != (parse_pos_do[j+5] if len(parse_pos_do)>j+5 else data):
            #         if not (i+3)%5==0:
            #             print(data)
            #             print(i)
            #             print(parse_pos[i-1:i+2])
            #             try:
            #                 float(data)
            #                 try:
            #                     float(parse_pos[j+1])
            #                     text_format = data[:1]+parse_pos[j+1][:1]
            #                 except:
            #                     text_format = parse_pos[j-1][:1]+data[:1]
            #                 text += f"\nmove {i} {text_format}"
            #             except:
            #                 text += f"\nchange {i} {data}"
            # parse_pos_do = parse_pos

            
    file = open(path, 'w', encoding='utf-8')
    file.write(text)
    file.close()
##def sumStrs(strings):
##    s = ''
##    for string in strings:
##        s += string
##    return s
##def sumMas(mass):
##    mas = []
##    for i in mass:
##        i = [i]
##        mas += i
##    return mas
##def insert(string,i,*strings):
##    try:
##        return string[:i]+sumStrs(strings)+string[i:]
##    except:
##        return string[:i]+sumMas(strings)+string[i:]
##class histStr():
##    __slots__ = ('data')
##    def __init__(self,string):
##        self.data = ['i',0,string]
##    def get(self,i=None):
##        if i == None:
##            i = len(self.data)//3
##        s = ""
##        for i in range(0,i*3,3):
##            if self.data[i] == 'i':
##                print(f"до:{s}")
##                s = insert(s,self.data[i+1],self.data[i+2])
##                print(f"после:{s}")
##            elif self.data[i] == 'd':
##                print(i,len(self.data))
##                s = s[0:self.data[i+1]]+s[self.data[i+2]:len(s)]
##            elif self.data[i] == 'm':
##                s = s*self.data[i+1]
##            else:
##                print(len(s))
##                s = s[:self.data[i+1]]+self.data[i]+s[self.data[i+2]:]
##        return s
##    def d(self,sttI,endI,histPos=None):
##        if histPos == None:
##            histPos = len(self)
##        self.data.indert(histPos,('d',sttI,endI))
##    def c(self,sttI,endI,str,histPos):
##        if histPos==None:
##            histPos = len(self)
##        self.data = insert(self.data,histPos*3,str,sttI,endI)
##    def i(self,i,str):
##        self.data.extend(('i',i,str))
##    def mul(self,n):
##        self.data.extend(('m',n,None))
##    def set(self,string,histPos=None):
##        if histPos==None:
##            histPos = len(self)
##        try: string.get()
##        except: pass
##        p = False
##        sttI = 0
##        i3 = 0
##        str = self.get()
##        for i in range(len(str)):
##            c1 = str[i]
##            c2 = string[i]
##            if c1 == c2:
##                if p:
##                    p = False
##                    self.c(sttI,i,string[sttI:i],histPos)
##                    i3 += 1
##                else:
##                    sttI = i
##            else:
##                p = True
##        if p:
##            self.c(sttI,i,string[sttI:i],histPos)
##            i3 += 1
##        return i3 
##    def __getitem__(self,i):
##        self.get(i)
##    def __iadd__(self,str):
##        str = histStr(str)
##        i(len(self.data)-1,str)
##    def __imul__(self,n):
##        self.mul(n)
##        
##    def __len__(self):
##        return len(self.data)//3
    

class FrameC():
    __slots__ = ('Frame','pos','move')
    def __init__(self,Frame,pos,move):
        self.Frame = Frame
        self.pos = pos
        self.move = move
def hide_console():
    from ctypes import windll
    windll.user32.ShowWindow(windll.kernel32.GetConsoleWindow(), False)
#проверка
SETUP_DEFAULT = {
    'paths ./': False,
    'path': 'default'
}
setup = None
from json import dumps, loads
def check():
    global setup
    try:
        file = open('./setup_chess','r')
        text = file.read()
        file.close()
        try:
            setup = loads(text)
        except:
            setup = SETUP_DEFAULT
    except FileNotFoundError:
        file = open('./setup_chess','w')
        text = dumps(SETUP_DEFAULT)
        file.write(text)
        file.close()
        setup = SETUP_DEFAULT
def update_setup():
    global setup
    print("update")
    file = open('./setup_chess','w')
    file.write(dumps(setup))
    file.close()
def change_dirictory_images(dirictory):
    for img_name in figure_picture:
        figure_picture[img_name] = dirictory+figure_picture[img_name][31:]
check()
if setup == None:
    setup = SETUP_DEFAULT
    update_setup()
if setup.get('paths ./'):
    change_dirictory_images('.')
if setup.get('path') and setup['path']!='default':
    change_dirictory_images(setup['path'])
def check_images():
    not_found = []
    for img_name in figure_picture:
        img_val = figure_picture[img_name]
        try:
            open(img_val,'rb').close()
        except FileNotFoundError:
            not_found.append(img_name)
    return not_found
from tkinter import simpledialog
not_found = check_images()
if len(not_found)>0:
    messagebox.showerror('Error',f'произошла ошибка. игра не нашла {len(not_found)} изображен{'ий' if len(not_found)>2 else 'ия' if len(not_found)==2 else 'ие'} фигур.')
    if len(not_found) == len(figure_picture):
        choice = ('вы исправите.','вы переместите картинки туда же где и chess.py.', 'поменять директорию поиска','ничего не делать')+(('использовать относительный путь') if not setup.get('paths ./') else ('удалить использование относительного путя'),)
        select = multiple_choice('выберете вареант решения проблеммы.', 'произошла ошибка. выберите вареант исправления ошибки:\n',choice)
        if select != 'вы исправите.' and select != 'вы переместите картинки туда же где и chess.py.' and select != 'ничего не делать':
            if select == 'использовать относительный путь':
                setup['paths ./'] = True
            else:
                setup['paths ./'] = False
                if select == 'поменять директорию поиска':
                    setup['path'] = simpledialog.askstring('Выбор','введите дирикторию (default для по умолчанию):')
            update_setup()
    else:
        messagebox.showerror('Error',f"похоже вы удалили или переименовали эти изображения:\nформат имя+w если белый иначе +b\n{not_found}")
