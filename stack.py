# -*- coding: utf-8 -*-
# https://www.codeeval.com/open_challenges/9/
import sys

class Stack():
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def is_empty(self):
        return len(self.elements) == 0

def is_integer(s):
    return s.isdigit() or (s.startswith('-') and s[1:].isdigit())

def parse_file(filepath):
    numbers = []
    with open(filepath) as data:
        lines = data.readlines()
        for line in lines:
            numbers.append([int(elem) for elem in line.split() if is_integer(elem)])
    return numbers

def get_prefilled_stack(numbers):
    s = Stack()
    for number in numbers:
        s.push(number)
    return s

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: %s input' % sys.argv[0]
        sys.exit()

    filepath = sys.argv[1]

    numbers = parse_file(filepath)
    for line in numbers:
        s = get_prefilled_stack(line)
        x = 0
        while not s.is_empty():
            elem = s.pop()
            if x % 2 == 0:
                print elem,
            x += 1
        print ''
