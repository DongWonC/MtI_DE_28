
# selection_sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# insertion_sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):    # 인덱스 i부터 1까지 1씩 감소하며 반복하는
        if array[j] < array[j - 1]:    # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:    # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

#