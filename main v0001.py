import requests
import bs4
import json
import tkinter as tk
import os
import multiprocessing as mp

#Config

BaseInfo = []
CurrentDirectory = os.getcwd()

#Gui
winRoot = tk.Tk()
winRoot.resizable(False, False)
winRoot.geometry("600x600")
winRoot.title("WebScrapper - 0.0.1")
winRoot.config(bg="#4D6971")

def exit_script():
    quit()
def accept_script():
    resultLink = LinkArea.get("1.0", 'end-1c')
    resultUserAgent = UserAgentArea.get("1.0", 'end-1c')
    if resultLink != None and resultUserAgent != None:
        InUrl = resultLink
        User = {"User-Agent": resultUserAgent}
        if InUrl not in BaseInfo and User not in BaseInfo:
            BaseInfo.append(InUrl)
            BaseInfo.append(User)
            if len(BaseInfo) > 0:
                try:
                    with open(CurrentDirectory + "/parsingData.txt", "w") as f:
                        HttpReponse = getHttpResponse(BaseInfo[0], BaseInfo[1])
                        if HttpReponse.status_code == 200:
                            pass

                            f.close()
                        else:
                            pass
                except:
                    pass
        else:
            pass
    else:
        LinkArea.delete("1.0", "end")
        UserAgentArea.delete("1.0", "end")
        LinkArea.insert(0, "Bad Http link or you didn`t insert anything")
        UserAgentArea.insert(0, "Bad User Agent or you didn`t insert anything")

LinkArea = tk.Text(winRoot, bg="black", fg="white",
                    font=("Bangers", 20, "bold"), height=1, width=20)
UserAgentArea = tk.Text(winRoot, bg="black", fg="white",
                         font=("Bangers", 20, "bold"), height=1, width=20)
AcceptButton = tk.Button(winRoot, bg="#4DAB5E", fg="white",
                         font=("Bangers", 20, "bold"), text="Accept", width=7, command=accept_script)
DB_select = tk.Listbox(winRoot, bg="black", fg="white", font=("Bangers", 20, "bold"), height=3)
Exit_Button = tk.Button(winRoot, bg="#FF442A", fg="black",
                         font=("Bangers", 20, "bold"), text="Exit", width=7, command=exit_script)

DB_select.insert(0, "Text file")
DB_select.insert(1, "Json file")


def getHttpResponse(url, UserAgent=None):
    if UserAgent != None:
        req = requests.get(url, headers=UserAgent)
        return req
    else:
        req = requests.get(url)
        return req
def main(*args, **kwargs):
    LinkArea.place(x=90, y=90)
    UserAgentArea.place(x=90, y=180)
    AcceptButton.place(x=420, y=90)
    Exit_Button.place(x=420, y=180)
    DB_select.place(x=90, y=270)
    winRoot.mainloop()

if __name__ == '__main__':
    main(BaseInfo)