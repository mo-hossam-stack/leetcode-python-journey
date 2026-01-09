# Problem: All O`one Data Structure
# LeetCode: https://leetcode.com/problems/all-oone-data-structure/
# Difficulty: Hard

class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def append(self, node: Node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        self.size += 1

    def append_after(self, before : Node, node: Node):
        after = before.next
        before.next = node
        node.prev = before

        node.next = after
        after.prev = node
        self.size += 1

    def remove(self, node : Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        # del node
        self.size -= 1

class AllOne:

    def __init__(self):
        self.freq_map = defaultdict(lambda : DLL())
        self.freq = defaultdict(int)
        self.min_key = 0
        self.max_key = 0
        self.cache = {}


    def inc(self, key: str) -> None:
        self.freq[key] += 1
        if self.freq[key] == 1: 
            node = Node(key, -1)
            self.cache[key] = node
            self.freq_map[1].append(node)
            self.min_key = 1
            self.max_key = max(self.max_key, 1)
            self.freq
        else:
            node = self.cache[key]
            self.freq_map[self.freq[key] - 1].remove(node)
            self.freq_map[self.freq[key]].append(node)

            if self.min_key == self.freq[key] - 1 and self.freq_map[self.freq[key] - 1].size == 0:
                self.min_key = self.freq[key]
            self.max_key = max(self.max_key, self.freq[key])        

    def dec(self, key: str) -> None:
        self.freq[key] -= 1
        if self.freq[key] == 0: 
            node = self.cache[key]
            self.freq_map[1].remove(node)
            del self.cache[key]

            if not self.cache:
                self.min_key = 0
                self.max_key = 0
                return

            if self.freq_map[1].size == 0:

                while self.freq_map[self.min_key].size == 0:
                    self.min_key += 1
                while self.freq_map[self.max_key].size == 0:
                    self.max_key -= 1
        else:
            node = self.cache[key]
            self.freq_map[self.freq[key] + 1].remove(node)
            # if self.freq_map[self.freq[key] + 1].size == 0:
            #     del self.freq_map[self.freq[key] + 1]

            self.freq_map[self.freq[key]].append(node)

            if self.max_key == self.freq[key] + 1 and self.freq_map[self.freq[key] + 1].size == 0:
                self.max_key = self.freq[key]

            self.min_key = min(self.min_key, self.freq[key])

    def getMaxKey(self) -> str:
        # print(self.freq_map[2].head.next.key)
        # print('KEY MAX', self.max_key)
        if not self.cache: return ""
        return self.freq_map[self.max_key].head.next.key
        
    def getMinKey(self) -> str:
        if not self.cache: return ""
        # print('KEY', self.min_key)
        return self.freq_map[self.min_key].head.next.key

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

