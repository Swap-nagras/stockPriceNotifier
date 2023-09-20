from dotenv import load_dotenv
import os
import yagmail
import requests
from bs4 import BeautifulSoup

# Load environment variables from .env
load_dotenv()
def clean_text(text):
    changeWithPercent = text.split(" ")[1]
    output = float(changeWithPercent.strip("(%)"))
    return output
def get_subject():
    subject="Hi! The stocks have moved more than slightly today"
    return subject
def get_contents(stock_name, change):
    contents=f'Hey!\nThis email is automatically sent by the stock price notifier.\n {stock_name} has some movement today: {change}.'
    return contents
def send_email(sender, password, receiver, subject, contents):
    yag = yagmail.SMTP(user=sender, password=password)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("The email has been sent.")
def get_change_sunpharma():
    url="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/sunpharmaceuticalindustries/SPI"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("div", class_="pricupdn nsechange grn")
    if(rate is None):
        rate = soup.find("div", class_="pricupdn nsechange red")
    return rate.text
def get_change_vedanta():
    url="https://www.moneycontrol.com/india/stockpricequote/miningminerals/vedanta/SG"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("div", class_="pricupdn nsechange grn")
    if (rate is None):
        rate = soup.find("div", class_="pricupdn nsechange red")
    return rate.text
def get_change_auropharma():
    url="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/aurobindopharma/AP"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("div", class_="pricupdn nsechange grn")
    if (rate is None):
        rate = soup.find("div", class_="pricupdn nsechange red")
    return rate.text
def get_change_itc():
    url="https://www.moneycontrol.com/india/stockpricequote/diversified/itc/ITC"
    content = requests.get(url).text
    soup= BeautifulSoup(content, 'html.parser')
    rate = soup.find("div", class_="pricupdn nsechange grn")
    if (rate is None):
        rate = soup.find("div", class_="pricupdn nsechange red")
    return rate.text
def get_change_airtel():
    url="https://www.moneycontrol.com/india/stockpricequote/telecommunications-service/bhartiairtel/BA08"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("div", class_="pricupdn nsechange grn")
    if (rate is None):
        rate = soup.find("div", class_="pricupdn nsechange red")
    return rate.text
change_sunpharma = clean_text(get_change_sunpharma())
change_vedanta = clean_text(get_change_vedanta())
change_auropharma = clean_text(get_change_auropharma())
change_itc = clean_text(get_change_itc())
change_airtel = clean_text(get_change_airtel())

if(change_sunpharma>1 or change_sunpharma<1):
    sender = os.getenv("SENDER")
    receiver = os.getenv("RECEIVER_1")
    password = os.getenv("PASSWORD")
    subject = get_subject()
    contents = get_contents("Sun Pharmaceutical Industries", change_sunpharma)
    send_email(sender, password, receiver, subject, contents)

if(change_vedanta>1 or change_vedanta<1):
    sender = os.getenv("SENDER")
    receiver = os.getenv("RECEIVER_1")
    password = os.getenv("PASSWORD")
    subject = get_subject()
    contents = get_contents("Vedanta Ltd.", change_vedanta)
    send_email(sender, password, receiver, subject, contents)

if(change_auropharma>1 or change_auropharma<1):
    sender = os.getenv("SENDER")
    receiver = os.getenv("RECEIVER_1")
    password = os.getenv("PASSWORD")
    subject = get_subject()
    contents = get_contents("Aurobindo Pharma Ltd.", change_auropharma)
    send_email(sender, password, receiver, subject, contents)

if(change_itc>1 or change_itc<1):
    sender = os.getenv("SENDER")
    receiver = os.getenv("RECEIVER_1")
    password = os.getenv("PASSWORD")
    subject = get_subject()
    contents = get_contents("ITC Ltd.", change_itc)
    send_email(sender, password, receiver, subject, contents)

if(change_airtel>1 or change_airtel<1):
    sender = os.getenv("SENDER")
    receiver = os.getenv("RECEIVER_1")
    password = os.getenv("PASSWORD")
    subject = get_subject()
    contents = get_contents("Bharti Airtel Ltd.", change_airtel)
    send_email(sender, password, receiver, subject, contents)
