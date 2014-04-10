## Announcements ##

 * We will be regrading headers and returning some points
 * Exams graded. Will return grades first, and exams after scanning them

## Last Class ##

 * Any questions about storage and scope?
 * Storage and scope will likely be on the second midterm
 * Nobody showed up to the review session, so I guess not

## The C Preprocessor ##

### Basically Search and Replace ###

 * Using preprocessor definitions is the first step of compilation, before even tokenization
 * Replaces things and alters the source code.
 * Use gcc -E and you can see the *expanded source* before running things

### Three uses for preprocessing ###

 * Header file inclusion #include
 * Constant/Macro definition #define
 * Conditional compilation #if #endif
 * Any line beginning with # is a directive... if you need an extra line, end with a backslash

### #define ###

 *  #define identifier token-sequence
 * Replace any identifier with any series of tokens
 * Very different from declaring a variable, even a constant
 * Variables have a *type* and *storage class*, #defines don't
 * *Who remembers what the storage classes are*?
 * **EXERCISE 1**
 * DEFINES can include other DEFINES, but can't be recursive or circular!
 * Don't include semicolons in your #defines
 * Multi-line defines should be in curly brackets

### #defining macros ###

 * Macros are like functions
 * #define FOO(bar,baz) baz + bar
 * Arguments need parentheses
 * Arguments shouldn't have side effects!
 * **EXERCISE 2**
 * What are the tradeoffs? Speed, memory, type safety
 * **EXERCISE 3 (swap) **
 * Macros can be nested, so you need to expand them accordingly
 * **EXERCISE 4... (maybe homweork)**

### Other fun things

 * Want to quote something? use "#"
 * Want to concatenate two things? Use "##"


### #include ###

 * Takes a file and copy-pastes it into your source code
 * A < > file is a library file. a " " file is local. (change with -L and -I)
 * Usually done with header (.h) files! Remember, they need to appear before use!
 * HOW DO WE STOP AN INFINITE LOOP?

### #if and conditional compilation! ###

 * Any code that appears in an #if #endif block is removed if the statement is false
 * So to solve the last problem, we can define a constant.
 * We only include the code if the constant is NOT defined! #ifndef
 * You can do really cool stuff here. Like debugging.
 * Use -DTESTING=1 to define the constant debug during compilation.  Then include printfs only if TESTING is true!
 * Or define a macro or function. :)
 * **EXERCISE 5**







