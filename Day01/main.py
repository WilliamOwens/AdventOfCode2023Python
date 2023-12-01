import os

TRANSLATION = {
   'o': ['one'],
   't': ['two', 'three'],
   'f': ['four', 'five'],
   's': ['six', 'seven'],
   'e': ['eight'],
   'n': ['nine'],
}

NUM_TRANSLATION = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}

REV_TRANSLATION = {
   'e': ['eno', 'eerht', 'evif', 'enin'],
   'o': ['owt'],
   'r': ['ruof'],
   'x': ['xis'],
   'n': ['neves'],
   't': ['thgie'],
}

REV_NUM_TRANSLATION = {
  'eno': 1,
  'owt': 2,
  'eerht': 3,
  'ruof': 4,
  'evif': 5,
  'xis': 6,
  'neves': 7,
  'thgie': 8,
  'enin': 9
}

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return _input


def helper(line, position, reversed):
  if not reversed:
    for num in TRANSLATION.get(line[position]):
      if (NUM_TRANSLATION.get(line[position:(len(num) + position)])):
        return NUM_TRANSLATION.get(line[position:(len(num) + position)])
  else:
    for num in REV_TRANSLATION.get(line[position]):
      if ( REV_NUM_TRANSLATION.get(line[position:(len(num) + position)])):
        return REV_NUM_TRANSLATION.get(line[position:(len(num) + position)])
  return 0


def solution(calibrationDocument, useWords):
  runningTotal = 0
  for line in calibrationDocument:
    reversedLine = line[::-1]
    lineNumber = 0
    lookingLeft, lookingRight = True, True
    l, rev = 0, 0

    while (lookingLeft):
      if (line[l].isnumeric()):
        lineNumber += int(line[l]) * 10
        lookingLeft = False
      # This elif block is skipped if only looking for numbers
      elif (lookingLeft and useWords and TRANSLATION.get(line[l])):
        numToCheck = helper(line, l, False)
        if (numToCheck):
          lineNumber += numToCheck * 10
          lookingLeft = False
        else:
          l += 1
      else:
        l += 1
    
    while (lookingRight):
      if (reversedLine[rev].isnumeric()):
        lineNumber += int(reversedLine[rev])
        lookingRight = False
      # This elif block is skipped if only looking for numbers
      elif (lookingRight and useWords and REV_TRANSLATION.get(reversedLine[rev])):
        numToCheck = helper(reversedLine, rev, True)
        if (numToCheck):
          lineNumber += numToCheck
          lookingRight = False
        else:
          rev += 1
      else:
        rev += 1

    runningTotal += lineNumber
  return runningTotal


if __name__ == "__main__":
    _input = readFile("input.txt")
    # False only checks for numbers, True checks for words and numbers
    print(solution(_input, False))
    print(solution(_input, True))