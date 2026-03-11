> Markdown version for convenient browsing. Original files:
> - PDF: [DATA750_week04_notes.pdf](../DATA750_week04_notes.pdf)
> - DOCX: [DATA750_week04_notes.docx](DATA750_week04_notes.docx)

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
<th colspan="2">Week 4: Fourier Transform</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td colspan="2" style="text-align: right;"><em>Class meeting: 03 Feb 2026</em></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>complex numbers</p>
<ol type="1">
<li><p>standard form</p></li>
<li><p>polar form</p></li>
<li><p>view as rotation and scale matrices</p></li>
</ol></li>
<li><p>Discrete Fourier Transform (DFT)</p></li>
<li><p>Fourier Series</p></li>
<li><p>use numerical libraries to compute DFT/frequency information encoding</p></li>
<li><p>view DFT as product of an orthogonal matrix</p></li>
<li><p>use DFT to analyze a signal where the frequency varies in time</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5">Fourier Transform</td>
</tr>
<tr>
<td>Complex Numbers (CNs)</td>
<td colspan="4"><ul>
<li><p><strong>complex</strong> <strong>numbers</strong> (C) enable capturing roots of certain polynomials</p>
<ul>
<li><p><span class="math inline">0 = <em>x</em><sup>2</sup> + 1 </span></p></li>
<li><p><span class="math inline">0 = <em>x</em><sup>2</sup> + 2<em>x</em> + 2 = (<em>x</em> + 1)<sup>2</sup> + 1</span></p></li>
</ul></li>
<li><p><strong>Add</strong> an <strong>imaginary</strong> number <span class="math inline"><strong>i</strong></span> with <span class="math inline">$i\hat{}2 = - 1$</span></p>
<ul>
<li><p><span class="math inline">0 = <em>x</em><sup>2</sup> + 1 =  &gt; <em>x</em> = ±<em>i</em></span></p></li>
<li><p><span class="math inline">0 = <em>x</em><sup>2</sup> + 2<em>x</em> + 2  =  &gt; (<em>x</em> + 1)<sup>2</sup> + 1 = 0 =  &gt; <em>x</em> = −1± <em>i</em></span></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>CNs as Matrix</td>
<td colspan="4"><ul>
<li><p><span class="math inline">$1 &lt; \rightarrow \ \ \begin{bmatrix}
1 &amp; 0 \\
0 &amp; 1
\end{bmatrix}$</span></p></li>
<li><p><span class="math inline">$i &lt; \rightarrow \ \begin{bmatrix}
0 &amp; - 1 \\
1 &amp; 0
\end{bmatrix},\ i^{2} = \  - 1$</span> , counterclockwise <span class="math inline"><strong>90</strong><sup><strong>0</strong></sup></span> <strong>rotation</strong></p></li>
</ul></td>
</tr>
<tr>
<td>CNs Standard Format</td>
<td colspan="4"><ul>
<li><p><span class="math inline"><em>z</em> = <em>a</em> + <em>b</em><em>i</em>, <em>w</em><em>h</em><em>e</em><em>r</em><em>e</em> <em>a</em> <em>i</em><em>s</em> <em>t</em><em>h</em><em>e</em> <em>r</em><em>e</em><em>a</em><em>l</em> <em>p</em><em>a</em><em>r</em><em>t</em> <em>a</em><em>n</em><em>d</em> <em>i</em><em>b</em> <em>i</em><em>s</em> <em>t</em><em>h</em><em>e</em> <em>i</em><em>m</em><em>a</em><em>g</em><em>i</em><em>n</em><em>a</em><em>r</em><em>y</em> <em>p</em><em>a</em><em>r</em><em>t</em></span></p></li>
<li><p><span class="math inline">$a\  + \ ib\  = \ a\begin{bmatrix}
1 &amp; 0 \\
0 &amp; 1
\end{bmatrix} + b\begin{bmatrix}
0 &amp; - 1 \\
1 &amp; 0
\end{bmatrix} = \ \begin{bmatrix}
a &amp; - b \\
b &amp; a
\end{bmatrix}$</span></p></li>
</ul></td>
</tr>
<tr>
<td>CNs Polar Format</td>
<td colspan="4"><ul>
<li><p><span class="math inline">$r\  = \ |z|\  = \ \sqrt{a^{2} + b^{2}}$</span></p></li>
<li><p><span class="math inline"><em>a</em> + <em>i</em><em>b</em> = <em>r</em>cos <em>θ</em> + <em>i</em>sin <em>θ</em></span></p></li>
<li><p><span class="math inline">$a + ib = r\begin{bmatrix}
\cos\theta &amp; - \sin\theta \\
\sin\theta &amp; \cos\theta
\end{bmatrix}$</span></p></li>
</ul>
<p><span class="math display"><strong>z</strong> <strong>=</strong> <strong>a</strong> <strong>+</strong> <strong>i</strong><strong>b</strong></span></p>
<p>r</p>
<p><span class="math display"><em>θ</em></span></p></td>
</tr>
<tr>
<td>CN Multiplication</td>
<td colspan="4"><ul>
<li><p><span class="math inline"><strong>1</strong> <em>a</em><em>n</em><em>d</em> <strong>i</strong></span> <strong>commute</strong> so general <strong>multiplications</strong> work <strong>as</strong> <strong>expected</strong></p>
<ul>
<li><p><span class="math inline">$\mathbf{(a + ib)(c + id) = ac + ibc + iad + i\hat{}2\ bd}$</span></p></li>
</ul></li>
</ul>
<blockquote>
<p><span class="math display"> <strong>=</strong> <strong>a</strong><strong>c</strong> <strong>−</strong> <strong>b</strong><strong>d</strong> <strong>+</strong> <strong>i</strong><strong>(</strong><strong>b</strong><strong>c</strong> <strong>+</strong> <strong>a</strong><strong>d</strong><strong>)</strong></span></p>
</blockquote>
<ul>
<li><p><span class="math inline">$\left( \mathbf{a + ib} \right)\left( \mathbf{c + id} \right)\mathbf{\rightarrow}\begin{bmatrix}
\mathbf{a} &amp; \mathbf{- b} \\
\mathbf{b} &amp; \mathbf{a}
\end{bmatrix}\begin{bmatrix}
\mathbf{c} &amp; \mathbf{- d} \\
\mathbf{d} &amp; \mathbf{c}
\end{bmatrix}\mathbf{= \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }\begin{bmatrix}
\mathbf{ac - bd} &amp; \mathbf{- ad - bc} \\
\mathbf{ad + bc} &amp; \mathbf{ac - bd}
\end{bmatrix}$</span></p></li>
</ul>
<ul>
<li><p><strong>exponential</strong> form</p></li>
</ul>
<p>direction</p>
<p>magnitude</p>
<p><span class="math display"><em>r</em>  <em>e</em><sup><em>i</em><em>θ</em></sup></span></p>
<p>polar</p>
<p>form</p>
<ul>
<li><p><span class="math inline"><strong>e</strong><sup><strong>i</strong><strong>θ</strong></sup> <strong>=</strong> <strong>c</strong><strong>o</strong><strong>s</strong><strong>θ</strong> <strong>+</strong> <strong>i</strong> <strong>s</strong><strong>i</strong><strong>n</strong><strong>θ</strong></span></p></li>
<li><p><span class="math inline"><strong>e</strong><sup><strong>i</strong><strong>α</strong> <strong>+</strong> <strong>i</strong><strong>β</strong></sup><strong>=</strong><strong>e</strong><sup><strong>i</strong><strong>α</strong></sup><strong>e</strong><sup><strong>i</strong><strong>β</strong></sup></span></p></li>
<li><p><span class="math inline"><strong>z</strong> <strong>=</strong> <strong>a</strong> <strong>+</strong> <strong>i</strong><strong>b</strong> <strong>=</strong> <strong>r</strong> <strong>e</strong><sup><strong>i</strong><strong>θ</strong></sup></span></p></li>
</ul></td>
</tr>
<tr>
<td>Complex Conjugate</td>
<td colspan="4"><ul>
<li><p>a <strong>complex</strong> <strong>conjugate</strong> (<strong>CC</strong>) is formed by <strong>reversing</strong> the <strong>sign</strong> of the <strong>imaginary</strong> part of a complex <strong>number</strong></p></li>
<li><p><span class="math inline">$\overline{x + iy} = x - iy$</span> <strong>mirroring</strong> along the <strong>x-axis</strong> (<em>complex conjugate</em>)</p></li>
<li><p><span class="math inline">$\overline{z}z = (x + iy)(x - iy) = x^{2} + y^{2} = |z|^{2}$</span> CN*CC = <img src="generated_media\DATA750_week04_notes\media\image1.gif" /><span class="math inline"><strong>R</strong></span> <span class="math inline">(<strong>m</strong><strong>a</strong><strong>g</strong><strong>n</strong><strong>i</strong><strong>t</strong><strong>u</strong><strong>d</strong><strong>e</strong>)<sup><strong>2</strong></sup></span></p></li>
</ul>
<p>CC: https://www.khanacademy.org/math/</p></td>
</tr>
<tr>
<td>Real and Imaginary Parts</td>
<td colspan="4"><ul>
<li><p><span class="math inline">$re(z) = \frac{z + \ \overline{}z\ }{2}$</span> <span class="math inline">$im(z) = \frac{z + \overline{z}\ }{2i} = - i\frac{z + \ \overline{}z\ }{2}$</span></p></li>
</ul></td>
</tr>
<tr>
<td>Hermitian Matrix</td>
<td colspan="4"><ul>
<li><p>A <strong>Hermitian</strong> matrix is a <strong>square</strong> <strong>complex</strong> <strong>matrix A</strong> equal to its own conjugate transpose and equates to the <strong>conjugate</strong> <strong>transpose</strong> of the <strong>matrix</strong> / <strong>vector</strong></p>
<ul>
<li><p><span class="math inline">$A* = A^{H} = \overline{{(A}^{T})}$</span> Hermitian: <a href="https://en.wikipedia.org/wiki/Hermitian_matrix">https://en.wikipedia.org/wiki/Hermitian_matrix</a></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Inner Product</td>
<td colspan="4"><ul>
<li><p><span class="math inline">$u \cdot v = u^{H}v = \sum_{i}^{}{\overline{{\ u}_{i}}\ v_{i}\ }$</span></p></li>
<li><p><span class="math inline">$u \cdot v = \overline{v \cdot u}$</span></p></li>
</ul></td>
</tr>
<tr>
<td>CN and Imaginary Numbers in Julia</td>
<td colspan="4"><p>julia&gt; <span class="math inline"><em>z</em>1 = 2 + 3<strong>i</strong><strong>m</strong></span></p>
<p><span class="math display">‘<strong>i</strong><strong>m</strong>’ <strong>d</strong><strong>e</strong><strong>c</strong><strong>l</strong><strong>a</strong><strong>r</strong><strong>e</strong><strong>s</strong> <em>t</em><em>h</em><em>e</em> <strong>i</strong><strong>m</strong><strong>a</strong><strong>g</strong><strong>i</strong><strong>n</strong><strong>a</strong><strong>r</strong><strong>y</strong> </span></p>
<p><span class="math display"><em>p</em><em>a</em><em>r</em><em>t</em> <em>o</em><em>f</em> <em>t</em><em>h</em><em>e</em> <em>C</em><em>N</em></span></p>
<p><span class="math display"><strong>2</strong> <strong>+</strong> <strong>3</strong><strong>i</strong><strong>m</strong></span></p>
<p>julia&gt; <em>z2 = 1 - 1im</em></p>
<p><em><strong>1 - 1im</strong></em></p>
<p>julia&gt; <em>norm(z1)</em></p>
<p><span class="math display"><strong>g</strong><strong>e</strong><strong>t</strong> <strong>m</strong><strong>o</strong><strong>d</strong><strong>u</strong><strong>l</strong><strong>u</strong><strong>s</strong></span></p>
<p><em><strong>3.605551275463989</strong></em></p>
<p>julia&gt; <em>norm(z2)</em></p>
<p><em><strong>1.4142135623730951</strong></em></p>
<p><span class="math display"><strong>C</strong><strong>N</strong> <strong>m</strong><strong>u</strong><strong>l</strong><strong>t</strong><strong>i</strong><strong>p</strong><strong>l</strong><strong>i</strong><strong>c</strong><strong>a</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong></span></p>
<p>julia&gt; <em>z1*z2</em></p>
<p><em><strong>5 + 1im</strong></em></p>
<p>julia&gt; z1/z2</p>
<p><em><strong>-0.5 + 2.5im</strong></em></p>
<p><em>you get it…</em></p>
<p>julia&gt; <em>exp(1 +</em> <span class="math inline"><em>i</em><em>m</em></span><em>)</em></p>
<p><em><strong>1.4686939399158851 + 2.2873552871788423im</strong></em></p>
<p>julia&gt; <em>exp(1)*cos(1)</em></p>
<p><em><strong>1.4686939399158851</strong></em></p>
<p><em>conversion → complex</em></p>
<p>julia&gt; <em>sqrt(complex(-1))</em></p>
<p><em><strong>0.0 + 1.0im</strong></em></p>
<p>julia&gt; z = 3 + 2im</p>
<p><em><strong>3 + 2im</strong></em></p>
<p>julia&gt; <em>sqrt(z)</em></p>
<p><em><strong>1.8173540210239707 + 0.5502505227003375im</strong></em></p>
<p>julia&gt; <em>conj(z)</em></p>
<p><em><strong>3 - 2im</strong></em></p>
<p>julia&gt; <em>real(z)</em> julia&gt; <em>imag(z)</em></p>
<p><em><strong>3</strong> <strong>2</strong></em></p>
<p>julia&gt; angle(z)</p>
<p><em><strong>0.5880026035475675</strong></em></p></td>
</tr>
<tr>
<td>Fourier Transform</td>
<td colspan="4"><ul>
<li><p>A <strong>Fourier</strong> transform (FT) is a mathemetical technique that <strong>transforms</strong> a function of <strong>time</strong> <span class="math inline"><strong>x</strong><strong>(</strong><strong>t</strong><strong>)</strong></span>, to a fuciton of <strong>frequency</strong> <span class="math inline"><strong>X</strong><strong>(</strong><strong>ω</strong><strong>)</strong></span></p></li>
<li><p><strong>Three</strong> forms</p>
<ul>
<li><p>Fourier <strong>transform</strong></p></li>
<li><p>Fourier <strong>series</strong></p></li>
</ul></li>
</ul>
<p><span class="math display">$$``Fourier\ Transform"\ $$</span></p>
<p><span class="math display"><em>c</em><em>o</em><em>l</em><em>l</em><em>o</em><em>q</em><em>u</em><em>i</em><em>a</em><em>l</em><em>l</em><em>y</em> <em>a</em><em>n</em><em>d</em> <em>i</em><em>n</em></span></p>
<p><span class="math display"><em>t</em><em>h</em><em>i</em><em>s</em> <em>c</em><em>l</em><em>a</em><em>s</em><em>s</em></span></p>
<ul>
<li><p><strong>discrete</strong> Fourier transform (<strong>DFT</strong>)</p></li>
</ul>
<ul>
<li><p><strong>Fourier</strong> transform ↔ <strong>inverse</strong> transform</p>
<ul>
<li><p><strong>FTs</strong> are <strong>invertible</strong> using <strong>inverse</strong> of FT <strong>matrix</strong> <span class="math inline"><strong>F</strong><sup><strong>−</strong><strong>1</strong></sup></span></p></li>
</ul></li>
<li><p>For analytical functions on <span class="math inline"><strong>R</strong></span></p>
<ul>
<li><p><span class="math inline"><strong>F</strong>(<strong>ω</strong>)<strong>=</strong> ∫<sub><strong>−</strong><strong>∞</strong></sub><sup><strong>∞</strong></sup><strong>f</strong>(<strong>t</strong>)<strong>e</strong><sup><strong>−</strong><strong>i</strong><strong>ω</strong><strong>t</strong></sup><strong>d</strong><strong>t</strong></span></p></li>
<li><p><span class="math inline">$\mathbf{f}\left( \mathbf{t} \right)\mathbf{= \ }\frac{\mathbf{1}}{\mathbf{2}\mathbf{\pi}}\int_{\mathbf{- \infty}}^{\mathbf{\infty}}{\mathbf{F}\left( \mathbf{\omega} \right)\mathbf{e}^{\mathbf{- i\omega t}}}\mathbf{d\omega}$</span></p></li>
<li><p><strong>Euler’s</strong> formula: <span class="math inline"><strong>e</strong><sup><strong>i</strong><strong>ω</strong><strong>t</strong></sup><strong>=</strong><strong>cos</strong> (<strong>ω</strong><strong>t</strong>)<strong>+</strong> <strong>i</strong><strong>sin</strong> (<strong>ω</strong><strong>t</strong>)</span></p>
<ul>
<li><p>where <strong></strong> is the <strong>base</strong> of the <strong>natural</strong> <strong>log</strong>arithm, <strong></strong> is the imaginary unit <strong>(</strong><span class="math inline"><strong>i</strong><sup><strong>2</strong></sup> <strong>=</strong> <strong>−</strong><strong>1</strong></span><strong>),</strong> and <strong></strong> is the <strong>angle</strong> in <strong>radians</strong></p></li>
<li><p><strong>bridges</strong> complex <strong>analysis</strong> and trigonometry by relating the <strong>exponential</strong> function to <strong>sine</strong> and <strong>cosine</strong></p></li>
</ul></li>
</ul></li>
</ul>
<p>Fourier Transform: <a href="https://lpsa.swarthmore.edu/Fourier/Xforms/FXformIntro.html">https://lpsa.swarthmore.edu/Fourier/Xforms/FXformIntro.html</a></p>
<p>Euler’s Formula: https://www.youtube.com/watch?v=CRj-sbi2i2I</p></td>
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
<th>Fourier Series</th>
<th><ul>
<li><p>for anlytical functions that are periodic</p></li>
<li><p>a series expansion of a periodic function into a sum of trigonometric functions</p>
<ul>
<li><p><span class="math inline">$\mathbf{c}_{\mathbf{n}}\mathbf{=}\frac{\mathbf{1}}{\mathbf{L}}\int_{\mathbf{0}}^{\mathbf{L}}{\mathbf{f}\left( \mathbf{x} \right)}\mathbf{e}^{\frac{\mathbf{i\ 2}\mathbf{\pi n\ x}}{\mathbf{L}}\textit{\textbf{,}}}\mathbf{dx}$</span></p></li>
<li><p><span class="math inline">$\mathbf{f}\left( \mathbf{x} \right)\mathbf{= \ }\sum_{\mathbf{- \infty}}^{\mathbf{\infty}}{\mathbf{c}_{\mathbf{n}}\mathbf{e}^{\frac{\mathbf{i\ 2}\mathbf{\pi n\ x}}{\mathbf{L}}}}$</span></p></li>
</ul></li>
<li><p>we will not be using this in this class</p></li>
</ul>
<p>FS: https://en.wikipedia.org/wiki/Fourier_series</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Discrete Fourier Transform</td>
<td><ul>
<li><p>a <strong>fundamental</strong> mathematical <strong>technique</strong> in <strong>digital</strong> signal <strong>processing</strong> that <strong>converts</strong> a <strong>finite</strong> sequence of evenly spaced data <strong>samples</strong>, typically representing a <strong>signal</strong> in the <strong>time</strong> or <strong>spatial</strong> domain, into its corresponding <strong>frequency</strong> domain <strong>representation</strong>. It computes the <strong>amplitude</strong> and <strong>phase</strong> of different <strong>frequencies</strong> present in the signal, enabling <strong>analysis</strong> and <strong>manipulation</strong> of, for instance, audio or image data.</p></li>
</ul>
<p><span class="math display">$$\mathbf{c}_{\mathbf{k}}\mathbf{= \ }\frac{\mathbf{1}}{\mathbf{N}}\sum_{\mathbf{n = 0}}^{\mathbf{N - 1}}{\mathbf{x}_{\mathbf{n}}\mathbf{exp( - i}\frac{\mathbf{2}\mathbf{\pi i\ k\ n}}{\mathbf{N}}}\mathbf{)}$$</span></p>
<p><span class="math display">$$\mathbf{z}_{\mathbf{n}}\mathbf{=}\sum_{\mathbf{k = 0}}^{\mathbf{N - 1}}{\mathbf{c}_{\mathbf{k}}\mathbf{\exp}\left( \mathbf{- i}\frac{\mathbf{2}\mathbf{\pi i\ k\ n}}{\mathbf{N}} \right)}$$</span></p>
<p>DFT: https://en.wikipedia.org/wiki/Discrete_Fourier_transform</p></td>
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
<th>sin Transform</th>
<th><ul>
<li><p>a less complicated approach is to take back to a simpler transform, the <span class="math inline"><strong>sin</strong> </span> transform is related to the DFT</p></li>
</ul>
<p><span class="math display">$$\mathbf{v}_{\mathbf{k}}^{\mathbf{i}}\mathbf{= sin}\left. \ \left( \mathbf{\pi k}\frac{\mathbf{i}}{\mathbf{n}} \right.\  \right)\mathbf{,\ k = 1,\ldots,n - 1,\ \ i = 1,\ldots,\ n - 1}$$</span></p>
<blockquote>
<p><span class="math inline"><strong>n</strong> <strong>−</strong> <strong>1</strong></span> vectors, each with <span class="math inline"><strong>n</strong> <strong>−</strong> <strong>1</strong></span> values</p>
</blockquote>
<ul>
<li><p>all of those vectors are orthogonal to eachother</p></li>
</ul>
<p><span class="math display"><strong>v</strong><sub><strong>i</strong></sub><strong>⋅</strong><strong>v</strong><sub><strong>j</strong></sub> <strong>=</strong> <strong>0</strong><strong>,</strong> <strong>i</strong><strong>f</strong> <strong>k</strong> <strong>≠</strong> <strong>j</strong></span></p>
<p><span class="math display">$$\mathbf{v}_{\mathbf{i}}\mathbf{\cdot}\mathbf{v}_{\mathbf{j}}\mathbf{=}\sum_{\mathbf{i = 1}}^{\mathbf{n - 1}}{\mathbf{\sin}\left. \ \left( \mathbf{\pi k}\frac{\mathbf{i}}{\mathbf{n}} \right.\  \right)}\mathbf{\sin}\left. \ \left( \mathbf{\pi k}\frac{\mathbf{j}}{\mathbf{n}} \right.\  \right)\mathbf{= 0}$$</span></p>
<ul>
<li><p><span class="math inline"><strong>n</strong> <strong>−</strong> <strong>1</strong></span> orthogonal values with <span class="math inline"><strong>n</strong> <strong>−</strong> <strong>1</strong></span> entries, span all of <img src="generated_media\DATA750_week04_notes\media\image1.gif" /><span class="math inline">ℝ<sup><strong>n</strong> <strong>−</strong> <strong>1</strong></sup></span>, so they form am orthogonal basis</p></li>
</ul>
<ul>
<li><p>still, they are not quite orthonormal (orthogonal unit vectors)</p></li>
</ul>
<p>since, <span class="math inline">$\left| \mathbf{|v}_{\mathbf{k}} \right|\left. \ \mathbf{} \right|^{\mathbf{2}}\mathbf{=}\mathbf{v}_{\mathbf{k}}\mathbf{\cdot \ }\mathbf{v}_{\mathbf{k}}\mathbf{=}{\sum_{\mathbf{i = 1}}^{\mathbf{n - 1}}{\mathbf{\sin}^{\mathbf{2}}\left( \mathbf{\pi k}\frac{\mathbf{i}}{\mathbf{n}} \right)}}^{\mathbf{2}}\mathbf{=}\frac{\mathbf{n}}{\mathbf{2}}$</span></p>
<ul>
<li><p>create a basis matrix</p></li>
</ul>
<p><strong>Decompose a Signal</strong></p>
<p><span class="math display"><em>r</em><em>e</em><em>m</em><em>i</em><em>n</em><em>d</em><em>e</em><em>r</em> :  <strong>V</strong><sup><strong>T</strong></sup><strong>=</strong> <strong>V</strong><sup><strong>−</strong><strong>1</strong></sup>, <em>i</em><em>f</em> <strong>V</strong></span></p>
<p><span class="math display"><em>i</em><em>s</em> <em>a</em><em>n</em> <strong>o</strong><strong>r</strong><strong>t</strong><strong>h</strong><strong>o</strong><strong>g</strong><strong>o</strong><strong>n</strong><strong>a</strong><strong>l</strong> <strong>m</strong><strong>a</strong><strong>t</strong><strong>r</strong><strong>i</strong><strong>x</strong></span></p>
<ul>
<li><p><span class="math inline"><strong>V</strong> <strong>=</strong> [<strong>v</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>v</strong><sub><strong>2</strong></sub><strong>,</strong> <strong>⋯</strong><strong>,</strong><strong>v</strong><sub><strong>n</strong> <strong>−</strong> <strong>1</strong></sub>]</span></p></li>
</ul>
<blockquote>
<p><span class="math inline">$\mathbf{V}^{\mathbf{T}}\mathbf{V =}\frac{\mathbf{n}}{\mathbf{2}}\mathbf{I\ \ \ }\mathbf{\rightarrow \ }\mathbf{\ \ V}^{\mathbf{- 1}}\mathbf{=}\frac{\mathbf{2}}{\mathbf{n}}\mathbf{V}^{\mathbf{T}}$</span></p>
</blockquote>
<ul>
<li><p>ex: for a <span class="math inline"><strong>b</strong><strong>a</strong><strong>s</strong><strong>i</strong><strong>s</strong> <strong>V</strong></span>, there is a <span class="math inline"><strong>c</strong><strong>o</strong><strong>o</strong><strong>r</strong><strong>d</strong><strong>i</strong><strong>n</strong><strong>a</strong><strong>t</strong><strong>e</strong> <strong>c</strong></span> such that there is a <span class="math inline"><strong>v</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong> <strong>x</strong></span> that <span class="math inline"><strong>s</strong><strong>p</strong><strong>a</strong><strong>n</strong><strong>s</strong> <strong>V</strong></span>, such that<span class="math inline"><strong>:</strong> <strong>x</strong> <strong>=</strong> <strong>V</strong><strong>c</strong></span></p></li>
<li><p>any vector with <span class="math inline"><strong>n</strong> <strong>−</strong> <strong>1</strong></span> entries can be spanned by the <span class="math inline"><strong>V</strong> <strong>v</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong><strong>s</strong></span></p></li>
</ul>
<p><span class="math display"><em>r</em><em>e</em><em>m</em><em>i</em><em>n</em><em>d</em><em>e</em><em>r</em>: <em>a</em> <strong>b</strong><strong>a</strong><strong>s</strong><strong>i</strong><strong>s</strong> <em>i</em><em>s</em> <em>a</em> <em>s</em><em>e</em><em>t</em> <em>o</em><em>f</em> <strong>v</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong><strong>s</strong> </span></p>
<p><span class="math display"><em>t</em><em>h</em><em>a</em><em>t</em> <em>a</em><em>c</em><em>t</em><em>s</em> <em>a</em> <strong>f</strong><strong>o</strong><strong>u</strong><strong>n</strong><strong>d</strong><strong>a</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong><strong>a</strong><strong>l</strong>, <strong>m</strong><strong>i</strong><strong>n</strong><strong>i</strong><strong>m</strong><strong>a</strong><strong>l</strong> </span></p>
<p><span class="math display"><strong>b</strong><strong>u</strong><strong>i</strong><strong>l</strong><strong>d</strong><strong>i</strong><strong>n</strong><strong>g</strong> <strong>b</strong><strong>l</strong><strong>o</strong><strong>c</strong><strong>k</strong> <em>f</em><em>o</em><em>r</em> <em>a</em> <strong>v</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong> <strong>s</strong><strong>p</strong><strong>a</strong><strong>c</strong><strong>e</strong></span></p>
<p><span class="math display">$$\mathbf{x = Vc}\mathbf{\Rightarrow}\mathbf{V}^{\mathbf{T}}\mathbf{x =}\mathbf{V}^{\mathbf{T}}\mathbf{Vc =}\frac{\mathbf{n}}{\mathbf{2}}\mathbf{c}\mathbf{\Rightarrow}\mathbf{c =}\frac{\mathbf{2}}{\mathbf{n}}\mathbf{V}^{\mathbf{T}}\mathbf{x}$$</span></p>
<p><span class="math display">$$\mathbf{c}_{\mathbf{k}}\mathbf{=}\frac{\mathbf{2}}{\mathbf{n}}\mathbf{v}_{\mathbf{k}}\mathbf{\cdot x,k = 1,\ldots,n - 1}$$</span></p>
<ul>
<li><p><em>putting this together</em>: start with a <span class="math inline"><strong>v</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong> <strong>x</strong></span></p></li>
</ul>
<blockquote>
<p><span class="math inline">$\mathbf{x = Vc =}\mathbf{c}_{\mathbf{1}}\mathbf{v}_{\mathbf{1}}\mathbf{+ \cdots +}\mathbf{c}_{\mathbf{n - 1}}\mathbf{v}_{\mathbf{n - 1}}\mathbf{\Rightarrow}\mathbf{\ x}_{\mathbf{i}}\mathbf{=}\sum_{\mathbf{k = 1}}^{\mathbf{n - 1}}{\mathbf{c}_{\mathbf{k}}\mathbf{\ sin(\pi k}\frac{\mathbf{i}}{\mathbf{n}}\mathbf{)}}$</span></p>
</blockquote>
<ul>
<li><p>where the <span class="math inline"><strong>c</strong> <strong>v</strong><strong>a</strong><strong>l</strong><strong>u</strong><strong>e</strong><strong>s</strong></span> come from the vector</p></li>
</ul>
<p><em>vector</em></p>
<p><em>corresponds to:</em> <span class="math inline">|<strong>v</strong><sub><strong>k</strong></sub> |<sub><strong>i</strong></sub></span></p>
<p><span class="math display">$$\mathbf{c =}\frac{\mathbf{2}}{\mathbf{n}}\mathbf{V}^{\mathbf{T}}\mathbf{x}\mathbf{\Rightarrow}\mathbf{c}_{\mathbf{k}}\mathbf{=}\frac{\mathbf{2}}{\mathbf{n}}\mathbf{v}_{\mathbf{k}}\mathbf{\cdot x}\mathbf{\Rightarrow}\mathbf{c}_{\mathbf{k}}\mathbf{=}\frac{\mathbf{2}}{\mathbf{n}}\sum_{\mathbf{i = 1}}^{\mathbf{n - 1}}\mathbf{x}_{\mathbf{i}}\mathbf{sin(\pi k}\frac{\mathbf{i}}{\mathbf{n}}\mathbf{)}$$</span></p>
<ul>
<li><p>compare to the DFT equation</p></li>
</ul>
<p><em>vector decomposition</em></p>
<blockquote>
<p><span class="math inline">$\mathbf{c}_{\mathbf{k}}\mathbf{=}\frac{\mathbf{1}}{\mathbf{N}}\sum_{\mathbf{n = 0}}^{\mathbf{N - 1}}{\mathbf{x}_{\mathbf{n}}\mathbf{\ }\mathbf{exp}\mathbf{( - i}\frac{\mathbf{2}\mathbf{\pi kn}}{\mathbf{N}}\mathbf{)}}$</span> <span class="math inline">$\mathbf{z}_{\mathbf{n}}\mathbf{=}\sum_{\mathbf{k = 0}}^{\mathbf{N - 1}}{\mathbf{c}_{\mathbf{k}}\mathbf{\ }\mathbf{exp}\mathbf{(i}\frac{\mathbf{2\pi kn}}{\mathbf{N}}\mathbf{)}}$</span></p>
</blockquote>
<ul>
<li><p>any vector can be decomposed like this:</p></li>
</ul>
<p><strong>1</strong></p>
<p><strong>0.4</strong></p>
<p><strong>0.3</strong></p>
<p><strong>0.1</strong></p>
<p><strong>0</strong></p>
<p><strong>.</strong></p>
<p><strong>.</strong></p>
<p><strong>.</strong></p>
<p><strong>0</strong></p>
<ul>
<li><p><span class="math inline"><strong>x</strong><strong>=</strong><strong>v</strong><sub><strong>1</strong></sub><strong>+</strong><strong>0.4</strong><strong>v</strong><sub><strong>2</strong></sub><strong>+</strong><strong>0.3</strong><strong>v</strong><sub><strong>3</strong></sub><strong>+</strong><strong>0.1</strong><strong>v</strong><sub><strong>4</strong></sub> <strong>=</strong> <strong>V</strong><strong>x</strong> <strong>=</strong> <strong>V</strong></span></p></li>
</ul>
<ul>
<li><p>the <span class="math inline"><strong>sin</strong> </span> transform of <span class="math inline"><strong>x</strong></span> is the coordinate with respect to the basis</p></li>
</ul>
<p>Orthonormal: https://www.kristakingmath.com/blog/orthonormal-basis-for-a-vector-set</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Visualization</td>
<td><ul>
<li><p><img src="generated_media\DATA750_week04_notes\media\image3.png" style="width:3.33284in;height:4.56111in" /></p></li>
</ul>
<p><span class="math display"><strong>v</strong><sub><strong>1</strong></sub><strong>+</strong><strong>0.4</strong><strong>v</strong><sub><strong>2</strong></sub><strong>+</strong><strong>0.3</strong><strong>v</strong><sub><strong>3</strong></sub><strong>+</strong><strong>0.1</strong><strong>v</strong><sub><strong>4</strong></sub></span></p>
<p><strong>decomposed wave</strong></p>
<p><strong>composite waveform</strong></p>
<p><span class="math display"><strong>k</strong> <strong>=</strong> <strong>4</strong></span></p>
<p><span class="math display"><strong>k</strong> <strong>=</strong> <strong>2</strong></span></p>
<p><span class="math display"><strong>k</strong> <strong>=</strong> <strong>3</strong></span></p>
<p><span class="math display"><strong>k</strong> <strong>=</strong> <strong>4</strong></span></p></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
<tr>
<td colspan="2">DFT – Numerical View</td>
</tr>
<tr>
<td>Computing</td>
<td><ul>
<li><p>small variation in what numerical methods compute</p></li>
<li><p>fundamentally there is a standard matrix V</p></li>
</ul>
<p><span class="math display">$$V_{n,k} = \exp\left( i\frac{2\pi ikn}{N} \right)\ \ \ \ \ \ \ \ \ \ \ V^{- 1} = \frac{1}{N}V^{H}$$</span></p>
<ul>
<li><p>there is flexibility where you put that N factor numerically</p></li>
</ul>
<p>orthogonal (truly)</p>
<p>FFTW</p>
<p>easier to motivate</p>
<p><span class="math display">$$\mathbf{c =}\frac{\mathbf{1}}{\mathbf{N}}\mathbf{V}^{\mathbf{H}}\mathbf{x\ \ \ \ \ \ \ \ x\  = \ V\ c\ \ }$$</span></p>
<p><span class="math display">$$\mathbf{c =}\mathbf{V}^{\mathbf{H}}\mathbf{x\ \ \ \ \ \ \ \ \ \ \ \ \ x =}\frac{\mathbf{1}}{\mathbf{N}}\mathbf{Vc}$$</span></p>
<p><span class="math display">$$\mathbf{c =}\frac{\mathbf{1}}{\sqrt{\mathbf{N}}}\mathbf{V}^{\mathbf{H}}\mathbf{x\ \ \ \ x =}\frac{\mathbf{1}}{\sqrt{\mathbf{N}}}\mathbf{Vc}$$</span></p></td>
</tr>
<tr>
<td>Fast Fourier Transform (FFT) in Julia (ex 1)</td>
<td><p>julia&gt; using FFTW</p>
<p>julia&gt; x = Vector(range(start=0, step=0.1, length=10))</p>
<p>10-element Vector{Float64}:</p>
<p>0.0</p>
<p>0.1</p>
<p><span class="math display">$$x_{n} = \frac{n}{N}$$</span></p>
<p><span class="math display">$$y_{n} = sin\ (2\pi\frac{n}{N})$$</span></p>
<p>0.2</p>
<p>0.3</p>
<p>0.4</p>
<p>0.5</p>
<p>0.6</p>
<p>0.7</p>
<p>0.8</p>
<p>0.9</p>
<p>julia&gt; y = sin.(2pi*x)</p>
<p>10-element Vector{ComplexF64}:</p>
<p>1.2246467991473532e-16 + 0.0im</p>
<p>-5.50555994384384e-16 + 5.0im</p>
<p>1.2246467991473532e-16 - 2.1117696842213397e-16im</p>
<p>1.2246467991473532e-16 - 4.440892098500626e-16im</p>
<p>1.2246467991473532e-16 - 1.305145441260248e-16im</p>
<p>9.957992501029599e-17 + 0.0im</p>
<p>1.2246467991473532e-16 + 1.305145441260248e-16im</p>
<p>1.9440492184190732e-16 + 4.440892098500626e-16im</p>
<p>1.2246467991473532e-16 + 2.1117696842213397e-16im</p>
<p>-5.50555994384384e-16 + 5.0im</p></td>
</tr>
<tr>
<td>Fast Fourier Transform (FFT) in Julia (ex 2)</td>
<td><p>julia&gt; using FFTW</p>
<p>julia&gt; x = Vector(range(0, 1, 11))</p>
<p>11-element Vector{Float64}:</p>
<p>0.0</p>
<p>0.1</p>
<p>0.2</p>
<p>0.3</p>
<p>0.4</p>
<p>0.5</p>
<p>0.6</p>
<p>0.7</p>
<p>0.8</p>
<p>0.9</p>
<p>1.0</p>
<p>julia&gt; y = sin.(2pi*x)</p>
<p>julia&gt; fft(y)</p>
<p>11-element Vector{ComplexF64}:</p>
<p>-1.1102230246251565e-16 + 0.0im</p>
<p>4.447252663038674 + 4.928889952937341im</p>
<p>-0.4364947971936885 + 0.6791991628794149im</p>
<p>-0.35239245098458942 + 0.3057831273272211im</p>
<p>-0.3323496580110257 + 0.1517266249897483im</p>
<p>-0.3256303599998888 + 0.04681857752931811im</p>
<p>-0.3323496580110257 - 0.1517266249897483im</p>
<p>-0.35239245098458942 - 0.3057831273272211im</p>
<p>-0.4364947971936885 - 0.6791991628794149im</p>
<p>4.447252663038674 - 4.928889952937341im</p>
<p>-1.1102230246251565e-16 + 0.0im</p></td>
</tr>
<tr>
<td>Toeplitz Matrix</td>
<td>a <strong>structured</strong> <strong>diagonal</strong>-constant <strong>matrix</strong> where each <strong>descending</strong> <strong>diagonal</strong> from left to right <strong>contains</strong> the <strong>same</strong> <strong>elements</strong> defined <span class="math inline"><strong>T</strong><sub>(<strong>i</strong><strong>j</strong>)</sub><strong>=</strong><strong>t</strong><sub>(<strong>i</strong> <strong>−</strong> <strong>j</strong>)</sub></span>. these <strong>matrices</strong> are used in <strong>signal</strong> processing, <strong>image</strong> processing, and <strong>time</strong> <strong>series</strong> <strong>analysis</strong> for their <strong>efficiency</strong> in <strong>solving</strong> typically <strong>requiring</strong> only <span class="math inline"><strong>O</strong><strong>(</strong><strong>n</strong><strong>)</strong></span> distinct <strong>elements</strong> and <span class="math inline"><strong>O</strong>(<strong>n</strong><sup><strong>2</strong></sup>)</span>to <strong>solve</strong> <span class="math inline"><strong>A</strong><strong>x</strong> <strong>=</strong> <strong>y</strong></span><strong>.</strong></td>
</tr>
</tbody>
</table>
