class Node(object):
    """定义节点，指向元素和下一个节点的内存"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkedList(object):
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return (self.__head is None)

    def append(self, item):
        node = Node(item)

        if self.is_empty():
            """__head指向第一个节点"""
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            """有2个以上节点"""
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            # node.next = cur.next
            # cur.next = node

    def length(self):
        """cur游标"""
        cur = self.__head
        if self.is_empty():
            return 0
        else:
            count = 1
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        """遍历"""
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.elem, end=' ')
                cur = cur.next
            print(cur.elem)

    def add(self, item):
        """插入表头"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head
            # cur.next = node

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
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur.next != self.__head:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
            if cur.elem == item:
                return True
            return False

    def remove(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        prior = None
        # 此条件无法处理尾部结点，需要单独考虑
        while cur.next is not self.__head:
            if cur.elem == item:
                # 当删除的是头结点，需要找尾部结点
                if cur == self.__head:
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    # rear.next = cur.next
                    self.__head = cur.next
                    rear.next = self.__head
                # 中间结点
                else:
                    prior.next = cur.next
                return True
            else:
                prior = cur
                cur = cur.next
        # 尾部结点
        if cur.elem == item:
            if cur == self.__head:
                self.__head = None
            else:
                prior.next = cur.next
            return True
            # # 只有一个结点
            # if prior:
            #     prior.next = cur.next
            # else:
            #     self.__head = None


if __name__ == '__main__':
    scll = SingleCycleLinkedList()
    print(scll.is_empty())
    print(scll.length())

    scll.append(1)
    scll.append(2)
    scll.append(3)

    print(scll.is_empty())
    print(scll.length())
    scll.travel()

    scll.insert(0, 9)
    scll.travel()

    scll.add(7)
    scll.insert(0, 8)
    scll.travel()
    scll.append(4)
    scll.append(5)
    scll.travel()
    print(scll.search(3))
    print(scll.remove(1))
    scll.travel()
