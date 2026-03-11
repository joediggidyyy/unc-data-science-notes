---
generated_at_utc: 2026-03-08T23:56:04+00:00
generated_from: notes/Spring_2026/DATA750/Week07/docx/DATA750_week07_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA750_week07_notes.pdf](../DATA750_week07_notes.pdf)
> - DOCX: [DATA750_week07_notes.docx](DATA750_week07_notes.docx)

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
<th colspan="2">Eigenvalues</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td colspan="2" style="text-align: right;"><em>`</em></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>geometric understanding for eigenvalues and eigenvectors and how they relate to matrices</p></li>
<li><p>matrix transformation using diagonalization</p></li>
<li><p>special properties of symmetric matrices</p></li>
<li><p>orthogonal matrices, rotations and projection</p></li>
<li><p>SPD matrices and connection to quadratic forms</p></li>
<li><p>convolution, DFTs and eigen-decomposition</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4">Geometric Interpretation of <span class="math inline"><strong>A</strong><strong>x</strong></span></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td>Mapping</td>
<td colspan="4"><ul>
<li><p>eigenvalue <strong>decomposition</strong> can reveal <strong>structure</strong> of a matrix as an <strong>operator</strong></p></li>
</ul>
<p><strong><em>A = S</em></strong> <span class="math inline"><strong>Λ</strong></span><em><strong>S⁻¹</strong></em></p>
<ul>
<li><p><strong>apply</strong> to <span class="math inline">$\overrightarrow{\mathbf{x}}$</span> and move <strong>right</strong> to <strong>left</strong></p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>x</strong> <strong>=</strong> <strong>S</strong>(<strong>Λ</strong>(<strong>S</strong><sup><strong>−</strong><strong>1</strong></sup><strong>x</strong>))</span></p>
<ul>
<li><p>example:</p></li>
</ul>
<p><span class="math display">$$\mathbf{A =}\begin{bmatrix}
\mathbf{3} &amp; \mathbf{- 1} \\
\mathbf{- 1} &amp; \mathbf{3}
\end{bmatrix}$$</span></p>
<p><span class="math display">$$\mathbf{S =}\begin{bmatrix}
\mathbf{1} &amp; \mathbf{- 1} \\
\mathbf{- 1} &amp; \mathbf{1}
\end{bmatrix}\mathbf{\ \ \ \ \ \ \ }\mathbf{\Lambda}\mathbf{=}\begin{bmatrix}
\mathbf{2} &amp; \mathbf{0} \\
\mathbf{0} &amp; \mathbf{4}
\end{bmatrix}$$</span></p></td>
</tr>
<tr>
<td>Julia</td>
<td colspan="4"><p><strong>julia&gt; A = [3 -1; -1 3]</strong></p>
<p><strong>2×2 Matrix{Int64}:</strong></p>
<p><strong>3 -1</strong></p>
<p><strong>-1 3</strong></p>
<p><strong>julia&gt; eigen(A)</strong></p>
<p><strong>EigenFloat64, Float64, Matrix{Float64}, Vector{Float64})</strong></p>
<p><strong>values:</strong></p>
<p><strong>2-element Vector{Float64}:</strong></p>
<p><strong>2.0</strong></p>
<p><strong>4.0</strong></p>
<p><strong>vectors:</strong></p>
<p><strong>2×2 Matrix{Float64}:</strong></p>
<p><strong>0.707107 -0.707107</strong></p>
<p><strong>0.707107 0.707107</strong></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 30%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>1. Coordinate</th>
<th colspan="2"><p><span class="math display"><strong>A</strong><strong>x</strong> <strong>=</strong> <strong>S</strong>(<strong>Λ</strong>(<strong>S</strong><sup><strong>−</strong><strong>1</strong></sup><strong>x</strong>))</span></p>
<ul>
<li><p>definition of an inverse 2 x 2 matrix</p></li>
</ul>
<p><span class="math display">$$\mathbf{S}^{\mathbf{- 1}}\begin{bmatrix}
\mathbf{a} &amp; \mathbf{b} \\
\mathbf{c} &amp; \mathbf{d}
\end{bmatrix}^{\mathbf{- 1}}\mathbf{=}\frac{\mathbf{1}}{\mathbf{ad - bc}}\begin{bmatrix}
\mathbf{d} &amp; \mathbf{- b} \\
\mathbf{- c} &amp; \mathbf{a}
\end{bmatrix}$$</span></p>
<ul>
<li><p>so, for the matrix</p></li>
</ul>
<p><span class="math display">$$\mathbf{S =}\begin{bmatrix}
\mathbf{1} &amp; \mathbf{- 1} \\
\mathbf{1} &amp; \mathbf{1}
\end{bmatrix}\mathbf{,\ \ \ \ }\mathbf{S}^{\mathbf{- 1}}\mathbf{=}\frac{\mathbf{1}}{\mathbf{2}}\begin{bmatrix}
\mathbf{1} &amp; \mathbf{1} \\
\mathbf{- 1} &amp; \mathbf{1}
\end{bmatrix}$$</span></p>
<p>counterclockwise 45<sup>0</sup></p>
<p>scale up by <span class="math inline">$\sqrt{2}$</span></p>
<p>clockwise 45<sup>0</sup></p>
<p>scale down by <span class="math inline">$\sqrt{2}$</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>2. Scale</td>
<td colspan="2"><ul>
<li><p>multiplying by the <strong>eigenvalues</strong> in matrix <span class="math inline"><strong>Λ</strong></span> <strong>scales</strong> each vector <strong>independently</strong></p></li>
</ul>
<p>scales <span class="math inline"><em>x</em></span> by <span class="math inline">2</span></p>
<p>scales <span class="math inline"><em>y</em></span> by <span class="math inline">4</span></p>
<p><span class="math display">$$\mathbf{\Lambda}\mathbf{=}\begin{bmatrix}
\mathbf{2} &amp; \mathbf{0} \\
\mathbf{0} &amp; \mathbf{4}
\end{bmatrix}$$</span></p></td>
</tr>
<tr>
<td>3. Map Back</td>
<td colspan="2"><ul>
<li><p>finally, map back with <span class="math inline"><strong>S</strong></span></p></li>
</ul></td>
</tr>
<tr>
<td>Putting it Together</td>
<td colspan="2"><p><span class="math display"><strong>A</strong><strong>x</strong> <strong>=</strong> <strong>S</strong>(<strong>Λ</strong>(<strong>S</strong><sup><strong>−</strong><strong>1</strong></sup><strong>x</strong>))</span></p>
<p><span class="math display">$$\mathbf{Ax =}\begin{bmatrix}
\mathbf{1} &amp; \mathbf{- 1} \\
\mathbf{1} &amp; \mathbf{1}
\end{bmatrix}\begin{bmatrix}
\mathbf{2} &amp; \mathbf{0} \\
\mathbf{0} &amp; \mathbf{4}
\end{bmatrix}\left( \frac{\mathbf{1}}{\mathbf{2}}\begin{bmatrix}
\mathbf{1} &amp; \mathbf{1} \\
\mathbf{- 1} &amp; \mathbf{1}
\end{bmatrix}\mathbf{x} \right)\mathbf{=}\begin{bmatrix}
\mathbf{3} &amp; \mathbf{- 1} \\
\mathbf{- 1} &amp; \mathbf{3}
\end{bmatrix}\mathbf{x}$$</span></p>
<p><span class="math display">$$\mathbf{Ax =}\begin{bmatrix}
\mathbf{3}\mathbf{x}_{\mathbf{1}}\mathbf{-}\mathbf{x}_{\mathbf{2}} \\
\mathbf{-}\mathbf{x}_{\mathbf{1}}\mathbf{+ 3}\mathbf{x}_{\mathbf{2}}
\end{bmatrix}$$</span></p></td>
</tr>
<tr>
<td colspan="2">Symmetric Matrices</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td>Properties</td>
<td colspan="2"><ul>
<li><p>have <strong>real</strong> eigen <strong>values</strong> and <strong>vectors</strong></p></li>
<li><p><strong>orthogonal</strong> eigenvectors that <strong>span</strong> the <strong>space</strong></p></li>
<li><p>can be <strong>broken</strong> <strong>down</strong> into rank <span class="math inline"><strong>1</strong></span> matrices</p></li>
<li><p>easy to <strong>compute</strong> the 2-D norm and <strong>condition</strong> <strong>number</strong></p></li>
</ul>
<p>how much the output value of the function can change for a small change in the input argument</p>
<p><span class="math display">$$\left| \left| \mathbf{x} \right| \right|^{\mathbf{2}}\mathbf{=}\sqrt{\mathbf{x}_{\mathbf{1}}^{\mathbf{2}}\mathbf{+}\mathbf{x}_{\mathbf{2}}^{\mathbf{2}}}$$</span></p></td>
</tr>
<tr>
<td>Why Real Eigenvalues</td>
<td colspan="2"><ul>
<li><p>a <strong>matrix</strong> always has at least <strong>one</strong> <strong>eigenvalue</strong> (possibly <strong>complex</strong>)</p></li>
</ul>
<p><span class="math display"><strong>p</strong>(<strong>λ</strong>) <strong>=</strong> <strong>d</strong><strong>e</strong><strong>t</strong>(<strong>A</strong> <strong>−</strong> <strong>λ</strong><strong>I</strong>)<strong>=</strong>(<strong>−</strong><strong>1</strong>)<sup><strong>n</strong></sup><strong>λ</strong><sup><strong>n</strong></sup><strong>+</strong><strong>⋯</strong> <strong>+</strong> <strong>d</strong><strong>e</strong><strong>t</strong>(<strong>A</strong>)</span></p>
<ul>
<li><p>if, <span class="math inline"> <strong>A</strong><strong>u</strong> <strong>=</strong> <strong>λ</strong><strong>u</strong></span></p></li>
<li><p>for matrices, the <strong>dot</strong> <strong>product</strong> uses the <strong>complex conjugate</strong> transpose</p></li>
</ul>
<p><span class="math display">$$\left( \mathbf{Au} \right)^{\mathbf{H}}\mathbf{u\  = \ }\left( \mathbf{\lambda u} \right)^{\mathbf{H}}\mathbf{u\  = \ }\overline{\mathbf{\lambda}}\mathbf{u}^{\mathbf{H}}\mathbf{u\  = \ }\overline{\mathbf{\lambda}}\left| \textit{\textbf{|}}\mathbf{u} \right|\textit{\textbf{|}}^{\mathbf{2}}$$</span></p>
<p><span class="math display">$$\left( \mathbf{Au} \right)^{\mathbf{H}}\mathbf{u\  = \ }\mathbf{u}^{\mathbf{H}}\mathbf{A}^{\mathbf{H}}\mathbf{u\  = \ }\mathbf{u}^{\mathbf{H}}\mathbf{A\ u\  = \ }\mathbf{u}^{\mathbf{H}}\left( \mathbf{\lambda u} \right)\mathbf{= \ \lambda}\mathbf{u}^{\mathbf{H}}\mathbf{u\  = \ \lambda}\left| \textit{\textbf{|}}\mathbf{u} \right|\textit{\textbf{|}}^{\mathbf{2}}$$</span></p>
<p><span class="math inline">$\overline{\mathbf{z}}$</span> <strong>:</strong> obtained by <strong>reversing</strong> the <strong>sign</strong> of the <strong>imaginary</strong> part while <strong>keeping</strong> the <strong>real</strong> part the <strong>same</strong></p>
<ul>
<li><p>which <strong>implies</strong>,</p></li>
</ul>
<p><span class="math inline">$\overline{\mathbf{\lambda}}\mathbf{= \lambda}$</span> <span class="math inline"><strong>λ</strong>∈ ℝ</span></p></td>
</tr>
<tr>
<td>Why Orthogonal</td>
<td colspan="2"><ul>
<li><p>a key benefit of <strong>symmetric</strong> <strong>matrices</strong> is that the <strong>eigenvectors</strong> are <strong>orthogonal</strong></p></li>
</ul>
<p><span class="math inline"><strong>A</strong> <strong>u</strong><sub><strong>1</strong></sub><strong>=</strong> <strong>λ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub></span><strong>,</strong> <span class="math inline"><strong>A</strong> <strong>u</strong><sub><strong>2</strong></sub><strong>=</strong> <strong>λ</strong>  <sub><strong>2</strong></sub><strong>u</strong><sub><strong>2</strong></sub></span><strong>,</strong> <span class="math inline"><strong>λ</strong><sub><strong>1</strong></sub><strong>≠</strong> <strong>λ</strong><sub><strong>2</strong></sub></span> <span class="math inline"><strong>⇒</strong></span> <span class="math inline"><strong>u</strong><sub><strong>1</strong></sub><strong>•</strong><strong>u</strong><sub><strong>2</strong></sub> <strong>=</strong> <strong>0</strong></span></p>
<ul>
<li><p>why,</p></li>
</ul>
<p><span class="math display"><strong>u</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>A</strong> <strong>u</strong><sub><strong>2</strong></sub><strong>=</strong> <strong>u</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup>(<strong>A</strong> <strong>u</strong><sub><strong>2</strong></sub>)<strong>=</strong> <strong>u</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup>(<strong>λ</strong><sub><strong>2</strong></sub><strong>u</strong><sub><strong>2</strong></sub>)<strong>=</strong> <strong>λ</strong><sub><strong>2</strong></sub><strong>u</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>u</strong><sub><strong>2</strong></sub><strong>=</strong> <strong>λ</strong><sub><strong>2</strong></sub>(<strong>u</strong><sub><strong>1</strong></sub><strong>⋅</strong><strong>u</strong><sub><strong>2</strong></sub>)</span></p>
<p><span class="math display"><strong>u</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>A</strong> <strong>u</strong><sub><strong>2</strong></sub><strong>=</strong> (<strong>A</strong><sup><strong>T</strong></sup><strong>u</strong><sub><strong>1</strong></sub>)<sup><strong>T</strong></sup><strong>u</strong><sub><strong>2</strong></sub><strong>=</strong> (<strong>A</strong> <strong>u</strong><sub><strong>1</strong></sub>)<sup><strong>T</strong></sup><strong>u</strong><sub><strong>2</strong></sub><strong>=</strong> <strong>λ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>u</strong><sub><strong>2</strong></sub><strong>=</strong> <strong>λ</strong><sub><strong>1</strong></sub>(<strong>u</strong><sub><strong>1</strong></sub><strong>⋅</strong><strong>u</strong><sub><strong>2</strong></sub>)</span></p>
<ul>
<li><p>since the <strong>eigenvalues</strong> are <strong>different</strong>, the <strong>dot</strong> <strong>product</strong> has to be <span class="math inline"><strong>z</strong><strong>e</strong><strong>r</strong><strong>o</strong></span></p></li>
</ul>
<p><span class="math display"><strong>λ</strong><sub><strong>1</strong></sub>(<strong>u</strong><sub><strong>1</strong></sub><strong>⋅</strong><strong>u</strong><sub><strong>2</strong></sub>)<strong>=</strong> <strong>λ</strong><sub><strong>2</strong></sub>(<strong>u</strong><sub><strong>1</strong></sub><strong>⋅</strong><strong>u</strong><sub><strong>2</strong></sub>)</span></p>
<p><span class="math display">(<strong>λ</strong><sub><strong>1</strong></sub><strong>−</strong><strong>λ</strong><sub><strong>2</strong></sub>)(<strong>u</strong><sub><strong>1</strong></sub><strong>⋅</strong> <strong>u</strong><sub><strong>2</strong></sub>)<strong>=</strong> <strong>0</strong></span></p>
<p><span class="math display"><strong>u</strong><sub><strong>1</strong></sub><strong>⋅</strong><strong>u</strong><sub><strong>2</strong></sub><strong>=</strong> <strong>0</strong></span></p>
<ul>
<li><p><strong>normalize</strong> the <strong>eigenvectors</strong> so,</p></li>
</ul>
<p><span class="math display">$$|\textit{\textbf{|}}\mathbf{u}_{\mathbf{i}}^{\mathbf{2}}\mathbf{|}|\mathbf{= \ }\mathbf{u}_{\mathbf{i}}\mathbf{\cdot}\mathbf{u}_{\mathbf{i}}\mathbf{= \ 1}$$</span></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr>
<th>Orthogonal Diagonalization</th>
<th><ul>
<li><p><em>another benefit of symmetric matrices is that you have</em> <span class="math inline"><strong>n</strong> <strong>o</strong><strong>r</strong><strong>t</strong><strong>h</strong><strong>o</strong><strong>g</strong><strong>o</strong><strong>n</strong><strong>a</strong><strong>l</strong> <strong>e</strong><strong>i</strong><strong>g</strong><strong>e</strong><strong>n</strong><strong>v</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong><strong>s</strong></span></p></li>
</ul>
<p><span class="math display">$$\mathbf{q}_{\mathbf{i}}\mathbf{=}\frac{\mathbf{u}_{\mathbf{i}}}{\left| \left| \mathbf{u}_{\mathbf{i}} \right| \right|}\mathbf{\ }$$</span></p>
<ul>
<li><p><em>stack them into a matrix</em></p></li>
</ul>
<p><span class="math display">$$\mathbf{Q\  = \ }\left\lbrack \mathbf{q}_{\mathbf{1}}\textit{\textbf{;}}\mathbf{\ }\mathbf{q}_{\mathbf{2}}\textit{\textbf{;}}\mathbf{\ \cdots}\textit{\textbf{;}}\mathbf{\ }\mathbf{q}_{\mathbf{n}} \right\rbrack$$</span></p>
<ul>
<li><p><em>this is an orthogonal square matrix</em></p></li>
</ul>
<p><span class="math display"><strong>Q</strong><sup><strong>T</strong></sup><strong>Q</strong> <strong>=</strong> <strong>I</strong><strong>⇒</strong> <strong>Q</strong><sup><strong>−</strong><strong>1</strong></sup> <strong>=</strong> <strong>Q</strong><sup><strong>T</strong></sup></span></p>
<ul>
<li><p><em>this avoids explicitly computing a matrix inverse, which is required for general (non-symmetric) matrices</em></p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Spectral Decomposition</td>
<td><ul>
<li><p>this gives you a <strong>real</strong> <strong>valued</strong> <strong>factorization</strong></p></li>
</ul>
<p><span class="math display"><strong>A</strong> <strong>=</strong> <strong>Q</strong><strong>Λ</strong><strong>Q</strong><sup><strong>T</strong></sup></span></p>
<p><span class="math display">$$\mathbf{A\  = \ Q\ }\mathbf{\Lambda}\mathbf{Q}^{\mathbf{T}}\mathbf{= \ }\left\lbrack \mathbf{q}_{\mathbf{1}}\textit{\textbf{;}}\mathbf{\ }\mathbf{q}_{\mathbf{2}}\textit{\textbf{;}}\mathbf{\ \cdots}\textit{\textbf{;}}\mathbf{\ }\mathbf{q}_{\mathbf{n}} \right\rbrack\left\lbrack \begin{array}{r}
\mathbf{\lambda}_{\mathbf{1}}\mathbf{q}_{\mathbf{1}}^{\mathbf{T}} \\
\mathbf{.} \\
\mathbf{.} \\
\mathbf{.} \\
\mathbf{\lambda}_{\mathbf{n}}\mathbf{q}_{\mathbf{n}}^{\mathbf{T}}
\end{array} \right\rbrack$$</span></p>
<ul>
<li><p>apply this to a <span class="math inline"><strong>p</strong><strong>o</strong><strong>i</strong><strong>n</strong><strong>t</strong></span> <span class="math inline"><strong>x</strong></span></p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>x</strong> <strong>=</strong> <strong>λ</strong><sub><strong>1</strong></sub><strong>q</strong><sub><strong>1</strong></sub><strong>q</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>x</strong> <strong>+</strong> <strong>λ</strong><sub><strong>2</strong></sub><strong>q</strong><sub><strong>2</strong></sub><strong>q</strong><sub><strong>2</strong></sub><sup><strong>T</strong></sup><strong>x</strong> <strong>+</strong> <strong>⋯</strong><strong>+</strong> <strong>λ</strong><sub><strong>n</strong></sub><strong>q</strong><sub><strong>n</strong></sub><strong>q</strong><sub><strong>n</strong></sub><sup><strong>T</strong></sup><strong>x</strong></span></p>
<ul>
<li><p><strong>equivalent</strong> <strong>scalar</strong> form</p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>x</strong> <strong>=</strong> <strong>λ</strong><sub><strong>1</strong></sub>(<strong>q</strong><sub><strong>1</strong></sub><strong>⋅</strong><strong>x</strong>)<strong>q</strong><sub><strong>1</strong></sub><strong>+</strong> <strong>λ</strong><sub><strong>2</strong></sub>(<strong>q</strong><sub><strong>2</strong></sub><strong>⋅</strong><strong>x</strong>)<strong>q</strong><sub><strong>2</strong></sub><strong>+</strong><strong>⋯</strong><strong>+</strong><strong>λ</strong><sub><strong>n</strong></sub>(<strong>q</strong><sub><strong>n</strong></sub><strong>⋅</strong><strong>x</strong>)<strong>q</strong><sub><strong>n</strong></sub></span></p></td>
</tr>
<tr>
<td>Inverse</td>
<td><ul>
<li><p>if <strong>none</strong> of the eigenvalues are <span class="math inline"><strong>z</strong><strong>e</strong><strong>r</strong><strong>o</strong></span>, <span class="math inline"><strong>A</strong></span> is <strong>invertible</strong></p></li>
</ul>
<p><span class="math inline"><strong>A</strong><sup><strong>−</strong><strong>1</strong></sup> <strong>=</strong> <strong>Q</strong><strong>Λ</strong><sup><strong>−</strong><strong>1</strong></sup><strong>Q</strong><sup><strong>T</strong></sup></span> <span class="math inline"><strong>A</strong> <strong>=</strong> <strong>Q</strong><strong>Λ</strong><strong>Q</strong><sup><strong>T</strong></sup></span></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 29%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Quadratic Forms – SPD</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td>Symmetric Positive Definite</td>
<td colspan="2"><ul>
<li><p>symmetric matrices are always diagonalizable and have <strong>real eigenvalues</strong></p></li>
<li><p>if the eigenvalues are <strong>all positive</strong>, the matrix is called<br />
<strong>Symmetric Positive Definite (SPD)</strong></p></li>
<li><p>if they are <strong>all negative</strong>, the matrix is <strong>symmetric negative definite</strong></p></li>
<li><p>if they are <strong>all non-negative</strong> <span class="math inline">(≥ 0</span>), the matrix is <strong>symmetric positive semidefinite</strong></p></li>
<li><p><strong>projection</strong> expression</p></li>
</ul>
<p><span class="math display"><strong>q</strong><sub><strong>k</strong></sub><strong>q</strong><sub><strong>k</strong></sub><sup><strong>T</strong></sup><strong>x</strong> <strong>=</strong> (<strong>q</strong><sub><strong>k</strong></sub><strong>⋅</strong><strong>x</strong>)<strong>q</strong><sub><strong>k</strong></sub></span></p>
<ul>
<li><p>spectral <strong>expansion</strong> applied to a <strong>vector</strong></p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>x</strong> <strong>=</strong> <strong>λ</strong><sub><strong>1</strong></sub><strong>q</strong><sub><strong>1</strong></sub><strong>q</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>x</strong> <strong>+</strong> <strong>λ</strong><sub><strong>2</strong></sub><strong>q</strong><sub><strong>2</strong></sub><strong>q</strong><sub><strong>2</strong></sub><sup><strong>T</strong></sup><strong>x</strong> <strong>+</strong> <strong>⋯</strong><strong>+</strong> <strong>λ</strong><sub><strong>n</strong></sub><strong>q</strong><sub><strong>n</strong></sub><strong>q</strong><sub><strong>n</strong></sub><sup><strong>T</strong></sup><strong>x</strong></span></p>
<ul>
<li><p><strong>equivalent</strong> projection form</p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>x</strong> <strong>=</strong> <strong>λ</strong><sub><strong>1</strong></sub>(<strong>q</strong><sub><strong>1</strong></sub><strong>⋅</strong><strong>x</strong>)<strong>q</strong><sub><strong>1</strong></sub><strong>+</strong><strong>λ</strong><sub><strong>2</strong></sub>(<strong>q</strong><sub><strong>2</strong></sub><strong>⋅</strong><strong>x</strong>)<strong>q</strong><sub><strong>2</strong></sub><strong>+</strong><strong>⋯</strong><strong>+</strong> <strong>λ</strong><sub><strong>n</strong></sub>(<strong>q</strong><sub><strong>n</strong></sub><strong>⋅</strong><strong>x</strong>)<strong>q</strong><sub><strong>n</strong></sub></span></p></td>
</tr>
<tr>
<td>Quadratic Forms</td>
<td colspan="2"><ul>
<li><p>example of a <strong>quadratic</strong> form</p></li>
</ul>
<p><span class="math display"><strong>f</strong>(<strong>x</strong><strong>,</strong> <strong>y</strong>)<strong>=</strong> <strong>5</strong><strong>x</strong><sup><strong>2</strong></sup><strong>−</strong> <strong>2</strong><strong>x</strong><strong>y</strong> <strong>+</strong> <strong>5</strong><strong>y</strong><sup><strong>2</strong></sup></span></p>
<ul>
<li><p><strong>matrix</strong> form</p></li>
</ul>
<p><span class="math display"><strong>f</strong>(<strong>x</strong><strong>,</strong> <strong>y</strong>) <strong>=</strong> <strong>5</strong><strong>x</strong><sup><strong>2</strong></sup><strong>−</strong><strong>x</strong><strong>y</strong> <strong>−</strong> <strong>y</strong><strong>x</strong> <strong>+</strong> <strong>5</strong><strong>y</strong><sup><strong>2</strong></sup></span></p>
<blockquote>
<p><span class="math display"> <strong>=</strong> <strong>x</strong>(<strong>5</strong><strong>x</strong> <strong>−</strong> <strong>y</strong>)<strong>+</strong><strong>y</strong>(<strong>−</strong><strong>x</strong> <strong>+</strong> <strong>5</strong><strong>y</strong>)</span></p>
</blockquote>
<p><span class="math display">$$\mathbf{=}\left\lbrack \mathbf{x\ \ y} \right\rbrack\begin{bmatrix}
\mathbf{5} &amp; \mathbf{- 1} \\
\mathbf{- 1} &amp; \mathbf{5}
\end{bmatrix}\left\lbrack \begin{array}{r}
\mathbf{x} \\
\mathbf{y}
\end{array} \right\rbrack$$</span></p>
<p><span class="math display">$$\mathbf{=}\left\lbrack \mathbf{x\ \ y} \right\rbrack\left\lbrack \begin{array}{r}
\mathbf{5}\mathbf{x - y} \\
\mathbf{- x + 5}\mathbf{y}
\end{array} \right\rbrack$$</span></p>
<p><span class="math display">$$\mathbf{=}\left\lbrack \begin{array}{r}
\mathbf{x} \\
\mathbf{y}
\end{array} \right\rbrack^{\mathbf{T}}\mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^{\mathbf{T}}\left\lbrack \begin{array}{r}
\mathbf{x} \\
\mathbf{y}
\end{array} \right\rbrack$$</span></p>
<p><span class="math display"><strong>=</strong><strong>u</strong><sup><strong>T</strong></sup><strong>Λ</strong><strong>u</strong></span></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 29%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Julia</th>
<th colspan="2"><p>julia&gt; A = [5 -1; -1 5]</p>
<p>2×2 Matrix{Int64}:</p>
<p>5 -1</p>
<p>-1 5</p>
<p>julia&gt; eigen(A)</p>
<p>Eigen{Float64, Float64, Matrix{Float64}, Vector{Float64}}</p>
<p>values:</p>
<p>2-element Vector{Float64}:</p>
<p>4.0</p>
<p>6.0</p>
<p>vectors:</p>
<p>2×2 Matrix{Float64}:</p>
<p>-0.707107 -0.707107</p>
<p>-0.707107 0.707107</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Summary</td>
<td colspan="2"><ul>
<li><p>In general, for all <strong>symmetric</strong> matrices</p></li>
</ul>
<p><span class="math display"><strong>x</strong><sup><strong>T</strong></sup><strong>A</strong> <strong>x</strong> <strong>=</strong> (<strong>Q</strong><sup><strong>T</strong></sup><strong>x</strong>)<sup><strong>T</strong></sup><strong>Λ</strong>(<strong>Q</strong><sup><strong>T</strong></sup><strong>x</strong>)<strong>=</strong> <strong>u</strong><sup><strong>T</strong></sup><strong>Λ</strong><strong>u</strong> <strong>=</strong> <strong>λ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub><sup><strong>2</strong></sup><strong>+</strong> <strong>…</strong> <strong>+</strong> <strong>λ</strong><sub><strong>n</strong></sub><strong>u</strong><sub><strong>n</strong></sub><sup><strong>2</strong></sup></span></p>
<p>If the <strong>matrix</strong> is:</p>
<ul>
<li><p><strong>SPD</strong></p>
<ul>
<li><p>then all <strong>eigenvalues</strong> are strictly <strong>greater</strong> than <span class="math inline"><strong>0</strong></span></p></li>
<li><p>the form is <strong>convex</strong></p></li>
<li><p>passes <strong>through</strong> the <strong>origin</strong></p></li>
</ul></li>
<li><p><strong>negative</strong> definite</p>
<ul>
<li><p><span class="math inline"><strong>0</strong></span> is the <strong>unique</strong> <strong>maximum</strong></p></li>
</ul></li>
<li><p><strong>some</strong> eigenvalues are <strong>negative</strong> and others <strong>positive</strong></p>
<ul>
<li><p>the <strong>quadratic</strong> form has a <strong>saddle</strong> <strong>point</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Matrix Norm</td>
<td colspan="2"><ul>
<li><p>for matrix <strong>norms</strong>, we define</p></li>
</ul>
<p><span class="math display">$$\left| \textit{\textbf{|}}\mathbf{A} \right|\textit{\textbf{|}}\mathbf{\ }\mathbf{= \ }\mathbf{\max}_{\mathbf{x \neq 0\ }}\frac{\left| \left| \mathbf{Ax} \right| \right|}{\left| \left| \mathbf{x} \right| \right|}\mathbf{=}\mathbf{\max}_{\left| \left| \mathbf{x} \right| \right|\mathbf{= 1}}\left| \left| \mathbf{Ax} \right| \right|$$</span></p>
<ul>
<li><p><strong>Euclidean</strong> <strong>distance</strong> formula (<strong>2-norm</strong>)</p></li>
</ul>
<p><span class="math display">$$\mathbf{|}\textit{\textbf{|}}\mathbf{Ax}{\mathbf{|}\textit{\textbf{|}}}^{\mathbf{2}}\mathbf{= \ }\left( \mathbf{Ax} \right)^{\mathbf{T}}\left( \mathbf{Ax} \right)\mathbf{=}\mathbf{x}^{\mathbf{T}}\mathbf{A}^{\mathbf{T}}\mathbf{Ax =}\left( \mathbf{Q}^{\mathbf{T}}\mathbf{x} \right)^{\mathbf{T}}\mathbf{\Lambda}\left( \mathbf{Q}^{\mathbf{T}}\mathbf{x} \right)$$</span></p>
<ul>
<li><p>change of variables</p></li>
</ul>
<p><span class="math display">$$\left| \textit{\textbf{|}}\mathbf{x} \right|\textit{\textbf{|}}\mathbf{=}\mathbf{1}\mathbf{,}\mathbf{\ \ u =}\mathbf{Q}^{\mathbf{T}}\mathbf{x\ \ \  \Rightarrow}\mathbf{\ \ }\textit{\textbf{|}}\left| \mathbf{u} \right|\textit{\textbf{|}}\mathbf{=}\textit{\textbf{|}}\left| \mathbf{x} \right|\textit{\textbf{|}}\mathbf{=}\mathbf{1}$$</span></p>
<ul>
<li><p>bounding <strong>expressions</strong></p></li>
</ul>
<p><span class="math display">$$\textit{\textbf{|}}\left| \mathbf{Ax} \right|\textit{\textbf{|}}^{\mathbf{2}}\mathbf{=}\mathbf{\lambda}_{\mathbf{1}}\mathbf{u}_{\mathbf{1}}^{\mathbf{2}}\mathbf{+ \cdots +}\mathbf{\lambda}_{\mathbf{n}}\mathbf{u}_{\mathbf{n}}^{\mathbf{2}}\mathbf{\leq}\mathbf{\lambda}_{\mathbf{\max}}\left( \mathbf{u}_{\mathbf{1}}^{\mathbf{2}}\mathbf{+ \ \cdots + \ }\mathbf{u}_{\mathbf{n}}^{\mathbf{2}} \right)\mathbf{=}\mathbf{\lambda}_{\mathbf{\max}}$$</span></p>
<ul>
<li><p><strong>matrix</strong> 2-norm</p></li>
</ul>
<p><span class="math display">$$\textit{\textbf{|}}\mathbf{A}\textit{\textbf{|}}_{\mathbf{2}}\mathbf{=}\sqrt{\left( \mathbf{\lambda}_{\mathbf{\max}}\left( \mathbf{A}^{\mathbf{T}}\mathbf{A} \right) \right)}\mathbf{=}\mathbf{\sigma}_{\mathbf{\max}}\left( \mathbf{A} \right)\mathbf{\,}$$</span></p></td>
</tr>
<tr>
<td colspan="2">Eigenvalues for 1-D Convolution</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td>Convolution: 1D</td>
<td colspan="2"><ul>
<li><p>the <strong>DFT</strong> links <strong>convolutions</strong> and eigen <strong>decompositions</strong></p></li>
<li><p>simple 1-D <strong>convolution</strong>:</p>
<ul>
<li><p>input: <span class="math inline">$\overrightarrow{\mathbf{u}}$</span></p></li>
<li><p>output: <span class="math inline">$\overrightarrow{\mathbf{v}}$</span></p></li>
</ul></li>
</ul>
<p><span class="math display">$$\mathbf{v}_{\mathbf{j}}\mathbf{=}\frac{\mathbf{u}_{\mathbf{j - 1}}}{\mathbf{4}}\mathbf{+}\frac{\mathbf{u}_{\mathbf{j}}}{\mathbf{2}}\mathbf{+}\frac{\mathbf{u}_{\mathbf{j + 1}}}{\mathbf{4}}$$</span></p></td>
</tr>
<tr>
<td><p>Convolution:</p>
<p>Eigenvector</p></td>
<td colspan="2"><ul>
<li><p>use <strong>vectors</strong> from <strong>DFT</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{u}_{\mathbf{j}}\mathbf{=}\mathbf{\exp}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{kj}}{\mathbf{n}} \right)$$</span></p>
<ul>
<li><p><strong>evaluate</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{v}_{\mathbf{j}}\mathbf{=}\frac{\mathbf{u}_{\mathbf{j - 1}}}{\mathbf{4}}\mathbf{+}\frac{\mathbf{u}_{\mathbf{j}}}{\mathbf{2}}\mathbf{+}\frac{\mathbf{u}_{\mathbf{j + 1}}}{\mathbf{4}}$$</span></p>
<p><span class="math display">$$\mathbf{=}\frac{\mathbf{1}}{\mathbf{4}}\mathbf{\exp}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{k}\left( \mathbf{j - 1} \right)}{\mathbf{n}} \right)\mathbf{+}\frac{\mathbf{1}}{\mathbf{2}}\mathbf{\exp}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{kj}}{\mathbf{n}} \right)\mathbf{+}\frac{\mathbf{1}}{\mathbf{4}}\mathbf{\exp}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{k}\left( \mathbf{j + 1} \right)}{\mathbf{n}} \right)$$</span></p>
<p><span class="math display">$$\mathbf{=}\mathbf{\exp}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{kj}}{\mathbf{n}} \right)\mathbf{(}\frac{\mathbf{1}}{\mathbf{4}}\mathbf{\exp}\left( \mathbf{-}\frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{k}}{\mathbf{n}} \right)\mathbf{+}\frac{\mathbf{1}}{\mathbf{2}}\mathbf{+}\frac{\mathbf{1}}{\mathbf{4}}\mathbf{\exp}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{k}}{\mathbf{n}} \right)$$</span></p>
<p><span class="math display">$$\mathbf{=}\mathbf{\exp}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{kj}}{\mathbf{n}} \right)\left( \frac{\mathbf{1}}{\mathbf{2}}\mathbf{\cos}\left( \frac{\mathbf{2}\mathbf{\pi}\mathbf{k}}{\mathbf{n}} \right)\mathbf{+}\frac{\mathbf{1}}{\mathbf{2}} \right)$$</span></p>
<p><span class="math display"><strong>c</strong><strong>o</strong><strong>n</strong><strong>s</strong><strong>t</strong><strong>a</strong><strong>n</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>u</strong><sub><strong>j</strong></sub></span></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr>
<th>Convolution Operator</th>
<th><ul>
<li><p>consider,</p></li>
</ul>
<p><span class="math display">$$\mathbf{v}_{\mathbf{j}}\mathbf{=}\frac{\mathbf{u}_{\mathbf{j - 1}}}{\mathbf{4}}\mathbf{+}\frac{\mathbf{u}_{\mathbf{j}}}{\mathbf{2}}\mathbf{+}\frac{\mathbf{u}_{\mathbf{j + 1}}}{\mathbf{4}}$$</span></p>
<ul>
<li><p>with periodic boundary condition</p></li>
</ul>
<p><span class="math display"><strong>v</strong><strong>=</strong><strong>L</strong>(<strong>u</strong>)<strong>,</strong> <strong>L</strong><strong>:</strong>ℝ<sup></sup><strong>→</strong>ℝ<sup></sup></span></p>
<ul>
<li><p>the Fourier frequency vector</p></li>
</ul>
<p><span class="math display">$$\mathbf{q}_{\mathbf{k}}\mathbf{=}\left( \frac{\mathbf{1}}{\sqrt{\mathbf{n}}}\mathbf{ex}\mathbf{p}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{kj}}{\mathbf{n}} \right) \right)_{\mathbf{j = 1,}\mathbf{\ldots}\mathbf{,n}}$$</span></p>
<ul>
<li><p>eigenvector relation</p></li>
</ul>
<p><span class="math display"><strong>L</strong>(<strong>q</strong><sub><strong>k</strong></sub>)<strong>=</strong><strong>λ</strong><sub><strong>k</strong></sub><strong>q</strong><sub><strong>k</strong></sub></span></p>
<ul>
<li><p>eigenvalue</p></li>
</ul>
<p><span class="math display">$$\mathbf{\lambda}_{\mathbf{k}}\mathbf{=}\frac{\mathbf{co}\mathbf{s}\left( \frac{\mathbf{2}\mathbf{\pi}\mathbf{k}}{\mathbf{n}} \right)\mathbf{+ 1}}{\mathbf{2}}$$</span></p>
<ul>
<li><p>diagonalization of the operator</p></li>
</ul>
<p><span class="math display"><strong>L</strong>(<strong>u</strong>) <strong>=</strong> <strong>Q</strong><strong>Λ</strong><strong>Q</strong><sup><strong>H</strong></sup><strong>u</strong></span></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr>
<th><p>Convolution:</p>
<p>DFT</p></th>
<th><ul>
<li><p>since the Fourier frequencies are eigenvectors for the convolution operator, we can use that to evaluate the convolution</p></li>
<li><p>applying the operator (in a periodic domain)</p></li>
</ul>
<p><span class="math display">$$\mathbf{v}_{\mathbf{j}}\mathbf{=}\frac{\mathbf{u}_{\mathbf{j - 1}}}{\mathbf{4}}\mathbf{+}\frac{\mathbf{u}_{\mathbf{j}}}{\mathbf{2}}\mathbf{+}\frac{\mathbf{u}_{\mathbf{j + 1}}}{\mathbf{4}}$$</span></p>
<ul>
<li><p>equivalent matrix form</p></li>
</ul>
<p><span class="math display"><strong>v</strong> <strong>=</strong> <strong>Q</strong><strong>Λ</strong><strong>Q</strong><sup><strong>H</strong></sup><strong>u</strong></span></p>
<ul>
<li><p>eigenvalues</p></li>
</ul>
<p><span class="math display">$$\mathbf{\lambda}_{\mathbf{k}}\mathbf{=}\frac{\left( \mathbf{\cos}\left( \frac{\mathbf{2\pi k}}{\mathbf{n}} \right)\mathbf{+ 1} \right)}{\mathbf{2}}$$</span></p>
<ul>
<li><p>using the DFT:</p></li>
</ul>
<p><span class="math inline"><strong>Q</strong><sup><strong>H</strong></sup><strong>u</strong></span> apply the Fourier transform to <span class="math inline"><strong>u</strong></span></p>
<p><span class="math inline">     <strong>Λ</strong><strong>Q</strong><sup><strong>H</strong></sup><strong>u</strong></span> scale each <span class="math inline"><strong>k</strong> </span>component by the eigenvalue for the operator</p>
<p><span class="math inline"><strong>Q</strong><strong>Λ</strong><strong>Q</strong><sup><strong>H</strong></sup><strong>u</strong></span> apply the inverse Fourier transform to the output</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>

,
