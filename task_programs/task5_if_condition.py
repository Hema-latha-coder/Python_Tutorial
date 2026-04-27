acc_bal= 100000
atm_bal= 200000
wit_amt=20000

if atm_bal== 0 and acc_bal== 0:
    print("insufficient balance")
elif wit_amt >= 20000:
    print("Limit exceeds")
elif acc_bal > 0 and wit_amt <= 20000 :
    print("Enter 4 digit otp")
