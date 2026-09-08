func search(nums []int, target int) int {
    lp, rp := 0, len(nums) - 1
    for ;lp < rp; {
        mid := (lp + rp) / 2
        if nums[mid] == target {
            return mid
        }
        if nums[mid] < target {
            lp = mid + 1
        } else {
            rp = mid - 1
        }
    }
    if lp == rp && nums[lp] == target {
        return lp
    }
    return -1
}
