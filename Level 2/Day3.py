class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        fast, slow = head, head

        for i in range(n):
            fast = fast.next

        if not fast:
            return slow.next

        while(fast.next):
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head

class Solution(object):
    def isPalindrome_list(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        while (head):
            l.append(head.val)
            head = head.next  
        return l == l[::-1]

    def isPalindrome(self, head):
        fast, slow = head, head

        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        prev = None

        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True