# Brainstorm for a Probabilistic Computing Language

In a nutshell, I'd like to make it easier for people to run real-world models on quantum computers. 
By "real-world models", I mean calculations that represent an abstract version of the real world, that can inform future actions.
However, the quantum programming language world is currently lacking one thing: Abstraction.
Most quantum programming languages simply don't offer abstraction whatsoever -- they're glorified circuit languages usually wrapped in needlessly verbose syntax.
Of course, there are important exceptions to this rule. 
One of the most interesting is QA-prolog, which I am influenced by.
QA-prolog offers a prolog interface for a quantum annealer. 
So, for instance, one can submit the map-coloring problem as they would classically, and have it solved by a quantum computer.
However, it only offers a subset of prolog, which is already a specialized language.

I just believe that it's better to attempt making something, even just a prototype of a prototype, because this will allow us to learn how to design quantum programming languages of the future.
I'm reminded of the history of the C programming language: Dennis Ritchie's and Brian Kernighan's C is the basis for a large part of modern software. 
However, before it, there was B and BCPL, as well as languages before that.
The goal of this project is to write the precursor to one of these languages: I'd like to create minimal abstractions that allow for easier modeling.

Now, I believe that the source of these abstractions can be rooted in some kind of quantum data types. 

Models will fundamentally be composed of, generally, wave functions: Superpositions over all possible states.
First, consider modeling a classical distribution. 
We can successfully produce sampleable classical distributions on a quantum computer.
For instance, consider the following model from the Church programming language tutorial (a probabilistic context-free grammar):

```scheme
(define (sample distribution) (distribution))

(define (terminal t) (lambda () t))

(define D (lambda ()
            (map sample
                 (multinomial
                  (list (list (terminal 'the) )
                        (list (terminal 'a)))
                  (list (/ 1 2) (/ 1 2))))))
(define N (lambda ()
            (map sample
                 (multinomial
                  (list (list (terminal 'chef))
                        (list (terminal 'soup))
                        (list (terminal 'omelet)))
                  (list (/ 1 3) (/ 1 3) (/ 1 3))))))
(define V (lambda ()
            (map sample
                 (multinomial
                  (list (list (terminal 'cooks))
                        (list (terminal 'works)))
                  (list (/ 1 2) (/ 1 2))))))
(define A (lambda ()
            (map sample
                 (multinomial
                  (list (list (terminal 'diligently)))
                  (list (/ 1 1))))))
(define AP (lambda ()
             (map sample
                  (multinomial
                   (list (list A))
                   (list (/ 1 1))))))
(define NP (lambda ()
             (map sample
                  (multinomial
                   (list (list D N))
                   (list (/ 1 1))))))
(define VP (lambda ()
             (map sample
                  (multinomial
                   (list (list V AP)
                         (list V NP))
                   (list (/ 1 2) (/ 1 2))))))
(define S (lambda ()
            (map sample
                 (multinomial
                  (list (list NP VP))
                  (list (/ 1 1))))))
(S)
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
To make things even simpler, let's first just consider modeling a randomly sampled Noun-Phrase.
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
