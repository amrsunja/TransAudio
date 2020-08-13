import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import PhotoImage
from make_audio import DetachAudio

bg = '#1A171C'
fg = '#69FF18'

class TransAudio(Tk):

    def creat_win(self, width, height):
        
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        
        x = int(sw/2 - width/2)
        y = int(sh/2 - height/2)

        self.geometry(f'{width}x{height}+{x}+{y}')
        self.resizable(width=False, height=False)
        self.iconbitmap('img/logo.ico')
        self.attributes('-alpha', 0.94)
        self['bg'] = bg
    
    
#---------------------------------------------->  FUNCTION
def open_file():
    try:
        file = filedialog.askopenfilename(initialdir='C:\\', title='Select Video', filetypes=(('mp4 files', '*.mp4'), ('All files', '*.*')))
        
        entry.delete(first=0, last=END)
        entry.insert(END, file)
    except Exception:
        messagebox.showwarning(title='Choose corect file!', message='[+] Choose a video file (.mp4 - .mov)...')

def detach_audio():
    try:
        file = entry.get()     
                
        if os.path.exists('audio/'):
            audio = DetachAudio(file)
            messagebox.showinfo(title='All is complete', message='[ ! ] Audio has been separated from video')
            os.startfile('audio')

        else:
            os.mkdir('audio/')
            audio = DetachAudio(file)
            messagebox.showinfo(title='All is complete', message='[ ! ] Audio has been separated from video')
            os.startfile('audio')
    except Exception:
        messagebox.showerror(title='ERROR: 00x0090', message='[+] Choose a video file\n[+] Or video have not audio\n[+] Try again')


def help_window():
    #os.startfile('INSTRUCTION.txt')
    help_win = TransAudio()
    help_win.creat_win(350, 500)

    title = Label(help_win, text='INSTRUCTION', font='Prounx 15', fg=fg, bg=bg, ).pack(padx=10, pady=5)

    title = Label(help_win, text='''
    TransAudio - программа, которая
    отделяет звук от видео''', font='Tahoma 10', fg='white', bg=bg, ).pack(padx=10, pady=5)

    title = Label(help_win, text='__________________________________', font='Tahoma 10', fg='white', bg=bg, ).pack(padx=10, pady=6)
    

    title = Label(help_win, text='[1] Установите шрифты', font='Tahoma 10', fg='white', bg=bg, ).pack(padx=10, pady=10)
    title = Label(help_win, text='[2] Выберите видео файл', font='Tahoma 10', fg='white', bg=bg, ).pack(padx=10, pady=5)
    title = Label(help_win, text='[3] Нажмите на кнопку с драконом', font='Tahoma 10', fg='white', bg=bg, ).pack(padx=10, pady=5)
    title = Label(help_win, text='[?] Ваше аудио хранится в папке audio', font='Tahoma 10', fg='white', bg=bg, ).pack(padx=10, pady=5)


    
#---------------------------------------------->  
root = TransAudio()
root.creat_win(400, 450)

#---------------------------------------------->  TITLE
title = Label(root, text='ⓉransⒶudio', font='Prounx 15', bg=bg, fg=fg).pack(padx=10, pady=10)
title_line = Label(root, text='_________________________________', font='Prounx 8', bg=bg, fg=fg).pack(padx=10)


#---------------------------------------------->  Select File
entry = Entry(root, font='Tahoma 11', width=30, bg='#343A31', fg=fg, border=0)
entry.place(x=34, y=150)

image = PhotoImage(file='img/file2.png')
select = Button(root, image=image, bd=0, bg=bg, activebackground=bg, command=open_file)
select.place(x=340, y=146)


#---------------------------------------------->  Detach Audio
drago = PhotoImage(file='img/drago2.png')
detach = Button(root, image=drago, bg=bg, bd=0, activebackground=bg, command=detach_audio)
detach.place(x=125, y=250)

#---------------------------------------------->  Help
help_button = Button(root, text='?', font='Prounx 15', bg=bg, activebackground=bg, bd=0, fg=fg, command=help_window).place(x=350, y=400)




if __name__ == "__main__":
    root.mainloop()