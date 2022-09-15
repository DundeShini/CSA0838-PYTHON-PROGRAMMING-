def delchar(s,c):
    if len(c)==1:
        for i in range(len(s)):
            if c not in s[i]:
                print(s[i])
            else:
                continue
string= input("enter the string = ")
char = input("enter the character to be deleted = ")
delchar(string,char)
