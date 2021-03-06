'''
Emotion draw
Created on 4.3.2018

@author: Sami<sami@tabloiti.com>
'''
import roundrects
import pygame
from sys import getsizeof
import config

RED = (255,0,0)
TUR = (50,156,198)
BLACK = (0,0,0)
WHITE = (255,255,255)

#SIZEW = 320
#SIZEH = 240

#SIZEW = 480
#SIZEH = 320
pygame.init()
infoObject = pygame.display.Info()

H = infoObject.current_h
W = infoObject.current_w



if config.ROTATE:
    SIZEW = H
    SIZEH = W
else:
    SIZEW = W
    SIZEH = H

EW = 70*1.5 #Eye width
EH = 100*1.5 #Eye height
MARGIN = 10 #margin between eyes

if config.ROTATE:
	EYPOS = (SIZEH/2)-(EH/2) #common for both eye
	LEYPOS = (SIZEW/2)-(EW+MARGIN)
	REYPOS = (SIZEW/2)+MARGIN
else: 
	EYPOS = (SIZEH/2)-(EH/2) #common for both eye
	LEYPOS = (SIZEW/2)-(EW+MARGIN)
	REYPOS = (SIZEW/2)+MARGIN 

#Emotions
NEUTRAL 	= 	1
LOOKDOWN 	= 	2
LOOKUP		=	3
LOOKRIGHT 	= 	4
LOOKLEFT 	= 	5
DOUBT 		= 	6
HAPPY 		= 	7
BLINK		= 	8


def texts(surface, text1, text2, mode, state):
	font=pygame.font.Font(None,20)
	font2 = pygame.font.Font(None,20)
	#fpstext=font.render("FPS:" + str(text1)+ " STATE:" + mode, 1,WHITE)
	statestr = ' STATE:'  + str(state)
	fpstext=font.render("FPS:" + str(text1)+ " MODE:" + mode + statestr , 1,WHITE)
	iptext = font2.render(text2, 1,WHITE)
	surface.blit(fpstext, (0, 15))
	surface.blit(iptext, (SIZEW-iptext.get_width()-5,SIZEH-iptext.get_height()-5))

def facedetect(surface, text1):
	font=pygame.font.Font(None,20)
	text=font.render(str(text1), 1,WHITE)
	surface.blit(text, (SIZEW-text.get_width()-5, 15))

def neutral(surface):
	#rect: (x1, y1, width, height)
	state = NEUTRAL
	#left
	roundrects.round_rect(surface, [LEYPOS, EYPOS+10, EW, EH-20], TUR, rad=30)
	#right
	roundrects.round_rect(surface, [REYPOS, EYPOS, EW, EH], TUR, rad=30)

def happy(surface):
	state = HAPPY
	#left
	roundrects.round_rect(surface, [LEYPOS, EYPOS, EW, EH], TUR, rad=30)
	#right
	roundrects.round_rect(surface, [REYPOS, EYPOS, EW, EH], TUR, rad=30)
	#draw blak box
	#rect: (x1, y1, width, height)
	pygame.draw.rect(surface, BLACK, [LEYPOS-10, EYPOS+20, (EW*2)+35, EH+15])


def doubt(surface):
	state = DOUBT
	points = list()

	points.append ( ((SIZEW/2)-5, SIZEH/2) ) #left bottom
	points.append (((SIZEW/2)+40, 0)) #top point
	points.append (((SIZEW/2)+150, (SIZEH/2)-50)) #oikealaita 290,100

	#left
	roundrects.round_rect(surface, [LEYPOS, EYPOS+10, EW, EH-30], TUR, rad=30)
	#right
	roundrects.round_rect(surface, [REYPOS, EYPOS, EW, EH-20], TUR, rad=30)

	pygame.draw.polygon(surface,BLACK, points)


def lookdown(surface):
	state = LOOKDOWN
	#left
	roundrects.round_rect(surface, [LEYPOS, EYPOS+20, EW, EH], TUR, rad=30)
	#right
	roundrects.round_rect(surface, [REYPOS, EYPOS+20, EW, EH], TUR, rad=30)

def lookup(surface):
	state = LOOKUP
	#left
	roundrects.round_rect(surface, [LEYPOS, EYPOS-40, EW, EH], TUR, rad=30)
	#right
	roundrects.round_rect(surface, [REYPOS, EYPOS-40, EW, EH], TUR, rad=30)


def lookright(surface):
	state = LOOKRIGHT
	roundrects.round_rect(surface, [LEYPOS+20, EYPOS, EW, EH-20], TUR, rad=30)
	#right
	roundrects.round_rect(surface, [REYPOS+20, EYPOS, EW, EH], TUR, rad=30)
	pygame.display.update()

def lookleft(surface):
	state = LOOKLEFT
	roundrects.round_rect(surface, [LEYPOS-20, EYPOS, EW, EH], TUR, rad=30)
	#right
	roundrects.round_rect(surface, [REYPOS-20, EYPOS, EW, EH-20], TUR, rad=30)
  
def blink(surface):
	#left
	roundrects.round_rect(surface, [LEYPOS, EYPOS, EW, EH], TUR, rad=30)
	#right
	roundrects.round_rect(surface, [REYPOS, EYPOS, EW, EH], TUR, rad=30)
	#draw blak box
	#rect: (x1, y1, width, height)
	pygame.draw.rect(surface, BLACK, [LEYPOS-10, SIZEH/2, (EW*2)+35, EH/1.4]) #2
	pygame.draw.rect(surface, BLACK, [LEYPOS-10, (SIZEH/2)-SIZEH/4, (EW*2)+35, EH/1.4]) #2

def sleep(surface):
	#left
	roundrects.round_rect(surface, [LEYPOS, EYPOS, EW, EH], TUR, rad=30)
	#right
	roundrects.round_rect(surface, [REYPOS, EYPOS, EW, EH], TUR, rad=30)
	#draw blak box
	#rect: (x1, y1, width, height)
	pygame.draw.rect(surface, BLACK, [LEYPOS-10, SIZEH/2, (EW*2)+35, EH/1.4])
	pygame.draw.rect(surface, BLACK, [LEYPOS-10, (SIZEH/2)-SIZEH/4, (EW*2)+35, EH/1.4])
