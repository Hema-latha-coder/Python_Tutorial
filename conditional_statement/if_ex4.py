tam,eng,mat,sci,ss=87,90,30,76,88

if tam >= 35 and eng >= 35 and mat >=35 and sci >=35 and ss >=35:
    
    print("Pass")
    average = (tam+eng+mat+sci+ss)/5
    print("Average = ", average)
    
else:
    print("Fail")