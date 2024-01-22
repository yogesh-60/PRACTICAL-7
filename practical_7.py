file=open("practical-7.txt",'w')
string=input("string:")
reverse=string[::-1]
if(reverse==string):
    file.write(string)
    file.write('\n')
    file.write("it is a palindrome")
    
else:
    file.write("it is not a palindrome")