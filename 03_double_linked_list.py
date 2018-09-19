class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return (self.__head is None)

    def append(self, item):
        node = Node(item)

        if self.is_empty():
            """__head指向第一个节点"""
            self.__head = node
        else:
            cur = self.__head
            """有2个以上节点"""
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def length(self):
        """cur游标"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        """插入表头"""
        node = Node(item)
        node.next = self.__head
        # self.__head.prev = node
        self.__head = node
        node.next.prev = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head

            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def search(self, item):
        cur = self.__head
        count = 0

        while count < self.length():
            if cur.elem == item:
                return count

            else:
                cur = cur.next
                count += 1
        return False

        # cur = self.__head
        # while cur is not None:
        #     if cur.elem == item:
        #         return True
        #     else:
        #         cur = cur.next
        # return False

    def remove(self, item):
        cur = self.__head

        while cur is not None:
            if cur.elem == item:
                # 当删除的是头结点
                # if prior is None:
                if cur == self.__head:
                    self.__head = cur.next
                    # 只有一个结点
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    # 删除的是尾部结点
                    if cur.next:
                        cur.next.prev = cur.prev
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    dll = DoubleLinkedList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    dll.append(2)
    dll.append(3)

    print(dll.is_empty())
    print(dll.length())
    dll.travel()

    dll.insert(0, 9)
    dll.travel()

    dll.add(7)
    dll.insert(0, 8)
    dll.travel()
    dll.append(4)
    dll.append(5)
    dll.travel()
    print(dll.search(3))
    print(dll.remove(1))
    dll.travel()
