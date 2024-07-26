import sys


def mergesort(lst1, lst2):  # Sorts two lists into one sorted list (based on int val)
    combined = []
    while len(lst1) != 0 and len(lst2) != 0:   # Loops until one function is empty
        if lst1[0] < lst2[0]:
            combined.append(lst1[0])
            lst1 = lst1[1:]
        elif lst1[0] > lst2[0]:
            combined.append(lst2[0])
            lst2 = lst2[1:]

    if len(lst1) == 0:  # This if/elif statement determines which list is empty, then adds the non-empty list in
        return combined + lst2
    elif len(lst2) == 0:
        return combined + lst1


def sort(lst):
    dataset1 = lst[:len(lst) // 2]  # Will be empty when len(lst) == 0
    dataset2 = lst[len(lst) // 2:]  # When len(lst) is odd, this list will have 1 more element
    if len(dataset2) == 1:  # Because dataset2 always holds the extra, when len = 2 ds1 has either 1 or 0 elements.
        if not dataset1:    # Base case with odd numbers (dataset1 will now be empty)
            return dataset2
        elif dataset1[0] < dataset2[0]:    # These 'elif's sort the last 2 values left
            return dataset1 + dataset2
        elif dataset1[0] > dataset2[0]:
            return dataset2 + dataset1
    else:
        sorted_ds1 = sort(dataset1)
        sorted_ds2 = sort(dataset2)
    return mergesort(sorted_ds1, sorted_ds2)    # Sorts the two split lists


dataset = []
with open(sys.argv[1]) as input_file:
    for line in input_file:
        dataset.append(int(line))

sorted_ds = sort(dataset)   # Calls the sort function on the newly created dataset

with open(sys.argv[2], 'w') as output_file:
    for element in sorted_ds:
        # output_file.writelines(str(element) + '\n')
        output_file.writelines(f'{element:03d}\n')


if __name__ == "__main__":
    pass
