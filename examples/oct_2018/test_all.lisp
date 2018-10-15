(def start 0)
(multinomial .5 .5 start)
(if start
  (def a 1)
  (def a 0))
(x a)
(bernoulli 0.5 a)
(clear a)

(uniform 32 a)
