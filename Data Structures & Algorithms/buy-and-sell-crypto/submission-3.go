func maxProfit(prices []int) int {
    maxP, lp, rp := 0, 0, 1
    for ;rp < len(prices);rp++ {
        if prices[lp] > prices[rp] {
            lp = rp
        } else {
            maxP = max(maxP, prices[rp] - prices[lp])
        }
    }
    return maxP
}
