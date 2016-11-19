Title: Introduction to Matlab: lecture 4
Date: 2011-11-15
Category: Notes
Tags: matlab, code, teaching, bath
Slug: matlabbeamfe2
Authors: Amit
Status: draft

# Completing the beam FE program







\section{Aligned boundary conditions in the solver}

\begin{frame}{\mode<presentation>{Aligned boundary conditions in the solver}}
  The code developed for the solver in the previous lecture applied boundary conditions only in the global coordinate system ($u=0$ or $v=0$). To make the code a bit more general, we should handle aligned supports ($u'=0$ or $v'=0$).
  \begin{center}
  \includefigure{width=0.4\textwidth}{width=0.3\textwidth}{alignedbc}
  \end{center}
\end{frame}

\begin{frame}{Solution vector}
\begin{columns}
  \column{0.5\textwidth} Instead of solving for the a solution vector of the form:
 \begin{align}
  \mathbf{u} &= 
  \begin{Bmatrix}
    u_1\\v_1\\u_2\\v_2\\u_3\\v_3
  \end{Bmatrix}
 \end{align}
  \column{0.5\textwidth} we can look first for a solution of the form:
 \begin{align}
  \mathbf{u^\ast} &=
  \begin{Bmatrix}
    u_1\\v_1\\u_2\\v_2\\u'_3\\v'_3
  \end{Bmatrix}
 \end{align}
\end{columns}
where $\mathbf{u^\ast} = \mathbf{T}\mathbf{u}$, and 
\begin{align}
  \mathbf{T} &= \begin{bmatrix}
         I & 0 & 0 \\
         0 & I & 0 \\
         0 & 0 & t_3
       \end{bmatrix}
\end{align}
and $t_3$ is the transformation matrix for the orientation of the third node. We already have a function that calculates the transformation matrix.
\end{frame}

\begin{frame}{Implementing the boundary conditions}
  The information required for aligned boundary conditions is:
\begin{itemize}
  \item the node
  \item the orientation
  \item the restrained degrees of freedom
\end{itemize}
Instead of listing all the nodes as we have done previously for globally oriented boundary conditions, we can list just the required information:
\mfile{alignedbc.m}
e.g. to constrain node 2 of element 3 to only move in the $x'$ direction:
\mfile{alignedbcexample.m}
\end{frame}

\begin{frame}{Writing the MATLAB code}
  Writing the MATLAB code should be easy: we've already covered the loops and logic, and some of the functions (e.g. the transform matrix) already exist. Some other elements that need to change are:
  \begin{itemize}
    \item $\mathbf{F^\ast} = \mathbf{T}\mathbf{F}$
    \item $\mathbf{K^\ast} = \mathbf{T}\mathbf{K}\mathbf{T}^T$
  \end{itemize}
Remember, we're now solving the system:
\begin{align}
  \mathbf{K^\ast}\mathbf{u^\ast} &= \mathbf{F^\ast}
\end{align}
for the unknown vector $\mathbf{u^\ast}$: to get the global displacements ($\mathbf{u}$) back, we need to calculate:
\begin{align}
  \mathbf{u} &= \mathbf{T}^T\mathbf{u^\ast}
\end{align}
(recall that $\mathbf{T}^{-1} = \mathbf{T}^T$) 
\end{frame}

\section{`Frame' elements and shape functions}

\begin{frame}{\mode<presentation>{Shape functions and `frame' elements}}
  A frame element can sustain a bending moment or a transverse load. (Unlike the truss element.)

  Each node on the frame element has 3 degrees of freedom:
  \begin{itemize}
   \item displacement in $x$-direction ($u$)
   \item displacement in $y$-direction ($v$)
   \item rotation ($\phi$)
  \end{itemize}
  \begin{center}
    %\includefigure{width=0.5\textwidth}{width=0.32\textwidth}{frameelementlocal}
    \mode<presentation>{\def\svgwidth{0.5\textwidth}}
    \mode<article>{\def\svgwidth{0.32\textwidth}}
    \input{./figures/frameelementlocaltex.tex}
  \end{center}
\end{frame}

\begin{frame}{Frame element stiffness matrix}
The terms in the stiffness matrix can still be calculated directly.

The stiffness matrix for a 2-node frame element, with a solution vector of the form $\mathbf{u}'_e = [u'_1, v'_1, \phi_1, u'_2, v'_2, \phi_2]^T$ is:
 \begin{align}
   \mathbf{K}'_{e} = 
   \begin{bmatrix}
      k_{r} &  0       &  0           & -k_{r} &  0       & 0           \\
      0     &  12k_{b} &  6Lk_{b}     &  0     & -12k_{b} & 6Lk_{b}     \\
      0     &  6k_{b}  &  4L^{2}k_{b} &  0     &  -6k_{b} & 2L^{2}k_{b} \\
     -k_{r} &  0       &  0           &  k_{r} &  0       & 0           \\
      0     & -12k_{b} & -6Lk_{b}     &  0     &  12k_{b} & -6Lk_{b}    \\
      0     &  6k_{b}  &  2L^{2}k_{b} &  0     &  -6k_{b} & 4L^{2}k_{b}
   \end{bmatrix}
 \end{align}
where
 \begin{align}
  k_{r} &= \frac{AE}{L} & k_{b} &= \frac{EI}{L^3}
 \end{align}
\end{frame}

\begin{frame}{Solution of frame element system}
 The global stiffness matrix is formed in the same way it was for the truss element: only now, each node has 3 degrees-of-freedom.

 The element local displacement and element global force vectors take the form:
 \begin{align}
  \mathbf{u}'_e &= \begin{Bmatrix}u'_1 \\ v'_1 \\ \phi_1 \\ u'_2 \\ v'_2 \\ \phi_2\end{Bmatrix}
  &
  \mathbf{F}_e &= \begin{Bmatrix}F_x \\ F_y \\ M \\ F_x \\ F_y \\ M\end{Bmatrix}
 \end{align}

 The transformation matrix $\mathbf{T}$ needs to be modified to account for this extra degree of freedom. A rotational transform to the global coordinate system does not affect the nodal rotations or applied moments (i.e. $\phi = \phi'$, $M = M'$), so we can just insert the identity (i.e. $1$) in the relevant degrees-of-freedom.
\end{frame}

\begin{frame}{Postprocessing frame elements}
 The truss element exhibits uniform strain, i.e. the strain does not vary with $x'$. The frame element is capable of varying the strain along its length. Additionally, the element defines displacement (and hence strains) in the $y'$ direction. To determine displacement (and other derived quantities) at a point, we require the use of shape functions.

 If $\xi$ is a parametric coordinate along the length of the element, the displacements at any value of $\xi$ can be given by:
 \begin{align}
  u'_{x}(\xi) &= \sum_{i=1}^{n} N_{i}(\xi) u'_{x,n}\\
  \mathbf{u}'(\xi) &= \mathbf{N}(\xi)\mathbf{u}'_e \\
  \begin{Bmatrix}u'(\xi) \\ v'(\xi)\end{Bmatrix} &=
  \begin{bmatrix}
   N_{1x} & 0 & 0 & N_{2x} & 0 & 0 \\
   0 & N_{1y} & N_{1\theta} & 0 & N_{2y} & N_{2\theta} 
  \end{bmatrix}
  \begin{Bmatrix}
   u'_1 \\ v'_1 \\ \phi_1 \\ u'_2 \\ v'_2 \\ \phi_2
  \end{Bmatrix} \label{eq:shapefunction}
 \end{align}
\end{frame}

\begin{frame}{Shape functions for frame elements}
The shape functions for a frame element are defined for $-1\le\xi\le1$, and requires the length of the element $L$:
 \begin{align}
  N_{1x}(\xi) &= (1-\xi)/2 \nonumber \\
  N_{1y}(\xi) &= [1-\xi(3-\xi^2)/2]/2 \nonumber \\
  N_{1\theta}(\xi) &= \frac{L(1-\xi^2)}{8}(1-\xi) \nonumber \\
  N_{2x}(\xi) &= (1+\xi)/2 \nonumber \\
  N_{2y}(\xi) &= [1+\xi(3-\xi^2)/2]/2 \nonumber \\
  N_{2\theta}(\xi) &= \frac{-L(1-\xi^2)}{8}(1+\xi) \label{eq:shapefunctions}
 \end{align}
In MATLAB, we can write a function to return the shape function matrix:
 \mfile{shapefunction.m}
\end{frame}

\begin{frame}{Determining the displacement in MATLAB}
 Once the shape function matrix $\mathbf{N}$ is known, the displacements at any point can be determined.
 \mfile{displacements.m}
 where \mcode{ue_local} are the element nodal displacements. \mcode{ue_local} is determined by picking out the relevant nodal displacements for the element of interest from the global solution vector, and transforming back to the element's local coordinate system $(x',y')$.

To get displacements along the element, we can increment $\xi$, e.g. \mcode{xi = -1:0.1:1}.
\end{frame}

\begin{frame}{Derived quantities}
 Once displacements are known, the derived quantities (strains and stresses) can be calculated. The strain and bending moment are given by:
\begin{columns}
 \column{0.5\textwidth}
 \begin{align}
  \varepsilon_{x'}(x',\bar{y}) &= \frac{\mathrm{d}u'}{\mathrm{d}x'} -\bar{y}\frac{\mathrm{d}^2v'}{\mathrm{d}x'^2} \label{eq:strain} \\
  M(x') &= EI \frac{\mathrm{d}^2v'}{\mathrm{d}x'^2} \label{eq:bendingmoment}
 \end{align}
 \column{0.5\textwidth}
 \begin{center}
  \includefigure{width=0.7\textwidth}{width=0.4\textwidth}{neutralaxis}
 \end{center}
\end{columns}

\begin{itemize}
 \item $\bar{y}$ is the distance from the neutral axis
 \item $\frac{\mathrm{d}u'}{\mathrm{d}x'}$ is the mean axial strain---this is the same as it is for the truss element (previous lecture)
 \item $-\bar{y}\frac{\mathrm{d}^2v'}{\mathrm{d}x'^2}$ is the bending strain
\end{itemize}
Once the strains are known, calculating the stress is trivial.
\end{frame}

\begin{frame}{Differentiating the displacements}

We know the displacements in terms of the parametric coordinate, $\xi$, from equation \eqref{eq:shapefunction}. This parametric coordinate is a transform of the element coordinate system:
\begin{itemize}
 \item The range $0 \le x' \le L$ is mapped to $-1 \le \xi \le +1$
\end{itemize}
i.e. 
\begin{align}
 \xi(x') &= 2\frac{x'}{L} - 1 \label{eq:xixtransform}
\end{align}
if
\begin{align}
 \mathbf{u}'(\xi) &= \mathbf{N}(\xi) \mathbf{u}'_{e}
\end{align}
then
\begin{align}
 \frac{\mathrm{d}\mathbf{u}'(\xi)}{\mathrm{d}x'} &= \frac{\mathrm{d}\mathbf{N}(\xi)}{\mathrm{d}x'} \mathbf{u}'_{e}
\end{align}
($\mathbf{u}'_e$ are the discrete (nodal) values of the displacement, they are not a differentiable function.)
\end{frame}

\begin{frame}{Differentiating the shape function}
 The shape functions, given in equations \eqref{eq:shapefunctions}, are given in terms of $\xi$. To differentiate with respect to the local coordinate system ($x'$):
\begin{align}
 \frac{\mathrm{d}\mathbf{N}}{\mathrm{d}x'} &= \frac{\mathrm{d}\mathbf{N}}{\mathrm{d}\xi} \frac{\mathrm{d}\xi}{\mathrm{d}x'}
\end{align}
where $\mathrm{d}\xi/\mathrm{d}x'$ is given by differentiating \eqref{eq:xixtransform}, and is known as the Jacobian ($J$) of the transform. Similarly, 
\begin{align}
 \frac{\mathrm{d}^2\mathbf{N}}{\mathrm{d}x'^2} &= \frac{\mathrm{d}}{\mathrm{d}x'} \frac{\mathrm{d}\mathbf{N}}{\mathrm{d}x'} \nonumber \\
 &= \frac{\mathrm{d}}{\mathrm{d}x'} \frac{\mathrm{d}\mathbf{N}}{\mathrm{d}\xi} \frac{\mathrm{d}\xi}{\mathrm{d}x'} \nonumber \\
 &= \frac{\mathrm{d}}{\mathrm{d}\xi} \frac{\mathrm{d}\mathbf{N}}{\mathrm{d}\xi} \frac{\mathrm{d}\xi}{\mathrm{d}x'} \frac{\mathrm{d}\xi}{\mathrm{d}x'} \nonumber \\
 &= \frac{\mathrm{d}^2\mathbf{N}}{\mathrm{d}\xi^2} \left( \frac{\mathrm{d}\xi}{\mathrm{d}x'} \right)  ^2
\end{align}
\end{frame}

\begin{frame}{Postprocessing in MATLAB}
  We could write some functions, perhaps
\begin{itemize}
 \item \mcode{function N1 = shapefunction_derivative_1(xi,L)} and
 \item \mcode{function N2 = shapefunction_derivative_2(xi,L)}
\end{itemize}
to return the shape function derivative matrices. Since the shape functions are functions of $L$, they will need to be calculated for each element individually.

The Jacobian is also a function of $L$, so will also be calculated for each element.

Then the derivatives can be calculated in the same form as equation \eqref{eq:shapefunction}:
\begin{align}
 \frac{\mathrm{d}\mathbf{u}'}{\mathrm{d}x'} &= J \cdot \mathbf{N}^{(1)} \mathbf{u}'_{e} \\
 \frac{\mathrm{d}^{2}\mathbf{u}'}{\mathrm{d}x'^{2}} &= J^2 \cdot \mathbf{N}^{(2)} \mathbf{u}'_{e}
\end{align}
where $J$ is the Jacobian, and bracketed superscripts denote derivative with respect to the parametric coordinate system.

We now have sufficient information to calculate strains (and stresses) from equation \eqref{eq:strain}
\end{frame}

\section{Postprocessor and plotting}

\begin{frame}{A postprocessor to view the results}
\begin{itemize}
 \item In the previous lecture, the results of the analysis were presented as a MATLAB vector of values.
 \item MATLAB has some powerful plotting functions, so we can try to visualize these results to make them easier to understand.
\end{itemize}
 \begin{center}
  \includefigure{width=0.75\textwidth}{width=0.75\textwidth}{truss_tutorial}
 \end{center}
\end{frame}

\begin{frame}{Saving the results}
So that we don't have to re-run the whole model every time we want to create a plot, we can save the results to a file. 

\mode<article>{This step isn't necessary for the type of problems we might be solving, but when the models become larger and take a significant amount of time to run, it is useful to be able to keep a copy of the solution vector so that it can be processed at a later date.}

MATLAB has a function to allow any variable in memory to be saved to a \mcode{.mat} file:
 \mfile{saveexample.m}
Any string can be given as the filename (i.e. \mcode{filename} should be the name of a string variable, or the string variable itself, enclosed in \mcode{'inverted commas'}). If an extension for the filename isn't specified, most versions of MATLAB will add a \mcode{.mat} at the end.

These variables can be re-read back into memory with the command:
 \mfile{loadexample.m}

\end{frame}

\begin{frame}{The figure window}
\begin{itemize}
 \item The MATLAB command \mcode{figure} creates a new window for a figure (or plot). 
 \item All of the plotting commands create their own figure windows, so it's not necessary to explicitly create a `figure'.
 \item However, it's useful to use this command to ensure that a plot is created on a new figure window, and not an existing window.
\end{itemize}
 \begin{center}
   \includefigure{width=0.5\textwidth}{width=0.5\textwidth}{matlab_figure_blank}
 \end{center}
\end{frame}

\begin{frame}{The plot command}
 The plot command in its simplest form takes two arguments: a vector of $x$-values and a vector of $y$-values, e.g.
 \begin{columns}
  \column{0.5\textwidth} \mfile{plotx2.m}
  \column{0.5\textwidth} \begin{center} \includefigure{width=1.0\textwidth}{width=0.6\textwidth}{x2} \end{center}
 \end{columns}
\end{frame}

\begin{frame}{Formatting the plot}
 A third argument is used in the plot command to control the appearance of the plotted line. Some common options are:
\begin{center}
\rowcolors{1}{black!20}{black!10} 
\begin{tabular}{p{2.5cm}p{7.5cm}}
\textbf{symbol} & \textbf{line style} \\
$-$ & default \\
$--$ & dashed \\
$\colon$ & dotted \\
$-.$ & dash-dot \\
o & circle markers \\
$+$ & plus sign markers \\
$\ast$ & star markers \\
x & cross markers \\
r,g,y,b,k & colour: red, green, yellow, blue, black
\end{tabular}
\end{center}
\end{frame}

\begin{frame}{Using plot styles}
\mfile{plotmesh_nodes.m}
 \begin{center}
   \includefigure{width=0.75\textwidth}{width=0.75\textwidth}{truss_nodes}
 \end{center}

The full details on the capability of the \mcode{plot} command are given by typing \mcode{help plot} at the MATLAB command prompt.
\end{frame}

\begin{frame}{Plot lines}
 To plot the elements, we can use the \mcode{line} command. Before we do this, we use the command
\mfile{holdon.m}
to `hold' the plot, i.e. use the same figure for the next lines rather than creating a new figure window.

The \mcode{line} command is similar to the \mcode{plot} command in that it takes a list of $x$ and $y$ coordinates.
We can use it in a loop, to plot one `\mcode{line}' (with two pairs of $(x,y)$ coordinates) for every element:
\mfile{plotmesh_line.m}
\begin{center}
  \includefigure{width=0.7\textwidth}{width=0.75\textwidth}{truss_mesh}
\end{center}
\end{frame}

\begin{frame}{Adding colour}
 The \mcode{line} function also takes an argument \mcode{color} (note the incorrect spelling).
 Instead of giving the lines colours like 'b' for blue or 'r' for red, we can be more specific about the colour: the red, green and blue components can be specified as a row vector, using values between 0--1. Some examples are:
\begin{center}
\rowcolors{1}{black!20}{black!10} 
\begin{tabular}{p{2.5cm}p{7.5cm}}
\textbf{} & \textbf{colour} \\
\mcode{[0,0,0]} & black \\
\mcode{[1,0,0]} & red \\
\mcode{[0,1,0]} & green \\
\mcode{[0,0,1]} & blue \\
\mcode{[1,0,1]} & purple \\
\mcode{[1,1,1]} & white \\
\mcode{[0.5,0,0.5]} & dark purple
\end{tabular}
\end{center}
We could use the colour to represent one of the postprocressed results, e.g. stress or strain.
\mfile{line.m}
\end{frame}

\begin{frame}{The finished postprocessor with displacements}
\begin{center}
 \includefigure{width=0.7\textwidth}{width=0.75\textwidth}{truss_output}
\end{center}
\begin{itemize}
 \item The displacement is shown by plotting $\mathbf{x} + s\mathbf{u}$, where $s$ is a scaling factor.
 \item the colour represents the stress in the elements: blue is the lowest stress, red is the highest.
\end{itemize}
\end{frame}

\begin{frame}{The displacements for frame elements}
If the displacements are interpolated using the shape functions (at e.g. \mcode{xi = -1:0.1:1}), we can determine the displacements and plot the shape of a frame element. When plotting the line using \mcode{line(x,y)}, the parameters \mcode{x} and \mcode{y} will both be vectors.
\begin{center}
 \includefigure{width=0.7\textwidth}{width=0.75\textwidth}{frame_output}
\end{center}
\begin{itemize}
 \item The line command does not allow for change in colour along the length of a single line, so we can't use this command to plot variables that are a function of $x'$, such as bending moment. 
\end{itemize}
\end{frame}

\section{Conclusions}
\begin{frame}{\mode<presentation>{Conclusions}}
 \begin{itemize}
  \item We now have a pretty complete programme for performing both truss and frame analysis
\begin{itemize}
 \item it can incorporate boundary conditions aligned in the global or the element coordinate systems
 \item it can also calculate the derived quantities in the postprocessor using shape functions and their derivatives
\end{itemize}
  \item We've got an idea of the process of writing a MATLAB programme, including how to step through the code using the debugger to look for errors
  \item We can also use MATLAB to create graphical output to help with the interpretation of results
 \end{itemize}
\end{frame}
