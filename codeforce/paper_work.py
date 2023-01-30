import sys
input = sys.stdin.readline

days_number = int(input())

perf_stats = list(map(int, input().split()))


folders = []

folder_index = 0

loss_count_per_folder = 0

for i in perf_stats:

    if i < 0:
        loss_count_per_folder = loss_count_per_folder + 1

    if loss_count_per_folder > 2:
        loss_count_per_folder = 1
        folder_index = folder_index + 1

    if folder_index > len(folders)-1:
        folders.append([i])
    else:
        folders[folder_index].append(i)


print(folder_index+1)

for i in folders:
    print(len(i), end=" ")
