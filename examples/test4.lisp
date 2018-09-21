(def workspace 1 2)
(bernoulli 0.5 0)
(clear 0 0)
(if 0 
    (do (bernoulli 0.5 0)
        (uniform 3 workspace))
    (nop))
