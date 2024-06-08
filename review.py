#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Review 1 - 修正了默认参数使用可变对象的问题
def add_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

# Review 2 - 改进了字符串格式化方式
def format_greeting(name, age):
    return f"Hello, my name is {name} and I am {age} years old."

# Review 3 - 修正了类实例变量与类变量混淆的问题
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Review 4 - 增加线程安全机制
import threading

class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()
threads = [threading.Thread(target=worker, args=(counter,)) for _ in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()

# Review 5 - 修正了字典计数逻辑中的赋值运算符
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


