from z3 import Int, Real, Optimize, sat, solve, simplify, And

x = Real('x')
y = Real('y')
solve(x>2, y<9)
