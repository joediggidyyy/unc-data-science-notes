> Markdown version for convenient browsing. Original files:
> - PDF: [DATA750_week05_notes.pdf](../DATA750_week05_notes.pdf)
> - DOCX: [DATA750_week05_notes.docx](DATA750_week05_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Least Squares</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td colspan="2" style="text-align: right;"><em>03 Feb 2026</em></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>Extend the 1-D DFT to higher dimensions, and understand two-dimensional frequencies</p></li>
<li><p>Get a geometric intuition of projection onto a subspace.</p></li>
<li><p>Learn about least squares optimization and how they are solved using the Normal Equation.</p></li>
<li><p>Learn about weighted least squares and how the normal equation is modified.</p></li>
<li><p>How to use numerical libraries to solve linear least squares problems.</p></li>
<li><p>How to generalize least squares to higher order polynomials as well as exponential and power fits.</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5">2D FFT</td>
</tr>
<tr>
<td>2D Discrete Fourier Transform</td>
<td colspan="4"><ul>
<li><p>a <strong>vector</strong> <strong>space</strong> is a space where you can <strong>add</strong> and <strong>scale</strong> <strong>elements</strong></p></li>
<li><p><strong>vectors</strong> are just <strong>elements</strong> of a <strong>vector</strong> <strong>space</strong></p></li>
<li><p>two <strong>identify</strong> <strong>orthogonal</strong> elements, <strong>inner</strong> <strong>product</strong> is needed</p></li>
<li><p><strong>2D</strong> arrays (<strong>tensors</strong>) are <strong>vectors</strong> whose <strong>inner</strong> <strong>product</strong> is the <strong>sum</strong> of the <strong>pairwise</strong> <strong>products</strong> of the elements</p></li>
<li><p><strong>create</strong> and <strong>array</strong>/<strong>vector</strong></p></li>
</ul>
<p><span class="math display"><em>v</em><sup><em>k</em><sub>1</sub>, <em>k</em><sub>2</sub></sup> ∈ <em>R</em><sup><em>N</em><sub></sub> × <em>N</em><sub></sub></sup></span></p>
<ul>
<li><p>with <strong>two</strong> <strong>dimensions</strong></p></li>
</ul>
<blockquote>
<p><span class="math inline"><strong>v</strong><sub><strong>j</strong><sub><strong>1</strong></sub><strong>,</strong><strong>j</strong><sub><strong>2</strong></sub></sub><sup><strong>k</strong><sub><strong>1</strong></sub><strong>,</strong><strong>k</strong><sub><strong>2</strong></sub></sup></span> <span class="math inline">=</span> <span class="math inline">$\mathbf{\exp}{\textit{\textbf{!}}\left( \mathbf{i}\frac{\mathbf{2}\mathbf{\pi}\mathbf{j}_{\mathbf{1}}\mathbf{k}_{\mathbf{1}}}{\mathbf{N}_{\mathbf{1}}} \right)}$</span> <span class="math inline">$\mathbf{\exp}{\textit{\textbf{!}}\left( \mathbf{i}\frac{\mathbf{2}\mathbf{\pi}\mathbf{j}_{\mathbf{2}}\mathbf{k}_{\mathbf{2}}}{\mathbf{N}_{\mathbf{2}}} \right)}$</span></p>
</blockquote></td>
</tr>
<tr>
<td>Visualizing Waves</td>
<td colspan="4"><ul>
<li><p>this <strong>vector</strong> is both <strong>two</strong>-<strong>dimensional</strong> as well as <strong>complex</strong></p></li>
<li><p>the <strong>components</strong> are <strong>waves</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{v}_{\mathbf{j}_{\mathbf{1}}\mathbf{,}\mathbf{j}_{\mathbf{2}}}^{\mathbf{k}_{\mathbf{1}}\mathbf{,}\mathbf{k}_{\mathbf{2}}}\mathbf{=}\mathbf{\sin}{\textit{\textbf{!}}\left( \frac{\mathbf{2}\mathbf{\pi}\mathbf{j}_{\mathbf{1}}\mathbf{k}_{\mathbf{1}}}{\mathbf{N}_{\mathbf{1}}} \right)}\mathbf{\sin}{\textit{\textbf{!}}\left( \frac{\mathbf{2}\mathbf{\pi}\mathbf{j}_{\mathbf{2}}\mathbf{k}_{\mathbf{2}}}{\mathbf{N}_{\mathbf{2}}} \right)}$$</span></p>
<ul>
<li><p><strong>normalized</strong> index <strong>coordinates</strong></p></li>
</ul>
<p><span class="math display">$$\left( \frac{\mathbf{j}_{\mathbf{1}}}{\mathbf{N}_{\mathbf{1}}}\mathbf{,}\frac{\mathbf{j}_{\mathbf{2}}}{\mathbf{N}_{\mathbf{2}}} \right)$$</span></p>
<ul>
<li><p>as a point in a <strong>unit</strong> <strong>square</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{x =}\frac{\mathbf{j}_{\mathbf{1}}}{\mathbf{N}_{\mathbf{1}}}\mathbf{,}\mathbf{\quad}\mathbf{y =}\frac{\mathbf{j}_{\mathbf{2}}}{\mathbf{N}_{\mathbf{2}}}$$</span></p>
<ul>
<li><p><strong>continuous</strong> <strong>domain</strong> representation</p></li>
</ul>
<p><span class="math display"><strong>v</strong><sup><strong>k</strong><sub><strong>1</strong></sub><strong>,</strong><strong>k</strong><sub><strong>2</strong></sub></sup>(<strong>x</strong><strong>,</strong> <strong>y</strong>)<strong>=</strong><strong>s</strong><strong>i</strong><strong>n</strong>(<strong>2</strong><strong>π</strong><strong>k</strong><sub><strong>1</strong></sub><strong>x</strong>)<strong>s</strong><strong>i</strong><strong>n</strong>(<strong>2</strong><strong>π</strong><strong>k</strong><sub><strong>2</strong></sub><strong>y</strong>)</span></p>
<p><img src="generated_media\DATA750_week05_notes\media\image1.png" style="width:2.92993in;height:1.95658in" /></p>
<p>ChatGPT 5.2 1</p></td>
</tr>
<tr>
<td>Orthogonal Vectors</td>
<td colspan="4"><ul>
<li><p>the <strong>vectors</strong> are <strong>orthogonal</strong> to each other</p></li>
</ul>
<p><span class="math display">$$\mathbf{v}_{\mathbf{j}_{\mathbf{1}}\mathbf{,}\mathbf{j}_{\mathbf{2}}}^{\mathbf{k}_{\mathbf{1}}\mathbf{,}\mathbf{k}_{\mathbf{2}}}\mathbf{=}\mathbf{\exp}{\textit{\textbf{!}}\left( \frac{\mathbf{2}\mathbf{\pi i}\mathbf{j}_{\mathbf{1}}\mathbf{k}_{\mathbf{1}}}{\mathbf{N}_{\mathbf{1}}} \right)}\mathbf{\exp}{\textit{\textbf{!}}\left( \frac{\mathbf{2}\mathbf{\pi i}\mathbf{j}_{\mathbf{2}}\mathbf{k}_{\mathbf{2}}}{\mathbf{N}_{\mathbf{2}}} \right)}$$</span></p>
<ul>
<li><p><strong>orthogonality</strong> condition</p></li>
</ul>
<p><span class="math display"><strong>v</strong><sup><strong>r</strong><sub><strong>1</strong></sub><strong>,</strong><strong>r</strong><sub><strong>2</strong></sub></sup><strong>⋅</strong><strong>v</strong><sup><strong>s</strong><sub><strong>1</strong></sub><strong>,</strong><strong>s</strong><sub><strong>2</strong></sub></sup> <strong>=</strong> <strong>0</strong></span></p>
<p><span class="math display">  if  (<strong>r</strong><sub><strong>1</strong></sub><strong>,</strong><strong>r</strong><sub><strong>2</strong></sub>)<strong>≠</strong>(<strong>s</strong><sub><strong>1</strong></sub><strong>,</strong><strong>s</strong><sub><strong>2</strong></sub>)</span></p>
<ul>
<li><p>and the <strong>length</strong> of all the <strong>vectors</strong> are the <strong>same</strong> (vector <strong>norm</strong>)</p></li>
</ul>
<p><span class="math display">$$\left. \ \textit{\textbf{|}}\mathbf{v}^{\mathbf{k}_{\mathbf{1}}\mathbf{,}\mathbf{k}_{\mathbf{2}}} \right.\ \textit{\textbf{|}}^{\mathbf{2}}\mathbf{=}\mathbf{v}^{\mathbf{k}_{\mathbf{1}}\mathbf{,}\mathbf{k}_{\mathbf{2}}}\mathbf{\cdot}\mathbf{v}^{\mathbf{k}_{\mathbf{1}}\mathbf{,}\mathbf{k}_{\mathbf{2}}}\mathbf{=}\mathbf{N}_{\mathbf{1}}\mathbf{N}_{\mathbf{2}}$$</span></p>
<ul>
<li><p>the <strong>dot</strong> <strong>product</strong> is defined by listing <strong>all</strong> of the <strong>entries</strong> in a single <strong>list</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Projection</td>
</tr>
<tr>
<td>Solution</td>
<td colspan="4"><ul>
<li><p>the <strong>closest</strong> point <strong>p</strong> has the <strong>property</strong> that,</p></li>
</ul>
<p><span class="math display">(<strong>x</strong> <strong>−</strong> <strong>p</strong>)<strong>⋅</strong><strong>v</strong> <strong>=</strong> <strong>0</strong></span></p>
<ul>
<li><p>for every <strong>vector</strong> <strong>v</strong> in <strong>V</strong>, but that happens if,</p></li>
</ul>
<p><span class="math display">(<strong>x</strong> <strong>−</strong> <strong>p</strong>)<strong>⋅</strong><strong>v</strong><sub><strong>i</strong></sub> <strong>=</strong> <strong>0</strong></span></p>
<ul>
<li><p>for every <strong>vector</strong> in the <strong>basis</strong> for <strong>V</strong>,</p></li>
</ul>
<p><span class="math display"><strong>v</strong><sub><strong>i</strong></sub><sup><strong>T</strong></sup><strong>x</strong><strong>=</strong><strong>v</strong><sub><strong>i</strong></sub><sup><strong>T</strong></sup><strong>p</strong></span></p>
<ul>
<li><p><strong>since</strong>,</p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>=</strong>[<strong>v</strong><sub><strong>1</strong></sub> <strong>⋯</strong> <strong>v</strong><sub><strong>n</strong></sub>]</span></p>
<ul>
<li><p>that <strong>means</strong>,</p></li>
</ul>
<p><span class="math display"><strong>A</strong><sup><strong>T</strong></sup><strong>x</strong><strong>=</strong><strong>A</strong><sup><strong>T</strong></sup><strong>p</strong></span></p></td>
</tr>
<tr>
<td>QR Factorization</td>
<td colspan="4"><ul>
<li><p>to help with this, we use a very important <strong>factorization</strong> — <strong>QR</strong>.</p></li>
<li><p>given a <strong>matrix</strong> <strong>A</strong> with <strong>linearly</strong> <strong>independent</strong> columns, we can factor</p></li>
</ul>
<p><span class="math display"><strong>A</strong> <strong>=</strong> <strong>Q</strong><strong>R</strong></span></p>
<ul>
<li><p>example:</p></li>
</ul>
<p><span class="math display">$$\mathbf{A\  = \ }\left\lbrack \binom{\binom{\mathbf{2}}{\mathbf{0}}}{\binom{\mathbf{2}}{\mathbf{2}}}\mathbf{\ }\binom{\binom{\mathbf{1}}{\mathbf{1}}}{\binom{\mathbf{0}}{\mathbf{2}}} \right\rbrack\mathbf{= \ QR}$$</span></p>
<p><span class="math display">$$\mathbf{Q =}\frac{\mathbf{1}}{\sqrt{\mathbf{3}}}\left\lbrack \binom{\binom{\mathbf{1}}{\mathbf{0}}}{\binom{\mathbf{1}}{\mathbf{1}}}\mathbf{\ }\binom{\binom{\mathbf{1}}{\mathbf{1}}}{\binom{\mathbf{- 1}}{\mathbf{1}}} \right\rbrack\mathbf{,\ R =}\sqrt{\mathbf{3}}\begin{bmatrix}
\mathbf{2} &amp; \mathbf{1} \\
\mathbf{0} &amp; \mathbf{1}
\end{bmatrix}$$</span></p>
<p><span class="math display"><strong>v</strong><sub><strong>1</strong></sub><strong>=</strong><strong>r</strong><sub><strong>11</strong></sub><strong>q</strong><sub><strong>1</strong></sub></span></p>
<p><span class="math display"><strong>v</strong><sub><strong>2</strong></sub><strong>=</strong><strong>r</strong><sub><strong>12</strong></sub><strong>q</strong><sub><strong>1</strong></sub><strong>+</strong><strong>r</strong><sub><strong>22</strong></sub><strong>q</strong><sub><strong>2</strong></sub></span></p></td>
</tr>
<tr>
<td>Julia</td>
<td colspan="4"><p><strong>julia&gt; using LinearAlgebra</strong></p>
<p><strong>julia&gt; A = [2 1; 0 1; 2 0; 2 2];</strong></p>
<p><strong>julia&gt; qrf = qr(A);</strong></p>
<p><strong>julia&gt; Matrix(qrf.Q)</strong></p>
<p><strong>4×2 Matrix{Float64}:</strong></p>
<p><strong>-0.57735 2.29738e-17</strong></p>
<p><strong>-0.57735 -0.57735</strong></p>
<p><strong>-0.57735 0.57735</strong></p>
<p><strong>-0.57735 -0.57735</strong></p>
<p><strong>julia&gt; R = qrf.R</strong></p>
<p><strong>2×2 Matrix{Float64}:</strong></p>
<p><strong>-3.4641 -1.73205</strong></p>
<p><strong>0.0 -1.73205</strong></p>
<p><strong>julia&gt; Q = qrf.Q</strong></p>
<p><strong>4×2 Matrix{Float64}:</strong></p>
<p><strong>2.0 1.0</strong></p>
<p><strong>0.0 1.0</strong></p>
<p><strong>2.0 0.0</strong></p>
<p><strong>2.0 2.0</strong></p>
<p><strong>julia&gt; Q'*Q</strong></p>
<p><strong>2×2 Matrix{Float64}:</strong></p>
<p><strong>1.0 -2.01213e-17</strong></p>
<p><strong>-2.01213e-17 1.0</strong></p></td>
</tr>
<tr>
<td>Use QR for Projection</td>
<td colspan="4"><ul>
<li><p>combine</p></li>
</ul>
<p><span class="math display"><strong>A</strong><sup><strong>T</strong></sup><strong>z</strong> = <strong>A</strong><sup><strong>T</strong></sup><strong>x</strong></span></p>
<p><span class="math display"><strong>A</strong> = <strong>Q</strong><strong>R</strong></span></p>
<ul>
<li><p>get,</p></li>
</ul>
<p><span class="math display"><strong>R</strong><sup><strong>T</strong></sup><strong>Q</strong><sup><strong>T</strong></sup><strong>z</strong><strong>=</strong><strong>R</strong><sup><strong>T</strong></sup><strong>Q</strong><sup><strong>T</strong></sup><strong>x</strong></span></p>
<p><span class="math display"><strong>Q</strong><sup><strong>T</strong></sup><strong>z</strong><strong>=</strong><strong>Q</strong><sup><strong>T</strong></sup><strong>p</strong></span></p>
<ul>
<li><p><strong>p</strong> is in the <strong>span</strong> of <strong>Q</strong> <strong>columns</strong></p></li>
</ul>
<p><span class="math display"><strong>p</strong> <strong>=</strong> <strong>Q</strong><strong>c</strong></span></p>
<p><span class="math display"><strong>Q</strong><sup><strong>T</strong></sup><strong>z</strong><strong>=</strong><strong>Q</strong><sup><strong>T</strong></sup><strong>Q</strong><strong>c</strong> <strong>=</strong> <strong>c</strong></span></p>
<p><span class="math display"><strong>p</strong> <strong>=</strong> <strong>Q</strong><strong>c</strong> <strong>=</strong> <strong>Q</strong><strong>Q</strong><sup><strong>T</strong></sup><strong>z</strong></span></p></td>
</tr>
<tr>
<td colspan="5">Projection Onto a Subspace</td>
</tr>
<tr>
<td>Challenge</td>
<td colspan="4"><ul>
<li><p>look at a <strong>subspace</strong> in <strong>n dimensional</strong> <strong>space</strong>, spanned by <strong>k linearly</strong> <strong>independent</strong> <strong>vectors</strong> (a basis)</p></li>
</ul>
<p><span class="math display"><strong>V</strong> <strong>=</strong> <strong>s</strong><strong>p</strong><strong>a</strong><strong>n</strong>(<strong>v</strong><sub><strong>1</strong></sub><strong>,</strong><strong>v</strong><sub><strong>2</strong></sub><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>v</strong><sub><strong>k</strong></sub>)<strong>∈</strong>ℝ<sup><strong>n</strong></sup></span></p>
<ul>
<li><p>this is a <strong>k-dimensional subspace</strong></p></li>
<li><p>for a point <span class="math inline"><strong>x</strong><strong>∈</strong>ℝ<sup><strong>n</strong></sup><strong>,</strong> <strong>x</strong> <strong>∉</strong> <strong>V</strong></span>, find the point in the <strong>subspace</strong> <strong>V</strong> that is <strong>closest</strong> to <strong>x</strong></p></li>
<li><p>first observation is that <strong>every</strong> <strong>point</strong> in the <strong>subspace</strong> is of the form</p></li>
</ul>
<p><span class="math display"><strong>p</strong> <strong>=</strong> <strong>A</strong><strong>c</strong><strong>,</strong>  <strong>c</strong><strong>∈</strong>ℝ<sup><strong>k</strong></sup></span></p>
<p><span class="math display"><strong>A</strong><strong>=</strong>[<strong>v</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>v</strong><sub><strong>n</strong></sub>]</span></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr>
<th>Solution</th>
<th><ul>
<li><p>The closest point p has the property that</p></li>
</ul>
<p><span class="math display">(<strong>x</strong> <strong>−</strong> <strong>p</strong>)<strong>•</strong><strong>v</strong> <strong>=</strong> <strong>0</strong></span></p>
<ul>
<li><p>for every vector v in V</p></li>
<li><p>but that happens if</p></li>
</ul>
<p><span class="math display">(<strong>x</strong> <strong>−</strong> <strong>p</strong>)<strong>•</strong><strong>v</strong><sub><strong>i</strong></sub> <strong>=</strong> <strong>0</strong></span></p>
<ul>
<li><p>for every vector v in the basis for V</p></li>
</ul>
<p><span class="math display"><strong>v</strong><sub><strong>i</strong></sub><sup><strong>T</strong></sup><strong>x</strong><strong>=</strong><strong>v</strong><sub><strong>i</strong></sub><sup><strong>T</strong></sup><strong>p</strong></span></p>
<ul>
<li><p>since,</p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>=</strong>[<strong>v</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>v</strong><sub><strong>n</strong></sub>]</span></p>
<ul>
<li><p>that means:</p></li>
</ul>
<p><span class="math display"><strong>A</strong><sup><strong>T</strong></sup><strong>x</strong><strong>=</strong><strong>A</strong><sup><strong>T</strong></sup><strong>p</strong></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>QR Factorization</td>
<td><ul>
<li><p>given a matrix A, with linearly independent columns</p></li>
</ul>
<p><span class="math display"><strong>A</strong> <strong>=</strong> <strong>Q</strong><strong>R</strong></span></p>
<ul>
<li><p>ex:</p></li>
</ul>
<p>A=<span class="math inline">$\begin{bmatrix}
\begin{matrix}
2 \\
0 \\
2
\end{matrix} &amp; \begin{matrix}
1 \\
1 \\
0
\end{matrix} \\
2 &amp; 2
\end{bmatrix} = QR,\ \ \ \ \ \ \ Q = \frac{1}{\sqrt{3}}\begin{bmatrix}
\begin{matrix}
1 \\
0 \\
1
\end{matrix} &amp; \begin{matrix}
0 \\
1 \\
 - 1
\end{matrix} \\
1 &amp; 1
\end{bmatrix},\ \ \ \ \ \ \ R = \sqrt{3}\begin{bmatrix}
2 &amp; 1 \\
0 &amp; 1
\end{bmatrix}$</span></p></td>
</tr>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; using LinearAlgebra</strong></p>
<p><strong>julia&gt; A = [2 1;0 1;2 0;2 2];</strong></p>
<p><strong>julia&gt; qrf = qr(A)</strong></p>
<p><strong>julia&gt; Matrix(qrf.Q)</strong></p>
<p><strong>4x2 Matrix{Float64}:</strong></p>
<p><strong>-0.57735 2.29938e-17</strong></p>
<p><strong>0.0 -0.57735</strong></p>
<p><strong>-0.57735 0.57735</strong></p>
<p><strong>-0.57735 -0.57735</strong></p>
<p><strong>julia&gt; R = qrf.R</strong></p>
<p><strong>2x2 Matrix{Float64}:</strong></p>
<p><strong>-3.4641 -1.73205</strong></p>
<p><strong>0.0 -1.73205</strong></p>
<p><strong>julia&gt; Q*R</strong></p>
<p><strong>4x2 Matrix{Float64}:</strong></p>
<p><strong>2.0 1.0</strong></p>
<p><strong>0.0 1.0</strong></p>
<p><strong>2.0 4.85078e-18</strong></p>
<p><strong>2.0 2.0</strong></p>
<p><strong>julia&gt; Q'*Q</strong></p>
<p>we want a <strong>vector</strong> <span class="math inline"><strong>p</strong></span> that <strong>‘</strong>behaves’ like <span class="math inline"><strong>x</strong> </span>when <strong>‘</strong>viewed through’ the columns <strong>of</strong> <span class="math inline"><strong>A</strong></span></p>
<p><strong>2x2 Matrix{Float64}:</strong></p>
<p><strong>1.0 -2.01213e-17</strong></p>
<p><strong>-2.01213e-17 1.0</strong></p></td>
</tr>
<tr>
<td>Use QR for Projection</td>
<td style="text-align: center;"><p><span class="math inline"><strong>A</strong><sup><strong>T</strong></sup><strong>x</strong><strong>=</strong><strong>A</strong><sup><strong>T</strong></sup><strong>p</strong></span></p>
<p>choose a <strong>Q</strong> (<strong>orthogonal</strong>) and <strong>R</strong> (<strong>upper</strong> <strong>triangular</strong>) such that they are a <strong>decomposition</strong> of invertible <strong>matrix</strong> <strong>A</strong></p>
<p><span class="math display"><strong>A</strong> <strong>=</strong> <strong>Q</strong><strong>R</strong></span></p>
<ul>
<li><p>in <strong>least</strong> <strong>squares</strong> this translates to:</p></li>
</ul>
<p>‘<span class="math inline"><strong>p</strong></span> <em>is the <strong>closest</strong> <strong>vector</strong> to</em><span class="math inline"> <strong>x</strong></span> <em>that lives</em></p>
<p><em><strong>inside</strong> the <strong>column</strong> <strong>space</strong> of</em> <span class="math inline"><strong>A</strong></span>’</p>
<ul>
<li><p>now, <strong>replace</strong> <span class="math inline"><strong>A</strong></span> with its <span class="math inline"><strong>Q</strong><strong>R</strong> <strong>F</strong><strong>a</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong><strong>i</strong><strong>z</strong><strong>a</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong></span></p></li>
</ul>
<p><span class="math display"><strong>R</strong><sup><strong>T</strong></sup><strong>Q</strong><sup><strong>T</strong></sup><strong>x</strong><strong>=</strong><strong>R</strong><sup><strong>T</strong></sup><strong>A</strong><strong>T</strong></span></p>
<p><span class="math display"><strong>Q</strong><sup><strong>T</strong></sup><strong>x</strong><strong>=</strong><strong>Q</strong><sup><strong>T</strong></sup><strong>p</strong></span></p>
<ul>
<li><p>since <span class="math inline"><strong>p</strong></span> lies in the <strong>span</strong> of the <strong>columns</strong> of <strong>Q</strong>,</p></li>
</ul>
<p><span class="math display"><strong>p</strong> <strong>=</strong> <strong>Q</strong><strong>c</strong></span></p>
<ul>
<li><p>for some <strong>coefficient</strong> <span class="math inline"><strong>v</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong> <strong>c</strong></span> giving us,</p></li>
</ul>
<p><span class="math display"><strong>Q</strong><sup><strong>T</strong></sup><strong>x</strong><strong>=</strong><strong>Q</strong><sup><strong>T</strong></sup><strong>Q</strong><strong>c</strong></span></p>
<ul>
<li><p>because <strong>Q</strong> is <strong>orthogonal</strong></p></li>
</ul>
<p>Identity Matrix</p>
<p><span class="math display"><strong>Q</strong><sup><strong>T</strong></sup><strong>Q</strong> <strong>=</strong> <strong>I</strong></span></p>
<ul>
<li><p><strong>so,</strong></p></li>
</ul>
<p>translates to: ‘p is the projection of x onto the column space of A</p>
<p><span class="math inline"><strong>c</strong><strong>=</strong><strong>Q</strong><sup><strong>T</strong></sup><strong>x</strong></span><strong>.</strong></p>
<ul>
<li><p><strong>substituting</strong> back, we get,</p></li>
</ul>
<p><span class="math display"><strong>p</strong> <strong>=</strong> <strong>Q</strong><strong>Q</strong><sup><strong>T</strong></sup><strong>x</strong></span></p>
<ul>
<li><p>what does it all mean?</p>
<ul>
<li><p><strong>starting</strong> with a <span class="math inline"><strong>v</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong> <strong>x</strong> </span>that <strong>may</strong> or <strong>may</strong> <strong>not</strong> lie in the <strong>column</strong> <strong>space</strong> of <span class="math inline"><strong>A</strong></span>, the <strong>least</strong>-<strong>squares</strong> solution finds the <span class="math inline"><strong>v</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong> <strong>p</strong></span> <strong>inside</strong> that <strong>column</strong> <strong>space</strong> that is <strong>closest</strong> to <span class="math inline"><em>x</em></span>.</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; using LinearAlgebra</strong></p>
<p><strong>julia&gt; A = [2 1;0 1;2 0;2 2];</strong></p>
<p><strong>julia&gt; qrf = qr(A);</strong></p>
<p><strong>julia&gt; x = [1,2,3,4];</strong></p>
<p><strong>julia&gt; Q = Matrix(qrf.Q);</strong></p>
<p><strong>julia&gt; p = Q*Q'*x</strong></p>
<p><strong>4-element Vector{Float64}:</strong></p>
<p><strong>2.6666666666666665</strong></p>
<p><strong>0.9999999999999999</strong></p>
<p><strong>1.6666666666666667</strong></p>
<p><strong>3.6666666666666665</strong></p>
<p><strong>julia&gt; A'*(p-x)</strong></p>
<p><strong>2-element Vector{Float64}:</strong></p>
<p><strong>-4.440892098500626e-16</strong></p>
<p><strong>-4.440892098500626e-16</strong></p>
<p><strong>julia&gt; norm(x)</strong></p>
<p><strong>5.477225575051661</strong></p>
<p><strong>julia&gt; norm(p)</strong></p>
<p><strong>4.93288262316247</strong></p>
<p><strong>julia&gt; norm(p-x)</strong></p>
<p><strong>2.3804761428476167</strong></p>
<p><strong>julia&gt; sqrt(4.93^2+2.38^2)</strong></p>
<p><strong>5.4742234395557</strong></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Least Squares</th>
</tr>
</thead>
<tbody>
<tr>
<td>Challenge</td>
<td><ul>
<li><p>you <strong>have</strong> data <strong>points</strong></p></li>
</ul>
<p><span class="math display">(<strong>x</strong><sub><strong>1</strong></sub><strong>,</strong><strong>y</strong><sub><strong>1</strong></sub>)<strong>,</strong> (<strong>x</strong><sub><strong>2</strong></sub><strong>,</strong> <strong>y</strong><sub><strong>2</strong></sub>)<strong>,</strong> <strong>…</strong></span></p>
<ul>
<li><p>you <strong>want</strong> to <strong>approximate</strong> as a single <strong>line</strong></p></li>
</ul>
<p>basic <strong>line</strong> <strong>equation</strong>:</p>
<p>a = <strong>y-intercept</strong></p>
<p>b = <strong>slope</strong></p>
<p><span class="math display"><strong>f</strong>(<strong>x</strong>) <strong>=</strong> <strong>a</strong> <strong>+</strong> <strong>b</strong><strong>x</strong></span></p>
<ul>
<li><p><strong>ideally</strong>, each data point <strong>would</strong> <strong>satisfy</strong></p></li>
</ul>
<p><span class="math display"><strong>y</strong> <strong>=</strong> <strong>a</strong> <strong>+</strong> <strong>b</strong><strong>x</strong><sub><strong>i</strong></sub></span></p>
<ul>
<li><p>the <strong>expectation</strong> of this as a <strong>solution</strong> is</p></li>
</ul>
<p>meaning: the line should be pretty close</p>
<p><strong>unrealistic</strong>, so <strong>instead</strong></p>
<p><span class="math display"><strong>y</strong><sub><strong>i</strong></sub> <strong>≈</strong> <strong>a</strong> <strong>+</strong> <strong>b</strong><strong>x</strong><sub><strong>i</strong></sub></span></p></td>
</tr>
<tr>
<td>Rewriting the System of Equations as a Matrix</td>
<td><ul>
<li><p><strong>instead</strong> of <strong>writing</strong> an <strong>equation</strong> for <strong>each</strong> <strong>point</strong>, we <strong>stack</strong> them</p></li>
</ul>
<p><strong>linear</strong> <strong>expressions</strong></p>
<p>all of the <span class="math inline"><strong>y</strong><sub><strong>i</strong></sub></span> <strong>values</strong> go into <strong>one</strong> <strong>column</strong></p>
<p><span class="math display">$$\begin{bmatrix}
\begin{matrix}
\mathbf{y}_{\mathbf{1}} \\
\mathbf{y}_{\mathbf{2}} \\
\mathbf{y}_{\mathbf{3}}
\end{matrix} \\
\mathbf{y}_{\mathbf{4}} \\
\mathbf{y}_{\mathbf{5}}
\end{bmatrix}\mathbf{=}\left\lbrack \begin{matrix}
\begin{matrix}
\mathbf{1} \\
\mathbf{1} \\
\mathbf{1}
\end{matrix} \\
\mathbf{1} \\
\mathbf{1}
\end{matrix}\begin{matrix}
\begin{matrix}
\mathbf{\ \ x}_{\mathbf{1}} \\
{\mathbf{\ \ }\mathbf{x}}_{\mathbf{2}} \\
\mathbf{\ \ }\mathbf{x}_{\mathbf{3}}
\end{matrix} \\
{\mathbf{\ \ }\mathbf{x}}_{\mathbf{4}} \\
\mathbf{\ \ }\mathbf{x}_{\mathbf{5}}
\end{matrix} \right\rbrack\begin{bmatrix}
\mathbf{a} \\
\mathbf{b}
\end{bmatrix}$$</span></p>
<ul>
<li><p>so, the <strong>system</strong> <strong>becomes</strong></p></li>
</ul>
<p>compactly <strong>represents</strong> <strong>all</strong> <strong>equations</strong> in the system</p>
<p><span class="math display">$$\mathbf{y \approx A}\begin{bmatrix}
\mathbf{a} \\
\mathbf{b}
\end{bmatrix}$$</span></p></td>
</tr>
<tr>
<td>The Least Squares Solution</td>
<td><ul>
<li><p>finding a <strong>single</strong> choice of <span class="math inline"><strong>a</strong></span> and <span class="math inline"><strong>b</strong></span> to <strong>satisfy</strong> our <strong>equation</strong> is <strong>unlikely</strong></p></li>
<li><p>instead, we want to find <span class="math inline"><strong>a</strong></span> and <span class="math inline"><strong>b</strong></span> that make the <strong>total</strong> <strong>error</strong> as <strong>small</strong> as <strong>possible</strong></p></li>
</ul>
<p>why <strong>square</strong> the <strong>errors</strong>?</p>
<ul>
<li><p>negative and positive <strong>errors</strong> <strong>do</strong> <strong>not</strong> <strong>cancel</strong></p></li>
<li><p><strong>large</strong> errors <strong>penalize</strong> <strong>more</strong></p></li>
</ul>
<ul>
<li><p>for each point <strong>compute</strong> the <strong>veritcal</strong> <strong>distance</strong></p></li>
</ul>
<p><span class="math display"><strong>e</strong><strong>r</strong><strong>r</strong><strong>o</strong><strong>r</strong><sub><strong>i</strong></sub><strong>=</strong><strong>y</strong><sub><strong>i</strong></sub><strong>=</strong>(<strong>a</strong> <strong>+</strong> <strong>b</strong><strong>x</strong><sub><strong>i</strong></sub>)</span></p>
<ul>
<li><p>then, we <strong>minimize</strong> the <strong>error</strong></p></li>
</ul>
<p><span class="math display">$$\sum_{}^{}\left( \mathbf{erro}\mathbf{r}_{\mathbf{i}} \right)^{\mathbf{2}}$$</span></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr>
<th>Residual</th>
<th><ul>
<li><p>the residual is simply <em>the error at each data point,</em> expressed as</p></li>
</ul>
<p><span class="math inline"><strong>y</strong><strong>=</strong></span> <strong>measured</strong> values</p>
<p><span class="math inline"><strong>A</strong><strong>c</strong><strong>=</strong></span> <strong>predicted</strong> values</p>
<p><span class="math inline"><strong>r</strong><strong>=</strong></span> the <strong>difference</strong> between measured and predicted</p>
<p><span class="math display"><strong>r</strong> <strong>=</strong> <strong>y</strong> <strong>−</strong> <strong>A</strong><strong>c</strong></span></p>
<ul>
<li><p>so, for each point</p></li>
</ul>
<p><span class="math display"><strong>r</strong><strong>e</strong><strong>s</strong><strong>i</strong><strong>d</strong><strong>u</strong><strong>a</strong><strong>l</strong> <strong>=</strong> <strong>a</strong><strong>c</strong><strong>t</strong><strong>u</strong><strong>a</strong><strong>l</strong> <strong>v</strong><strong>a</strong><strong>l</strong><strong>u</strong><strong>e</strong> <strong>−</strong> <strong>p</strong><strong>r</strong><strong>e</strong><strong>d</strong><strong>i</strong><strong>c</strong><strong>t</strong><strong>e</strong><strong>d</strong> <strong>v</strong><strong>a</strong><strong>l</strong><strong>u</strong><strong>e</strong></span></p>
<ul>
<li><p>expressed as the matrix equation</p></li>
</ul>
<p><span class="math display">$$r = \begin{bmatrix}
\begin{matrix}
y_{1} \\
y_{2} \\
y_{3}
\end{matrix} \\
y_{4} \\
y_{5}
\end{bmatrix} - \left\lbrack \begin{matrix}
\begin{matrix}
1 \\
1 \\
1
\end{matrix} \\
1 \\
1
\end{matrix}\begin{matrix}
\begin{matrix}
{\mathbf{\ \ }\mathbf{x}}_{1} \\
{\ \ x}_{2} \\
{\ \ x}_{3}
\end{matrix} \\
{\ \ x}_{4} \\
{\ \ x}_{5}
\end{matrix} \right\rbrack\begin{bmatrix}
a \\
b
\end{bmatrix}$$</span></p>
<ul>
<li><p>which computes for every data point</p></li>
</ul>
<p><span class="math display"><strong>y</strong><sub><strong>i</strong></sub><strong>−</strong>(<strong>a</strong> <strong>+</strong> <strong>b</strong><strong>x</strong><sub><strong>i</strong></sub>)</span></p>
<ul>
<li><p>conceptually, this this means the data (<span class="math inline"><strong>y</strong></span>) equals the fitted line (<span class="math inline"><strong>A</strong><strong>c</strong></span>) plus error (<span class="math inline"><strong>r</strong></span>), or</p></li>
</ul>
<p><span class="math inline"><strong>y</strong><strong>=</strong></span> the <strong>data</strong></p>
<p><span class="math inline"><strong>A</strong><strong>c</strong><strong>=</strong></span> the <strong>model</strong></p>
<p><span class="math inline"><strong>r</strong><strong>=</strong></span> the <strong>‘leftover’</strong> part</p>
<p><span class="math display"><strong>y</strong> <strong>=</strong> <strong>A</strong><strong>c</strong> <strong>+</strong> <strong>r</strong></span></p>
<p>points: <strong>measured</strong> <strong>data</strong></p>
<p>8</p>
<p>6</p>
<p>4</p>
<p>2</p>
<p>vertical lines: <strong>residuals</strong></p>
<p>line: <strong>fitted</strong> <strong>model</strong></p>
<p>2 4 6 8 10</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr>
<th>Normal Equations</th>
<th><ul>
<li><p>we are trying to solve</p></li>
</ul>
<p><span class="math display"><em>A</em><em>c</em> ≈ <em>y</em></span></p>
<ul>
<li><p>but, usually there are more equations than knowns meaning no exact solutions exist</p></li>
<li><p>so, instead we ask<em>: which vector makes</em> <span class="math inline"><strong>A</strong><strong>c</strong></span> <em>as close as possible to</em> <span class="math inline"><strong>y</strong></span><em>?</em></p></li>
<li><p>to find the “close as possible” solution we measure the error using the residual</p></li>
</ul>
<p>primary goal</p>
<p><span class="math inline"><strong>r</strong> <strong>=</strong> <strong>y</strong> <strong>−</strong> <strong>A</strong><strong>c</strong></span>, minimizing <span class="math inline">||<strong>r</strong>||</span></p>
<ul>
<li><p>the key geometric idea, the best approximation <span class="math inline"><strong>p</strong> <strong>=</strong> <strong>A</strong><strong>c</strong></span> happens when</p></li>
</ul>
<p><strong>normal</strong> <strong>equations</strong></p>
<p>this says:</p>
<p>“the <strong>error</strong> must be <strong>perpendicular</strong> to the <strong>column</strong> <strong>space</strong>”</p>
<p><span class="math display"><strong>A</strong><sup><strong>T</strong></sup>(<strong>y</strong> <strong>−</strong> <strong>p</strong>) <strong>=</strong> <strong>0</strong></span></p>
<ul>
<li><p>turning that into equations, if <span class="math inline"><strong>p</strong> <strong>=</strong> <strong>A</strong><strong>c</strong></span></p></li>
</ul>
<p>projection <strong>condition</strong></p>
<p><span class="math display"><strong>A</strong><sup><strong>T</strong></sup><strong>y</strong><strong>=</strong><strong>A</strong><sup><strong>T</strong></sup><strong>A</strong><strong>c</strong></span></p>
<ul>
<li><p>solving for <span class="math inline"><strong>c</strong></span>, if <span class="math inline"><strong>A</strong><sup><strong>T</strong></sup><strong>A</strong></span> is invertible</p></li>
</ul>
<p><strong>gives</strong> least sq. <strong>solution</strong></p>
<p><span class="math display"><em>c</em> = (<em>A</em><sup><em>T</em></sup><em>A</em>)<sup>−1</sup><em>A</em><sup><em>T</em></sup><em>y</em></span></p>
<ul>
<li><p>what this accomplishes</p>
<ul>
<li><p>makes the residual perpendicular to the columns of <span class="math inline"><strong>A</strong></span></p></li>
<li><p>minimizes the size of the residual vector</p></li>
<li><p>gives the best approximation inside the column space</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; A = [1 1;2 1;3 1;4 1;6 1];</strong></p>
<p><strong>julia&gt; y = [2 4 5 4 7 0]';</strong></p>
<p><strong>julia&gt; c = (A'*A)\(A'*y)</strong></p>
<p><strong>2x1 Matrix{Float64}:</strong></p>
<p><strong>0.8513513513513513</strong></p>
<p><strong>1.0</strong></p>
<p><strong>julia&gt; c = A\y</strong></p>
<p><strong>2x1 Matrix{Float64}:</strong></p>
<p><strong>1.6756756756756768</strong></p>
<p><strong>0.8513513513513514</strong></p>
<p><strong>julia&gt; r = y-A*c</strong></p>
<p><strong>5x1 Matrix{Float64}:</strong></p>
<p><strong>-0.5270270270270281</strong></p>
<p><strong>0.6216216216216202</strong></p>
<p><strong>0.7702702702702684</strong></p>
<p><strong>-1.0810810810810825</strong></p>
<p><strong>-0.8108108108108102</strong></p></td>
</tr>
<tr>
<td>Generalization</td>
<td><ul>
<li><p>so far, we have <strong>discussed</strong> straight <strong>lines</strong>, but <strong>least</strong> <strong>squares</strong> can be <strong>applied</strong> to more <strong>complicated</strong> models</p></li>
</ul>
<p>a = <strong>intercept</strong></p>
<p>b = linear <strong>slope</strong></p>
<p><strong>c = curvature</strong></p>
<p><span class="math display"><strong>f</strong>(<strong>x</strong>) <strong>=</strong> <strong>a</strong> <strong>+</strong> <strong>b</strong><strong>x</strong> <strong>+</strong> <strong>c</strong><strong>x</strong><sup><strong>2</strong></sup></span></p>
<ul>
<li><p>this is clearly the <strong>equation</strong> of a <strong>parabola</strong></p></li>
<li><p>we still <strong>solve</strong></p></li>
</ul>
<p>this holds <strong>true</strong> for <strong>any</strong> degree <strong>polynomial</strong></p>
<p><span class="math display"><strong>A</strong><sup><strong>T</strong></sup><strong>A</strong><strong>c</strong><strong>=</strong><strong>A</strong><sup><strong>T</strong></sup><strong>y</strong></span></p>
<ul>
<li><p>we still <strong>compute</strong></p></li>
</ul>
<p><span class="math display"><strong>c</strong><strong>=</strong>(<strong>A</strong><sup><strong>T</strong></sup><strong>A</strong>)<sup><strong>−</strong><strong>1</strong></sup>  </span></p></td>
</tr>
</tbody>
</table>
