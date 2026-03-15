import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("article", class_="product_pod")

    print("Products and Prices:\n")

    for product in products:
        title = product.h3.a["title"]
        price = product.find("p", class_="price_color").text

        print(f"Product: {title}")
        print(f"Price: {price}")
        print("-" * 40)

else:
    print("Failed to fetch webpage")