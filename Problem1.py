n = int(input())          

D = {}                   

for i in range(n):        
    
    temp = input().strip()  # Get the string and strip id used to Remove leading/tailing spaces 

    temp = temp.replace(" ", "") 

   
    if temp.lower() not in D:
        D[temp] = 1          # If the string (in lowercase) is not in the dictionary, add it with a count of 1
    else:
        D[temp] += 1          # If the string (in lowercase) is already in the dictionary, increase its count by 1


res_non_occ = len(D)      


print(res_non_occ)            

for j in D.values():            #d.values() is used to get values from the dict
    print(j, end=" ")