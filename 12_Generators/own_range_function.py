# Lets create out own range function

class my_range:
    
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return my_range_interator(self)

class my_range_interator:

    def __init__(self,iterable_obj):
        self.iterable = iterable_obj
        # self.current = self.range_obj.start
    
    def __iter__(self):
        return self    
    
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
           raise StopIteration

        current = self.iterable.start
        self.iterable.start += 1
        return current  

# x= my_range(1,11)
for i in my_range(1,10):
    print(i)