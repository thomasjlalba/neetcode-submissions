type Node struct {
    val int
    next *Node
}

func NewNode(val int, next *Node) *Node {
    return &Node{
        val: val,
        next: next,
    }
}

type LinkedList struct {
    head *Node
    size int
}

func NewLinkedList() *LinkedList {
    return &LinkedList{nil, 0}
}

func (ll *LinkedList) Get(index int) int {
    if index >= ll.size {
        return -1
    }
    curr := ll.head
    for i := 0; i < index; i++ {
        curr = curr.next
    }
    return curr.val
}

func (ll *LinkedList) InsertHead(val int) {
    new_head := NewNode(val, ll.head)
    ll.head = new_head
    ll.size++    
}

func (ll *LinkedList) InsertTail(val int) {
    if ll.size == 0 {
        ll.head = NewNode(val, nil)
        ll.size++
        return
    }
    curr := ll.head
    for i := 1; i < ll.size; i++ {
        curr = curr.next
    }
    curr.next = NewNode(val, nil)
    ll.size++
}

func (ll *LinkedList) Remove(index int) bool {
    if index >= ll.size {
        return false
    }
    if index == 0 {
        ll.head = ll.head.next
        ll.size--
        return true
    }
    new_head := ll.head
    curr := new_head
    old := ll.head
    for i := 1; i < index; i++ {
        curr = curr.next
        old = old.next
    }
    old = old.next
    curr.next = old.next
    ll.head = new_head
    ll.size--
    return true
}

func (ll *LinkedList) GetValues() []int {
    ans := []int{}
    curr := ll.head
    for i := 0; i < ll.size; i++ {
        ans = append(ans, curr.val)
        curr = curr.next
    }
    return ans
}
