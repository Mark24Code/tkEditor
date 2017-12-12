import os
from tkinter import Tk, Menu, Frame, Button, Scrollbar, Label, Text, messagebox,filedialog, LEFT, RIGHT, X, Y, W, BOTH, BOTTOM, \
    YES, NO, SUNKEN,END

filename = ""

def authorDef():
    messagebox.showinfo('作者信息', 'Mark24Code')


def aboutDef():
    messagebox.showinfo('版本信息', 'MIT LICENSE  Copyrighht. @2017 All rights reserved.')

def openFileDef():
    filename = filedialog.askopenfilename(defaultextension='*')
    if filename == '':
        filename = None
    else:
        root.title(string=filename)
        textarea.delete(1.0,END)
        f = open(filename,'r')
        textarea.insert(1.0,f.read())
        f.close()

def newFileDef():
    global filename
    root.title(string="未命名文件")
    filename = None
    textarea.delete(1.0,END)

def saveAsDef():
    global filename
    filename = filedialog.asksaveasfilename(initialfile='未命名.txt',defaultextension="*")
    fh = open(filename,'w')
    fcontent = textarea.get(1.0,END)
    fh.write(fcontent)
    fh.close()
    root.title(string=filename)

def saveDef():
    global filename
    try:
        f = open(filename,'w')
        fcontent = textarea.get(1.0,END)
        f.write(fcontent)
        f.close()
    except:
        saveAsDef()


def cutDef():
    textarea.event_generate('<<Cut>>')

def copyDef():
    textarea.event_generate('<<Copy>>')

def pasteDef():
    textarea.event_generate('<<Paste>>')

def redoDef():
    textarea.event_generate('<<Redo>>')

def undoDef():
    textarea.event_generate('<<Undo>>')

root = Tk()
root.title(string='tkEditor')
root.geometry('500x500+100+100')

# menu
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label="新建", accelerator="Ctrl+N",command=newFileDef)
filemenu.add_command(label="打开", accelerator="Ctrl+O",command=openFileDef)
filemenu.add_command(label="保存", accelerator="Ctrl+S",command=saveDef)
filemenu.add_command(label="另存为", accelerator="Ctrl+Shift+S",command=saveAsDef)
menubar.add_cascade(label="文件", menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label="撤销", accelerator="Ctrl+Z",command=undoDef)
editmenu.add_command(label="重做", accelerator="Ctrl+Y",command=redoDef)
editmenu.add_separator()
editmenu.add_command(label="剪切", accelerator="Ctrl+X",command=cutDef)
editmenu.add_command(label="复制", accelerator="Ctrl+C",command=copyDef)
editmenu.add_command(label="粘贴", accelerator="Ctrl+V",command=pasteDef)
editmenu.add_separator()
editmenu.add_command(label="查找", accelerator="Ctrl+F")
editmenu.add_command(label="替换", accelerator="Ctrl+R")
editmenu.add_command(label="全选", accelerator="Ctrl+A")
menubar.add_cascade(label="编辑", menu=editmenu)

aboutmenu = Menu(menubar)
aboutmenu.add_command(label="作者", command=authorDef)
aboutmenu.add_command(label="版权", command=aboutDef)
menubar.add_cascade(label="关于", menu=aboutmenu)

# toolbar
toolbar = Frame(root, height=25, bg='#24292E')

openButton = Button(toolbar, text="打开",command=openFileDef)
openButton.pack(side=LEFT, padx=5, pady=5)
saveButton = Button(toolbar, text="保存",command=saveDef)
saveButton.pack(side=LEFT)

toolbar.pack(expand=NO, fill=X)

# statusbar
statusbar = Label(root, text="Ln0", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

# textarea & scroll

lnlabel = Label(root, width=2, bg="#6A737D", fg="#FFFFFF")
lnlabel.pack(side=LEFT, fill=Y)

textarea = Text(root, undo=True)
textarea.pack(fill=BOTH, expand=YES)

scroll = Scrollbar(textarea)
textarea.config(yscrollcommand=scroll.set)
scroll.config(command=textarea.yview)
scroll.pack(side=RIGHT, fill=Y)


# main app

root.mainloop()
