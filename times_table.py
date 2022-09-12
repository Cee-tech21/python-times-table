some_nums = [2, 3, 4, 5]
times_table = [[], [], [], []]
index = 0
for num in some_nums:
    
    for i in range(1, 6):
        print(f"{num} * {i} =", i * num)
        times_table[index].append(i * num)
    index += 1
    print("\n")

print(times_table[3])

### Output

#5 * 1 = 5
#5 * 2 = 10
#5 * 3 = 15
#5 * 4 = 20
#5 * 5 = 25


#[[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

