#!/usr/bin/

# rigthClick miniscreenshot
from mss.linux import MSS as mss
import mss.tools

import os
import pyautogui
from pymouse import PyMouseEvent
import time

os.chdir('/home/agustinmaletti/Escritorio/Python/Imagenes')


print(str(os.getcwd()))

def screenShotMini():
        def mousePositionX():
            a, b = pyautogui.position()
            a  = int(a)
            return (a) 
        def mousePositionY():
            a, b = pyautogui.position()
            b = int(b)
            return (b) 
  
        def createMonitor():
            menuMonitor = {
            'top': mousePositionY(), 'left': mousePositionX(), 
            'width': 223, 'height': 159}
            return menuMonitor

        def grabData(menuMonitor):
            sct = mss.mss()
            sct_img = sct.grab(menuMonitor)
            return sct_img
        '''executamos as duas funções anteriores'''
        
        imgThere = grabData(createMonitor())
   
        def saveTo():
            menuMonitor = createMonitor()      
            output = 'sct-{left}x{top}_{width}x{height}.png'.format(**menuMonitor) 
            mss.tools.to_png(imgThere.rgb, imgThere.size, output=output)
            return output    
        '''salvamos la imagen'''
        
        output = saveTo()
        
        def  checkColor(output):
            with open(output) as  img:
                a = img.getpixel(160, 36) 
                if  a == (56, 56, 56):
                    print('Gris')
            
            
class event(PyMouseEvent):
    
    def move(self, x, y):
        print('Mouse moved to', x,  y)
        time.sleep
    def click(self, x, y, button, press):
            if press:
                if button == 2:
                   print('Mouse Press at', x, y)
                   time.sleep(0.70)
                   screenShotMini()
                    
e = event() 
e.run()





   

'''

while ==True:

 im = pyautogui.screenshot('nombredefoto')
 im.getpixel(
 
 (a, b = (pyautogui.position())
    pixelColor = str(pyautogui.screenshot(region=).getpixel(a))


if color.getpixel in coordenadas pixel arriva == (1,2,3,)# color rgb
#mover mouse para arriva
pyautogui.moveRel(0,0,0,50)
else if color.pixel in coordenadas pixel abajo == (1,2,3)
mover mouse para abajo
'''






