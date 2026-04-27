stuMark = 117

if stuMark < 50:  # 85 < 50
    print("Fail")
    
elif stuMark == 50:  # 85 == 50
    print("Just Pass")
    
elif stuMark > 50 and stuMark < 60: # 85> 50 and 85 < 60
    print("Second class")
    
elif stuMark >= 60 and stuMark < 80: # 85 > 60 and 85 < 80 
    print("First class")
    
elif stuMark >=80 and stuMark <=95: # 85 >= 80 and 85 <= 95
    print("Excellent")
    
elif stuMark > 95 and stuMark <= 100:
    print("Distinction")
    
    
else:
    print("Given mark is invalid")