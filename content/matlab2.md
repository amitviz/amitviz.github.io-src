Title: Introduction to Matlab: lecture 2
Date: 2011-11-01
Category: Notes
Tags: matlab, code, teaching, bath
Slug: matlabbeamfe
Authors: Amit

# Beam Finite Element Analysis
Here, we're going to take a brief overview of the steps required in producing a Finite Element (FE) programme for beam analysis.

* **Not all the answers are in these notes!**
* There should be enough hints to produce a 2D FE code.
* If we can produce a 2D code, extending it to 3D should be trivial.

## Finite element analysis

### Parts of an FE program

![Parts of an FEA program](/images/fea2.png)

* Problem definition
    * component shape
    * materials
    * loads
* Preprocessor
    * digital representation: the 'geometry'
    * mathematical representation of material behaviour
    * discretization: 'meshing'
* Solver
    * form element stiffness matrices
    * assemble global matrices
    * apply boundary conditions
    * solve for nodal unknowns
* Postprocessor
    * calculate derived quantities, *e.g.* strains, stresses, thermal gradients
    * plotting and visualization tools
* Useful output
    * does my component work?

### Problem definition

**Truss** or **beam** elements

* defined by length $L$, area $A$, modulus $E$
* pin-jointed
* uniform strain
* fixed locations, sliding joints, free joints

Solve for displacements $\mathbf{u}$ (vector quantity), strains and stresses.

### Pre-processor

The problem definition already represents a suitable mesh: 'elements' correspond to beams, 'nodes' correspond to joints.

* a **node** is defined by its coordinates
* an **element** is defined by the nodes it connects

We can input these data directly in the form of a list (of course, MATLAB calls this a 'matrix'). It's also useful to input the moduli and areas: also as a list, since they might not be the same for all beams.

![2D beams](/images/2dbeams_annotated.png)

    #!matlab
    nodal_coordinates = [0,0; 1,0; 1,1];   % 1 row per node
    element_nodes = [1 2; 2 3; 1 3];       % 1 row/element
    element_area = [6; 6; 6]*1e-4;        % 1 row/element 
    element_modulus = [210; 210; 210]*1e9;
    % note that for the area and modulus, I've used a short
    %   hand form by multiplying a vector by a scalar
    nodal_forces = [0 0; 0 0; 1000e3 0]; % each node has
                                        %   a vector force
Remember: unit consistency!


### Information about the model
    :::matlab
    >> nodal_coordinates         % the full nodal coordinates list
    nodal_coordinates =
        0     0
        1     0
        1     1
    >> element_nodes             % the full element nodes list
    element_nodes =
        1     2
        2     3
        1     3
    >> % coordinates of node 2
    >> nodal_coordinates(2,:)    % from nodal_coordinates, pick row 2, all columns (x and y)
    ans =
        1     0
    >> % nodes of element 2
    >> element_nodes(2,:)        % from element_nodes, pick row 2, all columns (all nodes)
    ans =
        2     3
    >> % coordinates of element 2
    >> nodal_coordinates(element_nodes(2,:),:) % find the coordinates of the nodes of element 2
    ans =
        1     0
        1     1
    >> element_area(2)           % the cross-sectional area of element 2. Since this is a vector
    ans =                        %   we can be lazy and omit the other index (since it will
        0.0006                   %   always be 1)
    >> element_modulus(2)        % the modulus of element 2
    ans =
    2.1000e+11
    
### What about the element lengths?
The length of the element is also a factor. However, we don't need to input this information, since is is implicit in the nodal coordinates and element definitions. We could write a function to calculate it for us:
    
    #!matlab
    function [element_length] = calculate_length(arguments)
    % A function to calculate the length(s) of an element/ all the elements

    % define the function here!
    return;

The function will implement (for the 2D case):
\begin{align}
L = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\end{align}

![Element length calculation](/images/elementlength_calc.png)

Which arguments? A function is self contained, so it only has access to the variables that are passed to it.

Should we calculate all the lengths in one go, or calculate the length of one specified element?

### Solver--general

A reminder of the global system being solved ($\mathbf{u}$ is the unknown):
\begin{align}
 [K]\{u\} = \{F\}
\end{align}
This is a simultaneous system of equations. Each element must satisfy:
\begin{align}
 [K^e]\{u^e\} = \{F^e\}
\end{align}

The element solution vector ($\mathbf{u}^e$) defines the displacement of the element. It has 4 components, or **degrees-of-freedom**: $u_1, v_1, u_2, v_2$. We can choose to order these:
 \begin{align}
  \mathbf{u}^e = 
  \begin{Bmatrix}
    u_1\\v_1\\u_2\\v_2
  \end{Bmatrix}
  \text{ or }
  \begin{Bmatrix}
    u_1\\u_2\\v_1\\v_2
  \end{Bmatrix}
 \end{align}

![Degrees-of-freedom on a truss](/images/elementdisp.png)

The global solution vector is similar. We should choose and stick to one DOF ordering system.

### Solver--element matrices, local coordinates

We know the stiffness of a beam, $k$, in its longitudinal direction is given by:

\begin{align}
 k = \frac{EA}{L}
\end{align}

![Degrees-of-freedom in the local coordinate system](/images/elementlocal.png)

This corresponds to the direction $x'$ in the local coordinate system $(x',y')$, with associated displacements $(u',v')$, *i.e.* the system:
\begin{align}
 \begin{bmatrix}
  k & 0 & -k & 0 \\
  0 & 0 &  0 & 0 \\
 -k & 0 &  k & 0 \\
  0 & 0 &  0 & 0
 \end{bmatrix}
 \begin{Bmatrix}
  u'_1\\v'_1\\u'_2\\v'_2
 \end{Bmatrix}
 = 
 \begin{Bmatrix}
  F^{x'}_{1}\\F^{y'}_{1}\\F^{x'}_{2}\\F^{y'}_{2}
 \end{Bmatrix}
\end{align}

### Solver--local element matrices in MATLAB

We know how to get $E,A,\text{ and }L$ from the input data for a given element. We know how to create empty matrices, and how to get data into them.

So, creating the element stiffness matrices in the element coordinate system ($\mathbf{K}'^e$) should be simple!

Once we know how to calculate a single element, we can wrap the code in a loop to calculate for all the elements:
    
    #!matlab
    for element = 1:size(element_nodes,1) % total number of elements is given by the
                                        %   number of rows in the element nodes list
        E = element_modulus(element);     
        A = ...                           % collect all the parameters we need to
        ...                               %   calculate k

        k = ...                           % calculate k

        Ke_local = zeros(4,4);            % prepare an empty matrix for the local element
                                        %   stiffness matrix

        Ke_local(1,1) = ...               % put the relevant terms into the matrix!
    end

### Solver--element matrices in global coordinates
 Each node will have a displacement. So far, we've described that displacement in a local (element) coordinate system $(x',y')$. Where a node is shared by two elements, which element's coordinate system should be used?

 All the displacements shoud be expressed in the **global coordinate system**, $(x,y)$.

 The global and local coordinate systems can be transformed using the transformation matrix, $\mathbf{T^{\ast}}$ (in 2D):
 
\begin{align}
 \begin{Bmatrix}
  u' \\ v'
 \end{Bmatrix}
 &=
 \begin{bmatrix}
  \cos\theta & \sin\theta \\
 -\sin\theta & \cos\theta
 \end{bmatrix}
 \begin{Bmatrix}
  u \\ v
 \end{Bmatrix}
 & 
 \mathbf{u}' &= \mathbf{T^{\ast}}\mathbf{u}
\end{align}
Which allows us to perform the transform of the element local stiffness matrix:
\begin{align}
 \mathbf{K}^e = \mathbf{T}^T \mathbf{K}'^{e} \mathbf{T}
\end{align}

where in the case of a 2 node element,

\begin{align}
\mathbf{T} = \begin{bmatrix}\mathbf{T^{\ast}} & 0 \\ 0 & \mathbf{T^{\ast}}\end{bmatrix}
\end{align}

### Element transform in MATLAB

We need to know the angle, $\theta$ of the element. We could write a function, similar to our `calculate_length` function:

    #!matlab
    function [element_angle] = calculate_angle(arguments)
    % A function to calculate the angle of the elements
    % Think about which variables need to be passed in to calculate
    %   the angles
    % MATLAB's atan2 function might be useful here...
    return;

We could also do with a function to give us a transform matrix for any angle `theta`:

    #!matlab
    function [T] = transformmatrix(theta)
    % A function to calculate the transform matrix
    T = zeros(4,4);              % create an empty matrix
    T(1,1) = cos(theta);         % start filling it in...
    ...
    return;

Then, in the element loop, we can add the following lines:

    #!matlab
    theta = element_angle(element); % get the angle of the current element
    T = transformmatrix(theta);     % calculate the transform matrix
    Ke = T' * Ke_local * T;         % transform the local element stiffness matrix

### The global stiffness matrix

Now we have $\mathbf{K}^e$ for all the elements, we can construct the global stiffness matrix. This is a process called **assembly** or **scattering**.
Each of our elements had 4 DOF, (2 displacement components, $u$ and $v$, at each end of the element), and hence a $4\times4$ $\mathbf{K}^e$. We can calculate the size of $\mathbf{K}$ using the total number of degrees of freedom:

    :::matlab
    globaldof = size(nodal_coordinates,1) * size(nodal_coordinates,2);

Each element's stiffness contribution to the global stiffness matrix must be added in at the appropriate position.

### Scattering

Example: element 3 connects nodes 1 and 3 (`element_nodes(3,:)`):

Element stiffness matrix:
\begin{align*}
 \begin{array}{r}
  1, \mathbf{1}, x \\
  1, \mathbf{1}, y \\
  2, \mathbf{3}, x \\
  2, \mathbf{3}, y \\
 \end{array}
 \begin{bmatrix}
  k^{3}_{11} & k^{3}_{12} &  k^{3}_{13} & k^{3}_{14} \\  
  k^{3}_{21} & k^{3}_{22} &  k^{3}_{23} & k^{3}_{24} \\
  k^{3}_{31} & k^{3}_{32} &  k^{3}_{33} & k^{3}_{34} \\
  k^{3}_{41} & k^{3}_{42} &  k^{3}_{43} & k^{3}_{44}
 \end{bmatrix}
\end{align*}
Global stiffness matrix:
\begin{align*}
 \rightarrow
 \begin{bmatrix}
  k^{3}_{11} & k^{3}_{12} & 0 & 0 &  k^{3}_{13} & k^{3}_{14} \\  
  k^{3}_{21} & k^{3}_{22} & 0 & 0 &  k^{3}_{23} & k^{3}_{24} \\
  0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 \\
  k^{3}_{31} & k^{3}_{32} & 0 & 0 &  k^{3}_{33} & k^{3}_{34} \\
  k^{3}_{41} & k^{3}_{42} & 0 & 0 &  k^{3}_{43} & k^{3}_{44}
 \end{bmatrix}
 \begin{array}{l}
  \mathbf{1}, x \\
  \mathbf{1}, y \\
  \mathbf{2}, x \\
  \mathbf{2}, y \\
  \mathbf{3}, x \\
  \mathbf{3}, y
 \end{array}
\end{align*}

($1$:local or element node numbers; $\mathbf{1}$: global node numbers)

### The scattering process in MATLAB

    #!matlab
    K = zeros( );      % create an empty stiffness matrix of appropriate size

    for element = 1:size(element_nodes,1) 
        ...            % calculate all the terms necessary to give:
        Ke = ...       %   element stiffness matrix

        for local_node_number_r = 1:2      % loop through each node in the ROWS direction
            % First we figure out which global node this refers to:
            global_node_number_r = element_nodes(element,local_node_number_r);

            % Then we figure out where in the stiffness matrix the terms are:
            local_index_r  = 2*( local_node_number_r - 1) + [1 2];
            global_index_r = 2*(global_node_number_r - 1) + [1 2];

            for local_node_number_c = 1:2  % loop through each node in the COLUMNS direction
                % Follow the same process for the COLUMNS
                global_node_number_c = element_nodes(element,local_node_number_c);
                local_index_c  = 2*( local_node_number_c - 1) + [1 2];
                global_index_c = 2*(global_node_number_c - 1) + [1 2];

                % Then, we can add the relevant terms to the global stiffness matrix, K
                K(global_index_r,global_index_c) = K(global_index_r,global_index_c) ...
                                                + Ke(local_index_r,local_index_c);
            end
        end
    end


### The force vector

We have our stiffness matrix. We also need the force vector, $F$.

Remember, when we input this, we input it in the form:
 \begin{align}
  \begin{bmatrix}
   F_{x}^{1} & F_{y}^{1} \\
   F_{x}^{2} & F_{y}^{2} \\
   F_{x}^{3} & F_{y}^{3} 
  \end{bmatrix}
 \end{align}

but we really need it as a vector, with the same ordering scheme as the stiffness matrix:

 \begin{align}
  \begin{bmatrix}
   F_{x}^{1} \\ F_{y}^{1} \\
   F_{x}^{2} \\ F_{y}^{2} \\
   F_{x}^{3} \\ F_{y}^{3} 
  \end{bmatrix}
 \end{align}
 
We need to perform a similar scattering operation to form $F$. We only need 1 loop, since there is only 1 column in the vector.

### Applying boundary conditions

At the moment, the system is unconstrained: this means that there is no unique solution, and rigid body motion can occur. We need to input some boundary conditions:

  \begin{align}
   \begin{bmatrix}
    1 & 1 \\
    0 & 1 \\
    0 & 0
   \end{bmatrix}
   \begin{array}{l}
    \text{node 1: constrained (1) in x and y directions} \\
    \text{node 2: sliding joint, constrained in y only} \\
    \text{node 3: free: not constrained at all}
   \end{array}
  \end{align}

where $1$ indicates that a degree of freedom is constrained to no displacement.

The boundary condition is applied by eliminating the row and column relevent to the degree of freedom in the system of equations.

### Applying boundary conditions in MATLAB

Removing rows and columns from the matrix will change their size, and we might lose track of which row/column corresponds to which displacement. Instead, we can achieve the same by replacing the rows and columns by the relevant bits of the identity matrix:

\begin{align}
 \begin{bmatrix}
  k_{11} & k_{12} &  k_{13} & k_{14} \\  
  k_{21} & k_{22} &  k_{23} & k_{24} \\
  k_{31} & k_{32} &  k_{33} & k_{34} \\
  k_{41} & k_{42} &  k_{43} & k_{44}
 \end{bmatrix}
 \begin{Bmatrix}
  u_1 \\ v_1 \\ u_2 \\ v_2
 \end{Bmatrix}
 = 
 \begin{Bmatrix}
  F_{1}^{x} \\ F_{1}^{y} \\ F_{2}^{x} \\ F_{2}^{y}
 \end{Bmatrix}
\end{align}

Constraining $v_1=0$, 

\begin{align}
 \begin{bmatrix}
  k_{11} & 0 &  k_{13} & k_{14} \\  
  0      & 1 &  0      & 0      \\
  k_{31} & 0 &  k_{33} & k_{34} \\
  k_{41} & 0 &  k_{43} & k_{44}
 \end{bmatrix}
 \begin{Bmatrix}
  u_1 \\ v_1 \\ u_2 \\ v_2
 \end{Bmatrix}
 = 
 \begin{Bmatrix}
  F_{1}^{x} \\ 0 \\ F_{2}^{x} \\ F_{2}^{y}
 \end{Bmatrix}
\end{align}

Applying this process in MATLAB should be easy:

    #!matlab
    % in a loop iterating over the boundary conditions...

    if boundary_condition(i) == 1          % check if we need to constrain displacement
        
        % STIFFNESS MATRIX
        K(i,:) = 0;                        % set the whole row to zero
        K(:,i) = 0;                        % set the whole column to zero

        K(i,i) = 1;                        % set the term on the diagonal to 1

        % FORCE VECTOR
        F(i)   = 0;                        % set the term in the force vector to zero

    end

### Solving

Now all our hard work is done. The system is set up, and all that remains is for MATLAB to solve it for the unknowns (in our case, displacements). We saw how to do this using the MATLAB `backslash` operator earlier:

    #!matlab
    % Solve the system [K]{u} = {F} for unknown {u}
    u = K\F;

### Post processor

Once the displacements $\mathbf{u}$ are determined, calculating the strain shouldn't be difficult. Strain is given by:

  \begin{align}
    \varepsilon_{x'} = \frac{\partial u'}{\partial x'} = \frac{\Delta L}{L}
  \end{align}

where $\Delta L$ is the change in length of the element. The new length of the element (after displacement) is given by the length calculated using the original coordinates, $\mathbf{x}$, plus the displacements $\mathbf{u}$. In fact, we could probably reuse our function `calculate_length()`.

Knowing the strains, stresses are then trivial to calculate.

### Conclusions

Not all the required code has been given here, but there is enough to construct a simple beam element finite element code, in 1-, 2- or 3-D as required. Using information from earlier in the FE course, it should be possible to add in moment sustaining elements.
 
* The easiest way to get started in MATLAB is just to play with it
* Begin by using it as a calculator - a single operation at a time, rather than as a full programming language
* MATLAB 'thinks' in matrices: once the matrices are defined, MATLAB understands what it means  to e.g. multiply matrices
* Even when using it as a programming language, it's easy to go back to the command line and try typing a line in to see what it does

