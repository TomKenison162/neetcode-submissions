class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortedAnagrams ={}
        index = -1

        final_array = []
        for i in range(len(strs)):
    
            current = sortedAnagrams.get(''.join(sorted(strs[i])), -1)
  
            if current == -1:
                index +=1
                sortedAnagrams[''.join(sorted(strs[i]))] = index
                final_array.append([strs[i]])
                
            else:
                final_array[current].append(strs[i])
        return final_array
                

        