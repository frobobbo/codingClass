from FortniteAPI import FortniteAPI
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time
from PIL import Image, ImageDraw, ImageFont

#Fortnite Statistics Global Variables
soloScore = ""
duoScore = ""
squadScore = ""
soloKills = ""
duoKills = ""
squadKills = ""
soloWins = ""
duoWins = ""
squadWins = ""
totalKills = ""
totalWins = ""
totalScore = ""
totalWinPct = ""

def updateStats(fortniteUserName):
    FortniteAPI.api_key = 'feeee83b-54d6-42fc-b4c3-f47a5f58f16e'
    user = FortniteAPI('all',fortniteUserName)
    
    soloScore = str(user.stats.LIFETIME_SOLO_SCORE)
    duoScore = str(user.stats.LIFETIME_DUO_SCORE)
    squadScore = str(user.stats.LIFETIME_SQUAD_SCORE)
    soloKills = str(user.stats.LIFETIME_SOLO_KILLS)
    duoKills = str(user.stats.LIFETIME_DUO_KILLS)
    squadKills = str(user.stats.LIFETIME_SQUAD_KILLS)
    soloWins = str(user.stats.LIFETIME_SOLO_WINS)
    duoWins = str(user.stats.LIFETIME_DUO_WINS)
    squadWins = str(user.stats.LIFETIME_SQUAD_WINS)
    totalKills = str(user.stats.LIFETIME_KILLS)
    totalWins = str(user.stats.LIFETIME_WINS)
    totalScore = str(user.stats.LIFETIME_SCORE)
    totalWinPct = str(user.stats.LIFETIME_WIN_PERCENTAGE)


def clearDisplay(display, drawing):
  drawing.rectangle((0,0,width,height),outline=0,fill=0)
  display.clear()
  display.display()


#Initialize Display
RST = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

image1 = Image.new('1', (width,height))

draw = ImageDraw.Draw (image1)
draw.rectangle((0,0,width,height),outline=0,fill=0)

padding = -2
top = padding

bottom = height-padding
x=0
font = ImageFont.load_default()

fortniteUser = input("Enter your Fortnite Username: ") #'UNC_DoubleJ'

FortniteAPI.api_key = 'feeee83b-54d6-42fc-b4c3-f47a5f58f16e'
user = FortniteAPI('all',fortniteUser)

clearDisplay(disp, draw)
draw.text((x,top),    "Fortnite Stats for", font=font,fill=255)
draw.text((x,top+8),  "--------------", font=font,fill=255)
draw.text((x,top+16), fortniteUser, font=font,fill=255)
disp.image(image1)
disp.display()


time.sleep(2)

clearDisplay(disp, draw)
draw.text((x,top),    "Lifetime Stats", font=font,fill=255)
draw.text((x,top+8),  "--------------", font=font,fill=255)
draw.text((x,top+16), "Solo Kills: " + str(user.stats.LIFETIME_SOLO_KILLS), font=font,fill=255)
draw.text((x,top+26), "Duo Kills: " + str(user.stats.LIFETIME_DUO_KILLS), font=font,fill=255)
draw.text((x,top+36), "Squad Kills: " + str(user.stats.LIFETIME_SQUAD_KILLS), font=font,fill=255)
draw.text((x,top+46), "Solo Kills: " + str(user.stats.LIFETIME_SOLO_KILLS), font=font,fill=255)
draw.text((x,top+56), "Duo Kills: " + str(user.stats.LIFETIME_DUO_KILLS), font=font,fill=255)
disp.image(image1)
disp.display()



print('Current Season\n---------------')
print('Solo Kills: ' + str(user.stats.CURRENT_SOLO_KILLS))
print('Duo Kills: ' + str(user.stats.CURRENT_DUO_KILLS))
print('Squad Kills: ' + str(user.stats.CURRENT_SQUAD_KILLS))

print('\nLifetime\n---------------')
print('Solo Kills: ' + str(user.stats.LIFETIME_SOLO_KILLS))
print('Duo Kills: ' + str(user.stats.LIFETIME_DUO_KILLS))
print('Squad Kills: ' + str(user.stats.LIFETIME_SQUAD_KILLS))
print('Solo Score: ' + str(user.stats.LIFETIME_SOLO_SCORE))
print('Duo Score: ' + str(user.stats.LIFETIME_DUO_SCORE))
print('Squad Score: ' + str(user.stats.LIFETIME_SQUAD_SCORE))
