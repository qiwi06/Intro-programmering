text1=input("Skriv in ett tal:")
tal1=float(text1)
text2=input("skriv in ett till tal")
tal2=float(text2)
text3=input("skriv in ett tredje tal:")
tal3=float(text3)
if tal1>tal2:
    print("det andra talet är minst")
elif tal2>tal3:
    print("det tredje talet är minst")
elif tal1>tal3:
    print("det tredje talet är minst")
elif tal2>tal1:
    print("tal ett är minst")
elif tal3>tal1:
    print("tal ett är minst")
elif tal3>tal2:
    print("tal två är minst")

    