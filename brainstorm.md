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
[]

Classical probabilistic languages work by creating a model, and then searching parameters within the model.
The parts about a model that are known are coded beforehand using composites of exchangable random primitives.
Quantum computing possibly assists in this process, because quantum computers are fundamentally probabilistic.
Qubits are generally the exchangable random primitives that a classical approach would use as building blocks. 
For instance, a qubit that has undergone a hadamard gate is, when measured, equivalent to a coin flip.
Multiple qubits can be used to represent an arbitrary statistical state, when the state is known beforehand.
However, there is another element here, which is entanglement.
Entanglement allows conditioning of other probabilities based on simpler probabilities.
Its classical corollary is the post-measurement if statement.

Given a quantum computer with n qubits, we can generate a multinomial sample with 2^n options in a relative number of operations.
Any other distribution can be approximated with our multinomial distribution.
Additionally, it is very easy to "cross" or join distributions, and so we can simulate a very complicated process with a smaller number of inputs and operations.
For instance, crossing two m-wide multinomial distributions can give m^2 options with O(m) operations and inputs.

Something worth considering: Quantum computers are much better at building a single measurement, rather than approximating a distribution?
We can use grover's algorithm, or a variant of it, however, to do unstructured search in O(sqrt(n)) time.

Other applications allow a speedup that changes O(2^n) to O(n). 
This is potentially more interesting, because of the nature of the speedup.
Stated casually, this speedup is possible when we have a number of probabilistically interacting parts, and we care about observing a single measurement at the end of simulation.
This is very similar to a hofstadterian cognitive architecture, or any classical agent-based system. 


Consider an existing probabilistic programming language: Church.

In church, one of my favorite models is the following:

```scheme
(define (transition nonterminal depth)
  (case nonterminal
        (('atom)      (terms '(x 1 2)))
        (('operator)  (terms '(+ *)))
        (('predicate) (terms '(odd even)))
        (('expression) (multinomial (list '(atom)
                                          '(operator expression expression))
                                    (list (/ 3 4) (/ depth 4))))
        (('repeat) (just (list (terminal- 'repeat)
                                'expression
                                'expression)))
        (('range) (just (list (terminal- 'range)
                              'expression
                              'expression)))
        (('list-literal) (multinomial (list (list (terminal- 'list)
                                                  'expression)
                                            (list
                                                  (terminal- 'append)
                                                  'list-literal
                                                  'list-literal))
                                      (list (/ 3 4) (/ depth 4))))
        (('list-literal) (multinomial (list (list (terminal- 'list)
                                                  'expression))
                                            (list (terminal- 'append)
                                                  'list-literal
                                                  'list-literal)
                                      (list (/ 3 4) (/ depth 4))))
        (('list-type) (just '(list-literal range repeat)))
        (('concat) (multinomial (list (list (terminal- 'append)
                                            'list-type)
                                      (list (terminal- 'append)
                                            'list-type
                                            'concat))
                                (list (/ 3 4) (/ depth 4))))
        (('predicate-expr) (from depth (list '((predicate expression)))))
        (('conditional) (just (list (terminal- 'if) 
                                     'predicate
                                     'high-level
                                     'high-level)))
        (('high-level) (multinomial (list '(concat) '(atom)      '(conditional))
                                    (list (/ 3 8)    (/ 3 8) (/ depth 4))))
        (else 'error)))
```

This particular example is a multinomial distribution of list descriptions in the python programming language.
Suppose we want to find the computer program that describes a piece of data.
We can find this program by running grovers search, on the condition that our code matches our data.
In this way, we find an answer in sqrt(exp(n)) time. I'm not sure if this is interesting...?

TODO: Read church tutorial

Representation of useful probabilistic models using a quantum substrate... simple enough.
