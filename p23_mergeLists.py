# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

ListNode.__lt__ = lambda a, b: a.val < b.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 定义一个小顶堆，存储每个链表的第一个节点和节点值
        import heapq

        q = []

        heapq.heapify(q)
        for node in lists:
            if node:
                # 将节点的值和节点本身作为元组加入堆中
                heapq.heappush(q, (node, node.val))

        # 定义头节点和尾节点
        head = ListNode(0)
        tail = head

        # 循环直到堆为空
        while q:
            # 弹出堆顶元素
            node, val = heapq.heappop(q)
            # 将弹出的节点的下一个节点作为尾节点的下一个节点
            tail.next = node
            # 将尾节点指向下一个节点
            tail = tail.next

            # 如果弹出的节点的下一个节点不为空，则将其加入堆中
            if node.next:
                # 将节点的值和节点本身作为元组加入堆中
                # q.append((node[1].next.val, node[1].next))
                heapq.heappush(q, (node.next, node.next.val))

        return head.next