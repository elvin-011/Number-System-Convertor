import math
import os
import sys
print("NUMBER SYSTEM CONVERTOR")
hex2 = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
hex1 = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
while True:
    num1 = int(input("Choose the number of conversion:\n1:Decimal to Binary \n2:Decimal to Octal \n3:Decimal to Hexadecimal \n4:Octal to Decimal \n5:Hexadecimal to Decimal \n6:Binary to Decimal \n7:Octal to Binary \n8:Hexadecimal to Binary \n9:Binary to Octal \n10:Binary to Hexadecimal \n11:Octal to Hexadecimal \n12:Hexadecimal to Octal\n"))
    string = input("Enter the number to be converted:\n")
    if "." not in string:
        string = string+".0"
    sepernum = []
    sepernum1 = []
    i = r = d = 0
    stri = strd = ""
    s = "ABCDEF"
    number = "0123456789"

    def support(string1, num2):
        if num2 == 1 or num2 == 6 or num2 == 17 or num2 == 18 or num2 == 9 or num2 == 10:
            rad = 2
        elif num2 == 2 or num2 == 4 or num2 == 7 or num2 == 19 or num2 == 11 or num2 == 22:
            rad = 8
        elif num2 == 3 or num2 == 5 or num2 == 8 or num2 == 20 or num2 == 21 or num2 == 12:
            rad = 16
        else:
            print("Wrong input")
        sepernum = str(string1).split('.')
        inti = sepernum[0]
        deci = sepernum[1]
        return rad, inti, deci

    def DtoBOH(string1, n):
        stri = strd = ""
        r, i, d = support(string1, n)
        d = "."+d
        dl = len(d)
        if dl < 5:
            dl = 5
        d = float(d)
        i = int(i)
        b = True
        while b:
            rem = i % r
            # print(rem)
            if rem >= 10:
                rem = hex1[str(rem)]
            stri = str(rem)+stri

            i = i//r
            if i < r:
                b = False
        if not i == 0:
            stri = str(i)+stri

        for k in range(0, dl):
            d = d*r
            sepernum1 = str(d).split('.')
            i = int(sepernum1[0])
            d = str(sepernum1[1])
            d = "."+d
            d = float(d)
            if i >= 10:
                i = hex1[str(i)]
            strd = strd+str(i)
        finalstr = stri+"."+strd
        return(finalstr)

    # DtoBOH()

    def OHBtoD(string1, n):
        numi = numd = numf = 0
        r, i, d = support(string1, n)

        il = len(i)
        dl = len(d)
        j = il-1

        for k in range(0, il):
            if i[k] in s:
                alpha = int(hex2[i[k]])
            elif i[k] in number:
                alpha = int(i[k])
            else:
                print("Wrong input")
            numi = alpha*(pow(r, j))+numi

            j -= 1

        for k in range(0, dl):
            if d[k] in s:
                dalpha = int(hex2[d[k]])

            elif d[k] in number:
                dalpha = int(d[k])
            else:
                print("Wrong input")
            numd = dalpha*(pow(r, -(k+1)))+numd

        numf = numi+numd
        return(numf)

    # OHBtoD()

    def OHtoB(string1, n):
        num1 = n
        strd = OHBtoD(string, num1)
        strh = DtoBOH(strd, num1+10)
        return strh

    # OHtoB()

    def main():
        if num1 <= 3:
            finalstr = str(DtoBOH(string, num1))
        elif num1 <= 6:
            finalstr = str(OHBtoD(string, num1))
        elif num1 <= 12:
            finalstr = str(OHtoB(string, num1))
        else:
            print("Wrong input")
        if ".00000" in finalstr:
            finalstr = finalstr.split('.')[0]
        print(finalstr)

    main()
    inp = input("Do you want to check other number Press Y or N\n").lower()
    if inp == "y":
        os.system('cls')
        continue
    elif inp == "n":
        sys.exit()
