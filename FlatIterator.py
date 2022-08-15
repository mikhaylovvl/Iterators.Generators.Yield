class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.cursor = -1
        self.iter = 0
        self.iter2 = -1
        return self

    def __next__(self):
        self.cursor += 1
        self.iter2 += 1

        if self.cursor < len(self.nested_list[self.iter]):
            return self.nested_list[self.iter][self.iter2]
        else:
            self.iter += 1
            if self.iter == len(self.nested_list):
                raise StopIteration
            self.cursor = 0
            self.iter2 = 0
            return self.nested_list[self.iter][self.iter2]
