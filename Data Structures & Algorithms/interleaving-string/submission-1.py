class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        failed = set()
        def helper(i, j):
            if (i, j) in failed:
                return False
            if i + j >= len(s3):
                return True
            if i < len(s1):
                if s1[i] == s3[i + j]:
                    if helper(i + 1, j):
                        return True
                    failed.add((i + 1,j))
            if j < len(s2):
                if s2[j] == s3[i + j]:
                    if helper(i, j + 1):
                        return True
                    failed.add((i,j + 1))
            failed.add((i,j))
            return False
        return helper(0, 0)