from colorama import Fore
import requests
from bs4 import BeautifulSoup
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear_screen()

def search(query):
    url = f"https://duckduckgo.com/html/?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    search_results = []
    for result in soup.select(".results .result"):
        text = result.select_one(".result__title").text
        url = result.select_one(".result__url")["href"]
        search_results.append({"title": text, "url": url})
    return search_results

while True:
    print(Fore.GREEN)
    print("""
     .|'''.|                                    .   '||''''|                    ||                  
     ||..  '    ....    ....  ... ..    ....  .||.   ||  .    .. ...     ... . ...  .. ...     ....  
      ''|||.  .|...|| .|   ''  ||' '' .|...||  ||    ||''|     ||  ||   || ||   ||   ||  ||  .|...||
    .     '|| ||      ||       ||     ||       ||    ||        ||  ||    |''    ||   ||  ||  ||      
    |'....|'   '|...'  '|...' .||.     '|...'  '|.' .||.....| .||. ||.  '||||. .||. .||. ||.  '|...'
                                                                       .|....'                      

                                        <Anonymous Search Engine created by CCslayer1001>
    """)
    print(Fore.MAGENTA)
    query = input("Aramak istediğiniz şeyi girin (çıkmak için q tuşuna basın): ")
    clear_screen()
    if query == "q":
        break
    results = search(query)


    if results:
        print(f"Toplam {len(results)} sonuç bulundu:\n")
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result['title']}")
            print(f"   {result['url']}\n")
    else:
        print("Arama sonucu bulunamadı.\n")
