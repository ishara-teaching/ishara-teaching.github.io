
** REMEMBER SURVEY END OF CLASS **

Pointers
========
 * What did we cover last time?
 * Declaring pointers
 * setting poitners
 * setting pointed to values
 * matching the types of pointers

 
TODAY
=====
 * We're talking about pointers as args to functions
 * Pointers as return values of functions
 * Pointers OF functions
 * How pointers are like arrays
 * The strange strange world of string pointers
 
Pointers as args to functins
----------------------------
 * Useful for returning multiple values
 * Also useful for "fake" object orientation
 * **EXERCISE**
 
Pointers as return values
-------------------------
 * Useful for "factories" and such
 * return a value that you care about
 * **EXERCISE**
 
Pointers OF functions
---------------------
 * You can actually get pointers to functions as long as the data types match perfectly!
 * void test (int foo, int (*rt) ());
 * The standard library has functions like this all over the place, like quicksort
 * This is really close to polymorphism, though it has a lot of restrictions.
 
 
 
How are pointers like arrays?
-----------------------------
 * What happens when you make an array?
 * Well, first a chunk of memory is allocated, and then the first space is given a symbolic name.
 * That symbolic name is actually a pointer
 * *Let's review accessing array elements.*
 
Pointer arithmetic
------------------
 * What we've been doing when we calculate the memory offsets of array indices is doing pointer arithmetic.
 * The [ ] operator is actually an alias for the * operator.
 * Whenever you add a value to a pointer, the compiler implicitly multiplies that value by the size of the pointed to value (not the size of the pointer itself!)
 * So if we have a char, it's 1, an int it's 4, and an 86-byte struct, 86!
 * *If you understand pointer arithmetic, you've learned the single most important thing in C*
 * *If you don't, you are just like 90% of students*
 * **EXERCISE**
 
Differences
-----------
 * Anywhere you see a [], you can put a *, except on the left side
 * You can't write over an array (since A is a constant), but you CAN ovewrite *ap!
 
How about multiple dimensions?
------------------------------
 * It's the same thing!
 * However, let's say we're trying to fill up space - we want 4 arrays of varying lengths. What are our options?
 * **EXERCISE**



Strings are a special case
--------------------------
 * Strings are a special case
 * When you declare a string, you allocate space for the memory + \0. However
 * if you declare using char *foo="bar";
 * if you declare using char foo[]="bar";
 * You end up with different things 

Multiple dimensions
-------------------
 * Same issue as we had before with space.
 * You can declare an array that meets max size, or array of string pointers.
 * Pointers will be read-only, but you can still swap them!
 * **EXERCISE**
 
 
 
 
 
 
 