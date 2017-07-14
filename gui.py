try:
    import archook #The module which locates arcgis
    archook.get_arcpy()
    import arcpy
    print ('success')
except ImportError:
    print ('error')
    
import Tkinter as tk
from Tkinter import *
import ttk,Tkconstants,tkFileDialog
import csv

#variable

ams = []
estate = []
cr_c=[]
root = tk.Tk()

root.resizable(width=False,height=False)

root.title("TPK Generator")

root.rowconfigure(1,pad=20)
root.columnconfigure(1,pad=30)

#data pt

with open('list.csv', 'rb') as f:
    reader = csv.reader(f)
    ams = list(reader)

cr_c=[]
for k in ams:
    cr_c.append(k[1])
cr_c=sorted(set(cr_c))

for row in ams:
    estate.append(dict({'Estate':row[0], 'PT':row[1], 'EstateName':row[2],'Status':'waiting'}))


vals=('A','B','C')
valss=('A','D','C')

def okclick():
    if county.get() in cr_c:
        showall(county.get())
        btngen['state'] = 'normal'
    else:
        btngen['state'] = 'disabled'

def generateTPK():
    filename = tkFileDialog.askdirectory(initialdir="/", title='DIAL')
    print filename

def showall(estq):
    tree.delete(*tree.get_children())
    for c in estate:
        if c['PT']==estq:
            valuelist = str(c['PT'][:-1]), c['Estate'], str(c["EstateName"]),c["Status"]
            tree.insert('', 'end', text='.......', values=(valuelist))

leftframe = ttk.Frame(width=200, height=227, pad=20, relief=tk.SOLID)
rightframe = ttk.Frame(width=370, height=300)

tree = ttk.Treeview(rightframe, columns=('PT','Estate', 'EstateName', 'Status'))

tree['show'] = 'headings'
tree.heading('PT', text='PT')
tree.column('PT', width=80, anchor=W)

tree.heading('Estate', text='Estate')
tree.column('Estate', width=70, anchor=W)

tree.heading('EstateName', text='Estate Name')
tree.column('EstateName', width=190, anchor=W)

tree.heading('Status', text='Status')
tree.column('Status', width=100, anchor=CENTER)


treeScroll = ttk.Scrollbar(rightframe)
treeScroll.configure(command=tree.yview)
tree.configure(yscrollcommand=treeScroll.set)



tree.pack(side=LEFT)
treeScroll.pack(side=LEFT,fill=Y)

labelN= ttk.Label(leftframe,text="Pilih Nama PT :")
labelN.pack(anchor=W,pady=5)

countvar= StringVar()

countvar.set(cr_c[0])
county= ttk.Combobox(leftframe,values=cr_c,textvariable=countvar,state='readonly')
county.pack(anchor=W)

btnsel=tk.Button(leftframe,text="OK",command=okclick,width=5)
btnsel.pack(anchor=W,pady=10,padx=(0,8),side=LEFT)

btngen=tk.Button(leftframe,text="Generate TPK",command=generateTPK,width=11,state=DISABLED)
btngen.pack(anchor=(W),pady=10,side=RIGHT)




leftframe.grid(row=1,column=1)
rightframe.grid(row=1,column=2)


root.mainloop()
