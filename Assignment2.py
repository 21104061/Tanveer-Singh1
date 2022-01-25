#Question 1

print("Q1")
line = "Python is a case sensitive language."
print()

#Q1a
print("Q1a")
length = len(line)
print(length)
print()

#Q1b
print("Q1b")
reversed = line[length::-1]
print(reversed)
print()

#Q1c
print("Q1c")
sliced_Line = line[10:-9]
print(sliced_Line)
print()

#Q1d
print("Q1d")
replaced_line = line.replace(sliced_Line, "object oriented ") 
print(replaced_line)
print()

#Q1e
print("Q1e")
index_a = line.find('a') 
print(index_a)
print()

#Q1f
print("Q1f")
nospace = line.replace(" ", "")
print(nospace)
print()

#question2

print("Q2")
print()
Data = '''Hey, <Name> here!
My SID is <SID>
I am from <Address> and my CGPA is <CGPA> '''
name = input("Your Name:  ") #For cureent Question Take it 'ABC'
SId = input("Enter Your SID: ") #Take '2110XXXX'
Address = input("Enter your Address: ") #take It 'XYZ Apartment'
CGPA = input("Enter Your CGPA: ") #take '9.9'
New_Data1 = Data.replace("<Name>", name)
New_Data2 = New_Data1.replace("<SID>",SId ) 
New_Data3 = New_Data2.replace("<Address>", Address) 
New_Data = New_Data3.replace("<CGPA>", CGPA )

print(New_Data)
print()

#Question3

print("Q3")
#a = 56
#b = 10
a = 0b111000
b = 0b1010
print()

#Q3a
print("Q3a")
print(bin(a&b))
print()

#Q3b
print("Q3b")
print(bin(a|b))
print()

#Q3c
print("Q3c")
print(a^b)
print()

#Q3d
print("Q3d")
print(bin(a<<2)) #shifting a
print(bin(b<<2)) #shifting b
print()

#Q3e
print("Q3e")
print(bin(a>>2)) #shfting a right by 2 bits
print(bin(b>>4)) # Shifting b right by 4 bits
print()

#Q4
print("Q4")
number_1 = int(input("Enter First number:"))
number_2 = int(input("Enter Second number:"))
number_3 = int(input("Enter third number:"))

if(number_1>number_2):
    if(number_1>number_3):
        print(number_1," i.e. First Number is greatest.")
    else:
        print(number_3," i.e. Third Number is greatest.")
else:
    if(number_2>number_3):
        print(number_2," i.e. Second Number is greatest.")
    else:
        print(number_3," i.e. Third Number is greatest.")
print()

#Q5

print("Q5")
print("Is 'name' present in the sentence?")
line1 = input("Enter the sentence here: ")
if("name" in line1):
    print("Yes")
else:
    print("No")
print()

#Q6

print("Q6")
print("Is a Triangles with these lengths possible?")
length_1 = int(input("Enter First Side length:"))
length_2 = int(input("Enter Second Side length:"))
length_3 = int(input("Enter Third Side Length:"))

if(length_1 + length_2 > length_3 and length_2 + length_3 > length_1 and length_1 + length_3 > length_2):
    print("Yes")
else:
    print("No")

print("****************************************************************END*********************************************************************************************")