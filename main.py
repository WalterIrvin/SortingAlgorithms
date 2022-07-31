def bubble_sort(arr):
    """O(N^2) complexity"""
    is_sorted = True
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
                    is_sorted = False
        if is_sorted:
            break
    return new_array


def insertion_sort(arr):
    """O(N^2) complexity"""
    pass


def merge_sort(arr):
    """O(nlogn) complexity"""
    pass


def quick_sort(arr):

    pass


def heap_sort(arr):
    pass


class Node:
    def __init__(self):
        self.__data = None
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_elm):
        self.__next = next_elm


class SingleLinkedList:
    def __init__(self, init_list=None):
        self.head = Node()
        for item in init_list:
            self.append_node(item)

    def set_node_data(self, idx, data):
        """Sets the node data for a particular index of the list"""
        cur = self.get_node(idx)
        cur.set_data(data)

    def get_node_data(self, idx):
        """Gets the node data for a particular index of the list"""
        cur = self.get_node(idx)
        return cur.data

    def get_head(self):
        """Returns the start of the list"""
        return self.head

    def get_tail(self):
        """Goes through entire list until the next entry is None, then returns the last valid node"""
        cur = self.head
        while cur is not None:
            if cur.get_next() is None:
                break  # found tail
            cur = cur.get_next()
        return cur

    def get_node(self, idx):
        """Gets a specified node counting up through list, if the end of list is reached first, out of bounds error"""
        count = 0
        cur = self.head
        while cur is not None:
            cur = cur.get_next()
            count += 1
            if count == idx:
                return cur
        raise UnboundLocalError("Error: Out of bounds exception")

    def append_node(self, data):
        """Adds a new node to the end of the list."""
        tail = self.get_tail()
        if tail == self.head and tail.get_data() is None:
            # special case, empty list adding initial item
            tail.set_data(data)
        else:
            new_node = Node()
            new_node.set_data(data)
            tail.set_next(new_node)

    def prepend_node(self, data):
        """Adds a new node to the beginning of the list, reattaches existing head"""
        tmp = self.head
        self.head = Node()
        self.head.set_data(data)
        self.head.set_next(tmp)

    def insert_node(self, data, idx):
        """Inserts a new node to an arbitrary location in the list, reattaches nodes accordingly"""
        if idx == 0:
            # special case: prepending
            self.prepend_node(data)
        elif idx > 0:
            cur = self.get_node(idx)
            left = self.get_node(idx-1)
            new_node = Node()
            new_node.set_data(data)
            left.set_next(new_node)
            new_node.set_next(cur)

    def delete_node(self, idx):
        """Deletes a node from an arbitrary location in the list, reattaches nodes as needed."""
        if idx == 0:
            self.head = self.head.get_next()
        elif idx > 0:
            cur = self.get_node(idx)
            left = self.get_node(idx-1)
            left.set_next(cur.get_next())

    def print_list(self):
        cur = self.head
        while cur is not None:
            if cur == self.head:
                print("[{" + str(cur.get_data()) + "}, ", end="")
            elif cur.get_next() is not None:
                print("{" + str(cur.get_data()) + "}, ", end="")
            elif cur.get_next() is None:
                print("{" + str(cur.get_data()) + "}]")
            cur = cur.get_next()


class DoubleLinkedList:
    pass


class BinaryTree:
    pass


class Heap:
    pass


class HashMap:
    pass


def single_link_tester(data):
    arr = SingleLinkedList(data)
    arr.print_list()
    arr.delete_node(3)
    arr.print_list()
    arr.insert_node(42, 5)  # will function like append
    arr.print_list()

    for i in range(42):
        arr.prepend_node(i)
    arr.print_list()

    for i in range(14):
        arr.delete_node(0)
    arr.print_list()


def main():
    test_array = [4, 7, 1, 3, 5, 6]
    single_link_tester(test_array)


main()
