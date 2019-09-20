;(define bell (l (a b) ((H a) (CNOT a b))))
;(bell 0 1)
(define bell (l ((H %0) (CNOT %0 %1))))
(bell 0 1)
