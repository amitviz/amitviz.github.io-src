Title: Introduction to Matlab: lecture 1
Date: 2011-10-31
Category: Notes
Tags: matlab, code, teaching, bath
Slug: matlabbasics
Authors: Amit

# Matlab basics
The purpose of these lectures is to introduce the students to the MATLAB environment, and use it to solve simple beam finite element problems.

At the end of the lectures, the students should have enough information to be able to:

1. Use MATLAB to write complex programmes using multiple functions
2. Use the MATLAB help to get information on new commands and functions
3. Solve the tutorial questions

## Introduction to Matlab

### What is MATLAB?

* MATLAB is an interactive calculation environment, designed for working with matrices: the MATrix LABoratory
* MATLAB is also a powerful, but simple and easy-to-use programming language
* MATLAB also provides a number of `toolboxes' to extend its core functionality

MATLAB is available to use on the [GIGATERMS](rdp://gigaterms.campus.bath.ac.uk/) server.

MATLAB is also available from the BUCS website:

* University homepage>Computing Services>Software>[Secure Downloads Tool](https://isecure.bath.ac.uk/securedownloads/Default.aspx)

### Why use MATLAB for finite element analysis?
Finite element analysis is a simultaneous equation problem, and we can describe it using matrices:

\begin{align}
[K]\{u\} = \{F\}
\end{align}
 
MATLAB works natively with matrices as a data type. It can solve such a system by typing in:

    :::matlab
    u=K\F

Many of the steps involved are also matrix operations, such as coordinate transforms, or matrix inversions. A programming language is also useful to perform repeated operations, such as those applied to elements or nodes in a finite element program.

### The MATLAB desktop environment
![The Matlab desktop](/images/matlab_screen_annotated.png)

* **Current directory** This is where MATLAB first looks for the files that are to be run. Useful to create a new directory for a project.
* **Files** A list of all the function and script files in the current directory.
* **Command window** This is where commands are entered to MATLAB, and where the results are printed out.
* **Command prompt** The `>>`{matlab} prompt is where data and commands are typed in.
* **Variables** A list of all the variables that are currently held in memory.

### Simple calculations
The command window can be used as a simple calculator (`>>` is the MATLAB prompt, you don't need to type it in!):

    :::matlab
    >> 2*2             % multiplication

    ans =

        4

    >> sqrt(2)/2       % square-root function

    ans =

        0.7071

    >> pi * 5^2        % built-in variable pi

    ans =

    78.5398

    >> cos(pi/3)       % trigonometric functions

    ans =

        0.5000

### Variables
Variables can be used to store values for use later

    :::matlab
    >> clear all % clear existing variables from memory
    >> r = 5;    % radius r
    >> % note the semi-colon at the end to suppress MATLAB output
    >> % also note the use of the percent symbol (%) to insert comments
    >> area1 = pi * r^2

    area1 =

    78.5398

    >> r = 10;
    >> area2 = pi * r^2

    area2 =

    314.1593

    >> area2 / area1

    ans =

    4

### Types of variables
Any type of data can be stored in a variable, *e.g.*

    :::matlab
    i = 4              % integer variables

    j = 4.5            % floating point variables

    k = 1e-3           % floating point entered in exponential form

    l = 'some text'    % a string of characters

Matrices can also be stored in variables.

Note: the MATLAB notation `1e-3` is used to represent $1 \times 10^{-3}$

### What is a matrix?
A matrix is just a 2D array of values.

The matrix can be entered at the command line, surrounding the values with square brackets `[ ]`. Columns are separated by commas or spaces, rows by semi-colons or line breaks:

    :::matlab
    >> x = [1 2; 3 4]  % entered on a single line

    x =

        1     2
        3     4

    >> y = [5,6;7,8]   % can include commas if this helps readability

    y =

        5     6
        7     8

    >> z = [9 10       % press enter before the matrix is ended
    11 12]             %   with ], and MATLAB starts a new row

    z =

        9    10
        11    12


### Some useful matrices

    :::matlab
    >> x = zeros(2)    % a square 2x2 matrix of zeros

    x =

        0     0
        0     0

    >> x = zeros(2,3)  % a rectangular zeros matrix
                    %   note! row, column order 
    x =

        0     0     0
        0     0     0

    >> y = ones(2)     % a matrix of ones (here, 2x2)
                    %   can also be rectangular
    y =

        1     1
        1     1

    >> z = eye(2)      % a 2x2 identity matrix, I
                    %   note! this must be square
    z =

        1     0
        0     1


### Some terminology
Everything is a matrix in MATLAB!

* a **scalar** (single integer or floating point number) is a $1\times1$ matrix
* a **vector** or a **list** is simply a matrix where one of the dimensions is 1, *e.g.* a column vector (`zeros(3,1)`) or a row vector (`zeros(1,3)`).
* a **string** is a vector of characters
* an **array** is a term used for a **grid** of values: *i.e.*, a matrix!

Some of these terms will be used interchangeably in the remainder of the notes.

### Addressing matrices
Now that we have matrices full of zeros or ones, how do we get some useful information in and out of them?

    :::matlab
    >> x = magic(3)    % a built-in function to create a 3x3
                    %   magic-square (all rows, columns and diagonals
                    %   add up to the same value)
    x =

        8     1     6
        3     5     7
        4     9     2

    >> x(3,2)          % extracting a certain value (note row, columns
                    %   order again)
    ans =

        9

    >> x(3,2) = 0      % setting the value of a certain element

    x =

        8     1     6
        3     5     7
        4     0     2

### Addressing matrices: the colon operator}
To address an entire row or column, we can use the colon (`:`) operator

    :::matlab
    >> x = magic(3);   % the same matrix as the previous slide
    >> x(3,:)          % '3rd row, all the columns'

    ans =

        4     9     2

    >> x(:,2)          % 'all the rows, 2nd column'

    ans =

        1
        5
        9

    >> x(3,:) = [0 0 0]% replacing the 3rd row

    x =

        8     1     6
        3     5     7
        0     0     0

### The colon operator
Without any parameters, the colon represents an entire row or column. The colon can also be used with parameters, to represent a range of values.

    :::matlab
    >> x = 1:10        % all the numbers in the range from 1-10

    x =

        1     2     3     4     5     6     7     8     9    10

    >> y = 1:3:30      % all the numbers in the range from 1-30, in steps of 3

    y =

        1     4     7    10    13    16    19    22    25    28

    >> z = 5:-0.5:1    % the range 5-1, in steps of -0.5

    z =

        5.0000    4.5000    4.0000    3.5000    3.0000    2.5000    2.0000    1.5000    1.0000

### Specific matrix addressing with the colon
We can combine the 'range' use of the colon to pick out some specific values from a larger matrix:

    :::matlab
    >> x = magic(4)    % a 4x4 magic square

    x =

        16     2     3    13
        5    11    10     8
        9     7     6    12
        4    14    15     1

    >> y = 1:2:4       % every other number between 1-4

    y =

        1     3

    >> z = x(y,y)      % pick just these values out from x

    z =

        16     3
        9     6

### Matrix properties
In addition to getting data *from* the matrix, we can get data *about* the matrix:

    :::matlab
    >> x = magic(4);   % as previously
    >> [a b] = size(x) % the size of matrix x

    a =
        4
    b =
        4

    >> min(x)          % the minimum value in each column of x

    ans =
        4     2     3     1

    >> max(x)          % the maximum value in each column of x

    ans =
        16    14    15    13

    >> mean(x)         % the mean value of each column of x

    ans =
        8.5000    8.5000    8.5000    8.5000

### More on matrix sizes
The size command is very useful, since it will let us write programmes where we don't know before hand how large our matrices and vectors will be.

The `size` command can be used as follows:

    :::matlab
    >> x = zeros(5,2); % an example matrix with 5 rows and 2 columns
    >> [a b] = size(x) % as we've seen before, we can get the dimensions using size()
    a =
        5
    b =
        2
    % if we know which dimension we want, we can specify it as an optional argument
    %   to the size function
    >> size(x,1)       % the first dimension of x (i.e. number of rows)
    ans =
        5
    >> size(x,2)       % the second dimension of x (i.e. number of columns)
    ans =
        2
    % if we have a vector (a matrix with one of the dimensions as 1) we can also use
    >> y = zeros(1,6); % a row vector
    >> z = zeros(8,1); % a column vector
    >> length(y)
    ans =
        6
    >> length(z)
    ans =
        8

### Matrix algebra
Matrix algebra can be performed with the MATLAB matrices, e.g. for the system $Ax = b$,

    :::matlab
    >> A = magic(3)    % a 3x3 magic square
    A =
        8     1     6
        3     5     7
        4     9     2
    >> x = [1;2;3]     % a column vector x
    x =
        1
        2
        3
    >> b = A*x         % matrix multiplication to find b
    b =
        28
        34
        28
    >> x = inv(A)*b    % if b is known, we can find x by inverting A
    x =
        1.0000
        2.0000
        3.0000
    >> x = A\b         % more efficient than inverting A is using the backslash operator
    x =
        1
        2
        3


### Matrix algebra II
Some of the most useful functions are those to find the **inverse** and **transpose** of a matrix:

    :::matlab
    >> A = magic(3)    % the 3x3 magic square
    A =

        8     1     6
        3     5     7
        4     9     2
    >> inv(A)          % the inverse of matrix A
    ans =
        0.1472   -0.1444    0.0639
    -0.0611    0.0222    0.1056
    -0.0194    0.1889   -0.1028
    >> A'              % the transpose of A, using the inverted comma
    ans =
        8     3     4
        1     5     9
        6     7     2

Inverting the matrix is a computationally expensive problem. Although a system $Ax = b$ can be solved as $x = A^{-1}b$, the **backslash operator** (`A\b`) uses Gaussian elimination to solve without explicitly calculating $A^{-1}$.


### Array algebra
MATLAB treats everything as a matrix, but occasionally, we might want to treat a variable as simply a list (or grid) of values, rather than a matrix in the mathematical sense.

MATLAB behaves as expected when we multiply a 'matrix' or vector by a scalar, or add two matrices, and also includes a number of **piecewise operators**.

    :::matlab
    >> x = 1:3;        % x = [1 2 3]
    >> y = 2*x         % multiply by a scalar
    y =
        2     4     6
    >> x+y             % add 2 vectors (1D matrices)
    ans =
        3     6     9
    >> x .* y          % perform a piecewise multiplication (note the dot before the *)
    ans =
        2     8    18
    >> x ./ y          % perform a piecewise division (note the dot before the /)
    ans =
        0.5000    0.5000    0.5000

Note, matrix algebra rules don't allow us to perform ordinary multiplication between two vectors each of size $1\times3$. We could however transpose one of the vectors (*e.g.* `y = y'`).

### MATLAB scripting
When we want to perform the same actions over and over again, we can save the steps in a MATLAB script. A MATLAB script is just a series of commands, exactly as they would appear if they were typed in at the command prompt.

Here, we shall write a script to solve the roots ($y=0$) of the quadratic equation:

\begin{align}
  y = ax^2 + bx + c
\end{align}

A reminder, the solution is given by:

\begin{align}
  x = \frac{-b\pm\sqrt{b^2 - 4ac}}{2a}
\end{align}


### MATLAB scripting--the editor
![Matlab editor](/images/matlab_editor_annotated.png)

### MATLAB scripting--example
Using the commands that we already know, we can write the script:

    #!matlab
    a = 1;             % the input parameters: note the semi-colon at the end of the
    b =-5;             %   line to stop MATLAB from printing out these lines
    c = 6;

    % Here, the calculation is performed.
    x1 = (-b + sqrt(b^2 - 4*a*c))/2*a
    x2 = (-b - sqrt(b^2 - 4*a*c))/2*a
    % Since there's no semi-colon at the end, the results will be printed out.
    
If we save this file as `quadscript.m`, we can run it by typing the name `quadscript` at the command prompt:

    :::matlab
    >> quadscript
    x1 =
        3
    x2 =
        2

We could keep this script, and change the coefficients every time we wanted to solve a different problem, but there is a way we can write a script that we can use for any problem.


### Adding interactivity to scripts
Instead of including the coefficients in the script (*hard-coding* them) we could instead ask the user using the `input` function:

    #!matlab
    disp('Solving the equation: ax^2 + bx + c'); % display some info for the user
    a = input('Please input the value of a:');
    b = input('Please input the value of b:');    % get parameters typed in
    c = input('Please input the value of c:');

    x1 = (-b + sqrt(b^2 - 4*a*c))/2*a            % exactly the same as previously
    x2 = (-b - sqrt(b^2 - 4*a*c))/2*a
    
Saving as `quadscript2.m` and running:

    :::matlab
    >> quadscript2
    Solving the equation: ax^2 + bx + c
    Please input the value of a:1
    Please input the value of b:-5
    Please input the value of c:6
    x1 =
        3
    x2 =
        2
        
This is useful where we want input from the user, but we can't run a large programme that stops to ask for each new variable...


### MATLAB functions
A **function** is a self-contained piece of code that accepts a number of input variables, processes them, and then returns a number of answers.

We have already seen some of MATLAB's built-in functions:

* `cos(x)` (and similar trigonometric functions): takes an angle $x$ as its **argument**, or **parameter**, and returns the cosine of the angle
* `size(x)`: takes a matrix $x$ (remember: everything is a matrix!) and returns *two* values, the number of rows and the number of columns in the matrix

### The purpose of functions
Functions can be called in a number of ways, e.g.

    :::matlab
    >> cos(0.7854)     % supplying the argument directly to the function
    ans =
        0.7071

    >> theta = 0.7854;
    >> cos(theta)      % supplying a variable to the function
    ans =
        0.7071

    >> cos(pi/4)       % evaluating an expression as an argument
    ans =
        0.7071

All three methods here are equivalent. When all the input arguments are known, the function can calculate the outputs with no further intervention from the user. The input arguments can even come from another part of the programme.

### Defining a function
A MATLAB function is created in a file with a `.m` extension (just as a script). The first line of the script must take the following form, using the keyword `function`:

    #!matlab
    function [outputs] = function_name(input_arguments)

The function must be saved with the file name matching the function name (here, `function_name.m`). Somewhere, within the function file, all the outputs must be set. Ideally, the function should also end with `return;`, to return programme control to wherever the function was *called* from.


### An example function
The file `quadratic.m` contains the following:

    #!matlab
    function [x1,x2] = quadratic(a,b,c)
        % A function to return the roots of a quadratic equation

        x1 = (-b + sqrt(b^2 - 4*a*c))/2*a; % note the semi-colon to suppress output: we don't need
        x2 = (-b - sqrt(b^2 - 4*a*c))/2*a; %  the answer printed every time the function is called

    return;

$a,b,c$ are the arguments, $x1,x2$ are the return values. A comment is useful to explain what the function does: you may end up using this function in many other programmes, or it may even be used by many other people in their programmes.

    :::matlab
    >> [x1,x2] = quadratic(1,-5,6)
    x1 =
        3
    x2 =
        2


### Getting help
MATLAB has a comprehensive online help, which details all the functions and how to use them. 

![Matlab help](/images/matlab_help.png)

Additionally, a free online book, [Numerical Computing with MATLAB](http://www.mathworks.com/moler/chapters.html), is available, written by the inventor of MATLAB, Cleve Moler.

### Flow control in functions
An important part of a programme is its ability to make decisions based on input, and take actions based on that decision. There are two main ways of doing this:

    #!matlab
    if (condition)
        % actions to perform if condition is true
    elseif (condition2)
        % actions to perform if condition2 is true
    else
        % actions to perform if none of the above were true
    end

or

    #!matlab
    switch condition
        case condition1
            % actions to perform if condition==condition1
        case condition2
            % actions to perform if condition==condition2
        otherwise
            % actions to perform if condition doesn't match any of the above cases
    end

The conditions in both the `if` and `switch` expressions are based on **logical variables**, *i.e.* those that evaluate to true or false.

### Logical operators
A **logical variable** can have a value of **true** or **false**. Logical variables are normally created as the results of a comparison operation, and used for conditional statements (like `if`).

The logical operators and their meanings are as follows - `a` and `b` are any type of variable:

* `a == b` a is equal to b (using `a = b` is the most common error in `if` statements)
* `a \~= b` a is not equal to b
* `a < b; a <= b; a > b; a >= b` a is less than (or equal to), or greater than (or equal to) b

And where `a` and `b` are already logical variables themselves:

* `a \&\& b`; `a \& b` both a and b are true (scalar and vector)
* `a \|\| b`; `a \| b` either one of a or b is true (including both are true) (scalar and vector)
* `\~a` a special negation operator, i.e. $\sim$true is false, and $\sim$false is true


### Conditional statement example
Here is an example we might use in a finite element code, to detect if our elements meet a failure criteria:

    #!matlab
    if (abs(stress) >= criticalstress) && (stress > 0)
        % The abs() function returns the absolute value (or magnitude) of a variable
        
        % abs(stress) and criticalstress are numerical variables, the comparison
        %   will return either TRUE or FALSE (i.e. a logical variable)
        % Similarly, (stress > 0) will return TRUE or FALSE (i.e. a logical variable)
        % The && operator compares the two logical variables
        
        % Here is the case for TRUE, i.e.
        %   abs(stress) >= criticalstress       is   TRUE
        %   stress > 0                          is   TRUE
        disp('Element fails under tension');
        % The disp() function displays a string in the command window
    elseif (abs(stress) >= criticalstress) && (stress < 0)
        % Here, if the first conditional wasn't TRUE, we can try another
        disp('Element fails under compression');
    else
        % Here, is the default action to carry out if none of the conditions were TRUE
        disp('Element does not fail');
    end


### Looping in functions
In addition to conditional decision making, programmes are useful for repeatedly performing the same operation, or performing an operation on a sequence of variables.

MATLAB gives us two methods for looping:

    #!matlab
    for loop_variable = range
        % actions to perform using the loop_variable
        
        % use when we want to perform the actions a set number of times
    end

or

    #!matlab
    while condition
        % actions to perform while condition == TRUE (using the logical operators we
        %   saw earlier
        
        % use when we don't know how many times the loop needs to run
    end

Loops are incredibly useful, but there are occasions where their use is unnecessary, and even slows down the programme...


### Avoiding loops
An example of where we might want to use a loop is in a finite element programme: if we have a vector of the strains in all of our elements, we might want to work out the stress. Using loops, we could do:

    #!matlab
    for i = 1:length(strains)    % we can let the programme work out how many times
                                %   it needs to run the loop
        % i is the loop variable
        % the i-th stress is calculated by multiplying the i-th strain by the modulus
        stresses(i) = modulus * strains(i);
    end
    
But since MATLAB is designed (and optimized) to work with matrices (including vectors), we could use instead:

    #!matlab
    % if modulus is a scalar (i.e. there is one modulus for all locations)
    stresses = modulus * strains;

    % even if modulus is a vector with a different value at each location, we can use
    stresses = modulus .* strains;

`stresses` and `strains` are still vectors, but we've made the code much simpler to read, as well as much faster.
