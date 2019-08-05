(datatype entanglion
          (a qubit)
          (b qubit)
          (c (block 2 qubit)))

(define e (entanglion))
(x e.a)
(x e.b)
(cnot e.c)

(datatype supertanglion
          (a entanglion))

(define d (supertanglion a e))
