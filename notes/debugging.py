"""
Debugging techniques:

1. Read/Explain the Code
        Read what it actually says, not what you think you put.
        What does this line of code actually say and do??
        Read the documentation on functions if you are not sure.

        Try explaining the code out loud -  it slows your brain down to focus more on the problem.
        Doesn't need to be to another person - it is the vocalization process that is important
        Known as "rubber duck debugging" (explaining to inanimate object)
2. Be the CPU
        Use pencil/paper to work through the code, writing down variables and their values.
        Evaluate the expressions by hand
        Allows you to try different inputs without modifying the code.
3. Print Statements
        Let the CPU do the computations, and have it print out the values
        Allows you to trace the values through the code, as well as the flow of the program.
        Liberally sprinkling print statements throughout your code will allow you to identify
            At which point something is going wrong.
        *This may require breaking up statements in your code to generate intermediate values you want printed.
4. The IDE's debugger
        *Allows you to see everything:
            All variables in the current frame
            All variables in earlier frames in the program stack
            Allows you to set "watches" which specify statement/variables not part of your code
        In essence, you can step through your program one line, function, or expression at a time and see the state of
            the program as they execute.
        You can also set "Breakpoints" in your code that tell the debugger to stop at that point.

        *Some things will not be shown as the IDE tries to simplify your code and does background processing
"""