def multiplication_table(rows: int, cols: int):
    table = []
    for i in range(1, rows + 1):
        row = []
        for j in range(1, cols + 1):
            row.append(i*j)
        table.append(row)
    return table

print(multiplication_table(5,5))
print(multiplication_table(5,2))
#Output: [[1,2,3,4,5], [2,4,6,8,10], [3,6,9,12,15], 
#[4,8,12,16,20], [5,10,15,20,25]]
#Output: [[1,2], [2,4], [3,6], [4,8], [5,10]]

def merge_sorted_lists(list1, list2):
    #Merges two sorted lists into a single sorted list
    merged = []
    i, j = 0, 0
    
    #Traverse both lists and append the smaller element to
    #the merged list.
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
        
        #Append any remaining elements to the list
    while i < len(list1):
        merged.append(list1[i])
        i += 1
        
    while j < len(list2):
        merged.append(list2[j])
        j += 1
        
    return merged

list1 = [2,4,8]
list2 = [3,5]
print(merge_sorted_lists(list1, list2))
#Output: [2,3,4,5,8]

def sum_diagonal(matrix):
    n = len(matrix)
    main_diagonal_sum = 0
    anti_diagonal_sum = 0
    
    for i in range(n):
        main_diagonal_sum += matrix[i][i]
        anti_diagonal_sum += matrix[i][n - 1 - i]
    return main_diagonal_sum + anti_diagonal_sum

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(sum_diagonal(matrix))
#Output: 1 + 5 + 9 + 3 + 5 + 7 = 30

def first_occurence(nums: list, target: int):
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1

nums = [1,3,4,7,8]
target = 7
print(first_occurence(nums, target))

nums1 = [2,2,2,3]
target = 4
print(first_occurence(nums1, target))
#Output: 3
#Output: -1
