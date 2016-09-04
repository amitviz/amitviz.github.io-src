Title: Introduction to Matlab: lecture 2
Date: 2011-11-01
Category: Notes
Tags: matlab, code, teaching, bath
Slug: matlabbeamfe
Authors: Amit
Status: draft

## Beam Finite Element Analysis
### \mode<presentation>{Part 2: Finite Element Analysis}}
  Here, we're going to take a brief overview of the steps required in producing a Finite Element (FE) programme for beam analysis.
  
    \item \textbf{Not all the answers are in these notes!}
    \item There should be enough hints to produce a 2D FE code.
    \item If we can produce a 2D code, extending it to 3D should be trivial.
  
\end{frame}

### Parts of an FE programme}
\begin{columns}
\mode<article>{\begin{tabular}{p{0.33\textwidth}p{0.33\textwidth}p{0.33\textwidth}}}
  \column{0.33\textwidth}
     \begin{footnotesize}
      
        \item component shape
        \item materials
        \item loads
      
    \end{footnotesize}
  \column{0.33\textwidth}\mode<article>{&}
    % empty column
  \column{0.33\textwidth}\mode<article>{&}
     \begin{footnotesize}
      
        \item does my component work?
      
    \end{footnotesize}
\mode<article>{\end{tabular}}
\end{columns}

\begin{center}
  \includefigure{width=1.0\textwidth}{width=1.0\textwidth}{fea2}
\end{center}

\begin{columns}
\mode<article>{\begin{tabular}{p{0.33\textwidth}p{0.33\textwidth}p{0.33\textwidth}}}
  \column{0.33\textwidth}
     \begin{footnotesize}
      
        \item digital representation: `geometry'
        \item mathematical representation of material behaviour
        \item discretization: `meshing'
      
    \end{footnotesize}
  \column{0.33\textwidth}\mode<article>{&}
     \begin{footnotesize}
      
        \item form element stiffness matrices
        \item assemble global matrices
        \item apply boundary conditions
        \item solve for nodal unknowns
      
    \end{footnotesize}
  \column{0.33\textwidth}\mode<article>{&}
     \begin{footnotesize}
      
        \item calculate derived quantities, e.g. strains, stresses, thermal gradients
        \item plotting and visualization tools
      
    \end{footnotesize}
\mode<article>{\end{tabular}}
\end{columns}

\end{frame}

### Problem definition}
\begin{columns}
\column{0.5\textwidth}
\mode<presentation>{
\begin{center}
  \includefigure{width=1.0\textwidth}{width=0.5\textwidth}{2dbeams}
\end{center}
}
\column{0.5\textwidth}
\textbf{Truss} or \textbf{beam} elements

 \item defined by length $L$, area $A$, modulus $E$
 \item pin-jointed
 \item uniform strain
 \item fixed locations, sliding joints, free joints

Solve for displacements $\mathbf{u}$ (vector quantity), strains and stresses.
\end{columns}
\end{frame}

### Pre-processor}
The problem definition already represents a suitable mesh: `elements' correspond to beams, `nodes' correspond to joints.

 \item a \textbf{node} is defined by its coordinates
 \item an \textbf{element} is defined by the nodes it connects

We can input these data directly in the form of a list (of course, MATLAB calls this a `matrix'). It's also useful to input the moduli and areas: also as a list, since they might not be the same for all beams.
\begin{columns}
\column{0.4\textwidth}
\begin{center}
  \includefigure{width=1.0\textwidth}{width=0.5\textwidth}{2dbeams_annotated}
\end{center}
\column{0.6\textwidth}
\mfile{preproc.m}
Remember: unit consistency!
\end{columns}
\end{frame}

### Information about the model}
\label{meshinfo}
\mfile{preproc2.m} 
\end{frame}

### What about the element lengths?}
\label{elementlengthfunction}
 The length of the element is also a factor. However, we don't need to input this information, since is is implicit in the nodal coordinates and element definitions. We could write a function to calculate it for us:
\mfile{lengthfunctionprototype.m}
\begin{columns}
\column{0.6\textwidth}
The function will implement (for the 2D case):
\begin{align}
 L = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\end{align}
\column{0.4\textwidth}
\begin{center}
  \includefigure{width=0.6\textwidth}{width=0.3\textwidth}{elementlength_calc}
\end{center}
\end{columns}
Which arguments? A function is self contained, so it only has access to the variables that are passed to it.

Should we calculate all the lengths in one go, or calculate the length of one specified element?
\end{frame}

### Solver---general}
A reminder of the global system being solved ($\mathbf{u}$ is the unknown):
\begin{align}
 [K]\{u\} = \{F\}
\end{align}
This is a simultaneous system of equations. Each element must satisfy:
\begin{align}
 [K^e]\{u^e\} = \{F^e\}
\end{align}
\begin{columns}
 \column{0.6\textwidth}
 The element solution vector ($\mathbf{u}^e$) defines the displacement of the element. It has 4 components, or \textbf{degrees-of-freedom}: $u_1, v_1, u_2, v_2$. We can choose to order these:
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
 \column{0.4\textwidth}
\begin{center}
 \includefigure{width=0.8\textwidth}{width=0.30\textwidth}{elementdisp}
\end{center}
\end{columns}
The global solution vector is similar. We should choose and stick to one DOF ordering system.
\end{frame}

### Solver---element matrices, local coordinates}
 We know the stiffness of a beam, $k$, in its longitudinal direction is given by:
\begin{columns}
 \column{0.5\textwidth}
\begin{align}
 k = \frac{EA}{L}
\end{align}
 \column{0.5\textwidth}
 \begin{center}
 \includefigure{width=0.64\textwidth}{width=0.32\textwidth}{elementlocal}
 \end{center}
\end{columns}
This corresponds to the direction $x'$ in the local coordinate system $(x',y')$, with associated displacements $(u',v')$, i.e. the system:
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
\end{frame}

### Solver---local element matrices in MATLAB}
\label{elementmatrices}
 We know how to get $E,A,\text{ and }L$ from the input data for a given element, (slide~\ref{meshinfo}).

 We know how to create empty matrices (slide~\ref{usefulmatrices}), and how to get data into them (slide~\ref{matrixaddressing}).

 So, creating the element stiffness matrices in the element coordinate system ($\mathbf{K}'^e$) should be simple!

 Once we know how to calculate a single element, we can wrap the code in a loop to calculate for all the elements:
\mfile{elementmatrices.m} 
\end{frame}

### Solver---element matrices in global coordinates}
 Each node will have a displacement. So far, we've described that displacement in a local (element) coordinate system $(x',y')$. Where a node is shared by two elements, which element's coordinate system should be used?

 All the displacements shoud be expressed in the \textbf{global coordinate system}, $(x,y)$.

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
where in the case of a 2 node element, $\mathbf{T} = \begin{bmatrix}\mathbf{T^{\ast}} & 0 \\ 0 & \mathbf{T^{\ast}}\end{bmatrix}$.
\end{frame}

### Element transform in MATLAB}
We need to know the angle, $\theta$ of the element. We could write a function, similar to our \mcode{calculate_length} function:
\mfile{anglefunctionprototype.m}
We could also do with a function to give us a transform matrix for any angle \mcode{theta}:
\mfile{transformfunctionprototype.m}
Then, in the element loop (slide~\ref{elementmatrices}), we can add the following lines:
\mfile{elementtransformation.m}
\end{frame}

### The global stiffness matrix}
 Now we have $\mathbf{K}^e$ for all the elements, we can construct the global stiffness matrix. This is a process called \textbf{assembly} or \textbf{scattering}.
 Each of our elements had 4 DOF, (2 displacement components, $u$ and $v$, at each end of the element), and hence a $4\times4$ $\mathbf{K}^e$. We can calculate the size of $\mathbf{K}$ using the total number of degrees of freedom:
\mfile{globaldof.m}
Each element's stiffness contribution to the global stiffness matrix must be added in at the appropriate position.
\end{frame}

### Scattering}
Example: element 3 connects nodes 1 and 3 (\mcode{element_nodes(3,:)}).
Element stiffness matrix:
\begin{align*}
 \begin{array}{r}
  \text{\ding{192}, \ding{202}} x \\
  \text{\ding{192}, \ding{202}} y \\
  \text{\ding{193}, \ding{204}} x \\
  \text{\ding{193}, \ding{204}} y \\
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
  \text{\ding{202}} x \\
  \text{\ding{202}} y \\
  \text{\ding{203}} x \\
  \text{\ding{203}} y \\
  \text{\ding{204}} x \\
  \text{\ding{204}} y
 \end{array}
\end{align*}
(\ding{192}:local or element node numbers; \ding{202}: global node numbers)
\end{frame}

### The scattering process in MATLAB}
 \mfile{scattering.m}
\end{frame}

### The force vector}
 We have our stiffness matrix. We also need the force vector, $F$.
 
\begin{columns}[t]
 \column{0.5\textwidth}
Remember, when we input this, we input it in the form:
 \begin{align}
  \begin{bmatrix}
   F_{x}^{1} & F_{y}^{1} \\
   F_{x}^{2} & F_{y}^{2} \\
   F_{x}^{3} & F_{y}^{3} 
  \end{bmatrix}
 \end{align}
 \column{0.5\textwidth}
but we really need it as a vector, with the same ordering scheme as the stiffness matrix:
 \begin{align}
  \begin{bmatrix}
   F_{x}^{1} \\ F_{y}^{1} \\
   F_{x}^{2} \\ F_{y}^{2} \\
   F_{x}^{3} \\ F_{y}^{3} 
  \end{bmatrix}
 \end{align}
\end{columns}
 
We need to perform a similar scattering operation to form $F$. We only need 1 loop, since there is only 1 column in the vector.
\end{frame}

### Applying boundary conditions}
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
where `$1$' indicates that a degree of freedom is constrained to no displacement.

The boundary condition is applied by eliminating the row and column relevent to the degree of freedom in the system of equations.
\end{frame}

### Applying boundary conditions in MATLAB}
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
\end{frame}

### Applying boundary conditions in MATLAB II}
  Applying this process in MATLAB should be easy:
  \mfile{applybc.m}
\end{frame}

### Solving}
  Now all our hard work is done. The system is set up, and all that remains is for MATLAB to solve it for the unknowns (in our case, displacements). We saw how to do this using the MATLAB `backslash' operator earlier:
  \mfile{solve.m}
\end{frame}

### Post processor}
  Once the displacements $\mathbf{u}$ are determined, calculating the strain shouldn't be difficult. Strain is given by:
  \begin{align}
    \varepsilon_{x'} = \frac{\partial u'}{\partial x'} = \frac{\Delta L}{L}
  \end{align}
 where $\Delta L$ is the change in length of the element. The new length of the element (after displacement) is given by the length calculated using the original coordinates, $\mathbf{x}$, plus the displacements $\mathbf{u}$. In fact, we could probably reuse our function \mcode{calculate_length()}.

 Knowing the strains, stresses are then trivial to calculate.
\end{frame}

### Conclusions}
  Not all the required code has been given here, but there is enough to construct a simple beam element finite element code, in 1-, 2- or 3-D as required. Using information from earlier in the FE course, it should be possible to add in moment sustaining elements.
 
   \item The easiest way to get started in MATLAB is just to play with it
   \item Begin by using it as a calculator - a single operation at a time, rather than as a full programming language
   \item MATLAB `thinks' in matrices: once the matrices are defined, MATLAB understands what it means  to e.g. multiply matrices
   \item Even when using it as a programming language, it's easy to go back to the command line and try typing a line in to see what it does
 
\end{frame}
