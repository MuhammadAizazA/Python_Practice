class Example:
    def __init__(self, value=10):
        self.val = value
        print("Initializing object", value)

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(Value={self.val})"

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        if isinstance(other, Example):
            return self.val == other.val
        return False

    def __len__(self):
        # Define the length of the object (if applicable)
        return len(str(self.val))

    def __getitem__(self, key):
        # Define behavior for indexing, e.g., obj[key]
        # Note: This example assumes self.val is iterable
        return self.val[key]

    def __setitem__(self, key, value):
        # Define behavior for assigning a value to an item, e.g., obj[key] = value
        # Note: This example assumes self.val is mutable
        self.val[key] = value

# Example usage:

obj=Example()

Example.__init__(obj,90)


example_obj = Example(42)
print(repr(example_obj))
print(str(example_obj))
print(len(example_obj))
print(example_obj[0])  # Assumes self.val is iterable
example_obj[0] = 99   # Assumes self.val is mutable

