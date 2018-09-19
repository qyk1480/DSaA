class Node(object):
    """定义节点，指向元素和下一个节点的内存"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkedList(object):
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
        self.__head = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            prior = self.__head

            count = 0
            while count < (pos-1):
                prior = prior.next
                count += 1
            node.next = prior.next
            prior.next = node

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
        prior = None

        while cur is not None:
            if cur.elem == item:
                # 当删除的是头结点，包含只有一个结点
                # if prior is None:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    prior.next = cur.next
                return True
            else:
                prior = cur
                cur = cur.next
        return False


if __name__ == '__main__':
    sll = SingleLinkedList()
    print(sll.is_empty())
    print(sll.length())

    sll.append(1)
    sll.append(2)
    sll.append(3)

    print(sll.is_empty())
    print(sll.length())
    sll.travel()

    sll.insert(0, 9)
    sll.travel()

    sll.add(7)
    sll.insert(0, 8)
    sll.travel()
    sll.append(4)
    sll.append(5)
    sll.travel()
    print(sll.search(3))
    print(sll.remove(1))
    sll.travel()
