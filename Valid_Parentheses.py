class Solution(object):
    def isValid(self, s):
        dic = {')': '(', ']': '[', '}': '{'}
        
        rls = []
        for br in s:
            if br in dic.values():
                rls.append(br)
            if br in dic.keys():
                if not rls or rls.pop() != dic[br]:
                    return False
    
        return len(rls) == 0
        