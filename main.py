from bs4 import BeautifulSoup
import requests
import time
from plyer import notification


def check_price():
    global price

    # Link of amazon product:
    link = "https://www.amazon.com/ZOTAC-Graphics-IceStorm-Advanced-ZT-A30900J-10P/dp/B08ZL6XD9H/ref=sr_1_13?crid=37BV786QAD508&keywords=graphics+cards&qid=1666665739&qu=eyJxc2MiOiI3LjYwIiwicXNhIjoiNi45OCIsInFzcCI6IjYuMjQifQ%3D%3D&sprefix=%2Caps%2C64&sr=8-13&ufe=app_do%3Aamzn1.fos.2b70bf2b-6730-4ccf-ab97-eb60747b8daf"

    # Input your user-agent (unique to everyone)
    headers = {
        "User-Agent": "INPUT USER-AGENT HERE",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    attempts = 0
    while attempts < 3:
        try:
            webpage_response = requests.get(link, headers=headers)
            break
        except Exception as e:
            attempts += 1
            print("Error getting request, ensure internet connection is available and site is not down.")
            print(e)
            print("Attempting to reconnect after 15 seconds...")
            time.sleep(15)

    if attempts == 3:
        print("Unable to reconnect, please try again.")
        quit()

    soup = BeautifulSoup(webpage_response.content, "html.parser")
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")

    try:
        price = soup2.find_all("span", class_="a-offscreen")[0]
    except IndexError as e:
        print("Price not found.")
        print(e)
        exit()

    price = price.get_text()
    price = price.strip().strip("$").replace(",", "")

    date = str(time.ctime(time.time()))
    print(f"Price on {date} is: ${price}.")


def windows_notification():
    notification.notify(
        title="Price has dropped!",
        message="The price of the selected Amazon product has dropped by below your selected threshold!",
        timeout=60,
    )


while True:
    check_price()
    # Change price threshold if needed:
    if price < "1000":
        windows_notification()
    time.sleep(43200)
