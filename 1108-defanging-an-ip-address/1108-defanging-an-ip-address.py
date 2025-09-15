class Solution:
    def defangIPaddr(self, address: str) -> str:
        # for a in address:
        #     if a == '.':
        #         a.replace()
        

        return address.replace('.', '[.]')