import tkinter as tk



form=tk.Tk()

form.title('Zozamad Chat V1')
form.geometry('400x100')
form.resizable(False,False)

yazi=tk.Label(form,text='Buraya Istediginiz Entry I Yazabilirsiniz',fg='blue',bg='black',font='serif 15')
yazi.pack()
# Bu Kisim Ise Verileri Printe Donusturuyor

def receive():
    entry=ent1.get()
    print(entry)


# Asagi Kisimda Veriler Verilip ent1 Adli Stringden Aliniyor

ent1=tk.Entry(width=30,fg='red',bg='black',font='serif 15',)
ent1.pack()

tus=tk.Button(form,text='Enter',bg='black',fg='yellow',font='serif 10', command=receive)
tus.pack()

telif=tk.Label(form,text='© Butun Telif Haklari Zozamad Group a Saklidir ©',font='serif 8')
telif.pack()
form.mainloop()
# Made By RootManX#7356
