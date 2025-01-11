my_list = [1, 2, 3]
iterrator = iter(my_list)
# print(iterrator)

# print(next(iterrator))
# print(next(iterrator))
# print(next(iterrator))

for elem in my_list:
    print(elem)

class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i
    
count = Counter(5)

# for elem in count:
#     print(elem)
print(count.__next__())
print(next(count))

def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number**i
        i+=1


res = raise_to_the_degrees(123, 50)
print(res)

for _ in res:
    print(f"res {_} \n\n\n")