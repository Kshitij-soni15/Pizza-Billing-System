total_bill = 0 
e2 = 0 
c2 =  0 
b2 = 0
while total_bill >= 0:
    print('')
    a = input(' Size of pizza (s/m/l) : ')
    if a == 's' :
        b = int(input('qty : '))
        price = 150
        total_bill += b*150
        break
    elif a =='m':
        b = int(input('qty : '))
        price = 250
        total_bill += b*250
        break
    elif a == "l" :
        b = int(input('qty : '))
        price = 350
        total_bill += b*350
        break
    else:
        print('invalide selection : ')
        
while total_bill >= 0 :
    print('')
    extra_cheese = input('do you want extra cheese , y or n : ')
    if  extra_cheese == 'y' :
        extra_packets = int(input(' how many packets : '))
        total_bill += 50*extra_packets
        break
    elif  extra_cheese == 'n' :
        total_bill += 0
        extra_packets = 0
        break
    else : 
        print('invalid selection ')
        
while total_bill >= 0 :
    print('')
    cold_drink = input('do you want cold drink , y or n : ')
    if cold_drink == 'y' :
        bottles = int(input(' how many bottles : '))
        total_bill += 60*bottles
        break
    elif  cold_drink == 'n' :
        total_bill += 0
        bottles = 0 
        break
    else : 
        print('invalid selection ') 
print('')    



if total_bill<=499 :
     print('   ! dilivery charges : 50 , shope more than 499 for free dilivery !          ')
     j=input(" do you want to add items , y or n : ")
     if j=='y':
        while total_bill >= 0:
            print('')
            if a == 's' :
                b2 = int(input('qty to be add in pizza : '))
                price = 150
                total_bill += b2*150
                break
            elif a =='m':
                b2 = int(input('qty to be add in pizza : '))
                price = 250
                total_bill += b2*250
                break
            elif a == "l" :
                b2 = int(input('qty to be add in pizza : '))
                price = 350
                total_bill += b2*350
                break
            else:
                print('invalide selection : ')
        
        while total_bill >= 0 :
            print('')
            extra_cheese = input('do you want to add extra cheese , y or n : ')
            if  extra_cheese == 'y' :
                e2 = int(input(' how many packets : '))
                total_bill += 50*e2
                break
            elif  extra_cheese == 'n' :
                total_bill += 0
                extra_packets += 0
                break
            else : 
             print('invalid selection ')
        
        while total_bill >= 0 :
            print('')
            cold_drink = input('do you want to add cold drink , y or n : ')
            if cold_drink == 'y' :
                c2 = int(input(' how many bottles : '))
                total_bill += 60*c2
                break
            elif  cold_drink == 'n' :
                total_bill += 0
                c2 += 0 
                break
            else : 
                print('invalid selection ')
        print('')            
        print('')
        print('')
        print('-----------------------------------------------------------------------------')        
        print('------------------------------ bill -----------------------------------------')       
        print('')
        print('')
        print('   items            MRP                qty.              amount                ')
        print('   ')  
        print(f'   PIZZA({a})         {price}                 {b + b2}                {price*(b+b2)}             ')
        print(f'   CHEESE           50         '
    f'         {extra_packets +e2 }                {50*(e2+extra_packets)}  ')                                          
        print(f'   COLD DRINK       60                  {bottles + c2}                {60*(c2+bottles)}         ') 
        print('')
        if total_bill>=499 :
            print('                               ! FREE DILIVERY !                             ')
            print('')
            print(f'------------------------- total amount = {total_bill}--------------------------------')
            print('------------------------------------------------------------------------------')  
        if total_bill<499:
            print('                               ! NO FREE DILIVERY !                             ')
            print('')
            print(f'------------------------- total amount = {total_bill + 50}--------------------------------')
            print('------------------------------------------------------------------------------')
     if j == "n" :           
        print('')            
        print('')
        print('')
        print('-----------------------------------------------------------------------------')        
        print('------------------------------ bill -----------------------------------------')       
        print('')
        print('')
        print('   items            MRP                qty.              amount                ')
        print('   ')  
        print(f'   PIZZA({a})         {price}                 {b + b2}                {price*(b+b2)}             ')
        print(f'   CHEESE           50         '
      f'         {extra_packets+e2}                {50*(e2+extra_packets)}  ')                                          
        print(f'   COLD DRINK       60                  {bottles+c2}                {60*(c2+bottles)}         ') 
        print('')
        if total_bill>=499 :
            print('                               ! FREE DILIVERY !                             ')
            print('')
            print(f'------------------------- total amouny = {total_bill}--------------------------------')
            print('------------------------------------------------------------------------------')
   
        else:
            print('   ! dilivery charges : 50 , shope more than 499 for free dilivery !          ')
            print('')
            print(f'------------------------- total amouny = {total_bill + 50}--------------------------------')
            print('------------------------------------------------------------------------------')
else:
    print('')            
    print('')
    print('')
    print('-----------------------------------------------------------------------------')        
    print('------------------------------ bill -----------------------------------------')       
    print('')
    print('')
    print('   items            MRP                qty.              amount                ')
    print('   ')  
    print(f'   PIZZA({a})         {price}                 {b+b2}                {price*(b+b2)}             ')
    print(f'   CHEESE           50         '
     f'         {extra_packets +e2}                {50*(e2+extra_packets)}  ')                                          
    print(f'   COLD DRINK       60                  {bottles + c2}                {60*(c2+bottles)}         ') 
    print('')
    if total_bill>=499 :
        print('                               ! FREE DILIVERY !                             ')
        print('')
        print(f'------------------------- total amount = {total_bill}--------------------------------')
        print('------------------------------------------------------------------------------')   
