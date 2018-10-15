(def workspace1 1 2)
(def workspace2 2 3)
(bernoulli 0.5 0) ; Deciding NP or VP
(clear 0 0)
(if 0 
    ; if NP
    (do (bernoulli 0.5 0) ; Deciding D of NP
        (uniform 3 workspace1))  ; Deciding N of NP
    ; if VP
    (do (bernoulli 0.5 0) ; Deciding V,AP or V,NP
        (clear 0 0)
        (if 0
            ; if V,AP
            (bernoulli 0.5 0) ; Deciding V of V,AP
            ; if V,NP
            (do (bernoulli 0.5 0)  ; Deciding V of V, NP
                (bernoulli 0.5 1)  ; Deciding D of NP
                (uniform 3 workspace2))))) ; Deciding N of NP
