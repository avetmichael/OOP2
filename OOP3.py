import random
import math


class matrix():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.arr = []
        for i in range(a):
            self.arr.append([])
            for j in range(b):
                self.arr[-1].append(random.randint(-20, 20))


ob = matrix(4, 4)


class Solution():
    def __init__(self, ob):
        self.ob = ob

    def ex_432(self):
        a = 0
        n = len(self.ob.arr)
        for i in range(0, n):
            for j in range(0, n - i):
                if (i + j) % 2 == 1:
                    a = a + (self.ob.arr[i][j] ** 2)
                z = math.sqrt(a)
        return z
###############
    def ex_435(self):
        a = 0
        n = len(self.ob.arr)
        for i in range(0, n - 1):
            for j in range(0, n - 1 - i):
                if int(self.ob.arr[i][j]) % 5 == 0:
                    a = a + 1
        return a

############
    def ex_436(self):
        a = 0
        b = 0
        n = len(self.ob.arr)
        for i in range(1, n):
            for j in range(0, i):
                if -7 <= self.ob.arr[i][j] and self.ob.arr[i][j] <= 3:
                    a = a + self.ob.arr[i][j]
                    b = b + 1
        return a / b
############
    def ex_439(self):
        a = 1
        n = len(self.ob.arr)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if (i + j) % 2 == 1:
                    a = a * self.ob.arr[i][j]
        return a
#############
    def ex_440(self):
        a = 0
        n = len(self.ob.arr)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if (i + j) % 2 == 0:
                    a = a + self.ob.arr[i][j]
        return a
###############
    def ex_442(self):
        a = 0
        b = 0
        n = len(self.ob.arr)
        for i in range(0, n - 1):
            for j in range(0, n - 1 - i):
                if self.ob.arr[i][j] < 0:
                    a = a + self.ob.arr[i][j]
                    b = b + 1
        return a / b
######################
    def ex_445(self):
        a = 0
        k = 8
        n = len(self.ob.arr)
        for i in range(1, n):
            for j in range(0, i):
                if math.fabs(self.ob.arr[i][j]) > k:
                    a = a + 1
        return a
####################
    def ex_447(self):
        b = 1
        a = 9
        n = len(self.ob.arr)
        for i in range(0, n):
            for j in range(0, n - i):
                if self.ob.arr[i][j] < a:
                    b = b * self.ob.arr[i][j]
        return b
###################
    def ex_449(self):
        a = 0
        n = len(self.ob.arr)
        for i in range(0, n - 1):
            for j in range(0, n - 1 - i):
                if int(self.ob.arr[i][j]) % 4 == 0:
                    a = a + self.ob.arr[i][j]
        return a

p1 = Solution(ob)
print(p1.ex_432())
print(p1.ex_435())
print(p1.ex_436())
print(p1.ex_439())
print(p1.ex_440())
print(p1.ex_442())
print(p1.ex_445())
print(p1.ex_447())
print(p1.ex_449())