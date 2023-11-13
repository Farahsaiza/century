def leapyear(X):
    if X%400==0 or (X%4==0 and X%100!=0) :
        return  True
    else:
        return False
    
def century(X):
    year=(X-1)*100
  
    return year
        
    

c=int(input("enter a century: "))
year=century(c)
i=0
while i<=100:
    years=year+i
    if leapyear(years)== True:
        print(years)
    
    i=i+1




  
