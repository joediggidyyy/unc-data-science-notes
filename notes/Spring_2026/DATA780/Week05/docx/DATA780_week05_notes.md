---
generated_at_utc: 2026-02-23T19:29:34+00:00
generated_from: notes/Spring_2026/DATA780/Week05/docx/DATA780_week05_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week05_notes.pdf](../DATA780_week05_notes.pdf)
> - DOCX: [DATA780_week05_notes.docx](DATA780_week05_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 12%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Classification II</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Discriminative vs Generative Models</td>
</tr>
<tr>
<td>Discriminative Models</td>
<td colspan="2"><ul>
<li><p><strong>directly</strong> look at <strong>estimating</strong> the <strong>likelihood</strong> of <span class="math inline"><strong>y</strong></span> given <span class="math inline"><strong>x</strong></span></p></li>
</ul>
<p><strong>Direct</strong></p>
<p><span class="math display"><strong>P</strong>(<strong>Y</strong>|<strong>X</strong>)</span></p>
<ul>
<li><p>has <strong>no</strong> <strong>knowledge</strong> of the <strong>distribution</strong> of <span class="math inline"><strong>X</strong></span></p></li>
<li><p><strong>cannot</strong> <strong>generate</strong> <strong>synthetic</strong> instances <span class="math inline"><strong>P</strong>(<strong>X</strong><strong>,</strong> <strong>Y</strong>)</span></p></li>
<li><p>these are the <strong>models</strong> we have studied in <strong>earlier</strong> <strong>chapters</strong></p>
<ul>
<li><p><strong>linear</strong> regression, <strong>logistic</strong> regression</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Generative Models</td>
<td colspan="2"><ul>
<li><p>models the <strong>joint</strong> <strong>distribution</strong> between <span class="math inline"><strong>x</strong></span> and <span class="math inline"><strong>y</strong></span></p></li>
</ul>
<p><strong>Indirect</strong></p>
<p><span class="math display"><strong>P</strong>(<strong>X</strong><strong>,</strong> <strong>Y</strong>)</span></p>
<p><span class="math display">$$\mathbf{P}\left( \mathbf{Y} \middle| \mathbf{X} \right)\mathbf{=}\frac{\mathbf{P}\left( \mathbf{X,Y} \right)}{\int_{}^{}{\mathbf{P}\left( \mathbf{X,Y} \right)\mathbf{dY}}}$$</span></p>
<ul>
<li><p><strong>can</strong> <strong>generate</strong> instances of <span class="math inline">(<strong>X</strong><strong>,</strong> <strong>Y</strong>)</span></p></li>
</ul></td>
</tr>
<tr>
<td>Optimal Classifier</td>
<td colspan="2"><ul>
<li><p><strong>Bayes</strong> <strong>Rule</strong></p></li>
</ul>
<p><strong>Discriminative</strong> approach</p>
<p><span class="math display">$$\mathbf{P}\left( \mathbf{X} \middle| \mathbf{Y} \right)\mathbf{=}\frac{\mathbf{P}\left( \mathbf{X} \middle| \mathbf{Y} \right)\mathbf{P}\left( \mathbf{Y} \right)}{\mathbf{P}\left( \mathbf{X} \right)}$$</span></p>
<p><span class="math display">$$\mathbf{P}\left( \mathbf{Y = y} \middle| \mathbf{X = x} \right)\mathbf{=}\frac{\mathbf{P}\left( \mathbf{X = x} \middle| \mathbf{Y = y} \right)\mathbf{P}\left( \mathbf{Y = y} \right)}{\mathbf{P}\left( \mathbf{X = x} \right)}$$</span></p>
<ul>
<li><p><strong>optimal</strong> <strong>classifier</strong></p></li>
</ul>
<p>applying <strong>Bayes Rule</strong> (<strong>Generative</strong>)</p>
<p><span class="math display">$$\mathbf{f}^{\mathbf{*}}\left( \mathbf{x} \right)\mathbf{=}\underset{\mathbf{Y = y}}{\mathbf{argmax}}{\mathbf{P}\left( \mathbf{Y = y} \middle| \mathbf{X = x} \right)}$$</span></p>
<p><span class="math display">$$\mathbf{f*}\left( \mathbf{x} \right)\mathbf{=}\underset{\mathbf{Y = y}}{\mathbf{argmax}}{\mathbf{P}\left( \mathbf{X = x} \middle| \mathbf{Y = y} \right)\mathbf{P}\left( \mathbf{Y = y} \right)}$$</span></p>
<ul>
<li><p>class <strong>prior</strong>: tells you the</p></li>
</ul>
<p><strong>liklihoods</strong> <strong>without</strong> any</p>
<p><strong>knowledge</strong> of <strong>input</strong></p>
<ul>
<li><p>class <strong>conditional</strong>: tells</p></li>
</ul>
<p><strong>distribution</strong> of input <strong>features</strong> <strong>given</strong> the label <span class="math inline"><strong>y</strong></span></p>
<p>Class <strong>Conditional</strong> <strong>Density</strong></p>
<p>Class <strong>Prior</strong></p></td>
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
<th colspan="2">Generative Approach with Gaussians</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gaussians</td>
<td><ul>
<li><p>we can now <strong>consider</strong> appropriate <strong>models</strong> for the two terms</p>
<ul>
<li><p>class <strong>probability</strong> <span class="math inline"><strong>P</strong>(<strong>Y</strong> <strong>=</strong> <strong>y</strong>)</span></p>
<ul>
<li><p><span class="math inline"><strong>B</strong><strong>e</strong><strong>r</strong><strong>n</strong><strong>o</strong><strong>u</strong><strong>l</strong><strong>l</strong><strong>i</strong>(<strong>θ</strong>)</span></p></li>
<li><p><span class="math inline"><strong>P</strong>(<strong>Y</strong> <strong>=</strong> <strong>h</strong><strong>e</strong><strong>a</strong><strong>d</strong><strong>s</strong>) <strong>=</strong> <strong>θ</strong>     <strong>P</strong>(<strong>Y</strong> <strong>=</strong> <strong>t</strong><strong>a</strong><strong>i</strong><strong>l</strong><strong>s</strong>) <strong>=</strong> <strong>1</strong> <strong>−</strong> <strong>θ</strong></span></p></li>
</ul></li>
<li><p>class <strong>conditional</strong> distribution of <span class="math inline"><strong>P</strong>(<strong>X</strong> <strong>=</strong> <strong>x</strong>|<strong>Y</strong> <strong>=</strong> <strong>y</strong>)</span></p>
<ul>
<li><p><strong>Gaussian</strong> class <strong>contitional</strong> (two dimensions)</p></li>
<li><p><span class="math inline">$\mathbf{P(X\  = \ x\ |\ Y\  = \ y)\  = \ }\frac{\mathbf{1}}{\sqrt{\mathbf{2}\mathbf{\pi|}\mathbf{\Sigma}_{\mathbf{y}}}}\mathbf{exp}\mathbf{(}\frac{\left( \mathbf{x -}\mathbf{\mu}_{\mathbf{y}} \right)\mathbf{\Sigma}_{\mathbf{y}}^{\mathbf{- 1}}\left( \mathbf{x\  - \ }\mathbf{\mu}_{\mathbf{y}} \right)^{\mathbf{T}}}{\mathbf{2}}$</span><strong>)</strong></p></li>
<li><p>parameters are <strong>dependant</strong> on the <strong>values</strong> we are <strong>conditioning</strong></p></li>
<li><p>for <strong>Gaussian</strong>, <span class="math inline"><strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong></span> and <span class="math inline"><strong>c</strong><strong>o</strong><strong>v</strong><strong>a</strong><strong>r</strong><strong>i</strong><strong>a</strong><strong>n</strong><strong>c</strong><strong>e</strong></span> are <strong>dependant</strong> on <span class="math inline"><strong>y</strong></span> value</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Gaussian Bayes Classifier</td>
<td><ul>
<li><p>classifier that <strong>models</strong> the <strong>joint</strong> <strong>likelihood</strong> using class condition distributers by <strong>esitmating</strong> the <strong>marginal</strong> <strong>distribution</strong> of <span class="math inline"><strong>y</strong></span></p>
<ul>
<li><p>gives <strong>probablity</strong> for of <span class="math inline"><strong>y</strong></span> for <strong>all</strong> potential <strong>values</strong></p></li>
</ul></li>
<li><p>then, we <strong>model</strong> <span class="math inline"><strong>x</strong></span> given <span class="math inline"><strong>y</strong></span> by <strong>fitting</strong> a <strong>Gaussian</strong></p>
<ul>
<li><p>we are <strong>varying</strong> the <strong>mean</strong> and <strong>covariance</strong> matrix</p></li>
</ul></li>
</ul>
<blockquote>
<p><strong>depending</strong> on <span class="math inline"><strong>y</strong></span></p>
</blockquote>
<ul>
<li><p>each <span class="math inline"><strong>y</strong></span> gets its own <strong>mean</strong> and <strong>covariance</strong> <strong>matrix</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Decision Boundary of Gaussian Bayes</td>
<td style="text-align: center;"><p><img src="generated_media\DATA780_week05_notes\media\image1.png" style="width:3.21435in;height:2.11406in" /></p>
<p>the <strong>decision</strong> <strong>boundary</strong> can take <strong>different</strong> <strong>forms</strong> (generally <strong>quadratic</strong> for <strong>Gaussians</strong>)</p></td>
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
<th>Gaussian Bayes Parameters</th>
<th><ul>
<li><p>as stated, for each potential value of <span class="math inline"><strong>y</strong></span></p>
<ul>
<li><p>estimating probability</p></li>
<li><p>estimating Gaussian</p></li>
</ul></li>
<li><p>estimating conditional Gaussian parameters</p></li>
</ul>
<p><strong>data</strong> is <strong>split</strong> into <span class="math inline"><strong>c</strong></span> “buckets” given <span class="math inline"><strong>c</strong></span> potential <strong>values</strong></p>
<p><span class="math display">{(<strong>x</strong><sub><strong>i</strong></sub><strong>,</strong><strong>y</strong><sub><strong>i</strong></sub>)}<sub><strong>i</strong> <strong>=</strong> <strong>1</strong></sub><sup><strong>n</strong></sup></span></p>
<p><strong>estimate</strong> <strong>mean</strong> and <strong>covariance</strong> parameters for <strong>each</strong></p>
<p><span class="math display"><strong>y</strong> <strong>=</strong> <strong>1</strong>     <strong>y</strong> <strong>=</strong> <strong>2</strong>   <strong>…</strong>    <strong>y</strong> <strong>=</strong> <strong>c</strong></span></p>
<p><span class="math display"><strong>μ</strong><sub><strong>y</strong><strong>1</strong></sub><strong>,</strong><strong>ϵ</strong><sub><strong>y</strong><strong>1</strong></sub>        <strong>μ</strong><sub><strong>y</strong><strong>2</strong></sub><strong>,</strong><strong>ϵ</strong><sub><strong>y</strong><strong>2</strong></sub>          <strong>μ</strong><sub><strong>y</strong><strong>3</strong></sub><strong>,</strong><strong>ϵ</strong><sub><strong>y</strong><strong>3</strong></sub></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>How Many Parameters are Needed to Learn?</td>
<td><ul>
<li><p><strong>class</strong> <strong>probability</strong></p></li>
</ul>
<p><span class="math inline"><strong>p</strong><sub><strong>0</strong></sub><strong>,</strong><strong>p</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>p</strong><sub><strong>k</strong></sub></span> all sum to <strong>1</strong></p>
<ul>
<li><p><span class="math inline"><strong>P</strong>(<strong>Y</strong> <strong>=</strong> <strong>y</strong>) <strong>=</strong> <strong>p</strong> <strong>f</strong><strong>o</strong><strong>r</strong> <strong>a</strong><strong>l</strong><strong>l</strong> <strong>y</strong> <strong>i</strong><strong>n</strong> <strong>0</strong><strong>,</strong> <strong>1</strong><strong>,</strong> <strong>2</strong><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>k</strong></span></p></li>
</ul>
<p><span class="math display"><strong>k</strong> <strong>−</strong> <strong>1</strong> <em>p</em><em>a</em><em>r</em><em>m</em><em>e</em><em>t</em><em>e</em><em>r</em><em>s</em> <em>n</em><em>e</em><em>e</em><em>d</em><em>e</em><em>d</em> <em>i</em><em>f</em> <strong>k</strong> <em>l</em><em>a</em><em>b</em><em>e</em><em>l</em><em>s</em></span></p>
<p><span class="math display"><strong>μ</strong><sub><strong>y</strong></sub><strong>−</strong><strong>d</strong> <strong>•</strong> <strong>d</strong><strong>i</strong><strong>m</strong> <strong>v</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong></span></p>
<p><span class="math display"><strong>ϵ</strong><sub><strong>y</strong></sub><strong>−</strong><strong>d</strong> <strong>×</strong> <strong>d</strong> <strong>m</strong><strong>a</strong><strong>t</strong><strong>r</strong><strong>i</strong><strong>x</strong></span></p>
<ul>
<li><p><strong>class</strong> <strong>conditional</strong> distribution of features</p></li>
</ul>
<p><span class="math display"><strong>P</strong>(<strong>X</strong> <strong>=</strong> <strong>x</strong>|<strong>Y</strong> <strong>=</strong> <strong>y</strong>) <strong>∼</strong> <strong>N</strong>(<strong>μ</strong><sub><strong>y</strong></sub><strong>,</strong><strong>ϵ</strong><sub><strong>y</strong></sub>) <em>f</em><em>o</em><em>r</em> <em>e</em><em>a</em><em>c</em><em>h</em> <strong>y</strong></span></p></td>
</tr>
<tr>
<td colspan="2">Discrete Features</td>
</tr>
<tr>
<td>Binary Classification</td>
<td><ul>
<li><p><strong>example</strong>: black and white image</p>
<ul>
<li><p>each <strong>image</strong> is <strong>represented</strong> as a <strong>vector</strong> of <span class="math inline"><strong>d</strong></span> binary <strong>features</strong></p></li>
<li><p><strong>black</strong>=1, <strong>white</strong>=0</p></li>
</ul></li>
<li><p><strong>training</strong> data</p>
<ul>
<li><p><strong>input</strong>, <span class="math inline"><em>X</em></span></p></li>
</ul></li>
</ul>
<blockquote>
<p><span class="math inline"><strong>n</strong></span> <span class="math inline"><em>i</em><em>m</em><em>a</em><em>g</em><em>e</em><em>s</em></span></p>
</blockquote>
<p><span class="math display"><strong>2</strong></span></p>
<p><strong>1</strong></p>
<ul>
<li><p><strong>label</strong>, <span class="math inline"><em>Y</em></span></p></li>
</ul>
<blockquote>
<p><span class="math inline"><strong>1</strong>              <strong>2</strong></span> <span class="math inline"><strong>n</strong></span> <span class="math inline"><em>l</em><em>a</em><em>b</em><em>e</em><em>l</em><em>s</em></span></p>
</blockquote></td>
</tr>
<tr>
<td>Discrete Bayes Model</td>
<td><p><span class="math display"><strong>P</strong>(<strong>Y</strong> <strong>=</strong> <strong>y</strong>)<strong>=</strong> <strong>p</strong><sub><strong>y</strong></sub><strong>,</strong></span></p>
<p><span class="math display"> <strong>f</strong><strong>o</strong><strong>r</strong> <strong>a</strong><strong>l</strong><strong>l</strong> <strong>y</strong> <strong>∈</strong> {<strong>0</strong><strong>,</strong> <strong>1</strong><strong>,</strong> <strong>2</strong><strong>,</strong><strong>…</strong><strong>,</strong> <strong>9</strong>}<strong>,</strong> </span></p>
<p><span class="math display"><strong>Σ</strong><sub>{<strong>y</strong> <strong>=</strong> <strong>0</strong>}<sub><strong>y</strong></sub><sup>{<strong>9</strong>}<strong>p</strong></sup></sub><strong>=</strong> <strong>1</strong></span></p>
<p><span class="math display"><strong>P</strong>(<strong>X</strong> <strong>=</strong> <strong>x</strong>|<strong>Y</strong> <strong>y</strong>)</span></p>
<p><span class="math display"> <strong>∼</strong> <strong>F</strong><strong>o</strong><strong>r</strong> <strong>e</strong><strong>a</strong><strong>c</strong><strong>h</strong> <strong>l</strong><strong>a</strong><strong>b</strong><strong>e</strong><strong>l</strong> <strong>y</strong><strong>,</strong> <strong>m</strong><strong>a</strong><strong>i</strong><strong>n</strong><strong>t</strong><strong>a</strong><strong>i</strong><strong>n</strong> <strong>a</strong> <strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>a</strong><strong>b</strong><strong>i</strong><strong>l</strong><strong>i</strong><strong>t</strong><strong>y</strong> <strong>t</strong><strong>a</strong><strong>b</strong><strong>l</strong><strong>e</strong> <strong>w</strong><strong>i</strong><strong>t</strong><strong>h</strong> </span></p>
<p><span class="math display">$$\mathbf{2\hat{}d\  - \ 1\ entrie}\mathbf{s}$$</span></p></td>
</tr>
<tr>
<td colspan="2">Getting Rid of Parameters</td>
</tr>
<tr>
<td>What is wrong with too many parameters?</td>
<td><ul>
<li><p>even for a <strong>single</strong> <strong>parameter</strong>, to build an <strong>accurate</strong> <strong>representation</strong>, you need <strong>hundreds</strong>, or even <strong>thousands</strong>, of training <strong>samples</strong></p></li>
<li><p><strong>generative</strong> models often use <span class="math inline">$\mathbf{10\hat{}x}$</span> paramters where <span class="math inline"><strong>x</strong> <strong>&gt;</strong> <strong>10000</strong></span></p></li>
</ul></td>
</tr>
<tr>
<td>Conditional Independence</td>
<td><ul>
<li><p><span class="math inline"><strong>X</strong></span> is <strong>condtionally</strong> <strong>independent</strong> of <span class="math inline"><strong>Y</strong></span> given Z:</p>
<ul>
<li><p>Probability <strong>distribution</strong> governing <span class="math inline"><strong>X</strong> </span>is <strong>independent</strong> of the value of <span class="math inline"><strong>Y</strong></span>, <strong>given</strong> the value of <span class="math inline"><strong>Z</strong></span></p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>(</strong><strong>∀</strong> <strong>x</strong><strong>,</strong> <strong>y</strong><strong>,</strong> <strong>z</strong><strong>)</strong>  <strong>P</strong><strong>(</strong><strong>X</strong> <strong>=</strong> <strong>x</strong> <strong>|</strong> <strong>Y</strong> <strong>=</strong> <strong>y</strong><strong>,</strong> <strong>Z</strong> <strong>=</strong> <strong>z</strong><strong>)</strong> <strong>=</strong> <strong>P</strong><strong>(</strong><strong>X</strong> <strong>=</strong> <strong>x</strong> <strong>|</strong> <strong>Z</strong> <strong>=</strong> <strong>z</strong><strong>)</strong></span></p>
<p><strong>Note:</strong> This does <em><strong>not</strong></em> mean thunder is independent of rain!</p>
<ul>
<li><p><strong>equivelent</strong> to:</p></li>
</ul>
<p><span class="math display"><strong>P</strong><strong>(</strong><strong>X</strong><strong>,</strong> <strong>Y</strong> <strong>|</strong> <strong>Z</strong><strong>)</strong> <strong>=</strong> <strong>P</strong><strong>(</strong><strong>X</strong> <strong>|</strong> <strong>Z</strong><strong>)</strong> <strong>P</strong><strong>(</strong><strong>Y</strong> <strong>|</strong> <strong>Z</strong><strong>)</strong></span></p>
<ul>
<li><p>for <strong>example</strong>:</p></li>
</ul>
<p><span class="math display"><strong>P</strong><strong>(</strong><strong>T</strong><strong>h</strong><strong>u</strong><strong>n</strong><strong>d</strong><strong>e</strong><strong>r</strong> <strong>|</strong> <strong>R</strong><strong>a</strong><strong>i</strong><strong>n</strong><strong>,</strong> <strong>L</strong><strong>i</strong><strong>g</strong><strong>h</strong><strong>t</strong><strong>n</strong><strong>i</strong><strong>n</strong><strong>g</strong><strong>)</strong> <strong>=</strong> <strong>P</strong><strong>(</strong><strong>T</strong><strong>h</strong><strong>u</strong><strong>n</strong><strong>d</strong><strong>e</strong><strong>r</strong> <strong>|</strong> <strong>L</strong><strong>i</strong><strong>g</strong><strong>h</strong><strong>t</strong><strong>n</strong><strong>i</strong><strong>n</strong><strong>g</strong><strong>)</strong></span></p></td>
</tr>
<tr>
<td>Naïve Bayes Classifier</td>
<td><ul>
<li><p><strong>Bayes</strong> <strong>Classifier</strong> with additional “<strong>naive</strong>” <strong>assumption</strong></p></li>
</ul>
<p><span class="math display">$$X = \genfrac{[}{]}{0pt}{}{X_{1}}{X_{2}}\ $$</span></p>
<p><span class="math display"><strong>P</strong><strong>(</strong><strong>X</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>X</strong><sub><strong>2</strong></sub> <strong>|</strong> <strong>Y</strong><strong>)</strong> <strong>=</strong> <strong>P</strong><strong>(</strong><strong>X</strong><sub><strong>1</strong></sub> <strong>|</strong> <strong>X</strong><sub><strong>2</strong></sub><strong>,</strong> <strong>Y</strong><strong>)</strong> <strong>P</strong><strong>(</strong><strong>X</strong><sub><strong>2</strong></sub> <strong>|</strong> <strong>Y</strong><strong>)</strong></span></p>
<p><span class="math display"><strong>=</strong> <strong>P</strong><strong>(</strong><strong>X</strong><sub><strong>1</strong></sub> <strong>|</strong> <strong>Y</strong><strong>)</strong> <strong>P</strong><strong>(</strong><strong>X</strong><sub><strong>2</strong></sub> <strong>|</strong> <strong>Y</strong><strong>)</strong></span></p>
<p><span class="math inline">$X = \begin{bmatrix}
\begin{matrix}
x_{1} \\
x_{2}
\end{matrix} \\
\ldots \\
x_{d}
\end{bmatrix}$</span></p>
<p><span class="math display">$$\mathbf{P(}\mathbf{X}_{\mathbf{1}}\mathbf{,\ }\mathbf{\ldots}\mathbf{,\ }\mathbf{X}_{\mathbf{d}}\mathbf{\ |\ Y)\  = \ }\prod_{\mathbf{i = 1}}^{\mathbf{d}}\mathbf{P(X\_ i\ |\ Y)}\mathbf{\ }$$</span></p>
<ul>
<li><p>if <strong>conditional</strong> <strong>independence</strong> assumption <strong>holds</strong>, <strong>Naïve Bayes</strong> (NB) is an <strong>optimal</strong> <strong>classifier</strong> (but worse otherwise).</p></li>
</ul>
<p>has <strong>fewer</strong> <strong>parameters</strong>, so <strong>less</strong> <strong>training</strong> data even though <strong>assumption</strong> may be <strong>violated</strong></p>
<ul>
<li><p><strong>Bayes</strong> <strong>classifier</strong> with additional “<strong>naive</strong>” <strong>assumption</strong></p></li>
</ul>
<p><strong>features</strong> are <strong>independent</strong> given class:</p>
<p><span class="math display">$$\mathbf{P(}\mathbf{X}_{\mathbf{1}}\mathbf{,\ \ldots,\ }\mathbf{X}_{\mathbf{d}}\mathbf{\ |\ Y)\  = \ }\prod_{\mathbf{i = 1}}^{\mathbf{d}}\mathbf{P(X\_ i\ |\ Y)}$$</span></p>
<p><span class="math display"><strong>f</strong><sub><strong>N</strong><strong>B</strong></sub><strong>(</strong><strong>x</strong><strong>)</strong> <strong>=</strong> <strong>a</strong><strong>r</strong><strong>g</strong><strong>m</strong><strong>a</strong><strong>x</strong><sub><strong>y</strong></sub> <strong>P</strong><strong>(</strong><strong>x</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>.</strong><strong>.</strong><strong>.</strong><strong>,</strong> <strong>x</strong><sub><strong>d</strong></sub> <strong>|</strong> <strong>y</strong><strong>)</strong> <strong>P</strong><strong>(</strong><strong>y</strong><strong>)</strong></span></p>
<p><span class="math display">$$\mathbf{= \ argma}\mathbf{x}_{\mathbf{y}}\mathbf{\ }\prod_{\mathbf{i = 1}}^{\mathbf{d}}{\mathbf{P(}\mathbf{x}_{\mathbf{i}}\mathbf{\ |\ y)\ P(y)}}\mathbf{\ }$$</span></p></td>
</tr>
<tr>
<td><p>Parameters Needed for</p>
<p>Bernoulli Conditionals</p></td>
<td><ul>
<li><p>how many <strong>parameters</strong>?</p></li>
</ul>
<p><span class="math inline"><strong>K</strong> <strong>−</strong> <strong>1</strong></span> free parameters</p>
<p><span class="math display"><em>i</em><em>f</em> <strong>K</strong> <strong>l</strong><strong>a</strong><strong>b</strong><strong>e</strong><strong>l</strong><strong>s</strong></span></p>
<ul>
<li><p>class <strong>probabilities</strong>:</p></li>
</ul>
<p><span class="math display"><strong>Y</strong> <strong>∈</strong> <strong>{</strong><strong>1</strong><strong>,</strong> <strong>2</strong><strong>,</strong> <strong>.</strong><strong>.</strong><strong>.</strong><strong>,</strong> <strong>K</strong><strong>}</strong></span></p>
<p><span class="math display"><strong>P</strong><strong>(</strong><strong>Y</strong> <strong>=</strong> <strong>y</strong><strong>)</strong><strong>=</strong><strong>p</strong><sub><strong>y</strong></sub> <strong>f</strong><strong>o</strong><strong>r</strong> <strong>a</strong><strong>l</strong><strong>l</strong> <strong>y</strong></span></p>
<ul>
<li><p>class <strong>conditional</strong> <strong>distribution</strong> of features</p></li>
</ul>
<p><strong>linear</strong> instead of <strong>exponential</strong></p>
<p><strong>in d!</strong></p>
<p>(<strong>Naive</strong> <strong>Bayes</strong> <strong>assumption</strong>):</p>
<p><span class="math display"><strong>P</strong><strong>(</strong><strong>X</strong><sub><strong>i</strong></sub> <strong>=</strong> <strong>x</strong><sub><strong>i</strong></sub> <strong>|</strong> <strong>Y</strong> <strong>=</strong> <strong>y</strong><strong>)</strong></span></p></td>
</tr>
<tr>
<td>Naïve Bayes Algorithm: Discrete Features</td>
<td><ul>
<li><p><strong>training</strong> data:</p></li>
</ul>
<blockquote>
<p><span class="math inline">{ (<strong>x</strong><sup><strong>j</strong></sup><strong>,</strong> <strong>y</strong><sup><strong>j</strong></sup>)}<sub><strong>j</strong> <strong>=</strong> <strong>1</strong></sub><sup><strong>n</strong></sup>    </span> <span class="math inline"><strong>X</strong><sup><strong>j</strong></sup> <strong>=</strong> <strong>(</strong><strong>X</strong><sub><strong>1</strong></sub><sup><strong>j</strong></sup> <strong>,</strong> <strong>.</strong><strong>.</strong><strong>.</strong><strong>,</strong>  <strong>X</strong><sub><strong>d</strong></sub><sup><strong>j</strong></sup><strong>)</strong></span></p>
</blockquote>
<ul>
<li><p><strong>maximum</strong> liklihood <strong>estimates</strong></p>
<ul>
<li><p>class <strong>probability:</strong></p></li>
</ul></li>
</ul>
<blockquote>
<p><span class="math display">$$\mathbf{P(y)\  = \ }\frac{\mathbf{\#\{\ j\ :\ }\mathbf{Y}^{\mathbf{j}}\mathbf{\  = \ y\ \}\ }}{\mathbf{n}}\mathbf{\ }$$</span></p>
</blockquote>
<ul>
<li><p>class <strong>conditional</strong> <strong>distribution</strong>:</p></li>
</ul>
<blockquote>
<p><span class="math display">$$\frac{\mathbf{P(}\mathbf{x}_{\mathbf{i}}\mathbf{,\ y)}}{\mathbf{P(y)}}\mathbf{=}\frac{\mathbf{\#\{\ j\ :\ }\mathbf{X}_{\mathbf{i}}^{\mathbf{j}}\mathbf{=}\mathbf{x}_{\mathbf{i}}\mathbf{,\ }\mathbf{Y}^{\mathbf{j}}\mathbf{= y\ \}}}{\mathbf{\#\{\ j\ :\ }\mathbf{Y}^{\mathbf{j}}\mathbf{\  = \ y\ \}}}\mathbf{\ }$$</span></p>
</blockquote>
<ul>
<li><p><strong>Naive Bayes</strong> Prediction <strong>(</strong>Test Data)</p></li>
</ul>
<p><span class="math inline"><strong>2</strong><strong>K</strong><strong>d</strong></span> free parameters</p>
<p><span class="math display"><em>i</em><em>f</em> <strong>K</strong> <strong>l</strong><strong>a</strong><strong>b</strong><strong>e</strong><strong>l</strong><strong>s</strong></span></p>
<blockquote>
<p><span class="math display"><strong>X</strong> <strong>=</strong> <strong>(</strong><strong>x</strong><sub><strong>1</strong></sub><strong>,</strong>  <strong>.</strong><strong>.</strong><strong>.</strong><strong>,</strong>  <strong>x</strong><sub><strong>d</strong></sub><strong>)</strong></span></p>
<p><span class="math display">$$\mathbf{Y\  = \ argma}\mathbf{x}_{\mathbf{y}}\mathbf{\ P}\left( \mathbf{y} \right)\prod_{\mathbf{i = 1}}^{\mathbf{d}}\frac{\mathbf{\ P}\left( \mathbf{x}_{\mathbf{i}}\mathbf{,\ y} \right)}{\mathbf{P}\left( \mathbf{y} \right)}\mathbf{\ }$$</span></p>
</blockquote></td>
</tr>
<tr>
<td>Gaussian Conditionals</td>
<td><ul>
<li><p>how many parameters</p></li>
</ul>
<p><span class="math display"><strong>P</strong><strong>(</strong><strong>X</strong><sub><strong>i</strong></sub><strong>=</strong><strong>x</strong><sub><strong>i</strong></sub> <strong>|</strong> <strong>Y</strong> <strong>=</strong> <strong>y</strong><strong>)</strong> <strong>∼</strong> <strong>N</strong><strong>(</strong><strong>μ</strong><sub><strong>i</strong><strong>y</strong></sub><strong>,</strong> <strong>σ</strong><sub><strong>i</strong><strong>y</strong></sub><sup><strong>2</strong></sup><strong>)</strong></span></p>
<p><span class="math display"><strong>f</strong><strong>o</strong><strong>r</strong> <strong>e</strong><strong>a</strong><strong>c</strong><strong>h</strong> <strong>c</strong><strong>l</strong><strong>a</strong><strong>s</strong><strong>s</strong> <strong>y</strong><strong>a</strong><strong>n</strong><strong>d</strong> <strong>e</strong><strong>a</strong><strong>c</strong><strong>h</strong> <strong>f</strong><strong>e</strong><strong>a</strong><strong>t</strong><strong>u</strong><strong>r</strong><strong>e</strong> <strong>(</strong><strong>p</strong><strong>i</strong><strong>x</strong><strong>e</strong><strong>l</strong><strong>)</strong> <strong>i</strong><strong>.</strong></span></p></td>
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
<th colspan="2">Class Probability (putting it all together)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Class Conditional Distribution</td>
<td><p><span class="math display"><strong>P</strong>(<strong>Y</strong> <strong>=</strong> <strong>y</strong>)<strong>=</strong> <strong>p</strong><sub><strong>y</strong></sub><strong>F</strong><strong>r</strong><strong>e</strong><strong>e</strong> <strong>p</strong><strong>a</strong><strong>r</strong><strong>a</strong><strong>m</strong><strong>e</strong><strong>t</strong><strong>e</strong><strong>r</strong><strong>s</strong><strong>:</strong> <strong>K</strong> <strong>−</strong> <strong>1</strong></span></p>
<ul>
<li><p><strong>Gaussian</strong> <strong>Naïve</strong> <strong>Bayes</strong></p></li>
</ul>
<p><span class="math display"><strong>P</strong><strong>(</strong><strong>X</strong><sub><strong>i</strong></sub><strong>=</strong><strong>x</strong><sub><strong>i</strong></sub> <strong>|</strong> <strong>Y</strong> <strong>=</strong> <strong>y</strong><strong>)</strong> <strong>∼</strong> <strong>N</strong><strong>(</strong><strong>μ</strong><sub><strong>i</strong><strong>y</strong></sub><strong>,</strong> <strong>σ</strong><sub><strong>i</strong><strong>y</strong></sub><sup><strong>2</strong></sup><strong>)</strong></span></p>
<ul>
<li><p>for each <strong>class</strong> <span class="math inline"><strong>y</strong> </span>and each feature <span class="math inline"><strong>i</strong>:</span></p></li>
</ul>
<p><span class="math display"><strong>P</strong><strong>a</strong><strong>r</strong><strong>a</strong><strong>m</strong><strong>e</strong><strong>t</strong><strong>e</strong><strong>r</strong><strong>s</strong> <strong>p</strong><strong>e</strong><strong>r</strong> <strong>c</strong><strong>l</strong><strong>a</strong><strong>s</strong><strong>s</strong> <strong>−</strong> <strong>f</strong><strong>e</strong><strong>a</strong><strong>t</strong><strong>u</strong><strong>r</strong><strong>e</strong> <strong>p</strong><strong>a</strong><strong>i</strong><strong>r</strong><strong>:</strong> <strong>2</strong></span></p>
<p><span class="math display"><strong>T</strong><strong>o</strong><strong>t</strong><strong>a</strong><strong>l</strong> <strong>c</strong><strong>l</strong><strong>a</strong><strong>s</strong><strong>s</strong> <strong>−</strong> <strong>c</strong><strong>o</strong><strong>n</strong><strong>d</strong><strong>i</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong><strong>a</strong><strong>l</strong> <strong>p</strong><strong>a</strong><strong>r</strong><strong>a</strong><strong>m</strong><strong>e</strong><strong>t</strong><strong>e</strong><strong>r</strong><strong>s</strong><strong>:</strong> <strong>2</strong><strong>K</strong><strong>d</strong></span></p>
<ul>
<li><p>Total <strong>Number</strong> of <strong>Parameters</strong></p></li>
</ul>
<p><span class="math display">(<strong>K</strong> <strong>−</strong> <strong>1</strong>)<strong>+</strong> <strong>2</strong> <strong>K</strong> <strong>d</strong></span></p></td>
</tr>
<tr>
<td>Generative vs Naive Generative</td>
<td><ul>
<li><p><strong>Generative</strong> Model for <strong>Classification</strong></p></li>
</ul>
<p><span class="math display"><strong>P</strong><strong>(</strong><strong>X</strong><sub><strong>i</strong></sub> <strong>=</strong> <strong>x</strong><sub><strong>i</strong></sub> <strong>|</strong> <strong>Y</strong> <strong>=</strong> <strong>y</strong><strong>)</strong>      <strong>P</strong><strong>(</strong><strong>Y</strong> <strong>=</strong> <strong>y</strong><strong>)</strong></span></p>
<ul>
<li><p><strong>Naïve</strong> <strong>Bayes</strong> Algorithm</p></li>
</ul>
<p><span class="math display">$$\prod_{\mathbf{i = 1}}^{\mathbf{d}}{\mathbf{P(X\_ i\ |\ Y)}\mathbf{\ \ \ \ \ \ P(Y = y)}}$$</span></p></td>
</tr>
<tr>
<td>Case Study</td>
<td><ul>
<li><p>Classify <strong>e-mails</strong></p></li>
</ul>
<p><span class="math display"><strong>Y</strong> <strong>=</strong> <strong>{</strong>Spam<strong>,</strong>NotSpam<strong>}</strong></span></p>
<ul>
<li><p>Classify <strong>news</strong> <strong>articles</strong></p></li>
</ul>
<p><span class="math display"><strong>Y</strong><strong>=</strong>{topic of the article}</span></p>
<ul>
<li><p>Classify <strong>webpages<br />
</strong><span class="math display"><strong>Y</strong> <strong>=</strong> <strong>{</strong>Student<strong>,</strong>Professor<strong>,</strong>Project<strong>,</strong> <strong>…</strong> <strong>}</strong></span></p></li>
<li><p>What <strong>about</strong> the <strong>features</strong> <span class="math inline"><strong>X</strong></span>?</p></li>
</ul>
<p><span class="math display"><strong>T</strong><strong>h</strong><strong>e</strong> <strong>t</strong><strong>e</strong><strong>x</strong><strong>t</strong><strong>!</strong></span></p></td>
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
<th>Summary</th>
<th><ul>
<li><p>Optimal decision using Bayes classifier</p></li>
<li><p>Naïve Bayes classifier</p>
<ul>
<li><p>What’s the assumption</p></li>
<li><p>Why we use it</p></li>
<li><p>How do we learn it</p></li>
</ul></li>
<li><p>Gaussian NB</p>
<ul>
<li><p>Features are still conditionally independent</p></li>
<li><p>Each feature has a Gaussian distribution given class</p></li>
</ul></li>
<li><p>Text classification</p>
<ul>
<li><p>Bag-of-words model</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
