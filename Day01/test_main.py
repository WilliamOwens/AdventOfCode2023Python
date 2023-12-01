from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    _secondInput = readFile("test_input2.txt")
    assert solution(_input, False) == 142
    print("Passed Day 01 Part 1")
    assert solution(_secondInput, True) == 281
    print("Passed Day 01 Part 2")

if __name__ == "__main__":
    test()