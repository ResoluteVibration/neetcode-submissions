class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "".join(
            f"#{len(word)}#" + ",".join(str(ord(ch)) for ch in word) + ","
            for word in strs
        )
        return encoded

        
    def decode(self, s: str) -> List[str]:
        parts = s.split("#")
        decoded = [
            "".join(chr(int(code)) for code in parts[i + 1].split(",") if code)
            for i in range(1, len(parts), 2)
        ]
        return decoded
