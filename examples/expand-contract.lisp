(define control (block 6 qubit))
(define tail    (block 2 qubit))

(collect control 6)
(cnot 6 7)
(expand  control 6)

;(simU control 6 X 7)
