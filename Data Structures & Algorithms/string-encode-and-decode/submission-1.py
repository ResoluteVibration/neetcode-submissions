class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = [str(len(i)) for i in strs]
        encoded=""
        for i, j in zip(strs,lens):
            encoded+="#"+j+"#"
            for ch in i:
                encoded = encoded + str(ord(ch))+","
        # print(f"Encoded: {encoded}")
        return encoded

        
    def decode(self, s: str) -> List[str]:
        words = []
        parts = s.split("#")
        for i in range(1, len(parts), 2):
            length = parts[i]
            # print(length)
            asci = parts[i+1].split(",")
            # print(asci)
            word = "".join(chr(int(i)) for i in asci if i)
            words.append(word)
        return words
