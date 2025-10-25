# Problem: Design Movie Rental System  
# LeetCode: https://leetcode.com/problems/design-movie-rental-system/  
# Difficulty: Hard  

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(SortedList)
        self.sm_p = {}
        self.rented = SortedList()

        for s, m, p in entries:
            self.movies[m].add((p, s))
            self.sm_p[(s, m)] = p

    def search(self, movie: int) -> List[int]:
        res = []
        n = len(self.movies[movie])
        for i in range(5):
            if i == n:
                break
            res.append(self.movies[movie][i][1])
        return res

    def rent(self, shop: int, movie: int) -> None:
        p = self.sm_p[(shop, movie)]
        self.movies[movie].discard((p, shop))
        self.rented.add((p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.sm_p[(shop, movie)]
        self.movies[movie].add((p, shop))
        self.rented.discard((p, shop, movie))

    def report(self) -> List[List[int]]:
        res = []
        n = len(self.rented)
        for i in range(5):
            if i == n:
                break
            res.append([self.rented[i][1], self.rented[i][2]])  # [s, m]
        return res


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop, movie)
# obj.drop(shop, movie)
# param_4 = obj.report()