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
