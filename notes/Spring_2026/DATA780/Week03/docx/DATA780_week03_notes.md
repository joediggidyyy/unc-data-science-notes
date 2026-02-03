---
generated_at_utc: 2026-02-03T07:44:09+00:00
generated_from: notes/Spring_2026/DATA780/Week03/docx/DATA780_week03_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week03_notes.pdf](../DATA780_week03_notes.pdf)
> - DOCX: [DATA780_week03_notes.docx](DATA780_week03_notes.docx)

---

<table style="width:100%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 3%" />
<col style="width: 0%" />
<col style="width: 12%" />
<col style="width: 23%" />
<col style="width: 12%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Regression</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td colspan="6" style="text-align: right;"><em>No Class Meeting (MLK Day)</em></td>
</tr>
<tr>
<td colspan="9"><ul>
<li><p>a machine learning task where we predict a real-valued output response given an input vector</p></li>
<li><p>linear and non-linear regression models</p></li>
<li><p>analytic (closed-form) solution to learn an optimal model from training data</p></li>
<li><p>gradient descent and stochastic gradient descent algorithms</p></li>
<li><p>model complexity and overfitting</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Readings</td>
<td colspan="5" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="9"><ul>
<li><p><a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf#page=157">https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf#page=157</a></p></li>
</ul></td>
</tr>
<tr>
<td colspan="9">Bishop, Pattern Recognition and Machine Learning (2006) pp. 137-152</td>
</tr>
<tr>
<td rowspan="6">Key Concepts</td>
<td colspan="4"><strong>Linear Model</strong></td>
<td colspan="4" style="text-align: right;">a <strong>function</strong> that <strong>adds</strong> up <strong>weighted</strong> <strong>inputs</strong></td>
</tr>
<tr>
<td colspan="4"><strong>Loss</strong></td>
<td colspan="4" style="text-align: right;">a <strong>measure</strong> of how <strong>wrong</strong> <strong>predictions</strong> are</td>
</tr>
<tr>
<td colspan="4"><strong>Least</strong> <strong>Squares</strong></td>
<td colspan="4" style="text-align: right;">find <strong>weights</strong> that make <strong>loss</strong> as <strong>small</strong> as <strong>possible</strong></td>
</tr>
<tr>
<td colspan="4"><strong>Basis</strong> <strong>Function</strong></td>
<td colspan="4" style="text-align: right;">transforms <strong>input</strong> so <strong>models</strong> can <strong>capture</strong> more <strong>complex</strong> <strong>patterns</strong></td>
</tr>
<tr>
<td colspan="4"><strong>Maximum</strong> <strong>Likelihood</strong></td>
<td colspan="4" style="text-align: right;">statistical way to <strong>find</strong> <strong>weights</strong> that make <strong>observed</strong> <strong>data</strong> most <strong>probable</strong></td>
</tr>
<tr>
<td colspan="4"><strong>Predictive</strong> <strong>Distribution</strong></td>
<td colspan="4" style="text-align: right;"><strong>range</strong> of possible <strong>outputs</strong> with <strong>associated</strong> <strong>confidence</strong></td>
</tr>
<tr>
<td>Scope of Reading</td>
<td colspan="8"><ul>
<li><p><strong>fit</strong> a linear <strong>model</strong> to <strong>data</strong></p></li>
<li><p><strong>measure</strong> model <strong>efficacy</strong></p></li>
<li><p><strong>interpret</strong> the <strong>model</strong> statistically</p></li>
</ul></td>
</tr>
<tr>
<td>Linear Regression Model</td>
<td colspan="8"><ul>
<li><p>the <strong>linear</strong> <strong>model</strong> predicts <span class="math inline"><em>y</em>(<em>x</em>) = <em>w</em><sub>0</sub> + <em>w</em><sub>1</sub><em>x</em><sub>1</sub> + <em>w</em><sub>2</sub><em>x</em><sub>2</sub> + … + <em>w</em><sub><em>D</em></sub><em>x</em><sub><em>D</em></sub></span></p></li>
</ul>
<p>where:</p>
<ul>
<li><p><span class="math inline"><em>x</em>  = 〖<em>x</em><sub>1</sub>, <em>x</em><sub>2</sub>, …, <em>x</em><sub><em>D</em></sub>)</span> is a <strong>vector</strong> of <strong>inputs</strong>.</p></li>
<li><p><span class="math inline"><em>w</em> = (<em>w</em><sub>0</sub>, <em>w</em><sub>1</sub>, …, <em>w</em><sub><em>D</em></sub>)</span> are <strong>parameters</strong> (<strong>weights</strong>).</p></li>
</ul>
<ul>
<li><p><span class="math inline"><em>w</em><sub>0</sub></span> is the <strong>bias</strong> (or <strong>intercept</strong>)</p></li>
<li><p>each <span class="math inline"><em>w</em><sub><em>j</em></sub></span> <strong>scales</strong> the <strong>corresponding</strong> input <strong>feature</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Loss Function: Sum of Squared Errors</td>
<td colspan="8"><ul>
<li><p>to <strong>train</strong> the <strong>model</strong>, we choose <strong>weights</strong> that make <strong>predictions</strong> <strong>close</strong> to real <strong>targets</strong></p></li>
<li><p><strong>measure</strong> each <strong>data</strong> point</p>
<ul>
<li><p><strong>error</strong> = <strong>predicted</strong> <strong>value</strong> – <strong>actual</strong> <strong>value</strong></p></li>
</ul></li>
<li><p>sum <strong>squared</strong> <strong>errors</strong> over all <strong>data</strong> <strong>points</strong></p>
<ul>
<li><p><span class="math inline">$E(w) = \sum_{\left\{ n = 1 \right\}}^{N}{\left( y\ \left( x_{n} \right) - t_{n} \right)^{2}}$</span></p></li>
</ul></li>
<li><p><strong>advantages</strong></p>
<ul>
<li><p>all <strong>errors</strong> are <strong>positive</strong></p></li>
<li><p><strong>large</strong> <strong>errors</strong> are <strong>penalized</strong> more</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Finding the Best Weights (Least Squares)</td>
<td colspan="8"><ul>
<li><p>set the <strong>derivative</strong> of <strong>error</strong> with <strong>respect</strong> to <strong>weights</strong> to <strong>zero</strong></p>
<ul>
<li><p>produces a <strong>formula</strong> that can be <strong>solved</strong> in a single <strong>step</strong></p></li>
</ul></li>
<li><p>in <strong>matrix</strong> <strong>form</strong></p>
<ul>
<li><p>let Φ = <strong>design</strong> <strong>matrix</strong> (features for all <strong>data</strong> <strong>points</strong>)</p></li>
<li><p>let <strong>t</strong> = <strong>vector</strong> of <strong>target</strong> <strong>values</strong></p></li>
<li><p><strong>optimal</strong> <strong>weights</strong>: <span class="math inline"><em>w</em><sup>*</sup>= (<em>Φ</em><sup><em>T</em></sup><em>Φ</em>)<sup>−1</sup><em>Φ</em><sup><em>T</em></sup><em>t</em></span></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Geometric Interpretation</td>
<td colspan="8"><ul>
<li><p>the <strong>model</strong> attempts to find the <strong>closest</strong> <strong>fit</strong> of a <strong>hyperplane</strong> to the <strong>data</strong> points</p></li>
<li><p>the <strong>error</strong> <strong>vector</strong> is <strong>orthogonal</strong> to the <strong>column</strong> <strong>space</strong> of the <strong>design</strong> <strong>matrix</strong></p></li>
<li><p>we protect <strong>target</strong> <strong>values</strong> onto the <strong>space</strong> spanned by <strong>basis</strong> <strong>functions</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Basis Functions</td>
<td colspan="8"><ul>
<li><p>nonlinear <strong>relationships</strong> can be <strong>modeled</strong> <strong>linearly</strong> in <strong>transformed</strong> <strong>space</strong> using <strong>basis</strong> <strong>functions</strong></p>
<ul>
<li><p><strong>polynomial:</strong> <span class="math inline"><strong>ϕ</strong><sub><strong>j</strong></sub>(<strong>x</strong>)<strong>=</strong><strong>x</strong><sup><strong>j</strong></sup></span></p></li>
<li><p><strong>Gaussian:</strong> <span class="math inline">$\mathbf{\varphi}_{\mathbf{j}}\left( \mathbf{x} \right)\mathbf{=}\mathbf{\exp}\left( \mathbf{-}\frac{\left( \mathbf{x\  -}\mathbf{\mu}_{\mathbf{j}}\mathbf{)} \right.〗^{\mathbf{2}}}{{\mathbf{2}\mathbf{s}}_{\mathbf{j}}^{\mathbf{2}}} \right)$</span></p></li>
</ul></li>
<li><p>the model becomes:<span class="math inline"> <em>y</em>(<em>x</em>) = ∑<sub><em>j</em></sub><em>w</em><sub><em>j</em></sub> <em>ϕ</em><sub><em>j</em></sub>(<em>x</em>)</span></p></li>
</ul></td>
</tr>
<tr>
<td>Probabilistic Interpretation</td>
<td colspan="8"><ul>
<li><p>we <strong>assume</strong> targets are <strong>generated</strong> by <strong>model</strong> plus <strong>Gaussian</strong> <strong>noise</strong> with <strong>zero</strong> <strong>mean</strong> and <strong>variance</strong> <span class="math inline"><strong>σ</strong><sup><strong>2</strong></sup></span></p></li>
<li><p>likely<strong>:</strong> <span class="math inline"><strong>p</strong><strong>(</strong><strong>t</strong><sub><strong>n</strong></sub><strong>∣</strong><strong>x</strong><sub><strong>n</strong></sub><strong>,</strong> <strong>w</strong><strong>,</strong> <strong>β</strong><strong>)</strong><strong>=</strong>𝒩(<strong>t</strong><sub><strong>n</strong></sub><strong>∣</strong><strong>w</strong><sup><strong>T</strong></sup><strong>ϕ</strong><strong>(</strong><strong>x</strong><sub><strong>n</strong></sub><strong>)</strong><strong>,</strong><strong>β</strong><sup><strong>−</strong><strong>1</strong></sup><strong>)</strong></span></p></li>
<li><p>where<strong>:</strong> <span class="math inline"><strong>β</strong> <strong>=</strong> <strong>1</strong><strong>/</strong><strong>σ</strong><sup><strong>2</strong></sup></span> is the <strong>noise precision</strong></p></li>
</ul>
<p><em>(this turns <strong>least</strong> <strong>squares</strong> into <strong>maximum</strong> <strong>likelihood</strong> estimation)</em></p></td>
</tr>
<tr>
<td>Maximum Likelihood for Weights</td>
<td colspan="8"><ul>
<li><p>under <strong>Gaussian</strong> <strong>noise</strong>, the <strong>likelihood</strong> of the entire <strong>dataset</strong> is the <strong>product</strong> of individual <strong>Gaussian</strong> <strong>terms</strong></p></li>
<li><p><strong>maximizing</strong> <strong>likelihood</strong> is equivalent to <strong>minimizing</strong> <strong>squared</strong> <strong>errors</strong></p></li>
<li><p><strong>least</strong>-<strong>squares</strong> solution = <strong>maximum</strong> <strong>likelihood</strong> solution</p></li>
</ul></td>
</tr>
<tr>
<td>Predictive Distribution</td>
<td colspan="8"><ul>
<li><p>once we <strong>estimate</strong> <strong>weights</strong>, predicted distribution of a new <strong>input</strong> <strong>x<sub>* </sub></strong>is <strong>Gaussian</strong></p></li>
<li><p>mean<strong>:</strong> <span class="math inline"><strong>y</strong>(<strong>x</strong><sub><strong>*</strong></sub>)<strong>=</strong><strong>w</strong><sub><strong>T</strong></sub><strong>ϕ</strong><strong>(</strong> <strong>x</strong><sub><strong>*</strong></sub><strong>)</strong></span></p></li>
<li><p><strong>variance</strong> depends on <strong>noise</strong> <strong>variance</strong> and how far <strong>x<sub>*</sub></strong> is from <strong>training</strong> inputs</p></li>
<li><p>this gives <strong>prediction,</strong> and <strong>confidence</strong> in <strong>prediction</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Overfitting and Regularization</td>
<td colspan="8"><ul>
<li><p>if the <strong>model</strong> has <strong>too</strong> many <strong>parameters</strong> it may <strong>fit</strong> <strong>noise</strong> <strong>instead</strong> of the <strong>true</strong> <strong>pattern</strong></p></li>
<li><p>to <strong>reduce</strong> <strong>overfitting</strong></p>
<ul>
<li><p><strong>add</strong> a <strong>penalty</strong> for <strong>large</strong> weights (<strong>regularization</strong>)</p></li>
<li><p>this can be <strong>interpreted</strong> as <strong>having</strong> a <strong>prior</strong> on <strong>weights</strong></p></li>
</ul></li>
<li><p><strong>regularization</strong> <strong>solution</strong> balances the <strong>fit</strong> to <strong>data</strong> and <strong>simplicity</strong> of <strong>model</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td colspan="5" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4">Linear Regression</td>
<td colspan="5" style="text-align: right;"></td>
</tr>
<tr>
<td>Definition</td>
<td colspan="8"><ul>
<li><p><strong>supervised</strong> <strong>learning</strong> technique used to <strong>train</strong> <strong>models</strong> with multiple input variables mapped to a single Real value</p></li>
<li><p>we <strong>map</strong> the <strong>vectorized</strong> <strong>inputs</strong> to a corresponding <strong>output</strong></p></li>
</ul></td>
</tr>
<tr>
<td>1-D and Multi-D</td>
<td colspan="8"><ul>
<li><p><strong>one</strong>-<strong>dimensional</strong>: models a <strong>real</strong> valued <strong>input</strong> to a <strong>real</strong> variable <strong>response</strong> so that, <span class="math inline"><strong>y</strong> <strong>=</strong> <strong>m</strong><strong>x</strong> <strong>+</strong> <strong>b</strong></span></p></li>
<li><p><strong>multi</strong>-<strong>dimensional</strong>: models <strong>vectorized</strong> <strong>real</strong> values to a <strong>single</strong> <strong>response</strong> variable, <span class="math inline"><em>ŷ</em>  =  <strong>β</strong><sub><strong>i</strong><strong>1</strong></sub><strong>x</strong><sub><strong>1</strong></sub><strong>+</strong> <strong>β</strong><sub><strong>i</strong><strong>2</strong></sub><strong>x</strong><sub><strong>2</strong></sub><strong>+</strong> <strong>β</strong><sub><strong>0</strong></sub></span></p></li>
</ul></td>
</tr>
<tr>
<td>MLE Roadmap</td>
<td colspan="8"><p><em><strong>MLE = ‘maximum likelihood estimation’</strong></em></p>
<ul>
<li><p><em>the <strong>roadmap</strong></em></p></li>
</ul>
<ol type="1">
<li><p><strong>establish</strong> model <strong>likelihood</strong> for <strong>data</strong></p></li>
<li><p><strong>derive</strong> an analytical <strong>formula</strong> for optimal <strong>parameters</strong> on training <strong>data</strong></p></li>
<li><p>extend to a nonlinear model</p></li>
</ol>
<ul>
<li><p><span class="math inline">$\mathbf{\ }\binom{\mathbf{arg\ max}}{\mathbf{₍}\mathbf{\theta}\mathbf{₎}}\prod_{\mathbf{ᵢ}\mathbf{₌}\mathbf{₁}}^{\mathbf{ⁿ}}{\mathbf{p\theta(y}\mathbf{ᵢ}\mathbf{\ |\ x}\mathbf{ᵢ}\mathbf{)}}\mathbf{\ }$</span><strong>supervised task</strong>, <strong>IID</strong> data <strong>(</strong>IID: <strong>Independent</strong> and <strong>Identically</strong> <strong>Distributed</strong> <strong>Data</strong>; for <strong>n</strong> data points: <span class="math inline">𝒟 <strong>=</strong> <strong>{</strong><strong>(</strong><strong>x</strong><strong>ᵢ</strong><strong>,</strong> <strong>y</strong><strong>ᵢ</strong><strong>)</strong><strong>}</strong><strong>ᵢ</strong><strong>₌</strong><strong>₁</strong><strong>ⁿ</strong></span><strong>)</strong></p></li>
<li><p>if we set up the <strong>maximum</strong> <strong>likelihood</strong> <strong>estimation</strong> task for linear regression will be <strong>equivalent</strong> for linear regression to <strong>minimizing</strong> the <strong>sum</strong> of <strong>squared</strong> <strong>errors</strong></p></li>
<li><p><span class="math inline">$\binom{\mathbf{arg\ max}}{\mathbf{\theta}}\prod_{\mathbf{ᵢ}\mathbf{₌}\mathbf{₁}}^{\mathbf{ⁿ}}{\mathbf{p\theta(y}\mathbf{ᵢ}\mathbf{\ }\mathbf{\mid}\mathbf{\ x}\mathbf{ᵢ}\mathbf{)}}\mathbf{\ }$</span></p></li>
</ul>
<p><span class="math display">$$\mathbf{= \ }\binom{\mathbf{arg\ max}}{\mathbf{\theta}\mathbb{\in R}\mathbf{ᵖ}}\mathbf{- \ }\sum_{\mathbf{ᵢ}\mathbf{₌}\mathbf{₁}}^{\mathbf{ⁿ}}{\mathbf{(y}\mathbf{ᵢ}\mathbf{\  - \ \theta}\mathbf{ᵀ}\mathbf{x}\mathbf{ᵢ}\mathbf{)²}}$$</span></p>
<blockquote>
<p><span class="math display">$$\mathbf{= \ }\binom{\mathbf{arg\ min}}{\mathbf{\theta}\mathbb{\in R}\mathbf{ᵖ}}\mathbf{\ }\sum_{\mathbf{ᵢ}\mathbf{₌}\mathbf{₁}}^{\mathbf{ⁿ}}{\mathbf{(y}\mathbf{ᵢ}\mathbf{\  - \ \theta}\mathbf{ᵀ}\mathbf{x}\mathbf{ᵢ}\mathbf{)²}}$$</span></p>
</blockquote></td>
</tr>
<tr>
<td>Model and Likelihood</td>
<td colspan="8"><ul>
<li><p><strong>Linear</strong> <strong>Probabilistic</strong> <strong>Model</strong>: <span class="math inline"><strong>y</strong> <strong>=</strong> <strong>θ</strong><strong>ᵀ</strong><strong>x</strong> <strong>+</strong> <strong>ε</strong></span>, where</p>
<ul>
<li><p><span class="math inline"><strong>θ</strong><strong>ᵀ</strong></span> is the <strong>vector</strong> of <strong>parameters</strong></p></li>
<li><p><span class="math inline"><strong>x</strong></span> is the <strong>vector</strong> of <strong>covariances</strong></p></li>
<li><p>and <span class="math inline"><strong>ε</strong></span> is <strong>real</strong> value <strong>noise</strong> of the model<em><strong>:</strong></em> <span class="math inline"><strong>ε</strong> <strong>∼</strong> 𝒩(<strong>0</strong><strong>,</strong> <strong>σ</strong><strong>²</strong><strong>)</strong></span></p></li>
</ul></li>
<li><p><strong>linear</strong> combination of <strong>covariates</strong>: <span class="math inline"><strong>∑</strong><strong>ᵢ</strong><sup><strong>=</strong><strong>1</strong></sup><strong>ᵖ</strong> <strong>θ</strong><strong>ᵢ</strong> <strong>x</strong><strong>ᵢ</strong></span></p></li>
</ul></td>
</tr>
<tr>
<td>Conditional Likelihood</td>
<td colspan="8"><ul>
<li><p><strong>Conditioned on x</strong>, the response variable <strong><em>y</em></strong> follows a <strong>Gaussian</strong> <strong>distribution</strong> with mean <span class="math inline"><strong>θ</strong><strong>ᵀ</strong><strong>x</strong> </span>and variance <span class="math inline"><strong>σ</strong><strong>²</strong></span></p></li>
<li><p>because we are <strong>adding</strong> a <strong>mean</strong> <strong>zero</strong> <strong>noise</strong>, and we know that <strong>adding</strong> a <strong>constant</strong> to a Gaussian is <strong>equivalent</strong> to <strong>changing</strong> its <strong>mean</strong>, the <strong>Gaussian</strong> goes from <strong>zero</strong> to the added <strong>constant</strong></p></li>
<li><p>so, <strong>y</strong>, given <strong>x</strong>, will be a <strong>Gaussian</strong> <strong>centered</strong> at the <strong>linear</strong> <strong>prediction</strong> with <strong>variance</strong> given by <strong>sigma</strong> squared, <span class="math inline"><strong>Y</strong> <strong>∼</strong> 𝒩<strong>(</strong><strong>θ</strong><strong>ᵀ</strong><strong>x</strong><strong>,</strong> <strong>σ</strong><strong>²</strong><strong>)</strong></span></p></li>
</ul></td>
</tr>
<tr>
<td>MLE with Dataset</td>
<td colspan="8"><ul>
<li><p><strong>Estimating the Model</strong></p>
<ul>
<li><p>given data, how can we estimate <span class="math inline"><strong>θ</strong></span>?</p></li>
<li><p><strong>construct</strong> maximum likelihood estimator (<strong>MLE</strong>)</p>
<ul>
<li><p><strong>derive</strong> the <strong>log</strong>-<strong>likelihood</strong></p></li>
<li><p><strong>find</strong> <span class="math inline"><strong>θ</strong></span> MLE that <strong>maximizes</strong> likelihood</p>
<ul>
<li><p><strong>analytically</strong>: take <strong>derivative</strong> and <strong>set</strong> to <strong>0</strong></p></li>
<li><p><strong>iteratively</strong>: (stochastic) <strong>gradient</strong> <strong>descent</strong></p></li>
</ul></li>
</ul></li>
</ul></li>
<li><p><strong>defining the likelihood</strong></p>
<ul>
<li><p><strong>conditional density:</strong></p></li>
</ul></li>
</ul>
<blockquote>
<p><span class="math inline">$\mathbf{p\theta(y\ }\mathbf{\mid}\mathbf{\ x)\  = \ (}\frac{\mathbf{1}}{\mathbf{(}\mathbf{\sigma}\sqrt{\mathbf{2}\mathbf{\pi}}}\mathbf{)\ }\mathbf{\cdot}\mathbf{\ exp( -}\frac{\mathbf{(y\ }\mathbf{-}\mathbf{\ }\mathbf{\theta}\mathbf{ᵀ}\mathbf{x)²}}{\mathbf{2}\mathbf{\sigma ²}}\mathbf{\ )}$</span></p>
</blockquote>
<ul>
<li><p><strong>likelihood function:</strong></p></li>
</ul>
<blockquote>
<p><span class="math inline">ℒ<strong>(</strong><strong>θ</strong><strong>;</strong> 𝒟<strong>)</strong> <strong>=</strong> <strong>∏</strong><strong>ᵢ</strong><strong>₌</strong><strong>₁</strong><strong>ⁿ</strong> <strong>p</strong><strong>θ</strong><strong>(</strong><strong>y</strong><strong>ᵢ</strong> <strong>∣</strong> <strong>x</strong><strong>ᵢ</strong><strong>)</strong></span> <strong>=</strong></p>
<p><span class="math inline">$\mathbf{\prod}\mathbf{ᵢ}\mathbf{₌}\mathbf{₁ⁿ}\mathbf{\ }\frac{\mathbf{1}}{\mathbf{\sigma\sqrt{}(2}\mathbf{\pi)}}\mathbf{\  \cdot \ exp(\  -}\frac{\mathbf{(y}\mathbf{ᵢ}\mathbf{\  - \ \theta}\mathbf{ᵀ}\mathbf{x}\mathbf{ᵢ}\mathbf{)²}}{\mathbf{2}\mathbf{\sigma ²}}\mathbf{\ )}$</span> <strong>=</strong></p>
<p><span class="math display">$$\frac{\mathbf{1}}{\mathbf{\sigma ⁿ\ }\left( \mathbf{2}\mathbf{\pi} \right)_{\frac{\mathbf{n}}{\mathbf{2}}}}\mathbf{\ exp(\ }\frac{\mathbf{1}}{\mathbf{2}\mathbf{\sigma ²}}\mathbf{\sum}\mathbf{ᵢ}\mathbf{₌}\mathbf{₁ⁿ}\mathbf{\ (y}\mathbf{ᵢ}\mathbf{\  - \ \theta}\mathbf{ᵀ}\mathbf{x}\mathbf{ᵢ}\mathbf{)²\ )}$$</span></p>
</blockquote></td>
</tr>
<tr>
<td>Analytical Solution</td>
<td colspan="8"><ul>
<li><p><strong>minimizing</strong> the <strong>likelihood</strong> (minimizing the squared error) is a <strong>convex</strong> <strong>function</strong> where we <strong>seek</strong> the slope (<strong>gradient</strong>) <strong>= 0</strong></p></li>
</ul>
<blockquote>
<p><img src="generated_media\DATA780_week03_notes\media\image1.png" style="width:2.41467in;height:1.03294in" /></p>
</blockquote>
<ul>
<li><p>the <strong>gradient</strong> is generalizing the <strong>derivative</strong> for <strong>multivariate</strong> <strong>functions</strong></p></li>
</ul>
<p><span class="math display"><strong>−</strong><strong>∇</strong><strong>θ</strong> <strong>log</strong>  ℒ<strong>(</strong><strong>θ</strong><strong>)</strong> <strong>=</strong> <strong>∇</strong><strong>θ</strong> <strong>∑</strong><strong>ᵢ</strong><strong>₌</strong><strong>₁</strong><strong>ⁿ</strong> <strong>(</strong><strong>y</strong><strong>ᵢ</strong> <strong>−</strong> <strong>θ</strong><strong>ᵀ</strong><strong>x</strong><strong>ᵢ</strong><strong>)</strong><strong>²</strong></span></p>
<p><strong>Chain rule → =</strong> <span class="math inline"><strong>−</strong><strong>2</strong> <strong>∑</strong><strong>ᵢ</strong><strong>₌</strong><strong>₁</strong><strong>ⁿ</strong> <strong>(</strong><strong>y</strong><strong>ᵢ</strong> <strong>−</strong> <strong>θ</strong><strong>ᵀ</strong><strong>x</strong><strong>ᵢ</strong><strong>)</strong> <strong>x</strong><strong>ᵢ</strong></span></p>
<blockquote>
<p><span class="math display"><strong>=</strong>  <strong>−</strong> <strong>2</strong> <strong>∑</strong><strong>ᵢ</strong><strong>₌</strong><strong>₁</strong><strong>ⁿ</strong> <strong>y</strong><strong>ᵢ</strong> <strong>x</strong><strong>ᵢ</strong> <strong>+</strong> <strong>2</strong> <strong>∑</strong><strong>ᵢ</strong><strong>₌</strong><strong>₁</strong><strong>ⁿ</strong> <strong>(</strong><strong>θ</strong><strong>ᵀ</strong> <strong>x</strong><strong>ᵢ</strong><strong>)</strong> <strong>x</strong><strong>ᵢ</strong></span></p>
</blockquote>
<ul>
<li><p><strong>rewriting</strong> with <strong>matrix</strong> notation</p>
<ul>
<li><p><strong>represent</strong> data <span class="math inline">$\mathcal{D}\mathbf{\  = \ }\left\{ \mathbf{\ }\left( \mathbf{x}\mathbf{ᵢ,\ }\mathbf{y}\mathbf{ᵢ} \right) \right\}\binom{\mathbf{n}}{\mathbf{i}\mathbf{= 1}}$</span> as,</p></li>
</ul></li>
</ul>
<blockquote>
<p><strong>covariate</strong> (design) <strong>matrix</strong>:</p>
<p><strong>n</strong> <span class="math inline">$\mathbf{X}\mathbf{\  =}\binom{\binom{\mathbf{-}\mathbf{x}_{\mathbf{1}}\mathbf{-}}{\mathbf{-}\mathbf{x}_{\mathbf{2}}\mathbf{-}}}{\binom{\mathbf{\ldots}}{\mathbf{-}\mathbf{x}_{\mathbf{n}}\mathbf{-}}}\mathbf{\in}\mathbf{\ }\mathbf{R}\mathbf{ⁿᵖ}$</span></p>
<p><strong>p</strong></p>
<p><span class="math display"><strong>a</strong><strong>s</strong><strong>s</strong><strong>u</strong><strong>m</strong><strong>e</strong> <strong>X</strong> <strong>h</strong><strong>a</strong><strong>s</strong> <strong>r</strong><strong>a</strong><strong>n</strong><strong>k</strong> <strong>p</strong> <strong>(</strong><strong>n</strong><strong>o</strong><strong>t</strong> <strong>d</strong><strong>e</strong><strong>g</strong><strong>e</strong><strong>n</strong><strong>e</strong><strong>r</strong><strong>a</strong><strong>t</strong><strong>e</strong><strong>)</strong></span></p>
<p><strong>response</strong> <strong>vector</strong></p>
<p><strong>n</strong> <span class="math inline">$\mathbf{Y}\mathbf{= \ }\binom{\binom{\mathbf{y}_{\mathbf{1}}}{\mathbf{y}_{\mathbf{2}}}}{\binom{\begin{array}{r}
\mathbf{.} \\
\mathbf{.} \\
\mathbf{.}
\end{array}}{\mathbf{y}_{\mathbf{n}}}}\mathbf{\in}\mathbf{\ }\mathbf{R}\mathbf{ⁿ}$</span></p>
</blockquote>
<p><strong>1</strong></p>
<ul>
<li><p><strong>rewriting</strong> the <strong>gradient</strong> in matrix form</p></li>
</ul>
<blockquote>
<p><span class="math display"><strong>−</strong><strong>∇</strong><strong>θ</strong> <strong>log</strong>  ℒ<strong>(</strong><strong>θ</strong><strong>)</strong> <strong>=</strong>  <strong>−</strong> <strong>2</strong> <strong>∑</strong><strong>ᵢ</strong><strong>₌</strong><strong>₁</strong><strong>ⁿ</strong> <strong>y</strong><strong>ᵢ</strong> <strong>x</strong><strong>ᵢ</strong> <strong>+</strong> <strong>2</strong> <strong>∑</strong><strong>ᵢ</strong><strong>₌</strong><strong>₁</strong><strong>ⁿ</strong> <strong>(</strong><strong>θ</strong><strong>ᵀ</strong> <strong>x</strong><strong>ᵢ</strong><strong>)</strong> <strong>x</strong><strong>ᵢ</strong></span></p>
<p><span class="math display"><strong>=</strong>  <strong>−</strong> <strong>2</strong> <strong>X</strong><strong>ᵀ</strong> <strong>Y</strong> <strong>+</strong> <strong>2</strong> <strong>X</strong><strong>ᵀ</strong> <strong>X</strong> <strong>θ</strong></span></p>
</blockquote>
<ul>
<li><p>our goal is <strong>gradient</strong> <strong>= 0</strong> which gives,</p></li>
</ul>
<p><span class="math display"><strong>X</strong><sub><strong>T</strong></sub><strong>X</strong><strong>θ</strong><strong>=</strong><strong>X</strong><sub><strong>T</strong></sub><strong>Y</strong></span></p>
<p><span class="math display"><strong>θ</strong><strong>=</strong>(<strong>X</strong><sub><strong>T</strong></sub><strong>X</strong>)<sup><strong>−</strong><strong>1</strong></sup><strong>(</strong><strong>X</strong><sub><strong>T</strong></sub><strong>Y</strong><strong>)</strong> </span></p></td>
</tr>
<tr>
<td>Computing with MLE Parameters</td>
<td colspan="6"><ul>
<li><p><strong>computing</strong> the MLE: <span class="math inline">${\widehat{\widehat{\mathbf{\theta}}}}_{\mathbf{MLE}}\mathbf{\  = \ (Xᵀ\ X)⁻¹\ Xᵀ\ Y}$</span></p>
<ul>
<li><p><strong>not</strong> <strong>typically</strong> solved by <strong>inverting</strong> <span class="math inline"><strong>X</strong><sub><strong>T</strong></sub><strong>X</strong></span></p></li>
<li><p>solved using <strong>direct</strong> <strong>methods</strong>:</p>
<ul>
<li><p><strong>Cholesky</strong> <strong>factorization</strong></p>
<ul>
<li><p>up to a <strong>factor</strong> of <strong>2</strong> faster</p></li>
</ul></li>
<li><p><strong>QR</strong> <strong>factorization</strong></p>
<ul>
<li><p><strong>more</strong> numerically <strong>stable</strong></p></li>
</ul></li>
</ul></li>
<li><p>solved using <strong>various</strong> <strong>iterative</strong> <strong>methods</strong>:</p>
<ul>
<li><p>(stochastic) <strong>gradient</strong> <strong>descent</strong></p></li>
</ul></li>
</ul></li>
</ul></td>
<td colspan="2" style="text-align: right;"><p><strong>or use the built-in solver in your math library</strong></p>
<p><strong>R:</strong></p>
<p><strong>solve(Xt %*% X, Xt %*% y)</strong></p></td>
</tr>
<tr>
<td>Cholesky Factorization</td>
<td colspan="5"><p>solve for:</p>
<p><span class="math display">$${\widehat{\mathbf{\theta}}}_{\mathbf{MLE}}\mathbf{\ \ }\left( \mathbf{X}\mathbf{ᵀ}\mathbf{\ X} \right){\widehat{\mathbf{\theta}}}_{\mathbf{MLE}}\mathbf{\  = \ X}\mathbf{ᵀ}\mathbf{\ Y}$$</span></p>
<ul>
<li><p><strong>compute</strong> symm. <strong>matrix</strong></p></li>
<li><p>compute <strong>vector</strong></p></li>
<li><p><strong>Cholesky</strong> <strong>factorization</strong></p>
<ul>
<li><p><strong>L</strong> is <strong>lower</strong> <strong>triangular</strong></p></li>
</ul></li>
<li><p><strong>forward</strong> <strong>subs</strong>. to solve:</p></li>
<li><p><strong>backward</strong> <strong>subs</strong>. to solve:</p></li>
</ul></td>
<td colspan="2" style="text-align: right;"><p><span class="math display"><strong>C</strong><strong>=</strong><strong>X</strong><sup><strong>T</strong></sup> <strong>X</strong></span></p>
<p><span class="math display"><strong>d</strong><strong>=</strong><strong>X</strong><sup><strong>T</strong></sup> <strong>Y</strong></span></p>
<p><span class="math display"><strong>L</strong><strong>L</strong><sup><strong>T</strong></sup> <strong>=</strong> <strong>C</strong></span></p>
<p><span class="math display"><strong>L</strong><strong>z</strong> <strong>=</strong> <strong>d</strong></span></p>
<p><span class="math display">$${\mathbf{L}^{\mathbf{T}}\widehat{\mathbf{\theta}}}_{\mathbf{MLE}}\mathbf{= z}$$</span></p></td>
<td style="text-align: left;"><p><span class="math display"><strong>O</strong><strong>(</strong><strong>n</strong><strong>p</strong><sup><strong>2</strong></sup><strong>)</strong></span></p>
<p><span class="math display"><strong>O</strong><strong>(</strong><strong>n</strong><strong>p</strong><strong>)</strong></span></p>
<p><span class="math display"><strong>O</strong><strong>(</strong><strong>p</strong><sup><strong>3</strong></sup><strong>)</strong> </span></p>
<p><span class="math display"><strong>O</strong><strong>(</strong><strong>P</strong><sup><strong>2</strong></sup><strong>)</strong></span></p>
<p><span class="math display"><strong>O</strong><strong>(</strong><strong>P</strong><sup><strong>2</strong></sup><strong>)</strong></span></p></td>
</tr>
<tr>
<td rowspan="2">Solving Triangular System</td>
<td colspan="5"><table>
<colgroup>
<col style="width: 24%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>11</strong></sub></span></th>
<th style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>12</strong></sub></span></th>
<th style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>13</strong></sub></span></th>
<th style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>14</strong></sub></span></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>22</strong></sub></span></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>23</strong></sub></span></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>24</strong></sub></span></td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>33</strong></sub></span></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>34</strong></sub></span></td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>44</strong></sub></span></td>
</tr>
</tbody>
</table></td>
<td colspan="2" style="text-align: right;"><table>
<colgroup>
<col style="width: 25%" />
<col style="width: 29%" />
<col style="width: 28%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"></th>
<th style="text-align: center;"><span class="math display"><strong>x</strong><sub><strong>1</strong></sub></span></th>
<th rowspan="4" style="text-align: center;"><span class="math display"><strong>=</strong></span></th>
<th style="text-align: center;"><span class="math display"><strong>b</strong><sub><strong>1</strong></sub></span></th>
</tr>
<tr>
<th style="text-align: center;"><span class="math display">*</span></th>
<th style="text-align: center;"><span class="math inline"><strong>x</strong><sub><strong>2</strong></sub></span></th>
<th style="text-align: center;"><span class="math display"><strong>b</strong><sub><strong>2</strong></sub></span></th>
</tr>
<tr>
<th style="text-align: center;"></th>
<th style="text-align: center;"><span class="math display"><strong>x</strong><sub><strong>3</strong></sub></span></th>
<th style="text-align: center;"><span class="math display"><strong>b</strong><sub><strong>3</strong></sub></span></th>
</tr>
<tr>
<th style="text-align: center;"></th>
<th style="text-align: center;"><span class="math display"><strong>x</strong><sub><strong>4</strong></sub></span></th>
<th style="text-align: center;"><span class="math display"><strong>b</strong><sub><strong>4</strong></sub></span></th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><table>
<colgroup>
<col style="width: 20%" />
<col style="width: 29%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>11</strong></sub><strong>x</strong><sub><strong>1</strong></sub></span></th>
<th style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>12</strong></sub><strong>x</strong><sub><strong>2</strong></sub></span></th>
<th style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>13</strong></sub><strong>x</strong><sub><strong>3</strong></sub></span></th>
<th style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>14</strong></sub><strong>x</strong><sub><strong>4</strong></sub></span></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>22</strong></sub></span></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>23</strong></sub></span></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>24</strong></sub></span></td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>33</strong></sub></span></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>34</strong></sub></span></td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><span class="math display"><strong>A</strong><sub><strong>44</strong></sub></span></td>
</tr>
</tbody>
</table></td>
<td colspan="2" style="text-align: right;"><table>
<colgroup>
<col style="width: 83%" />
<col style="width: 7%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th><span class="math display">$$\mathbf{x}_{\mathbf{1}}\mathbf{=}\frac{\mathbf{b}_{\mathbf{1}}\mathbf{-}\mathbf{A}_{\mathbf{12}}\mathbf{x}_{\mathbf{2}}\mathbf{-}\mathbf{A}_{\mathbf{13}}\mathbf{x}_{\mathbf{3}}\mathbf{-}\mathbf{A}_{\mathbf{14}}\mathbf{x}_{\mathbf{4}}}{\mathbf{A}_{\mathbf{11}}}$$</span></th>
<th rowspan="4"></th>
<th style="text-align: center;"><span class="math display"><em>b</em><sub>1</sub></span></th>
</tr>
<tr>
<th><span class="math display">$$\mathbf{x}_{\mathbf{2}}\mathbf{=}\frac{\mathbf{b}_{\mathbf{2}}\mathbf{-}\mathbf{A}_{\mathbf{23}}\mathbf{x}_{\mathbf{3}}\mathbf{-}\mathbf{A}_{\mathbf{24}}\mathbf{x}_{\mathbf{4}}}{\mathbf{A}_{\mathbf{22}}}$$</span></th>
<th style="text-align: center;"><span class="math display"><em>b</em><sub>2</sub></span></th>
</tr>
<tr>
<th style="text-align: center;"><span class="math display">$$\mathbf{x}_{\mathbf{3}}\mathbf{=}\frac{\mathbf{b}_{\mathbf{3}}\mathbf{-}\mathbf{A}_{\mathbf{34}}\mathbf{x}_{\mathbf{4}}}{\mathbf{A}_{\mathbf{33}}}$$</span></th>
<th style="text-align: center;"><span class="math display"><em>b</em><sub>3</sub></span></th>
</tr>
<tr>
<th style="text-align: center;"><span class="math display">$$\mathbf{x}_{\mathbf{4}}\mathbf{=}\frac{\mathbf{b}_{\mathbf{4}}}{\mathbf{A}_{\mathbf{44}}}$$</span></th>
<th style="text-align: center;"><span class="math display"><em>b</em><sub>4</sub></span></th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr>
<th>Iterative Optimization</th>
<th><ul>
<li><p>Gradient descent is an iterative operation concerned with minimizing some loss with respect to certain parameters</p></li>
<li><p>Minimize <span class="math inline"><strong>L</strong><strong>(</strong><strong>θ</strong></span>) with respect to <span class="math inline"><strong>θ</strong></span></p></li>
</ul>
<p><span class="math display"><strong>F</strong><strong>o</strong><strong>r</strong> <strong>τ</strong> <strong>f</strong><strong>r</strong><strong>o</strong><strong>m</strong> <strong>0</strong> <strong>t</strong><strong>o</strong> <strong>c</strong><strong>o</strong><strong>n</strong><strong>v</strong><strong>e</strong><strong>r</strong><strong>g</strong><strong>e</strong><strong>n</strong><strong>c</strong><strong>e</strong><strong>:</strong></span></p>
<p><span class="math display"><strong>θ</strong><sup><strong>τ</strong> <strong>+</strong> <strong>1</strong></sup><strong>=</strong><strong>θ</strong><sup><strong>τ</strong></sup><strong>−</strong><strong>ρ</strong><strong>(</strong><strong>τ</strong><strong>)</strong> <strong>∇</strong><strong>L</strong><strong>(</strong><strong>θ</strong><sup><strong>τ</strong></sup><strong>)</strong></span></p>
<p>direction of steepest ascent</p>
<p>learning rate</p>
<p>Gradient Descent Illustrated</p>
<p><span class="math display"><strong>−</strong><strong>l</strong><strong>o</strong><strong>g</strong> ℒ<strong>(</strong><strong>θ</strong><strong>)</strong></span></p>
<p><span class="math display"><strong>S</strong><strong>l</strong><strong>o</strong><strong>p</strong><strong>e</strong> <strong>=</strong> <strong>0</strong></span></p>
<p>θ⁽⁰⁾ θ⁽¹⁾</p>
<p>θ⁽²⁾ θ⁽³⁾</p>
<p><span class="math display">$$\mathbf{\theta\hat{}\hat{}3\  = \ }{\widehat{\mathbf{\theta}}}_{\mathbf{MLE}}$$</span></p>
<p><strong>convex function</strong></p></th>
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
<th>Speeding Up Gradient Descent</th>
<th><ul>
<li><p>What if P is large?</p>
<ul>
<li><p>the cost of <span class="math inline"><strong>O</strong><strong>(</strong><strong>n</strong><strong>p</strong><sup><strong>2</strong></sup><strong>)</strong> <strong>=</strong> <strong>O</strong><strong>(</strong><strong>n</strong><sup><strong>3</strong></sup><strong>)</strong></span> could be prohibitive</p></li>
</ul></li>
</ul>
<p>for <span class="math inline"><strong>τ</strong></span> from 0 to convergence</p>
<p><span class="math display"><strong>θ</strong><strong>⁽</strong><strong>ᵗ</strong><strong>⁺</strong><strong>¹</strong><strong>⁾</strong> <strong>=</strong> <strong>θ</strong><strong>⁽</strong><strong>ᵗ</strong><strong>⁾</strong> <strong>−</strong> <strong>ρ</strong><strong>(</strong><strong>τ</strong><strong>)</strong> <strong>∇</strong><strong>ₜ</strong> <strong>l</strong><strong>o</strong><strong>g</strong> ℒ<strong>(</strong><strong>θ</strong><strong>⁽</strong><strong>ᵗ</strong><strong>⁾</strong> <strong>|</strong> 𝒟<strong>)</strong></span></p>
<p><span class="math display">$$\mathbf{\propto}\mathbf{\ }\mathbf{\theta}^{\mathbf{(}}\mathbf{ᵗ}^{\mathbf{)}}\mathbf{- \ \rho}\left( \mathbf{\tau} \right)\mathbf{\nabla ₜ}\mathbf{\ }\sum_{\mathbf{i - 1}}^{\mathbf{n}}\left( \mathbf{y}\mathbf{ᵢ}\mathbf{\  - \ \theta}\mathbf{ᵀ}\mathbf{x}\mathbf{ᵢ} \right)^{\mathbf{2}}\mathbf{\ \ \ \ \ \ \ \ \ \ \ \ }$$</span></p>
<p><span class="math display"><strong>=</strong> <strong>θ</strong><strong>⁽</strong><strong>ᵗ</strong><strong>⁾</strong> <strong>+</strong> <strong>ρ</strong><strong>(</strong><strong>τ</strong><strong>)</strong> <strong>⋅</strong> <strong>2</strong> <strong>∑</strong><strong>ᵢ</strong><strong>₌</strong><strong>₁</strong><strong>ⁿ</strong> <strong>(</strong><strong>y</strong><strong>ᵢ</strong> <strong>−</strong> <strong>θ</strong><strong>ᵀ</strong><strong>x</strong><strong>ᵢ</strong><strong>)</strong> <strong>x</strong><strong>ᵢ</strong>           <strong>O</strong><strong>(</strong><strong>n</strong><strong>p</strong><strong>)</strong></span></p>
<ul>
<li><p>can we do better?</p>
<ul>
<li><p>Solution: iterative methods</p>
<ul>
<li><p>gradient descent:</p></li>
</ul></li>
</ul></li>
</ul>
<blockquote>
<p><span class="math display">$$\mathbf{L(\theta)\  = \ }\frac{\mathbf{1}}{\mathbf{2}\mathbf{n}}\sum_{\mathbf{i - 1}}^{\mathbf{n}}{\mathbf{(y}\mathbf{ᵢ}\mathbf{\  - \ \theta}\mathbf{ᵀ}\mathbf{x}\mathbf{ᵢ}\mathbf{)²}}$$</span></p>
</blockquote>
<p>for <span class="math inline"><strong>τ</strong></span> from 0 to convergence</p>
<p><span class="math display"><strong>θ</strong><strong>ᵗ</strong><sup><strong>+</strong><strong>1</strong></sup><strong>=</strong><strong>θ</strong><strong>ᵗ</strong> <strong>−</strong> <strong>ρ</strong><strong>(</strong><strong>τ</strong><strong>)</strong> <strong>∇</strong><strong>L</strong><strong>(</strong><strong>θ</strong><strong>ᵗ</strong><strong>)</strong></span></p>
<blockquote>
<p><span class="math display">$$\mathbf{= \theta}\mathbf{ᵗ}\mathbf{\  + \ \rho(\tau)\  \cdot \ }\frac{\mathbf{1}}{\mathbf{n}}\mathbf{)}\sum_{\mathbf{i - 1}}^{\mathbf{n}}{\mathbf{(y}\mathbf{ᵢ}\mathbf{\  - \ \theta}\mathbf{ᵀ}\mathbf{x}\mathbf{ᵢ}\mathbf{)\ x}\mathbf{ᵢ}}$$</span></p>
</blockquote>
<p>estimate of the gradient</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Stochastic Gradient Descent</td>
<td><ul>
<li><p><strong>decomposable</strong> <strong>loss</strong></p></li>
<li><p><strong>loss</strong> can be written as a <strong>sum</strong> of the <strong>loss</strong> on <strong>each</strong> <strong>record</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{L}\mathbf{(}\mathbf{\theta}\mathbf{)\  = \ \sum ᵢ}\mathbf{₌}\mathbf{₁ⁿ\ }\mathbf{L}\mathbf{ᵢ(}\mathbf{\theta}\mathbf{)\  = \ }\sum_{\mathbf{i - 1}}^{\mathbf{n}}{\mathbf{L(\theta,\ x}\mathbf{ᵢ}\mathbf{,\ y}\mathbf{ᵢ}\mathbf{)}}$$</span></p>
<ul>
<li><p><strong>equivalent</strong> to <strong>minimize</strong></p></li>
</ul>
<p><span class="math display">$$\frac{\mathbf{1}}{\mathbf{n}}\mathbf{\ L(\theta) =}\frac{\mathbf{1}}{\mathbf{n}}\sum_{\mathbf{i - 1}}^{\mathbf{n}}{\mathbf{L(\theta,\ x}\mathbf{ᵢ}\mathbf{,\ y}\mathbf{ᵢ}\mathbf{)}}$$</span></p>
<ul>
<li><p>with <strong>gradients</strong></p></li>
</ul>
<p><span class="math display">$$\frac{\mathbf{1}}{\mathbf{n}}\mathbf{\nabla}\mathbf{\theta}\mathbf{\ L(}\mathbf{\theta}\mathbf{) =}\frac{\mathbf{1}}{\mathbf{n}}\sum_{\mathbf{i}\mathbf{\in B}}^{}{\mathbf{\ }\mathbf{\nabla}\mathbf{\theta}\mathbf{\ L(}\mathbf{\theta}\mathbf{,\ x}\mathbf{ᵢ}\mathbf{,\ y}\mathbf{ᵢ}\mathbf{)}}\mathbf{\approx}\frac{\mathbf{1}}{\mathbf{|B|}}\sum_{\mathbf{i}\mathbf{\in B}}^{}{\mathbf{\ }\mathbf{\nabla}\mathbf{\theta}\mathbf{\ L(}\mathbf{\theta}\mathbf{,\ x}\mathbf{ᵢ}\mathbf{,\ y}\mathbf{ᵢ}\mathbf{)}}$$</span></p>
<p><span class="math display"><em>B</em> ∼ <em>r</em><em>a</em><em>n</em><em>d</em><em>o</em><em>m</em> <em>s</em><em>u</em><em>b</em><em>s</em><em>e</em><em>t</em> <em>o</em><em>f</em> <em>i</em><em>n</em><em>d</em><em>i</em><em>c</em><em>e</em><em>s</em></span></p>
<ul>
<li><p><strong>decomposable</strong> <strong>loss</strong>:</p></li>
</ul>
<p><span class="math display">$$L(\theta)\  = \ \sum_{\mathbf{i - 1}}^{\mathbf{n}}{Lᵢ(\theta)} = \sum_{\mathbf{i - 1}}^{\mathbf{n}}{L(\theta,\ xᵢ,\ yᵢ)}$$</span></p>
<p><span class="math display"><em>l</em><em>o</em><em>s</em><em>s</em> <em>c</em><em>a</em><em>n</em> <em>b</em><em>e</em> <em>w</em><em>r</em><em>i</em><em>t</em><em>t</em><em>e</em><em>n</em> <em>a</em><em>s</em> <em>a</em> <em>s</em><em>u</em><em>m</em> <em>o</em><em>f</em> <em>t</em><em>h</em><em>e</em> <em>l</em><em>o</em><em>s</em><em>s</em> <em>o</em><em>n</em> <em>e</em><em>a</em><em>c</em><em>h</em> <em>r</em><em>e</em><em>c</em><em>o</em><em>r</em><em>d</em></span></p>
<ul>
<li><p><strong>visualizing</strong> <strong>gradient</strong> <strong>descent</strong></p></li>
</ul>
<p><img src="generated_media\DATA780_week03_notes\media\image2.png" style="width:3.46875in;height:2.3125in" /></p>
<p><em>Image generated with ChatGPT (GPT-5.2), OpenAI. Joe Waller.</em></p></td>
</tr>
<tr>
<td>Stochastic Gradient Descent for Linear Regression</td>
<td><ul>
<li><p>for linear regression, <strong>stochastic</strong> <strong>gradient</strong> <strong>descent</strong> is just a matter of <strong>randomly</strong> <strong>subsampling</strong> <strong>indices</strong> and then <strong>computing</strong> <strong>gradient</strong></p></li>
<li><p><strong>construct</strong> a noisy <strong>estimate</strong> of the <strong>gradient</strong>:</p></li>
<li><p>for <strong>τ</strong> from <strong>0</strong> to <strong>convergence</strong></p></li>
</ul>
<ol type="1">
<li><p>pick a <strong>random</strong> <span class="math inline"><strong>i</strong></span></p></li>
<li><p><span class="math inline"><strong>θ</strong><sup><strong>τ</strong> <strong>+</strong> <strong>1</strong></sup><strong>=</strong><strong>θ</strong><sup><strong>τ</strong></sup><strong>+</strong> <strong>ρ</strong><strong>(</strong><strong>τ</strong><strong>)</strong> <strong>(</strong><strong>y</strong><strong>ᵢ</strong><strong>−</strong><strong>θ</strong><sup>(<strong>τ</strong>)<sub><strong>T</strong></sub></sup><strong>x</strong><strong>ᵢ</strong><strong>)</strong> <strong>x</strong><strong>ᵢ</strong>           <strong>O</strong><strong>(</strong><strong>n</strong><strong>p</strong><strong>)</strong></span></p></li>
</ol>
<ul>
<li><p>applies to <strong>streaming</strong> <strong>data</strong> <span class="math inline"><strong>O</strong><strong>(</strong><strong>p</strong><strong>)</strong></span> storage</p></li>
<li><p>optimizing using a <strong>single</strong> <strong>data</strong> <strong>point</strong> at a time opens the door for ‘<strong>online’</strong> or ‘<strong>streaming’</strong> <strong>optimization</strong></p></li>
<li><p>this <strong>ability</strong> to only consider <strong>select</strong> <strong>data</strong> points at a time comes in especially <strong>useful</strong> when <strong>training</strong> a <strong>large</strong> <strong>model</strong> with <strong>limited</strong> <strong>hardware</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Nonlinear Regression</td>
<td><ul>
<li><p><strong>linear</strong> <strong>regression</strong> can represent nonlinear functions by <strong>applying</strong> nonlinear <strong>feature</strong> <strong>transformations</strong> and <strong>modeling</strong> the output as a <strong>linear</strong> <strong>combination</strong> of those <strong>features</strong></p></li>
<li><p><strong>representing</strong> the design <strong>matrix</strong> on our chosen <strong>feature</strong> <strong>space</strong>,</p></li>
<li><p>train:</p></li>
</ul>
<p><span class="math inline">$\mathbf{\Phi}\left( \mathbf{X} \right)\mathbf{:\ n\  \times \ k\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \Phi}\left( \mathbf{X} \right)\mathbf{=}\genfrac{[}{]}{0pt}{}{\binom{\mathbf{- \varphi}\left( \mathbf{x}^{\mathbf{1}} \right)\mathbf{-}}{\mathbf{- \varphi}\left( \mathbf{x}^{\mathbf{2}} \right)\mathbf{-}}}{\binom{\mathbf{\vdots}}{\mathbf{- \ \varphi}\left( \mathbf{x}\mathbf{ₙ} \right)\mathbf{-}}}\mathbf{\ }$</span></p>
<p><span class="math inline">$\widehat{\mathbf{\theta}}\mathbf{\leftarrow solv}\mathbf{e}_{\mathbf{\theta}}\mathbf{(\Phi(X)ᵀ\ \Phi(X)\ \theta\  = \ \Phi(X)ᵀ\ Y\ )}$</span></p>
<ul>
<li><p>test:</p></li>
</ul>
<p><span class="math inline"><strong>x</strong><sup><strong>′</strong></sup><strong>:</strong> <strong>p</strong> <strong>×</strong> <strong>1</strong></span> <span class="math inline"><strong>φ</strong>(<strong>x</strong><sup><strong>′</strong></sup>)<strong>:</strong> <strong>k</strong> <strong>×</strong> <strong>1</strong></span></p>
<ul>
<li><p><span class="math inline">$\mathbf{ŷ\  \leftarrow \ \theta\hat{}}\mathbf{ᵀ}\mathbf{\ \varphi(x')}$</span></p></li>
</ul></td>
</tr>
<tr>
<td>Overfitting and Model Variance</td>
<td><ul>
<li><p><strong>overfitting</strong> can give a <strong>false</strong> <strong>sense</strong> of doing “really well”</p></li>
<li><p><strong>Underfitting</strong> occurs when a machine learning <strong>model</strong> is too <strong>simple</strong> to capture the underlying <strong>patterns</strong> in <strong>data</strong>, resulting in <strong>poor</strong> <strong>performance</strong> on both <strong>training</strong> and <strong>testing</strong> datasets</p></li>
</ul>
<p><strong>underfitting</strong></p>
<p><strong>overfitting</strong></p></td>
</tr>
<tr>
<td>Regularization to Prevent Overfitting</td>
<td><ul>
<li></li>
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
<th colspan="2">Live Session Notes</th>
<th style="text-align: right;">30 Oct 2025</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"></td>
</tr>
<tr>
<td>Project Proposal</td>
<td colspan="2"><ul>
<li><p>due 02/11</p></li>
<li><p>deliverables</p>
<ul>
<li><p>state the task</p></li>
<li><p>state the goals</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
</tbody>
</table>
