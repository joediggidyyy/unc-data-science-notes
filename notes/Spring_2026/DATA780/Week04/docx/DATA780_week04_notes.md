---
generated_at_utc: 2026-02-11T05:13:43+00:00
generated_from: notes/Spring_2026/DATA780/Week04/docx/DATA780_week04_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
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
<tr>
<td colspan="2">Fitting the Modes</td>
<td></td>
</tr>
<tr>
<td>Logistic Regression Model</td>
<td colspan="2"><ul>
<li><p><span class="math inline">$\mathbf{P}_{\mathbf{\theta}}\left( \mathbf{y = 1}\mid\mathbf{x} \right)\mathbf{=}\mathbf{\sigma}\left( \mathbf{\phi}\left( \mathbf{x} \right)^{\mathbf{T}}\mathbf{\theta} \right)\mathbf{=}\frac{\mathbf{1}}{\mathbf{1 +}\mathbf{ex}\mathbf{p}\left( \mathbf{-}\mathbf{\phi}\left( \mathbf{x} \right)^{\mathbf{T}}\mathbf{\theta} \right)}$</span></p></li>
</ul>
<p><img src="generated_media\DATA780_week04_notes\media\image1.png" style="width:1.89928in;height:1.91667in" /></p></td>
</tr>
<tr>
<td>Maximize the Likelihood</td>
<td colspan="2"><ul>
<li><p>as before, we <strong>maximize</strong> the <strong>likelihood</strong> of our data <strong>by</strong> <strong>minimizing</strong> the <strong>negative</strong> <strong>log</strong> <strong>likelihood</strong></p></li>
<li><p><span class="math inline">$\mathbf{argmax}_{\mathbf{\theta}}{\prod_{\mathbf{i = 1}}^{\mathbf{n}}{\widehat{\mathbf{P}_{\mathbf{\theta}}}\left( \mathbf{y}_{\mathbf{i}}\mid\mathbf{x}_{\mathbf{i}} \right)}}$</span> <span class="math inline">$\mathbf{=}\mathbf{\ \ \ \ \ \ \ \ \ \ \ \ \ }{\mathbf{ar}\mathbf{g}\mathbf{m}\mathbf{in}}_{\mathbf{\theta}}\mathbf{-}\frac{\mathbf{1}}{\mathbf{n}}\sum_{\mathbf{i = 1}}^{\mathbf{n}}{\mathbf{lo}\mathbf{g}{\widehat{\mathbf{P}_{\mathbf{\theta}}}\left( \mathbf{y}_{\mathbf{i}}\mid\mathbf{x}_{\mathbf{i}} \right)}}$</span></p></li>
</ul></td>
</tr>
<tr>
<td>(Average) Negative Log Likelihood</td>
<td colspan="2"><ul>
<li><p><span class="math inline">$\mathbf{\ }\mathbf{log}\mathbf{p}_{\mathbf{\theta}}\mathbf{(}\mathbf{y}_{\mathbf{i}}\mathbf{\mid}\mathbf{x}_{\mathbf{i}}\mathbf{) =}\left\{ \begin{array}{r}
\mathbf{log}\mathbf{\sigma}\mathbf{(}\mathbf{\theta}^{\mathbf{T}}\mathbf{x}_{\mathbf{i}}\mathbf{)} \\
\mathbf{log(1 - \sigma(}\mathbf{\theta}^{\mathbf{T}}\mathbf{x}_{\mathbf{i}}\mathbf{))}
\end{array} \right.\ \binom{\mathbf{y}_{\mathbf{i}}\mathbf{= 1}}{\mathbf{y}_{\mathbf{i}}\mathbf{= 0}}$</span></p></li>
<li><p><strong>to optimize according to “if statements” as above:</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{l}\mathbf{og}\mathbf{p}_{\mathbf{\theta}}\mathbf{\ }\mathbf{(}\mathbf{y}_{\mathbf{i}}\mathbf{\mid}\mathbf{x}_{\mathbf{i}}\mathbf{) =}\mathbf{IF}\textit{\textbf{\{}}\mathbf{y}_{\mathbf{i}}\mathbf{= 1}\textit{\textbf{\}}}\mathbf{\,}\mathbf{lo}\mathbf{g}{\mathbf{\sigma}\left( \mathbf{\theta}^{\mathbf{T}}\mathbf{x}_{\mathbf{i}} \right)}$$</span></p>
<p><span class="math display">$$\mathbf{+ \ }\mathbf{IF}\textit{\textbf{\{}}\mathbf{y}_{\mathbf{i}}\mathbf{= 0}\textit{\textbf{\}}}\mathbf{\,\ }\mathbf{log}\mathbf{(1 -}\mathbf{\sigma}\mathbf{(}\mathbf{\theta}^{\mathbf{T}}\mathbf{x}_{\mathbf{i}}\mathbf{))}$$</span></p>
<p><span class="math inline">                    <strong>=</strong><strong>y</strong><sub><strong>i</strong></sub> <strong>log</strong> <strong>σ</strong><strong>(</strong><strong>θ</strong><sup><strong>T</strong></sup><strong>x</strong><sub><strong>i</strong></sub><strong>)</strong> <strong>+</strong> <strong>(</strong><strong>1</strong><strong>−</strong><strong>y</strong><sub><strong>i</strong></sub><strong>)</strong><strong>log</strong> <strong>(</strong><strong>1</strong><strong>−</strong><strong>σ</strong><strong>(</strong><strong>θ</strong><sup><strong>T</strong></sup><strong>x</strong><sub><strong>i</strong></sub><strong>)</strong></span><strong>)</strong></p></td>
</tr>
<tr>
<td colspan="2">Minimizing the Loss</td>
<td></td>
</tr>
<tr>
<td>Logistic Loss Function</td>
<td colspan="2"><ul>
<li><p><strong>average KL divergence</strong> (simplified)</p></li>
</ul>
<p><span class="math display">$${\mathbf{ar}\mathbf{g}\mathbf{m}\mathbf{in}}_{\mathbf{\theta}}\mathbf{-}\frac{\mathbf{1}}{\mathbf{n}}\sum_{\mathbf{i = 1}}^{\mathbf{n}}\left( \mathbf{y}_{\mathbf{i}}\mathbf{lo}\mathbf{g}{\mathbf{\sigma}\left( \mathbf{\phi}\left( \mathbf{x}_{\mathbf{i}} \right)^{\mathbf{T}}\mathbf{\theta} \right)}\mathbf{+}\mathbf{lo}\mathbf{g}{\mathbf{\sigma}\left( \mathbf{-}\mathbf{\phi}\left( \mathbf{x}_{\mathbf{i}} \right)^{\mathbf{T}}\mathbf{\theta} \right)} \right)$$</span></p>
<ul>
<li><p>take <strong>derivative</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{\nabla}_{\mathbf{\theta}}\mathbf{L}\left( \mathbf{\theta} \right)\mathbf{= -}\frac{\mathbf{1}}{\mathbf{n}}\sum_{\mathbf{i = 1}}^{\mathbf{n}}\left( \mathbf{y}_{\mathbf{i}}\mathbf{\nabla}_{\mathbf{\theta}}\mathbf{\sigma}\left( \mathbf{\phi}\left( \mathbf{x}_{\mathbf{i}} \right)^{\mathbf{T}}\mathbf{\theta} \right)\mathbf{+}\mathbf{\nabla}_{\mathbf{\theta}}\mathbf{lo}\mathbf{g}{\mathbf{\sigma}\left( \mathbf{-}\mathbf{\phi}\left( \mathbf{x}_{\mathbf{i}} \right)^{\mathbf{T}}\mathbf{\theta} \right)} \right)$$</span></p>
<ul>
<li><p><strong>no</strong> general <strong>analytic</strong> <strong>solution</strong></p></li>
<li><p><strong>solved</strong> using <strong>numerical</strong> <strong>methods</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Useful Identity</td>
<td colspan="2"><ul>
<li><p><span class="math inline">$\frac{\mathbf{\partial}}{\mathbf{\partial}\mathbf{t}}\mathbf{\,}\mathbf{\sigma}\left( \mathbf{t} \right)\mathbf{=}\mathbf{\sigma}\left( \mathbf{t} \right)\left( \mathbf{1 -}\mathbf{\sigma}\left( \mathbf{t} \right) \right)$</span></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Gradient Descent</td>
<td></td>
</tr>
<tr>
<td>The G. D. Algorithm</td>
<td colspan="2"><ul>
<li><p><span class="math inline"><strong>θ</strong><sup><strong>0</strong></sup></span> ← <strong>initial</strong> <strong>vector</strong> (random, zeros, …)</p></li>
<li><p>for <span class="math inline"><strong>τ</strong></span> from <strong>0</strong> to <strong>convergence</strong></p></li>
</ul>
<p><span class="math inline"><strong>θ</strong><sup><strong>τ</strong> <strong>+</strong> <strong>1</strong></sup></span> <strong>←</strong> <span class="math inline"><strong>θ</strong><sup><strong>τ</strong></sup><strong>−</strong><strong>ρ</strong><strong>(</strong><strong>τ</strong><strong>)</strong><strong>(</strong><strong>∇</strong><sub><strong>θ</strong></sub><strong>L</strong><strong>(</strong><strong>θ</strong><strong>)</strong><strong>|</strong><sub><strong>θ</strong><strong>=</strong><strong>θ</strong><sup><strong>τ</strong></sup></sub></span></p>
<ul>
<li><p><span class="math inline"><strong>ρ</strong>(<strong>τ</strong>)</span> is the <strong>step</strong> <strong>size</strong> (learning rate)</p>
<ul>
<li><p>typically, <span class="math inline">$\frac{\mathbf{1}}{\mathbf{\tau}}$</span></p></li>
</ul></li>
<li><p><strong>converges</strong> when <strong>gradient</strong> is <span class="math inline"><strong>≈</strong></span> <strong>0</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Stochastic Gradient Descent</td>
<td colspan="2"><ul>
<li><p><strong>parameters</strong> are <strong>updated</strong> using one or <strong>small</strong> <strong>batches</strong></p></li>
<li><p>for many <strong>learning</strong> <strong>problems</strong>, the <strong>gradient</strong> is a <strong>sum</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{\nabla}_{\mathbf{\theta}}\mathbf{L}\left( \mathbf{\theta} \right)\mathbf{=}\frac{\mathbf{1}}{\mathbf{n}}\sum_{\mathbf{i = 1}}^{\mathbf{n}}\left( \mathbf{\sigma}\left( \mathbf{\phi}\left( \mathbf{x}_{\mathbf{i}} \right)^{\mathbf{T}}\mathbf{\theta} \right)\mathbf{-}\mathbf{y}_{\mathbf{i}} \right)\mathbf{\,}\mathbf{\phi}\left( \mathbf{x}_{\mathbf{i}} \right)$$</span></p>
<ul>
<li><p>for <strong>large</strong> <strong>n</strong> this can be <strong>costly</strong></p></li>
</ul>
<ul>
<li><p><strong>approximate</strong> the <strong>gradient</strong> by <strong>looking</strong> at a <strong>few</strong> random <strong>points</strong></p></li>
</ul>
<p>random sample of records</p>
<ul>
<li><p><span class="math inline">$\mathbf{\nabla}_{\mathbf{\theta}}\mathbf{L}\left( \mathbf{\theta} \right)\mathbf{\approx}\frac{\mathbf{1}}{\left| \mathbf{B} \right|}\sum_{\mathbf{i}\mathbf{\in}\mathbf{B}}^{}\left( \mathbf{\sigma}\left( \mathbf{\phi}\left( \mathbf{x}_{\mathbf{i}} \right)^{\mathbf{T}}\mathbf{\theta} \right)\mathbf{-}\mathbf{y}_{\mathbf{i}} \right)\mathbf{\,}\mathbf{\phi}\left( \mathbf{x}_{\mathbf{i}} \right)$</span></p></li>
</ul>
<p>batch size</p></td>
</tr>
<tr>
<td colspan="2">Linearly Separable Data</td>
<td></td>
</tr>
<tr>
<td>Definition</td>
<td colspan="2"><ul>
<li><p><strong>a classification dataset is said to be linearly separable if there exists a hyperplane that separates the two classes</strong></p></li>
</ul>
<p>X X</p>
<p>X X X X</p>
<p>X X X</p>
<p>X X X X</p>
<p>X X X X X</p>
<p>X XXX</p></td>
</tr>
<tr>
<td>Solution</td>
<td colspan="2"><ul>
<li><p>if data is linearly separable, logistic regression requires regularization</p></li>
<li><p>this is achieved by “tacking on” a penalty for the magnitude of <span class="math inline"><strong>θ</strong></span></p></li>
</ul>
<p><span class="math display">$$+ \ \ \ \ \mathbf{\lambda}\sum_{\mathbf{j = 1}}^{\mathbf{d}}\mathbf{\theta}_{\mathbf{j}}^{\mathbf{2}}$$</span></p>
<ul>
<li><p>prevents weights from diverging on linearly separable data</p></li>
<li><p>prevents overfitting</p></li>
</ul></td>
</tr>
<tr>
<td>Scikit-Learn</td>
<td colspan="2"><p>from sklearn.linear_model import LogisticRegression</p>
<p># sklearn adds regularization</p>
<p># C = 1 / by default lambda the inverse regularization parameter</p>
<p>model = LogisticRegression(C = 100.0)</p>
<p># Train the model</p>
<p>model.fit(df[['feat1', 'feat2']], df['label'])</p>
<p># Make predictions</p>
<p>test_df['label'] = model.predict(test_df[['feat1', 'feat2']])</p>
<p>test_df['P(Y|X)'] = model.predict_proba(test_df[['feat1', 'feat2']])</p></td>
</tr>
<tr>
<td>Binary Classification of Categorical Data</td>
<td colspan="2"><ul>
<li><p>for <span class="math inline"><strong>Y</strong> <em>i</em><em>n</em> <strong>{</strong><strong>1</strong><strong>,</strong>  <strong>.</strong><strong>.</strong><strong>.</strong>  <strong>,</strong> <strong>C</strong><strong>}</strong> </span>you <strong>train</strong> <strong>one</strong> binary <strong>classifier</strong> per class by <strong>grouping</strong> one classifier <strong>against</strong> all <strong>others</strong> for each classifier</p></li>
</ul>
<p><img src="generated_media\DATA780_week04_notes\media\image2.png" style="width:3.95189in;height:2.61982in" /></p>
<p>ChatGPT 5.2</p></td>
</tr>
<tr>
<td>Softmax multiclass classification</td>
<td colspan="2"><ul>
<li><p><span class="math inline">$\mathbf{P}\left( \mathbf{y = j}\mid\mathbf{x} \right)\mathbf{=}\frac{\mathbf{\exp}\left( \mathbf{x}^{\mathbf{T}}\mathbf{\theta}^{\mathbf{j}} \right)}{\sum_{\mathbf{k = 1}}^{\mathbf{K}}{\mathbf{\exp}\left( \mathbf{x}^{\mathbf{T}}\mathbf{\theta}_{\mathbf{k}} \right)}}$</span></p></li>
<li><p>separate <span class="math inline"><strong>θ</strong><sub><strong>j</strong></sub><strong>∈</strong><strong>R</strong><sup><strong>d</strong></sup></span> for each <strong>class</strong></p></li>
<li><p><strong>trained</strong> using <strong>GD</strong> methods</p></li>
<li><p>use <strong>K-1</strong> <strong>parameters</strong></p>
<ul>
<li><p><span class="math inline">$\mathbf{P}\left( \mathbf{y = k}\mid\mathbf{x} \right)\mathbf{= 1 -}\sum_{\mathbf{j}\mathbf{\neq}\mathbf{k}}^{}{\mathbf{P}\left( \mathbf{y = j}\mid\mathbf{x} \right)}$</span></p></li>
<li><p>often use <strong>K</strong> <strong>parameters</strong> + <strong>regularization</strong> to address “<strong>redundancy</strong>”</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>
