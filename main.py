from bs4 import BeautifulSoup
import requests
import smtplib
import os
import re
from dotenv import load_dotenv

# ====================== LOAD ENV VARIABLES ======================
load_dotenv()

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# ====================== CONFIG ======================
PRODUCT_URL = "https://www.amazon.in/Concept-Kart-Headphones-Mic-Blue/dp/B092MWY7T1?ref_=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_cai_p_0_0&pd_rd_i=B092MWY7T1&pd_rd_w=0sR2H&content-id=amzn1.sym.d1f93add-6486-42ac-94c7-352c77b4cb14&pf_rd_p=d1f93add-6486-42ac-94c7-352c77b4cb14&pf_rd_r=3RJMXEVEHKYXNAVZKEX0&pd_rd_wg=6O5QJ&pd_rd_r=2dbf3f4a-e1db-42d8-8521-e1bd27c0cdab&th=1"
TARGET_PRICE = 2000.0

# ====================== HEADERS ======================
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

# ====================== FETCH PAGE ======================
def fetch_page(url):
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")

# ====================== CHECK BLOCK ======================
def check_block(soup):
    if "captcha" in soup.text.lower():
        raise Exception("Blocked by Amazon (CAPTCHA detected)")

# ====================== GET TITLE ======================
def get_title(soup):
    tag = soup.find(id="productTitle")
    if not tag:
        raise Exception("Product title not found")
    return tag.get_text().strip()

# ====================== GET PRICE ======================
def get_price(soup):
    price_tag = soup.select_one(
        "#priceblock_ourprice, #priceblock_dealprice, .a-price .a-offscreen"
    )

    if not price_tag:
        raise Exception("Price not found")

    price_text = price_tag.get_text().strip()
    print("Raw price:", price_text)

    # Detect currency
    if "₹" in price_text:
        currency = "₹"
    elif "$" in price_text:
        currency = "$"
    else:
        currency = ""

    # Extract numeric value (handles commas)
    numbers = re.findall(r"\d[\d,]*\.?\d*", price_text)
    if not numbers:
        raise Exception("Could not extract numeric price")

    price_value = float(numbers[0].replace(",", ""))

    return price_value, currency

# ====================== SEND EMAIL ======================
def send_email(title, price, currency, url):
    message = f"{title}\nNow at {currency}{price}\n{url}"

    with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8")
        )

# ====================== MAIN ======================
def main():
    try:
        soup = fetch_page(PRODUCT_URL)
        check_block(soup)

        title = get_title(soup)
        price, currency = get_price(soup)

        print(f"\nProduct: {title}")
        print(f"Current Price: {currency}{price}")

        if price < TARGET_PRICE:
            print("Price dropped! Sending email...")
            send_email(title, price, currency, PRODUCT_URL)
        else:
            print("Price is still above target.")

    except Exception as e:
        print("Error:", e)

# ====================== RUN ======================
if __name__ == "__main__":
    main()