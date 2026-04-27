tam,eng,mat,sci,soc=89,75,72,56,67

if tam >= 40 and eng >= 40 and mat >= 40 and sci >= 40 and soc >= 40:
    print("Pass")
    average=(tam+eng+mat+sci+soc)/5
    print("Average=", average)

    if average == 50:
        print("Just pass")

    elif average > 50 and average <= 65:
        print("Second class")

    elif average > 66 and average <= 75:
        print("First class")

    elif average > 76 and average <= 85:
        print("Excellent")

    elif average > 86 and average <= 100:
        print("Extraordinary")

else:
    print("Fail")
    average=(tam+eng+mat+sci+soc)/5
    print("Average=", average)