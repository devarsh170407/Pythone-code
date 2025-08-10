list1 = [1, 2, 3, 4, 5, 3]
freq = {}
for i in list1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    
for key in freq:
    print("frequency of", key, "is:", freq[key])