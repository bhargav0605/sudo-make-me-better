class Solution:
    def checkAnagram(self, f_str: str, s_str: str) -> bool:
        return sorted(f_str) == sorted(s_str)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = set() 
        answers = []
        for index, value in enumerate(strs):
            if index in visited:
                continue
            visited.add(index)
            temp_ans = [value]
            for j in range(index + 1, len(strs)):
                if j not in visited:
                    if len(value) == len(strs[j]):
                        if self.checkAnagram(value, strs[j]):
                            visited.add(j)
                            temp_ans.append(strs[j])
            answers.append(temp_ans)
        return answers