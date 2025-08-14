while True:
    try :
        a=input("Fraction: ")
        x,y= map(int,a.split("/"))
        if y==0:
            raise ZeroDivisionError
        c=x/y
        p=(c*100)
        p=round(p)
       
        if x>y :
            continue
        if p<=1:
            print("E")

        elif p>=99:
            print("F") 
        else :
            print(p,"%")
        break       

    except (ValueError,ZeroDivisionError):
       continue
    

