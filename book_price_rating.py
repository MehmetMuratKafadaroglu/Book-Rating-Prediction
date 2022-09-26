from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#This programme predicts books rating between 1-5 with the price of it
class BookRegression():
    def __init__(self):
        self.csv = pd.read_csv("./data/books_scraped.csv")
        self.ratings = np.array([self.rating_to_int(rating) for rating in self.csv['Star_rating']])
        self.prices  = np.array(self.csv['Price'])
        self.model = linear_model.LinearRegression()
        self.categories  = self.csv['Book_category']
        self.model.fit([[i] for i in self.prices], self.ratings )

    @staticmethod
    def rating_to_int(rating):
        if rating == "One":
            return 1
        if rating == "Two":
            return 2
        if rating == "Three":
            return 3
        if rating == "Four":
            return 4
        if rating == "Five":
            return 5
        return ValueError("Rating should be between 1-5")

    def show(self):
        plt.plot(self.prices, self.ratings, 'o')
        m, b = np.polyfit(self.prices, self.ratings, 1)
        plt.plot(self.prices, m*self.prices+b, color='red')
        plt.show()

    def get_by_rating(self, rating):
        return [i for i in self.matrix if i[1] == rating]

if __name__ == "__main__":
     
    m = BookRegression()
    print(len(set(m.categories)))
    """while (i:= input("Please enter book price: ")) != "exit":
        
        i = int(i)
        print("Rating of the book is probably: ", str(m.model.predict([[i]])[0]) )"""
