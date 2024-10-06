# OPTION 2 - IMPLEMENT STACK
# DO NOT SHARE

# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values

from typing import Optional

class IntStack:
    def __init__(self) -> None:
        self.stack = InternalStack()
    def push(self, value: int) -> None:
        self.stack = InternalStack(value, self.stack)
    def pop(self) -> int:
        if self.stack.value is None:
            raise Exception("Tried to pop from empty stack")
        value, self.stack = self.stack.value, self.stack.rest
        return value
    def peek(self) -> int:
        if self.stack.value is None:
            raise Exception("Tried to peek in empty stack")
        return self.stack.value
    def size(self) -> int:
        return self.stack.size

class InternalStack:
    def __init__(self, value: Optional[int] = None, rest: Optional["InternalStack"] = None) -> None:
        self.value = value
        self.size = 0 if rest is None else rest.size + 1
        self.rest = rest
