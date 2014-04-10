Everything Else in C
====================
 * const
 * enum
 * typedef
 * bool
 * union
 * functions with var # of args
 * env variables
 * bit fields

## Basically everything on this list is a possible final exam question ##

Const
=====
 * const is a keyword that tells the compiler that something should not change
 * It's NOT the same as a macro
   * type safety, for example
 * const is mostly used with pointers: ```const char *```
 * It's very useful for telling the compiler and API that a function has no side effects on the pointed to data
 * A const char * can be changed, but things it points to can not.
 * A char const * can not be changed, but the things it points to can.
 * **exercise**

Enum
====
 * You don't know how beautiful I think enums are. :)
 * An enumeration is a data type for creating symbolic, ordered, compiler values
 * ```enum colors {red, orange, yellow, green, blue, purple};
 * ```enum colors hair```
 * In this enum, green is greater than yellow and less than blue.
 * Enums are a data type and as such, are type safe.
 * **EXERCISE**

Typedef
=======
 * Typedefs are highly useful and frequently misused.
 * Typedef allows you to create your own data types.
 * ```typedef char * string;```
 * ```typedef struct {foo, bar} mystruct```
 * Typedefs include pointers!
 * **EXERCISE**

Bool
====
 * The c99 type bool can only be a 1 or 0. If you try to assign any value other than 1 or 0, it will be assigned 1.
 * I don't like them, because they have funny behavior that isn't necessarily bool-like.

Unions
======
 * Unions are HIGHLY misunderstood, so listen up!
 * A union is a data type that can be many different datatypes depending on what you call.
 * ```union test { int a, double b }```
 * In a union, multiple data types are occupying the same location in memory
 * NOT A CAST, A RAW CONVERSION
 * **EXERCISE**

Functions with a var number of args
===================================
 * First of all, you need <stdarg>
 * Next, define your function with regular params, followed by ...

    int varfun(int test, ...)
    {
        int sum;
        va_list ap;
        va_start(ap, num);
        
        sum = 0;
        for(int i = 0; i < test; i++)
            sum += va_arg(ap, int);
        va_end(ap);
        
        return sum;
    }

 * The named parameters MUST have some indication as to how many args are unnamed and what their types are.

Environment Vars
================
 * getenv/setenv

Bitfields
=========
    struct Disk_register {
        unsigned ready:1;
        unsigned error_occurred:1;
        unsigned disk_spinning:1;
        unsigned write_protect:1;
        unsigned head_loaded:1;
        unsigned error_code:8;
        unsigned track:9;
        unsigned sector:5;
        unsigned command:5;
        }

 * Bitfields are not portable and can't be put in arrays
