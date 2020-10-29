# UPER == Understand, Plan, Execute, Reflect
"""
NOTES:

Understand - what the problem is before you try to solve it. Ask questions!
    Figure out the constraints: speed, time, money. 
    Inputs and outputs. Learn edge cases: dealing with big numbers, bugs, what input will break program? 
    This is where most of your time should be spent. Most challenging part as well. 

Plan - Planning phase (not coding yet). Can you see a brute force solution? MVP - minimum viable product. Results, not beauty.

Execute - turn pseudo-code into real code, turn your mock-ups into the real thing. Programming and coding begins. Should be simple

Reflect - Repeat, refactor, refine. If tests fail, go back to understand and plan. 


"""
"""
centered_average /// codingbat.com

Return the 'centered' average of an array of ints(integers), which we'll say is the mean average of the values, excpet ignoring the largest and smallest values in the array. If there are multiiple copies of the smallest value, ignore just one copy. and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length of 3 or more.

centered-average([1, 2, 3, 4, 100]) -> 3
centered-average([1, 1, 5, 5, 10, 8, 7]) -> 5
centered-average([-10, -4, -2, -4, -2, 0]) > -3


Understand - length of 3 or more. Sum of all the numbers. max - min. List, int division/rounding, all 6. Not sorted? Length of list -2
Plan 1 - sort the array? Remove first, remove last. Sum of all nums. Length = len(list).
Plan 2 - find min and max and remove them. (Remove is expensive, is slow for the computer to do.) or ignore using slices. Sum all of the numbers and subtracting the min and max from the total.

// 2 linkes in python mean num = 55 / 3 = 18.3333
integar division num // 3 = 18 (takes off all the decimals. Not rounding, but flooring.) Integers can not have decimals.

"""

def centered_average(nums):
#find the max number of nums
max_num = max(nums)
#find the min number
min_num = min(nums)
#get the sum of nums
current_sum = sum(nums)
#substract the max and min
final_sum = current_sum - max_num - min_num
#divide the value by the len(nums) - 2
return final_sum // (len(nums) -2)