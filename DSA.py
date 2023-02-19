# Problem 1
#Validating Subsequence of array
# First solution(using while loop)
# def ValidateSubSequence(array, sequence):
#     arrayindex=0
#     sequenceindex=0
#     while arrayindex < len(array) and  sequenceindex < len(sequence):
#         if sequence[sequenceindex] == array[arrayindex]:
#             sequenceindex += 1
#         arrayindex +=1
#     return sequenceindex == len(sequence)

# # 2nd Solution(using for loop)
# def isValidSubsequence(array, sequence):
#     sequenceinedx = 0
#     for items in array:
#         if sequenceinedx == len(sequence):
#             break
#         if items == sequence[sequenceinedx]:
#             sequenceinedx +=1
#     if sequenceinedx == len(sequence):
#         return True
#     return False

################################################################
            

        