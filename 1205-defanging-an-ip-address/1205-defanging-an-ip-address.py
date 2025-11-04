class Solution(object):
    def defangIPaddr(self, address):
        s = ''
        l = address.split('.')
        print(l)
        for i in address:
            if i.isdigit():
                s+=str(i)
            else:
                s+='[.]'            
            
        return s
        