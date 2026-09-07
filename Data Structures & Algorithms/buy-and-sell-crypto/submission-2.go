func maxProfit(prices []int) int {
    smallest := 101
    maxP := 0
    for _, price := range prices {
        if smallest > price {
            smallest = price
        } else {
            maxP = max(maxP, price - smallest)
        }
    }
    return maxP
}
