# do all the imports
import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime


def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_detail_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)

    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div",class_="col-xs-8 site-stats-count").find("ul").find_all("li")
    for item in info_div:
        print(item)
        print()



     #count= item.find("strong", class_="mob-hide").is_digit()
    # text= item.find("strong", class_="mob-hide").get_text()
     #print (text,": ",count)






get_corona_detail_of_india()

