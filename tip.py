#m=int(input("enter mass in kg: "))
#c=3*(10**8)
#E=m*(c**2)
#print(f"E={E} Joules")


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
   a=input("enter amout of the bill: ")
   return a.replace("$","")

def percent_to_float(p):
 main()




fn=input("file name")
a,b=fn.split(".")
if b=="gif" or "jpeg" or "png" or "jpg":
    print("image/",b, sep="")
elif b=="css" or"csv":
    print("image/", b, sep="")
elif b=="pdf"or"zip":
    print("application/", b, sep="")
elif b=="txt":
    print("text/plain")
elif b=="mp3":
    print

else:
    print("application/octet-stream")


