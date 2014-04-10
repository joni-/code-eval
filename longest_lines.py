# -*- coding: utf-8 -*-
# https://www.codeeval.com/open_challenges/2/
import sys, os

def check_args():
    if len(sys.argv) != 2:
        print 'Usage: %s filepath' % sys.argv[0]
        sys.exit()

def get_longest_lines_from_file(filepath):
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    count = int(data[0]) # Number of longest lines to fetch
    lines = data[1:]
    result = sorted(lines, key=len, reverse=True)[:count]
    return result

if __name__ == '__main__':
    check_args()
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print 'Invalid path: %s' % filepath
        sys.exit()
    longest_lines = get_longest_lines_from_file(filepath)
    for line in longest_lines:
        print line
