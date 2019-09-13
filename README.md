# Qurry 
[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](http://unitary.fund)  

Qurry is a prototype of a quantum probabilistic programming language, done with the [unitary fund](https://unitary.fund).
The official project duration is one year, but the language may be usable before then (and in fact, can already be used to use all of the QUIL spec with some useful abstractions on top, like if statements, variable names, and so on).

For more information on the progress of the project, see a [summary](brainstorm.md) (from early October), or an in-progress [paper](paper/paper.pdf). 

If you use Qurry or are influenced by it, all I ask is that you cite the software. A bibtex citation is available at the end of this file.
Once a paper is published, please cite that (I will update it here).

Since Qurry is currently in major rework (until `September 16th, 2019`), the instructions and description previously available on this readme have been commented out.

<!--

## Installation

Right now, Qurry can be cloned locally and run from this directory:

```bash
git clone https://github.com/LSaldyt/qurry
cd qurry
./compile examples/bell.lisp # Compile the bell state generator into a circuit
```

To run Qurry from anywhere, simply add this directory to your path:
```
export PATH=$PATH:/home/your-username/your-directory/qurry
```

## Usage

Currently, Qurry can be used with the entire QUIL spec, as well as some small abstractions.
To review the QUIL spec and its arguments, call `./quilarity`.

### Python bindings

Qurry acts as an extension to quil, and is usable in the same way:

```
>>> from qurry.api import *
>>> program = Program(bernoulli(0.5, 0), H(0))
>>> str(program)
'RX(pi/2) 0\nH 0\n'
>>>
```

Qurry is also usable as a standalone language, which can be converted to the above python syntax at will.  

For example, the trivial Bell-state program is expressed as the following:
```lisp
(h 0)
(cnot 0 1)
```

Gate names can be either upper-case or lower-case.

The following are new instructions that Qurry offers:
`def`, `bernoulli`, `clear`, `do`, `gaussian`, `if`, `map`, `multinomial`, `uniform`

First there are the simple classical-probabilistic structures `bernoulli`, `gaussian`, `multinomial`, and `uniform`.
Bernoulli simply rotates a qubit such that it will be measured as `|1>` with a certain probability:
For instance, `(bernoulli 0.5 0)` creates a fair coin from qubit 0. 
These can be chained together to create more complicated bit-states, which are useful in other algorithms, like Grover's or QFT.

Similarly, the `gaussian` function creates a discrete multinomial state which approximates a gaussian distribution.
It uses the `def` function to create a block of useable qubits:
```
(def gaussblock 0 4) ; block of 5 qubits
(gaussian 0 1.0 gaussblock)
```
Note that much of the computation here is (as currently implemented) happening classically. 
The gaussian cdf is not computed on the quantum computer, but instead a pre-determined discrete cdf is turned into a quantum gate which can be applied repeatedly to create multi-gaussian superpositions and so on.

Uniform does nothing special:
```lisp
(def uniformblock 0 7) ; eight qubits
(uniform uniformblock)
```

Multinomial can create any discrete multinomial distribution on qubits:
```
(def multinomialblock 0 7) ; eight qubits
(multinomial 0.1 0.2 0.1 0.0 0.1 0.4 0.1 0.0)
```

Next are control statements:

`map` simply applies a single-qubit operator to an entire block. This is very useful for initializing bases:

```
(def newbasis 0 7)
(map h newbasis)
```

The `if` and `do` statements are intuitive:
```
(bernoulli 0.5 0)
(measure 0 0)
(if 0 ; If the classical bit 0 is equal to 1
    (do (x 1)
        (x 2))
    (nop))
```
This circuit will produce `111` and `000` with equal probability (but NOT using entanglement, since there is a possible intermediate state of `00`).

## Hacking

Each language feature is located in `lib/constructs/` under a file that has the same name as the feature.
Doing this allows language features to be added dynamically.
The only requirement is that each feature-file have a function `create-feature` where `feature` is the name of the feature (i.e. `create-if`).
This function should take the arguments that the function does, and return valid QUIL code.  

For instance, the `if` statement is defined as follows:
`lib/constructs/if.py`:
```python3
from ..utils import named_uuid

if_template = '''# Conditional statement
JUMP-WHEN @{first} [{cond}]
  {b}
JUMP @{end}
LABEL @{first}
  {a}
LABEL @{end}'''

def create_if(cond, a, b, definitions=None):
    '''
    Create an if statement using labels and jumps.
    (if (equal 0 1) (X 1) (X 0))
    '''
    if definitions is None:
        definitions = dict()
    return if_template.format(
            cond=cond,
            a=a,
            b=b,
            first=named_uuid('first'),
            end=named_uuid('end'))
```

The `if` statement uses a raw quil template that boils down to jump instructions, and the function `create_if` is a reserved name in this file.
For more on contributing, see [HACKING.md](HACKING.md)

-->

```
@misc{saldyt_2018, title={Qurry, a probabilistic quantum programming language}, url={https://github.com/LSaldyt/qurry}, journal={GitHub}, author={Saldyt, Lucas}, year={2018}, month={Nov}}
```
