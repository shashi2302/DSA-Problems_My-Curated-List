(brute force):
def two_sum_brute_force(nums, target):
    # For every number in our list
    for i in range(len(nums)):
        # Check every other number that comes after it
        for j in range(i + 1, len(nums)):
            # If we found a pair that adds up to our target
            if nums[i] + nums[j] == target:
                # Return their positions (indexes)
                return [i, j]
    # If no solution is found, return an empty list
    return []

# Example
nums = [2, 7, 11, 15]
target = 9
print(two_sum_brute_force(nums, target))  # Output: [0, 1] because 2 + 7 = 9

(optimized):

def two_sum_optimized(nums, target):
    # Dictionary to store numbers we've seen and their positions
    seen = {}
    
    # Go through each number in our list
    for i, num in enumerate(nums):
        # Calculate what other number we need to reach our target
        needed_number = target - num
        
        # If we've already seen that number, we found our pair!
        if needed_number in seen:
            # Return both positions
            return [seen[needed_number], i]
        
        # Otherwise, remember this number and its position
        seen[num] = i
    
    # If no solution is found, return an empty list
    return []

# Example
nums = [2, 7, 11, 15]
target = 9
print(two_sum_optimized(nums, target))  # Output: [0, 1] because 2 + 7 = 9
