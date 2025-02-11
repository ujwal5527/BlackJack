num= int(input())
if num==1:
    print("Your hand value is 11.")
elif num>1 and num<=10:
    print(f"Your hand value is {num}.")
elif num==11 or num==12 or num==13:
    print("Your hand value is 10.")
else:
    print("BAD CARD")
