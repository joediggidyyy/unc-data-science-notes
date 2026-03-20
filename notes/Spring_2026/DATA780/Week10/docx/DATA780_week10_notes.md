---
generated_at_utc: 2026-03-20T18:58:28+00:00
generated_from: notes/Spring_2026/DATA780/Week10/docx/DATA780_week10_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week10_notes.pdf](../DATA780_week10_notes.pdf)
> - DOCX: [DATA780_week10_notes.docx](DATA780_week10_notes.docx)

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
<th colspan="2">Clustering</th>
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
<li><p>unsupervised machine learning</p></li>
<li><p>identify salient patterns in the data</p></li>
<li><p>k-means</p></li>
<li><p>lossy compression scheme</p></li>
<li><p>convergence and initialization</p></li>
<li><p>hierarchical clustering</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Reading</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><p>Pattern Recognition and Machine Learning</p>
<p>9.1 K-Means Clustering</p>
<p><a href="https://oa.ee.tsinghua.edu.cn/ouzhijian/pgm/pgm-pdf/PRML%20book.pdf">https://oa.ee.tsinghua.edu.cn/ouzhijian/pgm/pgm-pdf/PRML%20book.pdf</a></p>
<p>Elements of Statistical Learning</p>
<p>14.3 Cluster Analysis</p>
<p><a href="https://jqichina.wordpress.com/wp-content/uploads/2012/02/the-elements-of-statistical-learning.pdf">https://jqichina.wordpress.com/wp-content/uploads/2012/02/the-elements-of-statistical-learning.pdf</a></p>
<p><span class="math inline"><strong>K</strong></span> is assumed to be a <strong>known</strong> <strong>value</strong></p></td>
</tr>
<tr>
<td colspan="5">PRML: K-Means Clustering</td>
</tr>
<tr>
<td colspan="5">9.1 K-Means Clustering</td>
</tr>
<tr>
<td><p>What</p>
<p>K-Means Means..</p></td>
<td colspan="4"><ul>
<li><p>a <strong>non</strong>-<strong>probabilistic</strong> clustering method</p></li>
<li><p><strong>divides</strong> <span class="math inline"><strong>N</strong></span> datapoint into <span class="math inline"><strong>D</strong> <strong>−</strong> <strong>d</strong><strong>i</strong><strong>m</strong><strong>e</strong><strong>n</strong><strong>s</strong><strong>i</strong><strong>o</strong><strong>n</strong><strong>a</strong><strong>l</strong></span> Euclidean space into <span class="math inline"><strong>K</strong></span> <strong>clusters</strong></p></li>
<li><p>each cluster is <strong>represented</strong> by a <strong>prototype</strong> <strong>vector</strong> <span class="math inline"><strong>μ</strong><sub><strong>k</strong></sub></span> (cluster center)</p></li>
<li><p>objective is to <strong>assign</strong> each <strong>point</strong> to a <strong>cluster</strong> so that <strong>points</strong> are as <strong>close</strong> as possible to their <strong>assigned</strong> <strong>center</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Key Representation</td>
<td colspan="4"><ul>
<li><p>for each <strong>datapoint</strong> <span class="math inline"><strong>x</strong><sub><strong>n</strong></sub></span> there exist <strong>binary</strong> <strong>indicator</strong> variables <span class="math inline"><strong>r</strong><sub><strong>n</strong><strong>k</strong></sub></span></p></li>
</ul>
<p><span class="math display">1 − <em>o</em><em>f</em> − <em>K</em> <em>c</em><em>o</em><em>d</em><em>i</em><em>n</em><em>g</em></span></p>
<ul>
<li><p><span class="math inline"><strong>r</strong><sub><strong>n</strong><strong>k</strong></sub> <strong>=</strong> <strong>1</strong></span>: if <span class="math inline"><strong>x</strong><sub><strong>n</strong></sub></span> is assigned to cluster <span class="math inline"><strong>k</strong></span></p></li>
<li><p><span class="math inline"><strong>r</strong><sub><strong>n</strong><strong>k</strong></sub> <strong>=</strong> <strong>0</strong></span><strong>:</strong> else</p></li>
</ul>
<ul>
<li><p>using these indicators, K-means minimizes the distortion objective</p></li>
</ul>
<p>sum of squared distances from <strong>every</strong> <strong>point</strong> to its assigned <strong>cluster</strong> <strong>center</strong></p>
<p><span class="math display">$$\mathbf{J}\mathbf{=}\sum_{\mathbf{n = 1}}^{\mathbf{N}}{\sum_{\mathbf{k = 1}}^{\mathbf{K}}{\mathbf{r}_{\mathbf{nk}}\left| \left| \mathbf{x}_{\mathbf{n}}\mathbf{-}\mathbf{\mu}_{\mathbf{k}} \right| \right|^{\mathbf{2}}}}$$</span></p></td>
</tr>
<tr>
<td>How the Algorithm Works</td>
<td colspan="4"><p><strong>K-means</strong> alternates between <strong>two</strong> <strong>steps</strong></p>
<ul>
<li><p><strong>assignment</strong> step</p>
<ul>
<li><p><strong>keep</strong> the centers <span class="math inline"><strong>μ</strong><sub><strong>k</strong></sub></span> <strong>fixed</strong></p></li>
<li><p><strong>assign</strong> each <strong>point</strong> to the <strong>nearest</strong> center</p></li>
<li><p>formally, set <span class="math inline"><strong>r</strong><sub><strong>n</strong><strong>k</strong></sub> <strong>=</strong> <strong>1</strong></span> for the <strong>cluster</strong> whose <strong>center</strong> gives the <strong>smallest</strong> square <strong>distance</strong> to <span class="math inline"><strong>x</strong><sub><strong>n</strong></sub></span></p></li>
</ul></li>
<li><p><strong>update</strong> step</p>
<ul>
<li><p><strong>keep</strong> the assignments <strong>fixed</strong></p></li>
<li><p><strong>recompute</strong> each <strong>center</strong> as the <strong>mean</strong> of the <strong>points</strong> <strong>assigned</strong> to that <strong>cluster</strong></p></li>
</ul></li>
</ul>
<p>each <strong>prototype</strong> becomes the <strong>mean</strong> of its <strong>cluster</strong> <strong>members</strong></p>
<p><span class="math display">$$\mathbf{\mu}_{\mathbf{k}}\mathbf{=}\frac{\sum_{\mathbf{n}}^{}{\mathbf{r}_{\mathbf{nk}}\mathbf{x}_{\mathbf{n}}}}{\sum_{\mathbf{n}}^{}\mathbf{r}_{\mathbf{nk}}}$$</span></p></td>
</tr>
<tr>
<td>Iteration and Convergence</td>
<td colspan="4"><ul>
<li><p>these two <strong>steps</strong> <strong>cycle</strong> until</p>
<ul>
<li><p>the <strong>assignments</strong> <strong>stabilize</strong></p></li>
<li><p>exit <strong>criteria</strong> are <strong>met</strong></p></li>
</ul></li>
<li><p>each step <strong>reduces</strong> the <strong>objective</strong> <span class="math inline"><strong>J</strong></span></p></li>
<li><p><strong>only</strong> <strong>guaranteed</strong> to reach a <strong>local</strong> <strong>minimum</strong></p></li>
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
<th><p>Relation to Expectation</p>
<p>Maximization (EM)</p></th>
<th><ul>
<li><p>these two<span class="math inline"> <strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>s</strong></span> phases correspond to the <span class="math inline"><strong>E</strong> <strong>−</strong> <strong>s</strong><strong>t</strong><strong>e</strong><strong>p</strong></span> and <span class="math inline"><strong>M</strong> <strong>−</strong> <strong>s</strong><strong>t</strong><strong>e</strong><strong>p</strong></span></p>
<ul>
<li><p><span class="math inline"><strong>E</strong> <strong>−</strong> <strong>s</strong><strong>t</strong><strong>e</strong><strong>p</strong></span> <span class="math inline"><strong>↔︎</strong></span> reassigning points</p></li>
<li><p><span class="math inline"><strong>M</strong> <strong>−</strong> <strong>s</strong><strong>t</strong><strong>e</strong><strong>p</strong></span> <span class="math inline"><strong>↔︎</strong></span> recompute centers</p></li>
</ul></li>
<li><p><span class="math inline"><strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>s</strong></span> is a special non-probabilistic limit of <span class="math inline"><strong>E</strong><strong>M</strong></span> for Gaussian mixtures</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Practical Behavior</td>
<td><ul>
<li><p>“The Old Faithful” example shows</p>
<ul>
<li><p>the <strong>algorithm</strong> <strong>depends</strong> on the <strong>initial choice</strong> of centers</p></li>
<li><p><strong>poor</strong> <strong>initialization</strong> can require <strong>more</strong> <strong>iterations</strong></p></li>
<li><p>a common <strong>practical</strong> <strong>initialization</strong> is to choose <span class="math inline"><strong>K</strong></span><strong>random</strong> data points as the <strong>initial</strong> <strong>centers</strong></p></li>
</ul></li>
<li><p>the cost function <span class="math inline"><strong>J</strong></span> <strong>decreases</strong> after successive <span class="math inline"><strong>E</strong></span> and <span class="math inline"><strong>M</strong></span> <strong>steps</strong> until <strong>convergence</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Computational Issues</td>
<td><ul>
<li><p>a <strong>direct</strong> <strong>implementation</strong> can be <strong>slow</strong> because <strong>each</strong> assignment <strong>step</strong> compares <strong>every</strong> data <strong>point</strong> with <strong>every</strong> prototype <strong>vector</strong></p></li>
<li><p>the text mentions <strong>speedups</strong> based on</p>
<ul>
<li><p><strong>tree</strong>-<strong>based</strong> data structures for <strong>nearby</strong> <strong>points</strong></p></li>
<li><p><strong>triangle</strong>-<strong>inequality</strong> tricks to <strong>avoid</strong> unnecessary <strong>distance</strong> <strong>computations</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Online Stochastic Version</td>
<td><ul>
<li><p><strong>updates</strong> the <strong>nearest</strong> prototype <strong>after</strong> each <strong>incoming</strong> point</p></li>
</ul>
<p>decreases over time</p>
<p><span class="math display"><strong>μ</strong><sub><strong>k</strong></sub><sup><strong>n</strong><strong>e</strong><strong>w</strong></sup><strong>=</strong><strong>μ</strong><sub><strong>k</strong></sub><sup><strong>o</strong><strong>l</strong><strong>d</strong></sup><strong>+</strong><strong>η</strong><sub><strong>n</strong></sub>(<strong>x</strong><sub><strong>n</strong></sub><strong>−</strong><strong>μ</strong><sub><strong>k</strong></sub><sup><strong>o</strong><strong>l</strong><strong>d</strong></sup>)</span></p>
<ul>
<li><p>where <span class="math inline"><strong>η</strong><sub><strong>n</strong></sub></span>is a <strong>learning</strong> <strong>rate</strong></p></li>
<li><p>makes <span class="math inline"><strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>s</strong></span> suitable for <strong>sequential</strong> or <strong>streaming</strong>-style <strong>updates</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Limits of Standard K-Means</td>
<td><ul>
<li><p>standard <span class="math inline"><strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>s</strong></span> uses squared <strong>Euclidean</strong> <strong>distance</strong></p></li>
<li><p><strong>creates</strong> <strong>two</strong> important <strong>limitations</strong></p>
<ul>
<li><p>it is <strong>not</strong> <strong>appropriate</strong> for some variable <strong>types</strong>, such as <strong>categorical</strong> <strong>labels</strong></p></li>
<li><p>the <strong>mean</strong> can be <strong>sensitive</strong> to <strong>outliers</strong>, so the <strong>cluster</strong> <strong>centers</strong> may be <strong>non</strong>-<strong>robust</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Generalization: K-medoids</td>
<td><ul>
<li><p>generalizes <span class="math inline"><strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>s</strong></span> by <strong>replacing</strong> squared <strong>Euclidean</strong> <strong>distance</strong> with a more general <strong>dissimilarity</strong> <strong>measure</strong> <span class="math inline"><strong>V</strong>(<strong>x</strong><strong>,</strong><strong>x</strong><sup><strong>′</strong></sup>)</span>, yielding a <strong>new</strong> <strong>objective</strong>:</p></li>
</ul>
<p><span class="math display">$$\mathbf{J}^{\mathbf{'}}\mathbf{=}\sum_{\mathbf{n}\mathbf{= 1}}^{\mathbf{N}}{\sum_{\mathbf{k}\mathbf{= 1}}^{\mathbf{K}}\mathbf{r}_{\mathbf{nk}}}\mathbf{V}\left( \mathbf{x}_{\mathbf{n}}\mathbf{,}\mathbf{\mu}_{\mathbf{k}} \right)
$$</span></p>
<ul>
<li><p>this leads to <span class="math inline"><strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>d</strong><strong>o</strong><strong>i</strong><strong>d</strong><strong>s</strong></span></p>
<ul>
<li><p>assignment still <strong>sends</strong> each <strong>point</strong> to the <strong>nearest</strong> <strong>prototype</strong> under the <strong>chosen</strong> <strong>dissimilarity</strong></p></li>
<li><p>the <strong>update</strong> step is <strong>harder</strong></p></li>
<li><p>the <strong>prototype</strong> is often <strong>restricted</strong> to be one of the <strong>actual</strong> data <strong>points</strong> in the <strong>cluster</strong></p></li>
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
<th>Hard Assignments vs Soft Assignments</th>
<th><ul>
<li><p>hard assignment</p>
<ul>
<li><p>each point is assigned to exactly one cluster</p></li>
<li><p>some points may lie roughly between centers</p></li>
<li><p>so, hard assignment may be artificial</p></li>
</ul></li>
<li><p>soft assignments</p>
<ul>
<li><p>probabilistic model reflects uncertainty</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">9.1.1 Image Segmentation and Compression</td>
</tr>
<tr>
<td>Image Segmentation Example</td>
<td><ul>
<li><p>the textbook example applies <span class="math inline"><strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>s</strong></span> to color images by <strong>treating</strong> each <strong>pixel</strong> as a data <strong>point</strong> in a <span class="math inline"><strong>3</strong> <strong>−</strong> <strong>D</strong></span> RGB space</p>
<ul>
<li><p>one coordinate for</p>
<ul>
<li><p>red intensity</p></li>
<li><p>green intensity</p></li>
<li><p>blue intensity</p></li>
</ul></li>
</ul></li>
<li><p><span class="math inline"><strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>s</strong> </span></p>
<ul>
<li><p><strong>groups</strong> similar <strong>colors</strong> together</p></li>
<li><p><strong>redraws</strong> each pixel <strong>using</strong> the color of its <strong>assigned</strong> cluster <strong>center</strong></p></li>
<li><p>result is an image <strong>represented</strong> using <strong>only</strong> <span class="math inline"><strong>K</strong></span> <strong>colors</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Important Caveat for Example</td>
<td><ul>
<li><p>a major <strong>weakness</strong> is that it <strong>ignores</strong> spatial <strong>proximity</strong></p></li>
<li><p>two pixels <strong>far</strong> <strong>apart</strong> but <strong>similar</strong> in <strong>color</strong> may be put in the <strong>same</strong> <strong>cluster</strong></p></li>
<li><p><strong>nearby</strong> pixels are <strong>not</strong> <strong>treated</strong> as <strong>related</strong> just <strong>because</strong> they are <strong>adjacent</strong> in the image</p></li>
<li><p>this approach is <strong>simple</strong>, but <strong>not</strong> <strong>strong</strong> enough for general <strong>image</strong> <strong>segmentation</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Compression Viewpoint</td>
<td><ul>
<li><p>the <strong>same</strong> <strong>setup</strong> also gives a form of <strong>lossy</strong> <strong>compression</strong></p>
<ul>
<li><p><strong>instead</strong> of <strong>storing</strong> every <strong>original</strong> pixel <strong>vector</strong></p></li>
<li><p>store <strong>only</strong> the <strong>index</strong> <span class="math inline"><strong>k</strong></span> of the <strong>nearest</strong> <strong>cluster</strong> center</p></li>
<li><p>also, <strong>store</strong> the <span class="math inline"><strong>K</strong></span> center <strong>vectors</strong> themselves</p></li>
</ul></li>
<li><p>this is called <strong>vector</strong> <strong>quantization</strong></p></li>
<li><p>cluster <strong>centers</strong> are called <strong>code</strong>-<strong>book</strong> <strong>vectors</strong></p></li>
<li><p><strong>approximation</strong> is <strong>lossy</strong> because each original <strong>pixel</strong> is <strong>replaced</strong> by the <strong>nearest</strong> center, <strong>not</strong> <strong>preserved</strong> exactly</p></li>
</ul></td>
</tr>
<tr>
<td>Bit-Cost Calculation</td>
<td><ul>
<li><p>if an image has <span class="math inline"><strong>N</strong></span><strong>pixels</strong> and each RGB pixel uses <span class="math inline"><strong>24</strong></span> bits total</p></li>
</ul>
<p>rounded up as needed</p>
<ul>
<li><p>original image <strong>cost</strong> = <span class="math inline"><strong>24</strong><strong>N</strong> </span><strong>bits</strong></p></li>
<li><p><strong>compressed</strong> image <strong>cost</strong> = <span class="math inline"><strong>24</strong><strong>K</strong> <strong>+</strong> <strong>N</strong><strong>l</strong><strong>o</strong><strong>g</strong><sub><strong>2</strong></sub><strong>K</strong> </span><strong>bits</strong></p></li>
</ul>
<ul>
<li><p>for the <strong>image</strong> in the <strong>example</strong></p>
<ul>
<li><p>the <strong>original</strong> requires <strong>1,036,800 bits</strong></p></li>
</ul></li>
<li><p><strong>K-means-compressed</strong> versions require</p>
<ul>
<li><p><strong>43</strong>,<strong>248</strong> bits for <span class="math inline"><strong>K</strong> <strong>=</strong> <strong>2</strong></span></p></li>
<li><p><strong>86</strong>,<strong>472</strong> bits for <span class="math inline"><strong>K</strong> <strong>=</strong> <strong>3</strong></span></p></li>
<li><p><strong>173</strong>,<strong>040</strong> bits for <span class="math inline"><strong>K</strong> <strong>=</strong> <strong>10</strong></span></p></li>
</ul></li>
<li><p>these are <strong>4.2%</strong>, <strong>8.3%</strong>, and <strong>16.7%</strong> of the original size, respectively</p></li>
<li><p>the trade-off is clear, <strong>smaller</strong> <span class="math inline"><strong>K</strong></span> gives</p>
<ul>
<li><p><strong>more</strong> compression</p></li>
<li><p>smaller <strong>worse</strong> visual <strong>quality</strong></p></li>
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
<th colspan="2">Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td>Takeaway from Image Example</td>
<td><ul>
<li><p>shows that <strong>K-means</strong></p>
<ul>
<li><p><strong>clusters</strong> similar <strong>vectors</strong></p></li>
<li><p>can <strong>reduce</strong> <strong>data</strong> to a small codebook</p></li>
<li><p><strong>creates</strong> a direct <strong>trade</strong>-<strong>off</strong> between <strong>compression</strong> and <strong>fidelity</strong></p></li>
</ul></li>
</ul>
<p><strong>exploits</strong> local <strong>correlations</strong> in natural <strong>images</strong></p>
<ul>
<li><p>the text notes that <strong>for</strong> <strong>better</strong> image <strong>compression</strong></p>
<ul>
<li><p><strong>cluster</strong> small <strong>blocks</strong> of neighboring <strong>pixels</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><p>Overall Takeaways for</p>
<p>K-means</p></td>
<td><ul>
<li><p>K-means as an <strong>iterative</strong> <strong>algorithm</strong> that <strong>alternates</strong> between</p>
<ul>
<li><p><strong>assigning</strong> each point to its <strong>nearest</strong> <strong>center</strong></p></li>
<li><p><strong>updating</strong> each <strong>center</strong> to the <strong>mean</strong> of its <strong>assigned</strong> <strong>points</strong></p></li>
</ul></li>
<li><p><strong>properties</strong> of <span class="math inline"><strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>s</strong></span></p>
<ul>
<li><p><strong>minimizes</strong> within-cluster <strong>squared</strong> <strong>distance</strong></p></li>
<li><p><strong>converges</strong> to a <strong>local</strong> <strong>minimum</strong></p></li>
<li><p>uses <strong>hard</strong> <strong>assignments</strong></p></li>
<li><p>can be <strong>extended</strong> <strong>beyond</strong> <strong>Euclidean</strong> distance</p></li>
<li><p>can be <strong>applied</strong> <strong>to</strong> tasks like <strong>image</strong> <strong>segmentation</strong> and <strong>lossy</strong> <strong>compression</strong> through <strong>vector</strong> <strong>quantization</strong></p></li>
<li><p><strong>simplicity</strong> is its <strong>strength</strong></p></li>
<li><p>but is <strong>limited</strong> by <strong>assumptions</strong></p></li>
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
<th colspan="2">Async</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Clustering Goals</td>
</tr>
<tr>
<td>Two Classes of Learning Problems</td>
<td><ul>
<li><p><strong>supervised</strong> learning</p>
<ul>
<li><p>learning from pre-<strong>labeled</strong> <strong>data</strong></p>
<ul>
<li><p><strong>class labels</strong> (in classification)</p></li>
<li><p><strong>output values</strong> (regression)</p></li>
</ul></li>
<li><p><strong>train data:</strong> <span class="math inline">(<strong>X</strong><strong>,</strong> <strong>Y</strong>)</span>for inputs <span class="math inline"><strong>X</strong></span> and labels <span class="math inline"><strong>Y</strong></span></p></li>
</ul></li>
<li><p><strong>unsupervised</strong> learning</p>
<ul>
<li><p><strong>learning</strong> from <strong>unlabeled</strong>, <strong>unannotated</strong> data</p></li>
<li><p><strong>train data:</strong> <span class="math inline"><strong>X</strong></span> for unlabeled data</p></li>
</ul></li>
<li><p><strong>learn</strong> from salient <strong>patterns</strong> from the <strong>input</strong> <strong>features</strong> themselves</p></li>
</ul></td>
</tr>
<tr>
<td>Unsupervised Learning Methods</td>
<td><ul>
<li><p><strong>clustering</strong> methods</p>
<ul>
<li><p><strong>identify</strong> data <strong>groupings</strong></p></li>
<li><p><strong>non</strong>-<strong>probabilistic</strong> method</p>
<ul>
<li><p><strong>hierarchical</strong> clustering</p></li>
<li><p><strong>K-means</strong> algorithm</p></li>
</ul></li>
<li><p><strong>probabilistic</strong> method</p>
<ul>
<li><p><strong>mixture</strong> model</p></li>
</ul></li>
</ul></li>
<li><p><strong>density</strong> <strong>estimation</strong></p>
<ul>
<li><p><strong>determine</strong> data <strong>distribution</strong></p></li>
</ul></li>
<li><p><strong>dimensionality</strong> <strong>reduction</strong></p>
<ul>
<li><p>determine <strong>low-dimensional</strong> <strong>representation</strong></p></li>
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
<th>Clustering</th>
<th><ul>
<li><p>organizes data into clusters such that there is</p>
<ul>
<li><p>high intra-cluster similarity</p></li>
<li><p>low inter-cluster similarity</p></li>
</ul></li>
<li><p>optimal for finding natural groupings among objects</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Clustering as Lossy Compression</td>
</tr>
<tr>
<td>Data Shape</td>
<td><ul>
<li><p>data is <strong>stored</strong> as <strong>different</strong> data <strong>types</strong> with each having <strong>different</strong> <strong>sizes</strong> in memory</p></li>
<li><p>even <strong>within</strong> the <strong>same</strong> data <strong>type</strong> group – such as float – there are <strong>variations</strong> such as <strong>different</strong> degrees of <strong>precision</strong></p></li>
</ul></td>
</tr>
<tr>
<td>The Problem</td>
<td><ul>
<li><p>suppose you <strong>transmit</strong> the <strong>coordinates</strong> of points drawn <strong>randomly</strong> from this <strong>dataset</strong></p></li>
<li><p>you can <strong>install</strong> decoding <strong>software</strong> at the <strong>receiver</strong></p></li>
<li><p>you're <strong>only</strong> <strong>allowed</strong> to send <strong>two</strong> <strong>bits</strong> per point</p></li>
<li><p>this <strong>requires</strong> lossy <strong>compression</strong></p></li>
<li><p><strong>loss</strong> is <strong>defined</strong> as the <strong>sum</strong>-<strong>squared</strong> error between <strong>decoded</strong> coordinates and <strong>original</strong> coordinates</p></li>
</ul></td>
</tr>
<tr>
<td>Solutions: Minimizes Loss</td>
<td><ul>
<li><p><strong>simplified</strong> model</p></li>
</ul>
<p>send ‘<strong>00’</strong></p>
<p><strong>send</strong> the <strong>quadrant</strong> in the 2-D plane</p>
<p><strong>decoding:</strong></p>
<p>take the <strong>mean</strong> <strong>datapoint</strong> of the data <strong>clustered</strong> in that quadrant</p>
<p><strong>rezone</strong> partitions</p>
<p><strong>repeat</strong></p>
<p><strong>010</strong></p>
<p><strong>00</strong></p>
<p><strong>11</strong></p>
<p><strong>10</strong></p></td>
</tr>
<tr>
<td colspan="2">Optimizing Partitions and Centroids</td>
</tr>
<tr>
<td>K-Means</td>
<td><ul>
<li><p>ask user <strong>how</strong> <strong>many</strong> <strong>clusters</strong></p></li>
<li><p>randomly <strong>guess</strong> the <span class="math inline"><strong>k</strong></span> cluster <strong>center</strong> <strong>locations</strong></p></li>
<li><p>each datapoint <strong>determines</strong> which <strong>center</strong> is closest</p></li>
<li><p>each <strong>center</strong> “<strong>owns</strong>” a set of <strong>datapoints</strong></p></li>
<li><p>each center <strong>determines</strong> <strong>center</strong> of “owned” points</p></li>
<li><p><strong>center</strong> <strong>relocates</strong> to new position</p></li>
<li><p><strong>repeat</strong> until terminated</p></li>
</ul></td>
</tr>
<tr>
<td>K-Means Questions</td>
<td><ul>
<li><p><strong>what</strong> is it <strong>trying</strong> to <strong>optimize</strong>?</p></li>
<li><p>are we <strong>sure</strong> it <strong>will</strong> <strong>terminate</strong>?</p></li>
<li><p>are we <strong>sure</strong> it will <strong>find</strong> an <strong>optimal</strong> <strong>clustering</strong>?</p></li>
<li><p><strong>how</strong> should we <strong>start</strong> it?</p></li>
<li><p><strong>how</strong> could we <strong>automatically</strong> <strong>choose</strong> the <strong>number</strong> of <strong>centers</strong>?</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">K-Means Loss</td>
</tr>
<tr>
<td>Distortion</td>
<td><ul>
<li><p><strong>encoder</strong> function</p></li>
</ul>
<p><span class="math display">ℝ<sup><strong>m</strong></sup> <strong>→</strong> {<strong>1</strong><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>k</strong>}</span></p>
<ul>
<li><p><strong>decoder</strong> function</p></li>
</ul>
<p><span class="math display">{<strong>1</strong><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>k</strong>}<strong>→</strong> ℝ<sup><strong>m</strong></sup></span></p>
<ul>
<li><p><strong>define</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{Distortion\ }\mathbf{= \ }\sum_{\mathbf{i = 1}}^{\mathbf{R}}\left( \mathbf{\ }\mathbf{x}_{\mathbf{i}}\mathbf{- \ DECODE}\left( \mathbf{\ }\mathbf{ENCODE}\left( \mathbf{x}_{\mathbf{i}} \right) \right) \right)^{\mathbf{2}}$$</span></p>
<ul>
<li><p>if we set,</p></li>
</ul>
<p><span class="math inline"><strong>D</strong><strong>E</strong><strong>C</strong><strong>O</strong><strong>D</strong><strong>E</strong>[<strong>j</strong>]<strong>=</strong><strong>c</strong><sub><strong>j</strong></sub></span> then,</p>
<p><span class="math display">$$\mathbf{Distortion\ }\mathbf{= \ }\sum_{\mathbf{i = 1}}^{\mathbf{R}}\left( \mathbf{\ }\mathbf{x}_{\mathbf{i}}\mathbf{- \ }\mathbf{c}_{\mathbf{ENCODE}\left( \mathbf{x}_{\mathbf{i}} \right)} \right)^{\mathbf{2}}$$</span></p></td>
</tr>
<tr>
<td colspan="2">Minimizing Loss With Respect to Partitions</td>
</tr>
<tr>
<td>The Minimal Distortion</td>
<td><p><span class="math display">$$\mathbf{Distortion\ }\mathbf{= \ }\sum_{\mathbf{i = 1}}^{\mathbf{R}}\left( \mathbf{\ }\mathbf{x}_{\mathbf{i}}\mathbf{- \ }\mathbf{c}_{\mathbf{ENCODE}\left( \mathbf{x}_{\mathbf{i}} \right)} \right)^{\mathbf{2}}$$</span></p>
<ul>
<li><p>what <strong>priorities</strong> must <strong>cluster</strong> <strong>assignments</strong> have when <strong>distortions</strong> <strong>minimized</strong>?</p>
<ul>
<li><p><span class="math inline"><strong>x</strong><sub><strong>i</strong></sub></span> must be <strong>encoded</strong> by its <strong>nearest</strong> <strong>center</strong></p></li>
</ul></li>
</ul>
<blockquote>
<p><span class="math display">$$\mathbf{c}_{\mathbf{ENCODEI}\mathbf{(x}_{\mathbf{i}}\mathbf{)}}\mathbf{=}\begin{matrix}
\mathbf{argmin} \\
\mathbf{c}_{\mathbf{j}}\mathbf{\in}\left\{ \mathbf{c}_{\mathbf{1}}\mathbf{,}\mathbf{c}_{\mathbf{2}}\mathbf{,\ldots,}\mathbf{c}_{\mathbf{k}} \right\}
\end{matrix}\left( \mathbf{x}_{\mathbf{i}}\mathbf{-}\mathbf{c}_{\mathbf{j}} \right)^{\mathbf{2}}$$</span></p>
<p>at the <strong>minimal</strong> <strong>distortion</strong></p>
</blockquote></td>
</tr>
<tr>
<td colspan="2">Minimizing Loss With Respect to Centroids</td>
</tr>
<tr>
<td>The Minimal Distortion (2)</td>
<td><ul>
<li><p>what <strong>properties</strong> must <strong>centers</strong> <span class="math inline"><strong>c</strong><sub><strong>1</strong></sub><strong>,</strong><strong>c</strong><sub><strong>2</strong></sub><strong>,</strong> <strong>…</strong><strong>,</strong><strong>c</strong><sub><strong>k</strong></sub></span> have when <strong>distortion</strong> is <strong>minimized</strong>?</p></li>
<li><p>the <strong>partial</strong> <strong>derivative</strong> of <strong>distortion</strong> with respect to each <strong>center</strong> <strong>location</strong> must be <strong>zero</strong></p></li>
<li><p>this is a <strong>convex</strong> <strong>problem</strong>, so the <strong>minimum</strong> is where the <strong>derivative</strong> <strong>equals</strong> <strong>zero</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Steps</td>
<td><ul>
<li><p>from above: the <strong>partial</strong> <strong>derivative</strong> of <strong>distortion</strong> with respect to each <strong>center</strong> <strong>location</strong> must be <strong>zero</strong></p></li>
</ul>
<p><strong>OwnedBy(c_j):</strong></p>
<p>the set of records owned by center <span class="math inline"><em>c</em><sub><em>j</em></sub></span></p>
<p><span class="math display">$$Distortion\  = \ \sum_{\mathbf{i = 1}}^{\mathbf{R}}\left( \mathbf{x}_{\mathbf{i}}\mathbf{- \ }\mathbf{c}_{\mathbf{ENCODE}\left( \mathbf{x}_{\mathbf{i}} \right)} \right)^{\mathbf{2}}$$</span></p>
<blockquote>
<p><span class="math display">$$\ \ \ \ \ \ \ \ \ \ \  = \ \sum_{\mathbf{j = 1}}^{\mathbf{k}}{\sum_{\mathbf{i\  \in}\mathbf{\ OwnedBy}\left( \mathbf{c}_{\mathbf{j}} \right)}^{}\left( \mathbf{x}_{\mathbf{i}}\mathbf{- \ }\mathbf{c}_{\mathbf{j}} \right)^{\mathbf{2}}}$$</span></p>
<p><span class="math inline">$\frac{\partial Distortion}{\partial c_{j}}$</span> <span class="math inline">$= \frac{\partial}{\partial c_{j}}\sum_{i\  \in \ OwnedBy\left( c_{j} \right)}^{}\left( x_{i} - \ c_{j} \right)^{2}$</span></p>
<p><span class="math display">$$= \  - 2\ \sum_{i\  \in \ OwnedBy\left( c_{j} \right)}^{}\left( x_{i} - \ c_{j} \right)$$</span></p>
</blockquote>
<p><span class="math display">= 0   (<em>f</em><em>o</em><em>r</em> <em>a</em> <em>m</em><em>i</em><em>n</em><em>i</em><em>m</em><em>u</em><em>m</em>)</span></p></td>
</tr>
<tr>
<td colspan="2">Alternating and Convergence</td>
</tr>
<tr>
<td>At the Minimum Distortion</td>
<td><ul>
<li><p>what <strong>properties</strong> must <strong>centers</strong> <span class="math inline"><strong>c</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>c</strong><sub><strong>2</strong></sub><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>c</strong><sub><strong>k</strong></sub></span> have when <strong>distortion</strong> is <strong>minimized</strong>?</p>
<ul>
<li><p><span class="math inline"><strong>x</strong><sub><strong>i</strong></sub></span> must be <strong>encoded</strong> by its <strong>nearest</strong> <strong>center</strong></p></li>
<li><p>each <strong>center</strong> must be at the <strong>centroid</strong> of “<strong>owned</strong>” points</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td rowspan="2">Improving a Sub-Optimal Configuration</td>
<td><ul>
<li><p>what <strong>properties</strong> must be changed for <strong>centers</strong> <span class="math inline"><strong>c</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>c</strong><sub><strong>2</strong></sub><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>c</strong><sub><strong>k</strong></sub></span> when <strong>distortion</strong> is <strong>minimized</strong>?</p>
<ul>
<li><p>change the <strong>encoding</strong> so that <span class="math inline"><strong>x</strong><sub><strong>i</strong></sub></span> is <strong>encoded</strong> by its <strong>nearest</strong> <strong>center</strong></p></li>
<li><p>set each <strong>center</strong> to the <strong>centroid</strong> of “<strong>owned</strong>” points</p></li>
</ul></li>
<li><p><strong>neither</strong> operation is <strong>repeated</strong> in <strong>succession</strong></p></li>
<li><p>the <strong>approach</strong> must be <strong>alternation</strong> (<strong>K</strong>-<strong>means</strong>)</p></li>
</ul></td>
</tr>
<tr>
<td><ul>
<li><p>there are only a <strong>finite</strong> <strong>number</strong> of ways of partitioning <span class="math inline"><strong>R</strong></span> <strong>records</strong> into <span class="math inline"><strong>k</strong></span> <strong>groups</strong></p></li>
<li><p>so, there are <strong>only</strong> a <strong>finite</strong> <strong>number</strong> of possible <strong>configurations</strong> in which <strong>all</strong> <strong>centers</strong> are the <strong>centroids</strong> of the <strong>points</strong> they <strong>own</strong></p></li>
<li><p>if the <strong>configuration</strong> <strong>changes</strong> on an <strong>iteration</strong>, it must have <strong>improved</strong> the <strong>distortion</strong></p></li>
<li><p>therefore, each time the <strong>configuration</strong> <strong>changes</strong>, it must <strong>move</strong> to a <strong>configuration</strong> it has <strong>never</strong> <strong>been</strong> to before</p></li>
<li><p>if it <strong>tried</strong> to go on <strong>forever</strong>, it would <strong>eventually</strong> run out of <strong>configurations</strong></p></li>
</ul></td>
</tr>
<tr>
<td>K-Means Algorithm</td>
<td><ul>
<li><p>decide on a value for <span class="math inline"><strong>K</strong></span></p></li>
<li><p>initialize the <span class="math inline"><strong>K</strong></span> cluster centers randomly if necessary</p></li>
<li><p>decide the <strong>class</strong> <strong>memberships</strong> of the <span class="math inline"><strong>N</strong></span> objects by <strong>assigning</strong> them to the <strong>nearest</strong> <strong>cluster</strong> <strong>centroids</strong> (aka the center of gravity or mean)</p></li>
<li><p><strong>reestimate</strong> the <span class="math inline"><strong>K</strong></span> cluster <strong>centers</strong>, by assuming the <strong>memberships</strong> <strong>found</strong> above are <strong>correct</strong></p></li>
</ul>
<p><span class="math display">$${\widehat{\mathbf{\mu}}}_{\mathbf{k}}\mathbf{= \ }\left( \frac{\mathbf{1}}{\mathbf{C}_{\mathbf{k}}} \right)\sum_{\mathbf{i\  \in \ }\mathbf{C}_{\mathbf{k}}}^{}\mathbf{x}_{\mathbf{i}}$$</span></p>
<ul>
<li><p>if <strong>none</strong> of the <span class="math inline"><strong>N</strong></span> objects <strong>changed</strong> <strong>membership</strong> in the <strong>last</strong> <strong>iteration</strong>, exit</p></li>
<li><p>otherwise, <strong>repeat</strong> the <strong>process</strong> starting from the <strong>membership</strong> <strong>assignment</strong> step</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Local Minima and Initialization</td>
</tr>
<tr>
<td>Optimal Solution</td>
<td><ul>
<li><p>the <strong>optimal</strong> <strong>solution</strong> is <strong>not</strong> <strong>necessarily</strong> reached</p></li>
</ul>
<p>can you think of a configuration that converges to a state that does not have the minimum distortion?</p></td>
</tr>
<tr>
<td>Trying to Find Good Optima</td>
<td><ul>
<li><p><strong>choose</strong> a <strong>logical</strong> <strong>starting</strong> point</p></li>
<li><p>do <strong>many</strong> <span class="math inline"><strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>s</strong></span> runs from <strong>different</strong> start <strong>locations</strong></p></li>
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
<th></th>
<th><p>“<em>neat trick</em>”</p>
<ul>
<li><p>place first center on top of randomly chosen dataponit</p></li>
<li><p>place second center on data point that is as far away as possible form the first placement</p></li>
<li><p>place the <span class="math inline"><strong>j</strong><sup><strong>t</strong><strong>h</strong></sup></span> center on the datapoint that is as far away as possible from the closest of centers <span class="math inline"><strong>1</strong></span> through <span class="math inline"><strong>j</strong> <strong>−</strong> <strong>1</strong></span></p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Choosing K</td>
</tr>
<tr>
<td>Choosing K According to Distortion</td>
<td><ul>
<li><p>purely <strong>choosing</strong> according to <strong>distortion</strong> typically does <strong>not</strong> sufficiently <strong>solve</strong> for <span class="math inline"><strong>K</strong> <strong>−</strong> <strong>m</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>s</strong></span> and/or <strong>clustering</strong></p></li>
<li><p><strong>larger</strong> <span class="math inline"><strong>K</strong></span> values lead to <strong>less</strong> <strong>distortion</strong> but is <strong>not</strong> <strong>conducive</strong> to <strong>determinig</strong> clustering <strong>groups</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Choosing the Number of Centers</td>
<td><ul>
<li><p>the most <strong>common</strong> approach is to try to <strong>find</strong> the <strong>solution</strong> that <strong>minimizes</strong> the <strong>Schwarz</strong> <strong>Criterion</strong> (also related to the <strong>BIC</strong>)</p></li>
</ul>
<p>m = # dimensions</p>
<p>k = # centers</p>
<p>R = # records</p>
<p><span class="math display"><strong>D</strong><strong>i</strong><strong>s</strong><strong>t</strong><strong>o</strong><strong>r</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong> <strong>+</strong> <strong>λ</strong>(<strong>#</strong> <strong>p</strong><strong>a</strong><strong>r</strong><strong>a</strong><strong>m</strong><strong>e</strong><strong>t</strong><strong>e</strong><strong>r</strong><strong>s</strong>)<strong>log</strong> <strong>R</strong></span></p>
<p><span class="math display"><strong>=</strong> <strong>D</strong><strong>i</strong><strong>s</strong><strong>t</strong><strong>o</strong><strong>r</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong> <strong>+</strong> <strong>λ</strong> <strong>m</strong> <strong>k</strong><strong>log</strong> <strong>R</strong></span></p></td>
</tr>
<tr>
<td>Plot Objective Function Values of K = 1 to 6</td>
<td><ul>
<li><p>we can <strong>plot</strong> the <strong>objective</strong> function <strong>values</strong> for <span class="math inline"><strong>k</strong> <strong>=</strong> <strong>1</strong> <strong>t</strong><strong>o</strong> <strong>6</strong></span></p></li>
<li><p>the abrupt <strong>change</strong> at <span class="math inline"><strong>k</strong> <strong>=</strong> <strong>2</strong></span> is highly <strong>suggestive</strong> of <strong>two</strong> <strong>clusters</strong> in the data</p></li>
<li><p>this technique for <strong>determining</strong> the <strong>number</strong> of <strong>clusters</strong> is known as “<strong>knee</strong> <strong>finding</strong>” or “<strong>elbow</strong> <strong>finding</strong>”</p></li>
</ul>
<p><img src="generated_media\DATA780_week10_notes\media\image15.png" style="width:2.90698in;height:1.80252in" /></p>
<p>ChatGPT 5.3</p></td>
</tr>
<tr>
<td colspan="2">Applications</td>
</tr>
<tr>
<td>Common Uses of K-Means</td>
<td><ul>
<li><p>often used as an <strong>exploratory</strong> data <strong>analysis</strong> tool</p></li>
<li><p>in <strong>one</strong> <strong>dimension</strong>, a good way to <strong>quantize</strong> real-valued <strong>variables</strong> into <span class="math inline"><strong>k</strong></span> non-uniform <strong>buckets</strong></p></li>
<li><p>used on <strong>acoustic</strong> data, in <strong>speech</strong> <strong>understanding</strong>, to convert <strong>waveforms</strong> into one of <span class="math inline"><strong>k</strong></span> <strong>categories</strong> (known as <strong>vector</strong> <strong>quantization</strong>)</p></li>
<li><p>also used for <strong>choosing</strong> color <strong>palettes</strong> on old-fashioned <strong>graphical</strong> <strong>display</strong> devices</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Hierarchical Clustering</td>
</tr>
<tr>
<td>Two Types of Clustering</td>
<td><ul>
<li><p><strong>hierarchical</strong> algorithms</p>
<ul>
<li><p><strong>create</strong> a hierarchical <strong>decomposition</strong> of the set of <strong>objects</strong> using some criterion</p></li>
</ul></li>
<li><p><strong>partitioning</strong> algorithms</p>
<ul>
<li><p><img src="generated_media\DATA780_week10_notes\media\image16.png" style="width:3.27847in;height:2.05486in" /><strong>construct</strong> various <strong>partitions</strong> and then <strong>evaluate</strong> them by some criterion</p></li>
</ul></li>
</ul>
<p>ChatGPT 5.4</p></td>
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
<th><p>Hierarchical Clustering</p>
<p>(How To)</p></th>
<th><ul>
<li><p>bottom-up (agglomerative)</p>
<ul>
<li><p>starting with each item in its own cluster, find the best pair to merge into a new cluster</p></li>
<li><p>repeat until all clusters have “fused” together</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Agglomerating Clusters</td>
</tr>
<tr>
<td>Distance Matrix</td>
<td><ul>
<li><p><img src="generated_media\DATA780_week10_notes\media\image17.png" style="width:2.16279in;height:0.96806in" />contains the <strong>distances</strong> between <strong>every</strong> <strong>pair</strong> of objects in a <strong>database</strong></p></li>
</ul>
<p><img src="generated_media\DATA780_week10_notes\media\image18.png" style="width:0.45349in;height:0.74355in" /></p>
<p><img src="generated_media\DATA780_week10_notes\media\image19.png" style="width:0.40937in;height:0.66279in" /><img src="generated_media\DATA780_week10_notes\media\image18.png" style="width:0.30633in;height:0.68473in" /><img src="generated_media\DATA780_week10_notes\media\image20.png" style="width:0.36819in;height:0.7907in" /><img src="generated_media\DATA780_week10_notes\media\image21.png" style="width:0.35227in;height:0.72093in" /><img src="generated_media\DATA780_week10_notes\media\image22.png" style="width:0.34474in;height:0.7093in" /></p>
<p>similarity assessment: greater value = greater distance (less similar)</p>
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">0</th>
<th style="text-align: center;">3</th>
<th style="text-align: center;">2</th>
<th style="text-align: center;">7</th>
<th style="text-align: center;">8</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">0</td>
</tr>
</tbody>
</table>
<p><img src="generated_media\DATA780_week10_notes\media\image20.png" style="width:0.33009in;height:0.70888in" /><img src="generated_media\DATA780_week10_notes\media\image18.png" style="width:0.30633in;height:0.68473in" /><img src="generated_media\DATA780_week10_notes\media\image22.png" style="width:0.30521in;height:0.62791in" /><img src="generated_media\DATA780_week10_notes\media\image19.png" style="width:0.40937in;height:0.66279in" /></p>
<p>D( , ) = 3</p>
<p>D( , ) = 3</p></td>
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
<th>Bottom Up (Agglomerative)</th>
<th><ul>
<li><p>start with each item in its own cluster</p></li>
<li><p>find the best pair to merge into a new cluster</p></li>
<li><p>repeat until all clusters fuse together</p></li>
</ul>
<p>consider all possible combinations</p>
<p>choose the best one</p>
<p><img src="generated_media\DATA780_week10_notes\media\image23.png" style="width:0.20694in;height:0.4625in" /><img src="generated_media\DATA780_week10_notes\media\image24.png" style="width:0.23819in;height:0.51181in" /><img src="generated_media\DATA780_week10_notes\media\image21.png" style="width:0.24565in;height:0.50273in" /><img src="generated_media\DATA780_week10_notes\media\image21.png" style="width:0.24565in;height:0.50273in" /><img src="generated_media\DATA780_week10_notes\media\image19.png" style="width:0.30233in;height:0.48948in" /><img src="generated_media\DATA780_week10_notes\media\image22.png" style="width:0.25581in;height:0.52633in" /><img src="generated_media\DATA780_week10_notes\media\image19.png" style="width:0.30233in;height:0.48948in" /></p>
<p>…</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Linking Options</td>
</tr>
<tr>
<td rowspan="3">Computing Distance Between Clusters</td>
<td><ul>
<li><p><strong>single</strong> link</p>
<ul>
<li><p>cluster <strong>distance</strong> = distance of <strong>two</strong> <strong>closest</strong> members of <strong>each</strong> <strong>class</strong></p></li>
</ul></li>
</ul>
<p>optimal for long, skinny clusters</p>
<p>the shortest measured distance corresponds to the most similarity and they would be merged</p></td>
</tr>
<tr>
<td><ul>
<li><p><strong>complete</strong> link</p>
<ul>
<li><p>cluster <strong>distance</strong><img src="generated_media\DATA780_week10_notes\media\image32.png" style="width:2.65662in;height:1.48979in" /> = distance of the <strong>two</strong> <strong>farthest</strong> members</p></li>
</ul></li>
</ul>
<p>optimal for tight clusters</p></td>
</tr>
<tr>
<td><ul>
<li><p><strong>average</strong> link</p></li>
</ul>
<p>most used: most robust to noise</p>
<ul>
<li><p>cluster <strong>distance</strong> =</p></li>
</ul>
<blockquote>
<p><strong>average</strong> <strong>distance</strong> of <strong>all</strong> pairs</p>
</blockquote></td>
</tr>
</tbody>
</table>
