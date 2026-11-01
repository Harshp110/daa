import heapq
from itertools import count


class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None


def print_codes(root, code, total):
    if root is None:
        return total

    if root.left is None and root.right is None:
        if code == "":
            code = "0"

        print(root.ch, ":", code)
        total += root.freq * len(code)
        return total

    total = print_codes(root.left, code + "0", total)
    total = print_codes(root.right, code + "1", total)
    return total


n = int(input("Enter number of characters: "))

pq = []
unique_id = count()

for i in range(n):
    ch, freq = input("Enter character and frequency: ").split()
    node = Node(ch, int(freq))
    heapq.heappush(pq, (node.freq, next(unique_id), node))

while len(pq) > 1:
    left = heapq.heappop(pq)[2]
    right = heapq.heappop(pq)[2]

    parent = Node("-", left.freq + right.freq)
    parent.left = left
    parent.right = right

    heapq.heappush(pq, (parent.freq, next(unique_id), parent))

print("Huffman Codes:")
total_bits = print_codes(pq[0][2], "", 0)
print("Total Bits Required:", total_bits)
