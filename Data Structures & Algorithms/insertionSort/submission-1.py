# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        # first one always as is
        ans = [pairs]
        # to go through each iteration
        for i in range(1, len(pairs)):
            curr_list = ans[i - 1].copy()
            insert_pair = curr_list[i]
            for j in range(i):
                if insert_pair.key < curr_list[j].key:
                    # insert to the left of curr_list[j]
                    curr_list.pop(i)
                    curr_list.insert(j, insert_pair)
                    break
            ans.append(curr_list)
        return ans


