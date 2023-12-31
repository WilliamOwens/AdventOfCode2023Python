import os

TRANSLATION = {
   'o': [3],
   't': [3,5],
   'f': [4],
   's': [3,5],
   'e': [5],
   'n': [4],
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
   'e': [3,4,5],
   'o': [3],
   'r': [4],
   'x': [3],
   'n': [5],
   't': [5],
}

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return _input


def helper(line, position, reversed):
  if not reversed:
    for num in TRANSLATION.get(line[position]):
      if (NUM_TRANSLATION.get(line[position:(num + position)])):
        return NUM_TRANSLATION.get(line[position:(num + position)])
  else:
    for num in REV_TRANSLATION.get(line[position]):
      if ( NUM_TRANSLATION.get(line[(position + 1 - num):position + 1])):
        return NUM_TRANSLATION.get(line[(position + 1 - num):position + 1])
  return 0


def solution(calibrationDocument, useWords):
  runningTotal = 0
  for line in calibrationDocument:
    lineNumber = 0
    lookingLeft, lookingRight = True, True
    l, rev = 0, len(line) - 1

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
      if (line[rev].isnumeric()):
        lineNumber += int(line[rev])
        lookingRight = False
      # This elif block is skipped if only looking for numbers
      elif (lookingRight and useWords and REV_TRANSLATION.get(line[rev])):
        numToCheck = helper(line, rev, True)
        if (numToCheck):
          lineNumber += numToCheck
          lookingRight = False
        else:
          rev -= 1
      else:
        rev -= 1

    runningTotal += lineNumber
  return runningTotal


if __name__ == "__main__":
    _input = readFile("input.txt")
    # False only checks for numbers, True checks for words and numbers
    print(solution(_input, False))
    print(solution(_input, True))