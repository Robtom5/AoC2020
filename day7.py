import re

with open("./Day7Input.txt") as infile:
    fileContents = infile.readlines()

RULE_REGEX = re.compile(r'(?P<desc>^\D+ \D+) bags contain ')
CONTENT_REGEX = re.compile(r'(\d+) (\D+ \D+) bag')

rules = {}

# dummyRules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags."""
# fileContents = dummyRules.split('\n')

def load_rules(rawInput):
    for raw_line in rawInput:
        key = RULE_REGEX.match(raw_line)['desc']
        raw_contents = CONTENT_REGEX.findall(raw_line)
        contents = [(int(num), col) for num, col in raw_contents]
        rules[key] = contents

load_rules(fileContents)

TARGET = 'shiny gold'

def load_contents(bagColor):
    nestedBags = rules[bagColor]
    if nestedBags:
        nestedContent = []
        for number, color in nestedBags:
            nestedContent += number * [color]
            nestedContent += number * load_contents(color)
        return nestedContent
    else:
        return []

def find_color(bagColor):
    nestedBags = rules[bagColor]
    if nestedBags:
        containsTarget = False
        for number, color in nestedBags:
            if color == TARGET:
                return True
            else:
                containsTarget |= find_color(color)
        return containsTarget
    else:
        return False

# print(rules['light plum'])

# print(find_color('dim brown'))

total_with_target = 0

for key in rules:
    if (find_color(key)):
        total_with_target += 1

print(f"Total containing gold: {total_with_target}")

print(f"Total inside gold: {len(load_contents(TARGET))}")
