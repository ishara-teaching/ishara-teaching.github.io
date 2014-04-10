Security
========
 * As you may or may not know, security was my first area of research in grad school.
 * Security is a CONSTANTLY evolving field of computer science
 * **EXAMPLE**: Who knows what happened this week? Heartbleed


What are the goals of attackers?
--------------------------------
 * Confidentiality, Integrity, Availability


Who is responsible for security?
--------------------------------
 * The user? IT? The programmer?
 * **EXAMPLE**: In Canada, they actually pushed back the tax deadline to protect users from compromised sites.
 * With the heartbleed bug, are you liable if you deployed SSL with a bug?


So where do problems come from?
===============================
 * Programming bugs
 * Failure to validate inputs
 * Inadequate protection of secret info
 * False assumptions about operating environment

 * Be paranoid
 * Stay informed of security risks
 * Do thorough testing
 * Always check bounds on array operations
 * Minimize secrets


Validating Inputs
=================
 * Where does validation take place? Server.
 * Whitelisting vs Blacklisting
 * Special characters
 * Use well-established libraries

Resource Allocation
-------------------
 * What happens when you run out of resources?
 * Memory (malloc)
 * File Descriptors (fopen)
 * Stack Space
 * Threads


Buffer Overflow
===============
  * Where do they come from? Pointer arithmetic, essentially
  * Example of a buffer problem? Passwords in memory and "strcpy"
  * Even more dangerous, return addresses
  * How do you fix it? Safe length-limited string functions


Assumptions
===========
 * My favorite comment is ```/* this should never happen */```
 * Read documentation well: functions like fread do not null-terminate their strings.
 * Some functions let you call system commands, like fork, exec, system
 * Don't trust data from untrusted sources, this includes user input, file contents, and environment variables


Logging can be exploited
========================


Secrets and Randomness
======================
 * Security by obscurity
 * What secrets need to be protected?
 * The most random number is 17.
 * You need to make sure you can scrub memory
 * Don't put secrets in your source code
   * **EXAMPLE**: Or your git repo.
 

Race Conditions
===============
 * Basically the root cause of heartbleed
 * Taking advantage of the fact that secure operations are not necessarily atomic.


Let's do it ourselves!
======================
 * Password in source code
 * Function pointer!


 


 





