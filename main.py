from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

startURL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/albrino/WebScrape/chromedriver")
browser.get(startURL)

time.sleep(10)

def scrape():
    headers = ["Name", "Light-Years", "Mass", "Magnitude", "Discovery"]
    planetData = []
    
    for i in range(0, 489):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul in soup.find_all("ul", attrs={"class", "exoplanet"}):
            liTags = ul.find_all("li")
            tempList = []
            for index, liTag in enumerate(liTags):
                if index == 0:
                    tempList.append(liTag.find_all("a")[0].contents[0])
                else:
                    try:
                        tempList.append(liTag.contents[0])
                    except:
                        tempList.append("")
            planetData.append(tempList)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper2.csv", "w") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planetData)
        
scrape()