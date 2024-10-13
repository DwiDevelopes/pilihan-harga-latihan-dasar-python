print ("-------------------------------------------------------------------")
print ("Pilihlah Menu Yang Kami Sediakan Kepada Anda : ")
print ("1. Nasi Uduk")
print ("2. Mie Ayam")
print ("3. Soto Ayam")
print ("4. Sate Ayam")
print ("5. Ketoprak")
print ("-------------------------------------------------------------------")
masukan = int (input ("masukan pilihan anda dari 1 , 2 , 3 , 4 , dan 5 : "))

nilai = 0
if masukan == 1 :
    print ("anda memilih nasi uduk")
    rasa = (input ("Apakah rasanya enak ?  "))
    bintang = int (input ("berilah bintang kepada layanan kami 1 - 5 : " ))
    komen = input ("berilah alasan anda mengapa memilih nasi uduk : ")
    nilai = 12000
    berikan = (input ("berikan masukan anda terhadap kami : "))
    
if masukan == 2 :
    print ("anda memilih mie ayam")
    nilai = 14000
    rasa = (input ("Apakah rasanya enak ?  "))
    bintang = int (input ("berilah bintang kepada layanan kami 1 - 5 : " ))
    komen = input ("berilah alasan anda mengapa memilih Mie Ayam : ")
    berikan = (input ("berikan masukan anda terhadap kami : "))
    
if masukan == 3 :
    print ("anda memilih soto ayam")
    nilai = 16000
    rasa = (input ("Apakah rasanya enak ?  "))
    bintang = int (input ("berilah bintang kepada layanan kami 1 - 5 : " ))
    komen = input ("berilah alasan anda mengapa memilih Soto Ayam : ")
    berikan = (input ("berikan masukan anda terhadap kami : "))
    
if masukan == 4 :
    print ("anda memilih sate ayam")
    nilai = 20000
    rasa = (input ("Apakah rasanya enak ?  "))
    bintang = int (input ("berilah bintang kepada layanan kami 1 - 5 : " ))
    komen = input ("berilah alasan anda mengapa memilih Sate Ayam : ")
    berikan = (input ("berikan masukan anda terhadap kami : "))
    
if masukan == 5 :
    print ("anda memilih Ketoprak")
    nilai = 15000
    rasa = (input ("Apakah rasanya enak ?  "))
    bintang = int (input ("berilah bintang kepada layanan kami 1 - 5 : " ))
    komen = input ("berilah alasan anda mengapa memilih Ketoprak : ")
    berikan = (input ("berikan masukan anda terhadap kami : "))

else :
    print ("pilihlah yang benar di menu") 
    

      
print ("--------------------------------------------------")
print ("pilihan yang anda pilih adalah : ", nilai)
print ("Rasa yang ia Rasakan : ", rasa)
print ("Penilayan Kamu Adalah Terhadap Layanan Kami Adalah : ", bintang , "✨")
print ("Alasan Kamu Mengapa Memilih itu : ", komen)
print ("Masukan Yang Anda Berikan Terhadap Kami : ", berikan)
print ("--------------------------------------------------")