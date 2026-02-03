> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week04_notes.pdf](../DATA780_week04_notes.pdf)
> - DOCX: [DATA780_week04_notes.docx](DATA780_week04_notes.docx)

---

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Logistic Regression</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Overview</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>a machine learning task where we predict a real-valued output response given an input vector</p></li>
<li><p>linear and non-linear regression models</p></li>
<li><p>analytic (closed-form) solution to learn an optimal model from training data</p></li>
<li><p>gradient descent and stochastic gradient descent algorithms</p></li>
<li><p>model complexity and overfitting</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Readings</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p><a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf#page=157">https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf#page=157</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 28%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Async</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Logistic Regression</td>
<td></td>
</tr>
<tr>
<td>Definition</td>
<td colspan="2"><ul>
<li><p><strong>supervised</strong> <strong>learning</strong> technique used to <strong>train</strong> <strong>models</strong> for <strong>classification</strong> where <strong>y</strong> is <strong>categorical</strong></p></li>
<li><p>generally, <strong>links</strong> to a <strong>binary</strong> link<strong>;</strong> is <strong>x[a, b, c, …]</strong> <strong>likely</strong> to produce <strong>y</strong></p></li>
<li><p><strong>x ∈</strong> ℝ<strong>ᵈ ⇒ y ∈ {1, …, C}</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Fitting the Model</td>
<td colspan="2"><ul>
<li><p><strong>maximize</strong> the <strong>likelihood</strong> of <strong>y given x</strong></p></li>
<li><p><span class="math inline">$\mathbf{P}\mathbf{\ \hat{}\_}\mathbf{\theta}\mathbf{\ (}\mathbf{y}\mathbf{\  = \ 1\ |\ }\mathbf{x}\mathbf{)\  = \ }\mathbf{\sigma}\mathbf{(}\mathbf{\varphi}\mathbf{(}\mathbf{x}\mathbf{)ᵀ}\mathbf{\theta}\mathbf{)\  = \ }\frac{\mathbf{1}}{\mathbf{(1\  + \ exp( -}\mathbf{\varphi}\mathbf{(}\mathbf{x}\mathbf{)ᵀ}\mathbf{\theta}\mathbf{))}}\mathbf{\ \ }$</span></p></li>
<li><p>to <strong>maximize</strong> the likelihood by <strong>minimizing</strong> the <strong>negative</strong> <strong>log</strong> <strong>likelihood</strong> (<strong>NNL</strong>)</p></li>
<li><p><span class="math inline">$\mathbf{argmax}\mathbf{\_}\mathbf{\theta}\mathbf{\ \ \prod ᵢ}\mathbf{₌}\mathbf{₁ⁿ\ \ }\mathbf{P}\mathbf{\ \hat{}\_}\mathbf{\theta}\mathbf{(}\mathbf{y}\mathbf{ᵢ\ |\ }\mathbf{x}\mathbf{ᵢ)\  = \ }$</span></p></li>
</ul>
<blockquote>
<p><span class="math inline">$\mathbf{argmin\_\theta\  - \ }\frac{\mathbf{1}}{\mathbf{n}}\mathbf{\ \sum ᵢ}\mathbf{₌}\mathbf{₁ⁿ\ log\ P\hat{}\_\theta(yᵢ\ }\mathbf{\mid}\mathbf{\ xᵢ)}$</span> <strong>]</strong></p>
</blockquote>
<ul>
<li><p>putting the <strong>likelihood</strong> of <strong>y</strong> given <strong>x</strong> into <strong>terms</strong> of the <strong>regression</strong> model</p>
<ul>
<li><p>for <strong>y = 1</strong>, we need the <strong>probability</strong> of <strong>y = 1</strong> given <strong>x</strong> given by the <strong>sigmoid</strong> of the <strong>linear</strong> <strong>function</strong>: <strong>σ(θᵀxᵢ)</strong></p></li>
<li><p>for <strong>y = 0,</strong> we need the <strong>probability</strong> of <strong>y = 0</strong> given <strong>x</strong> is given by <strong>1 − σ(θᵀxᵢ)</strong></p></li>
<li><p>which <strong>implies</strong> an ‘<strong>if’</strong> <strong>statement</strong> in our algorithm</p></li>
<li><p>so, <span class="math inline">$\mathbf{\log}\mathbf{\ }\mathbf{p}\mathbf{\_}\mathbf{\theta}\mathbf{(}\mathbf{y}\mathbf{ᵢ\ |\ }\mathbf{x}\mathbf{ᵢ)\  = \ }\left\{ \begin{array}{r}
\mathbf{log\ \sigma(\theta ᵀxᵢ)} \\
\mathbf{\ log(1\  - \ \sigma(\theta ᵀxᵢ))}
\end{array} \right.\ $</span> <span class="math inline">$\binom{if\ yᵢ\  = \ 1}{\ if\ yᵢ\  = \ 0}$</span></p></li>
<li><p>utilizing <strong>indicator</strong> <strong>values</strong> as coefficients, we can effectively <strong>insert</strong> a Boolean ‘<strong>if’</strong> in the equation</p></li>
<li><p>so,<span class="math inline"><strong>log</strong> <strong>p</strong><sub><strong>θ</strong>(<strong>y</strong><strong>ᵢ</strong>  ∣  <strong>x</strong><strong>ᵢ</strong>)</sub><strong>=</strong></span></p></li>
</ul></li>
</ul>
<p><span class="math display">{<strong>y</strong><strong>ᵢ</strong> <strong>=</strong> <strong>1</strong>}<strong>log</strong> <strong>σ</strong>(<strong>θ</strong><strong>ᵀ</strong><strong>x</strong><strong>ᵢ</strong>)<strong>+</strong> </span></p>
<blockquote>
<p><span class="math display"><strong>1</strong>{<strong>y</strong><strong>ᵢ</strong> <strong>=</strong> <strong>0</strong>}<strong>log</strong> (<strong>1</strong> <strong>−</strong> <strong>σ</strong>(<strong>θ</strong><strong>ᵀ</strong><strong>x</strong><strong>ᵢ</strong>))</span></p>
<p>given <span class="math inline">$\left\{ \begin{array}{r}
\mathbf{1 =}\mathbf{1\ \ \ \ \ \ \ }\mathbf{if}\mathbf{\ }\mathbf{True}\mathbf{\ } \\
\mathbf{1 =}\mathbf{0\ \ \ \ \ \ \ }\mathbf{if}\mathbf{\ }\mathbf{False}
\end{array} \right.\ $</span></p>
</blockquote>
<ul>
<li><p>and finally, “after some algebra”, we conclude that</p></li>
</ul>
<p><span class="math display"><strong>arg</strong>  <strong>min</strong> <strong>₍</strong><strong>θ</strong><strong>₎</strong> <strong>−</strong> <strong>1</strong><strong>/</strong><strong>n</strong> <strong>∑</strong><strong>ᵢ</strong><strong>₌</strong><strong>₁</strong><strong>ⁿ</strong> <strong>(</strong> <strong>y</strong><strong>ᵢ</strong> <strong>φ</strong><strong>(</strong><strong>x</strong><strong>ᵢ</strong><strong>)</strong><strong>ᵀ</strong><strong>θ</strong> <strong>+</strong> <strong>log</strong> <strong>(</strong> <strong>σ</strong><strong>(</strong> <strong>−</strong><strong>φ</strong><strong>(</strong><strong>x</strong><strong>ᵢ</strong><strong>)</strong><strong>ᵀ</strong><strong>θ</strong> <strong>)</strong> <strong>)</strong> <strong>)</strong></span></p>
<p>is equivalent to minimizing a KL divergence known as the cross-<strong>entropy</strong> <strong>loss</strong></p>
<ul>
<li><p>this <strong>justifies</strong> the <strong>binary</strong> <strong>adjustment</strong> to the <strong>classification</strong> <strong>problem</strong></p></li>
</ul></td>
</tr>
</tbody>
</table>
