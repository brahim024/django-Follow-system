from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup as soup
from selenium import webdriver


    #Create your models here.

class LaunchEvent:
    def __init__(self):
            #use selenium to open a browser
        driver = webdriver.Chrome(executable_path=r'C:\Users\acer\Downloads\chromedriver_win32\chromedriver.exe')
        my_url = 'https://www.nasa.gov/launchschedule'
    
            #selenium browser waits 10 seconds allowing JS content to load then grabs page contents
        driver.implicitly_wait(10) # seconds
        driver.get(my_url)

            #selenium driver creates page_html which can be turned to soup
        page_html = driver.page_source
        driver.quit()

            #html parsing
        page_soup = soup(page_html, "html.parser")

            #grabs each launch 
        containers = page_soup.find_all("div", class_="launch-info")
        title_list = []# list to iterate in below for loop.
        date_list = []
        info_list = []

        for i in range(0, 3):
            title_list.append(containers[i].find(class_="title").get_text())
            date_list.append(containers[i].find(class_="date").get_text())
            info_list.append(containers[i].find(class_="description").get_text())

            #group iterations through zip function
        all_list = zip(title_list, date_list, info_list)
        self.all_list = all_list