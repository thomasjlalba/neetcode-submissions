func groupAnagrams(strs []string) [][]string {
    sortedMap := make(map[string][]string)
    ans := [][]string{}
    for _, str := range strs {
        // sort the strings
        runes := []rune(str)
        sort.Slice(runes, func(i, j int) bool {
            return runes[i] < runes[j]
        })
        sortedMap[string(runes)] = append(sortedMap[string(runes)], str)
    }
    // return ans as a list
    for _, list := range sortedMap {
        ans = append(ans, list)
    }
    return ans
}
