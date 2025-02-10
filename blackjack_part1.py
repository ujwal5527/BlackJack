num= int(input())
if num==1:
    print("Drew an Ace")
elif num==8:
    print("Drew an 8")
elif num<=10 and num!=8 and num>1:
    print(f"Drew a {num}")
elif num==11:
    print("Drew a Jack")
elif num==12:
    print("Drew a Queen")
elif num==13:
    print("Drew a King")
else:
    print("BAD CARD")

