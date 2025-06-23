class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        temp = ""

        for c in s:
            if len(temp) == k:
                res.append(temp)
                temp = ""
            temp += c
        
        while temp and len(temp) < k:
            temp += fill
        
        res.append(temp)

        return res
        
