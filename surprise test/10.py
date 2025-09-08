numbers = [1,2,5,10,11,14,17,20]
missing=[]  
for i in range(1,21):  
    if i not in numbers:  
        missing.append(i) 
print(missing)
