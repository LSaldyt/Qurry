(def start 0)
(def blocka 1 2)
(def blockb 1 2 classical)
(def blockc 3 4 quantum)

(x start)
(multinomial 0.02 0.96 0.02 blocka)



D(eterminer): (uniform 'the' 'a')
N(oun): (uniform 'chef' 'omelet' 'soup')
V(erb): (uniform 'cooks' 'works')
A(dverb): (uniform 'diligently')
AP(Adverb Phrase): (uniform A)
NP(Noun Phrase): (D, N)
VP(Verb Phrase): (uniform (V AP) (V NP))
S(entence): (NP, VP)


