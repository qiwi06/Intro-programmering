text1=input("Hur många heltal vill du ha?")
antal=int(text1)
start=input("Vilket är det minsta talet i serien?")
tal2=int(start)
index = tal2+antal
while tal2<index:
    print(tal2)
    tal2=tal2+1
print("klart")

