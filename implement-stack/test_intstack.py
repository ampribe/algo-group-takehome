from option2 import IntStack

def test_init():
    stack = IntStack()
    assert stack.size() == 0

def test_push():
    stack = IntStack()
    stack.push(4)
    assert stack.peek() == 4
    assert stack.size() == 1

def test_push_and_pop():
    stack = IntStack()
    stack.push(10)
    assert stack.size() == 1
    assert stack.pop() == 10
    assert stack.size() == 0

def test_push_peek_pop_multiple():
    stack = IntStack()
    stack.push(0)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.size() == 2
    assert stack.pop() == 3
    assert stack.peek() == 0
    stack.push(15)
    stack.push(100)
    stack.push(150)
    assert stack.size() == 4
    assert stack.pop() == 150
    assert stack.size() == 3
    assert stack.pop() == 100
    assert stack.size() == 2
    assert stack.pop() == 15
    assert stack.size() == 1
    assert stack.pop() == 0
    assert stack.size() == 0
    stack.push(-1)
    assert stack.peek() == -1
    assert stack.size() == 1
