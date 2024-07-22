# write  program read a binary file "stu.dat" and display the records of students having marks greater than 81
import struct
filename = "stu.dat"

print("Students having greater than 81 marks\n")
with open(filename, "rb") as file:
    while True:
        record_size = struct.calcsize('I50sf')
        data = file.read(record_size)
        if not data:
            break  
        rollno, name, marks = struct.unpack('I50sf', data)
        name = name.decode('utf-8').strip()  
        if marks > 81:
            print(f"Roll Number: {rollno}, Name: {name}, Marks: {marks:.2f}")