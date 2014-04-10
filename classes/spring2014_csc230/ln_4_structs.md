Before starting
===============
 * Grades for HW3, HW4, are done. Midterm 1 has also been returned.
 * HW5 due tonight.
 * Midterm 2 next tuesday. Study session monday. Bring questions, lots of questions.


STRUCTS, Take 2!
================
 * Structs are a composite data type consisting of ints, chars, and whatever else you like.
 * Let's look at the definition of a struct
 
```
    struct coord {
        int x;
        int y;
    };
   
    struct coord pos1;
    pos1.x = 5;
    pos1.y = -3;
    struct coord pos2 = {2,2};
    struct coord pos3 = {.y = 10, .x = 4};
    pos1 = pos2;
```
 
 * They are solely a form of storing data, but have some really neat features to them.
 * They can contain several struct variables of basically any data type.
 * These variables are accessed using the dot-notation you all know and love!
 * If you've been using dot notation before today, it's been wrong. Teach yourself the right way.
 * Don't forget the "struct <name>" syntax. YOU MUST INCLUDE THE STRUCT.
 * **EXERCISE** (go over)
 * One more thing! Structs can also CONTAIN structs! **EXERCISE** (notice how the variables don't conflict)

Structs are not objects
=======================
 * They are good at fooling you though. What's missing? (Member methods, no NEW call)
 * Can we cheat? (Fucntion pointers)

Structs in memory
=================
 * Packing and padding 
 * Important thing to note is that structures are "actually there"
 * This is a hard concept to get across. Structures are not a pointer to the first element, they are a DATA TYPE
 * But what about ARRAYs of STRUCTS?

```
    struct coord map[40] = { {3,3}, {9,1}, {8,6}  }
    map[5] = (struct coord) {4,7};
```

 * Let's do our memory mapping exercise! If I access map[4], what memory address is that?
 * sizeof struct!
 * Try doing arrays of structs yourself (review) **EXERCISE**

Structs in functions
====================
 * Just like everything else, structs can be input parameters and output results of functions
 * When a struct is a 
 * With me now!

```
struct coord north( struct coord pos )
{
    pos.y--;
    return pos;
}
```

 * When a parameter is a struct, remember that these are pass by value!
 * The argument is NOT CHANGED.
 * Now that we can return structs, we can return *multiple results in one function!*
 * Structs as return values **EXERCISE**

Now pointers
============
 * Structs can contain pointers.

```
    struct coord {
        int x;
        int y;
        struct coord *next;
        struct coord *prev;
    }
    
    struct coord p1 = {5,3,NULL,NULL};
    struct coord p2 = {5,4,NULL,&p1};
    struct coord p3 = *(p2.prev);
    struct coord *pp = p2.prev;
    int xs = p2.x + (*pp).x; // that's annoying!
    int ys = p2.y + pp->y; // arrow operator
    
```
 
 * struct 
 * Now pointers TO structs is very interesting.
 * The parens DO MATTER in the -> case
 * Arrow operator **EXERCISE**


Have you noticed a pattern?
===========================
 * Data type
 * In memory
 * In functions
 * How pointers work


