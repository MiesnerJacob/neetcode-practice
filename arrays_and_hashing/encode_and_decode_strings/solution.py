from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return "\u0001".join(strs) if strs else "NONE"

    def decode(self, s: str) -> List[str]:
        return [] if s == "NONE" else s.split("\u0001")