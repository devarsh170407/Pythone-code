# file1 =open(r"C:\Users\student\Downloads\ict.txt")
# for i in file1:
#       print(i)
      
#       # we read full file 
      
      
# file1 =open(r"C:\Users\student\Downloads\ict.txt")   
# print (file1.read())
# # we also read full file without for loop

# with open(r"C:\Users\student\Downloads\ict.txt",'r')as f1:
#      data = f1.read()
#      print(data)
#      # save in wuth and if we print than it also give data
#      #if we use in it is for check that file is available or not 
#      # eg s in p find s file is there in p or not it give true or false
     
     
# f1 =file1 =open(r'C:\Users\student\Downloads\ict.txt','r')   
# print(f1.read(5))
# # this is use to read specify function


# with open(r'C:\Users\student\Downloads\ict.txt','r') as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print (word)
# # this use to make all line in list 

# with open(r'C:\Users\student\Downloads\ict.txt','r') as file:
#     data = file.readlines(1)
#     for line in data:
#         word = line.split()
#         print (word)
#         # this use to read specific line 
        
# file = open("S.txt",'w')# create file
# file.write("Hi all \n")# what to write means make contain
# file.write("my name is slock")
# file.close()
# # it creat file in files and also open it
        
# file = open("a.txt",'w')# create file
# file.write("""Hi all \nmy name is slock""")# what to write means make contain

# file.close()
# # as we use """ we write all comand in one line """

# with open("file.txt", "w") as f: 
#     f.write("Hello World!!!") 
#     f.close()


# file = open("S.txt",'a')
# file.write("\n Department Department")
# file.close()
# # from append means a we add line in existint files


# file = open("S.txt",'w')
# file.write("\n Department Department")
# file.close()
# # it replace file with new line past line gones


# with open(r"S.txt", 'rb') as file:
#     binary_data = file.read() 
#     print(binary_data)

# #Writing binary files 
# with open(r"A.txt", 'wb') as f:
#     f.write(binary_data)
#     f.close()

# import csv
# # Reading from a CSV file
# with open(r"C:\Users\student\Downloads\data-1", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
