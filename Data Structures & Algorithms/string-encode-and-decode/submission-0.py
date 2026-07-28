from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            # Format: [length] + [#] + [string]
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        output = []
        i = 0
        
        while i < len(s):
            # 1. Find the delimiter '#' to figure out where the number ends
            j = i
            while s[j] != "#":
                j += 1
            
            # 2. Extract the length of the upcoming word
            length = int(s[i:j])
            
            # 3. Extract the word using the length
            word = s[j + 1 : j + 1 + length]
            output.append(word)
            
            # 4. Move the pointer to the start of the next chunk
            i = j + 1 + length
            
        return output


            
