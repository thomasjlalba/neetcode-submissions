func trap(height []int) int {
    if len(height) < 3 {
        return 0
    }
    ans := 0
    lp, rp := 0, len(height) - 1
    maxL, maxR := height[lp], height[rp]
    for lp < rp {
        if maxL < maxR {
            // shift lp
            lp++
            maxL = max(maxL, height[lp])
            ans += maxL - height[lp]
        } else {
            // shift rp
            rp--
            maxR = max(maxR, height[rp])
            ans += maxR - height[rp]
        }
    }
    return ans
}
