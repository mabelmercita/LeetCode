class Solution(object):
    def defangIPaddr(self, address):
        s = ''
        for i in address:
            if i.isdigit():
                s+=str(i)
            else:
                s+='[.]'            
            
        return s
        