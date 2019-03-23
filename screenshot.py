from PIL import ImageGrab
from PIL import Image
import webbrowser as wb
import time
import os

ctg = 'OL7'
f = open(ctg + '.txt', 'r')

lines = f.readlines()


for line in lines:

    placeid = line[:-1]
    print(placeid)
    
    if os.path.isfile(ctg +'/' + placeid + '.jpg') is True: continue

    wb.open('http://map.daum.net/link/roadview/' + placeid, new = 0, autoraise=True)

    time.sleep(5)

    img = ImageGrab.grab(bbox=(400,200,1920,900))
    img.save("temp.png")

    im = Image.open("temp.png")
    rgb_im = im.convert('RGB')
    rgb_im.save(ctg +'/' + placeid + '.jpg')
    

    
    #browserExe = "chrome.exe"
    #os.system("taskkill /f /im "+browserExe)
f

f.close()


#browserExe = "chrome.exe"
#os.system("taskkill /f /im "+browserExe)
