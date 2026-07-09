func groupAnagrams(strs []string) [][]string {
	hashMap := make(map[[26]int][]string) // key: array of size 26, 
	for _, str := range strs {
		arr := [26]int{}
		// bucket sort characters in str
		for _, c := range str {
			arr[c - 'a']++
		}
		// add to hashmap
		hashMap[arr] = append(hashMap[arr], str)
	}
	// return all values as ans
	ans := [][]string{}
	for _, val := range hashMap {
		ans = append(ans, val)
	}
	return ans
}
