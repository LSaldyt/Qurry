(def workspace 1 2)
(bernoulli 0.5 0) ; Deciding NP or VP
(clear 0 0)
(if 0 
    ; if NP
    (do (bernoulli 0.5 0) ; Deciding D of NP
        (uniform 3 1 2))  ; Deciding N of NP
    ; if VP
    (do (bernoulli 0.5 0) ; Deciding V,AP or V,NP
        (clear 0 0)
        (if 0
            ; if V,AP
            (bernoulli 0.5 0)) ; Deciding V of V,AP
            ; if V,NP
            (do (bernoulli 0.5 0)  ; Deciding V of V, NP
                (bernoulli 0.5 1)  ; Deciding D of NP
                (uniform 3 2 3)))) ; Deciding N of NP
