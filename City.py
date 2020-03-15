import numpy as np
from scipy.spatial import distance

class City:
    
    def __init__(self, _x: float, _y: float):
        self.x = _x
        self.y = _y
        self.name = None

    def __repr__(self):
        return 'City({}, {}, {})'.format(self.name, self.x, self.y)
    
    def distance_to(self, next_city: 'City'):
        u = [self.x, self.y]
        v = [next_city.x, next_city.y]
        return distance.euclidean(u, v)
    
    @staticmethod
    def get_random_city():
        random_x, random_y = np.random.uniform(0.0, 10000.0, 2)
        random_city = City(random_x, random_y)
        return random_city