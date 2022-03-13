import random,time
print("ON NUMARA TAHMİN PROGRAMINA HOŞGELDİNİZ")
while True:

    count=0
    try:

        demand=int(input('Lütfen tahmin etmemi istediğiniz kolon sayısını giriniz: '))
        while(count<demand):
            list=[57,16,77,6,55,52,2,11,29,73,27,53,75,28,5,60,71,7,15,65,46,4,20,38,69,1,51,35,79,36,25,62,80,37,
                   32,70,48,47,68,44,31,19,74,58,50,8,26,67,78,18,3,45,56,64,23,40,34,24,33,21,22,43,17,13,39,76,42,
                   49,54,14,10,30,59,9,41,12,66,63,61,72]


            guess=random.sample(list,10)

            time.sleep(0.5)
            count+=1
            print('Hesaplanıyor....')
            time.sleep(1)
            print(count, '.kolon: ',*sorted(guess))
        choice = input("Tekrar seçim için herhangi bir tuşa ve ENTER'a basın.Çıkmak için 'q' ya basın: ")
        if(choice=='q' or choice=='Q'):
            print(''' Bizi tercih ettiğiniz için teşekkürler...     
               ****İyi şanslar****
             Built by Sinan YILDIRIM''')
            time.sleep(3)
            break
    except ValueError:
        print("Hatalı seçim! Lütfen sayısal değer giriniz...")