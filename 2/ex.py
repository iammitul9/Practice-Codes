
  

  
# Driver Code 
  
dict ={"java":100, "python":112, "c":11} 
print("\n\n")

x = dict.items() 

#print("\n\n")

y = list(x)

#print("\n\n")
#print("\n\n")

j=0
while (j < len(x)):
	for a,b in x: 
		print(y[j])
		print(y[j][1])
		b = y[j][1]
		print (a)
		j += 1
		
		
		