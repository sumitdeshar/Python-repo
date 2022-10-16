# reading from external files
# dont run for fun it vhanges the files
#open("employee.txt","r") #read
#open("employee.txt","w") #write
#open("employee.txt","a") #append
#open("employee.txt","r+") #read and write
# whenever you open a file you have to make sure to close it also
employee_file = open("employee.txt","r")
#print(employee_file.readable())#checking whether it is readable or not it returns boolen o/p
#print(employee_file.read()) #read all files
#print(employee_file.readline()) #read single line
#print(employee_file.readline()) # read next line
#print(employee_file.readline()) #and next
print(employee_file.readlines()) # reads and puts every line in a array
employee_file.close()
#using for loop use other word instead of i only
employee_file = open("employee.txt","r")
for i in employee_file.readlines():
        print(i)
employee_file.close()
#editing in a file
employee_file = open("employee.txt","a")
employee_file.write("Toby - Human Resources")
employee_file.close()
#writing in a file
employee_file = open("employee.txt","a")
employee_file.write("Toby - Human Resources") # deletes everything and write the content
employee_file.close()
#creating new files
employee_file = open("employee1.txt","a")
employee_file.write("Toby - Human Resources") # deletes everything and write the content
employee_file.close()