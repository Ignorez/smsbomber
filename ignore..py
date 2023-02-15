from colorama import Fore, Style
from sms import SendSms
from time import sleep
from os import system
from requests import get

r = get("https://raw.githubusercontent.com/tingirifistik/Enough/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
    
while 1:
    system("cls||clear")
    print("""{}
    
  _____ _____ _   _  ____  _____  ______ 
 |_   _/ ____| \ | |/ __ \|  __ \|  ____|
   | || |  __|  \| | |  | | |__) | |__   
   | || | |_ | . ` | |  | |  _  /|  __|  
  _| || |__| | |\  | |__| | | \ \| |____ 
 |_____\_____|_| \_|\____/|_|  \_\______|
                                         
                                            
                          {}Discord: ign#0001  
    """.format(Fore.RED, Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = int(input(Fore.RED + "1. SMS Gönder\n2. Çıkış\n\n" + Fore.RED + "Seçim: "))
    except ValueError:
        system("cls||clear")
        print(Fore.RED + "Hatalı giriş yaptınız. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.RED + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.RED, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç adet SMS göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        sms = SendSms(str(tel_no))
        while sms.adet < kere:
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if sms.adet == kere:
                            break
                        exec("sms."+attribute+"()")
                        sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
