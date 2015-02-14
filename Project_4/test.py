#!/usr/bin/env python
# Tests the relevant functions

from World import World

# Create World
w = World(90)

# Add Some Variables and Values
w.addVar('A', 30)
w.addVar('B', 35)
w.addVar('C', 30)
w.addVar('D', 70)
w.addVar('E', 40)

w.addValue('q', 38)
w.addValue('r', 70)
w.addValue('s', 40)

# Add Constraints
w.addBinE('A', 'B')
w.addBinNE('C', 'D')
w.addBinS('A','E','r','s')

# Add Assignments and Test as we go
# When Empty
assert w.checkUnaryI(), 'UnaryI Fail when empty'
assert w.checkUnaryE(), 'UnaryE Fail when empty'
assert w.checkBinE(), 'BinE Fail when empty'
assert w.checkBinNE(), 'BinNE Fail when empty'
assert w.checkBinS(), 'BinS Fail when empty'
# No Conflicts
w.addAssignment('A', 'q')
w.addAssignment('B', 'q')
w.addAssignment('C', 'q')
w.addAssignment('D', 'r')
w.addAssignment('E', 's')
assert w.checkMinCapacity(), 'MinCapacity Should have passed'
assert not w.checkMaxCapacity(), 'MaxCapacity Should have Failed'
assert w.checkUnaryI(), 'UnaryI Fail at First Round of Assignment'
assert w.checkUnaryE(), 'UnaryE Fail at First Round of Assignment'
assert w.checkBinE(), 'BinE Fail at First Round of Assignment'
assert w.checkBinNE(), 'BinNE Fail at First Round of Assignment'
assert w.checkBinS(), 'BinS Fail at First Round of Assignment'
# Remove Assignment and add Conlicting Ones
# Remove
w.removeAssignment('A')
w.removeAssignment('B')
w.removeAssignment('C')
w.removeAssignment('D')
w.removeAssignment('E')
# Add and Test
w.addAssignment('A', 'r')
w.addAssignment('B', 'q')
w.addAssignment('C', 'r')
w.addAssignment('D', 'r')
w.addAssignment('E', 's')
assert not w.checkBinE(), 'BinE Did not Fail at Conflicting Round'
assert not w.checkBinNE(), 'BinNE Did not Fail at Conflicting Round'
assert not w.checkBinS(), 'BinS Did not Fail at Conflicting Round'




