#------------------------
# imported modules
#------------------------
import pyshorteners
import pyperclip
from tkinter import * 
#------------------------
# main
#------------------------
myApp = Tk()
myApp.geometry('500x400')
myApp.title('URL Shortener')
myApp.configure(bg='light blue')
myApp.resizable(False, False)
url = StringVar()
url_address = StringVar()
#------------------------
# functions
#------------------------
def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

def clear():
    url.set("")
    url_address.set("")
#------------------------
# GUI
#------------------------
Label(myApp, text = 'URL Shortener', font = 'poppins 20 bold',background='light blue',fg='black',justify='center').pack(pady=20)
Entry(myApp, textvariable = url,justify='center',width=50).pack()
Button(myApp,text='Generate URL',command=urlshortener,fg='Red',justify='center').pack(pady=10)

Label(myApp, text= 'Shortened URL', font = 'poppins 15 bold',background='light blue',fg='black',justify='center').pack(pady=10)
Entry(myApp, textvariable = url_address,justify='center',width=30).pack()
Button(myApp,text='Copy URL',command=copyurl,fg='Red',justify='center').pack(pady=10)
Button(myApp,text='CLEAR',command=clear,fg='Red',justify='center').pack(pady=10)


myApp.mainloop()
