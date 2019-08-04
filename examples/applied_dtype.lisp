(datatype entanglion
          (a qubit)
          (b qubit)
          (c (block 2 qubit)))

(define e (entanglion 0 0))
(x e.a)
(x e.b)
(cnot e.c)
