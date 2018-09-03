num1= int(input("Enter number 1 :"))
num2= int(input("Enter number 2 :"))
temp1=-1
temp2=-1
rem=0

for i in range (1,(num1//2)+1,):
	if(num1%i==0):
		temp1+=i
		
for i in range (1,(num2//2)+1,):
	if(num2%i==0):
		temp2+=i
		
print(temp1)
print (temp2)
	

if (temp1==num2 ):
	if(temp2==num1):
		print("Is buddy number")
	
else :
	print("Not buddy number")