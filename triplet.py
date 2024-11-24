# Input list and target sum
arr = [10, 20, 30, 9]
target_sum = 59

# Find the triplet
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] == target_sum:
                print(f"Triplet found: {arr[i]}, {arr[j]}, {arr[k]}")
                exit()

print("No triplet found.")

