import tkinter
import tkinter.messagebox
import sqlite3
class aplikasi():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('GENERATOR MONEY AND DIAMOND')
        self.window.geometry('450x450')
        self.window.config(bg='skyblue')


        #header_aplikasi
        self.judul_aplikasi = tkinter.Label(self.window,text='WELCOME TO CHEAT GENERATOR',bg='green',fg='white',font='arial',width=500)
        self.judul_aplikasi.pack(side='top')
        for x in range(1,2):
            self.enter = tkinter.Label(self.window,text='',bg='skyblue')
            self.enter.pack()
        #inputan
        self.label12 = tkinter.Label(self.window,text='Masukan Id Game',width=25,bg='skyblue',font='arial')
        self.entry13 = tkinter.Entry(self.window,width=25)
        self.label12.pack()
        self.entry13.pack()

        for x in range(0,1):
            self.spas = tkinter.Label(self.window,text='',bg='skyblue')
            self.spas.pack()

        self.label1 = tkinter.Label(self.window,text='Masukan E-mail',width=25,bg='skyblue',font='arial')
        self.entryl = tkinter.Entry(self.window,width=25,bg='white')
        self.label1.pack()
        self.entryl.pack()
        for ii in range(0,1):
            self.value = tkinter.Label(self.window,text='',bg='skyblue')
            self.value.pack()

        self.label100 = tkinter.Label(self.window,text='Masukan jumlah Diamond',width=25,bg='skyblue',font='arial')
        self.entry150 = tkinter.Entry(self.window,width=25,bg='white')
        self.label100.pack()
        self.entry150.pack()

        for a in range(0,1):
            self.enter1 = tkinter.Label(self.window,text='',bg='skyblue')
            self.enter1.pack()
        #inputan
        self.label2 = tkinter.Label(self.window,text='Masukan Password',width=25,bg='skyblue',font='arial')
        self.entry3 = tkinter.Entry(self.window,width=25,show='*')
        self.label2.pack()
        self.entry3.pack()

        for a in range(0,1):
            self.enter1 = tkinter.Label(self.window,text='',bg='skyblue')
            self.enter1.pack()

        

        #self.tombl
        self.tombol1 = tkinter.Button(self.window,text='Kirim Diamond',width=20,command=self.main)
        self.tombol1.pack()
        
        for xx in range(0,1):
            self.eeee = tkinter.Label(self.window,text='',bg='skyblue')
            self.eeee.pack()

        self.out = tkinter.Button(self.window,text='Exit',width=20,command=self.window.destroy)
        self.out.pack()




        self.judul_bawah = tkinter.Label(self.window,text='@azayakaminami@gmail.com 2020/2021',bg='black',fg='white',font='arial',width=500)
        self.judul_bawah.pack(side='bottom')
        self.window.mainloop()
    def main(self):
        cek_id = int(self.entry13.get())
        cek_em = str(self.entryl.get())
        cek_ps = str(self.entry3.get())
        def inputan_database():
            x = sqlite3.connect('data_id.db')
            v = x.cursor()
            v.execute("INSERT INTO data_member VALUES('%d','%s','%s')"%(cek_id,cek_em,cek_ps))
            x.commit()
        inputan_database()
        tkinter.messagebox.showinfo('NOTIFICATION','SELAMAT ID ANDA TELAH DI KIRIMKAN KE %s'%cek_em)
running = aplikasi()
    