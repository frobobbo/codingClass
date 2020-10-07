from fortniteClass import FortniteStats
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time
from PIL import Image, ImageDraw, ImageFont
from pynput.keyboard import Key, Listener

def clearDisplay(display, drawing):
  drawing.rectangle((0,0,width,height),outline=0,fill=0)
  display.clear()
  display.display()

#Initialize Display
RST = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()

width = disp.width
height = disp.height

screen1 = Image.new('1', (width,height))
screen2 = Image.new('1', (width,height))
screen3 = Image.new('1', (width,height))
screen4 = Image.new('1', (width,height))
screen5 = Image.new('1', (width,height))

drawOnScreen1 = ImageDraw.Draw(screen1)
drawOnScreen2 = ImageDraw.Draw(screen2)
drawOnScreen3 = ImageDraw.Draw(screen3)
drawOnScreen4 = ImageDraw.Draw(screen4)
drawOnScreen5 = ImageDraw.Draw(screen5)

clearDisplay(disp, drawOnScreen1)
clearDisplay(disp, drawOnScreen2)
clearDisplay(disp, drawOnScreen3)
clearDisplay(disp, drawOnScreen4)
clearDisplay(disp, drawOnScreen5)

padding = -2
top = padding

bottom = height-padding
x=0
font = ImageFont.load_default()

#End Initialize Display

fortniteUser = input("Enter your Fortnite Username: ") #'UNC_DoubleJ'

fStats = FortniteStats(fortniteUser)

print (f"Solo Score: {fStats.soloScore}")
print (f"Duo Score: {fStats.duoScore}")
print (f"Squad Score: {fStats.squadScore}")

print (f"Solo Kills: {fStats.soloKills}")
print (f"Duo Kills: {fStats.duoKills}")
print (f"Squad Kills: {fStats.squadKills}")

print (f"Solo Wins: {fStats.soloWins}")
print (f"Duo Wins: {fStats.duoWins}")
print (f"Squad Wins: {fStats.squadWins}")

print (f"Total Wins: {fStats.totalWins}")
print (f"Total Kills: {fStats.totalKills}")
print (f"Total Score: {fStats.totalScore}")
print (f"Total Win Percentage: {fStats.totalWinPct}")

#Create Screen 1
drawOnScreen1.text((x,top),    "Fortnite Stats for", font=font,fill=255)
drawOnScreen1.text((x,top+8),  "--------------", font=font,fill=255)
drawOnScreen1.text((x,top+16), fortniteUser, font=font,fill=255)

#Create Screen 2
drawOnScreen2.text((x,top),    "Solo Stats", font=font,fill=255)
drawOnScreen2.text((x,top+8),  "--------------", font=font,fill=255)
drawOnScreen2.text((x,top+16), "Kills: " + fStats.soloKills, font=font,fill=255)
drawOnScreen2.text((x,top+26), "Wins: " + fStats.soloWins, font=font,fill=255)
drawOnScreen2.text((x,top+36), "Score: " + fStats.soloScore, font=font,fill=255)

#Create Screen 3
drawOnScreen3.text((x,top),    "Duo Stats", font=font,fill=255)
drawOnScreen3.text((x,top+8),  "--------------", font=font,fill=255)
drawOnScreen3.text((x,top+16), "Kills: " + fStats.duoKills, font=font,fill=255)
drawOnScreen3.text((x,top+26), "Wins: " + fStats.duoWins, font=font,fill=255)
drawOnScreen3.text((x,top+36), "Score: " + fStats.duoScore, font=font,fill=255)

#Create Screen 4
drawOnScreen4.text((x,top),    "Squad Stats", font=font,fill=255)
drawOnScreen4.text((x,top+8),  "--------------", font=font,fill=255)
drawOnScreen4.text((x,top+16), "Kills: " + fStats.squadKills, font=font,fill=255)
drawOnScreen4.text((x,top+26), "Wins: " + fStats.squadWins, font=font,fill=255)
drawOnScreen4.text((x,top+36), "Score: " + fStats.squadScore, font=font,fill=255)

#Create Screen 5
drawOnScreen5.text((x,top),    "Total Stats", font=font,fill=255)
drawOnScreen5.text((x,top+8),  "--------------", font=font,fill=255)
drawOnScreen5.text((x,top+16), "Kills: " + fStats.totalKills, font=font,fill=255)
drawOnScreen5.text((x,top+26), "Wins: " + fStats.totalWins, font=font,fill=255)
drawOnScreen5.text((x,top+36), "Score: " + fStats.totalScore, font=font,fill=255)
drawOnScreen5.text((x,top+46), "Win %: " + fStats.totalWinPct, font=font,fill=255)


def on_keypress(key):
    if hasattr(key, 'char'):
        if key.char == '1':
            print("inside 1 block")
            disp.image(screen1)
            disp.display()
        if key.char == '2':
            disp.image(screen2)
            disp.display()
        if key.char == '3':
            disp.image(screen3)
            disp.display()
        if key.char == '4':
            disp.image(screen4)
            disp.display()
        if key.char == '5':
            disp.image(screen5)
            disp.display()
        if key.char == 'q':
            disp.clear()
            disp.display()
            return False
                   
with Listener(on_press=on_keypress) as listener:
    listener.join()





#if time.sleep(4)
#disp.image(screen2)
#disp.display()
#time.sleep(4)
#disp.image(screen3)
#disp.display()
#time.sleep(4)
#disp.image(screen4)
#isp.display()
#time.sleep(4)
#disp.image(screen5)
#disp.display()
