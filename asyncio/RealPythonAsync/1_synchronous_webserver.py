"""
A synchronous program is executed one step at a time. Even with conditional branching, loops and function calls, you can still think about the code in terms of taking one execution step at a time. When each step is complete, the program moves on to the next one.

Here are two examples of programs that work this way:

    -   Batch processing programs are often created as synchronous programs. You get some input, process it, and create some output. Steps follow one after the other until the program reaches the desired output. The program only needs to pay attention to the steps and their order.

    -   Command-line programs are small, quick processes that run in a terminal. These scripts are used to create something, transform one thing into something else, generate a report, or perhaps list out some data. This can be expressed as a series of program steps that are executed sequentially until the program is done.

An asynchronous program behaves differently. It still takes one execution step at a time. The difference is that the system may not wait for an execution step to be completed before moving on to the next one.

This means that the program will move on to future execution steps even though a previous step hasn’t yet finished and is still running elsewhere. This also means that the program knows what to do when a previous step does finish running.

In a synchronous program, if an execution step starts a database query, then the CPU is essentially idle until the database query is returned. For batch-oriented programs, this isn’t a priority most of the time. Processing the results of that IO operation is the goal. Often, this can take longer than the IO operation itself. Any optimization efforts would be focused on the processing work, not the IO.

Asynchronous programming techniques allow your programs to take advantage of relatively slow IO processes by freeing the CPU to do other work.
"""