# DATABASE FOR INTEGERS

This is a coding challenge submission with Guanyin Labs.

The goal of this project is to build a data structure for storing integers.
The data is stored in memory rather than persisted to disk.
AKA Recreate a simple database.

## TLDR - Quick Start Command

Command line takes in as many input files you are wanting to test.
The program outputs to screen.

```
python3 main.py input.txt input2.txt input3.txt ...
```

## My Assumptions

I assumed the input data came with little error.
Tarnsaction blocks have some sort of 'END' or 'COMMIT' to stop it.
I assumed the next user would utilize an input file with however many test cases written
and the output is printed to the terminal/screen.


## My Approach

I created my database as a module so it could be imported to other projects in the future, as these commands are simple to change and expand on. I was able to keep track of the command history using a stack which allowed for easy 'ROLLBACK' feature of this program and kept things in the order the 'SET' and 'UNSET' commands were ran. I noticed that these two commands were the only ones that wre really manipulating the database and emphasized them in the 'ROLLBACK' trying to look for edge cases such as running 'SET' after running 'BEGIN' where there were no variables to maintain. As for the order of when transactions were being recorded, it reminded me of a Leetcode problem (https://leetcode.com/problems/valid-parentheses/) where the expressions of a beginning and an end were inside of other expressions. Its nice because sub- expressions where BEGIN and COMMIT/ROLLBACK end the transaction are 'popped' out in the same order they were executed in, so a stack implementaion of the history worked nice here, especially for nested blocks. Using a Stack and Block History solved this problem.

## Getting Started

This program allows multiple inputs in the command line argument.

Folder's structure:

├── README.md

├── input.txt

├── main.py

└── database.py


### Prerequisites

Requires Python3 installed into your system.
To install visit: https://www.python.org/downloads/

### Running The Program

To run this program open it with any IDE of your choice.
These instructions assume a Mac environment for simplicity and the folder is in a known location.

Open Terminal (on Mac) and change directories into this folder.

```
cd folder you made
```

Make sure your test input file's are in the same level of this folder.

Example command:
```
python3 main.py input.txt
```

## Running the tests

Change the input file or add more input files in the command line when running the program.
ex:
```
python3 main.py input1.py input2.py
```
One could easily write the output to an output file if necessary.

# Time And Space Complexity

## TIME

- Reading in 'input.txt' O(n)
- Running Commands O(n), assuming the input file is correct this shouldn't take too long.
- Looping through "block history" O(m)

## SPACE

- Reading in 'input.txt' O(n)
- "Block History" Worst Case O(n), the size of the input file
- Database O(n)

## OVERALL

- Time: O(m*2n) -> O(n) (read/write, command list, and block history)
- Space: O(3n) (Database, history, and reading in the file)

Overall Complexity is dependent on the data:
In the Worst Case the input file runs a lot of 'SET' commands creating a larger database increasing time and space linearly as we store data. "Block history" also adds space, but is treated like a stack so computation is lower but still in the worst case can add space linearly.

## What could be improved

- Using switch statements instead of 'if' statements would reduce parameter checking computation.
- Figuring out a faster implementation of TRANSACTION LIFE CYCLE. I think there's a better implemenation of record keeping for this problem.     Using a dictionary implementation.
- Exception handling in the database class can be more specific.

## Author

* **Doran R. Martinez**
https://linkedin.com/in/doranmartinez

## License

This project is licensed for Guanyin Labs and under their discretion.

## Acknowledgments

* Thank you for taking the time to read this!
