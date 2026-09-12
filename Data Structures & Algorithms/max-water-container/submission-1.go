func maxArea(heights []int) int {
    lp, rp := 0, len(heights) - 1
    ans := 0
    for lp < rp {
        ans = max(ans, min(heights[lp], heights[rp]) * (rp - lp))
        if heights[lp] < heights[rp] {
            lp++
        } else {
            rp--
        }
    }
    return ans
}
