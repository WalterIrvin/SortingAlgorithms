def bubblesort(arr):
    sorted = True
    new_array = []
    for i in range(len(arr)):
        new_array.append(arr[i])

    for x in range(len(new_array)):
        for y in range(len(new_array)):
            if x != y:
                if new_array[x] < new_array[y]:
                    tmp = new_array[x]
                    new_array[x] = new_array[y]
                    new_array[y] = tmp
                    sorted = False
        if sorted:
            break
    return new_array


def main():
    test_array = [4, 7, 1, 3, 5, 6]
    final = bubblesort(test_array)
    print("begin:", test_array, "final:", final)


main()
