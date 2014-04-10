Pointers for the next 3 days
============================

Overview
--------
 * What are they
 * How do they work
 * Why are they useful


Indirection
-----------
 * Card catalog
 * Google search
 * "I don't have the information, but I know where to get it"

It's all just bits
------------------
 * Functions, variables, etc, they are all addresses
 * A program runs because everything knows where the information that matters is
 * registers vs memory
 * The symbol table (variables are given memory locations and passed between registers)
 * You "could" just use memory addresses. That's how assembly works

Declaring pointers
------------------
 * Pointers are variables. They have a storage class and data type.
 * The type of a pointer says "this memory location holds a memory location that holds an integer"
 * Pointers are not aliases.
 * Ampersand: addressof
 * Start: dereference

Let's do "fake assembly"
------------------------
 * c = a + b 
 * You can see real assembly using gcc -S
 * RAM (random access) you can access any memory using its address
 * *c = a + b
 * Show the fake assembly
 * Show the symbol table

Addresses vs values
-------------------
 * Demo on screen

Infinite levels of indirection
------------------------------

Pointers enable object orientation
----------------------------------
 * In Java, the 'new' keyword creates an object in the heap and a pointer on the stack
 * The pointer allows you to manipulate an object no matter where in memory it is

Pointer Types
-------------
 * **Remember this**
 * The pointer types have to agree. If you tell the computer an int is gonna be there, and you give it a float, sadness
 * You are allowed to cast pointers, it can be either really good or really bad
 * Learn the trick to match the data types, & add stars, * removes stars

Pointer bloopers (exercises)
----------------------------
    int a, b, *ap, *bp;
    char c, d, *cp, *dp;
    float f, g, *fp, *gp;
    
    ap = &c;
    *ap = 3333;
    c = ap;
     c = *ap;
    dp = ap;
    dp = ‘Q’;
    fp = 3.14159;
    gp = &fp;
     *gp = 3.14159;
    *fp = &gp;
     &gp = &fp;
    b = *a;
    b = &a;


 * There's a slide called sense and insensibility. Learn that slide

END OF MATERIAL FOR DAY ONE
===========================
 * If we have time, talk about pointers in function arguments


































