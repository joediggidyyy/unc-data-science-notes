---
generated_at_utc: 2026-03-09T05:35:10+00:00
generated_from: notes/Spring_2026/DATA780/Week08/docx/DATA780_week08_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week08_notes.pdf](../DATA780_week08_notes.pdf)
> - DOCX: [DATA780_week08_notes.docx](DATA780_week08_notes.docx)

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
<th colspan="2">Validation</th>
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
<li><p>test set methods</p></li>
<li><p>leave-one-out cross-validation</p></li>
<li><p>k-fold cross-validation</p></li>
<li><p>variants and imported caveats to validation techniques</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Reading</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><p><em>The Elements of Statistical Learning</em></p>
<p><a href="http://statistics.stanford.edu/~hastie/">Trevor Hastie</a>, <a href="http://statistics.stanford.edu/~tibs/">Robert Tibshirani</a>, <a href="http://statistics.stanford.edu/~jhf">Jerome Friedman</a></p>
<p>Chapter 7-7.2, 7.10</p>
<p>https://hastie.su.domains/ElemStatLearn/</p></td>
</tr>
<tr>
<td>Summary</td>
<td colspan="4"><ul>
<li><p>when <strong>building</strong> predictive <strong>models</strong>, two issues must be addressed</p>
<ul>
<li><p>model <strong>assessment</strong></p>
<ul>
<li><p>how well the model <strong>preforms</strong> on new data</p></li>
</ul></li>
<li><p>model <strong>selection</strong></p>
<ul>
<li><p>choose the <strong>best</strong> model <strong>complexity</strong></p></li>
</ul></li>
</ul></li>
<li><p>the <strong>key</strong> <strong>objective</strong> goes <strong>beyond</strong> simply <strong>fitting</strong> the training <strong>data</strong> to <strong>minimizing</strong> prediction <strong>error</strong> on future <strong>observations</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Key Takeaways</td>
<td colspan="4"><ul>
<li><p><strong>training</strong> error is <strong>not</strong> a reliable <strong>indicator</strong> of predictive <strong>performance</strong></p></li>
<li><p><strong>prediction</strong> error = (<strong>bias</strong>)<sup>2</sup> + <strong>variance</strong> + <strong>noise</strong></p></li>
<li><p><strong>increasing</strong> model <strong>complexity</strong> decreases <strong>bias</strong> but increases <strong>variance</strong></p></li>
<li><p>model <strong>assessment</strong> requires test <strong>error</strong> <strong>estimation</strong></p></li>
<li><p><strong>cross</strong>-<strong>validation</strong> is the most <strong>common</strong> <strong>method</strong> for doing this</p></li>
</ul></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 28%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Validation</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Error on Future Data</td>
</tr>
<tr>
<td>Fitting the Data</td>
<td colspan="2"><ul>
<li><p>we want the <strong>model</strong> to fit the <strong>data</strong></p>
<ul>
<li><p>without <strong>over</strong>-<strong>fitting</strong> or <strong>under-fitting</strong></p></li>
<li><p><strong>without</strong> becoming <strong>over</strong>-<strong>reliant</strong> on <strong>training</strong> data</p></li>
</ul></li>
<li><p>even if training <strong>error</strong> is <strong>low</strong> future <strong>errors</strong> can be <strong>high</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Model Complexity and Choices</td>
</tr>
<tr>
<td>Ideal Model Complexity</td>
<td colspan="2"><p>overfitting</p>
<p>underfitting</p>
<p><img src="generated_media\DATA780_week08_notes\media\image1.png" style="width:3.20833in;height:1.91181in" /></p>
<p>predictive</p>
<p>error</p>
<p>error on out-of-sample data</p>
<p>model complexity</p>
<p>error on in-sample data</p>
<p>ideal range for model complexity</p></td>
</tr>
<tr>
<td colspan="3">Model Complexity and Choices</td>
</tr>
<tr>
<td>Linear Regression</td>
<td colspan="2"><ul>
<li><p>often the <strong>trend</strong> in the data is <strong>not</strong> <strong>obvious</strong></p></li>
<li><p>you have to <strong>select</strong> the <strong>model</strong> that is <strong>best</strong> for your data</p></li>
</ul></td>
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
<th>Quadratic Regression</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Piecewise Non-Parametric Regression</td>
<td></td>
</tr>
<tr>
<td colspan="2">Test-Set Validation</td>
</tr>
<tr>
<td>Test-Set Method</td>
<td><ul>
<li><p><strong>randomly</strong> choose <strong>30%</strong> of the data to be a <strong>test</strong> set</p></li>
<li><p>the <strong>remainder</strong> is the <strong>training</strong> set</p></li>
<li><p>perform <strong>regression</strong> on the <strong>training</strong> set</p></li>
<li><p><strong>estimate</strong> your <strong>future</strong> performance with the <strong>test</strong> set</p></li>
<li><p>this can be <strong>achieved</strong> with any of the <strong>three</strong> <strong>models</strong></p></li>
<li><p>the <strong>optimal</strong> model is <strong>not</strong> always the model with the <strong>lowest</strong> <strong>error</strong></p></li>
<li><p>the optimal <strong>model</strong> is the model that performs <strong>best</strong> on the <strong>test</strong> <strong>set</strong> <strong>after</strong> being <strong>trained</strong> on the training set</p></li>
</ul></td>
</tr>
<tr>
<td>Results</td>
<td><ul>
<li><p><strong>good</strong> news</p>
<ul>
<li><p>simply <strong>choose</strong> the model with the <strong>best</strong> test-set <strong>score</strong></p></li>
</ul></li>
<li><p><strong>bad</strong> news</p>
<ul>
<li><p><strong>wastes</strong> data</p></li>
<li><p>to get the <strong>estimate</strong> we <strong>loose</strong> <strong>30%</strong> of the data</p></li>
<li><p>if data is <strong>sparse</strong>, test set can <strong>match</strong> or not match <strong>randomly</strong></p></li>
</ul></li>
</ul></td>
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
<th colspan="2">Leave-One-Out Cross-Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td>LOOCV Method</td>
<td><ul>
<li><p>for <span class="math inline"><strong>k</strong> <strong>=</strong> <strong>1</strong></span> top <span class="math inline"><strong>R</strong></span></p>
<ul>
<li><p>let <span class="math inline">(<strong>x</strong><sub><strong>k</strong></sub><strong>,</strong> <strong>y</strong><sub><strong>k</strong></sub>)</span> be the <span class="math inline"><strong>k</strong><sup><strong>t</strong><strong>h</strong></sup></span> record</p></li>
<li><p>temporarily <strong>remove</strong> <span class="math inline">(<strong>x</strong><sub><strong>k</strong></sub><strong>,</strong> <strong>y</strong><sub><strong>k</strong></sub>)</span> from the dataset</p></li>
<li><p><strong>train</strong> the remaining <span class="math inline"><strong>R</strong> <strong>−</strong> <strong>1</strong></span> datapoints</p></li>
<li><p><strong>note</strong> your <strong>error</strong> <span class="math inline">(<strong>x</strong><sub><strong>k</strong></sub><strong>,</strong> <strong>y</strong><sub><strong>k</strong></sub>)</span></p></li>
</ul></li>
<li><p>when you have done this to <strong>all</strong> points, report the mean <strong>error</strong></p></li>
<li><p>to do this you <strong>average</strong> the <strong>mean</strong> <strong>error</strong> from each run</p></li>
<li><p>this can be <strong>done</strong> with <strong>each</strong> of the three discussed <strong>methods</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Results</td>
<td><ul>
<li><p>this method is <strong>expensive</strong></p></li>
<li><p>does <strong>not</strong> <strong>waste</strong> data</p></li>
<li><p>this would be <strong>unmanageable</strong> with <strong>large</strong> datasets</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">K-Fold Cross-Validation</td>
</tr>
<tr>
<td>K-Fold Method</td>
<td><ul>
<li><p>randomly break the dataset into <span class="math inline"><strong>k</strong></span> partitions</p></li>
<li><p>for the partition</p></li>
</ul>
<ul>
<li><p>for the <strong>red</strong> partition</p></li>
<li><p>train on <strong>all</strong> the <strong>points</strong> <strong>not</strong> in the <strong>red</strong> partition</p></li>
<li><p>find the <strong>test</strong>-<strong>set</strong> sum of <strong>errors</strong> on the red points</p></li>
<li><p>repeat this for the <strong>green</strong> and <strong>blue</strong> partitions</p></li>
<li><p><strong>repeat</strong> this <strong>process</strong> with <strong>all</strong> of the candidate <strong>models</strong></p></li>
</ul></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th colspan="4">Contrasting Validation Methods</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="6"><p>Review of Cross-Validation Methods</p>
<p>sometimes there are algorithmic tricks for making these cheap</p></td>
<td></td>
<td>Downside</td>
<td>Upside</td>
</tr>
<tr>
<td><strong>Test-Set</strong></td>
<td><p><strong>variance</strong></p>
<p><strong>unreliable</strong> <strong>estimate</strong> of future performance</p></td>
<td><strong>cheap</strong></td>
</tr>
<tr>
<td><strong>Leave-One-Out</strong></td>
<td><strong>expensive</strong></td>
<td>does <strong>not</strong> <strong>waste</strong> data</td>
</tr>
<tr>
<td><strong>10-Fold</strong></td>
<td><p><strong>wastes</strong> <span class="math inline"><strong>10</strong><strong>%</strong></span> of the data</p>
<p><span class="math inline"><strong>10</strong><strong>x</strong></span> more <strong>expensive</strong> than test-set</p></td>
<td><p>only <strong>wastes</strong> <span class="math inline"><strong>10</strong><strong>%</strong></span></p>
<p>only <span class="math inline"><strong>10</strong><strong>x</strong></span> times more <strong>expensive</strong> instead of <span class="math inline"><strong>R</strong></span> times</p></td>
</tr>
<tr>
<td><strong>3-Fold</strong></td>
<td><p>more <strong>wasteful</strong> than <strong>10</strong>-<strong>fold</strong></p>
<p>more <strong>expensive</strong> than <strong>test</strong>-<strong>set</strong></p></td>
<td>slightly <strong>better</strong> than test-set</td>
</tr>
<tr>
<td><strong>R-Fold</strong></td>
<td colspan="2"><strong>identical</strong> to leave-one-out</td>
</tr>
<tr>
<td colspan="4">Cross-Validation Applications</td>
</tr>
<tr>
<td>Cross-Validation for Regression Hyper-Parameters</td>
<td colspan="3"><ul>
<li><p>choosing the <strong>number</strong> of <strong>hidden</strong> <strong>units</strong> in a neural net</p></li>
<li><p><strong>feature</strong> selection</p></li>
<li><p>choosing a <strong>polynomial</strong> <strong>degree</strong></p></li>
<li><p>choosing <strong>which</strong> <strong>regressor</strong> to use</p></li>
<li><p><strong>parametric</strong> vs <strong>non</strong>-parametric</p></li>
</ul></td>
</tr>
<tr>
<td>Cross-Validation for Classification</td>
<td colspan="3"><ul>
<li><p><strong>instead</strong> of <strong>computing</strong> the sum squared <strong>errors</strong> on a test set</p></li>
<li><p><strong>total</strong> number of <strong>misclassifications</strong> in a test set</p></li>
</ul></td>
</tr>
<tr>
<td>CV-Based Algorithm Choice</td>
<td colspan="3"><ul>
<li><p>compute <strong>10-fold</strong>-<strong>cv error</strong> for different <strong>model</strong> class</p></li>
<li><p><strong>train</strong> the data with the <strong>algorithm</strong> that gave the best <strong>CV</strong> score</p></li>
</ul></td>
</tr>
<tr>
<td>Choosing Hyperparameters</td>
<td colspan="3"><ul>
<li><p>perform <strong>test</strong> with every <strong>combination</strong> of <strong>hyperparameters</strong></p></li>
<li><p>for this <strong>hyperparameter</strong> set you will run <strong>18</strong> <strong>tests</strong></p>
<ul>
<li><p>hyperparameter 1 in {H11, H22}</p></li>
</ul></li>
</ul>
<p>2 x 3 x 3 = 18</p>
<ul>
<li><p><strong>hyperparameter 2 in {H21, H22, H23}</strong></p></li>
<li><p>hyperparameter 3 in {H31, H32, H33}</p></li>
</ul></td>
</tr>
<tr>
<td>Validation to Choose Bandwidth</td>
<td colspan="3"><ul>
<li><p>make a set of <strong>candidate</strong> <strong>bandwidths</strong> around the “rule of thumb” bandwidths (ex: average <strong>5<sup>th</sup></strong>-<strong>nearest</strong> <strong>neighbor</strong> distance</p></li>
</ul>
<p><span class="math display">ℋ= {<strong>2</strong><sup><strong>j</strong></sup><strong>h</strong><sub><strong>r</strong><strong>o</strong><strong>t</strong></sub>}<sub>{<strong>j</strong> <strong>=</strong>  <strong>−</strong> <strong>M</strong>}</sub><sup>{<strong>M</strong>}</sup></span></p>
<ul>
<li><p><strong>split</strong> the data into “<strong>train</strong>” and “<strong>validation</strong>” sets</p></li>
</ul>
<p><span class="math display"><strong>D</strong><sub><strong>v</strong><strong>a</strong><strong>l</strong></sub><strong>∩</strong> <strong>D</strong><sub><strong>t</strong><strong>r</strong><strong>n</strong></sub><strong>=</strong> <strong>⌀</strong></span></p>
<ul>
<li><p><strong>choose</strong> the bandwidth <span class="math inline"><strong>h</strong> <strong>∈</strong>ℋ </span>with the <strong>best</strong> likelihood</p></li>
</ul>
<p><span class="math inline">$\frac{\mathbf{1}}{\left| \mathbf{D}_{\mathbf{val}} \right|}\sum_{\mathbf{x\  \in \ }\mathbf{D}_{\mathbf{val}}}^{}{\mathbf{log(\ }{\widehat{\mathbf{p}}}_{\mathbf{h}\left( \mathbf{x} \right)}\mathbf{)}}$</span> <strong>=</strong></p>
<p><span class="math display">$$\left( \frac{\mathbf{1}}{\left| \mathbf{D}_{\mathbf{val}} \right|} \right)\sum_{\mathbf{x\  \in \ }\mathbf{D}_{\mathbf{val}}}^{}\mathbf{\log}\mathbf{\ (}\frac{\mathbf{1}}{\left| \mathbf{D}_{\mathbf{val}} \right|}\sum_{\mathbf{x\  \in \ }\mathbf{D}_{\mathbf{val}}}^{}{\mathbf{k}_{\mathbf{h}}\mathbf{(}\mathbf{x}^{\mathbf{'}}\mathbf{,\ x)}}$$</span></p></td>
</tr>
<tr>
<td colspan="4">Cross-Validation Alternatives</td>
</tr>
<tr>
<td>Other Cross-Validation Issues</td>
<td colspan="3"><ul>
<li><p>can do “<strong>leave</strong> all <strong>pairs</strong> out” or “<strong>leave</strong> all <strong>n-tuples</strong> out”</p></li>
<li><p><strong>k-folds</strong> where each <strong>fold</strong> is <strong>independently</strong> <strong>chosen</strong> subsets</p></li>
</ul></td>
</tr>
<tr>
<td>Alternatives to CV-Based Model Selection</td>
<td colspan="3"><ul>
<li><p>Model <strong>selection</strong> methods</p>
<ul>
<li><p><strong>Cross</strong>-validation</p></li>
<li><p><strong>AIC</strong> (Akaike information criterion)</p></li>
<li><p><strong>BIC</strong> (Bayesian information criterion)</p></li>
<li><p><strong>VC</strong> dimension (Vapnik–Chervonenkis dimension)</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>
