#minecraft photo booth

from mcpi.minecraft import Minecraft
from picamera import PiCamera
from time import sleep

mc = Minecraft.create()
cam = PiCamera()

def takeAPic():
    cam.start_preview()
    sleep(2)
    cam.capture('/home/pi/selfi.jpg')
    cam.stop_preview()


while True:
    x, y, z, = mc.player.getPos()
    sleep(1)
    
    if x >= 16.4 and x <= 16.6 and y == 17.0 and z >= 3.3 and z <= 3.4:
        mc.postToChat("In the PhotoBooth")
        takeAPic()
#    mc.postToChat((x,y,z))

#16.4036,17.0,3.3087

#mc.postToChat("Hello Minecraft World")