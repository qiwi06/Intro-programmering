svar=input("Skriv en form")
while svar!="rund":
    svar=input("fel gissa igen")
print("bra")

x=10
y=[1,0,1,1,0]
for z in y:
    x=x-2*z
print(x)
