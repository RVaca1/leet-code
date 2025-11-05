def max_subarray(nums):
    # Initialize
    current_sum = 0
    max_sum = float('-inf') # smallest n


    for num in nums:
        # either extend or start again the subarray
        current_sum = max(num, current_sum + num)

        #         Index	num	current_sum = max(num, current_sum + num)	max_sum = max(max_sum, current_sum)
        # 0	-2	max(-2, 0 + -2) = -2	max(-inf, -2) = -2
        # 1	1	max(1, -2 + 1) = 1	max(-2, 1) = 1
        # 2	-3	max(-3, 1 + -3) = -2	max(1, -2) = 1
        # 3	4	max(4, -2 + 4) = 4	max(1, 4) = 4
        # 4	-1	max(-1, 4 + -1) = 3	max(4, 3) = 4
        # 5	2	max(2, 3 + 2) = 5	max(4, 5) = 5
        # 6	1	max(1, 5 + 1) = 6	max(5, 6) = 6
        # 7	-5	max(-5, 6 + -5) = 1	max(6, 1) = 6
        # 8	4	max(4, 1 + 4) = 5	max(6, 5) = 6

        max_sum = max(max_sum, current_sum)

    return max_sum



input_sample = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# should output 6

print(max_subarray(input_sample))



