class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for str in strs:
            ret += str + ":;"
        return ret
        


    def decode(self, s: str) -> List[str]:
        ret = []
        word = ""
        lastChar = ""
 
        for i, c in enumerate(s):
            if c == ":" and s[i+1] == ";":
                ret.append(word)
                word = ""
                i += 1
            if c != ";" and s[i-1] != ":":
                word += c
            lastChar = c
        return ret

