type MinStack struct {
    mins []int
    stack []int
}

func Constructor() MinStack {
    return MinStack{
        mins: make([]int, 0),
        stack: make([]int, 0),
    }
}

func (this *MinStack) Push(val int) {
    this.stack = append(this.stack, val)
    if len(this.mins) == 0 || this.mins[len(this.mins) - 1] >= val {
        this.mins = append(this.mins, val)
    }
}

func (this *MinStack) Pop() {
    if (this.mins[len(this.mins) - 1] == this.stack[len(this.stack) - 1]) {
        this.mins = this.mins[:len(this.mins) - 1]
    }
    this.stack = this.stack[:len(this.stack) - 1]
}

func (this *MinStack) Top() int {
    return this.stack[len(this.stack) - 1]
}

func (this *MinStack) GetMin() int {
    return this.mins[len(this.mins) - 1]
}
