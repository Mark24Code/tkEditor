from tkinter import Tk, Menu, Frame, Button, LEFT, X, NO, Label, SUNKEN, W, BOTTOM, Text, YES, BOTH, Scrollbar, RIGHT, Y

root = Tk()
root.title = 'tkEditor'
root.geometry('500x500+100+100')

# menu
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label="新建", accelerator="Ctrl+N")
filemenu.add_command(label="打开", accelerator="Ctrl+O")
filemenu.add_command(label="保存", accelerator="Ctrl+S")
filemenu.add_command(label="另存为", accelerator="Ctrl+Shift+S")
menubar.add_cascade(label="文件", menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label="撤销", accelerator="Ctrl+Z")
editmenu.add_command(label="重做", accelerator="Ctrl+Y")
editmenu.add_separator()
editmenu.add_command(label="剪切", accelerator="Ctrl+X")
editmenu.add_command(label="复制", accelerator="Ctrl+C")
editmenu.add_command(label="粘贴", accelerator="Ctrl+V")
editmenu.add_separator()
editmenu.add_command(label="查找", accelerator="Ctrl+F")
editmenu.add_command(label="替换", accelerator="Ctrl+R")
editmenu.add_command(label="全选", accelerator="Ctrl+A")
menubar.add_cascade(label="编辑", menu=editmenu)

aboutmenu = Menu(menubar)
aboutmenu.add_command(label="作者")
aboutmenu.add_command(label="版权")
menubar.add_cascade(label="关于", menu=aboutmenu)

# toolbar
toolbar = Frame(root, height=25, bg='#24292E')
openButton = Button(toolbar, text="打开")
openButton.pack(side=LEFT, padx=5, pady=5)

saveButton = Button(toolbar, text="保存")
saveButton.pack(side=LEFT)
toolbar.pack(expand=NO, fill=X)

# statusbar
statusbar = Label(root, text="Ln0", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

# textarea

lnlabel = Label(root, width=2, bg="#6A737D", fg="#FFFFFF")
lnlabel.pack(side=LEFT, fill=Y)

textarea = Text(root, undo=True)
textarea.pack(fill=BOTH,expand=YES)

scroll = Scrollbar(textarea)
textarea.config(yscrollcommand=scroll.set)
scroll.config(command=textarea.yview)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
