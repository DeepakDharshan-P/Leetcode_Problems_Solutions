# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq


        dummy = ListNode(0)
        tail = dummy

        heap = []

        # Put first node of every list into heap
        for i in range(len(lists)):

            if lists[i] is not None:

                heapq.heappush(
                    heap,
                    (lists[i].val, i, lists[i])
                )

        # Continue until heap becomes empty
        while heap:

            # Get smallest node
            value, i, node = heapq.heappop(heap)

            # Attach node to result
            tail.next = node
            tail = tail.next

            # Put next node into heap
            if node.next is not None:

                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next

