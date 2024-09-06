class Solution: 
    def plusOne(self, digits:List[int]) -> List[int]:
        number = ''
        for i in range(0, len(digits)): 
            number += str(digits[i])

        number = int(number)+1
        number = [number]

        return list(map(int, str(number[0])))
