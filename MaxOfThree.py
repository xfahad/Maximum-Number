# FileName: MaxOfThree.py
# Author: xFahad
# Date: 07/15/16
# Description: This code gets 3 integers from user then displays the maximum number they entered.


def MaxNumber(nFirst, nSecond, nThird):
    if ((nFirstNum > nSecondNum) and (nFirstNum > nThirdNum)):
        return nFirstNum

    elif((nSecondNum > nFirstNum) and (nSecondNum > nThirdNum)):
        return nSecondNum

    elif((nThirdNum > nFirstNum) and (nThirdNum > nSecondNum)):
        return nThirdNum

nFirstNum = int (input('Please enter the First number:'))

nSecondNum = int(input('Please enter the Second number:'))

nThirdNum = int(input('Please enter the Third number:'))

nMax = MaxNumber(nFirstNum,nSecondNum,nThirdNum)

print('The maximum number you entered is', nMax)
