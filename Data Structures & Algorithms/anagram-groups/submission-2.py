class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ret = []
    used_indices = set()
    for i in range(len(strs)):
        if i not in used_indices:
            word = strs[i]
            pairs = [word]
            used_indices.add(i)
            for j in range(i + 1, len(strs)):
                compare = strs[j]
                if sorted(word) == sorted(compare):
                    pairs.append(compare)
                    used_indices.add(j)
            ret.append(pairs)
    return ret