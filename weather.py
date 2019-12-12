from tkinter import *
import os
import time
import feedparser


window = Tk()
window.resizable(False,False)
window.title("Hava Durumu")
window.config(bg = "#161E26")
window.geometry("250x300")


# KITA|ULKE|POSTAKODU|IL 
#

def hava():
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode="+ kita_input.get() + '|'+ ulke_input.get() + '|' + posta_input.get() + '|' + sehir_input.get())
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    print (parse[2], parse[4], parse[5])
    veri["text"] = (parse[2], parse[4], parse[5])
    return (hava)
    
    



welcome_label = Label(text = "Hava Durumu",bg = "#cc181e",fg = "#fff",width = 35)
welcome_label.pack()
#welcome_label.place(width = 200)

# Kıta 
kita_label = Label(text = "Kıta",bg = "#488bff",fg = "#fff")
kita_label.pack()
kita_label.place(x = 10,y = 30,width = 100,height = 20)

kita_input = Entry()
kita_input.pack()
kita_input.place(width = 100,x = 130,y = 30)

# Ülke

ulke_label = Label(text = "Ülke (Kısaltılmış)",bg = "#488bff",fg = "#fff")
ulke_label.pack()
ulke_label.place(x = 10,y = 70,width = 150,height = 20)

ulke_input = Entry()
ulke_input.pack()
ulke_input.place(width = 50,x = 175,y = 70)

# Posta Kodu

posta_label = Label(text = "Posta Kodu",bg = "#488bff",fg = "#fff")
posta_label.pack()
posta_label.place(x = 10,y = 110,width = 125,height = 20)

posta_input = Entry()
posta_input.pack()
posta_input.place(x = 145,y = 110,width = 95)

# Şehir

sehir_label = Label(text = "Şehir",bg = "#488bff",fg = "#fff")
sehir_label.pack()
sehir_label.place(x = 10,y = 150,width = 90,height = 20)

sehir_input = Entry()
sehir_input.pack()
sehir_input.place(x = 110,y = 150,width = 125)

# Buton

get_button = Button(text = "Hava Durumu",command = hava,bg = "#823783",fg = "#fff")
get_button.pack()
get_button.place(x = 25,y = 200,width = 200,height = 20)

# Veri 

veri = Label(text = "",bg = "#373F83",fg = "#fff")
veri.pack()
veri.place(y = 225,x = 20,width = 210,height = 50)

mainloop()


