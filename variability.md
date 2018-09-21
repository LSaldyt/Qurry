I noticed the following variability.
Here's the commands I used:
```
grid {curry}: ./compile examples/clear-into.lisp 
[['x', '0'], ['clear', '0', '0'], ['if', '0', ['x', '1'], ['nop']]]
{'10': 1.0}
{'10': 1.0}
172.70612716674805 ms simulated runtime
grid {curry}: ./compile examples/clear-into.lisp 
[['x', '0'], ['clear', '0', '0'], ['if', '0', ['x', '1'], ['nop']]]
{'10': 1.0}
{'10': 1.0}
182.56211280822754 ms simulated runtime
grid {curry}: ./compile examples/clear-into.lisp 
[['x', '0'], ['clear', '0', '0'], ['if', '0', ['x', '1'], ['nop']]]
{'10': 1.0}
{'10': 1.0}
5968.996286392212 ms simulated runtime
```

And the quil code from the last run:
```
X 0
# Clearing qubit 0
MEASURE 0 [0]
JUMP-UNLESS @qubit-0-768f3acb-ac53-42c2-a424-e57e63cc88c1 [0]
X 0
LABEL @qubit-0-768f3acb-ac53-42c2-a424-e57e63cc88c1
# Conditional statement
JUMP-WHEN @first-db57095e-6661-43b6-a8fc-9a67804b3293 [0]
  NOP
JUMP @end-8451a1df-03db-4267-943c-475f68837feb
LABEL @first-db57095e-6661-43b6-a8fc-9a67804b3293
  X 1
LABEL @end-8451a1df-03db-4267-943c-475f68837feb
```
