import requests
import bs4

result = requests.get("https://cellphones.com.vn/mobile/apple.html")
# print(result.status_code)
if result.status_code == 200:
    # print(result.text)
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    # print(soup)
    all_div = soup.find_all("div")
    print(all_div) 