#python program to create a random password genertor
import random
import string
print("welcome to our random password generator")
def main():
    
    length=int(input("enter the length of password you want:"))
    lowerD = string.ascii_lowercase 
    #print(lowerD)
    upperD = string.ascii_uppercase
    digitD=string.digits
    symbolsD=string.punctuation
    combine = upperD + lowerD + digitD + symbolsD
    x=random.sample(combine,length)
    #print(x)
    password="".join(x)
    print(password)
    main()
main()    

 