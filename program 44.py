#program for text rotating in pygame(graphics)

#import a library of functions called 'pygame'
import pygame
import sys
#initialize the game engine
pygame.init()

#define some colours
BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)

PI=3.141592653

#set the height and width of the screen
size=(400,500)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("rotate text")

#loop until the user clicks the close button.
done=False
clock=pygame.time.Clock()

text_rotate_degrees=0

#loop as long as done==false
while not done:

    for event in pygame.event.get(): #user did somethings
        if event.type==pygame.QUIT: #if user clicked close
            done=True #flag that we are done so we exit this loop

    #all drawing code happens after the for loop and but inside the main while not done loop.

    #clear the screen and set the screen and set the screen background
    screen.fill(WHITE)

    #draw some borders
    pygame.draw.line(screen,BLACK,[100,50],[200,50])
    pygame.draw.line(screen,BLACK,[100,50],[100,150])

    #select the font to use, size, bold, italics
    font=pygame.font.SysFont("calibri",25,True,False)

    #sideways text 
    text=font.render("sideways text",True,BLACK)
    text=pygame.transform.rotate(text,90)
    screen.blit(text,[0,0])

    #sideways text
    text=font.render("upside down text",True,BLACK)
    text=pygame.transform.rotate(text,180)
    screen.blit(text,[30,0])

    #flipped text
    text=font.render("flipped text",True,BLACK)
    text=pygame.transform.flip(text,False,True)
    screen.blit(text,[30,20])

    #animated rotation
    text=font.render("rotating text",True,BLACK)
    text=pygame.transform.rotate(text,text_rotate_degrees)
    text_rotate_degrees+=1
    screen.blit(text,[100,50])

    #go a head and update the screen with what we've drawn.
    #this must happen after all the other drawing commands.
    pygame.display.flip()

    #this limits the while loop to a max of 60 times per second.
    #leave this out and we will use all CPU we can.
    clock.tick(60)

pygame.quit()