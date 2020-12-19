class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def display(self):
        n = self
        res = []
        while n:
            res.append(str(n.val))
            n = n.next
        res.append('None')
        text = '-->'.join(res)
        print(text)

    @staticmethod
    def compare(self, other):
        if not self and not other:
            return True
        elif (self and not other) or (not self and other):
            return False
        if self.val == other.val:
            return Node.compare(self.next, other.next)
        return False

    @staticmethod
    def init_list(array):
        if not array:
            return
        head = node = Node(array[0])
        for a in array[1:]:
            node.next = Node(a)
            node = node.next
        return head

    @staticmethod
    def insert(head, val):
        new_node = Node(val) if not isinstance(val, Node) else val
        if not head:
            return new_node
        node = head
        node.next = new_node
        return head

    @staticmethod
    def search(head, val):
        while head:
            if head.val == val:
                return head
            head = head.next
        return

    @staticmethod
    def delete(head, val):
        pre_h = None
        n_head = head
        while head:
            if head.val == val:
                if pre_h:
                    Node._delete(pre_h)
                    break
            pre_h = head
            head = head.next
        return n_head

    @staticmethod
    def _delete(head):
        # 删除后继结点
        n_head = head
        if not head.next:
            n_head = None
        else:
            head.next = head.next.next
        return n_head


class DNode(Node):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


if __name__ == '__main__':
    nums = [4, 5, 7, 8]
    h = Node.init_list(nums)
    # h.display()
    Node.insert(h, 9)
    # h.display()
    Node.delete(h, 7)
    # h.display()
    n1 = Node.search(h, 5)
    # print('n1: {} val: {}'.format(n1, n1.val))

