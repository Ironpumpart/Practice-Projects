#maximum average subarray
def maximum_average(array, k):
    current_sum = sum(array[:k])
    max_sum = current_sum
    for i in range(k, len(array)):
        current_sum = current_sum + array[i] - array[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum / k

x = [1,12,-5,-6,50,3]
k = 4
print(maximum_average(x,k))

#function to reverse a string of words and remove multipe, leading, or trailing spaces.
#reverse words in a string
def reverse_words(string):
    word = string.strip().split()
    reversed_words = word[::-1]
    return ' '.join(reversed_words)

print(reverse_words('It is raining  outside carry an umbrella '))

def reverse_word_manual(s):
    result = []
    length = len(s)
    i = length - 1
    while i >= 0:
        while i >= 0 and s[i] == ' ':
            i -= 1
        if i < 0:
            break
        word_end = i
        while i >= 0 and s[i] != ' ':
            i -= 1
        word_start = i + 1
        result.append(s[word_start:word_end + 1])
    return ' '.join(result)
print(reverse_word_manual('this step is unecessarily long'))
# to return a boolean for a test to see if elements in a set or dictionary occures a unique number of times
# unique number of occurence
def test_unique_count(array):
    occurrence_dict = {}
    for num in array:
        if num in occurrence_dict:
            occurrence_dict[num] += 1
        else:
            occurrence_dict[num] = 1
    unique_count = set()
    for count in occurrence_dict.values():
        if count in unique_count:
            return False
        unique_count.add(count)
    return True
print(test_unique_count([1,2,2,1,1,3]))

#to find a possible triple in ascending order
#kth largest element in an array
def is_there_a_triple(arr):
    first = float('inf')
    second = float('inf')
    for num in arr:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False

print(is_there_a_triple([0,4,3,2,1,6]))

#valid palindrome 
def is_palindrome(s):
    filtered_word = ''.join([char.lower() for char in s if char.isalnum()])
    return filtered_word == filtered_word[::-1]

print(is_palindrome('race car'))

#maximum sim sunarray
def max_sum(nums):
    current_sum = 0
    max_sum = float('-inf')
    for i in nums:
        if i < 0:
            current_sum = 0
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum 

y = [2,-1,4,-4,8,9]
print(max_sum(y))
