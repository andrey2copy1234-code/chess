import array,math

class operatorAndEq():
    __slots__ = ()
    def __isub__(self,index,value=None):
        if value==None:
            return self.__sub__(index,False)
        else:
            self.vector[index] -= value
    def __iadd__(self,index,value=None):
        if value==None:
            return self.__add__(index,False)
        else:
            self.vector[index] += value
    def __imul__(self,index,value=None):
        if value==None:
            return self.__mul__(index,False)
        else:
            self.vector[index] *= value
    def __itruediv__(self,index,value=None):
        if value==None:
            return self.__truediv__(index,False)
        else:
            self.vector[index] /= value
    def __ifloordiv__(self,index,value=None):
        if value==None:
            self.vector = self.__floordiv__(index,False)
        else:
            self.vector[index] //= value
#bin functions
def to_binNumber(ob):
    try:
        return binInt.__binNumber__()
    except:
        raise TypeError("cannot convert type {type(binNum).__name__}.")
def to_bin(num,b=32):
    try:
        newArray = array.array('b',(False for i in range(b)))
        i = 0
        while num > 0:
            newArray[i] = num%2
            num //= 2
            i+=1
        return newArray
    except:
        try:
            return num.__binNumber__()
        except:
            raise TypeError("cannot convert type {type(num).__name__}.")
def dectobin(binNum):
    try:
        c = 0
        for i in range(len(binNum)):
            if binNum[i]: c += 2**(i+1)
        return c
    except:
        try:
            dectobin(binNum.__binNumber__())
        except:
            raise TypeError("cannot convert type {type(binNum).__name__}.")
#class
class binInt(operatorAndEq):
    """number in binary system.
only positive."""
    __slots__ = ('v','b')
    def __init__(self,value=0,b=32):
        try:
            self.v = to_bin(value,b)
        except:
            try:
                self.v = value.v
                if b == 32:
                    b = len(value.v)
            except:
                try:
                    self.v = value
                    b = len(value)
                except:
                    raise TypeError(f"expected int or float or binInt or array got {str(type(value))[8:-2:]}")
        self.b = b
    #functions
    def copy(self):
        return binInt(self)
    def getLI(self):
        pi = 0
        for i in range(self.b):
            if self.v[i]: pi = i
        return pi
    #bin operators
    #<< and >>
    def __lshift__(self,v):
        c = self.copy()
        for i in range(c.b):
            if abs(i-v)<self.b:
                c.v[i] = self.v[i-v]
            else:
                c.v[i] = False
        return c
    def __rshift__(self,v):
        c = self.copy()
        for i in range(c.b):
            if i+v<=c.b-1:
                c.v[i] = self.v[i+v]
            else:
                c.v[i] = False
        return c
    #bits operators
    def __xor__(n1,n2):
        return binInt(array.array('b',(n1[i]^n2[i] for i in range(n1.b))))
    def __rand__(n1,n2):
        return binInt(array.array('b',(n1[i] and n2[i] for i in range(n1.b))))
    def __ror__(n1,n2):
        return binInt(array.array('b',(n1[i] or n2[i] for i in range(n1.b))))
    def __invert__(n1):
        return binInt(array.array('b',(not n1[i] for i in range(n1.b))))
    #math operators
    def __neg__(self):
        raise TypeError("The binInt type only supports positive values.")
    def __add__(n1,n2,copy=True):
        newArray = binInt(array.array('b',(False for i in range(n1.b))))
        p = False
        for i in range(n1.b):
            if (n1[i] and n2[i]) or (p and (n1[i] or n2[i])):
                p=True
            elif n1[i] or n2[i]:
                newArray[i] = True
            elif p:
                newArray[i] = True
                p = False
        return newArray
    def __sub__(n1,n2,copy=True):
        newArray = binInt(array.array('b',(False for i in range(n1.b))))
        p = False
        for i in range(n1.b)[::-1]:
            if not n1[i] and n2[i]:
                p = True
            elif n1[i] and not n2[i]:
                if p:
                    p = False
                else:
                    newArray[i] = True
        return newArray
    def __mul__(n1,n2,copy=True):
        if copy:
            newArray = n1.copy()
        else:
            newArray = n1
        for i in range(1,n2.b):
            if n2.v[i]:
                newArray = newArray+(n1<<i)
        return newArray
    def __floordiv__(n1,n2,copy = True):
        n1 = n1.copy()
        ot = n1.b
        start = ot-n2.getLI()
        while start!=0:
            number = binInt(n1.v[start:ot:])
            num3 = n2.copy()
            if num3 <= number:
                n1.v[start:ot:] = (number-num3).v
            if n1.v[start:ot:] != 0:
                st = start
                start -= ot-start
                ot = st
            else:
                st -= 1
                start-=1
        return n1
    def __pow__(self,s):
        v = 1
        for i in range(s):
            self *= self
        return v
    #logic operators
    def __eq__(n1,n2): #=
        return n1.v==n2.v
    def __lt__(n1,n2): #<
        try:
            for i in range(n1.b)[::-1]:
                if n2[i] and not n1[i]:
                    return True
                elif n1[i] and not n2[i]:
                    return False
        except: pass
        return False
    def __le__(n1,n2):
        try:
            for i in range(n1.b)[::-1]:
                if n2[i] and not n1[i]:
                    return True
                elif n1[i] and not n2[i]:
                    return False
        except: pass
        return True
    def __gt__(n1,n2): #>
        try:
            for i in range(n1.b)[::-1]:
                if n1[i] and not n2[i]:
                    return True
                elif n2[i] and not n1[i]:
                    return False
        except: pass
        return False
    def __ge__(n1,n2): #>
        try:
            for i in range(n1.b)[::-1]:
                if n1[i] and not n2[i]:
                    return True
                elif n2[i] and not n1[i]:
                    return False
        except: pass
        return True
    #magic metods
    def __abs__(self):
        return self.__float__()
    def __len__(self):
        return self.b
    def __int__(self):
        c = 0
        for i in range(self.b):
            if self.v[i]: c += 2**(i)
        return c
    def __float__(self):
        c = 0.0
        for i in range(self.b):
            if self.v[i]: c += 2**(i)
        return c
    def __getitem__(self,index):
        return self.v[index]
    def __setitem__(self,index,value):
        self.v[index] = value
    def __str__(self):
        return str(self.__int__())
    def __repr__(self):
        return f"binInt size {self.b}b array ({self.__int__}) and in binary system ({self.v})"
    #my magic metods
    def __vector__(self):
        return Vector(self.v)
class binIntPAN(binInt):
    __slots__ = ('v','b','p')
    def __init__(self,value=0,b=32,p=True):
        try:
            self.v = binInt(to_bin(value,b))
            self.p = abs(value) == value
        except:
            try:
                self.v = value.v
                if b == 32:
                    b = value.b
                    try:
                        p = value.p
                    except:
                        p = True
            except:
                try:
                    self.v = value
                    b = len(value)
                except:
                    raise TypeError(f"expected int or float or binInt or array got {str(type(value))[8:-2:]}")
        self.b = b
        self.p = p
    def __abs__(self):
        return dectobin(self.v.v)
    def __int__(self):
        return dectobin(self.v.v) if self.p else -dectobin(self.v.v)
    def __float__(self):
        return float(self.__int__())
    #math operators
    def __add__(n1,n2):
        #p
        try:   p2 = n2.p
        except:p2 = True
        #v
        try:   v2 = n2.v.v
        except:v2 = n2
        if n1.p == p2:
            return binIntPAN(n1.v + v2,n1.b,p2)
        else:
            return binIntPAN(n1.v - v2,n1.b,n1.p if n1.v>=n1.p else not n1.p)
    def __sub__(n1,n2):
        #p
        try:   p2 = n2.p
        except:p2 = True
        #v
        try:   v2 = n2.v.v
        except:v2 = n2
        if n1.p == p2:
            return binIntPAN(n1.v - v2,n1.b,p2 if n1.v>=p2 else not p2)
        else:
            return binIntPAN(n1.v + v2,n1.b,n1.p)
    def __mul__(n1,n2):
        #p
        try:   p2 = n2.p
        except:p2 = True
        #v
        try:   v2 = n2.v.v
        except:v2 = n2
        if n1.p == p2:
            return binIntPAN(n1.v * v2,n1.b,True)
        else:
            return binIntPAN(n1.v * v2,n1.b,False)
#main module
class VF(operatorAndEq):
    'this class vector functions. this class using all in this lib.'
    __slots__ = ()
    # __ function __ work two vectors
    def __add__(self,vector2,copy=True):
        if copy:
            try: vector = self.copy()
            except: pass
        for i in range(len(vector)):
            vector[i] += vector2[i]
        return vector
    def __neg__(self):
        v2 = self.copy()
        for i in v2.vector:
            i = -i
        return v2
    def __sub__(self,vector,copy=True):
        if copy:
            try:    vector = vector.copy()
            except: pass
        for i in range(len(vector)):
            vector[i] = self.vector[i]-vector[i]
        return vector
    def __mul__(self,vector,copy=True):
        try:
            if copy:
                try: vector = vector.copy()
                except: pass
            for i in range(len(vector)):
                vector[i] *= self.vector[i]
            return vector
        except:
            v = self.copy()
            for i in range(len(v)):
                v.vector[i] = self.vector[i]*vector
            return v
    def __rmul__(self,vector):
        try:
            try: vector = vector.copy()
            except: pass
            for i in range(len(vector)):
                vector[i] *= self.vector[i]
            return vector
        except:
            v = self.copy()
            for i in range(len(v)):
                v.vector[i] = self.vector[i]*vector
            return v

    def __truediv__(self,vector):
        try:
            try:    vector = vector.copy()
            except: pass
            for i in range(len(vector)):
                vector[i] = self.vector[i]/vector[i]
            return vector
        except:
            v = self.copy()
            for i in range(len(v)):
                v.vector[i] = self.vector[i]/vector
            return v
    def __floordiv__(self,vector):
        try:
            try:    vector = vector.copy()
            except: pass
            for i in range(len(vector)):
                vector[i] = self.vector[i]//vector[i]
            return vector
        except:
            v = self.copy()
            for i in range(len(v)):
                v.vector[i] //= vector
            return v
    def __rtruediv__(self,vector):
        try:
            try:    vector = vector.copy()
            except: pass
            for i in range(len(vector)):
                vector[i] /= self.vector[i]
            return vector
        except:
            v = self.copy()
            for i in range(len(v)):
                v.vector[i] = vector/v.vector[i]
            return v
    def __rfloordiv__(self,vector):
        try:
            try:    vector = vector.copy()
            except: pass
            for i in range(len(vector)):
                vector[i] /= self.vector[i]
            return vector
        except:
            v = self.copy()
            for i in range(len(v)):
                v.vector[i] = vector/v.vector[i]
            return v
    def __pow__(self,v):
        c = self.copy()
        for ob in c:
            ob **= v
        return c
    def AFEI(self,action,copy=True,useCompile=True,optimize=2):
        """makes a condition for each item.
This function is intended for user input.
use FFEI if you need to do the same but not with text but with a function.
FFEI is more productive."""
        if useCompile:
            action = compile(action, "<string>", "eval",optimize=optimize)
        if copy:
            c = self.copy()
        else:
            c = self
        for i in range(len(self.vector)):
            c.vector[i] = eval(action,locals = {'i':i,'vector':self.vector},globals = {})
        return c
    def FFEI(self,f,copy=True):
        """callabel function for each item.
are passed to the function:
    arg1 - vector
    arg2 - index
the function returns the value that should be at the index.
you must have a function:
    f(vector,i)
    
if you need an analog for user input use AFEI."""
        if copy:
            c = self.copy()
        else:
            c = self
        for i in range(len(self.vector)):
            c.vector[i] = f(self.vector,i)
        return c
    def revers(self):
        return type(self)(self.t,self.vector[::-1])
    #input one item and change all items
    def forward(self,num):
        return self+self.getLookVector()*num
    def back(self,num):
        return self+self.getLookVector()*num
    def setMagnitude(self):
        self.vector = self.getLookVector()
    #return One Item but everything has an impact
    def getMaxValue(self):
        return max(self.vector)
    def getMinValue(self):
        return min(self.vector)

    def getLookVector(self):
        return VectorFunctions.divide(self.vector,self.magnitude())
    def magnitude(self):
        m = 0
        l = len(self.vector)
        for num in self.vector:
            m+=num**l
        return m**(1/l)
    def getSumOfAllItems(self):
        return sum(self.vector)

    def copy(self):
        return type(self)(self.t,self.vector[::])
    # __ functions __ One Item 
    def __getitem__(self,index):
        try:
            #start
            if index.start==None:start=1
            else: start = index.start
            #end
            if index.stop==None :end=-1
            else: end   = index.stop
            #step
            if index.step==None :step=1
            else: step  = index.step
            #return
            return type(self)(self.t,self.vector[start:end:step])
        except:
            return self.vector[int(index)]
    def __setitem__(self,index,value):
        self.vector[index] = value

    def __abs__(self):
        return self.magnitude()
    ## __ functions __
        
    #syntax
        
    def __iterdir__(self):
        return self.vector
    
    ##transform
    
    def __vector__(self):
        return self.copy()
    def __str__(self):
        return f"vector {self.vector}"
    def __repr__(self):
        return f"vector {self.vector}"
    #сравнивание
    def __eq__(v1,v2): #=
        try:
            return v1.vector == v2.vector
        except:
            return v1.vector == v2
    def __lt__(v1, v2):#<
        return v1.magnitude() < v2.magnitude()
    def __le__(v1, v2):#<=
        return v1.magnitude() <= v2.magnitude()
    def __gt__(v1, v2):#>
        return v1.magnitude() > v2.magnitude()
    def __ge__(v1, v2):#>=
        return v1.magnitude() >= v2.magnitude()
class Vector(VF):
    'The vector object represents a N-dimensional C array.'
    __slots__ = ('vector','t')
    def __init__(self,t = None,mas = ()):
        if t==None:t='f'
        try:
            if t=='n':
                self.vector = mas
            else:
                self.vector = array.array(t,mas)
        except Exception as err:
            try:
                self.vector = array.array(t, (mas.x, mas.y))
            except:
                if isinstance(t,str):
                    raise TypeError(f"cannot convert type {type(mas).__name__}. excepted list or tuple got {type(mas).__name__}. perhaps you passed the wrong tier in one arg.")
                else:
                    raise TypeError(f"the first arg ia a string,not a {type(t).__name__}")
        self.t = t
    def insertItem(self,index,item):
        self.vector.i(index,item)
    def append(self,item):
        self.vector.append(item)
    def extend(self,items):
        self.vector.extend(items)
    def deleteItem(self,index=-1):
        self.vector.delete(index)
    def appendItems(self,items):
        self.vector.extend(items)
    def __len__(self):
        return len(self.vector)
class VectorFunctions:
    __slots__ = ()
    def sum(vector1,vector2):
        return array.array('f',[vector1[i]+vector2[i] for i in range(len(vector1))])
    def minus(vector1,vector2):
        return array.array('f',[vector1[i]-vector2[i] for i in range(len(vector1))])
    def ChangeItem(vector,index,value):
        v2 = vector[::]
        v2[index] = value
        return v2
    def ItemMinusValue(vector,index,value):
        vector[index] -= value
        return vector
    def ItemSumValue(vector,index,value):
        vector[index] += value
        return vector
    def multiply(vector,number):
        return array.array('f',[num*number for num in vector])
    def divide(vector,number):
        return array.array('f',[num/number for num in vector])
    def copy(vector):
        return vector[::]
class Vector2(VF):
    'The vector object represents a two-dimensional C array.'
    __slots__ = ('vector','t')
    def __init__(self,t = None,mas = (0,0)):
        if t==None:t='f'
        try:
            if isinstance(mas,Vector):
                self.vector = mas.vector
            else:
                self.vector = array.array(t,mas)
        except Exception as err:
            try:
                self.vector = to_vector(mas).vector
            except:
                try:
                    self.vector = array.array(t,(mas.x,mas.y))
                except:
                    if isinstance(t,str):
                        raise TypeError(f"cannot convert type {type(mas).__name__}. excepted list or tuple got {type(mas).__name__}. perhaps you passed the wrong tier in one arg.")
                    else:
                        raise TypeError(f"the first arg ia a string,not a {type(t).__name__}")
        self.t = t
    def getRad(self):
        return math.atan(self.vector[1]/self.vector[0])
    def __len__(self):
        return 2
    def __add__(self,vec2):
        return Vector2(mas=(self[0]+vec2[0],self[1]+vec2[1]))

class Vector2AndPos2():
    """represents two 2D vectors.
one for position.two for rotate."""
    __slots__ = ('pos','value')
    def __init__(self,pos=(0,0),value = (0,0)):
        self.pos = Vector2(mas = pos)
        self.value = Vector2(mas = value)
    def LookVector(self):
        return self.value.LookVector()
    def forward(self,value):
        self.pos += self.value.LookVector()*value
    def back(self,value):
        self.pos -= self.value.LookVector()*value
    def getRad(self):
        return self.value.getRad()
    def left(self,rad):
        rad = self.value.getRad()-rad
        m = self.value.getMagnitude()
        self.value[0] = math.cos(rad)*m
        self.value[1] = math.sin(rad)*m
    def right(self,rad):
        rad = self.value.getRad()+rad
        m = self.value.getMagnitude()
        self.value[0] = math.cos(rad)*m
        self.value[1] = math.sin(rad)*m
    def __len__(self):
        return 2
    def __floatdiv__(self,vector):
        try:
            ob2 = self.copy()
            for i in range(len(ob2.value)):
                ob2.value[i] //= vector[i]
                ob2.pos[i] //= vector[i]
            return ob2
        except:
            ob2 = self.copy()
            for i in range(len(ob2.value)):
                ob2.value[i] //= vector
                ob2.pos[i] //= vector
            return ob2
    def __truediv__(self,vector):
        try:
            ob2 = self.copy()
            for i in range(len(ob2.value)):
                ob2.value[i] /= vector[i]
                ob2.pos[i] /= vector[i]
            return ob2
        except:
            ob2 = self.copy()
            for i in range(len(ob2.value)):
                ob2.value[i] /= vector
                ob2.pos[i] /= vector
            return ob2
    def __mul__(self,vector):
        try:
            ob2 = self.copy()
            for i in range(len(ob2.value)):
                ob2.value[i] *= vector[i]
                ob2.pos[i] *= vector[i]
            return ob2
        except:
            ob2 = self.copy()
            for i in range(len(ob2.value)):
                ob2.value[i] *= vector
                ob2.pos[i] *= vector
            return ob2
    def copy(self):
        return Vector2AndPos2(self.pos,self.value)
    def __imul__(self,index,value=None):
        if value==None:
            return self * index
        else:
            self.vector[index] *= value
    def __itruediv__(self,index,value=None):
        if value==None:
            return self / index
        else:
            self.vector[index] /= value
    def __ifloatdiv__(self,index,value=None):
        if value==None:
            self.vector = self // index
        else:
            self.vector[index] //= value
def CreateMatrix2Rotate(rad):
    return Vector2(mas=(math.cos(rad),math.sin(rad)))
def fromRadToDeg(rad):
    return rad*(180/math.pi)
def fromDegToRad(deg):
    return deg/(180/math.pi)

def to_vector(ob):
    try:
        return ob.__vector__()
    except:
        raise TypeError("cannot convert type {type(ob).__name__}.")
#random functions
import random
def forItems(items,f):
    i=0
    if i<len(items):
        while i!=len(items):
            f(i,items[i])
            i+=1
def getRandomItem(items):
    return items[random.randint(0,len(items)-1)]
def getRandomProcentItem(items,t=1):
    rn = random.randint(0,int((100/(t))-1))*t+1
    #print(rn)
    minP = 0
    if type(items) is dict:
        for i in items:
            if minP<=rn and minP+i>=rn:
                return items[i]
            minP += i
    else:
        for procent, item in items:
            if minP<=rn and minP+procent>=rn:
                return item
            minP+=procent
        
#vector create functions
def vrange(start,end=False,step=1):
    return Vector(mas = range(start if end else 0,end if end else start,step))
def vrotate(deg):
    return Vector2(mas=(math.sin(deg),math.cos(deg)))
def vfromline(l,string):
    return Vector(mas = (eval(string) for i in range(l)))
class vrandom:
    def vrandom(l,start=1,end=100):
        return Vector(mas = (random.randint(start,end) for i in range(l)))
    def vrandomitem(l,items,t='f'):
        return Vector(t,mas = (items[random.randint(0,len(items)-1)] for i in range(l)))
    def vrandomPercentitem(l,items,t='f'):
        return Vector(t,mas = (getRandomProcentItem(items) for i in range(l)))
#test
if __name__ == "__main__":
    for i in range(5000000): pass
    print(sum(vrange(100)))
    print("4*2:",(binInt(4,8)*binInt(2,8)))
    from tests import test_speed as test
    print("test speed add")
    test("Vector(mas=(1,2,3))+Vector(mas=(3,1,5))",globalsNames=globals())
    print("built-in function")
    test("for i in range(10000): vrange(100)*2",globalsNames=globals())
    print("user defined function")
    test("""def f(v,i):
    return v[i] * 2
for i in range(10000): vrange(100).FFEI(f)""",globalsNames=globals())
    print("eval")
    test("for i in range(10000): vrange(100).AFEI('vector[i]*2')",globalsNames=globals())
    from tests import test_memory as memory
    memory(vrange(1000))
