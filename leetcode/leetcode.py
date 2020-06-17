class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def isPalindrome(head):
    printList(head)
    reverse = reverseList(head)
    printList(head)
    while head!=None:
        if head.val==reverse.val:
            head=head.next
            reverse=reverse.next
        else:
            return False
    return True




def printList(head):
    while head!=None:
        print(head.val)
        head=head.next

def reverseList(head):
    prev = None
    current = head
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head


a=ListNode(1)
a2=ListNode(2,ListNode(1))
a.next=a2
a0=ListNode(1, a)
#printList(a0)
b=isPalindrome(a0)
print(b)

