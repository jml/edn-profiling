edn-profiling
=============

Code to help me profile edn &amp; parsley

## The problem

Parsley is pretty slow.  Using parsley to parse edn is pretty slow.  Using
parsley to incrementally parse edn using the iterGrammar thing in
`edn._parsley` is _amazingly_ slow, and appears to perform worse than
linearly.

Slow in CPython and in PyPy.

## The scripts

* `gen-much-edn.py`: make some data
* `nonstreaming.py`: get some timing information for the slow way
* `streaming.py`: get some timing information for the mega-slow way
* `profile-edn.py`: simple thing to get profile information

## The data

* `edn.prof`: output of a `profile-edn.py` run I did one time
* `edn.grind`: same data as `edn.prof`, but converted to kcachegrind format
