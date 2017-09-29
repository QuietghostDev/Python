#Grapher V2.1.0 by Ben Hamilton

from Tkinter import *
from math import *

#---------------------------------------------------------------------------
#standard definitions

root=Tk()
root.title('Graph')
win=Canvas(root,width=500,height=500,bg='white')
win.pack()
text=[]
xs=1
ys=1
sw=Toplevel(root)
sw.title('Function')
functions=[]
old=[250,250]
x_lines=[]
y_lines=[]
width=500
height=500

#--------------------------------------------------------------------------
#math definitions

def csc(x):
    return sin(x)**-1
def sec(x):
    return cos(x)**-1
def cot(num):
    return tan(num)**-1
def fac(num):
    tot=1
    if type(num) is not int:
        raise ValueError
    for i in range(num):
        tot=tot*(i+1)
    return tot
#----------------------------------------------------------------------------
#window definitions

def init_lines():
    #scaling lines
    x_lines.append(win.create_line(0,0,0,height,fill='grey'))
    x_lines.append(win.create_line(50,0,50,height,fill='grey'))
    x_lines.append(win.create_line(100,0,100,height,fill='grey'))
    x_lines.append(win.create_line(150,0,150,height,fill='grey'))
    x_lines.append(win.create_line(200,0,200,height,fill='grey'))
    x_lines.append(win.create_line(250,0,250,height,fill='black'))
    x_lines.append(win.create_line(300,0,300,height,fill='grey'))
    x_lines.append(win.create_line(350,0,350,height,fill='grey'))
    x_lines.append(win.create_line(400,0,400,height,fill='grey'))
    x_lines.append(win.create_line(450,0,450,height,fill='grey'))
    y_lines.append(win.create_line(0,0,width,0,fill='grey'))
    y_lines.append(win.create_line(0,50,width,50,fill='grey'))
    y_lines.append(win.create_line(0,100,width,100,fill='grey'))
    y_lines.append(win.create_line(0,150,width,150,fill='grey'))
    y_lines.append(win.create_line(0,200,width,200,fill='grey'))
    y_lines.append(win.create_line(0,250,width,250,fill='black'))
    y_lines.append(win.create_line(0,300,width,300,fill='grey'))
    y_lines.append(win.create_line(0,350,width,350,fill='grey'))
    y_lines.append(win.create_line(0,400,width,400,fill='grey'))
    y_lines.append(win.create_line(0,450,width,450,fill='grey'))

def init_second_window(scale):
    rx=Button(sw,command=scale.decrease_x_axis,text='Reduce X-axis')
    ex=Button(sw,command=scale.increase_x_axis,text='Extend X-axis')
    ry=Button(sw,command=scale.decrease_y_axis,text='Reduce Y-axis')
    ey=Button(sw,command=scale.increase_y_axis,text='Extend Y-axis')
    ok=Button(sw,command=get_and_eval_all,text='Print Function')
    add=Button(sw,command=add_function,text='Add Function')
    remove=Button(sw,command=remove_function,text='Remove Function')
    ok.grid(row=0,column=0,columnspan=2)
    rx.grid(row=1,columnspan=2,sticky=W+E)
    ry.grid(row=1,column=2,columnspan=2,sticky=W+E)
    ex.grid(row=2,column=0,columnspan=2,sticky=W+E)
    ey.grid(row=2,column=2,columnspan=2,sticky=W+E)
    add.grid(row=3,columnspan=2,sticky=W+E)
    remove.grid(row=3,column=2,columnspan=2,sticky=W+E)

#---------------------------------------------------------------------
#Layout

def reset():
    i=0
    while i<len(functions):
        functions[i].yeq.grid_remove()
        functions[i].inpt.grid_remove()
        functions[i].printval.grid_remove()
        functions[i].checkbox.grid_remove()
        functions[i].inputvallabel.grid_remove()
        functions[i].inputval.grid_remove()
        functions[i].y_output_label.grid_remove()
        i+=1

def layout():
    '''This function handles the layout of all the function stuff--their check boxes
    and their input boxes.'''
    i=0 #counter
    r=0 #row
    c=4 #column
    try:
        reset() #reset the widgets
    except:
        pass
    while i<len(functions):
        functions[i].yeq.grid(row=r*2,column=c+1)
        functions[i].inpt.grid(row=r*2,column=c+2,columnspan=2)
        functions[i].printval.grid(row=r*2+1,column=c,columnspan=4,sticky=W+E)
        functions[i].checkbox.grid(row=r*2,column=c)
        functions[i].inputvallabel.grid(row=r*2,column=c+4)
        functions[i].inputval.grid(row=r*2,column=c+5)
        functions[i].y_output_label.grid(row=r*2+1,column=c+4,columnspan=2)
        i+=1
        r+=1
    
    

#---------------------------------------------------------------------
#Multi-Function Related Code

def add_function(event=None):
    functions.append(Function())
    layout()

def remove_function(event=None):
    functions[len(functions)-1].var.set(0)
    functions[len(functions)-1].get_and_eval()
    functions[len(functions)-1].get_x_y()
    reset()
    functions.pop()
    layout()

def register_all(event):
    i=0
    while i<len(functions):
        functions[i].get_x_y(event)
        i+=1

def get_and_eval_all(event=None):
    i=0
    while i<len(functions):
        functions[i].get_and_eval()
        functions[i].eval_x_value()
        i+=1


#---------------------------------------------------------------------
#scaling

def init_scaling():
    text.append(win.create_text(10,260,text=s.snx[0]))
    text.append(win.create_text(50,260,text=s.snx[1]))
    text.append(win.create_text(100,260,text=s.snx[2]))
    text.append(win.create_text(150,260,text=s.snx[3]))
    text.append(win.create_text(200,260,text=s.snx[4]))
    text.append(win.create_text(240,260,text=s.snx[5]))
    text.append(win.create_text(300,260,text=s.snx[6]))
    text.append(win.create_text(350,260,text=s.snx[7]))
    text.append(win.create_text(400,260,text=s.snx[8]))
    text.append(win.create_text(450,260,text=s.snx[9]))
    #ys
    text.append(win.create_text(240,10,text=s.sny[0]))
    text.append(win.create_text(240,50,text=s.sny[1]))
    text.append(win.create_text(240,100,text=s.sny[2]))
    text.append(win.create_text(240,150,text=s.sny[3]))
    text.append(win.create_text(240,200,text=s.sny[4]))
    text.append(win.create_text(240,250,text=s.sny[5]))
    text.append(win.create_text(240,300,text=s.sny[6]))
    text.append(win.create_text(240,350,text=s.sny[7]))
    text.append(win.create_text(240,400,text=s.sny[8]))
    text.append(win.create_text(240,450,text=s.sny[9]))
    
def reset_scale():
    i=0
    while i<len(text)/2:
        win.itemconfig(text[i],text=s.snx[i])
        i+=1
    while i<len(text):
        win.itemconfig(text[i],text=s.sny[i-10])
        i+=1
    get_and_eval_all()

class Scaling():
    xscale=0.0
    yscale=0.0
    def __init__(self,xs,ys):
        self.xscale=float(xs)
        self.yscale=float(ys)
        self.snx=[self.xscale*-5,self.xscale*-4,self.xscale*-3,self.xscale*-2,self.xscale*-1,0,self.xscale,self.xscale*2,self.xscale*3,self.xscale*4]
        self.sny=[self.yscale*5,self.yscale*4,self.yscale*3,self.yscale*2,self.yscale*1,0,self.yscale*-1,self.yscale*-2,self.yscale*-3,self.yscale*-4]
    def reset_scaling(self,center=0):
        i=-5
        while i<5:
            posx=i*50+250
            posy=i*50+250
            posx=i-(posx-c.center[0])/500*10
            posy=-(i+(posy-c.center[1])/500*-10)
            self.snx[i+5]=self.xscale*posx
            if posy!=0:
                self.sny[i+5]=self.yscale*posy
            else:
                self.sny[i+5]=''
            i+=1
        reset_scale()

    def decrease_x_axis(self):
        self.xscale=self.xscale*0.5
        self.reset_scaling()
    def increase_x_axis(self):
        self.xscale=self.xscale*2
        self.reset_scaling()
    def decrease_y_axis(self):
        self.yscale=self.yscale*0.5
        self.reset_scaling()
    def increase_y_axis(self):
        self.yscale=self.yscale*2
        self.reset_scaling()

    def was(self,coord):#determines actual coordinate
        i=coord/500
        coord=coord+500*-i
        return coord

    def move_numbers(self):
        i=0
        ox=c.center[0]
        oy=c.center[1]
        x=240-ox
        if x<20:
            x=20
        if x>480:
            x=480
        y=260-oy
        if y<10:
            y=10
        if y>490:
            y=490
        while i<10:
            win.coords(text[i],self.was(50*i-ox),y)
            i+=1
        while i<20:
            win.coords(text[i],x,self.was(i*50-oy))
            i+=1

    def is_bold(self,num):#determine if the axis lines are bold
        if num>-250 and num<250:
            return True
        return False

    def move_lines(self):
        i=0
        ox=c.center[0]
        oy=c.center[1]
        #determine if the axis lines are bold
        if self.is_bold(ox):
            win.itemconfig(x_lines[5],fill='black')
        else:
            win.itemconfig(x_lines[5],fill='grey')
        if self.is_bold(oy):
            win.itemconfig(y_lines[5],fill='black')
        else:
            win.itemconfig(y_lines[5],fill='grey')
        #------
        while i<len(x_lines): #or y_lines for that matter
            win.coords(x_lines[i],self.was(i*50-ox),0,self.was(i*50-ox),500)
            win.coords(y_lines[i],0,self.was(i*50-oy),500,self.was(i*50-oy))
            i+=1

    def init_scaling(self):
        text.append(win.create_text(10,260,text=s.snx[0]))
        text.append(win.create_text(50,260,text=s.snx[1]))
        text.append(win.create_text(100,260,text=s.snx[2]))
        text.append(win.create_text(150,260,text=s.snx[3]))
        text.append(win.create_text(200,260,text=s.snx[4]))
        text.append(win.create_text(240,260,text=s.snx[5]))
        text.append(win.create_text(300,260,text=s.snx[6]))
        text.append(win.create_text(350,260,text=s.snx[7]))
        text.append(win.create_text(400,260,text=s.snx[8]))
        text.append(win.create_text(450,260,text=s.snx[9]))
        #ys
        text.append(win.create_text(240,10,text=s.sny[0]))
        text.append(win.create_text(240,50,text=s.sny[1]))
        text.append(win.create_text(240,100,text=s.sny[2]))
        text.append(win.create_text(240,150,text=s.sny[3]))
        text.append(win.create_text(240,200,text=s.sny[4]))
        text.append(win.create_text(240,300,text=s.sny[5]))
        text.append(win.create_text(240,350,text=s.sny[6]))
        text.append(win.create_text(240,400,text=s.sny[7]))
        text.append(win.create_text(240,450,text=s.sny[8]))
        text.append(win.create_text(240,490,text=s.sny[9]))

#-----------------------------------------------------------------------------------
#evaluatory section
class Function:

    def __init__(self):
        self.lines=[]
        for z in range(501):
            self.lines.append(win.create_line(0,0,1,1,fill='black',width=1))
        self.function=None
        self.inpt=Entry(sw)
        self.cir=win.create_oval(0,0,1,1,fill='black')
        self.yeq=Label(sw,text='y=')
        self.var=IntVar()
        self.checkbox=Checkbutton(sw, text='Show', variable=self.var, command=self.reprint)
        self.vals=StringVar()
        self.printval=Label(sw,textvariable=self.vals)
        self.inputvallabel=Label(sw,text='|| Enter Value for x:')
        self.inputval=Entry(sw)
        self.y_output=StringVar()
        self.y_output_label=Label(sw,textvariable=self.y_output)

    def eval_x_value(self):
        try:
            num=eval(self.inputval.get())
            value=self.eval_one_value(num)
            self.y_output.set(' y='+str(value)+', slope='+str(self.get_slope(num)))
        except:
            self.y_output.set(' y=[Illegal Input], slope=undef')
    
    def get_function(self):
        return self.inpt.get()

    def filter_func(self):
        #replace anything that needs replacement
        self.function=self.function.replace('^','**')
        self.function=self.function.replace(')(',')*(')
        self.function=self.function.replace('x(','x*(')
        self.function=self.function.replace(')x',')*x')
        self.function=self.function.replace('xx','x*x')
        self.function=self.function.replace('xx','x*x')
        self.function=self.function.replace('x'+'l','x*l')
        self.function=self.function.replace('xs','x*s')
        self.function=self.function.replace('xc','x*c')
        self.function=self.function.replace('xt','x*t')
        self.function=self.function.replace('xa','x*a')
        self.function=self.function.replace('xf','x*f')
        self.function=self.function.replace('x!','fac(x)')
        for c in range(10):
            self.function=self.function.replace(str(c)+'(',str(c)+'*(')
            self.function=self.function.replace(')'+str(c),')*'+str(c))
            self.function=self.function.replace(str(c)+'x',str(c)+'*x')
            self.function=self.function.replace('x'+str(c),'x*'+str(c))
            self.function=self.function.replace(str(c)+'l',str(c)+'*l')
            self.function=self.function.replace(str(c)+'s',str(c)+'*s')
            self.function=self.function.replace(str(c)+'c',str(c)+'*c')
            self.function=self.function.replace(str(c)+'t',str(c)+'*t')
            self.function=self.function.replace(str(c)+'a',str(c)+'*a')
            self.function=self.function.replace(str(c)+'!','fac('+str(c)+')')
            self.function=self.function.replace(str(c)+'f',str(c)+'*f')

    def get_and_eval(self):
        #the name says all
        self.function=self.get_function()
        self.filter_func()
        self.eval_function()

    def reprint(event):
        get_and_eval_all()

    def eval_function(self):
        #evaluates an entire function based on the x-span of the window
        new_func=self.function
        new_func_2=self.function
        x=(-5.00+c.center[0]/50.0)*s.xscale #----------------------->>>>>>>>adding the offset puts it in, subtracting it undoes it<<<<<<<<<<<<<<<-------------------
        xs=-5.00
        i=0
        while xs<5.01:#adjust to scale
            new_func=new_func.replace('x','('+str(x)+')')
            new_func_2=new_func_2.replace('x','('+str(x+(0.02*s.xscale))+')')
            try:
                if self.var.get()==0:
                    raise IndexError
                y=eval(new_func)/s.yscale
                y1=eval(new_func_2)/s.yscale
                if y-y1<10*s.yscale and y-y1>-10*s.yscale:
                    win.coords(self.lines[int(xs*50+250)],
                               int(xs*50+251),int(250-y*50-c.center[1]),int((xs+0.02)*50+251),int(250-y1*50-c.center[1]))
                else:
                    win.coords(self.lines[int(xs*50+250)],-5,-5,-3,-3)
                    
            except:
                win.coords(self.lines[int(xs*50+250)],-5,-5,-3,-3)
            new_func=self.function
            new_func_2=self.function
            x+=(0.01*s.xscale)
            xs+=0.01

    def eval_one_value(self,value):#evaluates a single input value
        self.function=self.get_function()
        self.filter_func()
        x=value
        self.function.replace('x','('+str(x)+')')
        return eval(self.function)

    def get_x_y(self,event=None):#displays the x/y values of where the mouse is at
        x=0
        try:
            x=(event.x-250)/50.0
            x=(c.center[0]/50.0+x)*s.xscale
            if self.var.get()==0:#check if the checkbox is checked
                raise IndexError
            y=self.eval_one_value(x)
            self.vals.set('x='+str(x)+', y='+str(y)+', slope='+str(self.get_slope(x)))
            win.coords(self.cir,event.x-3,247-y/s.yscale*50-c.center[1],event.x+2,252-y/s.yscale*50+2-c.center[1])
        except:
            self.vals.set('x='+str(x)+', y=undef, slope=undef')
            win.coords(self.cir,-5,-5,-5,-5)

    def get_slope(self,value):
        x1=self.eval_one_value(value)
        x2=self.eval_one_value(value+0.000000001)
        return int(round((x2-x1)/0.000000001*100000))/100000.0

#----------------------------------------------------------------------------------
#Offsetting Code

def real_coords(x,y):
    return [x+250,y+250]

def centered_coords(center_offset,x,y):
    return [x-center_offset[0],y-center_offset[1]]

def scaled_coords(ccx,ccy):
    return [ccx/s.xscale,ccy/s.yscale]

def offset(center,x,y):
    [x,y]=centered_coords(center,x,y)
    [x,y]=scaled_coords(x,y)
    [x,y]=real_coords(x,y)
    return [x,y]

def get_center():
    return c.center

class Center:
    center=[0,0]
    old=None
    
    def __init__(self):
        pass

    def change_center(self,event):
        if self.old==None:
            self.old=[event.x,event.y]
        new_x=event.x
        new_y=event.y
        self.center[0]=self.center[0]-(new_x-self.old[0])
        self.center[1]=self.center[1]-(new_y-self.old[1])
        self.old=[new_x,new_y]
        get_and_eval_all()
        s.move_numbers()
        s.move_lines()
        s.reset_scaling()

    def end_change(self,event):
        self.old=None



#----------------------------------------------------------------------------------
#Final Setup


s=Scaling(xs,ys)
c=Center()
init_lines()
init_scaling()
init_second_window(s)
win.bind('<Motion>',register_all)
sw.bind('<Return>',get_and_eval_all)
win.bind('<B1-Motion>',c.change_center)
win.bind('<ButtonRelease-1>',c.end_change)


while True:
    root.update()
    
