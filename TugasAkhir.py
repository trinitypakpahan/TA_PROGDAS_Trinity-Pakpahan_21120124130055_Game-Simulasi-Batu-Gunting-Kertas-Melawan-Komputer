import tkinter as tk
import random as random
from PIL import Image , ImageTk
from tkinter import messagebox
from tkinter import PhotoImage

pilihan = ["Batu", "Gunting", "Kertas"]
font_style= ("Times New Roman", 18)
bg_color= 'white'
pilihan_komputer = random.choice(pilihan)
menang = 0
skor = []

class MainApp:
    def __init__(self, apk):
        apk.title("Tugas Akhir")
        image = Image.open("pattern.jpeg")
        image = image.resize((500,500))
        self.photo = ImageTk.PhotoImage(image), 
        label_image = tk.Label(apk, image = self.photo)
        label_image.place(x=0, y=0)
        label_image.lower()
        menang = 0
        label1 = tk.Label(apk, text="Simulasi Batu Gunting Kertas",font=("Times New Roman",17),bg=bg_color)
        label1.place(x=70, y=10)
        label2 = tk.Label(apk, text= "Tekan tombol atas pilihan Anda" , font=font_style, bg=bg_color)
        label2.place(x=55, y=40)
        Batu = tk.Button(apk, text="Batu", command=self.pilih_batu)
        Batu.place(x=30, y= 80, width=100, height=100)
        Gunting = tk.Button(apk, text="Gunting", command=self.pilih_gunting)
        Gunting.place(x=165, y=80, width=100, height=100)
        Kertas = tk.Button(apk, text="Kertas", command=self.pilih_kertas)
        Kertas.place(x= 300, y=80, width=100, height=100)
        Simpanskor = tk.Button(apk, text="Simpan Skor Akhir", command=self.simpan_skor)
        Simpanskor.place(x= 300, y=200)
        Cekskor = tk.Button(apk, text="Cek Skor", command=self.cek_skor)
        Cekskor.place(x= 300, y=230)


    def pilih_batu(self):
        global pilihan_user
        pilihan_komputer = random.choice(pilihan)
        pilihan_user = "Batu"
        global labelpilihankomp
        global labelpilihankompakhir
        global labelbatukalah
        global labelbatumenang
        global labelbatuseri
        global menang
        labelpilihankomp = tk.Label(apk, text= "Pilihan Komputer :",font=font_style, bg=bg_color)
        labelpilihankomp.place(x=55, y=190)
        labelpilihankompakhir = tk.Label (apk, text=pilihan_komputer ,font=font_style, bg=bg_color)
        labelpilihankompakhir.place(x=55, y=220)
        match pilihan_komputer:
            case "Batu":
                labelbatuseri = tk.Label(apk, text= "Seri!",font=font_style, bg=bg_color)
                labelbatuseri.place(x=55, y=250)
            case "Gunting":
                labelbatumenang=tk.Label(apk, text= "Kamu Menang!",font=font_style, bg=bg_color)
                labelbatumenang.place(x=55, y=250)
                menang += 1
            case "Kertas":
                labelbatukalah = tk.Label(apk, text= "Kamu Kalah!",font=font_style, bg=bg_color)
                labelbatukalah.place(x=55, y=250)
                menang = 0
                    
    def pilih_gunting(self):
        global pilihan_user
        pilihan_komputer = random.choice(pilihan)
        pilihan_user = "Gunting"
        global menang
        global labelpilihankomp
        global labelpilihankompakhir
        global labelguntingkalah
        global labelguntingmenang
        global labelguntingseri
        labelpilihankomp = tk.Label(apk, text= "Pilihan Komputer :",font=font_style, bg=bg_color)
        labelpilihankomp.place(x=55, y=190)
        labelpilihankompakhir = tk.Label (apk, text=pilihan_komputer ,font=font_style, bg=bg_color)
        labelpilihankompakhir.place(x=55, y=220)
        match pilihan_komputer:
            case "Batu":
                labelguntingkalah = tk.Label(apk, text= "Kamu Kalah!",font=font_style, bg=bg_color)
                labelguntingkalah.place(x=55, y=250)
                menang = 0
            case "Gunting":
                labelguntingseri = tk.Label(apk, text= "Seri!",font=font_style, bg=bg_color)
                labelguntingseri.place(x=55, y=250)
            case "Kertas":
                labelguntingmenang = tk.Label(apk, text= "Kamu Menang!",font=font_style, bg=bg_color)
                labelguntingmenang.place(x=55, y=250)
                menang += 1

    def pilih_kertas(self):
        global pilihan_user
        pilihan_komputer = random.choice(pilihan)
        pilihan_user = "Kertas"
        global menang
        global labelpilihankomp
        global labelpilihankompakhir
        global labelkertaskalah
        global labelkertasmenang
        global labelkertasseri
        labelpilihankomp = tk.Label(apk, text= "Pilihan Komputer :",font=font_style, bg=bg_color)
        labelpilihankomp.place(x=55, y=190)
        labelpilihankompakhir = tk.Label (apk, text=pilihan_komputer ,font=font_style, bg=bg_color)
        labelpilihankompakhir.place(x=55, y=220)
        
        match pilihan_komputer:
            case "Batu":
                labelkertasmenang = tk.Label(apk, text= "Kamu Menang!",font=font_style, bg=bg_color)
                labelkertasmenang.place(x=55, y=250)
                menang += 1
            case "Gunting":
                labelkertaskalah = tk.Label(apk, text= "Kamu Kalah!",font=font_style, bg=bg_color)
                labelkertaskalah.place(x=55, y=250)
                menang = 0
            case "Kertas":
                labelkertasseri = tk.Label(apk, text= "Seri!",font=font_style, bg=bg_color)
                labelkertasseri.place(x=55, y=250)

    def simpan_skor(self):
        skor.append(menang)

    def cek_skor(self):
        global menang
        if menang < 0:
            messagebox.showinfo("Skor Anda", "Maaf, skor Anda belum ada.")
        else:
            messagebox.showinfo("Skor Anda", skor)
        menang = 0

if __name__ in "__main__":
    apk = tk.Tk()
    app = MainApp(apk)
    apk.geometry("450x400") 
    apk.resizable(False, False)
    apk.mainloop()

