import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()


base_url = "https://forum.donanimarsivi.com/uyeler/?key="

infos = ("staff_members","todays_birthdays","most_solutions","ozzmodz_badges_most_badges","most_messages")

try:
    print("**********************************")
    secim = int(input("""|\t1: Yöneticiler           |
|       2: Bugün Doğanlar        |
|       3: En İyi Cevaplar       |
|       4: En Fazla Rozet        |
|       5: En Gevezeler          |      
|      99: Cikis                 |
Seçiminiz (1, 2, 3, 4 veya 5): """))
    print("**********************************")

    if secim == 1:
        r = requests.get(base_url+infos[0], verify=False)
        r.raise_for_status()

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")

            yoneticiler = soup.find_all("div", class_="contentRow-main")
            print("----------- Yoneticiler ----------")
            for content_row in yoneticiler:
                h3_tag = content_row.find("h3", class_="contentRow-header")
                if h3_tag:
                    a_tag = h3_tag.find("a", class_="username")
                    if a_tag:
                        span_tag = a_tag.find("span")
                        if span_tag:
                            print(f"|   {span_tag.text.strip()}")
            print("**********************************")
    elif secim == 2:
        r = requests.get(base_url+infos[1], verify=False)
        r.raise_for_status()

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")

            bugunDoganlar = soup.find_all("div", class_="contentRow-main")

            print("--------- Bugün Doğanlar ---------")
            print("**********************************")
            for contentt in bugunDoganlar:
                h3_tag = contentt.find("h3", class_="contentRow-header")
                if h3_tag:
                    span_tag = h3_tag.find("a", class_="username")
                    if span_tag:
                        print(f"|\t  {span_tag.text.strip()}")
            print("**********************************")
    
    elif secim == 3:
        r = requests.get(base_url+infos[2], verify=False)
        r.raise_for_status()

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")

            eniyicevap = soup.find_all("div", class_="contentRow-main")

            print("---------- En İyi Cevap ----------")
            print("**********************************")
            for like in eniyicevap:
                h3_tag = like.find("h3", class_="contentRow-header")
                sayi_tag = like.find("div", class_="contentRow-extra contentRow-extra--largest")
                if h3_tag and sayi_tag:
                    span_tag = h3_tag.find("a", class_="username")
                    sayi_text = sayi_tag.get_text(strip=True)
                    if span_tag:
                        print(f"|{span_tag.text.strip()} ------ {sayi_text.strip()} en iyi cevap")
            print("**********************************")

    elif secim == 4:
        r = requests.get(base_url+infos[3], verify=False)
        r.raise_for_status()

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")

            rozetler = soup.find_all("div", class_= "contentRow-main")
            print("--------- En Fazla Rozet ---------")
            print("**********************************")
            
            for rozet in rozetler:
                h3_tag = rozet.find("h3", class_= "contentRow-header")
                sayi_tag = rozet.find("div", class_="contentRow-extra contentRow-extra--largest")
                if h3_tag and sayi_tag:
                    span_tag = h3_tag.find("a", class_="username")
                    sayi_text = sayi_tag.get_text(strip=True)
                    if span_tag:
                        print(f"|\t{span_tag.text.strip()} ------ {sayi_text.strip()}")
            print("**********************************")
    
    elif secim == 5:
        r = requests.get(base_url+infos[4], verify=False)
        r.raise_for_status()

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")

            rozetler = soup.find_all("div", class_= "contentRow-main")
            print("--------- En Gevezeler ---------")
            print("**********************************")
            
            for rozet in rozetler:
                h3_tag = rozet.find("h3", class_= "contentRow-header")
                sayi_tag = rozet.find("div", class_="contentRow-extra contentRow-extra--largest")
                if h3_tag and sayi_tag:
                    span_tag = h3_tag.find("a", class_="username")
                    sayi_text = sayi_tag.get_text(strip=True)
                    if span_tag:
                        print(f"|{span_tag.text.strip()} ------ {sayi_text.strip()} mesaj yazdi")
            print("**********************************")
    elif secim == 99:
        print("  Programdan cikiliyor ....")
        print("**********************************")
        sys.exit()
    else:
        print("Gecersiz islem........")
        print("**********************************")
except (requests.RequestException, ValueError, TypeError) as e:
    print("Sadece Belirtilen Numaralar Ile Islem Yapabilirsiniz ....")
