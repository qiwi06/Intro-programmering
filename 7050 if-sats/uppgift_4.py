text=input("Ange ett tal:")
tal=float(text)
if tal>=0 and tal <=9:
    print("talet är ensiffrigt")
elif tal>=10 and tal <=99:
    print("talet är tvåsiffrigt")
elif tal>=100 and tal<=999:
    print("talet är tresiffrigt")
elif tal>=1000:
    print("är minst ett fyrsiffrigttal")
elif tal<0:
    print("talet är negativt")
