class UnionFind:
    def __init__(self, n):
        """
        Initializes the Union-Find structure with n elements.
        Each element is initially in its own set.
        """
        self.parent = list(range(n))  # parent[i] stores the parent of element i
        self.rank = [0] * n          # rank[i] stores the rank (height) of the tree rooted at i

    def find(self, i):
        """
        Finds the representative (root) of the set containing element i.
        Uses path compression for optimization.
        """
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i, j):
        """
        Merges the sets containing elements i and j.
        Uses union by rank for optimization.
        Returns True if a union occurred, False otherwise (already in same set).
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False
        # Union by rank: attach the smaller rank tree under the root of the larger rank tree
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_j] < self.rank[root_i]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        return True

    def connected(self, i, j):
        """
        Checks if elements i and j are in the same set.
        """
        return self.find(i) == self.find(j)
