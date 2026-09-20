func minEatingSpeed(piles []int, h int) int {
    l, r:= 1, 1
    for _, pile := range piles {
        r = max(r, pile)
    }

    for l < r {
        mid := l + (r - l) / 2

        count := 0
        for _, pile := range piles {
            count += int(math.Ceil(float64(pile) / float64(mid)))
        }
        if count > h {
            l = mid + 1
        } else {
            r = mid
        }
    }
    return l
}
