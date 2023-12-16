import webview
import requests
from bs4 import BeautifulSoup

def scrape_flipkart_product(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract MRP
    mrp_element = soup.find('div', {'class': '_30jeq3 _1_WHN1'})
    if mrp_element:
        mrp = mrp_element.text.replace('₹', '').replace(',', '').strip()
    else:
        mrp = None

    # Extract Offer Details
    offer_element = soup.find('div', {'class': '_2ZdXDB'})
    if offer_element:
        offer = offer_element.text.strip()
    else:
        offer = None

    return mrp, offer

def open_flipkart_webview():
    product_url = 'https://www.flipkart.com/example-product-url'

    mrp, offer = scrape_flipkart_product(product_url)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flipkart MRP and Offer Checker</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>Flipkart MRP and Offer Checker</h1>
        <h2>Product URL: {product_url}</h2>
        <h3>MRP: ₹{mrp}</h3>
        <h3>Offer: {offer}</h3>
    </body>
    </html>
    """
    webview.create_window("Flipkart MRP and Offer Checker", html=html_content, width=800, height=600)
    webview.start()
open_flipkart_webview()