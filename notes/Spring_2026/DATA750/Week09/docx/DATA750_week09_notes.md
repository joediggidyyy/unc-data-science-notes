---
generated_at_utc: 2026-03-08T23:56:05+00:00
generated_from: notes/Spring_2026/DATA750/Week09/docx/DATA750_week09_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA750_week09_notes.pdf](../DATA750_week09_notes.pdf)
> - DOCX: [DATA750_week09_notes.docx](DATA750_week09_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th colspan="4">Principal Components &amp; Intro to Non-Linear Solvers</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Overview</td>
<td colspan="3" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>approximate tensors using the principal components</p></li>
<li><p>create a k dimensional vectors using the first principal components to describe data</p></li>
<li><p>approximate a function using an n-th order Taylor series with remainder</p></li>
<li><p>Newtons method for scalar equations</p></li>
<li><p>the secant method</p></li>
<li><p>the convergence properties.</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Principal Components</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5">Principal Components</td>
</tr>
<tr>
<td>Motivating Example</td>
<td colspan="4"><ul>
<li><p>often when collapsing a <strong>higher</strong> <strong>dimensional</strong> vector space <strong>into</strong> a <strong>lower</strong> <strong>dimensional</strong> representation, <strong>structure</strong> inherent to the data <strong>is</strong> <strong>lost</strong> or unrecognizable</p></li>
</ul>
<p><img src="generated_media\DATA750_week09_notes\media\image1.png" style="width:3.62287in;height:1.86886in" /></p>
<p>ChatGPT 5.3 Instant 1</p></td>
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
<th>PCA vs Least Squares</th>
<th><ul>
<li><p>principal components</p>
<ul>
<li><p>unsupervised learning</p></li>
<li><p>finds directions (components) of maximum variance in predictors</p></li>
</ul></li>
<li><p>vertical least squares</p>
<ul>
<li><p>supervised learning</p></li>
<li><p>minimizes squared vertical distances to predict <span class="math inline"><strong>Y</strong> </span>from <span class="math inline"><strong>X</strong></span></p></li>
</ul></li>
<li><p>orthogonal least squares</p>
<ul>
<li><p>supervised learning</p></li>
<li><p>minimizes the sum of squared perpendicular distances</p></li>
</ul></li>
</ul>
<p>Gemini 3</p>
<p><img src="generated_media\DATA750_week09_notes\media\image2.png" style="width:1.96944in;height:1.31458in" /><img src="generated_media\DATA750_week09_notes\media\image3.png" style="width:1.97153in;height:1.29931in" /></p>
<p>least squares</p>
<p><img src="generated_media\DATA750_week09_notes\media\image4.png" style="width:2.06597in;height:1.19792in" /></p>
<p>principal components projection</p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Numerics</td>
<td><ul>
<li><p>take the <strong>SVD</strong> of the <strong>data</strong> set</p></li>
</ul>
<p>“<strong>best</strong>” in the sense of <strong>maximizing</strong> the <em>first</em> term</p>
<p><span class="math display"><strong>D</strong><strong>=</strong> <strong>σ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub><strong>v</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup> <strong>+</strong> <strong>σ</strong><sub><strong>2</strong></sub><strong>u</strong><sub><strong>2</strong></sub><strong>v</strong><sub><strong>2</strong></sub><sup><strong>T</strong></sup></span></p>
<ul>
<li><p>the <strong>best</strong> one rank <strong>approximation</strong> is the <strong>first</strong> <strong>term</strong></p></li>
</ul>
<p><span class="math display"><strong>∥</strong><strong>D</strong><strong>∥</strong><sub><strong>F</strong></sub><sup><strong>2</strong></sup>  <strong>=</strong>  <strong>∥</strong><strong>σ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub><strong>v</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>∥</strong><sub><strong>F</strong> </sub><sup><strong>2</strong></sup><strong>+</strong>  <strong>∥</strong><strong>σ</strong><sub><strong>2</strong></sub><strong>u</strong><sub><strong>2</strong></sub><strong>v</strong><sub><strong>2</strong></sub><sup><strong>T</strong></sup><strong>∥</strong><sub><strong>F</strong></sub><sup><strong>2</strong></sup></span></p>
<p>which means <strong>minimizing</strong> the <em>next</em> term</p></td>
</tr>
<tr>
<td><p><strong>julia&gt; D</strong></p>
<p><strong>20×2 Matrix{Float64}:</strong></p>
<p><strong>0.0632719 -1.659</strong></p>
<p><strong>0.505667 0.376497</strong></p>
<p><strong>1.55698 1.27546</strong></p>
<p><strong>⋮</strong></p>
<p><strong>1.12682 0.0639133</strong></p>
<p><strong>-0.156161 0.402374</strong></p>
<p><strong>julia&gt; fact = svd(D);</strong></p>
<p><strong>julia&gt; U = fact.U; Vt = fact.V; S = fact.S;</strong></p>
<p><strong>julia&gt; S[1]*U[:,1]*transpose(Vt[1,:])</strong></p>
<p><strong>20×2 Matrix{Float64}:</strong></p>
<p><strong>-0.797864 0.797864</strong></p>
<p><strong>0.441082 -0.441082</strong></p>
<p><strong>1.41622 -1.41622</strong></p>
<p><strong>⋮</strong></p>
<p><strong>0.595365 -0.595365</strong></p>
<p><strong>0.123107 -0.123107</strong></p>
<p><strong>julia&gt; S</strong></p>
<p><em>rank one approximation</em><strong>:</strong></p>
<p><span class="math inline"><strong>v</strong><sub><strong>1</strong></sub>→</span> principle <strong>direction</strong> in feature space</p>
<p><span class="math inline"><strong>u</strong><sub><strong>1</strong></sub><strong>σ</strong><sub><strong>1</strong></sub>→</span> <strong>coordinates</strong> of observations along the direction <span class="math inline"><strong>v</strong><sub><strong>1</strong></sub></span></p>
<p><strong>2-element Vector{Float64}:</strong></p>
<p><strong>5.609571973558723</strong></p>
<p><strong>2.8092564856735898</strong></p></td>
</tr>
<tr>
<td><img src="generated_media\DATA750_week09_notes\media\image5.png" style="width:1.19514in;height:2.02431in" />The First Term</td>
<td><ul>
<li><p>the <strong>first</strong> term in</p></li>
</ul>
<p><span class="math display"><strong>∥</strong><strong>D</strong><strong>∥</strong><sub><strong>F</strong></sub><sup><strong>2</strong></sup>  <strong>=</strong>  <strong>∥</strong><strong>σ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub><strong>v</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>∥</strong><sub><strong>F</strong> </sub><sup><strong>2</strong></sup><strong>+</strong>  <strong>∥</strong><strong>σ</strong><sub><strong>2</strong></sub><strong>u</strong><sub><strong>2</strong></sub><strong>v</strong><sub><strong>2</strong></sub><sup><strong>T</strong></sup><strong>∥</strong><sub><strong>F</strong></sub><sup><strong>2</strong></sup></span></p>
<ul>
<li><p><strong>Frobenius</strong> <strong>norm</strong> <strong>squared</strong> is the sum of the two norms of each row squared</p></li>
</ul>
<p><span class="math display">$$\left| |A| \right|_{\mathbf{F}}^{\mathbf{2}}\mathbf{=}\sum_{}^{}\left| \left| \mathbf{r}_{\mathbf{k}} \right| \right|^{\mathbf{2}}$$</span></p>
<p><img src="generated_media\DATA750_week09_notes\media\image6.png" style="width:2.05578in;height:1.76317in" /></p>
<p><span class="math display"><strong>σ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub><strong>v</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup></span></p>
<p><em>the residual</em>:</p>
<p><span class="math display"><strong>D</strong><strong>−</strong><strong>σ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub><strong>v</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup></span></p>
<p>represents the remaining orthogonal variance</p>
<p>ChatGPT 5.3 Instant</p></td>
</tr>
<tr>
<td>The Second Term</td>
<td><ul>
<li><p>the <strong>second</strong> <strong>term</strong></p></li>
</ul>
<p><span class="math display"><strong>σ</strong><sub><strong>2</strong> </sub><strong>u</strong><sub><strong>2</strong> </sub><strong>v</strong><sub><strong>2</strong></sub><sup><strong>T</strong></sup></span></p>
<ul>
<li><p>the <strong>remaining</strong> <strong>SVD</strong> <strong>terms</strong> represent the <strong>residual</strong> structure <strong>not</strong> <strong>captured</strong> by the <strong>first</strong> principal component</p></li>
</ul></td>
</tr>
<tr>
<td rowspan="2">The 3-D Case</td>
<td><ul>
<li><p>find the best <strong>rank</strong> <span class="math inline"><strong>1</strong></span> and <span class="math inline"><strong>2</strong></span></p></li>
</ul>
<p><span class="math display"><strong>D</strong><strong>=</strong><strong>σ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub><strong>v</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>+</strong><strong>σ</strong><sub><strong>2</strong></sub><strong>u</strong><sub><strong>2</strong></sub><strong>v</strong><sub><strong>2</strong></sub><sup><strong>T</strong></sup><strong>+</strong><strong>σ</strong><sub><strong>3</strong></sub><strong>u</strong><sub><strong>3</strong></sub><strong>v</strong><sub><strong>3</strong></sub><sup><strong>T</strong></sup></span></p>
<p><span class="math display"><strong>∥</strong><strong>D</strong><strong>∥</strong><sub><strong>F</strong></sub><sup><strong>2</strong>  </sup> <strong>=</strong>  <strong>∥</strong><strong>σ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub><strong>v</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>∥</strong><sub><strong>F</strong></sub><sup><strong>2</strong></sup> <strong>+</strong>  <strong>∥</strong><strong>σ</strong><sub><strong>2</strong></sub><strong>u</strong><sub><strong>2</strong></sub><strong>v</strong><sub><strong>2</strong></sub><sup><strong>T</strong></sup>  <strong>+</strong>  <strong>σ</strong><sub><strong>3</strong></sub><strong>u</strong><sub><strong>3</strong></sub><strong>v</strong><sub><strong>3</strong></sub><sup><strong>T</strong></sup><strong>∥</strong><sub><strong>F</strong></sub><sup><strong>2</strong></sup></span></p>
<p>best <strong>rank</strong> <strong>1</strong>matrix</p>
<p><strong><br />
</strong><span class="math display"><strong>∥</strong><strong>D</strong><strong>∥</strong><sub><strong>F</strong>   </sub><sup><strong>2</strong></sup><strong>=</strong>  <strong>∥</strong><strong>σ</strong><sub><strong>1</strong></sub><strong>u</strong><sub><strong>1</strong></sub><strong>v</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup>  <strong>+</strong><strong>σ</strong> <sub><strong>2</strong></sub><strong>u</strong><sub><strong>2</strong></sub><strong>v</strong><sub><strong>2</strong></sub><sup><strong>T</strong></sup><strong>∥</strong><sub><strong>F</strong></sub><sup><strong>2</strong></sup> <strong>+</strong>  <strong>∥</strong><strong>σ</strong><sub><strong>3</strong></sub><strong>u</strong><sub><strong>3</strong></sub><strong>v</strong><sub><strong>3</strong></sub><sup><strong>T</strong></sup><strong>∥</strong><sub><strong>F</strong></sub><sup><strong>2</strong></sup></span></p>
<p>best <strong>rank</strong> <strong>2</strong> matrix</p>
<p><span class="math display">$$\mathbf{D = U}\begin{bmatrix}
\mathbf{\sigma}_{\mathbf{1}} &amp; \mathbf{0} &amp; \mathbf{0} \\
\mathbf{0} &amp; \mathbf{\sigma}_{\mathbf{2}} &amp; \mathbf{0} \\
\mathbf{0} &amp; \mathbf{0} &amp; \mathbf{0}
\end{bmatrix}\mathbf{V}^{\mathbf{T}}\mathbf{
}$$</span></p></td>
</tr>
<tr>
<td><p><strong>julia&gt; D</strong></p>
<p><strong>1000×3 Matrix{Float64}:</strong></p>
<p><strong>5.43274 7.90601 1.91714</strong></p>
<p><strong>1.07729 5.89151 3.75612</strong></p>
<p><strong>⋮</strong></p>
<p><strong>1.2538 4.87763 10.9128</strong></p>
<p><strong>julia&gt; fact = svd(D)</strong></p>
<p><strong>julia&gt; U = fact.U</strong></p>
<p><strong>julia&gt; S = fact.S</strong></p>
<p><strong>julia&gt; Vt = fact.Vt</strong></p>
<p><strong>julia&gt; S1 = Diagonal([S[1], 0, 0])</strong></p>
<p><strong>julia&gt; S2 = Diagonal([S[1], S[2], 0])</strong></p>
<p><strong>julia&gt; rank1 = U*S1*Vt</strong></p>
<p><strong>julia&gt; rank2 = U*S2*Vt</strong></p>
<p><strong>julia&gt; using DelimitedFiles</strong></p>
<p><strong>julia&gt; writedlm("/tmp/rank1.csv", rank1, ',')</strong></p>
<p><strong>julia&gt; writedlm("/tmp/rank2.csv", rank2, ',')</strong></p></td>
</tr>
</tbody>
</table>

**
**

separate a matrix $`\mathbf{D}`$ into **rank** **one** matrices

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 28%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Intro to Nonlinear Solvers</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><p>Nonlinear Solvers in 1-D</p>
<p>Taylor Series</p></td>
</tr>
<tr>
<td>Taylor Series</td>
<td colspan="2"><ul>
<li><p>from calculus, we know that for smooth functions</p></li>
</ul>
<p><span class="math display">$$\mathbf{f}\left( \mathbf{x} \right)\mathbf{=}\mathbf{f}\left( \mathbf{a} \right)\mathbf{+}\mathbf{f}^{\mathbf{'}}\left( \mathbf{a} \right)\left( \mathbf{x - a} \right)\mathbf{+}\left( \frac{\mathbf{f}^{\mathbf{''}}\left( \mathbf{a} \right)}{\mathbf{2!}} \right)\left( \mathbf{x - a} \right)^{\mathbf{2}}\mathbf{+}\left( \frac{\mathbf{f}^{\mathbf{'''}}\left( \mathbf{a} \right)}{\mathbf{3!}} \right)\left( \mathbf{x - a} \right)^{\mathbf{3}}\mathbf{+ \ldots}$$</span></p>
<p><span class="math display"><strong>|</strong><strong>x</strong> <strong>−</strong> <strong>a</strong><strong>|</strong> <strong>&lt;</strong> <strong>R</strong></span></p>
<ul>
<li><p>this typically only holds inside a convergence radius <span class="math inline"><strong>R</strong></span></p></li>
<li><p>if the derivatives exist and are continuous then,</p></li>
</ul>
<p>truncate after the <span class="math inline"><strong>n</strong></span>-th power</p>
<p>Taylor Series</p>
<p>“with a remainder”</p>
<p><span class="math display">$$\mathbf{f}\left( \mathbf{x} \right)\mathbf{=}\mathbf{f}\left( \mathbf{a} \right)\mathbf{+}\mathbf{f}^{\mathbf{'}}\left( \mathbf{a} \right)\left( \mathbf{x - a} \right)\mathbf{+ \ldots +}\left( \frac{\mathbf{f}^{\left( \mathbf{n} \right)}\left( \mathbf{a} \right)}{\mathbf{n!}} \right)\left( \mathbf{x - a} \right)^{\mathbf{n}}\mathbf{+}\left( \frac{\mathbf{f}^{\left( \mathbf{n + 1} \right)}\left( \mathbf{\xi} \right)}{\left( \mathbf{n + 1} \right)\mathbf{!}} \right)\left( \mathbf{x - a} \right)^{\left( \mathbf{n + 1} \right)}$$</span></p>
<p>Euler’s</p>
<p>Identity</p>
<p>Cosine</p>
<p>Taylor Series</p>
<p>Exponential</p>
<p>Taylor Series</p></td>
</tr>
<tr>
<td><p>Common Examples of Taylor Series</p>
<p>Complex Exponential</p>
<p>Expansion</p>
<p>Sine</p>
<p>Taylor Series</p></td>
<td colspan="2"><p><span class="math display">$$\mathbf{\exp}\left( \mathbf{x} \right)\mathbf{= \ 1\  + \ x + \ }\frac{\mathbf{x}^{\mathbf{2}}}{\mathbf{2}}\mathbf{\  + \ }\frac{\mathbf{x}^{\mathbf{3}}}{\mathbf{3!}}\mathbf{+ \ldots}$$</span></p>
<p><span class="math display">$$\mathbf{\sin}\left( \mathbf{x} \right)\mathbf{= x\  - \ }\frac{\mathbf{x}^{\mathbf{3}}}{\mathbf{3!}}\mathbf{\  + \ }\frac{\mathbf{x}^{\mathbf{5}}}{\mathbf{5!}}\mathbf{\  - \ldots}$$</span></p>
<p><span class="math display">$$\mathbf{\cos}\left( \mathbf{x} \right)\mathbf{= 1\  - \ }\frac{\mathbf{x}^{\mathbf{2}}}{\mathbf{2}}\mathbf{\  + \ }\frac{\mathbf{x}^{\mathbf{4}}}{\mathbf{4!}}\mathbf{- \ldots}$$</span></p>
<p><span class="math display">$$\mathbf{\exp}\left( \mathbf{ix} \right)\mathbf{= 1\  + \ ix\  + \ }\frac{\left( \mathbf{ix} \right)^{\mathbf{2}}}{\mathbf{2}}\mathbf{\  + \ }\frac{\left( \mathbf{ix} \right)^{\mathbf{3}}}{\mathbf{3!}}\mathbf{\  + \ }\frac{\left( \mathbf{ix} \right)^{\mathbf{4}}}{\mathbf{4!}}\mathbf{\  + \ }\frac{\left( \mathbf{ix} \right)^{\mathbf{5}}}{\mathbf{5!}}\mathbf{+ \ldots}$$</span></p>
<p><span class="math display">$$\mathbf{\exp}\left( \mathbf{ix} \right)\mathbf{= \ 1\  + \ ix\  - \ }\frac{\mathbf{x}^{\mathbf{2}}}{\mathbf{2}}\mathbf{\  - \ i}\frac{\mathbf{x}^{\mathbf{3}}}{\mathbf{3!}}\mathbf{\  + \ }\frac{\mathbf{x}^{\mathbf{4}}}{\mathbf{4!}}\mathbf{\  + \ i}\frac{\mathbf{x}^{\mathbf{5}}}{\mathbf{5!}}\mathbf{- \ldots}$$</span></p>
<p><span class="math display"> <strong>=</strong> <strong>c</strong><strong>o</strong><strong>s</strong>(<strong>x</strong>)<strong>+</strong><strong>i</strong> <strong>s</strong><strong>i</strong><strong>n</strong>(<strong>x</strong>)</span></p></td>
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
<th>Finding Roots</th>
<th><ul>
<li><p><img src="generated_media\DATA750_week09_notes\media\image7.png" style="width:2.25417in;height:1.39722in" />How to solve <span class="math inline"><strong>x</strong><strong>=</strong><strong>c</strong><strong>o</strong><strong>s</strong>(<strong>x</strong>)</span></p></li>
</ul>
<p><span class="math display"><em>f</em>(<em>x</em>) = <em>c</em><em>o</em><em>s</em>(<em>x</em>) − <em>x</em></span></p>
<p>wolframalpha.com</p>
<p><span class="math display"><strong>f</strong>(<strong>x</strong>) <strong>=</strong> <strong>c</strong><strong>o</strong><strong>s</strong>(<strong>x</strong>)<strong>−</strong><strong>x</strong></span></p>
<p>only one root</p>
<ul>
<li><p>approximate the root</p></li>
</ul>
<p><span class="math display"><strong>f</strong>(<strong>x</strong>) <strong>≈</strong> <strong>f</strong>(<strong>x</strong><sub><strong>0</strong></sub>)<strong>+</strong><strong>f</strong><sup><strong>′</strong></sup>(<strong>x</strong><sub><strong>0</strong></sub>)(<strong>x</strong><strong>−</strong><strong>x</strong><sub><strong>0</strong></sub>)</span></p>
<ul>
<li><p>find the exact root of the linearized model</p></li>
</ul>
<p><span class="math display"><strong>f</strong>(<strong>x</strong><sub><strong>0</strong></sub>)<strong>+</strong><strong>f</strong><sup><strong>′</strong></sup>(<strong>x</strong><sub><strong>0</strong></sub>)(<strong>x</strong><strong>−</strong><strong>x</strong><sub><strong>0</strong></sub>) <strong>=</strong> <strong>0</strong></span></p>
<p><strong>Newton’s</strong></p>
<p><strong>Method</strong></p>
<p><span class="math display">$$\mathbf{x -}\mathbf{x}_{\mathbf{0}}\mathbf{= - f}\left( \mathbf{x}_{\mathbf{0}} \right)\textit{\textbf{/}}\mathbf{f}^{\mathbf{'}}\left( \mathbf{x}_{\mathbf{0}} \right)$$</span></p>
<ul>
<li><p>use as next ‘guess’</p></li>
</ul>
<p><span class="math display">$$\mathbf{x}_{\mathbf{1}}\mathbf{=}\mathbf{x}_{\mathbf{0}}\mathbf{- f}\left( \mathbf{x}_{\mathbf{0}} \right)\textit{\textbf{/}}\mathbf{f}^{\mathbf{'}}\left( \mathbf{x}_{\mathbf{0}} \right)$$</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">Implementation</td>
<td><ul>
<li><p><strong>Newton’s</strong> <strong>Method</strong> / Newton–Raphson iterates</p></li>
</ul>
<p>with initial guess 0, the iteration converges quickly</p>
<blockquote>
<p><span class="math display">$$\mathbf{x}_{\left( \mathbf{n + 1} \right)}\mathbf{=}\mathbf{x}_{\mathbf{n}}\mathbf{- f}\left( \mathbf{x}_{\mathbf{n}} \right)\textit{\textbf{/}}\mathbf{f}^{\mathbf{'}}\left( \mathbf{x}_{\mathbf{n}} \right)$$</span></p>
</blockquote>
<p><span class="math display"><strong>f</strong>(<strong>x</strong>)<strong>=</strong><strong>cos</strong> (<strong>x</strong>)<strong>−</strong><strong>x</strong><strong>f</strong><sup><strong>′</strong></sup>(<strong>x</strong>)<strong>=</strong><strong>−</strong><strong>s</strong><strong>i</strong><strong>n</strong>(<strong>x</strong>)<strong>−</strong><strong>1</strong></span></p>
<p>second order convergence</p>
<ul>
<li><p><strong>double</strong> the number of <strong>digits</strong> in <strong>each</strong> <strong>step</strong></p></li>
</ul>
<p><span class="math display"><strong>e</strong><sub>(<strong>n</strong> <strong>+</strong> <strong>1</strong>)</sub><strong>≈</strong><strong>C</strong><strong>e</strong><sub><strong>n</strong></sub><sup><strong>2</strong></sup></span></p>
<p>error in the next step (n+1), is previous error squared times a constant C</p></td>
</tr>
<tr>
<td><p><strong>julia&gt; f(x) = cos(x) - x</strong></p>
<p><strong>f (generic function with 1 method)</strong></p>
<p><strong>julia&gt; fp(x) = -sin(x) - 1</strong></p>
<p><strong>fp (generic function with 1 method)</strong></p>
<p><strong>julia&gt; x0 = 0</strong></p>
<p><strong>0</strong></p>
<p><strong>julia&gt; x1 = x0 - f(x0)/fp(x0)</strong></p>
<p><strong>1.0</strong></p>
<p><strong>julia&gt; x2 = x1 - f(x1)/fp(x1)</strong></p>
<p><strong>0.7503638678402439</strong></p>
<p><strong>julia&gt; x3 = x2 - f(x2)/fp(x2)</strong></p>
<p><strong>0.7391128909113617</strong></p>
<p><strong>julia&gt; x4 = x3 - f(x3)/fp(x3)</strong></p>
<p><strong>0.739085133385284</strong></p>
<p><strong>julia&gt; x5 = x4 - f(x4)/fp(x4)</strong></p>
<p><strong>0.7390851332151607</strong></p></td>
</tr>
<tr>
<td><p><strong>julia&gt; x2 - x5</strong></p>
<p><strong>0.01127873462508322</strong></p>
<p><strong>julia&gt; x3 - x5</strong></p>
<p><strong>2.775769620100288e-5</strong></p>
<p><strong>julia&gt; x4 - x5</strong></p>
<p><strong>1.7012335984389892e-10</strong></p></td>
</tr>
<tr>
<td rowspan="2">When Convergence is Messy</td>
<td><ul>
<li><p>sometimes <strong>convergence</strong> can “bounce around” – <strong>taking</strong> some <strong>time</strong> to settle into a <strong>convergent</strong> pattern</p></li>
</ul>
<p><span class="math display">$$\mathbf{x}_{\left( \mathbf{n + 1} \right)}\mathbf{=}\mathbf{x}_{\mathbf{n}}\mathbf{-}\frac{\mathbf{f}\left( \mathbf{x}_{\mathbf{n}} \right)}{\mathbf{f}^{\mathbf{'}}\left( \mathbf{x}_{\mathbf{n}} \right)}$$</span></p>
<p><img src="generated_media\DATA750_week09_notes\media\image8.png" style="width:3.75472in;height:1.41522in" /></p>
<p>ChatGPT 5.3 Thinking</p></td>
</tr>
<tr>
<td><p><strong>julia&gt; x = x0</strong></p>
<p><strong>-6</strong></p>
<p><strong>julia&gt; x = x - f(x)/fp(x)</strong></p>
<p><strong>-0.5598827773710564</strong></p>
<p><strong>julia&gt; x = x - f(x)/fp(x)</strong></p>
<p><strong>2.441099878014685</strong></p>
<p><strong>julia&gt; x = x - f(x)/fp(x)</strong></p>
<p><strong>0.49191148608506574</strong></p>
<p><strong>julia&gt; x = x - f(x)/fp(x)</strong></p>
<p><strong>0.7564751611987038</strong></p>
<p><strong>julia&gt; x = x - f(x)/fp(x)</strong></p>
<p><strong>0.7391506975713239</strong></p>
<p><strong>julia&gt; x = x - f(x)/fp(x)</strong></p>
<p><strong>0.7390851341642681</strong></p>
<p><strong>julia&gt; x = x - f(x)/fp(x)</strong></p>
<p><strong>0.7390851332151607</strong></p></td>
</tr>
<tr>
<td rowspan="2">Secant Method</td>
<td><ul>
<li><p>there are some <strong>problems</strong> with <strong>Newton’s</strong> method</p>
<ul>
<li><p>you need <strong>both</strong> <span class="math inline"><strong>f</strong>(<strong>x</strong>)</span>and <span class="math inline"><strong>f</strong><strong>’</strong>(<strong>x</strong>)</span></p></li>
<li><p>can have a <strong>complicated</strong> <strong>convergence</strong> pattern</p></li>
</ul></li>
<li><p>solution is to <strong>approximate</strong> the <strong>derivative</strong> by <strong>taking</strong> the <strong>slope</strong> between two points</p></li>
</ul>
<p><span class="math display">$$\mathbf{x}_{\left( \mathbf{n + 1} \right)}\mathbf{=}\frac{\mathbf{x}_{\mathbf{n}}\mathbf{- f}\left( \mathbf{x}_{\mathbf{n}} \right)}{\left( \mathbf{f}\left( \mathbf{x}_{\mathbf{n}} \right)\mathbf{- f}\left( \mathbf{x}_{\left( \mathbf{n - 1} \right)} \right)\textit{\textbf{/}}\left( \mathbf{x}_{\mathbf{n}}\mathbf{-}\mathbf{x}_{\left( \mathbf{n - 1} \right)} \right) \right)}$$</span></p>
<ul>
<li><p>convergence is <strong>slower</strong>, but only a <strong>single</strong> <strong>function</strong> is needed at <strong>each</strong> <strong>step</strong></p></li>
<li><p>similar to <strong>Newton’s</strong> method, if it <strong>starts</strong> to close <strong>convergence</strong> <strong>accelerates</strong></p></li>
</ul></td>
</tr>
<tr>
<td><p><strong>julia&gt; f(x) = cos(x) - x</strong></p>
<p><strong>f (generic function with 1 method)</strong></p>
<p><strong>julia&gt; x0 = 0; x1 = 1; x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))</strong></p>
<p><strong>0.6850733573260451</strong></p>
<p><strong>julia&gt; x0 = x1; x1 = x2; x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))</strong></p>
<p><strong>0.736298997613654</strong></p>
<p><strong>julia&gt; x0 = x1; x1 = x2; x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))</strong></p>
<p><strong>0.739119361912693</strong></p>
<p><strong>julia&gt; x0 = x1; x1 = x2; x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))</strong></p>
<p><strong>0.739085112274639</strong></p>
<p><strong>julia&gt; x0 = x1; x1 = x2; x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))</strong></p>
<p><strong>0.7390851332151607</strong></p></td>
</tr>
</tbody>
</table>
