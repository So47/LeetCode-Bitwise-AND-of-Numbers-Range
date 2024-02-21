class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # i = 0

        # while left != right:
        #     left >>= 1
        #     right >>= 1
        #     i+=1
        # return left << i 

        # iteratively turning off the rightmost set bit in right until it is no longer greater than left
        while left < right:
            right &= (right-1)
        
        return right & left    

        
