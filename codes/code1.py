
pinkod = int(input("Pinkodni kiriting:"))
if pinkod == 5773:
    balance = 2500_000
    print("""
          1. Naqt pul yechish
          2. Naqt pul kirim qilish
          3. Balansni tekshirish
          4. Pin kodni o'zgartirish
          5. Sms xabarnoma
          6. Mobil aloqaga to'lov
          7. Komunal to'lovlar
          8. Davlat xizmatlari
          9. Chiqish
          """)
    n = int(input("Tanlang: "))
    match n:
        case 1:
            print("""
                  1. 50.000
                  2. 100.000
                  3. 150.000
                  4. 200.000
                  5. 500.000
                  6. Qo'lda kiritish
                  """)
            m = int(input("Tanlang: "))
            match m:
                case 1:
                    if m <= balance:
                        balance -= 50_000
                        print("Pul yechildi")
                case 2:
                    if m <= balance:
                        balance -= 100_000
                        print("Pul yechildi")
                case 3:
                    if m <= balance:
                        balance -= 150_000
                        print("Pul yechildi")
                case 4:
                    if m <= balance:
                        balance -= 200_000
                        print("Pul yechildi")   
                case 5:
                    if m <= balance:
                        balance -= 500_000
                        print("Pul yechildi")
                case 6:
                    pulni_kiritish = int(input("Kiriting:"))
                    if pulni_kiritish <= balance:
                        balance -= pulni_kiritish
                        print("Pul yechildi") 
                    else:
                        print("Mablag' yetarli emas!") 
        case 2:
           
            print("""
                  1. 50.000
                  2. 100.000
                  3. 150.000
                  4. 200.000
                  5. 500.000
                  6. Qo'lda kiritish
                  """)
            m = int(input("Tanlang: "))
            match m:
                case 1:
                        balance += 50_000
                        print(f"Balansingizga 50 000 so'm qo'shildi")
                case 2:
                    balance += 100_000
                    print(f"Balansingizga 100 000 so'm qo'shildi")
                case 3:
                    balance += 150_000
                    print(f"Balansingizga 150 000 so'm qo'shildi")   
                case 4:
                    balance += 200_000
                    print(f"Balansingizga 200 000 so'm qo'shildi")
                case 5:
                    balance += 500_000
                    print(f"Balansingizga 500 000 so'm qo'shildi") 
                case 6:
                        pulni_kiritish = int(input("Kiriting:"))
                        balance += pulni_kiritish
                        print(f"Balansingizga {pulni_kiritish} so'm qoshildi") 
        case 3:
            print(f"Balansingizda {balance} so'm pul bor")
        case 4:
            eski_pin = int(input("Eski pinkodni kiriting:"))
            if eski_pin == pinkod:
                yangi_pin = int(input("Yangi pinkodni kiriting \n kamida 4 raqam bo'lsin:"))
                tasdiqlash = int(input("Yangi pinkodni qayta kiriting:"))
                if yangi_pin == tasdiqlash and (4 <= yangi_pin <= 8):
                    pinkod == yangi_pin
                    print("Pinkod o'zgartirildi")
                elif yangi_pin < 4:
                    print("Pinkod kamida 4 raqamli bo'lishi kerak!")
                elif yangi_pin > 8:
                    print("Pinkod ko'pi bilan 8 raqamli bo'lishi kerak!")
                else:
                    print("Yangi pinkod mos kelmadi")
            else:
                print("Eski pinkod noto'g'ri")
        case 5:
            tel_number = input("Yangi telefon raqamni kiriting: ")
            if len(tel_number) == 12 and tel_number.isdigit() and tel_number.startswith("998"):
                print("SMS xizmati muvaffaqiyatli ulandi!!!") 
            else:
                print("To'g'ri telefon raqamini kiriting!!! ") 
        case 6:
            print("""
                  1. UZMOBILE
                  2. Ucell
                  3. Beeline
                  4. mobiuz
                  5. HUMANS
                  6. OQ
                  """)
            mobil_operatorlar = int(input(">>>"))
            match mobil_operatorlar:
                case 1:
                    tel_raqam = input("Telefon raqmni kiriting:")
                    if len(tel_raqam) == 12 and tel_raqam.isdigit() and (tel_raqam.startswith("99899") or tel_raqam.startswith("99895") or tel_raqam.startswith("99877")):
                        tolov_sum = int(input("To'lov summasini kiriting:"))
                        if balance >= tolov_sum:
                            balance -= tolov_sum
                            print(f"{tolov_sum} so'mlik to'lov amalga oshirildi")
                            print(f"Balansingizda:{balance} so'm qoldi")
                        else:
                            print("Balansingizda mablag' yetarli emas!")
                    else:
                        print("Telefon raqam noto'g'ri kiritildi!")
                case 2:
                    tel_raqam = input("Telefon raqmni kiriting:")
                    if len(tel_raqam) == 12 and tel_raqam.isdigit() and (tel_raqam.startswith("99893") or tel_raqam.startswith("99894")):
                        tolov_sum = int(input("To'lov summasini kiriting:"))
                        if balance >= tolov_sum:
                            balance -= tolov_sum
                            print(f"{tolov_sum} so'mlik to'lov amalga oshirildi")
                            print(f"Balansingizda:{balance} so'm qoldi")
                        else:
                            print("Balansingizda mablag' yetarli emas!")
                    else:
                        print("Telefon raqam noto'g'ri kiritildi!")
                case 3:
                    tel_raqam = input("Telefon raqmni kiriting:")
                    if len(tel_raqam) == 12 and tel_raqam.isdigit() and (tel_raqam.startswith("99890") or tel_raqam.startswith("99891")):
                        tolov_sum = int(input("To'lov summasini kiriting:"))
                        if balance >= tolov_sum:
                            balance -= tolov_sum
                            print(f"{tolov_sum} so'mlik to'lov amalga oshirildi")
                            print(f"Balansingizda:{balance} so'm qoldi")
                        else:
                            print("Balansingizda mablag' yetarli emas!")
                    else:
                        print("Telefon raqam noto'g'ri kiritildi!")    
                case 4:
                    tel_raqam = input("Telefon raqmni kiriting:")
                    if len(tel_raqam) == 12 and tel_raqam.isdigit() and tel_raqam.startswith("99897"):
                        tolov_sum = int(input("To'lov summasini kiriting:"))
                        if balance >= tolov_sum:
                            balance -= tolov_sum
                            print(f"{tolov_sum} so'mlik to'lov amalga oshirildi")
                            print(f"Balansingizda:{balance} so'm qoldi")
                        else:
                            print("Balansingizda mablag' yetarli emas!") 
                    else:
                        print("Telefon raqam noto'g'ri kiritildi!")       
                case 5:
                    tel_raqam = input("Telefon raqmni kiriting:")
                    if len(tel_raqam) == 12 and tel_raqam.isdigit() and tel_raqam.startswith("99833"):
                        tolov_sum = int(input("To'lov summasini kiriting:"))
                        if balance >= tolov_sum:
                            balance -= tolov_sum
                            print(f"{tolov_sum} so'mlik to'lov amalga oshirildi")
                            print(f"Balansingizda:{balance} so'm qoldi")
                        else:
                            print("Balansingizda mablag' yetarli emas!")
                    else:
                        print("Telefon raqam noto'g'ri kiritildi!")
                case 6:
                    tel_raqam = input("Telefon raqmni kiriting:")
                    if len(tel_raqam) == 12 and tel_raqam.isdigit() and tel_raqam.startswith("99820"):
                        tolov_sum = int(input("To'lov summasini kiriting:"))
                        if balance >= tolov_sum:
                            balance -= tolov_sum
                            print(f"{tolov_sum} so'mlik to'lov amalga oshirildi")
                            print(f"Balansingizda:{balance} so'm qoldi")
                        else:
                            print("Balansingizda mablag' yetarli emas!") 
                    else:
                        print("Telefon raqam noto'g'ri kiritildi!")   
        case 7:
            print("""
                  1. Elektr energiyasi
                  2. Gaz
                  3. Suv
                  4. Isitish tizimi
                  5. Uy-joy xizmati
                  """)
            tanlov = int(input("Kamunal to'lov turini tanlang:"))
            match tanlov:
                case 1:
                    tolov_sum = int(input("To'lov summasini kiriting:"))
                    if balance >= tolov_sum:
                        balance -= tolov_sum
                        print(f"{tolov_sum} so'mlik Elektr energiyasi uchun to'lov amalga oshirildi")
                        print(f"Balansingizda:{balance} so'm qoldi")
                    else:
                        print("Balansingizda mablag' yetarli emas!")
                case 2:
                    tolov_sum = int(input("To'lov summasini kiriting:"))
                    if balance >= tolov_sum:
                        balance -= tolov_sum
                        print(f"{tolov_sum} so'mlik Gaz uchun to'lov amalga oshirildi")
                        print(f"Balansingizda:{balance} so'm qoldi")
                    else:
                        print("Balansingizda mablag' yetarli emas!")
                case 3:
                    tolov_sum = int(input("To'lov summasini kiriting:"))
                    if balance >= tolov_sum:
                        balance -= tolov_sum
                        print(f"{tolov_sum} so'mlik Suv uchun to'lov amalga oshirildi")
                        print(f"Balansingizda:{balance} so'm qoldi")
                    else:
                        print("Balansingizda mablag' yetarli emas!")                            
                case 4:
                    tolov_sum = int(input("To'lov summasini kiriting:"))
                    if balance >= tolov_sum:
                        balance -= tolov_sum
                        print(f"{tolov_sum} so'mlik Isitish tizimi uchun to'lov amalga oshirildi")
                        print(f"Balansingizda:{balance} so'm qoldi")
                    else:
                        print("Balansingizda mablag' yetarli emas!")  
                case 5:
                    tolov_sum = int(input("To'lov summasini kiriting:"))
                    if balance >= tolov_sum:
                        balance -= tolov_sum
                        print(f"{tolov_sum} so'mlik Uy-joy xizmati uchun to'lov amalga oshirildi")
                        print(f"Balansingizda:{balance} so'm qoldi")
                    else:
                        print("Balansingizda mablag' yetarli emas!") 
        case 8:
            print("""
                  1. Jarimalar (YHXBB)
                  2. Soliqlar
                  3. Id karta boji
                  4. Haydovchilik guvohnomasi boji
                  """)
            tolov_turi = int(input("Davlat xizmatlari uchun to'lov turini tanlang:"))
            match tolov_turi:
                case 1:
                    id_karta = input("Mashina nomeri yoki JSHIR ni kiriting. Masalan (A672BA yoki 1234567890456): ")
                    if (len(id_karta) == 6 or len(id_karta) == 14) and id_karta.isalnum():
                        print("""
                            1. Tezlikni oshirganlik uchun 330.000 so'm jarima
                            2. Svetaforda qoyda buzganingiz uchun 500.000 so'm jarima
                            3. To'xtash qoidalarini buzganingiz uchun 220.000 so'm jarima
                            4. Sug'urta yo'qligi uchun 1.000.000 so'm jarima 
                            5. Hech qanday jarima yo'q 
                              """)
                        jarima = int(input("Sizda qaysi biri bo'yicha jarima bor? "))
                        match jarima:
                            case 1:
                                if balance >= 330_000:
                                    balance -= 330000
                                    print(f"To'lov amalga oshirildi \n Hisobingizda {balance} so'm pul qoldi")
                                else:
                                    print("Hisobingizda mablag' yetarli emas!")
                            case 2:
                                if balance >= 500_000:
                                    balance -= 500000
                                    print(f"To'lov amalga oshirildi \n Hisobingizda {balance} so'm pul qoldi")
                                else:
                                    print("Hisobingizda mablag' yetarli emas!")
                            case 3:
                                if balance >= 220_000:
                                    balance -= 220000
                                    print(f"To'lov amalga oshirildi \n Hisobingizda {balance} so'm pul qoldi")
                                else:
                                    print("Hisobingizda mablag' yetarli emas!")
                            case 4:
                                if balance >= 1000_000:
                                    balance -= 1000_000
                                    print(f"To'lov amalga oshirildi \n Hisobingizda {balance} so'm pul qoldi")
                                else:
                                    print("Hisobingizda mablag' yetarli emas!")
                            case 5:
                                print("Sizda hech qanday jarima turi aniqlanmadi")     
                case 2:
                    soliq_id = input("Pasport seriyasi yoki JSHIR ni kiriting. Masalan (AD6758846 yoki 56748935467324): ")  
                    if (len(soliq_id) == 9 or len(soliq_id) == 14)  and soliq_id.isalnum():
                        print("""
                              1. Transport solig'i - 300.000 so'm
                              2. Yer solig'i - 250.000 so'm
                              3. Mol-mulk solig'i - 400.000 so'm
                              4. Hech qanday soliq qarzi yo'q
                              """)
                        soliq_tolov = int(input("Sizda qaysi biri bo'yicha soliq qarzi mavjud? "))
                        match soliq_tolov:
                            case 1:
                                if balance >= 300_000:
                                    balance -= 300_000
                                    print(f"Transport solig'i bo'yicha to'lov amalga oshirildi \n Hisobingizda {balance} so'm pul qoldi")
                                else:print("Hisobingizda mablag' yetarli emas")  
                            case 2:
                                if balance >= 250_000:
                                    balance -= 250_000
                                    print(f"Yer solig'i bo'yicha to'lov amalga oshirildi \n Hisobingizda {balance} so'm pul qoldi")
                                else:print("Hisobingizda mablag' yetarli emas") 
                            case 3:
                                if balance >= 400_000:
                                    balance -= 400_000
                                    print(f"Mol-mulk solig'i bo'yicha to'lov amalga oshirildi \n Hisobingizda {balance} so'm pul qoldi")
                                else:print("Hisobingizda mablag' yetarli emas") 
                            case 4:print("Sizda hech qanday soliq qarzi mavjud emas") 
                case 3:
                    id_boji = input("Pasport seriyasi yoki JSHIR ni kiriting. Masalan (AD6744893 yoki 67589463765432): ")
                    if (len(id_boji) == 9 or len(id_boji) == 14) and id_boji.isalnum():  
                        print("""
                              1. Yangi ID karta olish: 150.000 so'm
                              2. Id kartani yuqotib qayta tiklash: 250.000 so'm
                              3. ID kartani mudatidan oldin almashtirish: 200.000 so'm
                              4. Hech qanday boj yo'q
                              """)
                        id_tolov = int(input("Qaysi biri bo'yicha to'lov qilmoqchisiz:"))
                        match id_tolov:
                            case 1:
                                if balance >= 150000:
                                    balance -= 150000
                                    print(f"To'lov amalga oshirildi \n Balansingizda {balance} so'm pul qoldi")
                                else:print("Hisobingizda mablag' yetarli emas!")
                                    
                            case 2:
                                if balance >= 250000:
                                    balance -= 250000
                                    print(f"To'lov amalga oshirildi \n Balansingizda {balance} so'm pul qoldi")
                                else:print("Hisobingizda mablag' yetarli emas!")        
                            case 3:
                                if balance >= 200000:
                                    balance -= 200000
                                    print(f"To'lov amalga oshirildi \n Balansingizda {balance} so'm pul qoldi")
                                else:print("Hisobingizda mablag' yetarli emas!") 
                                
                            case 4:print("Sizda ID karta boji yo'q")
                case 4:
                        prava = input("Pasport seriyasi yoki JSHIR kiriting. Masalan (AD2434676 yoki 35476543521238): ")
                        if (len(prava) == 9 or len(prava) == 14) and prava.isalnum():
                            print("""
                            1. Birinchi marta olish - 400.000 so'm
                            2. Yangilash (muddat tugagani uchun) - 300.000 so'm
                            3. Yo'qotilganini qayta tiklash - 500.000 so'm
                            4. Hech qanday boji yo'q
                            """)
                            prava_tolov = int(input("Qaysi bo'yicha to'lov qilmoqchisiz? "))
                            match prava_tolov:
                                case 1:
                                     if balance >= 400_000:
                                        balance -= 400_000
                                        print(f"Birinchi marta olish bo'yicha to'lov amalga oshirildi.\nHisobingizda {balance} so'm qoldi")
                                     else: print("Hisobingizda mablag' yetarli emas")
                                case 2:
                                    if balance >= 300_000:
                                      balance -= 300_000
                                      print(f"Yangilash bo'yicha to'lov amalga oshirildi.\nHisobingizda {balance} so'm qoldi")
                                    else: print("Hisobingizda mablag' yetarli emas")
                                case 3:
                                    if balance >= 500_000:
                                      balance -= 500_000
                                      print(f"Yo'qotilganini qayta tiklash bo'yicha to'lov amalga oshirildi.\nHisobingizda {balance} so'm qoldi")
                                    else: print("Hisobingizda mablag' yetarli emas")
                                case 4:
                                     print("Sizda haydovchilik guvohnomasi boji mavjud emas.")
        case 9:
            print("Xizmat ko'rsatish tugatildi!")
    print("Xizmatimizdan foydalanganingiz uchun rahmat")
                                            
else: 
    print("Pinkod xato!")
