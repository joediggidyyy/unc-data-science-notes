> Markdown version for convenient browsing. Original files:
> - PDF: [DATA750_week2_notes.pdf](../DATA750_week2_notes.pdf)
> - DOCX: [DATA750_week2_notes.docx](DATA750_week2_notes.docx)

---

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 38%" />
<col style="width: 14%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th>Matrix Solutions</th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td>Overview</td>
<td colspan="5" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="6"><ul>
<li><p>Calculate matrix condition number to get error bounds for solutions for <em>Ax=b</em></p></li>
<li><p>Manipulate matrices and determine when a matrix is not invertible</p></li>
<li><p>Compute coordinates using a basis, in particular an orthogonal basis</p></li>
<li><p>What PLU factorization is, how to compute it numerically and use it to solve linear systems.</p></li>
<li><p>What banded and sparse matrices are and how the structure is used for solving large matrices.</p></li>
<li><p>Matrix norms and condition numbers and how they are used to understand accuracy and numerical sensitivity.</p></li>
<li><p>Flattening higher dimensional tensors to describe linear actions as matrices.</p></li>
</ul></td>
</tr>
<tr>
<td>Solving Ax = b</td>
<td colspan="5" style="text-align: right;"></td>
</tr>
<tr>
<td>Gaussian Elimination</td>
<td colspan="5" style="text-align: right;"><ul>
<li><p><strong>GE</strong> is used to <strong>solve</strong> <em><strong>Ax = b</strong></em></p></li>
<li><p><strong>transform</strong> matrix into <strong>Row</strong> <strong>Echelon Form (REF)</strong> using <strong>Elementary</strong> <strong>Row</strong> <strong>Operations</strong> <strong>(ERO)</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Sparse Matrix</td>
<td colspan="5" style="text-align: right;"><ul>
<li><p>most <strong>elements</strong> are <strong>zero</strong></p></li>
<li><p><strong>only</strong> have to <strong>store</strong> the <strong>non</strong>-<strong>zero</strong> <strong>elements</strong> and their <strong>locations</strong></p></li>
<li><p><strong>efficient</strong> for <strong>storage</strong> and <strong>computation</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Banded Matrix</td>
<td colspan="5" style="text-align: right;"><ul>
<li><p>a <strong>sparse</strong> <strong>matrix</strong></p></li>
<li><p><strong>non</strong>-<strong>zero</strong> entries are <strong>confined</strong> to a <strong>diagonal</strong> band comprising the main diagonal and <strong>zero</strong> or more diagonals on either side</p></li>
</ul></td>
</tr>
<tr>
<td>Elementary Row Operations (ERO)</td>
<td colspan="5" style="text-align: right;"><ol type="1">
<li><p><strong>swap</strong> <strong>rows</strong> <em><strong>(R<sub>i</sub> ↔︎ R<sub>j</sub>)</strong></em></p>
<ul>
<li><p><strong>interchange</strong> two <strong>rows</strong></p></li>
</ul></li>
<li><p><strong>scale</strong> <strong>row</strong> <em><strong>(R<sub>i</sub> → cR<sub>i</sub>)</strong></em></p>
<ul>
<li><p><strong>multiply</strong> a <strong>row</strong> by a non-zero <strong>constant</strong> (c)</p></li>
<li><p>use to <strong>make</strong> a <strong>pivot</strong> 1</p></li>
</ul></li>
<li><p><strong>add</strong> multiple <strong>rows</strong> <em><strong>(R<sub>i</sub> → R<sub>i</sub> + c)</strong></em></p>
<ul>
<li><p><strong>replace</strong> a <strong>row</strong> with <strong>itself</strong> plus a <strong>multiple</strong> <em><strong>(c)</strong></em> of another <strong>row</strong></p></li>
<li><p>use to <strong>create</strong> <strong>zeros</strong> <strong>below</strong> a <strong>pivot</strong></p></li>
</ul></li>
</ol></td>
</tr>
<tr>
<td><p>Row Echelon Form</p>
<p>(REF)</p></td>
<td colspan="5" style="text-align: right;"><ul>
<li><p><strong>get</strong> the first <strong>pivot</strong></p>
<ul>
<li><p><strong>find</strong> the leftmost <strong>non</strong>-<strong>zero</strong> <strong>column</strong></p></li>
<li><p>if the <strong>top</strong> <strong>element</strong> (pivot) is <strong>zero</strong>, <strong>swap</strong> <strong>rows</strong> to make it non-zero</p></li>
</ul></li>
<li><p><strong>make</strong> <strong>pivot</strong> <strong>1</strong></p>
<ul>
<li><p><strong>optional</strong> for <strong>REF</strong>, <strong>required</strong> for <strong>RREF</strong></p></li>
<li><p><strong>multiply</strong> the <strong>pivot</strong> <strong>row</strong> by the <strong>reciprocal</strong> of the pivot</p></li>
</ul></li>
<li><p><strong>eliminate</strong> below <strong>pivot</strong></p>
<ul>
<li><p>use <strong>row</strong> <strong>addition</strong> to make all <strong>entries</strong> <strong>below</strong> the <strong>pivot</strong> <strong>zero</strong></p></li>
</ul></li>
<li><p><strong>repeat</strong></p>
<ul>
<li><p><strong>move</strong> to the next <strong>row</strong>/<strong>column</strong> (submatrix) and <strong>repeat</strong> steps</p></li>
</ul></li>
</ul>
<p><strong>1 – 3</strong> until the<br />
<strong>matrix</strong> is in <strong>REF</strong></p>
<ul>
<li><p>produces <strong>matrix</strong> with ‘<strong>staircase</strong> <strong>pattern’</strong> and <strong>zeros</strong> <strong>below</strong> <strong>pivots</strong></p></li>
</ul></td>
</tr>
<tr>
<td><p>Reduced Echelon Form</p>
<p>(RREF)</p></td>
<td colspan="5" style="text-align: right;"><ol type="1">
<li><p>follow <strong>REF</strong> steps</p></li>
<li><p>also, <strong>use</strong> row <strong>operations</strong> to make all <strong>entries</strong> <strong>above</strong> the <strong>pivots</strong> zero</p></li>
<li><p><strong>result</strong> it an <strong>identity</strong> <strong>matrix</strong> on the ‘A side’</p></li>
</ol></td>
</tr>
<tr>
<td>Back Substitution</td>
<td colspan="5" style="text-align: right;"><ol type="1">
<li><p>once in <strong>REF</strong>/<strong>RREF</strong>, <strong>start</strong> from the <strong>last</strong> non-zero <strong>equation</strong> and <strong>solve</strong> for the <strong>variable</strong></p></li>
<li><p><strong>substitute</strong> that <strong>value</strong> into the <strong>equation</strong> above it</p></li>
<li><p><strong>continue</strong> until all <strong>variables</strong> are <strong>found</strong></p></li>
</ol></td>
</tr>
<tr>
<td>Interpreting Solution</td>
<td colspan="5" style="text-align: right;"><ol type="1">
<li><p><strong>unique</strong> solution</p>
<ul>
<li><p><strong>no</strong> <strong>inconsistent</strong> <strong>rows</strong> (like 0 = 5)</p></li>
<li><p><strong>no</strong> <strong>rows</strong> of all <strong>zeros</strong> (except very <strong>last</strong> row)</p></li>
</ul></li>
<li><p><strong>infinite</strong> solution</p>
<ul>
<li><p>a <strong>row</strong> of all <strong>zeros</strong> (0 = 0) <strong>indicates</strong> a <strong>free</strong> <strong>variable</strong> (ex: x + y = 5)</p></li>
</ul></li>
<li><p><strong>no</strong> <strong>solution</strong></p>
<ul>
<li><p>an <strong>inconsistent</strong> <strong>row</strong> (ex: 0 = r where r ≠ 0)</p></li>
</ul></li>
</ol></td>
</tr>
<tr>
<td>Example</td>
<td colspan="5" style="text-align: right;"><ul>
<li><p><strong>Solve</strong> the <strong>system</strong> of <strong>linear</strong> <strong>equations</strong> using <strong>matrices</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week2_notes\media\image1.png" style="width:1.57314in;height:0.88554in" /></p>
<ul>
<li><p><strong>write</strong> the <strong>augmented</strong> <strong>matrix</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week2_notes\media\image2.png" style="width:1.59397in;height:0.84387in" /></p>
<ul>
<li><p><strong>perform</strong> row <strong>operations</strong> to obtain <strong>REF</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week2_notes\media\image3.png" style="width:4.05265in;height:0.85429in" /></p>
<p><img src="generated_media\DATA750_week2_notes\media\image4.png" style="width:4.14641in;height:0.8647in" /></p>
<ul>
<li><p><strong>interchange</strong> two <strong>rows</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week2_notes\media\image5.png" style="width:4.55272in;height:0.82303in" /></p>
<ul>
<li><p><strong>perform</strong> row <strong>operations</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week2_notes\media\image6.png" style="width:4.11516in;height:0.84387in" /></p>
<p><img src="generated_media\DATA750_week2_notes\media\image7.png" style="width:3.82345in;height:0.83345in" /></p>
<ul>
<li><p>the last <strong>matrix</strong> <strong>represents</strong> the <strong>equivalent</strong> <strong>system</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week2_notes\media\image8.png" style="width:1.33352in;height:0.80219in" /></p>
<ul>
<li><p><strong>solution</strong> is <strong>obtained</strong> using <strong>back</strong>-<strong>substitution</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week2_notes\media\image9.png" style="width:0.8647in;height:0.29171in" /></p></td>
</tr>
<tr>
<td><p>LU</p>
<p>Factorization</p></td>
<td colspan="5" style="text-align: right;"><ul>
<li><p>any <strong>non</strong>-<strong>singular</strong> <strong>matrix</strong> <em><strong>A</strong></em> can be <strong>factored</strong> into a <strong>lower</strong> triangular matrix <em><strong>(L)</strong></em> and an <strong>upper</strong> <strong>triangular</strong> matrix <em><strong>(U)</strong></em></p></li>
</ul></td>
</tr>
<tr>
<td><p>Upper</p>
<p>Triangular</p>
<p>Matrix</p></td>
<td colspan="5" style="text-align: right;"><img src="generated_media\DATA750_week2_notes\media\image10.png" style="width:4.7715in;height:1.71899in" /></td>
</tr>
<tr>
<td><p>Lower</p>
<p>Triangular</p>
<p>Matrix</p></td>
<td colspan="5" style="text-align: right;"><img src="generated_media\DATA750_week2_notes\media\image11.png" style="width:4.79234in;height:1.73983in" /></td>
</tr>
<tr>
<td><p>Validate</p>
<p>Solution</p>
<p>Using</p>
<p>Python</p></td>
<td colspan="5" style="text-align: right;"><img src="generated_media\DATA750_week2_notes\media\image12.png" style="width:4.93997in;height:1.8354in" /></td>
</tr>
<tr>
<td><p>LU</p>
<p>Transformation</p>
<p>Using Python</p></td>
<td colspan="5" style="text-align: right;"><img src="generated_media\DATA750_week2_notes\media\image13.png" style="width:4.59439in;height:4.3131in" /></td>
</tr>
<tr>
<td>Sources</td>
<td colspan="5" style="text-align: right;"><p><a href="https://www.cs.cornell.edu/~tomf/notes/cs421-cheat-sheet.pdf">https://www.cs.cornell.edu/~tomf/notes/cs421-cheat-sheet.pdf</a></p>
<p><a href="https://www.scribd.com/document/858540190/Gaussian-Elimination-and-Gauss#:~:text=%EF%82%B7%20Transforms%20a%20matrix%20into%20reduced%20row%2Dechelon%20form.&amp;text=zeros%20everywhere%20else.&amp;text=final%20matrix.&amp;text=for%20certain%20applications%2C%20especially%20finding%20the%20inverse%20of%20a%20matrix.&amp;text=the%20matrix%20is%20in%20reduced%20row%20echelon%20form.&amp;text=variable%20represented%20in%20the%20matrix%20system">https://www.scribd.com/document/858540190/Gaussian-Elimination-and-Gauss</a>.</p>
<p><a href="https://courses.lumenlearning.com/waymakercollegealgebra/chapter/solve-a-system-with-gaussian-elimination/">https://courses.lumenlearning.com/waymakercollegealgebra/chapter/solve-a-system-with-gaussian-elimination/</a></p>
<p>https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html</p></td>
</tr>
<tr>
<td colspan="5">Spline</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="6">uses systems of linear equations to find piecewise polynomial functions (splines) that smoothly connect data points</td>
</tr>
<tr>
<td colspan="3">Key Concepts</td>
<td colspan="3" style="text-align: right;"><ul>
<li><p><strong>piecewise</strong> <strong>polynomials</strong></p>
<ul>
<li><p>A <strong>spline</strong> is made of <strong>multiple</strong> <strong>polynomial</strong> <strong>pieces</strong> joined at <strong>specific</strong> <strong>points</strong> called <strong>knots</strong> or <strong>breakpoints</strong></p></li>
</ul></li>
<li><p><strong>linear</strong> <strong>splines</strong></p>
<ul>
<li><p><strong>connecting</strong> points with <strong>straight</strong> <strong>lines</strong>, represented by <span class="math inline"><strong>y</strong> <strong>=</strong> <strong>a</strong> <strong>+</strong> <strong>b</strong><strong>x</strong></span> for each <strong>segment</strong>, solvable with <strong>basic</strong> <strong>linear</strong> <strong>equations</strong></p></li>
</ul></li>
<li><p><strong>higher</strong>-<strong>order</strong> <strong>splines</strong></p>
<ul>
<li><p>use <strong>higher</strong> <strong>degree</strong> <strong>polynomials</strong> for smoother <strong>transitions</strong></p></li>
</ul></li>
<li><p><strong>knots</strong>/<strong>breakpoints</strong></p>
<ul>
<li><p>points where the <strong>polynomial</strong> <strong>pieces</strong> <strong>connect</strong>, often <strong>data</strong> <strong>points</strong> themselves</p></li>
</ul></li>
<li><p><strong>continuity</strong> <strong>conditions</strong></p>
<ul>
<li><p>to <strong>ensure</strong> smoothness, <strong>derivatives</strong> must <strong>match</strong> at the <strong>knots</strong>, creating the <strong>system</strong> of <strong>linear</strong> <strong>equations</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Solve Using Linear Algebra</td>
<td colspan="3" style="text-align: right;"><ul>
<li><p><strong>define</strong> <strong>polynomials</strong></p>
<ul>
<li><p><em><strong>N</strong></em> data points produce <em><strong>N – 1</strong></em> segments</p></li>
<li><p>each <strong>segment</strong> has its own <strong>polynomial</strong></p></li>
</ul></li>
<li><p><strong>interpolation</strong> <strong>constraints</strong></p>
<ul>
<li><p>set up <strong>equations</strong> ensuring <img src="generated_media\DATA750_week2_notes\media\image14.gif" /><span class="math inline"><em>P</em><sub><em>k</em></sub>(<em>x</em><sub><em>k</em></sub>) = <em>y</em><sub><em>k</em></sub> </span>and <span class="math inline"><em>P</em><sub><em>k</em></sub>(<em>x</em><sub><em>k</em> + 1</sub>) = <em>y</em><sub><em>k</em> + 1</sub></span></p></li>
<li><p>the <strong>spline</strong> passes <strong>through</strong> the <strong>data</strong> points</p></li>
</ul></li>
<li><p><strong>smoothness</strong> <strong>constraints</strong></p>
<ul>
<li><p>add <strong>equations</strong> for <strong>derivative</strong> <strong>continuity</strong> at <strong>interior</strong> <strong>knots</strong></p></li>
<li><p><strong>introduces</strong> more <strong>unknowns</strong> and <strong>equations</strong></p></li>
</ul></li>
<li><p><strong>boundary</strong> <strong>conditions</strong></p>
<ul>
<li><p>add <strong>conditions</strong> for the <strong>ends</strong></p></li>
<li><p>natural <strong>cubic</strong> <strong>splines</strong> have <strong>zero</strong> <strong>second</strong> <strong>derivatives</strong> at the <strong>ends</strong></p></li>
</ul></li>
<li><p><strong>solve</strong> the <strong>system</strong></p>
<ul>
<li><p>the <strong>result</strong> is a <strong>large</strong> <strong>system</strong> of <strong>linear</strong> <strong>equations</strong></p></li>
<li><p>often <strong>represented</strong> as <em><strong>Ax = b</strong></em></p></li>
<li><p><strong>solve</strong> for <strong>unknown</strong> <strong>coefficients</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Sources</td>
<td colspan="3" style="text-align: right;"><p><a href="https://en.wikipedia.org/wiki/Spline">https://en.wikipedia.org/wiki/Spline</a></p>
<p><a href="https://people.computing.clemson.edu/">https://people.computing.clemson.edu/</a></p></td>
</tr>
<tr>
<td colspan="4">Condition Number</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="6">the condition number <em>(CN)</em> of a matrix measures how sensitive the solution of a linear system or the inverse of the matrix is to changes in the input data</td>
</tr>
<tr>
<td colspan="2">Low Condition Number</td>
<td colspan="4" style="text-align: right;"><ul>
<li><p>indicates a <em><strong>well</strong>-<strong>conditioned</strong></em> <strong>matrix</strong></p></li>
<li><p>means that <strong>small</strong> <strong>input</strong> <strong>errors</strong> lead to <strong>small</strong> <strong>output</strong> <strong>errors</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">High Condition Number</td>
<td colspan="4" style="text-align: right;"><ul>
<li><p>indicates an <em><strong>ill-conditioned</strong></em> matrix that is <strong>nearly</strong> <strong>singular</strong></p></li>
<li><p><strong>small</strong> <strong>input</strong> <strong>errors</strong> can cause <strong>massive</strong> <strong>errors</strong> in the solution</p></li>
<li><p>potentially leads to inaccurate results</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Matrix Norm</td>
<td colspan="4" style="text-align: right;"><ul>
<li><p>a <strong>measure</strong> of <strong>how</strong> <strong>large</strong> a matrix’s <strong>elements</strong> are</p></li>
<li><p>the <strong>magnitude</strong> of the <strong>matrix</strong></p></li>
<li><p>is a <strong>real</strong> <strong>number</strong> between <em><strong>1 and ∞</strong></em></p></li>
<li><p>denoted: <em><strong>|| A ||</strong></em></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Key Points</td>
<td colspan="4" style="text-align: right;"><ul>
<li><p>for any <strong>matrix</strong> <em><strong>A</strong></em>, <strong>cond(A) ≥ 1</strong></p></li>
<li><p>for the <strong>identity</strong> <strong>matrix</strong> <em><strong>I, cond(I) = 1</strong></em></p></li>
<li><p>for any <strong>matrix</strong> <em><strong>A</strong></em> and a <strong>non</strong>-<strong>zero</strong> scalar <em><strong>γ</strong></em>, <em><strong>cond(γA) = cond(A)</strong></em></p></li>
<li><p>for any <strong>diagonal</strong> <strong>matrix</strong> <em><strong>D</strong></em>, <em><strong>cond(D) = (max( |d<sub>i</sub>| ) / min( |d<sub>i</sub>| ))</strong></em></p></li>
<li><p>The <strong>condition</strong> <strong>number</strong> is a measure of <strong>how</strong> <strong>close</strong> a matrix is to being <strong>singular</strong>: a matrix with <strong>large</strong> condition <strong>number</strong> is nearly <strong>singular</strong>, whereas a <strong>matrix</strong> with a condition <strong>number</strong> <strong>close</strong> <strong>to</strong> <em><strong>1</strong></em> is <strong>far</strong> from being <strong>singular</strong></p></li>
<li><p>The <strong>determinant</strong> of a <strong>matrix</strong> is <strong>NOT</strong> a <strong>good</strong> indicator to <strong>check</strong> whether a <strong>matrix</strong> is near <strong>singularity</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">General Method</td>
<td colspan="4" style="text-align: right;"><ul>
<li><p><strong>calculate</strong> the <strong>product</strong> of the matrix <strong>norm</strong> of <em><strong>A</strong></em> and the matrix <strong>norm</strong> of <em><strong>A<sup>-1</sup></strong></em></p></li>
<li><p><em><strong>cond(A) = ||A|| ● ||A<sup>-1</sup>||</strong></em> using the <strong>same</strong> matrix <strong>norm</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">2-Norm Method (Singular Values)</td>
<td colspan="4" style="text-align: right;"><ul>
<li><p><strong>compute Singular Value Decomposition</strong></p>
<ul>
<li><p><strong>perform the</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Sources</td>
<td colspan="4" style="text-align: right;">https://courses.grainger.illinois.edu/cs357/fa2023/notes/ref-10-condition.html</td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 28%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Live Session Notes</th>
<th style="text-align: right;">13 Jan 2026</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><ul>
<li><p>Matrix Solutions</p></li>
<li></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
</tbody>
</table>
