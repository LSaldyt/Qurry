# Brainstorm for a Probabilistic Quantum Programming Language

Modern quantum programming, despite its progress, is still esoteric to the average programmer. 
In general, programming languages offer a midway point between a person's mental model and literal machine instructions.
So, the question to be resolved is: How do most programmers model algorithms, and what intermediates can make it easier to turn mental models into code?

There are two main goals for providing abstractions in quantum programming:
 - Allow novices to more quickly create useful and interesting models
 - Allow experienced programmers to create models more efficiently, so that they can focus on more important design aspects

Previous attempts at designing quantum programming languages can give insights for the design of new ones:
First, there are circuit languages, which provide no abstraction, but are useful for interfacing with normal languages or compiling into.
Circuit languages are also adequate for those who are already experienced with quantum programming.
Second, there are the quantum-annealing family of languages, which can actually provide abstraction, but limit the scope of solvable problems.
Third, there are existing attempts at higher-level universal gate languages.

I'll chose one example from each class:
 - Most of the circuit languages are more or less equivalent. They allow a basic gate set (H, CNOT, etc) and measurement. Rigetti pyquil offers hybrid instructions, which makes it a slight step above previous circuit languages. Essentially, this class of languages is for expressing raw quantum circuits in code, while intentionally electing not to offer abstractions. This class of languages will be useful to compile into.
 - QA-Prolog: A quantum-annealer compiler for a subset of prolog. It is similar to a lot of other quantum annealing languages. Essentially, users can express problems in a very similar format to how problems are expressed classically, but users can only express a restricted subset of problems. Quantum annealers have their uses, but, generally speaking, they are not as powerful or general as gate-model computers. The abstraction offered, however, is work mimicking.
 - Robert Tucci's work ("Quantum Fog", "Qubiter"): Tucci's work offers modeling of bayesian networks on quantum computers, and is an interesting sister project to this one. I think that this is moving in the correct direction, by balancing usefulness with expressivity.

 Considering each of the above, I believe that there is an interesting gap to be filled: That of a language which offers lightweight abstractions, but still allows the general power of quantum computing.
Of course, this is a big goal, and likely one that will only be partially fulfilled.
I believe that it's better to attempt making something, even just a prototype of a prototype, because this will allow us to learn how to design quantum programming languages of the future.
I'm reminded of the history of the C programming language: Dennis Ritchie's and Brian Kernighan's C is the basis for a large part of modern software. 
However, before it, there was B and BCPL, as well as languages before that.
The goal of this project is to write the precursor to one of these languages: I'd like to create minimal abstractions that allow for easier modeling.

There are some easy targets for providing abstraction: common things like functions, conditionals, loops, integer data types, and so on. 
However, let's jump into the quantum/probabilistic side of things.

Models will fundamentally be composed of, generally, wave functions: Superpositions over all possible states.
First, consider modeling a classical distribution. 
We can successfully produce sampleable classical distributions on a quantum computer.
For instance, consider the following model from the Church programming language tutorial (a probabilistic context-free grammar):

```scheme
(define (transition nonterminal)
  (case nonterminal
        (('D) (multinomial(list (list (terminal 'the))
                                (list (terminal 'a)))
                          (list (/ 1 2) (/ 1 2))))
        (('N) (multinomial (list (list (terminal 'chef))
                                 (list (terminal 'soup))
                                 (list (terminal 'omelet)))
                           (list (/ 1 3) (/ 1 3) (/ 1 3))))
        (('V) (multinomial (list (list (terminal 'cooks))
                                 (list (terminal 'works)))
                           (list (/ 1 2) (/ 1 2))))
        (('A) (multinomial (list (list (terminal 'diligently)))
                           (list (/ 1 1))))
        (('AP) (multinomial (list (list 'A))
                            (list (/ 1 1))))
        (('NP) (multinomial (list (list 'D 'N))
                            (list (/ 1 1))))
        (('VP) (multinomial (list (list 'V 'AP)
                                  (list 'V 'NP))
                            (list (/ 1 2) (/ 1 2))))
        (('S) (multinomial (list (list 'NP 'VP))
                           (list (/ 1 1))))
        (else 'error)))
```

More succinctly, this is specifying the following (toy) language model:
```scheme
D(eterminer): (uniform 'the' 'a')
N(oun): (uniform 'chef' 'omelet' 'soup')
V(erb): (uniform 'cooks' 'works')
A(dverb): (uniform 'diligently')
AP(Adverb Phrase): (uniform A)
NP(Noun Phrase): (D, N)
VP(Verb Phrase): (uniform (V AP) (V NP))
S(entence): (NP, VP)
```

We can model this in curry using similar multinomial distributions and local classical mappings.
To make things even simpler, let's first just consider modeling a randomly sampled Noun-Phrase (which is the first part in sampling a full toy sentence).
The noun-phrase is a concatenation of a determiner and a noun. In our toy example, we have two determiners and three nouns, both uniformly sampled, which makes for a total of six options with equal probability.
So, we'll need three qubits to model this. Curry has builtins for these distributions.
```scheme
(def determiner-qubit 0)
(def noun-qubits 1 2)
(bernoulli 0.5 determiner-qubit)
(multinomial 0.33 0.33 0.34 noun-qubits)
```

The output is the following (using a local simulator):
```
grid {curry}: ./compile examples/test.lisp

[['def', 'determiner-qubit', '0'],
 ['def', 'noun-qubits', '1', '2'],
 ['bernoulli', '0.5', 'determiner-qubit'],
 ['multinomial', '0.33', '0.33', '0.34', 'noun-qubits']]

{'000': 0.17, '001': 0.16, '010': 0.17, '011': 0.17, '100': 0.16, '101': 0.16}

277.4035930633545 ms simulated runtime
```

In our output, the rightmost bit is representing the determiner, and the other two bits are representing the noun.
So the output is (sic):
```python3
{'the chef' : 1/6, 'a chef' : 1/6, 'the omelet' : 1/6, 'a omelet' : 1/6, 'the soup' : 1/6, 'a soup' : 1/6}
```
Curry contains functionality to decode what these bits mean, but I will explain this in detail later.

Now, let's consider the rest of the model.
When we sample a Verb Phrase, it contains recursive elements.
So, it will branch (with equal probabilities) to either (V AP) or (V NP).
Before diving in, let's look at branching in quantum computers.

Consider preparing a bell state:
```
(h 0)
(cnot 0 1)
```
And distinguish this from the following, which will produce the same classical measurements, but no entanglement (because the state of the first qubit is known before producing the state in the second qubit). 
In this case, the state 01 is possible, because the first qubit may be measured in the 1 state, and the second qubit is unprepared, and in the zero state.
```
(bernoulli 0.5 0)
(measure 0 0)
(if 0 (x 1) (nop))
```

So, when creating a probabilistic model which branches, we distinguish between these two types of branching, because only one truly creates an entangled state.
However, this makes representing information slightly more difficult, because we will not know which bits correspond to which states (unless we encode this, which we will).

First, consider an example that produces the probability distribution:
`[1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/8, 1/8, 1/12, 1/12, 1/12]`.
We can produce this by a simple:
```scheme
(def space 0 3)
(multinomial 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/8, 1/8, 1/12, 1/12, 1/12 space)
```
But obviously this requires computing the distribution in advance.
Another possibility is the following:
```
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
```

Still, there's a better way:

```
```
