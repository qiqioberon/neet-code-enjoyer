class MyHashMap:

    def __init__(self):
        self.array = []

    def put(self, key: int, value: int) -> None:
        if self.array:
            first_val = [array[0] for array in self.array]
            if key in first_val:
                for array in self.array:
                    if key == array[0]:
                        array[1] = value
            else:
                self.array.append([key, value])
        else:
            self.array.append([key, value])
        

    def get(self, key: int) -> int:
        if self.array:
            first_val = [array[0] for array in self.array]
            print(first_val)
            if key in first_val:
                for array in self.array:
                    if key == array[0]:
                        return array[1]
            else:
                return -1
        else:
            return -1

    def remove(self, key: int) -> None:
        if self.array:
            first_val = [array[0] for array in self.array]
            if key in first_val:
                for array in self.array:
                    if key == array[0]:
                        self.array.remove([key, array[1]])
