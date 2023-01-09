import subprocess
import tkinter as tk
import webbrowser
import threading
import time
import requests
from zipfile import ZipFile
import os
import sys
import shutil
import json
import webview

def weboie():
    webbrowser.open('https://login.live.com/oauth20_authorize.srf?client_id=8b479237-cf82-4ff0-8648-cc7de41cfe1b&response_type=code&scope=XboxLive.signin%20offline_access&redirect_uri=http%3A%2F%2Flocalhost%3A62396%2Fms-oauth%2Fresponse')

def loginBtn():
    try:
        os.remove("data.json")
    except:
        pass
    t42 = threading.Thread(target=weboie)
    os.system("java -jar Authenticator.jar")
    #webview.create_window('OrangeClient Sign in', 'https://login.live.com/oauth20_authorize.srf?client_id=8b479237-cf82-4ff0-8648-cc7de41cfe1b&response_type=code&scope=XboxLive.signin%20offline_access&redirect_uri=http%3A%2F%2Flocalhost%3A62396%2Fms-oauth%2Fresponse')
    
    #webview.start()
    

def getAuth():
    req = requests.get("https://orangeclient.neoeducation.tk/authenticator", stream=True,verify=False)
    with open("Authenticator.jar","wb") as f:
        for chunk in req.iter_content(chunk_size=128):
            f.write(chunk)

t439 = threading.Thread(target=getAuth,daemon=True)
t439.start()

if not os.path.exists("goodimg.png"):
    req = requests.get("https://orangeclient.neoeducation.tk/img", stream=True, verify=False)
    with open("goodimg.png","wb") as f:
        for chunk in req.iter_content(chunk_size=128):
            f.write(chunk)

win = tk.Tk()
win.config(width=160,height=90)
win.title("OrangeClient Launcher")
photo = tk.PhotoImage(file="./goodimg.png")
win.iconphoto(False, photo)
win.geometry("640x360")


upfrm = tk.Frame(win)
ctrfrm = tk.Frame(win)
dwnfrm = tk.Frame(win)
ctrdwnfrm = tk.Frame(ctrfrm)


stlbl = tk.Label(dwnfrm, text=" ", font=("Arial", 10))
mcDirLbl = tk.Label(ctrfrm, text="Enter MC Directory (optional)")
mcDirectory = tk.Text(ctrfrm,height = 2, width = 20)
mcDirLbl.pack(side=tk.TOP)
mcDirectory.pack(side=tk.TOP)



RamLbl = tk.Label(ctrdwnfrm, text="Enter RAM (Megabytes)(not optional)")
RamIn = tk.Text(ctrdwnfrm,height = 2, width = 20)
RamIn.pack(side=tk.BOTTOM)
RamLbl.pack(side=tk.BOTTOM)

def upzipstuff():
    stlbl.config(text="Getting ready for unzipping...")
    try:
        shutil.rmtree("natives")
    except:
        pass
    try:
        shutil.rmtree("libraries")
    except:
        pass
    os.mkdir("natives")
    os.mkdir("libraries")
    stlbl.config(text="Unzipping natives...")
    with ZipFile("natives.zip", 'r') as zObject:
        zObject.extractall(path="natives/")
    stlbl.config(text="Unzipping libraries...")
    with ZipFile("libraries.zip", 'r') as zObject:
        zObject.extractall(path="libraries/")
    stlbl.config(text="Launching...")
    with open("data.json","r") as f:
        data = json.load(f)
        os.system("java -"+ "Xms512M "+ "-Xmx" + RamIn.get(1.0, "end-1c") + "M "+ "-Djava.library.path=\".\\natives\" "+ "-cp \".\\libraries\\*;.\\OrangeClient.jar\" "+ "net.minecraft.client.main.Main "+ "--width 854 "+ "--height 480 "+ "--username 0rangy "+ "--version 1.8.8 "+ "--gameDir \"" + mcDirectory.get(1.0, "end-1c") + "\" "+ "--assetsDir \"" + mcDirectory.get(1.0, "end-1c") + "\\assets" + "\" "+ "--assetIndex 1.8.8 "+ "--uuid da96d7c6-bcf2-4ef9-8156-d2917a48ebd2 "+ "--accessToken " + data["token"])
    


def downloadClientJar():
    stlbl.config(text="Downloading client jar...")
    req = requests.get("https://orangeclient.neoeducation.tk/clientjar", stream=True, verify=False)
    with open("OrangeClient.jar","wb") as f:
        for chunk in req.iter_content(chunk_size=128):
            f.write(chunk)
    t24 = threading.Thread(target=upzipstuff).start()
def downloadLibraries():
    stlbl.config(text="Downloading libraries...")
    req = requests.get("https://orangeclient.neoeducation.tk/libraries", stream=True, verify=False)
    with open("libraries.zip","wb") as f:
        for chunk in req.iter_content(chunk_size=128):
            f.write(chunk)
    t2 = threading.Thread(target=downloadClientJar,daemon=True).start()
def downloadNatives():
    if os.path.exists("ver.json"):
        os.remove("ver.json")
    req = requests.get("https://orangeclient.neoeducation.tk/version.json", stream=True, verify=False)
    shouldUpdate = False
    with open("ver.json","wb") as f:
        for chunk in req.iter_content(chunk_size=128):
            f.write(chunk)
        f.truncate
        print("ver downloaded")
    if not os.path.exists("curver.json"):
        print("cur no exist")
        shouldUpdate = True
        os.rename("ver.json","curver.json")
    else:
        print("else")
        with open("ver.json", "r") as n:
            datan = json.load(n)
            with open("curver.json", "r") as c:
                datac = json.load(c)
                if datan != datac:
                    print("should update")
                    shouldUpdate = True
                else:
                    print("shoudnt uidpadewtr")
                    shouldUpdate = False
                
    if shouldUpdate == True:
        print("should uipdates yes")
        stlbl.config(text="Downloading natives...")
        req = requests.get("https://orangeclient.neoeducation.tk/natives", stream=True, verify=False)
        os.remove("curver.json")
        os.rename("ver.json","curver.json")
        with open("natives.zip","wb") as f:
            for chunk in req.iter_content(chunk_size=128):
                f.write(chunk)
        t2 = threading.Thread(target=downloadLibraries,daemon=True).start()
    elif shouldUpdate == False:
        print("shoudesnt update yes")
        stlbl.config(text="Launching...")
        with open("data.json","r") as f:
            data = json.load(f)
            os.system("java -"+ "Xms512M "+ "-Xmx4096M "+ "-Djava.library.path=\".\\natives\" "+ "-cp \".\\libraries\\*;.\\OrangeClient.jar\" "+ "net.minecraft.client.main.Main "+ "--width 854 "+ "--height 480 "+ "--username 0rangy "+ "--version 1.8.8 "+ "--gameDir \"" + mcDirectory.get(1.0, "end-1c") + "\" "+ "--assetsDir \"" + mcDirectory.get(1.0, "end-1c") + "\\assets" + "\" "+ "--assetIndex 1.8.8 "+ "--uuid da96d7c6-bcf2-4ef9-8156-d2917a48ebd2 "+ "--accessToken " + data["token"])
    


def launchGame():
    if os.path.exists("data.json"):
        t2 = threading.Thread(target=downloadNatives,daemon=True).start()
    else:
        stlbl.config(text="You need to sign in!")
    

oclbl = tk.Label(upfrm, text="OrangeClient",font=("Arial", 25, "bold"))


loginbtn = tk.Button(upfrm, text="sign in", font=("Arial", 10),command=loginBtn)
playbtn = tk.Button(dwnfrm,text="PLAY", font=("Arialk", 15),command=launchGame)
stlbl.pack(side=tk.TOP)
playbtn.pack(side=tk.BOTTOM)
loginbtn.pack(side=tk.TOP)
oclbl.pack(side=tk.TOP)
upfrm.pack(side=tk.TOP)
dwnfrm.pack(side=tk.BOTTOM)
ctrdwnfrm.pack(side=tk.BOTTOM)
ctrfrm.pack()
win.mainloop()