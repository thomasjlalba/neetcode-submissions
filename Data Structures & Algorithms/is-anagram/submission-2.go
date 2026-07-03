import(
    "maps"
)

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    s_map := make(map[byte]int)
    t_map := make(map[byte]int)
    for i := 0; i < len(s); i++ {
        s_map[s[i]]++
        t_map[t[i]]++
    }
    return maps.Equal(s_map, t_map)
}
