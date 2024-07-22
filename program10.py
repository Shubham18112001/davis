# write a program to create a binary file "stu.dat" and enter students roll no., name and marks till the user wants

import struct
filename = "stu.dat"
with open(filename, "wb") as file:
    while True:
        rollno = int(input("Enter roll number: "))
        name = input("Enter name (max 50 characters): ").ljust(50)[:50] 
        marks = float(input("Enter marks: "))      
        packed_data = struct.pack('I50sf', rollno, name.encode('utf-8'), marks)
        file.write(packed_data)        
        continue_input = input("Do you want to enter another student? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break
print("Data has been written to", filename)

print("********************************")

with open(filename, "rb") as file:
    while True:
        data = file.read(struct.calcsize('I50sf'))
        if not data:
            break
        rollno, name, marks = struct.unpack('I50sf', data)
        name = name.decode('utf-8').strip()  
        print(f"Roll Number: {rollno}, Name: {name}, Marks: {marks}")

print("********************************")
