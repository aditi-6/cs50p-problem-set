print("amount due: 50")
def main():
    ad= 50
    accepted_coins=[5,10,25]

    while ad > 0:
        c=int(input("inset coin: "))
        
        if c in accepted_coins:
            ad-= c
        else:
            print(f"amount due: {ad}")
            continue

        if ad>0:
            print(f"amount due = {ad}")
    print(f"owed amount:{ad}")


main() 
        


