class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        max_seq_len=0

        for n in num_set:
            if  (n-1) not in num_set:
                seq_start=n
                next_element=n+1
                seq_len=1
                while next_element in num_set:
                    seq_len+=1
                    next_element+=1
                max_seq_len=max(max_seq_len,seq_len)
        return max_seq_len







        
        