> Markdown version for convenient browsing. Original files:
> - PDF: [DATA750_week10_notes.pdf](../DATA750_week10_notes.pdf)
> - DOCX: [DATA750_week10_notes.docx](DATA750_week10_notes.docx)

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
<th colspan="2">Nonlinear Solvers</th>
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
<li><p>compute the numerical inverse of a function using Newton’s method</p></li>
<li><p>compute partial derivatives and compute the first three terms of a Taylor series approximation for a function of multiple arguments</p></li>
<li><p>identify the three terms for the Taylor series in terms of an approximation of a function multiple arguments</p></li>
<li><p>relate Taylor series terms to tangent plane and critical points</p></li>
<li><p>applying Newtons method in higher dimensions to solve a nonlinear system of equations</p></li>
<li><p>the convergence challenges for Newtons method</p></li>
<li><p>why Newton’s method is not the complete solution for a nonlinear solver</p></li>
<li><p>the data structures used for forward differentiation</p></li>
<li><p>use numerical libraries that implement the forward differentiation approach</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5">Nonlinear Solvers in 1-D Part 2</td>
</tr>
<tr>
<td>Use Case</td>
<td colspan="4"><ul>
<li><p><strong>p</strong>robability <strong>d</strong>ensity <strong>f</strong>unction for the <strong>normal</strong> <strong>distribution</strong> for a given center and <strong>standard</strong> <strong>deviation</strong></p></li>
</ul>
<p>Probability Density Function</p>
<p><span class="math display">$$\mathbf{f}\left( \mathbf{x} \right)\mathbf{=}\frac{\mathbf{1}}{\mathbf{\sigma}\sqrt{\left( \mathbf{2}\mathbf{\pi} \right)}}\mathbf{e}^{\mathbf{-}\frac{\mathbf{1}}{\mathbf{2}}\left( \frac{\mathbf{x - \mu}}{\mathbf{\sigma}} \right)^{\mathbf{2}}}$$</span></p>
<p>Cumulative Distribution Function</p>
<ul>
<li><p><strong>probability</strong> that a value is <strong>less</strong> than <span class="math inline"><strong>x</strong></span></p></li>
</ul>
<p><span class="math display">$$\mathbf{\Phi}\left( \mathbf{x} \right)\mathbf{=}\frac{\mathbf{1}}{\mathbf{\sigma}\sqrt{\left( \mathbf{2}\mathbf{\pi} \right)}}\int_{\mathbf{- \infty}}^{\mathbf{x}}{\mathbf{e}^{\mathbf{-}\frac{\mathbf{1}}{\mathbf{2}}}\left( \frac{\mathbf{t - \mu}}{\mathbf{\sigma}} \right)^{\mathbf{2}}\mathbf{dt}}\mathbf{=}\frac{\mathbf{1}}{\mathbf{2}}\left\lbrack \mathbf{1 +}\mathbf{erf}\left( \frac{\mathbf{x - \mu}}{\mathbf{\sigma}\sqrt{\left( \mathbf{2} \right)}} \right) \right\rbrack$$</span></p>
<ul>
<li></li>
<li><p>where <span class="math inline"><strong>e</strong><strong>r</strong><strong>f</strong>(<strong>x</strong>)</span> is a special <strong>function</strong> <strong>defined</strong> by</p></li>
</ul>
<p>Error Function</p>
<p><span class="math display"><em>e</em><em>r</em><em>f</em> = error funciton</span></p>
<p><span class="math display">$$\mathbf{erf}\left( \mathbf{x} \right)\mathbf{=}\frac{\mathbf{2}}{\sqrt{\mathbf{\pi}}}\int_{\mathbf{0}}^{\mathbf{x}}{\mathbf{e}^{\mathbf{-}\mathbf{t}^{\mathbf{2}}}\mathbf{dt}}$$</span></p></td>
</tr>
<tr>
<td rowspan="2">Invert</td>
<td colspan="4"><ul>
<li><p>to find the <strong>inverse</strong> we view it as a <strong>root</strong> <strong>finding</strong> <strong>problem</strong></p></li>
</ul>
<p><span class="math display"><strong>y</strong> <strong>=</strong><strong>e</strong><strong>r</strong><strong>f</strong>(<strong>x</strong>)<strong>→</strong> <strong>f</strong>(<strong>x</strong>)<strong>=</strong><strong>e</strong><strong>r</strong><strong>f</strong>(<strong>x</strong>)<strong>−</strong> <strong>y</strong> <strong>=</strong> <strong>0</strong></span></p>
<ul>
<li><p>we need an <strong>initial</strong> <strong>guess</strong>, and for most <span class="math inline"><strong>x</strong><strong>e</strong><strong>r</strong><strong>f</strong>(<strong>x</strong>)</span> is close to <span class="math inline"><strong>x</strong></span><strong>,</strong> so</p></li>
</ul>
<p><span class="math display"><strong>x</strong><sub><strong>0</strong></sub> <strong>=</strong> <strong>y</strong></span></p>
<ul>
<li><p>for <strong>Newtons</strong> <strong>method</strong> we need the <strong>derivative</strong> of <span class="math inline"><strong>e</strong><strong>r</strong><strong>f</strong>(<strong>x</strong>)</span>, but that comes from the <strong>fundamental</strong> <strong>theorem</strong> of <strong>calculus</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{er}\mathbf{f}\left( \mathbf{x} \right)\mathbf{=}\frac{\mathbf{2}}{\sqrt{\mathbf{\pi}}}\int_{\mathbf{0}}^{\mathbf{x}}{\mathbf{e}^{\mathbf{-}\mathbf{t}^{\mathbf{2}}}\mathbf{dt\ \ \ }}\mathbf{\rightarrow \ \ \ \ }\mathbf{er}\mathbf{f}^{\mathbf{'}}\left( \mathbf{x} \right)\mathbf{=}\frac{\mathbf{2}}{\sqrt{\mathbf{\pi}}}\mathbf{e}^{\mathbf{-}\mathbf{x}^{\mathbf{2}}}$$</span></p>
<ul>
<li><p>which leads to the <strong>iteration</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{x}_{\mathbf{n + 1}}\mathbf{= \ }\mathbf{x}_{\mathbf{n}}\mathbf{-}\frac{\mathbf{f}\left( \mathbf{x}_{\mathbf{n}} \right)}{\mathbf{f}^{\mathbf{'}}\left( \mathbf{x}_{\mathbf{n}} \right)}\mathbf{= \ }\mathbf{x}_{\mathbf{n}}\mathbf{-}\frac{\mathbf{er}\mathbf{f}\left( \mathbf{x}_{\mathbf{n}} \right)\mathbf{- y}}{\frac{\mathbf{2}}{\sqrt{\mathbf{\pi}}}\mathbf{e}^{\mathbf{-}\mathbf{x}_{\mathbf{n}}^{\mathbf{2}}}}$$</span></p>
<p><span class="math display">$$\mathbf{= \ }\mathbf{x}_{\mathbf{n}}\mathbf{-}\frac{\sqrt{\mathbf{\pi}}}{\mathbf{2}}\mathbf{e}^{\mathbf{x}_{\mathbf{n}}^{\mathbf{2}}}\left( \mathbf{erf}\left( \mathbf{x}_{\mathbf{n}} \right)\mathbf{-}\mathbf{y} \right)$$</span></p></td>
</tr>
<tr>
<td colspan="4"><p><strong>julia&gt; using SpecialFunctions</strong></p>
<p><a href="https://specialfunctions.juliamath.org/v0.1/">https://specialfunctions.juliamath.org/v0.1/</a></p>
<p><strong>julia&gt; y = 0.5; x = y;</strong></p>
<p><strong>julia&gt; x = x - \sqrt(\pi)/2 * exp(x^2) * (erf(x) - y)</strong></p>
<p><strong>0.47667241214786027</strong></p>
<p><strong>julia&gt; x = x - \sqrt(\pi)/2 * exp(x^2) * (erf(x) - y)</strong></p>
<p><strong>0.47693624301317533</strong></p>
<p><strong>julia&gt; x = x - \sqrt(\pi)/2 * exp(x^2) * (erf(x) - y)</strong></p>
<p><strong>0.4769362762044694</strong></p>
<p><strong>julia&gt; x = x - \sqrt(\pi)/2 * exp(x^2) * (erf(x) - y)</strong></p>
<p><strong>0.4769362762044699</strong></p>
<p><strong>julia&gt; x = x - \sqrt(\pi)/2 * exp(x^2) * (erf(x) - y)</strong></p>
<p><strong>0.4769362762044699</strong></p>
<p><strong>julia&gt; erf(x)</strong></p>
<p><strong>0.5</strong></p></td>
</tr>
<tr>
<td colspan="5">Taylor Series in Higher Dimensions</td>
</tr>
<tr>
<td>Taylor Series</td>
<td colspan="4"><ul>
<li><p>function of <strong>one</strong> <strong>argument</strong> the Taylor Series</p></li>
</ul>
<p><span class="math display">$$\mathbf{f}\left( \mathbf{x} \right)\mathbf{= \ f}\left( \mathbf{a} \right)\mathbf{+ \ }\mathbf{f}^{\mathbf{'}}\left( \mathbf{a} \right)\left( \mathbf{x - a} \right)\mathbf{+ \ \cdots +}\frac{\mathbf{f}^{\left( \left( \mathbf{n} \right) \right)\left( \mathbf{a} \right)}}{\mathbf{n!}}\left( \mathbf{x - a} \right)^{\mathbf{n}}\mathbf{+}\frac{\mathbf{f}^{\left( \left( \mathbf{n + 1} \right) \right)\left( \mathbf{a} \right)}}{\left( \mathbf{n + 1} \right)\mathbf{!}}\left( \mathbf{\xi - a} \right)^{\mathbf{n + 1}}$$</span></p>
<ul>
<li><p>consider the case of a <strong>vector</strong> <strong>valued</strong> <strong>function</strong> of one variable</p></li>
</ul>
<p><span class="math display"><strong>f</strong> <strong>:</strong> <strong>R</strong><strong>→</strong> <strong>R</strong><sup><strong>n</strong></sup></span></p>
<ul>
<li><p>component by component, <strong>vector</strong> <strong>valued</strong> <strong>derivative</strong></p></li>
</ul>
<p><span class="math display"><strong>f</strong> <strong>:</strong> <strong>R</strong> <strong>→</strong><strong>R</strong><sup><strong>m</strong></sup>   </span></p>
<p><span class="math display"><strong>f</strong>(<strong>t</strong>)<strong>=</strong> [<strong>t</strong><sup><strong>2</strong></sup><strong>;</strong> <strong>t</strong> <strong>+</strong><strong>s</strong><strong>i</strong><strong>n</strong>(<strong>t</strong>)] </span></p>
<p><span class="math display"><strong>f</strong><sup><strong>′</strong></sup>(<strong>t</strong>)<strong>=</strong> [<strong>2</strong><strong>t</strong><strong>;</strong> <strong>1</strong> <strong>+</strong><strong>c</strong><strong>o</strong><strong>s</strong>(<strong>t</strong>)]</span></p>
<p><span class="math display"><strong>f</strong>(<strong>t</strong>)<strong>=</strong> [<strong>a</strong><sup><strong>2</strong></sup><strong>;</strong> <strong>a</strong> <strong>+</strong><strong>s</strong><strong>i</strong><strong>n</strong>(<strong>a</strong>)]</span></p>
<p><span class="math display">$$\mathbf{+ \ }\left\lbrack \mathbf{2}\mathbf{a;\ 1\  +}\mathbf{co}\mathbf{s}\left( \mathbf{a} \right) \right\rbrack\left( \mathbf{t - a} \right)\mathbf{\ \  + \ \ }\frac{\left\lbrack \mathbf{2;\  -}\mathbf{si}\mathbf{n}\left( \mathbf{a} \right) \right\rbrack\left( \left( \mathbf{t - a} \right)^{\mathbf{2}} \right)}{\mathbf{2!}}\mathbf{+}\mathbf{\cdots}$$</span></p></td>
</tr>
<tr>
<td><ul>
<li><p>Taylor Series in 2D</p></li>
</ul>
<p><span class="math display"><strong>F</strong>(<strong>x</strong><sub><strong>0</strong></sub><strong>,</strong> <strong>y</strong>)<strong>=</strong></span></p></td>
<td colspan="4"><ul>
<li><p>now we allow the <strong>scalar</strong> function to have <strong>multiple</strong> input <strong>arguments</strong></p></li>
</ul>
<p><span class="math display"><strong>F</strong>(<strong>x</strong><strong>,</strong> <strong>y</strong>)<strong>=</strong> <strong>F</strong>(<strong>x</strong><sub><strong>0</strong></sub> <strong>+</strong> (<strong>x</strong> <strong>−</strong> <strong>x</strong><sub><strong>0</strong></sub>)<strong>,</strong> <strong>y</strong><sub><strong>0</strong></sub> <strong>+</strong> (<strong>y</strong> <strong>−</strong> <strong>y</strong><sub><strong>0</strong></sub>))</span></p>
<ul>
<li><p><strong>focus</strong> on the <strong>first</strong> argument, and keep the <strong>second</strong> argument <strong>fixed</strong></p></li>
</ul>
<p><span class="math display"><strong>F</strong>(<strong>x</strong><strong>,</strong> <strong>y</strong>)<strong>=</strong> <strong>F</strong>(<strong>x</strong><sub><strong>0</strong></sub> <strong>+</strong> (<strong>x</strong> <strong>−</strong> <strong>x</strong><sub><strong>0</strong></sub>)<strong>,</strong> <strong>y</strong>)</span></p>
<ul>
<li><p>now that we have a <strong>function</strong> of a <strong>single</strong></p></li>
</ul>
<p>represents the tangent plane approximation of the function at the point <span class="math inline"><strong>(</strong><strong>x</strong><sub><strong>0</strong></sub><strong>,</strong> <strong>y</strong><sub><strong>0</strong></sub><strong>)</strong></span> along the <span class="math inline"><strong>y</strong> <strong>−</strong> <strong>a</strong><strong>x</strong><strong>i</strong><strong>s</strong></span></p>
<blockquote>
<p><strong>argument</strong>, apply the standard <strong>Taylor's</strong> <strong>Series</strong></p>
</blockquote>
<p>as a <strong>function</strong> of <span class="math inline"><strong>y</strong></span><strong>:</strong></p>
<p><span class="math display">$$\mathbf{\ }\frac{\mathbf{f}^{\mathbf{''}}\left( \mathbf{y}_{\mathbf{0}} \right)\left( \left( \mathbf{y\  - \ }\mathbf{y}_{\mathbf{0}} \right)^{\mathbf{2}} \right)}{\mathbf{2!}}$$</span></p>
<p>quadratic</p>
<p>linear term</p>
<p>constant</p>
<p><span class="math display">$$\mathbf{F}\left( \mathbf{x}_{\mathbf{0}}\mathbf{,}\mathbf{y}_{\mathbf{0}}\mathbf{+ \ }\left( \mathbf{y\  - \ }\mathbf{y}_{\mathbf{0}} \right) \right)\mathbf{= F}\left( \mathbf{x}_{\mathbf{0}}\mathbf{,\ }\mathbf{y}_{\mathbf{0}} \right)\mathbf{+}\frac{\mathbf{\partial F\ }}{\mathbf{\partial y}}\left( \mathbf{x}_{\mathbf{0}}\mathbf{,\ }\mathbf{y}_{\mathbf{0}} \right)\left( \mathbf{y -}\mathbf{y}_{\mathbf{0}} \right)\mathbf{+}\frac{\mathbf{\partial}^{\mathbf{2}}\mathbf{F}}{\mathbf{\partial}\mathbf{y}^{\mathbf{2}}}\left( \mathbf{x}_{\mathbf{0}}\mathbf{,\ }\mathbf{y}_{\mathbf{0}} \right)\frac{\left( \left( \mathbf{y\  - \ }\mathbf{y}_{\mathbf{0}} \right)^{\mathbf{2}} \right)}{\mathbf{2!}}\mathbf{+}\mathbf{\cdots}$$</span></p>
<p><span class="math display"> <strong>f</strong>(<strong>y</strong><sub><strong>0</strong></sub>)</span></p>
<p><span class="math display"><strong>f</strong>(<strong>y</strong><sub><strong>0</strong></sub><strong>+</strong>(<strong>y</strong> <strong>−</strong> <strong>y</strong><sub><strong>0</strong></sub>))</span></p>
<p><span class="math display"><strong>f</strong><sup><strong>′</strong></sup>(<strong>y</strong><sub><strong>0</strong></sub>)(<strong>y</strong> <strong>−</strong> <strong>y</strong><sub><strong>0</strong></sub>)</span></p>
<p><strong>Partial Differentiation:</strong></p>
<p>by holding <span class="math inline"><strong>x</strong></span> constant, you treat the multivariable function <span class="math inline"><strong>F</strong><strong>(</strong><strong>x</strong><sub><strong>0</strong></sub><strong>,</strong> <strong>y</strong><strong>)</strong></span> as a univariate function<span class="math inline"> <strong>f</strong><strong>(</strong><strong>y</strong><strong>)</strong></span></p>
<p>this allows the use of standard Taylor</p>
<p>expansion rules using partial derivatives <span class="math inline">$\frac{\mathbf{\partial F\ }}{\mathbf{\partial y}}$</span></p>
<p><strong>by symmetry</strong>, the expansion along the <span class="math inline"><strong>x</strong> <strong>−</strong> <strong>a</strong><strong>x</strong><strong>i</strong><strong>s</strong></span> is identical, substituting all <span class="math inline"><strong>y</strong></span> terms for <span class="math inline"><strong>x</strong></span> and holding <span class="math inline"><strong>y</strong></span> constant</p>
<p>a little busy</p></td>
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
<th>The Symmetry Rule</th>
<th><ul>
<li><p>the Taylor expansion for any single variable is performed by holding all other variables constant at the anchor point <span class="math inline">(<strong>x</strong><sub><strong>0</strong></sub><strong>,</strong> <strong>y</strong><sub><strong>0</strong></sub>)</span></p></li>
</ul>
<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 21%" />
<col style="width: 30%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Axis of Expansion</strong></th>
<th style="text-align: center;"><strong>Variable Held Constant</strong></th>
<th style="text-align: center;"><strong>Resulting Univariate Function</strong></th>
<th style="text-align: center;"><strong>First-Order (Linear) Term</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>y-axis</strong></td>
<td style="text-align: center;"><span class="math display"><strong>x</strong> <strong>=</strong> <strong>x</strong><sub><strong>0</strong></sub></span></td>
<td style="text-align: center;"><span class="math display"><strong>f</strong>(<strong>y</strong>)<strong>=</strong> <strong>F</strong>(<strong>x</strong><sub><strong>0</strong></sub><strong>,</strong> <strong>y</strong>)</span></td>
<td style="text-align: center;"><span class="math display">$$\frac{\mathbf{\partial F}}{\mathbf{\partial y}}\left( \mathbf{x}_{\mathbf{0}}\mathbf{,\ }\mathbf{\ y}_{\mathbf{0}} \right)\left( \mathbf{y\  - \ }\mathbf{y}_{\mathbf{0}} \right)$$</span></td>
</tr>
<tr>
<td style="text-align: center;"><strong>x-axis</strong></td>
<td style="text-align: center;"><span class="math display"><strong>y</strong> <strong>=</strong> <strong>y</strong><sub><strong>0</strong></sub></span></td>
<td style="text-align: center;"><span class="math display"><strong>f</strong>(<strong>x</strong>)<strong>=</strong> <strong>F</strong>(<strong>x</strong><strong>,</strong> <strong>y</strong><sub><strong>0</strong></sub>)</span></td>
<td style="text-align: center;"><span class="math display">$$\frac{\partial F}{\partial x}\mathbf{\ }\left( \mathbf{x}_{\mathbf{0}}\mathbf{,\ }\mathbf{y}_{\mathbf{0}} \right)\left( \mathbf{x\  - \ }\mathbf{x}_{\mathbf{0}} \right)$$</span></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr>
<td>Combine</td>
<td><ul>
<li><p>group by powers, and skip <span class="math inline">(<strong>x</strong><sub><strong>0</strong></sub><strong>,</strong> <strong>y</strong><sub><strong>0</strong></sub>)</span></p></li>
</ul>
<p>1. the <strong>single</strong> <strong>variables</strong> start (along <span class="math inline"><strong>x</strong></span>)</p>
<p><span class="math display">$$F(x,\ y) = \ F\left( x_{0},\ y \right) + \frac{\partial F}{\partial x}\left( x_{0},\ y \right)\left( x\  - \ x_{0} \right) + \frac{\partial^{2}F}{\partial x^{2}}\left( x_{0},\ y \right)\frac{\left( \left( x\  - \ x_{0} \right)^{2} \right)}{2!} + \cdots$$</span></p>
<p>2. the <strong>full</strong> bivariate <strong>expansion</strong> (<strong>all</strong> terms)</p>
<p><span class="math display">$$F(x,\ y) = \ F\left( x_{0},\ y_{0} \right) + \frac{\partial F}{\partial x}\left( x\  - \ x_{0} \right) + \frac{\partial F}{\partial y}\left( y\  - \ y_{0} \right)$$</span></p>
<p><span class="math display">$$+ \frac{1}{2}\left\lbrack \frac{\partial^{2}F}{\left( \partial x^{2} \right)\left( x\  - \ x_{0} \right)^{2}} + \frac{2\left( \partial^{2}F \right)}{(\partial x\ \partial y)\left( x\  - \ x_{0} \right)\left( y\  - \ y_{0} \right)} + \frac{\partial^{2}F}{\left( \partial y^{2} \right)\left( y\  - \ y_{0} \right)^{2}} \right\rbrack$$</span></p>
<p>3. the <strong>matrix</strong> wrap-up (<strong>quadratic</strong> <strong>form</strong>)</p>
<p><span class="math display">$$F(x,\ y) = \ F\left( x_{0},\ y_{0} \right) + \ \left\lbrack \frac{\partial F}{\partial x},\frac{\partial F}{\partial y} \right\rbrack\left\lbrack x\  - \ x_{0};\ y\  - \ y_{0} \right\rbrack$$</span></p>
<p><span class="math display">$$+ \frac{1}{2}\left\lbrack x\  - \ x_{0},\ y\  - \ y_{0} \right\rbrack\left\lbrack \frac{\partial^{2}F}{\partial x^{2}},\frac{\partial^{2}F}{\partial x\ \partial y};\frac{\partial^{2}F}{\partial x\ \partial y},\frac{\partial^{2}F}{\partial y^{2}} \right\rbrack\left\lbrack x\  - \ x_{0};\ y\  - \ y_{0} \right\rbrack$$</span></p></td>
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
<th colspan="2">Approximations</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tangent Plane</td>
<td><ul>
<li><p>Taylor Series in two dimensions for a scalar valued function is</p></li>
</ul>
<p><span class="math display">$$\mathbf{f}\left( \mathbf{x}_{\mathbf{0}}\mathbf{,}\mathbf{y}_{\mathbf{0}} \right)\mathbf{+ \ }\left\lbrack \mathbf{\ }\frac{\mathbf{\partial f}}{\mathbf{\partial x}}\mathbf{,\ }\frac{\mathbf{\partial f}}{\mathbf{\partial y}} \right\rbrack\mathbf{\ }\left\lbrack \mathbf{\ }\begin{array}{r}
\mathbf{x\  - \ }\mathbf{x}_{\mathbf{0}} \\
\mathbf{y\  - \ }\mathbf{y}_{\mathbf{0}}
\end{array}\mathbf{\ } \right\rbrack$$</span></p>
<p><span class="math display">$$\mathbf{+ \ \ }\frac{\mathbf{1}}{\mathbf{2}}\left\lbrack \begin{array}{r}
\mathbf{x\  - \ }\mathbf{x}_{\mathbf{0}} \\
\mathbf{y\  - \ }\mathbf{y}_{\mathbf{0}}
\end{array} \right\rbrack^{\mathbf{T}}\left\lbrack \mathbf{\ \ }\begin{array}{r}
\frac{\mathbf{\partial}^{\mathbf{2}}\mathbf{f}}{\mathbf{\partial}\mathbf{x}^{\mathbf{2}}}\mathbf{,\ \ }\frac{\mathbf{\partial}^{\mathbf{2}}\mathbf{f}}{\mathbf{\ \partial x\ \partial y}} \\
\frac{\mathbf{\partial}^{\mathbf{2}}\mathbf{f}}{\mathbf{\partial x\ \partial y}}\mathbf{,\ \ }\frac{\mathbf{\partial}^{\mathbf{2}}\mathbf{f}}{\mathbf{\partial}\mathbf{y}^{\mathbf{2}}}
\end{array}\mathbf{\ } \right\rbrack\mathbf{\ \ }\left\lbrack \mathbf{\ }\begin{array}{r}
\mathbf{x\  - \ }\mathbf{x}_{\mathbf{0}} \\
\mathbf{y\  - \ }\mathbf{y}_{\mathbf{0}}
\end{array}\mathbf{\ } \right\rbrack\mathbf{\ \  +}\mathbf{\cdots}$$</span></p>
<ul>
<li><p>approximations handles what happens close by</p>
<ul>
<li><p>the point the second term shrinks faster than the first</p></li>
</ul></li>
</ul>
<p><span class="math display">$$\mathbf{f}\left( \mathbf{x,y} \right)\mathbf{= \ f}\left( \mathbf{x}_{\mathbf{0}}\mathbf{,\ }\mathbf{y}_{\mathbf{0}} \right)\mathbf{+ \ }\left( \frac{\mathbf{\partial f}}{\mathbf{\partial x}}\left( \mathbf{x}_{\mathbf{0}}\mathbf{,\ }\mathbf{y}_{\mathbf{0}} \right)\mathbf{,}\frac{\mathbf{\partial f}}{\mathbf{\partial y}}\left( \mathbf{x}_{\mathbf{0}}\mathbf{,\ }\mathbf{y}_{\mathbf{0}} \right) \right)\mathbf{\cdot}\left( \mathbf{x\  - \ }\mathbf{x}_{\mathbf{0}}\mathbf{,\ y\  - \ }\mathbf{y}_{\mathbf{0}} \right)$$</span></p>
<p><span class="math display"><strong>z</strong> <strong>=</strong> <strong>a</strong> <strong>+</strong> (<strong>b</strong><strong>,</strong> <strong>c</strong>)<strong>⋅</strong> (<strong>x</strong> <strong>−</strong> <strong>x</strong><sub><strong>0</strong></sub><strong>,</strong> <strong>y</strong> <strong>−</strong> <strong>y</strong><sub><strong>0</strong></sub>)</span></p>
<p>plane equation</p>
<p><span class="math display"><strong>−</strong><strong>b</strong><strong>x</strong> <strong>−</strong> <strong>c</strong><strong>y</strong> <strong>+</strong> <strong>1</strong><strong>z</strong> <strong>=</strong> <strong>a</strong> <strong>−</strong> <strong>b</strong><strong>x</strong><sub><strong>0</strong></sub> <strong>−</strong> <strong>c</strong><strong>y</strong><sub><strong>0</strong></sub> <strong>=</strong> <strong>C</strong></span></p>
<p><strong>nor</strong> does it require the <strong>number</strong> of <strong>input</strong> <strong>arguments</strong> to be the <strong>same</strong> as output</p></td>
</tr>
<tr>
<td>General</td>
<td><ul>
<li><p>this is <strong>not</strong> <strong>limited</strong> to <strong>two</strong> <strong>dimensions</strong></p></li>
</ul>
<blockquote>
<p><span class="math display">$$F\left( \ \left\lbrack \ \begin{array}{r}
x \\
y \\
z
\end{array}\  \right\rbrack\  \right) = \ \left\lbrack \ \begin{array}{r}
\cos(x) + \ y \\
x^{2} + \ 2y^{2} - \ z
\end{array}\  \right\rbrack$$</span></p>
</blockquote>
<p><span class="math display">$$F\left( \ \left\lbrack \ \begin{array}{r}
x \\
y \\
z
\end{array}\  \right\rbrack\  \right) \approx F\left( \ \left\lbrack \ \begin{array}{r}
x_{0} \\
y_{0} \\
z_{0}
\end{array}\  \right\rbrack\  \right) + \ \left\lbrack \ \begin{array}{r}
 - \text{ }\sin(x)\ \ \ \ \ \ \ 1\ \ \ \ \ \ \ \ \ \ 0 \\
\ \ \ \ \ \ \ \ 2x\ \ \ \ \ \ \ \ \ \ \ 4y\ \ \  - 1
\end{array}\  \right\rbrack\left\lbrack \ \begin{array}{r}
\ x\  - \ x_{0} \\
y\  - \ y_{0} \\
z\  - \ z_{0}
\end{array}\  \right\rbrack$$</span></p>
<p>Jacobian</p></td>
</tr>
</tbody>
</table>
