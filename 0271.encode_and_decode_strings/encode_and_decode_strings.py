"""
Design an algorithm to encode a list of strings to a string.The encoded string is then sent over the network
and is decoded back to the original list of strings.
"""
import json
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return json.dumps(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return json.loads(s)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
