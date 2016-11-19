Title: Introduction to Matlab: lecture 3
Date: 2011-11-14
Category: Notes
Tags: matlab, code, teaching, bath
Slug: matlabdebugging
Authors: Amit

# Debugging

The last lectures introduced MATLAB, then focussed on developing the structure of the solver part of the finite element programme.

This lecture, we look at the process of debugging a programme in MATLAB.

By the end of this lecture, the students should be able to:

* Debug scripts and functions written in MATLAB

## Debugging MATLAB scripts and functions
It's unlikely that the MATLAB scripts and functions that you write will work perfectly first time: they will have **bugs**.

The process of identifying and eliminating these is called **debugging**, and MATLAB has some useful tools to help.

### Bugs
The easiest type of bug to find is one that prevents MATLAB from running your programme. 

MATLAB presents an error message in the command window, along with an explanation of why it has stopped, and where the error is.

    :::matlab
    ??? Attempted to access nodes(3,2); index out of bounds because size(nodes)=[2,6].

    Error in ==> elementL at 3
    dy = nodes(elements(e,2),2) - nodes(elements(e,1),2);

    Error in ==> globalK at 6
        L = elementL(nodes,elements,el);
    
If MATLAB knows where the error is, you can click on the script or function name to open the MATLAB Editor and go to the correct line in the appropriate file to make the corrections.

MATLAB also traces the error: here, the error is in function `elementL`, which was called by another function, `globalK`.

More difficult to track down are bugs that don't prevent MATLAB from running your code, but which produce incorrect answers.

To use the debugging tools, we should have some idea of where the bug might be, and which line(s) of code that we are interested in. Then, we can set a **breakpoint** in the code.

* A breakpoint is a point in the code where instead of continuing as MATLAB would normally do, MATLAB will pause. This allows examining of the variables that are in memory at this point.

### Setting breakpoints for a run
A breakpoint is set in a MATLAB file from the MATLAB editor. Any line that can have a breakpoint set has a little `-` next to the line number.
 
The breakpoint is set or cleared by either clicking on the `-`, or clicking on the ![Set breakpoint icon](/images/matlab_db2.png) icon
 
![Setting the breakpoint](/images/set_breakpoint.png)

The code is run by using the function name at the command line as usual, or by clicking on the ![Play icon](/images/matlab_db1.png) icon.

When MATLAB reaches the breakpoint, it pauses, and indicates which step it is at with a little green arrow next to the line:

![The program paused at the breakpoint](/images/run_breakpoint.png)

### During a breakpoint
When MATLAB pauses for a breakpoint, it returns control to the user in the command window.  The Command prompt is slightly different to the normal one:

    :::matlab
    3   dy = nodes(elements(e,2),2) - nodes(elements(e,1),2);
    K>> 

* The first line gives the line number in the file at which MATLAB has paused (and a copy of the line).
* The `K>>` is the MATLAB debug prompt

From here, all the usual MATLAB commands are available. Additionally, you have access to all the variables that are in memory at this point in the programme: they are listed in the *Workspace* pane in MATLAB. At this point, it's worth checking that the variables contain what you expect them to contain!

Once we're done inspecting the programme at it's current state, there are a few options:

* ![Step icon](/images/matlab_db4.png) Using the `Step' button, MATLAB will run the current line, and pause at the next line. Using this option, we can run a function one line at a time, checking that each step does what you expect it to.
* ![Step in icon](/images/matlab_db5.png) With the `Step in' button, instead of just stepping to the next line in a function or script file, we can follow the flow of our programme into another script file.
* ![Step out icon](/images/matlab_db6.png) If we decide that the bug is not within the current function, the `Step out' button runs the remainder of the function, and pauses in whatever the parent function was.
* ![Continue icon](/images/matlab_db7.png) If we want to skip over a lot of code, we can run it to the next breakpoint (or if there are none, to the end of the programme).
* ![Exit debug icon](/images/matlab_db8.png) Exit debug mode, without running the rest of the programme.

### Summary of Debugging commands

* ![Play icon](/images/matlab_db1.png) Run file
* ![Set breakpoint icon](/images/matlab_db2.png) Set or Clear breakpoint
* ![Clear all breakpoints icon](/images/matlab_db3.png) Clear all breakpoints in all files
* ![Exit debug icon](/images/matlab_db8.png) Exit debug mode
* ![Step icon](/images/matlab_db4.png) Step (to the next line)
* ![Step in icon](/images/matlab_db5.png) Step in (to a function file)
* ![Step out icon](/images/matlab_db6.png) Step out (of the function file)
* ![Continue icon](/images/matlab_db7.png) Continue (to the next breakpoint)

