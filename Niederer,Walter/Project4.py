import itertools

# NUM_TO_READ = 100, 23 kb
# 200, 27kb
# 300, 31kb, sorted up to 500 lines
# 400, 32kb, sorted up to 500 lines
# 500, same as aboce

NUM_TO_READ = 500
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
    print("hello")

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


divided_file = []
buffer_file = []
total_nums = 0
num_to_read_from_file = NUM_TO_READ // len(file_list)
for i in range(0, len(file_list) + 1):
    for file in file_list:
        for x in read_ints(file, i * num_to_read_from_file, (i + 1) * num_to_read_from_file):
            if len(buffer_file) <= 500:
                buffer_file.append(x)
            else:
                merge_sort(buffer_file, 0, len(buffer_file) - 1)
                write_ints_append("output.txt", buffer_file)
                buffer_file.clear()

        print(len(buffer_file))

is_sorted("output.txt")

        # if len(buffer_file) >= 500:

