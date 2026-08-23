class Solution:
    def decodeString(self, s: str) -> str:
        num_stack=[]
        str_stack=[]

        for i in range(len(s)):
            if i>0 and s[i].isdigit() and s[i-1].isdigit():
                x=num_stack.pop() *10 +int(s[i])
                num_stack.append(x)

            elif i>0 and s[i].isdigit() and not s[i-1].isdigit():
                num_stack.append(int(s[i]))

            elif i==0 and s[i].isdigit():
                num_stack.append(int(s[i]))

            elif s[i]!="]":
                str_stack.append(s[i])
            elif s[i]=="]":
                c=""
                while str_stack[-1]!="[":
                    a=str_stack.pop()
                    c="".join([a,c])
                str_stack.pop()
                if len(num_stack)!=0:
                    n=num_stack.pop()
                str_stack.append(n*c)
        b=""
        for a in str_stack:
            b="".join([b,a])
        return b



        