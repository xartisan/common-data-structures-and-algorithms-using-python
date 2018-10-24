class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self._head = None
        self._size = 0

    def insert_start(self, data):
        new_node = Node(data, self._head)
        self._head = new_node
        self._size += 1

    def remove(self, data):
        dummy = Node(None, self._head)
        prev = dummy
        while prev.next_node:
            if prev.next_node.data == data:
                break
            prev = prev.next_node

        if prev.next_node is None:
            return
        prev.next_node = prev.next_node.next_node
        self._head = dummy.next_node
        self._size -= 1

    def insert_end(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            return
        cur = self._head
        while cur.next_node:
            cur = cur.next_node
        cur.next_node = new_node
        self._size += 1

    @property
    def size(self):
        return self._size

    def to_list(self):
        rv = []
        cur = self._head
        while cur:
            rv.append(cur.data)
            cur = cur.next_node
        return rv

    def __repr__(self):
        return ' -> '.join(str(i) for i in self.to_list())


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_start(1)
    print(ll)
    ll.insert_start(2)
    print(ll)
    ll.insert_start(3)
    print(ll)
    ll.insert_end(4)
    ll.insert_start(10)
    print(ll)
    ll.remove(1)
    print(ll)
    ll.remove(10)
    print(ll)
    ll.remove(3)
    print(ll)
    print(ll.size)
