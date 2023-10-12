#MKHABELE MMM
#28/06/2023
def main():
   camelCase=input("camelCase: ")
   for i in camelCase:
         if i.isupper()==True:
             print("_"+i.lower(),end="")
         else:
             print(i,end='')
main()