import csv
file = open('test.csv', 'w')
    
print ("welcome to our small supermarket ")
choose1=int (input ("enter 1 for customers \nenter 2 for owner "))  #choose if client or owner 
i=1
bannanaprice=10
mangoprice=15
appelprice=20
waterprice=5
coffeprice=10
peppsiprice=16
prices=[peppsiprice,coffeprice,waterprice,appelprice,mangoprice,bannanaprice]
grocerylist=['banana','mango','appel']
drinkslist=['water','coffe','peppsi']
quantityG=[20,10,5]
quantityD=[20,10,5]

while (i) :
    if (choose1==1):
        choose2=int(input ("to see categories of product enter 1\nto back enter 2\n"))
        if(choose2==1):
            choose3=int(input("for grocery enter 1\nfor drinks enter 2\n"))
            if(choose3==1):
                print ()
                choose4=int (input("1-bannana (10 egp)\n2-mango (15 egp)\n3-appel(20 egp)\n "))
                if(choose4==1):
                            banana=int(input("enter value"))
                            pricebanana=banana*bannanaprice
                            print("----------Total--------------\n")
                            print("now price = ",+pricebanana,"EGP")
                            print("quantity ",+banana)
                            quantityG[0]=quantityG[0]-banana
                            # break
                elif(choose4==2):
                        mango=int(input("enter value"))
                        pricemango=mango*mangoprice
                        print("now price = ",+pricemango,"EGP")
                        print("quantity ",+mango)
                        quantityG[1]=quantityG[1]-mango
                        # break
                elif(choose4==3):
                        appel=int(input("enter value"))
                        priceappel=appel*appelprice
                        print("----------Total--------------\n")
                        print("now price = ",+priceappel,"EGP")
                        print("quantity ",+appel)
                        quantityG[2]=quantityG[2]-appel
                        # break
                   
            elif(choose3==2):
                    choose5=int (input("1-water(5 egp)\n2-coffe(10 egp)\n3-peppsi(16 egp)\n "))
                    if(choose5==1):
                            water=int(input("enter value"))
                            pricewater=water*waterprice
                            print("----------Total--------------\n")
                            print("now price = ",+pricewater,"EGP")
                            print("quantity ",+water)
                            quantityD[0]=quantityD[0]-water

                            # break
                    elif(choose5==2):
                            coffe=int(input("enter value"))
                            pricecoffe=coffe*coffeprice
                            print("----------Total--------------\n")
                            print("now price = ",+pricecoffe,"EGP")
                            print("quantity ",+coffe)
                            quantityD[1]=quantityD[1]-coffe
                            # break
                    elif(choose5==3):
                            peppsi=int(input("enter value"))
                            pricepeppsi=peppsi*bannanaprice
                            print("----------Total--------------\n")
                            print("now price = ",+pricepeppsi,"EGP")
                            print("quantity ",+peppsi)
                            quantityD[2]=quantityD[2]-1
                            # break
                  
        elif(choose2==2):
            i==0 
            break
    if(choose1==2)  :
        print("welcome sir")
        choose6=int(input('enter 1- to add item 2-to Show stock 3-to exit'))
        if(choose6==1):
            choose7=input ("choose which category to add in grocery (g) drinks (d)")
            if (choose7 =="g"):
                newitem=input("enter new item\n")
                grocerylist.append(newitem)
                newprice=int(input("enter new price\n"))
                prices.append(newprice)
                print("list now\n")
                print(grocerylist)
                break
            elif(choose7=="d"):
                newitem2=input("enter new item\n")
                drinkslist.append(newitem)
                newprice2=int(input("enter new price\n"))
                prices.append(newprice2)
                print("list now\n")
                print(drinkslist)
                break
        elif(choose6==2)   :
            new=input("choose which category to show (g) grocerry (d) drinks")
          
            if (new=='g'):
                print(grocerylist)
                print(quantityG)
            if (new=='d'):
                print(drinkslist)
                print(quantityD)
        if(choose6==3):
            i==0
            break
writer = csv.writer(file)
writer.writerow(grocerylist)
writer.writerow(quantityG)
writer.writerow(drinkslist)
writer.writerow(quantityD)
file.close() 