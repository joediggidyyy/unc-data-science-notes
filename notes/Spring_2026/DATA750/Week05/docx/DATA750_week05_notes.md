---
generated_at_utc: 2026-02-11T05:13:42+00:00
generated_from: notes/Spring_2026/DATA750/Week05/docx/DATA750_week05_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
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
<p><span class="math display"><em>v</em><sup><em>k</em><sub>1</sub>, <em>k</em><sub>2</sub></sup> ∈ <em>R</em><sup><em>N</em><sub>𝟙</sub> × <em>N</em><sub>𝟚</sub></sup></span></p>
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
<p>ChatGPT 5.2</p></td>
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
</tbody>
</table>
