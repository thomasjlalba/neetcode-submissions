func checkInclusion(s1 string, s2 string) bool {
	// get char count of s1
    hm := make(map[byte]int)
    for _, c := range s1 {
        hm[byte(c)]++
    }
    lp := 0
    for rp := 0; rp < len(s2); rp++ {
        // should rp not be in hm, then claw back lp until it is so or no more
        _, exists := hm[s2[rp]]
        for ;!exists && lp < rp; lp++ {
            hm[s2[lp]]++
            _, exists = hm[s2[rp]]
        }
        _, exists = hm[s2[rp]]
        if exists {
            hm[s2[rp]]--
            if hm[s2[rp]] == 0 {
                delete(hm, s2[rp])
            }
        } else {
            lp++
        }

        if len(hm) == 0 {
            return true
        }
    }
    return false
}
