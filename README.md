# Z Algorithm Implementation
Lightning fast pattern matching in Python

<img src="demos/z_algo.gif" alt="z_algo_demo" width="100%"/>

******************************

### Setup + Install
The standalone `main.py` requires the `colorarma` library for the visual demo. It is strongly encouraged to use [Python virtual environments](https://virtualenv.pypa.io/en/stable/installation.html) when installing external libraries.

```
virtualenv virt
source virt/bin/activate
pip install -r requirements.txt
```

******************************

### Usage

Standalone script:
`python run.py <PATTERN> <INPUT STRING>`

******************************

### Results
See the [Experiments page](Experiments.md) for timed comparisons of my Z-algorithm implementation with my implementation of naive string matching, as well as the Boyer-Moore algorithm implementation

******************************

### Z Algorithm Intuition
Z algorithm is a linear time string matching algorithm which runs in O(`n + m`) complexity. Z algorithm is used to find all occurrence of a pattern (size `m`) in a string S (of size `n`). <br>

Our goal is to create a Z array of the same length as our string, where the element Z[k] of Z array stores length of the longest substring starting from our input_string[k] that matches our pattern.<br> 

We begin by concatenating our pattern `P` with our input string `T` to obtain `P$T` (`$` being a character not found in either `P` or `T`). We then process our Z input `P$T` by iterating over the letters in the string (index `k` from 0 to `n` - 1) and maintain two pointers `l` and `r`,  where 1 ≤ `l` ≤ `k` ≤ `r`, and the interval of the z-input from `l` to `r` matches a substring of the pattern. <br>

As we process the Z-input, at each new index we encounter one of two cases:
1. if `k` > `r`: then there is no pattern substring that encapsulates the character of the Z-input at index `k` (no Z-box 'jumps over' `k`). Now we must try to match our z-input[`k`] to z-ipnut[`0`] and compute how many characters, starting at index `k` match the prefix of our z-input, OR
2. if `k` ≤ `r`: then there _is_ a pattern substring that encapsulates the character of the Z-input at index `k` (some Z-box 'jumps over' `k`). We can look at the index `k'` = `k` - `l` in our Z-array. Now we have to examine two sub-cases:
	1. Z-array[`k'`] < `B` where `B` = `r` - `k` + 1, we know that there is no prefix substring starting at 
    Z-ipnut[`k`], since otherwise Z-input[`k'`] would be larger. Therefore, we can inherit our previously computed values so  Z-array[`k`] = Z-array[`k'`] and both `l` and `r` remain unchanged
    2. Z-array[`k'`] ≥ `B` where `B` = `r` - `k` + 1. Then we know we can extend our Z-box at `k`. So `l` = `k` and begin matching Z-input[`k`] to Z-input[`0`]. We then update `r` = `k` + `j` where `j` = the number of characters of the prefix we match with starting at Z-input[`k`]


******************************

### Implementation Details & Challenges
The implementation is my own work, taken almost exclusively from the course notes. The challenges that arose from converting a high-level description were mostly off-by-one based. Descriptions of the algorithm typically use 1-indexed arrays and inclusive ranges. Python, however, uses 0-indexed arrays, and for ranges that are in the form `list[start:stop]`, Python includes the `start` index, but excludes the `stop` index.

For more information and other reference implementations, please check out [this Geeks for Geeks blog post](https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/), and [this HackerEarth blog post](https://www.hackerearth.com/practice/algorithms/string-algorithm/z-algorithm/tutorial/)
