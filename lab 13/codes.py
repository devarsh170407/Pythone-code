
# file1 = open(r"C:\Users\devar\OneDrive\Desktop\ict.txt")

# with open("ict.txt", 'r') as f:
#     text = f.read()

# lines = text.splitlines()
# words = text.split()
# chars = len(text)

# print("Lines:", len(lines))
# print("Words:", len(words))
# print("Characters:", chars)



# with open("ict.txt", 'r') as f1, open("ict1.txt", 'r') as f2, open("merged.txt", 'w') as fout:
#     fout.write(f1.read())
#     fout.write("\n")
#     fout.write(f2.read())



# import csv

# with open('data-1.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# lines_list = []
# with open("ict.txt", 'r') as f:
#     for line in f:
#         lines_list.append(line.strip())

# print(lines_list)



# f1 = open(r"ict.txt")
# print(f1.read())


# f1 = open(r"ict.txt")

# # Print every line one by one
# for each in f1:
#     print(each)



# with open(r"ict.txt", 'r') as f1:  
#     data = f1.read() 
# print(data)

# f1 = open(r"ict.txt")
# print(f1.read(5))


# with open(r'a.tif', 'rb') as file:
#     binary_data = file.read()


# with open(r"ict.txt", 'r') as file:
# data = file.readlines()
# for line in data:
#     word = line.split()
#     print(word)

# import csv

# with open('output.csv', 'w', newline='') as file:
# writer = csv.writer(file)
# writer.writerow(['Name', 'Subject', 'Mark'])
# writer.writerow(['Aansh', 'PWP', 9])
# writer.writerow(['Ashutosh', 'PWP', 10])
# file.close()


# file = open("ict1.txt", 'w')
# file.write("ICT ICT ICT \n")
# file.write("ICT ICT ICT ICT ICT")
# file.close()

# with open("file.txt", "w") as f: 
#     f.write("Hello World!!!") 
#     f.close()


# with open('a.tif', 'rb') as f:   
#     binary_data = f.read()

# # Then, write binary data to a new file
# with open('c.tif', 'wb') as f:   
#     f.write(binary_data)