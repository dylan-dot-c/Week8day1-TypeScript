# The Hamming Distance is a measure of similarity between two strings of equal length. Complete the function so that it returns the number of positions where the input strings do not match.

# Examples:
# a = "I like turtles"
# b = "I like turkeys"
# Result: 3

# a = "Hello World"
# b = "Hello World"
# Result: 0

# a = "espresso"
# b = "Expresso"
# Result: 2

# Notes:
# You can assume that the two inputs are ASCII strings of equal length.

def solution(string1, string2):
    count = 0
    for c in range(len(string1)):
        print("C", c)
        if string1[c] != string2[c]:
            count += 1
    return count

print(solution("apple", "app1e"))
