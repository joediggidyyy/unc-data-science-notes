> Markdown version for convenient browsing. Original files:
> - PDF: [DATA750_week1_notes.pdf](../DATA750_week1_notes.pdf)
> - DOCX: [DATA750_week1_notes.docx](DATA750_week1_notes.docx)

---

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 26%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Matrices</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Objectives</td>
<td colspan="2" style="text-align: right;"><strong>06 Jan 2025</strong></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>review linear algebra concepts and terminology</p></li>
<li><p>set up and numerically solve linear systems in Julia</p></li>
<li><p>create and manipulate matrices in Julia</p>
<ol type="1">
<li><p>transposes</p></li>
<li><p>sub-blocks</p></li>
<li><p>sparse matrices</p></li>
</ol></li>
<li><p>recognize an orthogonal matrix and describe its properties</p></li>
<li><p>compute coordinates using a basis, in particular an orthogonal basis</p></li>
<li><p>compute lengths of vectors and find angles of vectors in higher dimensions</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Linear Algebra Review</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><p>Linear algebra provides a way of compactly representing and operating on sets of linear equations. Stanford has a 26-page online linear algebra for machine learning review guide that I recommend. <a href="https://cs229.stanford.edu/section/cs229-linalg.pdf">https://cs229.stanford.edu/section/cs229-linalg.pdf</a></p>
<p>the following data and screenshots are taken from the stanford.edu pdf</p></td>
</tr>
<tr>
<td>Basic Concept</td>
<td colspan="3"><p>represent and operate on sets of linear equations</p>
<p>starting with:</p>
<p><img src="generated_media\DATA750_week1_notes\media\image1.png" style="width:2.06279in;height:0.70843in" /></p>
<p>convert to the form:</p>
<p><img src="generated_media\DATA750_week1_notes\media\image2.png" style="width:1.03139in;height:0.38547in" /></p>
<p>to arrive at:</p>
<p><img src="generated_media\DATA750_week1_notes\media\image3.png" style="width:2.57328in;height:0.64592in" /></p></td>
</tr>
<tr>
<td>Notation</td>
<td colspan="3"><p><img src="generated_media\DATA750_week1_notes\media\image4.png" style="width:0.88554in;height:0.32296in" />: a matrix with m rows and m columns</p>
<p><img src="generated_media\DATA750_week1_notes\media\image5.png" style="width:0.62509in;height:0.29171in" /> : a vector with n entries</p>
<p><img src="generated_media\DATA750_week1_notes\media\image6.png" style="width:0.3438in;height:0.31254in" /> : the transpose of x</p>
<p><img src="generated_media\DATA750_week1_notes\media\image7.png" style="width:0.6876in;height:0.3438in" /> : value ‘A’ at the i<sup>th</sup> row and the j<sup>th</sup> column</p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 29%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Matrix Multiplication</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Definition</td>
<td colspan="2"><img src="generated_media\DATA750_week1_notes\media\image8.png" style="width:4.96944in;height:1.53146in" /> for the <strong>matrix</strong> <strong>product</strong> to exist, the number of <strong>columns</strong> in <strong>A</strong> must <strong>equal</strong> the number of <strong>rows</strong> in <strong>B</strong></td>
</tr>
<tr>
<td><p>Dot Product</p>
<p>(Inner Product)</p></td>
<td colspan="2"><p><img src="generated_media\DATA750_week1_notes\media\image9.png" style="width:5.22969in;height:1.26272in" /></p>
<p><strong>dot</strong> <strong>products</strong> are special cases of matrix multiplication where</p>
<ul>
<li><p><strong>output</strong> is a <strong>scalar</strong></p></li>
<li><p><img src="generated_media\DATA750_week1_notes\media\image10.png" style="width:0.87512in;height:0.33338in" /></p></li>
</ul></td>
</tr>
<tr>
<td>Outer Product</td>
<td colspan="2"><p><img src="generated_media\DATA750_week1_notes\media\image11.png" style="width:5.15283in;height:1.43409in" /></p>
<ul>
<li><p><strong>output</strong> is an 𝑚×𝑛 <strong>matrix</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Matrix-Vector Multiplication</td>
<td colspan="2"><p><img src="generated_media\DATA750_week1_notes\media\image12.png" style="width:5.22918in;height:1.54305in" /></p>
<ul>
<li><p>‘<strong>y’</strong> is a <strong>linear</strong> <strong>combination</strong> of the <strong>columns</strong> of ‘A’, where the <strong>coefficients</strong> of the linear combination are given by the <strong>entries</strong> <strong>of</strong> ‘<strong>x’</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Matrix-Matrix Multiplication</td>
<td colspan="2"><p><img src="generated_media\DATA750_week1_notes\media\image13.png" style="width:0.5in;height:0.29128in" /><img src="generated_media\DATA750_week1_notes\media\image14.png" style="width:5.28457in;height:1.22065in" /></p>
<p><strong>where</strong>,<img src="generated_media\DATA750_week1_notes\media\image15.png" style="width:3.84429in;height:0.31254in" /></p></td>
</tr>
<tr>
<td>Properties of Matrix Multiplication</td>
<td colspan="2"><img src="generated_media\DATA750_week1_notes\media\image16.png" style="width:5.28072in;height:1.18365in" /></td>
</tr>
<tr>
<td colspan="2">Operations and Properties</td>
<td></td>
</tr>
<tr>
<td>Diagonal Matrix</td>
<td colspan="2"><img src="generated_media\DATA750_week1_notes\media\image17.png" style="width:5.2307in;height:0.92096in" /></td>
</tr>
<tr>
<td>Identity Matrix</td>
<td colspan="2"><p>a <strong>special</strong> <strong>case</strong> of the <strong>diagonal</strong> <strong>matrix</strong> where all non-zero values = <strong>1</strong></p>
<p><img src="generated_media\DATA750_week1_notes\media\image18.png" style="width:5.18281in;height:1.21652in" /></p></td>
</tr>
<tr>
<td>Transpose</td>
<td colspan="2"><p><img src="generated_media\DATA750_week1_notes\media\image19.png" style="width:5.16952in;height:0.75444in" /></p>
<p><strong>properties</strong> of transpose:</p>
<p><img src="generated_media\DATA750_week1_notes\media\image20.png" style="width:1.8838in;height:0.92361in" /></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr>
<th>Symmetric Matrices</th>
<th><p><img src="generated_media\DATA750_week1_notes\media\image21.png" style="width:5.67738in;height:0.2402in" /></p>
<p>any square matrix can be represented as a sum of a symmetric matrix and anti-symmetric matrix where the first matrix is symmetric and the second is antisymmetric</p>
<p><img src="generated_media\DATA750_week1_notes\media\image22.png" style="width:2.08139in;height:0.58958in" /></p>
<p>the set of all symmetric matrices of size <em>n</em> is denoted as</p>
<p><img src="generated_media\DATA750_week1_notes\media\image23.png" style="width:4.47979in;height:0.28129in" /></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Trace</td>
<td><p><img src="generated_media\DATA750_week1_notes\media\image24.png" style="width:5.09659in;height:0.91368in" /></p>
<p><strong>properties</strong> of <strong>trace</strong>:</p>
<p><img src="generated_media\DATA750_week1_notes\media\image25.png" style="width:5.13714in;height:1.49903in" /></p></td>
</tr>
<tr>
<td>Norms</td>
<td><p><img src="generated_media\DATA750_week1_notes\media\image26.png" style="width:5.16287in;height:0.9901in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image27.png" style="width:5.17864in;height:2.90779in" /></p></td>
</tr>
<tr>
<td>Linear Dependance</td>
<td><img src="generated_media\DATA750_week1_notes\media\image28.png" style="width:5.06456in;height:2.45653in" /></td>
</tr>
<tr>
<td>Inverse</td>
<td><p><img src="generated_media\DATA750_week1_notes\media\image29.png" style="width:5.19123in;height:0.56793in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image30.png" style="width:5.14747in;height:0.38001in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image31.png" style="width:4.89326in;height:0.89696in" /></p></td>
</tr>
<tr>
<td>Orthogonal Matrices</td>
<td><img src="generated_media\DATA750_week1_notes\media\image32.png" style="width:5.15226in;height:1.08219in" /></td>
</tr>
<tr>
<td>Span</td>
<td><img src="generated_media\DATA750_week1_notes\media\image33.png" style="width:5.20013in;height:0.90447in" /></td>
</tr>
<tr>
<td>Range</td>
<td><img src="generated_media\DATA750_week1_notes\media\image34.png" style="width:5.17914in;height:0.75861in" /></td>
</tr>
<tr>
<td>Nullspace</td>
<td><img src="generated_media\DATA750_week1_notes\media\image35.png" style="width:5.24772in;height:0.7894in" /></td>
</tr>
<tr>
<td>Determinant</td>
<td><p><img src="generated_media\DATA750_week1_notes\media\image36.png" style="width:5.15759in;height:3.30725in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image37.png" style="width:5.18718in;height:3.56785in" /></p>
<p>these <strong>three</strong> <strong>properties</strong> lend to these <strong>properties</strong>:</p>
<p><img src="generated_media\DATA750_week1_notes\media\image38.png" style="width:5.22013in;height:1.60877in" /></p></td>
</tr>
<tr>
<td>Quadratic Form</td>
<td><p><img src="generated_media\DATA750_week1_notes\media\image39.png" style="width:5.23033in;height:1.46628in" /></p>
<p><strong>implies</strong>:</p>
<p><img src="generated_media\DATA750_week1_notes\media\image40.png" style="width:5.11499in;height:2.65314in" /></p></td>
</tr>
</tbody>
</table>

**
**

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 29%" />
<col style="width: 52%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr>
<th>Eigenvalues and Eigenvectors</th>
<th colspan="3"><p><img src="generated_media\DATA750_week1_notes\media\image41.png" style="width:5.22263in;height:0.65283in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image42.png" style="width:5.23643in;height:5.35224in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image43.png" style="width:5.24073in;height:0.83202in" /></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>The Gradient</td>
<td colspan="3"><p><img src="generated_media\DATA750_week1_notes\media\image44.png" style="width:5.27612in;height:2.88665in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image45.png" style="width:5.53034in;height:1.2656in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image46.png" style="width:5.63767in;height:0.83842in" /></p></td>
</tr>
<tr>
<td>The Hessian</td>
<td colspan="3"><p><img src="generated_media\DATA750_week1_notes\media\image47.png" style="width:5.48837in;height:1.61485in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image48.png" style="width:5.5in;height:0.71218in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image49.png" style="width:5.44186in;height:0.96105in" /></p></td>
</tr>
<tr>
<td>Gradients of the Determinant</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image50.png" style="width:5.4798in;height:1.51163in" /></td>
</tr>
<tr>
<td>The Lagrangian</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image51.png" style="width:5.4641in;height:3in" /></td>
</tr>
<tr>
<td colspan="2">Async Materials</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4">Matrices</td>
</tr>
<tr>
<td>Linear Transformation</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image52.png" style="width:5.49917in;height:2.10795in" /></td>
</tr>
<tr>
<td>Gaussian Elimination</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image53.png" style="width:5.63323in;height:2.23193in" /></td>
</tr>
<tr>
<td>Solution with Inverse</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image54.png" style="width:5.64129in;height:2.6276in" /></td>
</tr>
<tr>
<td colspan="4">Numerics</td>
</tr>
<tr>
<td>Numerical Software</td>
<td colspan="3"><p><img src="generated_media\DATA750_week1_notes\media\image55.png" style="width:5.41757in;height:3.04218in" /></p>
<p><img src="generated_media\DATA750_week1_notes\media\image56.png" style="width:5.61262in;height:2.46512in" /></p></td>
</tr>
<tr>
<td colspan="4">Matrix Operations</td>
</tr>
<tr>
<td>Transpose</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image57.png" style="width:5.66881in;height:3.32558in" /></td>
</tr>
<tr>
<td>Transpose and Product</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image58.png" style="width:5.67918in;height:3.18605in" /></td>
</tr>
<tr>
<td>Row and Column Vectors</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image59.png" style="width:5.58287in;height:3.38372in" /></td>
</tr>
<tr>
<td>Dot Product</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image60.png" style="width:5.74736in;height:3.68605in" /></td>
</tr>
<tr>
<td>Sub-Blocks</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image61.png" style="width:3.32558in;height:2.49085in" /><img src="generated_media\DATA750_week1_notes\media\image62.png" style="width:2.41631in;height:2.5814in" /></td>
</tr>
<tr>
<td>Products of Block Matrices</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image63.png" style="width:5.73768in;height:2.98837in" /></td>
</tr>
<tr>
<td>Example</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image64.png" style="width:5.76744in;height:2.44685in" /></td>
</tr>
<tr>
<td colspan="3">Angles and Orthogonal Matrices</td>
<td></td>
</tr>
<tr>
<td>Length and Angles</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image65.png" style="width:5.66914in;height:2.37123in" /></td>
</tr>
<tr>
<td>Rotation in 2-D</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image66.png" style="width:5.4402in;height:2.56998in" /></td>
</tr>
<tr>
<td>Angles and Orthogonal Matrices</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image67.png" style="width:5.30712in;height:2.61274in" /></td>
</tr>
<tr>
<td>2-D Geometric View</td>
<td colspan="3"><img src="generated_media\DATA750_week1_notes\media\image68.png" style="width:5.4917in;height:2.796in" /></td>
</tr>
</tbody>
</table>

**
**

| Coordinates |  |  |
|----|----|----|
| Definition | <img src="generated_media\DATA750_week1_notes\media\image69.png" style="width:4.22031in;height:2.52713in" /> |  |
| Coordinate Transform | <img src="generated_media\DATA750_week1_notes\media\image70.png" style="width:4.14773in;height:2.30132in" /> |  |
| Subspaces | <img src="generated_media\DATA750_week1_notes\media\image71.png" style="width:4.11174in;height:2.75052in" /> |  |
| Subspaces and Coordinates | <img src="generated_media\DATA750_week1_notes\media\image72.png" style="width:5.37849in;height:2.56398in" /> |  |
| Finding the Coordinate | <img src="generated_media\DATA750_week1_notes\media\image73.png" style="width:5.57997in;height:2.03228in" /> |  |

| Live Session Notes | 06 Jan 2026 |
|--------------------|-------------|

| Instructor     | Joseph Slagel (Tanner)                                  |     |
|----------------|---------------------------------------------------------|-----|
| Email          | <[REDACTED_EMAIL]>                                        |     |
| Website        | <https://shemesh.larc.nasa.gov/people/jts/> \<\< NASA!! |     |
| Office Hours   | Friday at 12:00 pm                                      |     |
| What to expect |                                                         |     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><ul>
<li><p>“a really fun class”</p></li>
<li><p>Julia programming language</p></li>
<li><p>assignments due on Sunday</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| Julia Programming Language |     |
|----------------------------|-----|

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th>What is Julia?</th>
<th><ul>
<li><p>an open-source, multi-platform, high-level, high-performance</p></li>
</ul>
<p>programming language for technical computing.</p>
<ul>
<li><p>an LLVM-based JIT compiler that allows it to match the performance</p></li>
</ul>
<p>of languages such as C and FORTRAN without the hassle of low-level code</p>
<ul>
<li><p>dynamically typed, provides multiple dispatches, and is designed for</p></li>
</ul>
<p>parallelism and distributed computation.</p>
<ul>
<li><p>many built-in mathematical functions, including special functions</p></li>
</ul>
<p>(e.g. Gamma) and supports complex numbers right out of the box.</p>
<ul>
<li><p>generates code automagically thanks to Lisp-inspired macros.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Julia Commands</td>
</tr>
<tr>
<td>Accessing Help</td>
<td><img src="generated_media\DATA750_week1_notes\media\image74.png" style="width:4.18808in;height:1.69815in" /></td>
</tr>
<tr>
<td>Comments</td>
<td><img src="generated_media\DATA750_week1_notes\media\image75.png" style="width:5.08325in;height:0.50056in" /></td>
</tr>
<tr>
<td>Information About Objects</td>
<td><img src="generated_media\DATA750_week1_notes\media\image76.png" style="width:5.44684in;height:0.49794in" /></td>
</tr>
<tr>
<td>Using Packages</td>
<td><img src="generated_media\DATA750_week1_notes\media\image77.png" style="width:5.36533in;height:3.47965in" /></td>
</tr>
<tr>
<td>The Working Directory</td>
<td><img src="generated_media\DATA750_week1_notes\media\image78.png" style="width:5.25073in;height:1.35436in" /></td>
</tr>
<tr>
<td>Arithmetic Operators</td>
<td><img src="generated_media\DATA750_week1_notes\media\image79.png" style="width:5.14655in;height:4.5423in" /></td>
</tr>
<tr>
<td>Assignment Operators</td>
<td><img src="generated_media\DATA750_week1_notes\media\image80.png" style="width:5.63975in;height:1.56282in" /></td>
</tr>
<tr>
<td>Numeric Comparison Operators</td>
<td><img src="generated_media\DATA750_week1_notes\media\image81.png" style="width:5.66697in;height:1.50029in" /></td>
</tr>
<tr>
<td>Logical Operators</td>
<td><img src="generated_media\DATA750_week1_notes\media\image82.png" style="width:5.716in;height:1.04793in" /></td>
</tr>
<tr>
<td>Other Operators</td>
<td><img src="generated_media\DATA750_week1_notes\media\image83.png" style="width:5.30107in;height:1.29396in" /></td>
</tr>
<tr>
<td>Creating Vectors</td>
<td><img src="generated_media\DATA750_week1_notes\media\image84.png" style="width:5.74866in;height:2.60959in" /></td>
</tr>
<tr>
<td>Vector Functions</td>
<td><img src="generated_media\DATA750_week1_notes\media\image85.png" style="width:4.50063in;height:2.44826in" /></td>
</tr>
<tr>
<td>Selecting Vector Elements</td>
<td><img src="generated_media\DATA750_week1_notes\media\image86.png" style="width:5.43915in;height:4.55635in" /></td>
</tr>
<tr>
<td>Characters and Strings</td>
<td><img src="generated_media\DATA750_week1_notes\media\image87.png" style="width:5.32366in;height:4.18808in" /></td>
</tr>
<tr>
<td>Combining and Splitting Strings</td>
<td><img src="generated_media\DATA750_week1_notes\media\image88.png" style="width:5.88422in;height:2.28144in" /></td>
</tr>
<tr>
<td>Finding and Mutating Strings</td>
<td><img src="generated_media\DATA750_week1_notes\media\image89.png" style="width:5.78316in;height:3.31029in" /></td>
</tr>
<tr>
<td>Defining DataFrames</td>
<td><img src="generated_media\DATA750_week1_notes\media\image90.png" style="width:5.12254in;height:4.39451in" /></td>
</tr>
<tr>
<td>Manipulating DataFrames</td>
<td><img src="generated_media\DATA750_week1_notes\media\image91.png" style="width:5.23094in;height:4.33595in" /></td>
</tr>
</tbody>
</table>
