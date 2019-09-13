; Shows off entanglement through higher-order functions

(define control (block 6 qubit))
(define work    (block 5 qubit))
(define control2 (block 3 qubit))

(map H control)
(CNU control work X 13)

(map H control2)
(cascadeU control2 X 20)
