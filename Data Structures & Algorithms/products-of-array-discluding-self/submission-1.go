func productExceptSelf(nums []int) []int {
    pre, post := make([]int, len(nums)), make([]int, len(nums))
    pre[0] = 1
    post[len(nums) - 1] = 1
    for i := 1; i < len(nums); i++ {
        pre[i] = pre[i - 1] * nums[i - 1]
        post[len(nums) - i - 1] = post[len(nums) - i] * nums[len(nums) - i]
    }
    ans := make([]int, len(nums))
    for i := 0; i< len(nums); i++ {
        ans[i] = pre[i] * post[i]
    }
    return ans
}
