"""
Populate database with coding challenges for Code Battle feature
Run this script once to add challenges to production database
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartquizarena.settings')
django.setup()

from codebattle.models import Challenge

# Define coding challenges
CHALLENGES = [
    {
        "title": "Two Sum",
        "description": "Find two numbers that add up to a target",
        "problem_statement": """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].""",
        "sample_io": """Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]""",
        "test_cases": [
            {"input": {"nums": [2,7,11,15], "target": 9}, "output": [0,1]},
            {"input": {"nums": [3,2,4], "target": 6}, "output": [1,2]},
            {"input": {"nums": [3,3], "target": 6}, "output": [0,1]}
        ],
        "difficulty": "easy",
        "time_limit": 300,
        "language": "python",
        "reference_solution": """def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []"""
    },
    {
        "title": "Reverse String",
        "description": "Reverse a string in-place",
        "problem_statement": """Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]""",
        "sample_io": """Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]""",
        "test_cases": [
            {"input": {"s": ["h","e","l","l","o"]}, "output": ["o","l","l","e","h"]},
            {"input": {"s": ["H","a","n","n","a","h"]}, "output": ["h","a","n","n","a","H"]}
        ],
        "difficulty": "easy",
        "time_limit": 300,
        "language": "python",
        "reference_solution": """def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1"""
    },
    {
        "title": "Valid Palindrome",
        "description": "Check if a string is a palindrome",
        "problem_statement": """A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return true if it is a palindrome, or false otherwise.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.""",
        "sample_io": """Input: s = "A man, a plan, a canal: Panama"
Output: true

Input: s = "race a car"
Output: false""",
        "test_cases": [
            {"input": {"s": "A man, a plan, a canal: Panama"}, "output": True},
            {"input": {"s": "race a car"}, "output": False}
        ],
        "difficulty": "easy",
        "time_limit": 300,
        "language": "python",
        "reference_solution": """def isPalindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]"""
    },
    {
        "title": "FizzBuzz",
        "description": "Classic FizzBuzz problem",
        "problem_statement": """Given an integer n, return a string array answer (1-indexed) where:

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.

Example:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]""",
        "sample_io": """Input: n = 3
Output: ["1","2","Fizz"]

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]""",
        "test_cases": [
            {"input": {"n": 3}, "output": ["1","2","Fizz"]},
            {"input": {"n": 5}, "output": ["1","2","Fizz","4","Buzz"]}
        ],
        "difficulty": "easy",
        "time_limit": 300,
        "language": "python",
        "reference_solution": """def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result"""
    },
    {
        "title": "Maximum Subarray",
        "description": "Find the contiguous subarray with the largest sum",
        "problem_statement": """Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.""",
        "sample_io": """Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Input: nums = [1]
Output: 1""",
        "test_cases": [
            {"input": {"nums": [-2,1,-3,4,-1,2,1,-5,4]}, "output": 6},
            {"input": {"nums": [1]}, "output": 1}
        ],
        "difficulty": "medium",
        "time_limit": 300,
        "language": "python",
        "reference_solution": """def maxSubArray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum"""
    },
]

def populate_challenges():
    """Add challenges to the database"""
    created_count = 0
    
    for challenge_data in CHALLENGES:
        challenge, created = Challenge.objects.get_or_create(
            title=challenge_data["title"],
            defaults=challenge_data
        )
        
        if created:
            print(f"✓ Created challenge: {challenge.title}")
            created_count += 1
        else:
            print(f"- Challenge already exists: {challenge.title}")
    
    print(f"\n✅ Successfully populated {created_count} new challenges!")
    print(f"📊 Total challenges in database: {Challenge.objects.count()}")

if __name__ == "__main__":
    print("🚀 Populating database with coding challenges...\n")
    populate_challenges()
