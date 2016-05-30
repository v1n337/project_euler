import time

number_of_paths = 0
global_cache = dict()


class LatticePoint(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.number_of_paths = 0

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not ((self.x, self.y) == (other.x, other.y))

    def __repr__(self):
        return "x-" + str(self.x) + " | y-" + str(self.y)

    def get_lattice_path(self):

        if self in global_cache:
            self.number_of_paths = global_cache[self]
            # print "read from global cache"
            return

        if self.x + self.y == 1:
            global number_of_paths
            number_of_paths += 1
            self.number_of_paths = 1
            # print "number_of_paths incremented to ", number_of_paths
        else:
            if(self.y != 0):
                lattice_point = LatticePoint(self.x, self.y - 1)
                lattice_point.get_lattice_path()
                self.number_of_paths = \
                    self.number_of_paths + lattice_point.number_of_paths
            if(self.x != 0):
                lattice_point = LatticePoint(self.x - 1, self.y)
                lattice_point.get_lattice_path()
                self.number_of_paths = \
                    self.number_of_paths + lattice_point.number_of_paths
        global_cache[self] = self.number_of_paths

start_time = time.time()
start_lattice_point = LatticePoint(20, 20)
start_lattice_point.get_lattice_path()
print start_lattice_point.number_of_paths, "paths found"
# print global_cache

print "it took ", int(time.time() - start_time), "seconds"
