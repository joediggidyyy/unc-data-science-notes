---
generated_at_utc: 2026-03-08T23:56:06+00:00
generated_from: notes/Spring_2026/DATA780/Week06/docx/DATA780_week06_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week06_notes.pdf](../DATA780_week06_notes.pdf)
> - DOCX: [DATA780_week06_notes.docx](DATA780_week06_notes.docx)

---

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 6%" />
<col style="width: 34%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr>
<th>Neural Networks</th>
<th></th>
<th></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview (what we will cover)</td>
<td style="text-align: right;"><em>16 Feb 2026</em></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>modern neural networks</p>
<ol type="1">
<li><p>are not new</p></li>
<li><p>not all that different from previously discussed machine learning models</p></li>
<li><p>rely on function compositions to learn useful features</p></li>
<li><p>have a hierarchical architecture</p></li>
<li><p>employ non-linearities</p></li>
</ol></li>
<li><p>the building blocks of neural networks</p>
<ol type="1">
<li><p>units</p></li>
<li><p>layers</p></li>
<li><p>implemented using matrix operations</p></li>
</ol></li>
<li><p>pros and cons of neural networks</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Reading</td>
<td colspan="2" style="text-align: right;">Be prepared for substantial hybrid assignment for next week</td>
</tr>
<tr>
<td colspan="4"><p><a href="https://www.deeplearningbook.org/contents/mlp.html">https://www.deeplearningbook.org/contents/mlp.html</a>, Ch. 6: Deep Feedforward Networks</p>
<p><img src="generated_media\DATA780_week06_notes\media\image1.png" style="width:2.42542in;height:2.46826in" /></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Artificial Neural Networks</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Logistic Regression</p>
<p>(review)</p>
<p>https://tenor.com/search/im-rich-bitch-g</p>
<p><img src="generated_media\DATA780_week06_notes\media\image2.png" style="width:0.98542in;height:1.62917in" /></p>
<p>https://tenor.com/search/im-rich-bitch-g 2</p>
<p>https://tenor.com/search/im-rich-bitch-g 3</p></td>
<td><p><span class="math display"><strong>Pr</strong> (<strong>Y</strong> <strong>=</strong> <strong>1</strong> ∣ <strong>X</strong> <strong>=</strong> <strong>x</strong>)<strong>=</strong>(<strong>1</strong><strong>+</strong><strong>exp</strong> (<strong>−</strong><strong>x</strong><sup><strong>T</strong></sup><strong>β</strong>))<sup><strong>−</strong><strong>1</strong></sup></span></p>
<ul>
<li><p><strong>logistic</strong> <strong>regression</strong></p>
<ul>
<li><p><img src="generated_media\DATA780_week06_notes\media\image3.png" style="width:0.72986in;height:0.625in" />it’s <strong>statistics</strong>!</p></li>
<li><p>it has been around <strong>60</strong> <strong>years</strong></p></li>
<li><p>probably will <strong>not</strong> get you</p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>Pr</strong> [<strong>Y</strong> = <strong>1</strong> | <strong>X</strong> = <strong>x</strong>] = (<strong>1</strong> + <strong>exp</strong> (−<strong>f</strong>(<strong>x</strong>)<sup><strong>T</strong></sup> <strong>β</strong>))<sup>−<strong>1</strong></sup></span></p>
<ul>
<li><p><strong>logistic</strong> regression with <strong>neural</strong> <strong>network</strong> <strong>learned</strong> features</p>
<ul>
<li><p><img src="generated_media\DATA780_week06_notes\media\image4.png" style="width:0.74861in;height:0.63542in" /><strong>not</strong> <strong>statistics</strong>…</p></li>
<li><p>IS <strong>deep</strong> <strong>learning</strong></p></li>
<li><p>has <strong>ONLY</strong> been around <strong>50</strong> <strong>years</strong></p></li>
<li><p><strong><u>GET PAID</u>.</strong></p></li>
</ul></li>
</ul>
<p>Images by</p>
<p>ChatGPT 5.2</p></td>
</tr>
<tr>
<td colspan="2">Neural Networks Big Picture</td>
</tr>
<tr>
<td>Machine Learning Supervised Loss</td>
<td><ul>
<li><p><strong>supervised</strong> <strong>loss</strong>: a set of <strong>parameters</strong> that are typically <strong>operating</strong> <strong>linearly</strong> over <strong>input</strong> features</p></li>
</ul>
<p><span class="math display">$$\mathbf{argmi}\mathbf{n}_{\mathbf{\theta}}\sum_{\mathbf{i = 1}}^{\mathbf{N}}{\mathcal{l}_{\mathbf{\theta}}\left( \mathbf{x}_{\mathbf{i}}\mathbf{,\ }\mathbf{y}_{\mathbf{i}} \right)}$$</span></p></td>
</tr>
<tr>
<td>NN Supervised Loss</td>
<td><ul>
<li><p>still using a <strong>linear</strong> or similar <strong>sigmoid</strong> <strong>predictor</strong> over <strong>learnable</strong> features</p></li>
</ul>
<p><span class="math display">$$\mathbf{argmi}\mathbf{n}_{\mathbf{\theta,w}}\sum_{\mathbf{i = 1}}^{\mathbf{N}}{\mathcal{l}_{\mathbf{\theta}}\left( \mathbf{f}_{\mathbf{w}\left( \mathbf{x}_{\mathbf{i}} \right)}\mathbf{,\ }\mathbf{y}_{\mathbf{i}} \right)}$$</span></p>
<ul>
<li><p>there are <strong>additional</strong> <strong>parameters</strong> known as <strong>weights</strong> (<span class="math inline"><strong>ω</strong></span>) that we <strong>optimize</strong> over <strong>in</strong> <strong>addition</strong> to the linear <strong>features</strong></p></li>
<li><p>the <strong>weights</strong> <strong>determine</strong> the <strong>learnable</strong> <strong>features</strong></p></li>
<li><p>the <strong>number</strong> of <strong>output</strong> <strong>features</strong> will <strong>not</strong> necessarily <strong>coincide</strong> with the <strong>number</strong> of <strong>input</strong> features</p></li>
</ul>
<p><span class="math display"><strong>f</strong><sub><strong>ω</strong></sub>(<strong>x</strong>)<strong>:</strong> ℝ<sup><strong>d</strong></sup><strong>→</strong>ℝ<sup><strong>k</strong></sup></span></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr>
<th>NN Regression Loss</th>
<th><p><span class="math display">$$\mathbf{argmi}\mathbf{n}_{\mathbf{\theta}\mathbf{,}\mathbf{w}}\mathbf{\ }\sum_{\mathbf{i}\mathbf{= 1}}^{\mathbf{N}}{\mathbf{\theta}^{\mathbf{T}}\left( \mathbf{f}_{\mathbf{\omega}}\left( \mathbf{x}_{\mathbf{i}} \right)\mathbf{-}\mathbf{y}_{\mathbf{i}} \right)^{\mathbf{2}}}\mathbf{\ }$$</span></p>
<ul>
<li><p>key ingredients</p>
<ul>
<li><p>nonlinear</p></li>
<li><p>hierarchical</p></li>
<li><p>universal</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Non-Linear Mappings</td>
</tr>
<tr>
<td>Linear Mapping</td>
<td><p><span class="math display"><strong>ŷ</strong><sub><strong>θ</strong></sub>(<strong>x</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>x</strong><sub><strong>2</strong></sub>)<strong>=</strong> <strong>θ</strong><sub><strong>1</strong></sub><strong>x</strong><sub><strong>1</strong></sub><strong>+</strong> <strong>θ</strong><sub><strong>2</strong></sub><strong>x</strong><sub><strong>2</strong></sub><strong>+</strong> <strong>θ</strong><sub><strong>0</strong></sub></span></p>
<p>Linear Mapping</p>
<ul>
<li><p><img src="generated_media\DATA780_week06_notes\media\image5.png" style="width:1.77083in;height:1.36092in" />many <strong>standard</strong> <strong>learning</strong> methods, such as <strong>ordinary</strong> <strong>least</strong> <strong>squares</strong> regression and <strong>logistic</strong> regression, are <strong>formulated</strong> as a <strong>linear</strong> <strong>map</strong> in the <strong>input</strong> space</p></li>
<li><p>this is <strong>adequate</strong> your <strong>goal</strong> is to <strong>map</strong> a <strong>boundary</strong> line <strong>between</strong> <strong>classes</strong></p></li>
</ul>
<p>ChatGPT 5.2</p></td>
</tr>
<tr>
<td>Non-Linear Mapping</td>
<td><p><span class="math display">$$\mathbf{ŷ}_{\mathbf{\theta}}\left( \mathbf{x}_{\mathbf{1}}\mathbf{,\ }\mathbf{x}_{\mathbf{2}} \right)\mathbf{= \ }\sum_{\mathbf{j = 1}}^{\mathbf{k}}{\mathbf{\theta}_{\mathbf{j}}\mathbf{f}_{\mathbf{j}}\left( \mathbf{x}_{\mathbf{1}}\mathbf{,\ }\mathbf{x}_{\mathbf{2}} \right)}$$</span></p>
<ul>
<li><p><img src="generated_media\DATA780_week06_notes\media\image6.png" style="width:1.77083in;height:1.36042in" />these <strong>methods</strong> can be <strong>extended</strong> to a <strong>linear</strong> <strong>map</strong> in a <strong>nonlinear</strong> <strong>space</strong></p></li>
</ul>
<p>Non-Linear Mapping</p>
<ul>
<li><p>one perspective of what <strong>neural</strong> <strong>networks</strong> are doing is that they are <strong>learning</strong> a <strong>set</strong> of <span class="math inline"><strong>k</strong></span> <strong>features</strong> that can be <strong>linearly</strong> <strong>combined</strong> <strong>calculate</strong> an <strong>output</strong></p></li>
</ul>
<p>ChatGPT 5.2</p></td>
</tr>
<tr>
<td colspan="2">Hierarchal Features</td>
</tr>
<tr>
<td>“Stacking” Features</td>
<td><ul>
<li><p>one aspect that add to a <strong>neural</strong> <strong>network’s</strong> <strong>usefulness</strong> is that we can <strong>build</strong> <strong>features</strong> on top of features <strong>iteratively</strong> forming a <strong>hierarchical</strong> feature <strong>map</strong></p></li>
<li><p>we can combine simple features to derive more complicated feature sets</p></li>
<li><p>this adds rich <strong>semantic</strong> <strong>meaning</strong> into calculated <strong>output</strong> features</p></li>
</ul></td>
</tr>
<tr>
<td>One Layer</td>
<td><ul>
<li><p>a <strong>single</strong> <strong>layer</strong> transforms <strong>input</strong> features to <strong>output</strong> features</p></li>
</ul>
<p>the dimensions of the input vector does not have to match the dimensions of the output vector</p>
<p><span class="math display">ℝ<sup><em>s</em></sup> ↦ ℝ<sup><em>s</em><sup>′</sup></sup></span></p>
<p><span class="math display">$$\binom{\mathbf{x}}{\begin{array}{r}
input \\
features
\end{array}} \Rightarrow \binom{\mathbf{x}^{\mathbf{'}}}{\begin{array}{r}
output \\
features
\end{array}}$$</span></p></td>
</tr>
<tr>
<td>Two Layers</td>
<td><ul>
<li><p>in a <strong>two</strong>-<strong>layer</strong> <strong>NN</strong>, the <strong>output</strong> from the <strong>previous</strong> layer becomes the <strong>input</strong> for the <strong>next</strong> layer</p></li>
</ul>
<p><span class="math display">$$\binom{\mathbf{x}}{\begin{array}{r}
input \\
features
\end{array}} \Rightarrow \binom{\mathbf{x}^{\mathbf{'}}}{\begin{array}{r}
output \\
features
\end{array}} \Rightarrow \binom{\mathbf{x}^{\mathbf{''}}}{\begin{array}{r}
output \\
features
\end{array}}$$</span></p>
<p>Two-Layer Neural Network</p>
<p><img src="generated_media\DATA780_week06_notes\media\image7.png" style="width:2.68056in;height:1.96875in" /></p>
<p>ChatGPT 5.2</p></td>
</tr>
<tr>
<td>Features of Features</td>
<td><ul>
<li><p>this builds a <strong>function</strong> of <strong>nested</strong> <strong>functions</strong></p></li>
</ul>
<p><span class="math display"><strong>f</strong><sub><strong>w</strong></sub><strong>(</strong><strong>x</strong><strong>)</strong> <strong>=</strong> <strong>f</strong><sub><strong>w</strong><sub><strong>m</strong></sub></sub><sup><strong>m</strong></sup> <strong>(</strong><strong>…</strong><strong>f</strong><sub><strong>w</strong><sub><strong>2</strong></sub></sub><sup><strong>2</strong></sup><strong>(</strong> <strong>f</strong><sub><strong>w</strong><sub><strong>1</strong></sub></sub><sup><strong>1</strong></sup><strong>(</strong><strong>x</strong><strong>)</strong> <strong>)</strong><strong>…</strong><strong>)</strong></span></p>
<ul>
<li><p><strong>alternate</strong> notation</p></li>
</ul>
<p><span class="math display"><strong>f</strong><sub><strong>w</strong></sub>(<strong>x</strong>) <strong>=</strong> <strong>(</strong> <strong>f</strong><sub><strong>w</strong><sub><strong>m</strong></sub></sub><sup><strong>m</strong></sup> <strong>∘</strong> <strong>.</strong><strong>.</strong><strong>.</strong> <strong>∘</strong> <strong>f</strong><sub><strong>w</strong><sub><strong>2</strong></sub></sub><sup><strong>2</strong></sup> <strong>∘</strong> <strong>f</strong><sub><strong>w</strong><sub><strong>1</strong></sub></sub><sup><strong>1</strong></sup> <strong>)</strong><strong>(</strong><strong>x</strong><strong>)</strong></span></p></td>
</tr>
<tr>
<td colspan="2">Building Blocks</td>
</tr>
<tr>
<td>Function Composition</td>
<td><ul>
<li><p>simply stacking linear functions can become problematic</p></li>
<li><p>e.g. <strong>combining</strong> nested <strong>linear</strong> <strong>equations</strong> that <strong>result</strong> in a <strong>linear</strong> equation is <strong>not</strong> <strong>helpful</strong>:</p></li>
</ul>
<p><span class="math display"><strong>f</strong> <strong>=</strong> <strong>w</strong><strong>x</strong> <strong>+</strong> <strong>b</strong><strong>=</strong><strong>w</strong><sup><strong>3</strong></sup>(<strong>w</strong><sup><strong>2</strong></sup>(<strong>w</strong><sup><strong>1</strong></sup><strong>x</strong><strong>+</strong><strong>b</strong><sup><strong>1</strong></sup>)<strong>+</strong><strong>b</strong><sup><strong>2</strong></sup>)<strong>+</strong><strong>b</strong><sup><strong>3</strong></sup></span></p>
<ul>
<li><p>the “fix” is to <strong>add</strong> an <strong>addition</strong> <strong>function</strong> which we call a <strong>non</strong>-<strong>linearity</strong> <span class="math inline"><strong>r</strong></span> that takes the <strong>output</strong> of the <strong>linear</strong> <strong>function</strong> to <strong>apply</strong> an <strong>element</strong>-<strong>wise</strong> <strong>non</strong>-<strong>linearity</strong> as shown in the previous section:</p></li>
</ul>
<p><strong>(</strong>can take other <strong>non-linear</strong> forms<strong>)</strong></p>
<p><span class="math inline">( <strong>f</strong><sub><strong>w</strong><sub><strong>m</strong></sub></sub><sup><strong>m</strong></sup> <strong>∘</strong> <strong>…</strong> <strong>∘</strong> <strong>f</strong><sub><strong>w</strong><sub><strong>2</strong></sub></sub><sup><strong>2</strong></sup> <strong>∘</strong> <strong>f</strong><sub><strong>w</strong><sub><strong>1</strong></sub></sub><sup><strong>1</strong></sup> )(<strong>x</strong>)   </span><img src="generated_media\DATA780_week06_notes\media\image8.png" style="width:0.47674in;height:0.35747in" alt="Check Mark Transparent Images – Browse ..." /></p>
<p><img src="generated_media\DATA780_week06_notes\media\image9.png" style="width:4.66732in;height:2.09404in" /></p>
<p><span class="math display"><em>o</em><em>u</em><em>t</em><em>p</em><em>u</em><em>t</em><em>s</em>  ∈ ℝ</span></p>
<p>ChatGPT 5.2</p>
<p><span class="math display">$$\mathbf{b\  + \ }\sum_{\mathbf{i = 1}}^{\mathbf{n}}{\mathbf{x}_{\mathbf{i}}\mathbf{\ }\mathbf{w}_{\mathbf{i}}}\mathbf{\ }$$</span></p>
<p><strong>linear</strong> combination (dot product)</p>
<p><span class="math display"> ∈ ℝ<sup><em>s</em>()</sup></span></p>
<p><span class="math display"> ∈ ℝ<sup><em>s</em>() × <em>s</em>( − 1)</sup></span></p>
<p><span class="math inline"> ∈ ℝ<sup><em>s</em>()</sup></span> <span class="math inline"> ∈ ℝ<sup><em>s</em>( − 1)</sup></span></p></td>
</tr>
<tr>
<td>Matrix Notation</td>
<td><p><span class="math display"><strong>L</strong><strong>a</strong><strong>y</strong><strong>e</strong><strong>r</strong> −<strong>1</strong> <strong>→</strong> <strong>L</strong><strong>a</strong><strong>y</strong><strong>e</strong><strong>r</strong></span></p>
<p><span class="math display">$${\overrightarrow{\mathbf{\varphi}}}^{\mathbf{(}\mathcal{l}\mathbf{)}}\mathbf{= \sigma(\ }\mathbf{W}^{\mathcal{l}}\mathbf{\ }{\overrightarrow{\mathbf{\varphi}}}^{\mathbf{(}\mathcal{l -}\mathbf{1}\mathbf{)}}\mathbf{\  +}\overrightarrow{\mathbf{b}^{\mathbf{(}\mathcal{l}\mathbf{)}}}\mathbf{)}$$</span></p>
<p><strong>expanded form:</strong></p>
<p><span class="math display">$$\begin{bmatrix}
\mathbf{\varphi}_{\mathbf{1}}^{\mathcal{l}} \\
\mathbf{\varphi}_{\mathbf{2}}^{\mathcal{l}} \\
\begin{matrix}
\mathbf{.} \\
\mathbf{.}
\end{matrix}
\end{bmatrix}\mathbf{=}\mathbf{\sigma}\left( \genfrac{[}{]}{0pt}{}{\begin{matrix}
\mathbf{- w}_{\mathbf{1}}^{\mathcal{l}}\mathbf{-} \\
\mathbf{- w}_{\mathbf{2}}^{\mathcal{l}}\mathbf{-}
\end{matrix}}{\begin{array}{r}
\mathbf{.} \\
\mathbf{.}
\end{array}}\mathbf{\ }\begin{bmatrix}
\begin{matrix}
{\overrightarrow{\mathbf{\varphi}}}_{\mathbf{1}}^{\left( \mathcal{l -}\mathbf{1} \right)} \\
{\overrightarrow{\mathbf{\varphi}}}_{\mathbf{2}}^{\left( \mathcal{l -}\mathbf{1} \right)} \\
\mathbf{.}
\end{matrix} \\
\mathbf{.}
\end{bmatrix}\mathbf{+}\begin{bmatrix}
\begin{matrix}
\mathbf{b}_{\mathbf{1}}^{\mathcal{l}} \\
\mathbf{b}_{\mathbf{2}}^{\mathcal{l}} \\
\mathbf{.}
\end{matrix} \\
\mathbf{.}
\end{bmatrix} \right)\mathbf{\ }\mathbf{\ }\mathbf{=}\left\lbrack \begin{array}{r}
\mathbf{\sigma}\left( \mathbf{W}^{\mathcal{l}}\mathbf{(}\overrightarrow{\mathbf{\varphi}^{\mathcal{l}\mathbf{- 1}}}\mathbf{+}\mathbf{b}_{\mathbf{1}}^{\mathcal{l}} \right) \\
\mathbf{.} \\
\mathbf{.} \\
\mathbf{.}\mathbf{\ }
\end{array} \right\rbrack$$</span></p>
<p>network with one hidden layer</p>
<p><span class="math display">$$\mathbf{\sigma}\mathbf{(}\mathbf{W}^{\left( \mathbf{1} \right)}\mathbf{x + \ }\overrightarrow{\mathbf{b}^{\left( \mathbf{1} \right)}}\mathbf{)}$$</span></p>
<p>regression loss for network with two hidden layers</p>
<p>and a linear output layer</p>
<p><span class="math display">(<strong>f</strong>(<strong>x</strong>)<strong>−</strong> <strong>y</strong>)<sup><strong>2</strong></sup><strong>=</strong> </span></p>
<p><span class="math display">$$\left( \mathbf{\ }\mathbf{W}^{\mathbf{(3)}}\mathbf{\sigma}\left( \mathbf{\ }\mathbf{W}^{\mathbf{(2)}}\mathbf{\sigma}\left( \mathbf{\ }\mathbf{W}^{\mathbf{(1)}}\mathbf{x\  + \ }\overrightarrow{\mathbf{b}^{\mathbf{(1)}}} \right)\mathbf{+ \ }\overrightarrow{\mathbf{b}^{\mathbf{(2)}}} \right)\mathbf{+ \ }\overrightarrow{\mathbf{b}^{\mathbf{(3)}}}\mathbf{- \ }\mathbf{y}^{\mathbf{2}}\mathbf{\ } \right)^{\mathbf{2}}$$</span></p></td>
</tr>
<tr>
<td>Non-linearities</td>
<td><ul>
<li><p>when we <strong>compute</strong> <strong>gradients</strong>, we multiply by the <strong>derivatives</strong> of the <strong>activation</strong> <strong>functions</strong></p></li>
<li><p>for <strong>saturated</strong> <strong>units</strong>—those receiving very <strong>large</strong> <strong>positive</strong> or very <strong>large</strong> <strong>negative</strong> inputs—the <strong>slope</strong> of the <strong>activation</strong> function is <strong>close</strong> to <strong>zero</strong></p></li>
<li><p>because the <strong>derivative</strong> is <strong>near</strong> <strong>zero</strong>, the <strong>gradient</strong> becomes very <strong>small</strong></p></li>
<li><p>as a result, <strong>weight</strong> <strong>updates</strong> during <strong>gradient</strong> <strong>descent</strong> are <strong>minimal</strong>, and learning <strong>slows</strong> <strong>down</strong> significantly</p></li>
</ul>
<p><img src="generated_media\DATA780_week06_notes\media\image10.png" style="width:2.74931in;height:1.84514in" /></p>
<p>“vanishing gradients”</p>
<ul>
<li><p>to <strong>resolve</strong> <strong>vanishing</strong> <strong>gradients</strong>, non-linearities such as the <strong>ReLU</strong> or <strong>rectified</strong> <strong>linear</strong> <strong>unit</strong> have been used</p></li>
<li><p>although the <strong>ReLU</strong> is a <strong>simple</strong> function, it is <strong>non</strong>-<strong>linear</strong> (piece-wise linear)</p></li>
<li><p><strong>other</strong> non-linear <strong>functions</strong> such as <strong>Leaky</strong> <strong>ReLU</strong> (ReLU with <strong>non</strong>-<strong>zero</strong> resolution of <strong>negative</strong> values) and <strong>other piece-wise functions</strong></p></li>
</ul>
<p><img src="generated_media\DATA780_week06_notes\media\image11.png" style="width:3.45544in;height:2.20658in" /></p>
<p>ChatGPT 5.2</p>
<p><img src="generated_media\DATA780_week06_notes\media\image12.png" style="width:3.45544in;height:1.93577in" /></p>
<p>ChatGPT 5.2</p></td>
</tr>
<tr>
<td></td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr>
<th>Live Session Notes</th>
<th style="text-align: right;">16 Feb 2026</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><ul>
<li><p>Be prepared for substantial hybrid assignment for next week</p></li>
</ul>
<p><strong>BINARY CROSS ENTROPY (BCE)</strong></p>
<p><strong>Mathematical explanation</strong><br />
<em><strong>To get from the Binary Cross-Entropy formula to the Softplus version in the code, we substitute the sigmoid function</strong></em></p>
<p><span class="math display">$$\sigma(z) = \frac{1}{1 + e^{- z}}
$$</span><em><strong>into the loss equation and simplify.</strong></em></p>
<ul>
<li><p>HW02 is due 18 Feb</p></li>
</ul>
<p>thank you Gerhard!</p>
<ul>
<li><p>review BCE for this assignment</p></li>
<li><p>attn: data mining and machine learning. pg 623</p></li>
</ul>
<p><span class="math display">$$\mathbf{L}\mathbf{OSS\  = \ neg}\left( \mathbf{log\ likelihood} \right)\mathbf{E}\mathbf{0,1,L}\left( \mathbf{\theta} \right)\mathbf{-}\prod_{\mathbf{i}}^{}{}_{}\mathbf{p}\left( \mathbf{y}_{\mathbf{i}} \middle| \mathbf{x}_{\mathbf{i}}\mathbf{,}\mathbf{\theta} \right)$$</span></p>
<p><span class="math display"><strong>l</strong><strong>o</strong><strong>g</strong><strong>L</strong>(<strong>θ</strong>)<strong>=</strong><strong>E</strong><sub><strong>i</strong></sub><strong>l</strong><strong>o</strong><strong>g</strong><strong>P</strong>(<strong>y</strong><sub><strong>i</strong></sub>|<strong>x</strong><sub><strong>i</strong></sub><strong>,</strong><strong>θ</strong>)</span></p>
<p><span class="math display"><strong>m</strong><strong>i</strong><strong>n</strong> <strong>−</strong> <strong>l</strong><strong>o</strong><strong>s</strong><strong>s</strong> <strong>↔</strong><strong>m</strong><strong>i</strong><strong>n</strong><strong>(</strong><strong>n</strong><strong>e</strong><strong>g</strong><strong>(</strong><strong>l</strong><strong>o</strong><strong>g</strong> <strong>−</strong> <strong>l</strong><strong>i</strong><strong>k</strong><strong>e</strong><strong>l</strong><strong>i</strong><strong>h</strong><strong>o</strong><strong>o</strong><strong>d</strong><strong>)</strong> <strong>=</strong> <strong>n</strong><strong>e</strong><strong>g</strong><strong>(</strong><strong>m</strong><strong>a</strong><strong>x</strong><strong>(</strong><strong>l</strong><strong>o</strong><strong>g</strong> <strong>−</strong> <strong>l</strong><strong>i</strong><strong>k</strong><strong>e</strong><strong>l</strong><strong>i</strong><strong>h</strong><strong>o</strong><strong>d</strong><strong>)</strong></span></p>
<p>for a single sample with true label y E ???</p>
<p>and predicted probabliltiy p</p>
<p>if y=1: we want max(P(y=1|x))=p</p>
<p>if y=0: we want max(P(y=0|x)-1-p</p>
<p>'one could also use'</p>
<p><img src="generated_media\DATA780_week06_notes\media\image13.png" style="width:2.51875in;height:1.00694in" /></p>
<ul>
<li><p><a href="https://playground.tensorflow.org/#activation=tanh&amp;batchSize=10&amp;dataset=">https://playground.tensorflow.org/#activation=tanh&amp;batchSize=10&amp;dataset=</a></p></li>
</ul>
<blockquote>
<p>circle&amp;regDataset=reg-lane&amp;learningRate=0.03&amp;regularizationRate=0&amp;noise=</p>
<p>0&amp;networkShape=4,2&amp;seed=0.02680&amp;showTestData=false&amp;discretize=</p>
<p>false&amp;percTrainData=50&amp;x=true&amp;y=true&amp;xTimesY=false&amp;xSquared=</p>
<p>false&amp;ySquared=false&amp;cosX=false&amp;sinX=false&amp;cosY=false&amp;sinY=</p>
<p>false&amp;collectStats=false&amp;problem=classification&amp;initZero=false&amp;hideText=false</p>
</blockquote>
<ul>
<li><p>The <a href="https://arxiv.org/abs/1412.6980">Adam (Adaptive Moment Estimation) optimizer</a> is a popular, efficient gradient-based optimization algorithm used to train deep learning models by combining the advantages of <a href="https://www.google.com/search?q=Momentum&amp;rlz=1C1CHBF_enUS1175US1175&amp;oq=adam+optimizer&amp;gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDUyNjNqMGo3qAIIsAIB8QXEd9i4WLQbZQ&amp;sourceid=chrome&amp;ie=UTF-8&amp;ved=2ahUKEwjWvc3Bnt-SAxVUQjABHYdsBHoQgK4QegQIARAF">Momentum</a> and <a href="https://www.google.com/search?q=RMSprop&amp;rlz=1C1CHBF_enUS1175US1175&amp;oq=adam+optimizer&amp;gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDUyNjNqMGo3qAIIsAIB8QXEd9i4WLQbZQ&amp;sourceid=chrome&amp;ie=UTF-8&amp;ved=2ahUKEwjWvc3Bnt-SAxVUQjABHYdsBHoQgK4QegQIARAG">RMSprop</a>.</p></li>
</ul>
<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr>
<th colspan="2">General Steps to Build a Neural Network: TensorFlow</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Step Description</td>
</tr>
<tr>
<td><ol type="1">
<li><p>Import Libraries</p></li>
</ol></td>
<td>Import TensorFlow and helper packages.</td>
</tr>
<tr>
<td><ol start="2" type="1">
<li><p>Prepare the Data</p></li>
</ol></td>
<td>Load, clean, normalize, and split into train/test sets.</td>
</tr>
<tr>
<td><ol start="3" type="1">
<li><p>Define the Model</p></li>
</ol></td>
<td>Use Sequential or Functional API (e.g., Input → Dense).</td>
</tr>
<tr>
<td><ol start="4" type="1">
<li><p>Compile the Model</p></li>
</ol></td>
<td>Set optimizer, loss function, and metrics.</td>
</tr>
<tr>
<td><ol start="5" type="1">
<li><p>Train the Model</p></li>
</ol></td>
<td>Use model.fit() with epochs and batch size.</td>
</tr>
<tr>
<td><ol start="6" type="1">
<li><p>Evaluate the Model</p></li>
</ol></td>
<td>Use model.evaluate() on test data.</td>
</tr>
<tr>
<td><ol start="7" type="1">
<li><p>Make Predictions</p></li>
</ol></td>
<td>Use model.predict() on new/unseen data.</td>
</tr>
</tbody>
</table>
<ul>
<li><p>(comprehensive!) project proposal feedback has been sent out</p>
<ul>
<li><p>suggested references have been provided</p>
<ul>
<li><p>when perusing suggested references (Google Scholar), check at least one paper cited by that publication</p></li>
<li><p>focus on the methodology and reporting techniques</p></li>
</ul></li>
</ul></li>
<li><p>be sure to mark the ‘completed by’ on CW assignments</p>
<ul>
<li><p>coming up</p></li>
<li><p>week 7</p>
<ul>
<li><p>neural networks 2</p></li>
</ul></li>
<li><p>week 8</p>
<ul>
<li><p>cross-validation</p></li>
<li><p><em>midway report</em></p>
<ul>
<li><p>four page .pdf</p></li>
<li><p>NeruIPS-style files w/ overleaf template</p></li>
</ul></li>
<li><p>MIDTERM!!!</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;"><p>part 1</p>
<ul>
<li><p>questionnaire</p>
<ul>
<li><p>multiple choice</p></li>
<li><p>free response</p></li>
</ul></li>
<li><p>study guide provided in week 7</p></li>
<li><p>closed notes</p></li>
<li><p>“optional questions” (extra credit?)</p></li>
</ul></td>
<td style="text-align: center;"><p><strong>part 2</strong></p>
<ul>
<li><p>applied problems</p>
<ul>
<li><p><strong>long notebook</strong></p></li>
<li><p><strong>short sections</strong></p></li>
<li><p>NO AGENTS!</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>
