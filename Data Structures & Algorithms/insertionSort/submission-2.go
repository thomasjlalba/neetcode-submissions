// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func insertionSort(pairs []Pair) [][]Pair {
    ans := [][]Pair{}

    for i := 0; i < len(pairs); i++ {
        for j := i - 1; j >= 0; j-- {
            if pairs[j + 1].Key < pairs[j].Key {
                // swap
                tmp := pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = tmp
            } else {
                break
            }
        }
        clone := make([]Pair, len(pairs))
        copy(clone, pairs)
        ans = append(ans, clone)
    }
    return ans
}
