from automation import *
import openpyxl as excel
from tkinter import filedialog
from tkinter import *
import os
#read Excel file 
def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    for cell in range(len(firstCol)):
        contact = firstCol[cell].value 
        if type(contact) == int :
            lst.append(contact) 
        else : 
            

       # contact = str(firstCol[cell].value)
            contact = f"\"{contact}\""
            # contact = "\"" + contact + "\""
            lst.append(contact)
    return lst


def loadfile():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("excel files","*.xlsx"),("all files","*.*")))
    print (filename)
    global targets
    targets = readContacts(filename)
    print(targets)
    Lb.delete(0,END)
    [Lb.insert(END, item) for item in targets]

def getimg():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("image files","*.jpg"),("all files","*.*")))
    global imagepath
    imagepath=filename.replace("/", "\\")
    filesize = (os.path.getsize(imagepath) / 1024 ) / 1024 
    print ( filesize )
    if( filesize > 64 ) :
        print("video is greater than 64, please select again ")
        var1.set(0)
    print (imagepath)

def getdoc():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("docx files","*.docx"),("all files","*.*")))
    global documentpath
    documentpath=filename.replace("/", "\\")
    filesize = (os.path.getsize(document) / 1024 ) / 1024 
    print ( filesize )
    if( filesize > 100 ) :
        print("file is greater than 100, please select again ")
        var2.set(0)
    
    print(documentpath)


def callback():
    message = T.get(1.0, "end-1c")
    print(message)
    toSendImage = var1.get()
    if(toSendImage == 0 ):
        global imagepath
        imagepath = None
    caption = Timg.get(1.0, "end-1c")
    toSendDocument = var2.get()
    if(toSendDocument == 0 ):
        global documentpath
        documentpath = None
    #targets = [918898280634]
    SendMessage(message , targets , toSendImage , caption , toSendDocument , imagepath  , documentpath  )


root = Tk()
root.geometry('600x500')

b = Button(root, text="Load",width= 25,command = loadfile)
b.grid(row=0,column=4,padx=150,pady=20)

Lb = Listbox(root)  
Lb.grid(row=1,column=4) 
l = Label(root, text='type your text message') 
l.grid(row=2,column=3)

T = Text(root, height=2, width=30)
T.grid(row=2,column=4,padx=50,pady=20)

var1 = IntVar() 
Checkbutton(root, text='send image',variable=var1,command=getimg).grid(row=3, column=4) 
l1=Label(root,text='Select any image')
l1.grid(row=4,column=3,padx=50,pady=20)
Timg = Text(root, height=2, width=30)
Timg.grid(row=4,column=4,padx=50,pady=20)

var2 = IntVar() 
Checkbutton(root, text='send document',variable=var2,command=getdoc).grid(row=5,column=4) 
b = Button(root, text="send",width= 25, command=callback)
b.grid(row=6, column=4)

root.mainloop()
