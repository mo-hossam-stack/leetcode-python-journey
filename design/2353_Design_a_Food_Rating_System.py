# Problem: Design a Food Rating System
# LeetCode: https://leetcode.com/problems/design-a-food-rating-system/
# Difficulty: Medium

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cuisine = defaultdict(str)
        self.cuisine_ratings = defaultdict(SortedSet)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_cuisine[food] = (cuisine, rating)
            self.cuisine_ratings[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.food_cuisine[food]
        self.food_cuisine[food] = (cuisine, newRating)

        self.cuisine_ratings[cuisine].remove((-rating, food))
        self.cuisine_ratings[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_ratings[cuisine][0][1]
