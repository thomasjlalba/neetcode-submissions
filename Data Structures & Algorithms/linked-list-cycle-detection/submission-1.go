/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
    hs := make(map[*ListNode]struct{})
    for ;head != nil ; head = head.Next {
        if _, exists := hs[head]; exists {
            return true
        }
        hs[head] = struct{}{}
    }
    return false
}
