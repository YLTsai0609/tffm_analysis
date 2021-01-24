from sklearn.feature_extraction import DictVectorizer
import numpy as np


def load_movielens(filename, path="dataset/ml-100k/"):
    data = []
    y = []
    users = set()
    items = set()
    with open(path + filename) as f:
        for line in f:
            (user, movieid, rating, ts) = line.split('\t')
            data.append({"user_id": str(user), "movie_id": str(movieid)})
            y.append(float(rating))
            users.add(user)
            items.add(movieid)

    return (data, np.array(y), users, items)


class Movielens:
    def __init__(self, path: str, filename: str) -> None:
        self.path = path
        self.filename = filename
        self.x, self.y, self.users, self.items = load_movielens(
            filename, path=path)


# train_data, list user_id, item_id pair
# [{'user_id': '1', 'movie_id': '1'}, {'user_id': '1', 'movie_id': '2'}, {'user_id': '1', 'movie_id': '3'}, {'user_id': '1', 'movie_id': '4'}, {'user_id': '1', 'movie_id': '5'}]

# y_train, list, item rating

# train_users : set user_id
# train_items : set item_id
if __name__ == "__main__":
    train_data, y_train, train_users, train_items = load_movielens("ua.base")
    test_data, y_test, test_users, test_items = load_movielens("ua.test")
    v = DictVectorizer()

    X_train = v.fit_transform(train_data)
    X_test = v.transform(test_data)

    y_train.shape += (1,)

    # print(train_data.shape)
    print(y_train[:5])
    print(train_users[:5])
