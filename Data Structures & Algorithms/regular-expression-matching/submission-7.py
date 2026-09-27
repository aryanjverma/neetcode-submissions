class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        l = []
        isStar = []
        for char in p:
            if char == "*":
                isStar[-1] = True
            else:
                l.append(char)
                isStar.append(False)
        
        def helper(sindex, lindex):
            if lindex == len(l):
                if sindex == len(s):
                    return True
                return False
            if sindex == len(s):
                if isStar[lindex]:
                    return helper(sindex, lindex + 1)
                return False
            if (sindex, lindex) in dp:
                return dp[(sindex, lindex)]
            
            if (l[lindex] == "."  or l[lindex] == s[sindex]) and helper(sindex + 1, lindex + 1):
                return True
            if isStar[lindex]:
                
                if (l[lindex] == "."  or l[lindex] == s[sindex]):
                    if helper(sindex + 1, lindex):
                        return True
                
                if helper(sindex, lindex + 1):
                    return True
            dp[(sindex, lindex)] = False
            return False
        return helper(0, 0)