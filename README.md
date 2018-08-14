# Curry 

Curry is a prototype of a quantum probabilistic programming language, done with the [unitary fund](unitary.fund).
The official project duration is one year, but the language may be usable before then (and in fact, can already be used to use all of the QUIL spec).

This project has resumed!

Currently the name "Curry" is up for debate. I have other ideas, and I'm open to suggestions. However, Curry is both an incredible food and comes from Haskell Curry. It also respects the naming of the "Church" programming language.

Essentially, this project aims to allow people to build probabilistic models and run them on a quantum computer without using raw assembly instructions. 
Instead, the goal is to build common quantum random primitives and distributions that can be used to compose larger probabilistic structures, without referencing raw quantum computer instructions whatsoever (or at least, unless doing so was desired).
The current implementation uses a python "compiler", but this is just for quick prototyping and integration with `pyquil`. In the future, this project may be embedded in Clojure (the world's greatest programming language) or the compiler may be written in a faster programming language.
There are plans to integrate this with other language APIs.

Robert Tucci has also done very interesting work on quantum bayesian nets, and his work is worth checking out [here](https://github.com/artiste-qb-net/quantum-fog).
