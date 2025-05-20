class Counter:
    pass
    count = 0
    def __init__(self):
        pass
        Counter.count += 1
    
    @classmethod
    def show_count(cls):
        pass
        print(f"Total objects created : {cls.count}")

if __name__ == "__main__":
    pass
    obj1 = Counter()
    obj1 = Counter()
    obj1 = Counter()
    Counter.show_count()
