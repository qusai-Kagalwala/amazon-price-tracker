# 🛒 Amazon Price Tracker (Python)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)
![PRs](https://img.shields.io/badge/PRs-Welcome-orange)
![Made By](https://img.shields.io/badge/Made%20By-Qusai%20Kagalwala-blueviolet)

Track Amazon product prices in real-time and get notified instantly via email when the price drops below your desired threshold.

---

## 📌 Overview

This project is a Python-based automation tool that scrapes product data from Amazon and monitors price changes. When the product price falls below a specified target, the system sends an automated email alert.

---

## ⚡ Features

* 🔍 Real-time Amazon price scraping
* 💰 Accurate price extraction with currency handling
* 📧 Email notifications using SMTP
* 🛡️ CAPTCHA detection to prevent false scraping
* 🔐 Secure credential management using `.env`
* ⚙️ Clean and modular code structure

---

## 🧠 How It Works

1. Sends an HTTP request to the Amazon product page
2. Parses HTML using BeautifulSoup
3. Extracts product title and price
4. Compares with target price
5. Sends email alert if condition is met

---

## 🧰 Tech Stack

* Python
* BeautifulSoup
* Requests
* SMTP (smtplib)
* python-dotenv

---

## 📂 Project Structure

```
amazon-price-tracker/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repository

```
git clone https://github.com/qusai-Kagalwala/amazon-price-tracker.git
cd amazon-price-tracker
```

---

### 2️⃣ Install Dependencies

```
pip install requests beautifulsoup4 python-dotenv
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file:

```
SMTP_ADDRESS=smtp.gmail.com
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

> ⚠️ Use **App Password**, not your actual Gmail password.

---

### 4️⃣ Update Script

```
PRODUCT_URL = "your-amazon-product-url"
TARGET_PRICE = 2000.0
```

---

### 5️⃣ Run the Script

```
python main.py
```

---

## 📸 Sample Output

```
Product: Concept Kart Headphones with Mic
Current Price: ₹2199.0
Price is still above target.
```

OR

```
Price dropped! Sending email...
```

---

## 🔒 Security Notes

* Never commit `.env` file
* Use `.gitignore` to protect sensitive data
* Avoid exposing email credentials

---

## ⚠️ Disclaimer

* Amazon may block scraping via CAPTCHA
* HTML structure may change over time
* This project is for educational purposes only

---

## 🚀 Future Enhancements

* ⏱️ Scheduled tracking (cron jobs)
* 📊 Price history tracking (database)
* 🤖 Telegram / WhatsApp alerts
* 🌐 Web dashboard (Flask / MERN)
* 📦 Multi-product tracking support

---

## 👨‍💻 Author

**Qusai Kagalwala**

* GitHub: https://github.com/qusai-Kagalwala
* LinkedIn: https://www.linkedin.com/in/qusai-kagalwala/

---

## ⭐ Show Support

If you found this project useful, consider giving it a ⭐ on GitHub!
