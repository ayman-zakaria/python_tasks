'''import time
n=9
# Upper portion
u = (n - 1) // 2;
# Lower portion
l = 3 * n // 2 - 1;
for z in range(4):
    for i in range(n):
        for j in range(n):
    # Check conditions to print the right arrow
            if ( j + i == u or j + i == l or i == u ) :
                print("*", end = "")
        
            # Otherwise, print space
            else:
                print(" ", end = "")
        print()
    time.sleep(1)'''
import time 
import os


for i in range(1):
    #left
    for row in range(2,7):
        for col in range (0,5):
            if (row +col==4) or (row-col==4)  or (row==4)  :
                   print ("*",end="")
            else :
                   print (" ",end="")
        print()
    time.sleep(1)
    #os.system('cls')
    #down
    for row in range(4,9):
        for col in range( 0,7):
            if col in range (0,2,1):
                print (" ",end="")
            elif  (row-col==4)  or (col==4) or (col+row==12) :
                print ("*",end="")
            else:
                print (" ",end="")
        print()
    


    time.sleep(1)
    #os.system('cls')
    
    #right

    for row in range(2,7):
        for col in range (0,9):
            if col in range(0,4,1):
                print (" ",end="")
            elif  (col-row==4)  or (row==4) or (col+row==12) :
                   print ("*",end="")
            else :
                   print (" ",end="")
        print()

    time.sleep(1)
    #os.system('cls')

    #up
    for row in range(0,5):
        for col in range (0,7):
            if col in range(0,2,1):
                print (" ",end="")

            elif  (col+row==4)  or (col==4) or (col-row==4) :
                   print ("*",end="")
            else :
                   print (" ",end="")
        print()
    time.sleep(1)
    #os.system('cls')





