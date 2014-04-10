What is an API?
===============
 * Before we start, what is an API?
 * It's an interface that tells programmers what to do and how to use their code
 * When you solve a problem, try to think about "if I could ask someone to do something for me..."


The standard library
====================
 * Standard libraries help you do math, strings, and other fancy stuff
 * The syntax, the parts of code that turn into assembly, are a tiny part of the language.
 * The real richness of a language comes from its standard library
 * In this lecture, we'll be looking at four libraries in particular out of the 24 that are there
   * math
   * errno
   * stdlib
   * stdio
 * The purpose of a **standard** library is to provide a checklist: you don't have a C environment unless you have this

 
Remember headers
----------------
 * Every "library" is represented as a ".h" header file
 * There are implications. One is that most of these headers are linked automatically by the C compiler



math.h
======
 * To use it, include math.h and link to the math library
 * As the name implies, provides several math functions and constants
   * M_E
   * M_PI
   * M_SQRT
 * We have functions like trigonometry (cos, sin, tan, all in radians)
 * Functions have domains of legal input
 * Where does that go? JAVADOC.
 * Functions for exponentiation: exp, exp2, log, log2, pow, sqrt
 * Other functions: fabs, floor, ceiling
 * **EXERCISE** (prepare an errno)


errno.h
=======
 * Errno gives you the power to print standard error messages.
 * Remember that we can only return 1 value. Errno is a global value that is used to stick error codes when functions fail
 * Errno also provides a function "perror" that prints the error message associated with these constants.
 * Always set errno to 0 before doing anything that might set errno
 * One example is "No such file or directory".
 * Math.h returns errors when the domain is violated, the output overflows, and so on.


stdlib.h
========
 * You already know about abort and exit
 * stdlib also contains useful things like malloc and free. it's  real kitchen sink of a library
 * Then there's bsearch (binary search) and qsort (quicksort)
 * These require function pointers and certain structures of data


stdio.h
=======
 * Handles input and output between buffers and/or streams
   * A stream is a one-way flow of characters, usually tied to a file or a terminal.
   * printf prints characters to the stdout stream
   * A buffer is a null-terminated char array
 * Opening files in C is a pain, but I find it easier than java
 
Files
-----
 * fopen(fname, mode): open a stream to a file
   * Returns a pointer to the stream if it works, returns NULL and sets errno if fails
   * Also opens a file descriptor on the OS side. You need to fclose() it when you're done!
   * Mode is a C string: "r" read, "w" write, "a" append, "b" binary
   * **EXERCISE**
 * We've spoken about byte-order before, right? Remember, some systems store ints backwards

 
 * fgetc(FILE*)
 * getc(FILE*)  (like getchar, but stdin is implied)
 * fputc(c, FILE*)
 * putc(c, FILE*) (putchar with stdout implied)
 
 * ungetc lets you put a character back in the stream!
 * fread() lets you read multiple bytes from a file into a buffer
 * fwrite() lets you write a buffer to a file, byte ordering matters!
 
Fancier stuff
-------------
 * fscanf and fprintf
 * sscanf and sprintf
 
 * feof, ferror, clearerr
 * Instead of using errno, each stream has its own error storage. you can check the state of any stream using things like ferror.
 
 


