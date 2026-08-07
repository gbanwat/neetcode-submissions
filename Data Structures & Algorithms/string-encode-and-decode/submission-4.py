class Solution:

    def encode(self, strs: List[str]) -> str:
        a=""
        for s in strs:
            a+=str(len(s))+"#"+s
        return a

    def decode(self, s: str) -> List[str]:
        i=0
        str_list=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            str_list.append(s[j+1:(j+1+int(s[i:j]))])
            i=j+1+int(s[i:j])
        return str_list

                





            

                
                
