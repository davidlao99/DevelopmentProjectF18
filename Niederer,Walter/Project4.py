import itertools

# NUM_TO_READ = 100, 23 kb
# 200, 27kb
# 300, 31kb, sorted up to 500 lines
# 400, 32kb, sorted up to 500 lines
# 500, same as aboce

NUM_TO_READ = 425
ARRAY_SIZE = 8500


def merge_sort(in_list, left, right):
    if left < right:
        mid = (left + (right - 1)) // 2
        merge_sort(in_list, left, mid)
        merge_sort(in_list, mid + 1, right)
        merge(in_list, left, mid, right)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * int(n1)
    R = [0] * int(n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_arrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0

    # Traverse both array
    while i < n1 and j < n2:

        # Check if current element
        # of first array is smaller
        # than current element of
        # second array. If yes,
        # store first array element
        # and increment first array
        # index. Otherwise do same
        # with second array
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1

    # Store remaining elements
    # of first array
    while i < n1:
        arr3[k] = arr1[i];
        k = k + 1
        i = i + 1

    # Store remaining elements
    # of second array
    while j < n2:
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1

def read_ints(filename, start, end):
    divided_list = []
    with open(filename) as int_file:
        for line in itertools.islice(int_file, start, end):
            divided_list.append(int(line.rstrip()))
        int_file.close()

    return divided_list


def write_ints(filename, list_to_write):
    with open(filename, "w+") as write_file:
        for num in list_to_write:
            write_file.write(str(num) + "\n")
        write_file.close()


def write_ints_append(filename, list_to_write):
    with open(filename, "a+") as write_file:
        for num in list_to_write:
            write_file.write(str(num) + "\n")
        write_file.close()


def merge_files(files):
    # iterate through all the files
    buffer = []
    total_nums = 0
    nums_total = 0
    for i in range(0, len(files)):
        for file in files:
            for num in read_ints(file, i * 25, (i + 1) * 25):
                print(i)
                if len(buffer) < 500:
                    buffer.append(num)
                    total_nums += 1

                # i = 1 by this point...probably why 500 elems are dropped
                else:
                    merge_sort(buffer, 0, len(buffer) - 1)
                    print(len(buffer))
                    file_biggest_int = read_ints("output.txt", (i) * 499, (i) * 500)

                    print(len(file_biggest_int))
                    if len(file_biggest_int) == 0:
                        write_ints_append("output.txt", buffer)
                        buffer.clear()
                    print(file_biggest_int)

                    if buffer[0] > file_biggest_int[0]:
                        write_ints_append("output.txt", buffer)
                        buffer.clear()

                    else:
                        print(i)
                        array_2 = read_ints("output.txt", (i) * 500, (i + 1) * 500)
                        print(array_2)
                        print(len(array_2))
                        print(len(buffer))
                        merge_arrays(buffer, array_2, len(buffer), 500)
                        buffer.clear()

        # print("Length of buffer: " + str(len(buffer)))

    print("Total ints processed in else: " + str(nums_total))
    print("Total ints processed in if: " + str(total_nums))
    is_sorted("output.txt")


def is_sorted(filename):
    sorted_array = []
    with open(filename) as int_file:
        for line in int_file:
            sorted_array.append(int(line.rstrip()))
        int_file.close()

    if all(sorted_array[i] <= sorted_array[i + 1] for i in range(len(sorted_array) - 1)):
        print("File is sorted")
    else:
        print("File is not sorted")



# print(divided_list)
# divided_list = read_ints("randomInts.txt", 10, 10)
# print(divided_list)
# write_ints("test.txt", divided_list)


file_list = []
for i in range(0, ARRAY_SIZE // NUM_TO_READ):
    divided_list = read_ints("randomInts.txt", i * NUM_TO_READ, (i + 1) * NUM_TO_READ)
    merge_sort(divided_list, 0, len(divided_list) - 1)
    write_ints("test" + str(i + 1) + ".txt", divided_list)
    file_list.append("test" + str(i + 1) + ".txt")
    # print("Iteration: " + str(i))


# divided_file = []
# buffer_file = []
# total_nums = 0
# num_to_read_from_file = NUM_TO_READ // len(file_list)
# for i in range(0, len(file_list) + 1):
#     for file in file_list:
#         for x in read_ints(file, i * num_to_read_from_file, (i + 1) * num_to_read_from_file):
#             if len(buffer_file) <= 500:
#                 buffer_file.append(x)
#             else:
#                 merge_sort(buffer_file, 0, len(buffer_file) - 1)
#                 write_ints_append("output.txt", buffer_file)
#                 buffer_file.clear()
#
#         print(len(buffer_file))

merge_files(file_list)
is_sorted("output.txt")

        # if len(buffer_file) >= 500:

