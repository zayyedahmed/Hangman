# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:11:31 2020

@author: Akhmed
"""

import random
hurufyangharusnyadicoba=[]
hurufyangudahdicoba=[]
again=True
while True:
    if again:
        #BUAT NENTUIN KATA YANG HARUS DITEBAK
        pertanyaan = random.choice(["Nama Binatang", "Nama Bunga", "Nama Negara Asia"])
        print("Pertanyaan Adalah: " + pertanyaan)
        if pertanyaan == "Nama Binatang" :
            jawaban = random.choice(["Kuda", "Kucing", "Ular", "Ayam"]).lower()
        elif pertanyaan == "Nama Bunga":
            jawaban = random.choice(["Mawar", "Melati", "Rafflesia", "Anggrek"]).lower()
        else: 
            jawaban = random.choice(["Irak", "Indonesia", "Malaysia", "India"]).lower()
        soalnya=list(jawaban)
        kesempatan=len(jawaban)+5 #jumlah gambar hangman      
        kesalahan = 5      

        for i in jawaban:
            hurufyangharusnyadicoba.append(' _ ')
        print("Kata yang Harus ditebak : "+''.join(hurufyangharusnyadicoba))
        print("Nyawa Anda: ", kesalahan)
        print("Kesempatan Untuk Menebak ", kesempatan, "Kali")
        #BUAT MAENNYA
        while True:
            huruf=input("Tebak hurufnya : ")
            if huruf in hurufyangudahdicoba:
                print("Masukan Huruf Lain ")
            elif len(huruf)>1:
                print("Invalid Input")
            else:
                kesempatan-=1
                hurufyangudahdicoba.append(huruf)
                
                if huruf in soalnya: #hurufnya bener
                    print("Betul")
                    print("Nyawa Anda: ", kesalahan)
                    if kesempatan > 0:
                        print("Kesempatan Anda: ", kesempatan)
                    for j in range(len(soalnya)):
                        if huruf == soalnya[j]:
                            tempathuruf=j
                            hurufyangharusnyadicoba[tempathuruf]=huruf
                    print("kata yang harus ditebak : "+''.join(hurufyangharusnyadicoba))
                else: #hurufnya salah
                    kesalahan -=1
                    print("Nyawa Anda Tinggal", kesalahan)
                    if kesalahan == 4:
                        print ("_________")
                        print ("|    |")
                        print ("|")
                        print ("|")
                        print ("|")
                        print ("|")
                        print ("|________")
                        print ("COBA LAGI, JANGAN MENYERAH!!!!")
                    elif kesalahan == 3:
                        print ("_________")
                        print ("|    |")
                        print ("|    O")
                        print ("|")
                        print ("|")
                        print ("|")
                        print ("|________")
                        print ("COBA LAGI, JANGAN MENYERAH!!!!")
                    elif kesalahan == 2:
                        print ("_________")
                        print ("|    |")
                        print ("|    O")
                        print ("|    |")
                        print ("|    |")
                        print ("|")
                        print ("|________")
                        print ("COBA LAGI, JANGAN MENYERAH!!!!")
                    elif kesalahan == 1:
                        print ("_________")
                        print ("|    |")
                        print ("|    O")
                        print ("|   \|/")
                        print ("|    |")
                        print ("|")
                        print ("|________")
                        print ("COBA LAGI, JANGAN MENYERAH!!!!")
                    else:
                        print ("_________")
                        print ("|    |")
                        print ("|    O")
                        print ("|   \|/")
                        print ("|    |")
                        print ("|   / \ ")
                        print ("|________")
                    if kesempatan > 0:
                        print("sisa kesempatan : ",kesempatan)
                    print("kata yang harus ditebak : "+''.join(hurufyangharusnyadicoba))
            #KONDISI MENANG KALAH
            jawabannya=''.join(hurufyangharusnyadicoba)
            if jawabannya==jawaban:
                print("Jawaban Benar!!!!!")
                break
            elif kesalahan==0:
                print("Sayang Sekali, Nyawa Anda Habis")
                print("Jawabanya Adalah ",jawaban)
                break
        mainlagi=input("Ingin Main Lagi? (y: lanjut, Any Key: exit) : ").lower()
        if mainlagi=='y':
            hurufyangharusnyadicoba=[]
            hurufyangudahdicoba=[]
            again=True
        else:
            print("Terima Kasih Telah Bermain!!!!")
            break
    else:
        break
