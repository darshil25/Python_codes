sale = input("Enter Total Sales in Rs. : ")
sale = int(sale)

if sale >= 100000 :
    bs = 4000
    hra = 20 * bs/100
    da = 110 * bs/100
    cv = 500
    incentive = sale * 10/100
    bonus = 1000
else:
    bs = 4000
    hra = 10 * bs/100
    da = 110 * bs/100
    cv = 500
    incentive = sale * 4/100
    bonus = 500

ts = bs + hra + da + cv + incentive + bonus
print ("\nTotal Sales : %.2f"%(sale))
print ("\nBasic Salary : %.2f"%(bs))
print ("\nHra          : %.2f"%(hra))
print ("\nDa           : %.2f"%(da))
print ("\nConveyance   : %.2f"%(cv))
print ("\nIncentive    : %.2f"%(incentive))
print ("\nBonus        : %.2f"%(bonus))
print ("\nGross Salary : %.2f"%(ts))