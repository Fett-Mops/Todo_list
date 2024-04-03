import customtkinter as ct
import json
from CTkScrollableDropdown import *

root = ct.CTk()
WIDTH, HEIGHT = 600,600
json_loc = 'C:/your/path/to/jason/'

#works But neds finishing touch

l = []
frm = []
grey_fram = ('#DBDBDB','#2B2B2B')
grey=('#CCCCCC','#333333')
r= ct.Variable()
ff = ct.Variable()
file = 'data.json'
grey_disa = '#61676C'
def write_json(path:str, inp:any)->None:
        with open (path, 'w') as f:
            json.dump([dic, inp], f, indent=4)
            
def read_json(path:str)->any:
    global dic
    with open (path) as f:
            fs = json.load(f)
            dic = fs[0]
            r.set(dic)
            return fs[1]
        

def add(text):
    lis[dic].append([text.get(),False])
    write_json(json_loc+file, lis)
    fo(len(lis[dic])-1,lis[dic][-1])
    
def disa(index):
    if l[index].get() == 1:
       
        frm[index].configure(fg_color=grey) 
        lis[dic][index][1] = 1
    else:
        frm[index].configure(fg_color=grey_disa) 
        lis[dic][index][1] = 0
    write_json(json_loc+file, lis)
            
def fo(i,t):
    l.append(ct.Variable())
    frame.grid_columnconfigure(0,weight=1)
    frame.grid_rowconfigure(i,weight=1)
    fr = ct.CTkFrame(frame,fg_color=grey_disa)
    fr.grid(row=i, column=0,sticky='swen',pady=5,padx=5)
    fr.grid_rowconfigure(0,weight=1)
    fr.grid_columnconfigure(0,weight=1)
    frm.append(fr)
    
    check = ct.CTkCheckBox(fr,text=t[0],variable=l[i],command=lambda i=i :(disa(i), l[i]))
    check.grid(row=0,column=0, sticky='nswe',padx=5,pady=5)
    but = ct.CTkButton(fr, text='delete',command=lambda i=i: (dele(i)))
    but.grid(row=0,column=1,pady=5,padx=5)
    if t[1] == True:
        l[i].set(1) 
        fr.configure(fg_color=grey)  
        
def dele(i):
    frm[i].destroy()
    lis[dic].pop(i)
    frame.update()
    write_json(json_loc+file, lis)
    for child in frame.winfo_children():
        child.destroy()
    read_json(json_loc+file)
    for i,t in enumerate(lis[dic]):
        fo(i,t)

def men(d):
    global dic
    if d != 'new':
        dic = d
        
        for child in frame.winfo_children():
            child.destroy()
    
        for i,t in enumerate(lis[dic]):
            fo(i,t)
        write_json(json_loc+file,lis)
    else:
        new()    
def new():
    global dic,lis
    dia = ct.CTkInputDialog(text="List Name:", title="New List")
    d = dia.get_input()
   
    if d ==None:
        return
        
    else:
        dic =d
        print(dic)
        
    r.set(dic)
    lis[dic] = []
    write_json(json_loc+file,lis)
    lis =read_json(json_loc+file)

    s = list(lis.keys())
    
    s.append('new')
    ff.set(s)
    menue.configure(values=ff.get())
    men(dic)
    
def delm():
    global dic, lis
    del lis[dic]
  
    dic = list(lis.keys())[0]
    r.set(dic)
    write_json(json_loc+file,lis)
    lis = read_json(json_loc+file)
    s = list(lis.keys())
    
    s.append('new')
    ff.set(s)
    menue.configure(values=ff.get())
    men(dic)
    
global lis, menue


lis = read_json(json_loc+file)

root.geometry(f'{WIDTH}'+'x'+f'{HEIGHT}')
root.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(2,weight=2)
s = list(lis.keys())
s.append('new')
ff.set(s)

menue = ct.CTkOptionMenu(root,variable= r, command=men, values=ff.get())
menue.grid(row=0, column=0, sticky='nswe',pady=(5,0), padx=5)
dn = ct.CTkEntry(root)
#Delm?
de = ct.CTkButton(root, text='delete', command=delm)
de.grid(row=0,column=1,sticky='nswe',pady=(5,0), padx=(0,10))

inp = ct.CTkFrame(root,height=  100)
inp.grid(row=1, column=0, sticky='nswe',pady=5,padx=5,columnspan=3)
inp.grid_columnconfigure(0,weight=2)
inp.grid_columnconfigure(1, weight=1)
inp.grid_rowconfigure([0,1], weight=1)


ent = ct.CTkEntry(inp, fg_color='#3fadad')
ent.grid(row=0, column=0, sticky='nswe',pady=5, padx=5)
but = ct.CTkButton(inp,text='add',command=(lambda k=ent:(add(k))))
but.grid(row=0, column=1, sticky='nswe',pady=5, padx=(0,5))

frame= ct.CTkScrollableFrame(root,width=500,height=500)
frame.grid(row=2, column=0,sticky='nswe',pady=(0,5), padx=5,columnspan=3)

for i,t in enumerate(lis[dic]):
    fo(i,t)
root.mainloop()
