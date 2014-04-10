From last lecture
=================
 * Let's warm up with an exercise! 14.03
 * Any questions about 14.04 or 14.05?

Dynamic Memory Allocation
=========================
 * Motivation: lots of students tried to use a stack with a local variable
 * In Java, we could do this easily, because of the NEW keyword
 * What happens when you use NEW?
 * Memory allocated in heap by OS, initialized, pointer to new memory is returned
 * We are going to manually do this in C using a function called MALLOC.

Using Malloc
------------
 * ```void *malloc(size_t sz)```
 * Allocates 'sz' bytes from the heap and returns a pointer to the first byte
 * "example, malloc'ing an array"
 * Note! Malloc does not initialize data.
 * ```void *calloc(size_t num, size_t sz)```
 * Calloc allocates sz*num bytes AND starts them at zero (it's basically a wrapper)
 * Which one is slower?
 * **EXERCISE 2**

Realloc and Free
----------------
 * ```void *realloc(void *ptr, size_t sz)```
 * This will try to take the ptr and change the size of the memory associated with it.
 * If the new size is smaller, ptr will not change.
 * If the new size is larger, ptr might change, but memory will be copied to new area
 * If the resizing can't be done, returns null and ptr remains unchanged
 * When you're done, ```void free(void *ptr)```, free your memory
 * This tells the OS you're finished with it
 * **EXERCISE 3**


All those times I went over memory maps has prepared us for this day!
---------------------------------------------------------------------
 * Describe what happens under the hood, use the stack example
 * Talk about various problems, such as writing past end of memory and memory leaks

Memory leaks
------------
 * What happens if you lose your last pointer to malloc'd memory? You can't free it!
 * This is a memory leak. Garbage collectors do something called "pointer counting" to keep track of memory, but C doesn't have that. So you have to be careful.
 * Valgrind is a tool that sticks pointer counting into your program and tells you if you have leaks
 * We'll be using valgrind for HW6
 * ```gcc –Wall –std=c99 –g program.c –o program```
 * ```valgrind –leak-check=yes ./program```
 * **EXERCISE 4**
 
Now that we're done
-------------------
 * **EXERCISE 1**

