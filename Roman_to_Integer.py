class Solution(object):
    def romanToInt(self, s):
        roma = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        re = 0
        for i in range(0,(len(s)-1)):
            if roma[s[i]] < roma[s[i+1]]:
                re = re - roma[s[i]]
            else:
                re = re + roma[s[i]]
        re = re + roma[s[-1]]

        return re


        