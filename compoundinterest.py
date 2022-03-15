print("coding challenge 1, compund interest.py");


print("welcome to wolving compound interest calculator");
print("This program calculates your potential returns when you invest with us");


p = float(input("How much would you like to invest?:"))
t = int(input("how long are you planning to invest?:"))
r = float(input("what is the interest rate on your account?:"))
n = int(input("what is the number of times the interest is compounded per year?:"))
p = round(p,2)
r = r/100
a = p*(1+(r/n))**(n*t)
a = format(a, '.2f');


print("\n")
print("Year   Period   Old Balance   Interest   New Balance")
print("------------------------------------------------------------------------------")

oldBalance = p
for year in range(1,t+1):
      count =1
      for period in range(1,n+1):
          interest = oldBalance*(r/n)
          newBalance = oldBalance + interest
          if (count == 1):
              print(f"{year}        {period}     £{oldBalance:.2f}     £{interest:.2f}     £{newBalance:.2f}")

          else:
              print(f"         {period}     £{oldBalance:.2f}     £{interest:.2f}     £{newBalance:.2f}")


          oldBalance = newBalance
          count+=1


print("\n")
print(f"£{p} invested at {r*100}% for {t} years compounded {n} times per year is: £{a}" )
