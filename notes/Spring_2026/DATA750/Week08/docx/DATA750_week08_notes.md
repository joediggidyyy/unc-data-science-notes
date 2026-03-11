---
generated_at_utc: 2026-03-08T23:56:04+00:00
generated_from: notes/Spring_2026/DATA750/Week08/docx/DATA750_week08_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA750_week08_notes.pdf](../DATA750_week08_notes.pdf)
> - DOCX: [DATA750_week08_notes.docx](DATA750_week08_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Singular Value Decomposition</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>eigenvalues, and eigenvectors, and higher-dimensional tensors</p></li>
<li><p>convolution in 2-D as a linear transformation</p></li>
<li><p>convolution and eigen decomposition</p></li>
<li><p>SVD decomposition</p></li>
<li><p>left and right singular values</p></li>
<li><p>computing and utilizing numerical libraries</p></li>
<li><p>similarity/relationship between SVD and matrix diagonalization</p></li>
<li><p>computing rank-k approximations</p></li>
<li><p>using the Frobenius norm to compute distances in matrix space</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5">Eigenvalues for 2D Convolution</td>
</tr>
<tr>
<td>Convolution: 2D</td>
<td colspan="4"><ul>
<li><p>this is very similar to the 1-D case</p></li>
</ul>
<p><span class="math display">$$\mathbf{v}_{\mathbf{j}_{\mathbf{1}}\mathbf{,}\mathbf{j}_{\mathbf{2}}}^{\mathbf{k}_{\mathbf{1}}\mathbf{,}\mathbf{k}_{\mathbf{2}}}\mathbf{=}\mathbf{\exp}{\textit{\textbf{!}}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{j}_{\mathbf{1}}\mathbf{k}_{\mathbf{1}}}{\mathbf{N}_{\mathbf{1}}} \right)}\mathbf{\exp}{\textit{\textbf{!}}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{j}_{\mathbf{2}}\mathbf{k}_{\mathbf{2}}}{\mathbf{N}_{\mathbf{2}}} \right)}$$</span></p>
<p>freq in x direction</p>
<p>freq in y direction</p>
<ul>
<li><p>ex: the <strong>LaPlace</strong> kernel</p></li>
</ul>
<p>eigenvectors for any convolutional kernel</p>
<p><span class="math display"><strong>−</strong><strong>u</strong><sub><strong>i</strong><strong>,</strong> <strong>j</strong> <strong>−</strong> <strong>1</strong></sub><strong>−</strong><strong>u</strong><sub><strong>i</strong> <strong>−</strong> <strong>1</strong><strong>,</strong> <strong>j</strong></sub><strong>+</strong><strong>4</strong><strong>u</strong><sub><strong>i</strong><strong>,</strong> <strong>j</strong></sub><strong>−</strong><strong>u</strong><sub><strong>i</strong> <strong>+</strong> <strong>1</strong><strong>,</strong> <strong>j</strong></sub><strong>−</strong><strong>u</strong><sub><strong>i</strong><strong>,</strong> <strong>j</strong> <strong>+</strong> <strong>1</strong></sub></span></p>
<p>each term is just a shift in the i or j coordinate</p></td>
</tr>
<tr>
<td>Numerical</td>
<td colspan="4"><p><span class="math display"><strong>Q</strong><strong>Λ</strong><strong>Q</strong><sup><strong>H</strong></sup><strong>u</strong></span></p>
<ul>
<li><p>for an <span class="math inline"><strong>m</strong> <strong>×</strong> <strong>n</strong></span> <span class="math inline"><strong>2</strong> <strong>−</strong> <strong>D</strong> <strong>a</strong><strong>r</strong><strong>r</strong><strong>a</strong><strong>y</strong></span>, each matrix is <span class="math inline"><strong>M</strong><strong>N</strong> <strong>×</strong> <strong>M</strong><strong>N</strong></span></p></li>
</ul>
<p>one of <span class="math inline"><strong>M</strong> <strong>×</strong> <strong>N</strong></span> vectors in the <span class="math inline"><strong>Q</strong> <strong>m</strong><strong>a</strong><strong>t</strong><strong>r</strong><strong>i</strong><strong>x</strong></span></p>
<ul>
<li><p><strong>Fourier</strong> mode</p></li>
</ul>
<p><span class="math display">$$\mathbf{v}_{\mathbf{j}_{\mathbf{1}}\mathbf{,}\mathbf{j}_{\mathbf{2}}}^{\mathbf{k}_{\mathbf{1}}\mathbf{,}\mathbf{k}_{\mathbf{2}}}\mathbf{=}\mathbf{\exp}{\textit{\textbf{!}}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{j}_{\mathbf{1}}\mathbf{k}_{\mathbf{1}}}{\mathbf{N}_{\mathbf{1}}} \right)}\mathbf{\exp}{\textit{\textbf{!}}\left( \frac{\mathbf{i}\mathbf{2}\mathbf{\pi}\mathbf{j}_{\mathbf{2}}\mathbf{k}_{\mathbf{2}}}{\mathbf{N}_{\mathbf{2}}} \right)}$$</span></p>
<ul>
<li><p><strong>however,</strong> if <span class="math inline"><strong>M</strong> <strong>a</strong><strong>n</strong><strong>d</strong> <strong>N</strong></span> are powers of <span class="math inline"><strong>2</strong></span>, the <strong>cost</strong> of the <strong>FFT</strong> is</p></li>
</ul>
<p><span class="math inline"><strong>O</strong>(<strong>M</strong><strong>N</strong>(<strong>log</strong> (<strong>M</strong>)<strong>+</strong><strong>log</strong> (<strong>N</strong>)))</span> and not <span class="math inline"><strong>O</strong>((<strong>M</strong><strong>N</strong>)<sup><strong>2</strong></sup>)</span></p></td>
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
<th rowspan="4">Julia</th>
<th><p>Steps</p>
<p>1</p>
<ul>
<li><p>first, set up a simple <span class="math inline"><strong>u</strong></span> where we know the answer</p></li>
<li><p>create the Laplace stencil on a periodic domain</p></li>
</ul>
<p>2</p>
<ul>
<li><p>evaluate the Fourier transform of the stencil</p></li>
</ul>
<p>3</p>
<p>note that the values are all real numbers</p>
<ul>
<li><p>these correspond to the eigenvalues, but they are packed into an array rather than listed individually</p></li>
<li><p>the top-left entry is <span class="math inline"><strong>0</strong></span>, because that is the eigenvalue corresponding to the constant function <span class="math inline"><strong>1</strong></span></p></li>
</ul></th>
</tr>
<tr>
<th><p><strong>julia&gt; using FFTW</strong></p>
<p>1</p>
<p><strong>julia&gt; u = zeros(6,6); u[3,4] = 1;</strong></p>
<p><strong>6×6 Matrix{Float64}:</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 1.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p>2</p>
<p><strong>julia&gt; s=zeros(6,6); s[1,1]=4; s[2,1]=-1; s[1,2]=-1; s[6,1]=-1; s[1,6]=1;</strong></p>
<p><strong>6×6 Matrix{Float64}:</strong></p>
<p><strong>4.0 -1.0 0.0 0.0 0.0 -1.0</strong></p>
<p><strong>-1.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>-1.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p>3</p>
<p><strong>julia&gt; L = fft(s)</strong></p>
<p><strong>6×6 Matrix{ComplexF64}:</strong></p>
<p><strong>0.0+0.0im 1.0+0.0im 3.0+0.0im 4.0+0.0im 3.0+0.0im 1.0+0.0im</strong></p>
<p><strong>1.0+0.0im 2.0+0.0im 4.0+0.0im 5.0+0.0im 4.0+0.0im 2.0+0.0im</strong></p>
<p><strong>3.0+0.0im 4.0+0.0im 6.0+0.0im 7.0+0.0im 6.0+0.0im 4.0+0.0im</strong></p>
<p><strong>4.0+0.0im 5.0+0.0im 7.0+0.0im 8.0+0.0im 7.0+0.0im 5.0+0.0im</strong></p>
<p><strong>3.0+0.0im 4.0+0.0im 6.0+0.0im 7.0+0.0im 6.0+0.0im 4.0+0.0im</strong></p>
<p><strong>1.0+0.0im 2.0+0.0im 4.0+0.0im 5.0+0.0im 4.0+0.0im 2.0+0.0im</strong></p></th>
</tr>
<tr>
<th><ul>
<li><p>now, we <strong>evaluate</strong></p></li>
</ul>
<p><span class="math display"><strong>Q</strong><strong>Λ</strong><strong>Q</strong><sup><strong>H</strong></sup><strong>u</strong></span></p>
<ul>
<li><p>the <strong>diagonal</strong> matrix just <strong>scales</strong> each <strong>element</strong> of the <strong>vector</strong></p></li>
</ul>
<p>both are packed the same way as <span class="math inline">2<em>D</em></span> arrays</p>
<ul>
<li><p>the <strong>last</strong> product is the <strong>inverse</strong> <span class="math inline"><strong>D</strong><strong>F</strong><strong>T</strong></span></p></li>
<li><p>because the <strong>initial</strong> <strong>vector</strong> was <strong>simple</strong>, the <strong>convolution</strong> just <strong>inserts</strong> the <strong>stencil</strong></p></li>
<li><p>because of the <strong>three</strong> <span class="math inline"><strong>F</strong><strong>F</strong><strong>T</strong></span> calls, the <strong>total</strong> <strong>cost</strong> is</p></li>
</ul>
<p><span class="math display"><strong>O</strong>(<strong>M</strong><strong>N</strong>(<strong>log</strong> (<strong>M</strong>)<strong>+</strong><strong>l</strong><strong>o</strong><strong>g</strong>(<strong>N</strong>)))</span></p></th>
</tr>
<tr>
<th><p><strong>julia&gt; first = L.*fft(u);</strong></p>
<p><strong>julia&gt; sol = ifft(first)</strong></p>
<p><strong>6×6 Matrix{ComplexF64}:</strong></p>
<p><strong>0.0+0.0im 0.0+0.0im 0.0+0.0im 0.0+0.0im 0.0+0.0im 0.0+0.0im</strong></p>
<p><strong>0.0+0.0im 0.0+0.0im 0.0+0.0im 0.0+0.0im -1.0+0.0im 0.0+0.0im</strong></p>
<p><strong>1.23358e-16+0.0im -2.46716e-17+0.0im -2.46716e-17+0.0im -2.46716e-17+0.0im</strong></p>
<p><strong>3.70074e-17+0.0im 1.23358e-17+0.0im -3.70074e-17+0.0im 1.23358e-17+0.0im</strong></p>
<p><strong>julia&gt; real(sol)</strong></p>
<p><strong>6×6 Matrix{Float64}:</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 -1.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 -4.0 -1.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 -1.0 0.0 0.0</strong></p>
<p><strong>1.23358e-16 -2.46716e-17 -2.46716e-17 1.23358e-16 -2.46716e-17 -2.46716e-17</strong></p>
<p><strong>3.70074e-17 1.23358e-17 -3.70074e-17 1.23358e-17 -3.70074e-17 1.23358e-17</strong></p></th>
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
<th rowspan="2">Convolution</th>
<th><ul>
<li><p>this method is used in codes that compute a convolution</p></li>
<li><p>here is a library function that takes in a convolution kernel as a <span class="math inline"><strong>5</strong> <strong>×</strong> <strong>5</strong> <strong>m</strong><strong>a</strong><strong>t</strong><strong>r</strong><strong>i</strong><strong>x</strong></span></p></li>
</ul>
<p>the array is padded with zeros</p></th>
</tr>
<tr>
<th><p><strong>julia&gt; using DSP</strong></p>
<p><strong>julia&gt; A = zeros(5,5); A[3,2] = 1; A[5,5] = 1;</strong></p>
<p><strong>julia&gt; A</strong></p>
<p><strong>5×5 Matrix{Float64}:</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 1.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 0.0 0.0</strong></p>
<p><strong>0.0 0.0 0.0 0.0 1.0</strong></p>
<p><strong>julia&gt; G = [1 2 3; 4 5 6; 7 8 9];</strong></p>
<p><strong>julia&gt; Out = conv(A,G)</strong></p>
<p><strong>7×7 Matrix{Float64}:</strong></p>
<p><strong>-4.45009e-16 0.0 1.45009e-15 8.70052e-16 0.0 0.0 2.90017e-16</strong></p>
<p><strong>4.6693e-16 7.25044e-16 5.80035e-16 5.07531e-16 -5.80035e-16 -5.80035e-16 0.0</strong></p>
<p><strong>7.43918e-17 1.0 2.0 3.0 -5.80035e-16 5.80035e-16 5.80035e-16</strong></p>
<p><strong>-4.6693e-16 4.0 5.0 6.0 -7.25044e-17 7.25044e-16 5.80035e-16</strong></p>
<p><strong>-3.5316e-16 7.0 8.0 9.0 1.0 2.0 3.0</strong></p>
<p><strong>1.37898e-16 4.35026e-16 4.35026e-16 8.70052e-16 4.0 5.0 6.0</strong></p>
<p><strong>3.0532e-16 5.80035e-16 2.90017e-16 1.37758e-15 7.0 8.0 9.0</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">De-Convolution</td>
<td><ul>
<li><p>where things become very interesting is for deconvolving</p></li>
</ul>
<p><span class="math display"><strong>−</strong><strong>u</strong><sub><strong>i</strong><strong>,</strong> <strong>j</strong> <strong>−</strong> <strong>1</strong></sub><strong>−</strong><strong>u</strong><sub><strong>i</strong> <strong>−</strong> <strong>1</strong><strong>,</strong> <strong>j</strong></sub><strong>+</strong><strong>4</strong><strong>u</strong><sub><strong>i</strong><strong>,</strong> <strong>j</strong></sub><strong>−</strong><strong>u</strong><sub><strong>i</strong> <strong>+</strong> <strong>1</strong><strong>,</strong> <strong>j</strong></sub><strong>−</strong><strong>u</strong><sub><strong>i</strong><strong>,</strong> <strong>j</strong> <strong>+</strong> <strong>1</strong></sub> <strong>=</strong> <strong>−</strong><strong>h</strong><sup><strong>2</strong></sup><strong>f</strong><sub><strong>i</strong><strong>,</strong> <strong>j</strong></sub></span></p>
<ul>
<li><p>means: find <span class="math inline"><em>u</em></span> such that when you convolve it with the stencil you get the right-hand side</p></li>
</ul>
<p><span class="math display"><strong>Q</strong><strong>Λ</strong><strong>Q</strong><sup><strong>H</strong></sup><strong>u</strong> <strong>=</strong> <strong>b</strong></span></p>
<p><span class="math display"><strong>u</strong><strong>=</strong>(<strong>Q</strong><strong>Λ</strong><strong>Q</strong><sup><strong>H</strong></sup>)<sup><strong>−</strong><strong>1</strong></sup><strong>b</strong> <strong>=</strong> <strong>Q</strong><strong>Λ</strong><sup><strong>−</strong><strong>1</strong></sup><strong>Q</strong><sup><strong>H</strong></sup><strong>b</strong></span></p>
<ul>
<li><p>this needs a small tweak, since for this operator the matrix is not invertible</p></li>
</ul>
<p>one of the eigenvalues is 0</p>
<ul>
<li><p>that means that <span class="math inline"><strong>f</strong><strong>f</strong><strong>t</strong>(<strong>b</strong>)</span> must have a <span class="math inline"><strong>z</strong><strong>e</strong><strong>r</strong><strong>o</strong></span> in the corresponding term</p></li>
</ul>
<p>note that this solves the problem on a periodic domain</p></td>
</tr>
<tr>
<td><p><strong>julia&gt; L = fft(s)</strong></p>
<p><strong>julia&gt; Linv = 1.0 ./ L; Linv[1,1] = 0;</strong></p>
<p><strong>julia&gt; u = real(ifft( fft(b) .* Linv ));</strong></p></td>
</tr>
<tr>
<td colspan="2">Computing the SVD</td>
</tr>
<tr>
<td>SVD Factorization</td>
<td><ul>
<li><p><strong>limitations</strong> of eigen decomposition</p>
<ul>
<li><p>only <strong>valid</strong> for <strong>square</strong> matrices</p></li>
<li><p>for <strong>some</strong> matrices, we <strong>must</strong> use <strong>complex</strong> <strong>numbers</strong> to diagonalize</p></li>
</ul></li>
</ul>
<p><span class="math inline"><strong>Q</strong></span>: orthogonal, square</p>
<p><span class="math inline"><strong>Λ</strong></span><strong>:</strong> diagonal, real</p>
<ul>
<li><p><strong>SVD</strong> <strong>fixes</strong> all of that</p>
<ul>
<li><p>for a <strong>symmetric</strong> matrix</p></li>
</ul></li>
</ul>
<p><span class="math inline"><strong>U</strong><strong>,</strong> <strong>V</strong></span>: orthogonal; only square if <span class="math inline"><strong>A</strong></span> is square</p>
<p><span class="math inline"><strong>Σ</strong></span><strong>:</strong> diagonal, real, non-negative</p>
<p><span class="math display"><strong>A</strong> <strong>=</strong> <strong>Q</strong><strong>Λ</strong><strong>Q</strong><sup><strong>T</strong></sup></span></p>
<ul>
<li><p>for any <strong>matrix</strong></p></li>
</ul>
<p><span class="math inline"><strong>#</strong></span> of rows in <span class="math inline"><strong>A</strong></span> = <span class="math inline"><strong>#</strong></span> rows in <span class="math inline"><strong>U</strong></span></p>
<p><span class="math inline"><strong>#</strong></span> of cols in <span class="math inline"><strong>A</strong></span> = <span class="math inline"><strong>#</strong></span> cols in <span class="math inline"><strong>V</strong><sup><strong>T</strong></sup></span></p>
<p><span class="math display"><strong>A</strong> <strong>=</strong> <strong>U</strong><strong>Σ</strong><strong>V</strong><sup><strong>T</strong></sup></span></p></td>
</tr>
<tr>
<td>How to Compute</td>
<td><ul>
<li><p>take a <strong>tall</strong> matrix <span class="math inline"><strong>m</strong> <strong>≥</strong> <strong>n</strong></span></p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>∈</strong>ℝ<sup><strong>m</strong><strong>×</strong><strong>n</strong></sup></span></p>
<ul>
<li><p>start by <strong>diagonalizing</strong> the <span class="math inline"><strong>n</strong> <strong>×</strong> <strong>n</strong></span> symmetric <strong>matrix</strong></p></li>
</ul>
<p><span class="math display"><strong>A</strong><sup><strong>T</strong></sup><strong>A</strong> <strong>=</strong> <strong>V</strong><strong>Λ</strong><strong>V</strong><sup><strong>T</strong></sup></span></p>
<ul>
<li><p>the <strong>columns</strong> of <span class="math inline"><strong>V</strong></span> form an <strong>orthonormal</strong> <strong>basis</strong> for the <span class="math inline"><strong>n</strong> <strong>−</strong> <strong>d</strong><strong>i</strong><strong>m</strong><strong>e</strong><strong>n</strong><strong>s</strong><strong>i</strong><strong>o</strong><strong>n</strong><strong>a</strong><strong>l</strong></span> space</p></li>
<li><p>apply <span class="math inline"><strong>A</strong></span> to each <strong>vector</strong></p></li>
</ul>
<p><span class="math display">(<strong>A</strong><strong>v</strong><sub><strong>i</strong></sub>)<strong>⋅</strong>(<strong>A</strong><strong>v</strong><sub><strong>j</strong></sub>)<strong>=</strong>(<strong>A</strong><strong>v</strong><sub><strong>i</strong></sub>)<sup><strong>T</strong></sup><strong>A</strong><strong>v</strong><sub><strong>j</strong></sub><strong>=</strong><strong>v</strong><sub><strong>i</strong></sub><sup><strong>T</strong></sup><strong>A</strong><sup><strong>T</strong></sup><strong>A</strong><strong>v</strong><sub><strong>j</strong></sub><strong>=</strong><strong>v</strong><sub><strong>i</strong></sub><sup><strong>T</strong></sup>(<strong>λ</strong><sub><strong>j</strong></sub><strong>v</strong><sub><strong>j</strong></sub>)<strong>=</strong><strong>λ</strong><sub><strong>j</strong></sub>(<strong>v</strong><sub><strong>i</strong></sub><strong>⋅</strong><strong>v</strong><sub><strong>j</strong></sub>)</span></p>
<ul>
<li><p>if <span class="math inline"><strong>i</strong> <strong>=</strong> <strong>j</strong></span> it shows that the <strong>eigenvalue</strong> is <strong>non</strong>-<strong>negative</strong></p></li>
</ul>
<p><span class="math display"><strong>0</strong><strong>≤</strong>∥<strong>A</strong><strong>v</strong><sub><strong>i</strong></sub>∥<sup><strong>2</strong></sup><strong>=</strong><strong>λ</strong><sub><strong>j</strong></sub>∥<strong>v</strong><sub><strong>j</strong></sub>∥<sup><strong>2</strong></sup><strong>=</strong><strong>λ</strong><sub><strong>j</strong></sub></span></p>
<ul>
<li><p>the <strong>lengths</strong> of these <strong>vectors</strong> are called the <span class="math inline"><strong>s</strong><strong>i</strong><strong>n</strong><strong>g</strong><strong>u</strong><strong>l</strong><strong>a</strong><strong>r</strong> <strong>v</strong><strong>a</strong><strong>l</strong><strong>u</strong><strong>e</strong><strong>s</strong></span></p></li>
</ul>
<p><span class="math display">$$\mathbf{\sigma}_{\mathbf{i}}\mathbf{=}\left\| \mathbf{A}\mathbf{v}_{\mathbf{i}} \right\|\mathbf{=}\sqrt{\mathbf{\lambda}_{\mathbf{i}}}$$</span></p>
<ul>
<li><p><strong>sorting</strong> the values from <strong>largest</strong> to <strong>smallest</strong> meant that the tail could be <span class="math inline"><strong>0</strong></span></p></li>
<li><p>let’s say that the <strong>first</strong> <span class="math inline"><strong>r</strong> <strong>≤</strong> <strong>n</strong></span> are <span class="math inline"><strong>n</strong><strong>o</strong><strong>n</strong> <strong>−</strong> <strong>z</strong><strong>e</strong><strong>r</strong><strong>o</strong><strong>,</strong> </span>then <span class="math inline"><strong>n</strong> <strong>−</strong> <strong>r</strong>  <strong>z</strong><strong>e</strong><strong>r</strong><strong>o</strong><strong>s</strong></span></p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>V</strong> <strong>=</strong> <strong>A</strong>[<strong>v</strong><sup><strong>1</strong></sup><strong>v</strong><sup><strong>2</strong></sup><strong>…</strong><strong>v</strong><strong>ₙ</strong>]<strong>=</strong>[<strong>A</strong><strong>v</strong><sup><strong>1</strong></sup><strong>A</strong><strong>v</strong><sup><strong>2</strong></sup><strong>…</strong><strong>A</strong><strong>v</strong><strong>ᵣ</strong><strong>0</strong><strong>…</strong><strong>0</strong>]</span></p>
<ul>
<li><p>the <strong>first</strong> <span class="math inline"><strong>r</strong></span> vectors are <span class="math inline"><strong>n</strong><strong>o</strong><strong>n</strong> <strong>−</strong> <strong>z</strong><strong>e</strong><strong>r</strong><strong>o</strong></span>, and what we just showed is that they are <strong>orthogonal</strong></p></li>
</ul>
<p><span class="math display">(<strong>A</strong><strong>v</strong><strong>ᵢ</strong>)<strong>⋅</strong>(<strong>A</strong><strong>v</strong><strong></strong>)<strong>=</strong><strong>λ</strong><strong></strong>(<strong>v</strong><strong>ᵢ</strong><strong>⋅</strong><strong>v</strong><strong></strong>) <strong>=</strong> <strong>0</strong><strong>,</strong> <strong>i</strong><strong>≠</strong><strong>j</strong></span></p>
<ul>
<li><p>which means that the <strong>following</strong> <strong>vectors</strong> are <strong>orthonormal</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{u}\mathbf{ᵢ}\mathbf{=}\mathbf{Av}\mathbf{ᵢ}\textit{\textbf{/}}\left\| \mathbf{Av}\mathbf{ᵢ} \right\|\mathbf{= Av}\mathbf{ᵢ}\textit{\textbf{/}}\mathbf{\sigma}\mathbf{ᵢ}\mathbf{,i =}\mathbf{1,\ldots,r}$$</span></p>
<ul>
<li><p>we <strong>create</strong> <span class="math inline"><strong>n</strong> <strong>−</strong> <strong>r</strong></span> more <strong>vectors</strong> that are all <strong>orthonormal</strong></p></li>
<li><p>we could even <strong>create</strong> <span class="math inline"><strong>m</strong> <strong>−</strong> <strong>r</strong></span> more (<span class="math inline"><strong>m</strong> <strong>≥</strong> <strong>n</strong></span>)</p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>v</strong><strong>ᵢ</strong> <strong>=</strong> <strong>σ</strong><strong>ᵢ</strong> <strong>u</strong><strong>ᵢ</strong></span></p>
<p>but these have no numerical use</p>
<p><span class="math display"><strong>A</strong><strong>V</strong> <strong>=</strong> <em>A</em>[<strong>v</strong><sup><strong>1</strong></sup><strong>v</strong><sup><strong>2</strong></sup><strong>…</strong><strong>v</strong><strong>ₙ</strong>]<strong>=</strong>[<strong>σ</strong><sup><strong>1</strong></sup><strong>u</strong><sup><strong>1</strong></sup><strong>σ</strong><sup><strong>2</strong></sup><strong>u</strong><sup><strong>2</strong></sup><strong>…</strong><strong>σ</strong><strong>ₙ</strong><strong>u</strong><strong>ₙ</strong>]<strong>=</strong>[<strong>u</strong><sup><strong>1</strong></sup><strong>u</strong><sup><strong>2</strong></sup><strong>…</strong><strong>u</strong><strong>ₙ</strong>]<strong>Σ</strong> <strong>=</strong> <strong>U</strong><strong>Σ</strong></span></p>
<ul>
<li><p><span class="math inline"><strong>V</strong></span> is <strong>invertible</strong> and <strong>orthogonal</strong> so,</p></li>
</ul>
<p><span class="math display"><strong>A</strong> <strong>=</strong> <strong>U</strong><strong>Σ</strong><strong>V</strong><strong>ᵀ</strong></span></p></td>
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
<th rowspan="2">Preferred Method (Julia)</th>
<th><ul>
<li><p>start with a <span class="math inline"><strong>4</strong> <strong>×</strong> <strong>3</strong></span> matrix <span class="math inline"><strong>A</strong></span></p></li>
</ul>
<p>1</p>
<ul>
<li><p>dedicated SVD routines do a faster and more accurate job</p></li>
<li><p>Julia computes the thin form, so <span class="math inline"><strong>U</strong></span> is <span class="math inline"><strong>4</strong> <strong>×</strong> <strong>3</strong></span></p></li>
<li><p>the singular values are not moved to <span class="math inline"><strong>0</strong></span></p></li>
</ul>
<p>2</p>
<p>clearly more accurate than the previous method</p>
<ul>
<li><p>the <span class="math inline"><strong>V</strong></span> matrix is stored in terms of the transpose, not <span class="math inline"><strong>V</strong></span></p></li>
</ul>
<p>3</p></th>
</tr>
<tr>
<th><p><strong>julia&gt; A</strong></p>
<p><strong>4×3 Matrix{Float64}:</strong></p>
<p><strong>2.64434 2.77354 0.87934</strong></p>
<p><strong>-0.114416 0.854368 0.645425</strong></p>
<p><strong>-0.763388 4.9565 1.01532</strong></p>
<p><strong>-0.0203128 -2.02325 -1.04917</strong></p>
<p><strong>julia&gt; f = svd(A)</strong></p>
<p><strong>SVD{Float64, Float64, Matrix{Float64}, Vector{Float64}}</strong></p>
<p><strong>U factor:</strong></p>
<p><strong>4×3 Matrix{Float64}:</strong></p>
<p>1</p>
<p><strong>-0.459242 -0.152173 0.827237</strong></p>
<p><strong>0.153632 -0.553737 0.0936324</strong></p>
<p><strong>-0.806229 0.480617 -0.285158</strong></p>
<p><strong>-0.348253 0.662741 0.474971</strong></p>
<p><strong>singular values:</strong></p>
<p><strong>3-element Vector{Float64}:</strong></p>
<p>2</p>
<p><strong>6.35597336610859</strong></p>
<p><strong>0.8198324736388264</strong></p>
<p><strong>2.759682200799747e-16</strong></p>
<p><strong>Vt factor:</strong></p>
<p><strong>3×3 Matrix{Float64}:</strong></p>
<p>3</p>
<p><strong>0.111627 -0.957811 -0.264837</strong></p>
<p><strong>-0.49214 0.178244 -0.852072</strong></p>
<p><strong>-0.863329 0.225451 -0.45148</strong></p></th>
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
<th rowspan="2"><p>Special Case:</p>
<p>same matrices transposed</p>
<p><span class="math display"><strong>m</strong> <strong>&lt;</strong> <strong>n</strong></span></p></th>
<th><ul>
<li><p>for broad matrices (row &lt; column) the transpose is tall, so take the SVD of that and transpose it back</p></li>
</ul>
<p><span class="math display">$$\mathbf{A\hat{}T\  = \ U\ \Sigma\ V\hat{}T}$$</span></p>
<p><span class="math display">$$\mathbf{A\  = \ V\ \Sigma\ U\hat{}T}$$</span></p></th>
</tr>
<tr>
<th><p><strong>julia&gt; f = svd(A)</strong></p>
<p><strong>SVD{Float64, Float64, Matrix{Float64}, Vector{Float64}}</strong></p>
<p><strong>U factor:</strong></p>
<p><strong>4×3 Matrix{Float64}:</strong></p>
<p><strong>-0.459242 -0.152173 0.827237</strong></p>
<p><strong>0.153632 -0.553737 0.0936324</strong></p>
<p><strong>-0.806229 0.480617 -0.285158</strong></p>
<p><strong>-0.348253 0.662741 0.474971</strong></p>
<p><strong>singular values:</strong></p>
<p><strong>3-element Vector{Float64}:</strong></p>
<p><strong>6.35597336610859</strong></p>
<p><strong>0.8198324736388264</strong></p>
<p><strong>2.759682200799747e-16</strong></p>
<p><strong>Vt factor:</strong></p>
<p>same matrices transposed</p>
<p><strong>3×3 Matrix{Float64}:</strong></p>
<p><strong>0.111627 -0.957811 -0.264837</strong></p>
<p><strong>-0.49214 0.178244 -0.852072</strong></p>
<p><strong>-0.863329 0.225451 -0.45148</strong></p>
<p><strong>julia&gt; ft = svd(A')</strong></p>
<p><strong>SVD{Float64, Float64, Adjoint{Float64, Matrix{Float64}}, Vector{Float64}}</strong></p>
<p><strong>U factor:</strong></p>
<p><strong>3×3 adjoint(::Matrix{Float64}) with eltype Float64:</strong></p>
<p><strong>0.111627 -0.49214 0.863329</strong></p>
<p><strong>-0.957811 0.178244 0.225451</strong></p>
<p><strong>-0.264837 -0.852072 -0.45148</strong></p>
<p><strong>singular values:</strong></p>
<p><strong>3-element Vector{Float64}:</strong></p>
<p><strong>6.35597336610859</strong></p>
<p>adjoint means conjugate transposed</p>
<p><strong>0.8198324736388264</strong></p>
<p><strong>2.759682200799747e-16</strong></p>
<p><strong>Vt factor:</strong></p>
<p><strong>3×4 adjoint(::Matrix{Float64}) with eltype Float64:</strong></p>
<p><strong>-0.459242 0.153632 -0.806229 0.348253</strong></p>
<p><strong>-0.152173 -0.553737 0.480617 0.662741</strong></p>
<p><strong>0.827237 0.0936324 -0.285158 0.47497</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
