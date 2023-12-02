from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution(_input) == 142
    print("Passed Day 02 Part 1")
    assert solution(_input) == 281
    print("Passed Day 02 Part 2")

if __name__ == "__main__":
    test()