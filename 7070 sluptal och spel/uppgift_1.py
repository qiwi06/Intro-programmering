import random

text=input("Vill du spela? j/n:")
while text=="j":
   

    tal = random.randint(1, 6)
    print(tal)
    tal2= random.randint(1, 6)
    print(tal2)
    if tal==tal2:
        print("vinst")
    else:
        print("förlust")
    text=input("Vill du spela? j/n:")
print("Vad roligt att du spelade en stund!")
