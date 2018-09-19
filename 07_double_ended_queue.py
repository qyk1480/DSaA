class DoubleEndedQueue(object):
    """2个栈的合并"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)

    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return (self.__list == [])

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    deq = DoubleEndedQueue()
    print(deq.is_empty())
    deq.add_front(1)
    deq.add_rear(2)
    deq.add_front(3)
    deq.add_rear(4)
    print(deq.size())

    print(deq.pop_rear())
    print(deq.pop_front())
    print(deq.pop_front())
    print(deq.pop_front())
    print(deq.size())
