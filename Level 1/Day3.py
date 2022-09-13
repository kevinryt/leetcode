class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def transform_to_int_list(self, link_list):
        int_list = []
        if link_list.val == None:
            return int_list
        
        while(link_list.next!= None):
            int_list.append(link_list.val)
            link_list = link_list.next
            
        int_list.append(link_list.val)
        return int_list
    
    def transform_to_link_list(self, int_list):
        link_list = ListNode(1)
        current = link_list
        for i in range(len(int_list)-1):
            current.val = int_list[i]
            current.next = ListNode(i+2)
            current = current.next
        current.val = int_list[-1]
        return link_list
        
    def mergeTwoLists_with_fuc(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        int_list1 = self.transform_to_int_list(list1)
        int_list2 = self.transform_to_int_list(list2)
        int_list = int_list1 + int_list2
        int_list = sorted(int_list)
        if len(int_list) ==  0:
            link_list = ListNode(1)
            link_list.val = None
            return link_list
        else:
            return self.transform_to_link_list(int_list)

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next
    
    def reverseList_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            cur = head
            if head.next:
                cur = self.reverseList(head.next)
                head.next.next = head
            cur.next = None
            return cur
        else:
            return None

    def reverseList_loop(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current, previous = head, None
        
        while(current):
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return current