class Solution:
    def shiftingLetters(self, s: str, query: List[List[int]]) -> str:
        N = len(s)
        line = [0 for _ in range(N+1)]
        
        for [l, r, val] in query:
            #decrement
            if val == 0:
                line[l] += -1
                line[r+1] += 1
            #increment
            else:
                line[l] += 1
                line[r+1] -= 1
        
        prefix_sum_line = 0
        new_s = ''
        for i in range(N):
            prefix_sum_line += line[i]
            #add total update to old letter to get new letter
            new_letter = (((ord(s[i]) + prefix_sum_line) - ord('a')) % 26) + ord('a')
            new_s += chr(new_letter)
        
        return new_s