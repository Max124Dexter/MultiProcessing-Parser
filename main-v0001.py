import requests
import bs4
import smtplib
import os
import time
import logging
from multiprocessing import Process, Pool, Lock

#Config
""" Config data will be inputed from simple GUI which is wrotten on TKinter modul
    As it is prototype and pre-alpha URL and User-Agent are taken from my computer as an exsample 
"""
Domen_KeyWord = "https://www.binance.com"
RootURL = "https://www.binance.com/ru"
UserAgent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                           " AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/91.0.4472.124 Safari/537.36"}
AllLinksOnSite = []
SubLinks = []


OutputData = {}
ChoosedProtocol = "" # It can be one of : .txt, .json, .csv, .xml or you can send it on your Email
Logging = True # By default it always True but you can change param and it won`t be logged



def getHttpResponses(url, UserAgent=None):
    """ Send base Http request on choosed you url, requires 1 param
        Second param is User Agent it is optional but  I recomend you insert it too 'cause most of sites
        block IPs without User Agent
    """
    if UserAgent !=None:
        request = requests.get(url, headers=UserAgent)
        return request
    else:
        request = requests.get(url)
        return request

def getAllstatusCodes(url, UserAgent):
    if Domen_KeyWord in url:
        HttpResponse = getHttpResponses(url, UserAgent)
        if HttpResponse.status_code == 200:
            logging.info(f"{time.ctime()} Successful connecting to : {url}")
        #    AllSublinks = getSubLinks(HttpResponse.content)
         #   for el in AllSublinks:
          #      SubLinks.append(el)
        else:
            logging.error(f"{time.ctime()} Error connecting to: {url} \n HttpStatus code is : {HttpResponse.status_code}")
    # else:
       # HttpResponse = getHttpResponses(Domen_KeyWord + url, UserAgent)
        #if HttpResponse.status_code == 200:
         #   logging.info(f"{time.ctime()} Successful connecting to : {url}")
          #  AllSublinks = getSubLinks(HttpResponse.content)
           # for el in AllSublinks:
            #    SubLinks.append(el)
      #  else:
       #     logging.error(
        #        f"{time.ctime()} Error connecting to: {url} \n HttpStatus code is : {HttpResponse.status_code}")


def getBaseLinks(html_page):
    """ This function is needed just to take all links from base ROOT url and then """
    soup = bs4.BeautifulSoup(html_page, "html.parser")
    for i in soup.findAll("body"):
        for el in i.find_all('a', href=True):
            AllLinksOnSite.append(el['href'])
        return AllLinksOnSite


def getSubLinks(html_page):
    """Here we are taking all sub links in based links (Copypasted from function getBaseLinks()"""
    soup = bs4.BeautifulSoup(html_page, "html.parser")
    for i in soup.findAll("body"):
        for el in i.find_all('a', href=True):
            SubLinks.append(el['href'])
        return SubLinks


def getNeededContent(html_page):
    pass

def convertData_in_txt(data):
    pass

def convertData_in_json(data):
    pass

def convertData_in_csv(data):
    pass

def convertData_in_xml(data):
    pass

def sendDataBySMTP(data):
    pass


def main(*args, **kwargs):
    BaseHttpResponse = getHttpResponses(RootURL, UserAgent) # Send base request on needed us site
    if BaseHttpResponse.status_code == 200: # If HTTP response is OK begin scrapping all links from base page
        logging.info(f"{time.ctime()} Successful connecting to : {RootURL} \n"
                     f"Http Status code is: {BaseHttpResponse.status_code}") # log if everything is ok

        StartScrappingLinksFromBase = time.time() # Start counting how much time will take parsing all links


        AllLinksOnSite = getBaseLinks(BaseHttpResponse.content) # Getting all links from base root url

        EndScrappingLinksFromBase = time.time()# End counting how much time will take parsing all links

        TotalScrappingLinksFromBaseTime = EndScrappingLinksFromBase - StartScrappingLinksFromBase # Sum how much time it took
        if AllLinksOnSite.__sizeof__() > 0:
            logging.info(f"{time.ctime()} Successful scrapping all links from ROOT url: {RootURL} \n "
                         f"Total time of scrapping links from base links is : {TotalScrappingLinksFromBaseTime}") #log

            StartScrappingAllSubLinks = time.time()

           #Multiprocessing code

         #   Processes = []
          #  for link in AllLinksOnSite :
           #     Proc = Process(target=getAllstatusCodes, name=f"Process:{os.getpid()} ", args=(link, UserAgent))
            #    Processes.append(Proc)
             #   Proc.start()

           #  for proc in Processes:
            #     proc.join()

            FinishingScrappingAllSubLinks = time.time()
            TotalTimeOfScrappingSubLinks = FinishingScrappingAllSubLinks - StartScrappingAllSubLinks

            if SubLinks.__sizeof__() > 0:
                logging.info(f"{time.ctime()} Succesful scrapping all sublinks")
                logging.info(f"{time.ctime()} Total time of scrapping all sublinks: {TotalTimeOfScrappingSubLinks}")


            else:
                logging.info(f"{time.ctime()} Error scrapping all sublinksS")

        else:
            logging.error(f"{time.ctime()} Error with scrapping all links from ROOT url: {RootURL} \n")
    else:
        logging.error(f"{time.ctime()}  Problem with connection to: {RootURL} \n "
                      f"Http Status code is: {BaseHttpResponse.status_code}")

if __name__ == '__main__':
    logging.basicConfig(filename='parserLogs.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s <| ',
                        level=logging.INFO)
    StartingProgram= time.time()
    main(RootURL, UserAgent, AllLinksOnSite)
    FinishingProgram = time.time()
    TotalTimeTaking = FinishingProgram - StartingProgram
    logging.info(f"{time.ctime()} All parsing time took : {TotalTimeTaking} seconds")
    quit()