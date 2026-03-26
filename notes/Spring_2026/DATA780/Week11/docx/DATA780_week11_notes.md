> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week11_notes.pdf](../DATA780_week11_notes.pdf)
> - DOCX: [DATA780_week11_notes.docx](DATA780_week11_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Dimensionality Reduction</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td colspan="2" style="text-align: right;"><em>23 Mar 2026</em></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>feature vectors</p></li>
<li><p>data manifold</p></li>
<li><p>how Principal Component Analysis finds a linear subspace</p></li>
<li><p>applications in images and data visualization</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Reading</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><p>Pattern Recognition and Machine Learning</p>
<p>12.1: Principal Component Analysis (PCA)</p></td>
</tr>
<tr>
<td colspan="5">Principal Component Analysis</td>
</tr>
<tr>
<td>Core Idea</td>
<td colspan="4"><ul>
<li><p><strong>PCA</strong> is a method for <strong>finding</strong> a <strong>lower</strong>-<strong>dimensional</strong> representation of data that <strong>preserves</strong> as much of the <strong>important</strong> <strong>structure</strong> as possible</p></li>
<li><p>PCA <strong>looks</strong> for a small number of <strong>new</strong> <strong>axes</strong>, called <strong>principal</strong> <strong>components</strong>, such that:</p>
<ul>
<li><p>the projected <strong>data</strong> <strong>varies</strong> as <strong>much</strong> as <strong>possible</strong> along those axes</p></li>
<li><p>the <strong>axes</strong> are mutually <strong>orthogonal</strong></p></li>
<li><p>the <strong>lower</strong>-<strong>dimensional</strong> representation <strong>loses</strong> as <strong>little</strong> <strong>information</strong> as possible <strong>under</strong> a <strong>squared</strong>-<strong>error</strong> notion of <strong>reconstruction</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Why PCA is Useful</td>
<td colspan="4"><ul>
<li><p><strong>real</strong> <strong>data</strong> often <strong>lives</strong> in a <strong>high</strong>-<strong>dimensional</strong> space</p></li>
<li><p>the <strong>true</strong> <strong>degrees</strong> of <strong>freedom</strong> may be <strong>much</strong> <strong>smaller</strong></p></li>
<li><p><strong>PCA</strong> <strong>helps</strong> by:</p>
<ul>
<li><p>reducing <strong>dimensionality</strong></p></li>
<li><p><strong>compressing</strong> data</p></li>
<li><p>removing <strong>redundancy</strong> caused by <strong>correlated</strong> <strong>variables</strong></p></li>
<li><p>making <strong>visualization</strong> <strong>easier</strong></p></li>
<li><p><strong>preparing</strong> data for <strong>later</strong> <strong>modeling</strong> steps</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Setup</td>
<td colspan="4"><ul>
<li><p>suppose <strong>each</strong> data <strong>point</strong> is a <strong>vector</strong></p></li>
</ul>
<p><span class="math display"><strong>x</strong><sub><strong>n</strong></sub> <strong>∈</strong> <strong>R</strong><sup><strong>D</strong></sup></span></p>
<ul>
<li><p>PCA first <strong>centers</strong> the <strong>data</strong> by <strong>subtracting</strong> the sample <strong>mean</strong>, so the <strong>transformed</strong> data has <strong>mean</strong> <span class="math inline"><strong>0</strong></span></p></li>
<li><p>then, <strong>studies</strong> the sample <strong>covariance</strong> <strong>matrix</strong>, whose <strong>eigenvectors</strong> <strong>determine</strong> the principal <strong>directions</strong></p></li>
<li><p>in <strong>Bishop’s</strong> development, the <strong>principal</strong> <strong>components</strong> are obtained from the <strong>eigenvalue</strong> <strong>problem</strong> for the <strong>covariance</strong> <strong>matrix</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">View 1: Maximum-Variance Formulation</td>
</tr>
<tr>
<td>Idea</td>
<td colspan="4"><ul>
<li><p>the <strong>first</strong> principal <strong>component</strong> is the <strong>direction</strong> onto which the projected <strong>data</strong> has the <strong>largest</strong> possible <strong>variance</strong></p></li>
<li><p><strong>Then</strong>:</p>
<ul>
<li><p>the <strong>second</strong> principal <strong>component</strong> is the <strong>direction</strong> of <strong>largest</strong> <strong>remaining</strong> variance</p></li>
<li><p>it must be <strong>orthogonal</strong> to the <strong>first</strong></p></li>
<li><p>the <strong>third</strong> is <strong>orthogonal</strong> to the <strong>first</strong> <strong>two</strong></p></li>
<li><p>and <strong>so</strong> <strong>on</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Key Result</td>
<td colspan="4"><ul>
<li><p>the <strong>optimal</strong> <strong>directions</strong> are the <strong>eigenvectors</strong> of the <strong>covariance</strong> <strong>matrix</strong></p>
<ul>
<li><p>the <strong>eigenvector</strong> with the <strong>largest</strong> <strong>eigenvalue</strong> gives the <strong>first</strong> principal <strong>component</strong></p></li>
<li><p>the <strong>next</strong> largest <strong>eigenvalue</strong> gives the <strong>second</strong> <strong>component</strong></p></li>
<li><p><strong>larger</strong> eigenvalue = <strong>more</strong> <strong>variance</strong> explained by that component</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="5">View 2: Minimum-Error Formulation</td>
</tr>
<tr>
<td>Idea</td>
<td colspan="4"><ul>
<li><p><strong>PCA</strong> can also be <strong>derived</strong> as a <strong>reconstruction</strong> problem</p></li>
<li><p><strong>project</strong> the <strong>data</strong> into a <strong>lower</strong>-<strong>dimensional</strong> subspace</p></li>
<li><p>then <strong>reconstruct</strong> it <strong>back</strong> into the <strong>original</strong> space</p></li>
<li><p><strong>choose</strong> the <strong>subspace</strong> that <strong>minimizes</strong> the <strong>average</strong> <strong>squared</strong> reconstruction <strong>error</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Important Conclusion</td>
<td colspan="4"><ul>
<li><p>the <strong>solution</strong> to this <strong>minimum</strong>-<strong>error</strong> <strong>problem</strong> is the same <strong>subspace</strong> found by the <strong>maximum</strong>-<strong>variance</strong> approach</p></li>
<li><p>so <strong>PCA</strong> has <strong>two</strong> equivalent <strong>interpretations</strong>:</p>
<ul>
<li><p>keep <strong>directions</strong> of <strong>largest</strong> <strong>variance</strong></p></li>
<li><p><strong>minimize</strong> information <strong>loss</strong> under <strong>squared</strong> <strong>reconstruction</strong> error</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Reconstruction picture</td>
<td colspan="4"><ul>
<li><p>if you <strong>keep</strong> only <span class="math inline"><strong>M</strong><strong>&lt;</strong><strong>D</strong></span> principal <strong>components</strong>:</p>
<ul>
<li><p>each <strong>point</strong> is <strong>projected</strong> onto an <span class="math inline"><strong>M</strong><strong>−</strong><strong>d</strong><strong>i</strong><strong>m</strong><strong>e</strong><strong>n</strong><strong>s</strong><strong>i</strong><strong>o</strong><strong>n</strong><strong>a</strong><strong>l</strong></span> linear <strong>subspace</strong></p></li>
<li><p>the <strong>reconstruction</strong> is the <strong>closest</strong> <strong>point</strong> to the <strong>original</strong> <strong>data</strong> point within that <strong>subspace</strong></p></li>
<li><p>the <strong>discarded</strong> <strong>components</strong> correspond to <strong>lost</strong> <strong>information</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Choosing Fewer Dimensions</td>
<td colspan="4"><ul>
<li><p>if you <strong>keep</strong> only the <strong>first</strong> <strong>few</strong> principal <strong>components</strong>, you get a <strong>compressed</strong> <strong>representation</strong></p></li>
<li><p>this <strong>works</strong> <strong>well</strong> when:</p>
<ul>
<li><p>the <strong>first</strong> few <strong>eigenvalues</strong> are much <strong>larger</strong> than the rest</p></li>
<li><p><strong>most</strong> <strong>variance</strong> is <strong>concentrated</strong> in a <strong>small</strong> number of <strong>directions</strong></p></li>
</ul></li>
<li><p>in that case, the <strong>data</strong> can be <strong>approximated</strong> <strong>well</strong> using a <strong>low</strong>-<strong>dimensional</strong> linear <strong>manifold</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">High-Dimensional Data Case</td>
</tr>
<tr>
<td>Large Dimensionality Case</td>
<td colspan="4"><ul>
<li><p>directly solving the <strong>covariance</strong> <strong>eigenvalue</strong> problem can be <strong>expensive</strong></p></li>
<li><p>a <strong>useful</strong> <strong>trick</strong> is to <strong>work</strong> with a <strong>matrix</strong> involving <strong>inner</strong> <strong>products</strong> between <strong>data</strong> points <strong>instead</strong></p></li>
<li><p>this is especially <strong>helpful</strong> when the <strong>number</strong> of <strong>data</strong> <strong>points</strong> is <strong>smaller</strong> than the <strong>ambient</strong> <strong>dimension</strong></p></li>
<li><p>the <strong>nonzero</strong> <strong>eigenvalues</strong> are <strong>shared</strong> across these <strong>equivalent</strong> <strong>formulations</strong></p></li>
<li><p>this matters because <strong>PCA</strong> is <strong>often</strong> <strong>applied</strong> in settings like:</p>
<ul>
<li><p><strong>images</strong></p></li>
<li><p>text <strong>features</strong></p></li>
<li><p>other very <strong>high</strong>-<strong>dimensional</strong> <strong>observations</strong></p></li>
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
<col style="width: 28%" />
<col style="width: 10%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr>
<th colspan="4">What PCA is Actually Finding</th>
</tr>
</thead>
<tbody>
<tr>
<td>PCA Finds a Linear Subspace</td>
<td colspan="3"><ul>
<li><p><strong>assumes</strong> the important <strong>structure</strong> can be <strong>captured</strong> by straight-line <strong>combinations</strong> of <strong>basis</strong> directions</p></li>
<li><p>does <strong>not</strong> <strong>model</strong> nonlinear <strong>curved</strong> <strong>manifolds</strong></p></li>
<li><p>later <strong>methods</strong> in the chapter <strong>extend</strong> this <strong>idea</strong> <strong>probabilistically</strong> and <strong>nonlinearly</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Limits of PCA</td>
<td colspan="3"><ul>
<li><p>it is <strong>linear</strong></p></li>
<li><p>it is <strong>driven</strong> by <strong>variance</strong>, <strong>not</strong> necessarily by <strong>task</strong> <strong>relevance</strong></p></li>
<li><p>large <strong>variance</strong> <strong>directions</strong> are <strong>not</strong> always the most <strong>meaningful</strong> for <strong>prediction</strong></p></li>
<li><p>it is <strong>sensitive</strong> to variable <strong>scaling</strong> unless <strong>preprocessing</strong> is done carefully</p></li>
<li><p>standard <strong>PCA</strong> is <strong>not</strong> a full <strong>probabilistic</strong> <strong>model</strong> in this <strong>initial</strong> <strong>formulation</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Summary</td>
</tr>
<tr>
<td><p>PCA</p>
<p>Section 12.1</p></td>
<td colspan="3"><ul>
<li><p>can be <strong>understood</strong> as:</p>
<ul>
<li><p>a way to <strong>find</strong> a <strong>low</strong>-<strong>dimensional</strong> representation of <strong>high</strong>-<strong>dimensional</strong> data</p></li>
<li><p>a method <strong>based</strong> on <strong>eigenvectors</strong> of the <strong>covariance</strong> <strong>matrix</strong></p></li>
<li><p>a <strong>maximum</strong>-<strong>variance</strong> method</p></li>
<li><p>equivalently, a <strong>minimum</strong> <strong>squared</strong> <strong>reconstruction</strong> error method</p></li>
<li><p>a <strong>linear</strong> <strong>dimensionality</strong> <strong>reduction</strong> technique that <strong>prepares</strong> the ground for <strong>probabilistic</strong> <strong>PCA</strong> and related <strong>latent</strong>-<strong>variable</strong> <strong>models</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Dimensionality Reduction</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4">Another Type of Unsupervised Learning Task</td>
</tr>
<tr>
<td>Supervised vs Unsupervised Learning</td>
<td colspan="2"><p><strong>Supervised</strong> Learning</p>
<ul>
<li><p>data: <span class="math inline"><strong>(</strong><strong>x</strong><strong>,</strong> <strong>y</strong><strong>)</strong></span></p>
<ul>
<li><p><span class="math inline"><strong>x</strong></span> is <strong>data</strong></p></li>
<li><p><span class="math inline"><strong>y</strong></span> is <strong>label</strong></p></li>
</ul></li>
<li><p>goal:</p>
<ul>
<li><p>learn a <strong>function</strong> to <strong>map</strong> <span class="math inline"><strong>x</strong> <strong>→</strong> <strong>y</strong></span></p></li>
</ul></li>
<li><p>examples:</p>
<ul>
<li><p><strong>classification</strong></p></li>
<li><p>regression</p></li>
<li><p><strong>object</strong> <strong>detection</strong></p></li>
<li><p>semantic <strong>segmentation</strong></p></li>
<li><p>image <strong>captioning</strong></p></li>
</ul></li>
</ul></td>
<td><p><strong>Unsupervised</strong> Learning</p>
<ul>
<li><p>data: <span class="math inline"><strong>x</strong> </span></p>
<ul>
<li><p>just <strong>data</strong></p></li>
<li><p><strong>no</strong> <strong>labels</strong></p></li>
</ul></li>
<li><p>goal:</p>
<ul>
<li><p><strong>learn</strong> underlying <strong>hidden</strong> <strong>structure</strong> of the data</p></li>
</ul></li>
<li><p>examples:</p>
<ul>
<li><p><strong>clustering</strong></p></li>
<li><p>dimensionality <strong>reduction</strong></p></li>
<li><p>feature <strong>learning</strong></p></li>
<li><p>density <strong>estimation</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Dimensionality Reduction</td>
<td colspan="3"><ul>
<li><p><strong>unsupervised</strong> learning <strong>method</strong></p></li>
<li><p>discovering the <strong>degrees</strong> <strong>of</strong> <strong>freedom</strong> of the underlying instances</p></li>
<li><p>what are the <strong>core</strong> <strong>dimensions</strong> of the dataset</p></li>
</ul></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 39%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr>
<th colspan="3">Linear Encoder and Decoder</th>
</tr>
</thead>
<tbody>
<tr>
<td>Encode</td>
<td colspan="2"><ul>
<li><p>for 3-D data, <strong>encoding</strong> converts the <strong>3-D data to 2-D</strong></p></li>
</ul>
<p><img src="generated_media\DATA780_week11_notes\media\image1.png" style="width:3.12791in;height:1.59384in" /></p>
<p>ChatGPT 5.4</p>
<ul>
<li><p>data preparation (<strong>normalization</strong>)</p></li>
<li><p><strong>compute</strong> the <strong>covariance</strong> <strong>matrix</strong> </p></li>
<li><p><img src="generated_media\DATA780_week11_notes\media\image2.gif" />apply <strong>SVD</strong></p></li>
<li><p><strong>project</strong> the 3-D <strong>vertices</strong> onto the <strong>plane</strong> formed by the <strong>first</strong> <strong>two</strong> <strong>eigenvectors</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Decode</td>
<td colspan="2"><ul>
<li><p>for 3-D data, <strong>decoding</strong> converts the <strong>2-D data back to 3-D</strong></p></li>
</ul>
<p><img src="generated_media\DATA780_week11_notes\media\image3.png" style="width:3.12791in;height:1.59384in" /></p>
<p><strong>ChatGPT 5.4</strong></p>
<ul>
<li><p><strong>map</strong> the <strong>2D</strong> <strong>points</strong> back to the <strong>3D</strong> <strong>space</strong> using the <strong>transpose</strong> of the <strong>principal</strong> <strong>components</strong> matrix</p></li>
<li><p>add the <strong>mean</strong> (gravity center) of the <strong>original</strong> <strong>data</strong> back to the <strong>reconstructed</strong> <strong>points</strong> to place the <strong>object</strong> in its <strong>original</strong> position</p></li>
<li><p>if the <strong>2D</strong> <strong>representation</strong> was <strong>heavily</strong> <strong>compressed</strong>, surface <strong>refinement</strong> or <strong>3D</strong> <strong>convolutional</strong> neural <strong>networks</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Linear Encoder and Decoder</td>
</tr>
<tr>
<td></td>
<td><strong>encode</strong></td>
<td><strong>decode</strong></td>
</tr>
<tr>
<td>K-Means</td>
<td><ul>
<li><p><span class="math inline"><strong>x</strong><strong>∈</strong>ℝ<sup><strong>d</strong></sup><strong>→</strong>{<strong>1</strong><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>k</strong>}</span></p></li>
</ul></td>
<td><ul>
<li><p><span class="math inline">{<strong>1</strong><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>k</strong>} <strong>→</strong> <strong>C</strong><strong>C</strong><strong>e</strong><strong>n</strong><strong>t</strong><strong>e</strong><strong>r</strong>(<strong>x</strong>)<strong>∈</strong>ℝ<sup><strong>d</strong></sup></span></p></li>
</ul></td>
</tr>
<tr>
<td>Dim-Reduction</td>
<td><ul>
<li><p><span class="math inline"><strong>x</strong><strong>∈</strong>ℝ<sup><strong>d</strong></sup><strong>→</strong>ℝ<sup><strong>k</strong></sup><strong>,</strong>   <strong>k</strong> <strong>&lt;</strong> <strong>d</strong></span></p></li>
</ul></td>
<td><ul>
<li><p><span class="math inline">$\mathbf{z \in}\mathbb{R}^{\mathbf{k}}\mathbf{\rightarrow}\widehat{\mathbf{x}}\mathbf{\in}\mathbb{R}^{\mathbf{d}}$</span></p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Two Views on Dimensionality Reduction</td>
</tr>
<tr>
<td>Simple Dimensionality Reduction</td>
<td colspan="2"><ul>
<li><p>using a <strong>2-D scatter</strong> <strong>plot</strong> as an example, one “<strong>view</strong>” would be to <strong>project</strong> the set <strong>directly</strong> to the <strong>x-axis</strong></p></li>
</ul>
<p>2.0</p>
<p>1.5</p>
<p>1.0</p>
<p>0.5</p>
<p>0</p>
<p>-0.5</p>
<p>-1.5</p>
<p>-2.0</p>
<p>-2.0 -1.5 -1.0 - 0.5 0 0.5 1.0 1.5 2.0</p></td>
</tr>
<tr>
<td>PCA</td>
<td colspan="2"><ul>
<li><p>this method has us <strong>determining</strong> a linear <strong>frame</strong> of reference <strong>corresponding</strong> <strong>to</strong> the direction of <strong>greatest</strong> <strong>variance</strong></p></li>
</ul>
<p><img src="generated_media\DATA780_week11_notes\media\image7.png" style="width:3.29213in;height:1.86484in" /></p>
<p>the projection here is more “spread out” giving a broader representation of the data</p></td>
</tr>
<tr>
<td colspan="3">Maximum Variance View</td>
</tr>
<tr>
<td>PCA: Max Variance</td>
<td colspan="2"><ul>
<li><p>PCA is a <strong>linear</strong> <strong>dimensionality</strong> <strong>reduction</strong> technique</p></li>
<li><p>find the <strong>directions</strong> of <strong>maximum</strong> <strong>variance</strong> in the data</p></li>
</ul>
<p><span class="math display">⟨⟨<em>x</em><sub><em>i</em></sub>⟩⟩<sub><em>i</em> = 1</sub><sup><em>N</em></sup></span></p>
<ul>
<li><p><strong>assume</strong> that the <strong>data</strong> is <strong>centered</strong>, i.e.</p></li>
</ul>
<p><span class="math display">$$\sum_{i}^{}{x_{i} = 0}$$</span></p></td>
</tr>
<tr>
<td><p>To Center Your</p>
<p>Data at <span class="math inline"><strong>μ</strong> <strong>=</strong> <strong>0</strong></span></p>
<p>to center data at zero:</p>
<ul>
<li><p>find <span class="math inline"><strong>μ</strong></span> <strong>(</strong>mean of data set<strong>)</strong></p></li>
<li><p>subtract <span class="math inline"><strong>μ</strong></span> from each datapoint</p></li>
</ul>
<p>(linear transformation)</p></td>
<td colspan="2"><ul>
<li><p><strong>centered</strong> <strong>data</strong> transformation</p></li>
</ul>
<p><span class="math inline"><strong>x</strong><sub><strong>i</strong></sub><sup><strong>′</strong></sup><strong>=</strong> <strong>x</strong><sub><strong>i</strong></sub><strong>−</strong> <strong>μ</strong></span><strong>,</strong> where <span class="math inline">$\mathbf{\mu\ }\mathbf{= \ }\left( \frac{\mathbf{1}}{\mathbf{N}} \right)\sum_{\mathbf{i = 1}}^{\mathbf{N}}\mathbf{x}_{\mathbf{i}}$</span></p>
<ul>
<li><p>thus,</p></li>
</ul>
<p><span class="math display">$$\mathbf{x}_{\mathbf{i}}^{\mathbf{'}}\mathbf{= \ }\mathbf{x}_{\mathbf{i}}\mathbf{- \ }\left( \frac{\mathbf{1}}{\mathbf{N}} \right)\sum_{\mathbf{i = 1}}^{\mathbf{N}}\mathbf{x}_{\mathbf{i}}$$</span></p></td>
</tr>
<tr>
<td>PCA: Max Variance, cont.</td>
<td colspan="2"><ul>
<li><p><strong>find</strong> a set of <strong>orthogonal</strong> vectors <span class="math inline"><strong>v</strong><strong>_</strong><strong>1</strong><strong>,</strong> <strong>.</strong><strong>.</strong><strong>.</strong><strong>,</strong> <strong>v</strong><strong>_</strong><strong>k</strong></span></p>
<ul>
<li><p>the <strong>first</strong> principal component <span class="math inline">(<strong>P</strong><strong>C</strong>)<strong>v</strong><sub><strong>1</strong></sub></span> is the <strong>direction</strong> of largest <strong>variance</strong></p></li>
<li><p>the <strong>second</strong> <span class="math inline"><strong>P</strong><strong>C</strong> <strong>v</strong><sub><strong>2</strong></sub></span> is the <strong>direction</strong> of largest <strong>variance</strong> <strong>orthogonal</strong> to <span class="math inline"><strong>v</strong><sub><strong>1</strong></sub></span></p></li>
<li><p>the <span class="math inline"><strong>i</strong><sup><strong>t</strong><strong>h</strong></sup> <strong>P</strong><strong>C</strong> <strong>v</strong><sub><strong>i</strong></sub></span> is the <strong>direction</strong> of <strong>largest</strong> variance <strong>orthogonal</strong> to <span class="math inline"><strong>v</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>.</strong><strong>.</strong><strong>.</strong><strong>,</strong> <strong>v</strong><sub><strong>i</strong> <strong>−</strong> <strong>1</strong></sub></span></p></li>
</ul></li>
<li><p><span class="math inline"><strong>V</strong><sub><strong>D</strong> <strong>×</strong> <strong>k</strong></sub></span> gives projection</p></li>
</ul>
<blockquote>
<p><span class="math inline"><strong>z</strong><sub><strong>i</strong></sub><strong>=</strong><strong>V</strong><sup><strong>T</strong></sup><strong>x</strong><sub><strong>i</strong></sub> </span> for <strong>datapoint</strong> <span class="math inline"><strong>x</strong><sub><strong>i</strong></sub></span></p>
<p><strong>Z = XV</strong> for <strong>entire</strong> <strong>dataset</strong></p>
</blockquote></td>
</tr>
<tr>
<td>Expressed in Matrix Notation</td>
<td colspan="2" style="text-align: center;"><p><span class="math inline">$\mathbf{V =}\left\lbrack \begin{matrix}
\mathbf{|} \\
\mathbf{v}_{\mathbf{1}} \\
\mathbf{|}
\end{matrix}\begin{matrix}
\mathbf{|} \\
\mathbf{v}_{\mathbf{2}} \\
\mathbf{|}
\end{matrix}\begin{matrix}
\mathbf{\ \ \ \ldots} &amp; \begin{matrix}
\mathbf{|} \\
\mathbf{v}_{\mathbf{k}} \\
\mathbf{|}
\end{matrix}
\end{matrix} \right\rbrack$</span> where, <span class="math inline"><strong>x</strong><sub><strong>i</strong></sub><strong>∈</strong>ℝ<sup><strong>D</strong></sup></span></p>
<blockquote>
<p><span class="math inline">$\mathbf{z}_{\mathbf{i}}\mathbf{=}\mathbf{v}^{\mathbf{T}}\mathbf{x}\mathbf{=}\left\lbrack \begin{matrix}
\mathbf{-} \\
\mathbf{-} \\
\mathbf{-}
\end{matrix}\begin{matrix}
\mathbf{v}_{\mathbf{1}} \\
\mathbf{\ldots} \\
\mathbf{v}_{\mathbf{k}}
\end{matrix}\begin{matrix}
\mathbf{-} \\
\mathbf{-} \\
\mathbf{-}
\end{matrix} \right\rbrack\begin{bmatrix}
\mathbf{|} \\
\mathbf{x}_{\mathbf{i}} \\
\mathbf{|}
\end{bmatrix}\mathbf{=}\begin{bmatrix}
\mathbf{v}_{\mathbf{1}}^{\mathbf{T}}\mathbf{x}_{\mathbf{i}} \\
\mathbf{\ldots} \\
\mathbf{v}_{\mathbf{k}}^{\mathbf{T}}\mathbf{x}_{\mathbf{i}}
\end{bmatrix}$</span> where, <span class="math inline"><strong>z</strong><sub><strong>i</strong></sub><strong>∈</strong>ℝ<sup><strong>k</strong></sup></span></p>
</blockquote></td>
</tr>
<tr>
<td>PCA: Max Variance, cont.</td>
<td colspan="2"><ul>
<li><p>we wish to <strong>find</strong> <span class="math inline"><strong>v</strong><strong>_</strong><strong>1</strong></span> so that <span class="math inline">$\mathbf{\ }\sum_{\mathbf{i = 1}}^{\mathbf{N}}\mathbf{z}_{\mathbf{i}}^{\mathbf{2}}$</span> is <strong>maximized</strong></p></li>
</ul>
<p><span class="math display">$$\sum_{\mathbf{i = 1}}^{\mathbf{N}}{\mathbf{\ }\mathbf{z}_{\mathbf{i}}^{\mathbf{2}}}\mathbf{=}\mathbf{z}^{\mathbf{T}}\mathbf{z}\mathbf{= \ }\mathbf{v}_{\mathbf{1}}^{\mathbf{T}}\mathbf{X}^{\mathbf{T}}\mathbf{X}\mathbf{\ }\mathbf{v}_{\mathbf{1}}$$</span></p>
<p>important constraint</p>
<ul>
<li><p>the <strong>maximum</strong> value attained by</p></li>
</ul>
<p><span class="math inline"><strong>v</strong><sub><strong>1</strong></sub><sup><strong>T</strong></sup><strong>X</strong><sup><strong>T</strong></sup><strong>X</strong> <strong>v</strong><sub><strong>1</strong></sub></span> for <span class="math inline">||<strong>v</strong><sub><strong>1</strong></sub>||<strong>=</strong> <strong>1</strong></span></p>
<ul>
<li><p>is the <strong>largest</strong> <strong>eigenvalue</strong> of</p></li>
</ul>
<p><span class="math display"><strong>X</strong><sup><strong>T</strong></sup><strong>X</strong></span></p></td>
</tr>
<tr>
<td colspan="3">Reconstruction View</td>
</tr>
<tr>
<td>Best Reconstruction</td>
<td colspan="2"><ul>
<li><p>we have i.i.d. data <span class="math inline">⟨⟨<strong>x</strong><sub><strong>i</strong></sub>⟩⟩<sub><strong>i</strong> <strong>=</strong> <strong>1</strong></sub><sup><strong>N</strong></sup></span> data matrix <span class="math inline"><strong>X</strong></span></p></li>
<li><p>find a <span class="math inline"><em>k</em></span>-dimensional linear projection that best represents the data</p></li>
<li><p>suppose <span class="math inline"><strong>V</strong><sub><strong>k</strong></sub><strong>∈</strong> ℝ<sup><strong>D</strong><strong>×</strong><strong>k</strong></sup></span> is such that columns of <span class="math inline"><strong>V</strong><sub><strong>k</strong></sub></span> are orthonormal</p></li>
<li><p><img src="generated_media\DATA780_week11_notes\media\image8.png" style="width:1.55208in;height:1.34766in" />project data <span class="math inline"><strong>X</strong></span> onto subspace defined by <span class="math inline"><em>V</em><sub><em>k</em></sub></span></p></li>
</ul>
<p>reconstructed datapoint</p>
<p><span class="math display"><strong>Z</strong> <strong>=</strong> <strong>X</strong> <strong>V</strong><sub><strong>k</strong></sub></span></p>
<ul>
<li><p>minimize reconstruction error</p></li>
</ul>
<p>initial datapoint</p>
<p><span class="math display"><strong>z</strong><sub><strong>i</strong></sub></span></p>
<p><span class="math display">$$\sum_{\mathbf{i = 1}}^{\mathbf{N}}{\mathbf{||\ }\mathbf{x}_{\mathbf{i}}\mathbf{-}\mathbf{V}_{\mathbf{k}}\mathbf{\ }\mathbf{V}_{\mathbf{k}}^{\mathbf{T}}\mathbf{\ }\mathbf{x}_{\mathbf{i}}\mathbf{\ |}\left. \ \mathbf{} \right|^{\mathbf{2}}}$$</span></p></td>
</tr>
<tr>
<td colspan="3">Singular Value Decomposition</td>
</tr>
<tr>
<td>Full vs Thin SVD</td>
<td colspan="2" style="text-align: center;"><p><span class="math inline"><strong>X</strong> <strong>=</strong> <strong>U</strong> <strong>Σ</strong> <strong>V</strong><sup><strong>T</strong></sup></span> (assume <span class="math inline"><strong>N</strong> <strong>&gt;</strong> <strong>D</strong></span>)</p>
<ul>
<li><p><strong>thin</strong> <strong>SVD</strong></p></li>
</ul>
<blockquote>
<p><span class="math display"><strong>U</strong> <strong>i</strong><strong>s</strong> <strong>N</strong> <strong>×</strong> <strong>D</strong><strong>,</strong> </span></p>
<p><span class="math display"><strong>Σ</strong> <strong>i</strong><strong>s</strong> <strong>D</strong> <strong>×</strong> <strong>D</strong><strong>,</strong> </span></p>
<p><span class="math inline"><strong>V</strong> <strong>i</strong><strong>s</strong> <strong>D</strong> <strong>×</strong> <strong>D</strong><strong>,</strong> </span></p>
<p><span class="math display"><strong>U</strong><sup><strong>T</strong></sup> <strong>U</strong><strong>=</strong><strong>V</strong><sup><strong>T</strong></sup> <strong>V</strong><strong>=</strong><strong>I</strong><sub><strong>D</strong></sub></span></p>
</blockquote>
<ul>
<li><p><span class="math inline"><strong>Σ</strong></span> is diagonal with <span class="math inline"><strong>σ</strong><sub><strong>1</strong></sub><strong>≥</strong> <strong>σ</strong><sub><strong>2</strong></sub><strong>≥</strong> <strong>…</strong> <strong>≥</strong> <strong>σ</strong><sub><strong>D</strong></sub><strong>≥</strong> <strong>0</strong></span></p></li>
<li><p>The first <span class="math inline"><strong>k</strong></span> principal components are the first <span class="math inline"><strong>k</strong></span> columns of <span class="math inline"><strong>V</strong></span></p></li>
</ul>
<p><span class="math inline"><strong>U</strong></span> and <span class="math inline"><strong>V</strong></span> are <strong>orthonormal</strong> matrices</p>
<ul>
<li><p><strong>Full</strong> <strong>SVD</strong>:</p></li>
</ul>
<blockquote>
<p><span class="math display"><strong>U</strong> <strong>i</strong><strong>s</strong> <strong>N</strong> <strong>×</strong> <strong>N</strong><strong>,</strong></span></p>
<p><span class="math display"><strong>Σ</strong> <strong>i</strong><strong>s</strong> <strong>N</strong> <strong>×</strong> <strong>D</strong><strong>,</strong> </span></p>
<p><span class="math inline"><strong>V</strong> <strong>i</strong><strong>s</strong> <strong>D</strong> <strong>×</strong> <strong>D</strong> </span></p>
</blockquote></td>
</tr>
<tr>
<td>Full vs Thin SVD Visualization</td>
<td colspan="2"><p><img src="generated_media\DATA780_week11_notes\media\image9.png" style="width:0.31086in;height:0.92014in" /><img src="generated_media\DATA780_week11_notes\media\image9.png" style="width:0.31105in;height:0.9207in" /><img src="generated_media\DATA780_week11_notes\media\image9.png" style="width:0.31105in;height:0.9207in" /><img src="generated_media\DATA780_week11_notes\media\image9.png" style="width:0.31105in;height:0.9207in" /><img src="generated_media\DATA780_week11_notes\media\image9.png" style="width:0.31105in;height:0.9207in" /><img src="generated_media\DATA780_week11_notes\media\image10.png" style="width:0.64935in;height:0.3048in" /><img src="generated_media\DATA780_week11_notes\media\image9.png" style="width:0.31105in;height:0.9207in" /><img src="generated_media\DATA780_week11_notes\media\image11.png" style="width:4.81404in;height:2.96104in" /></p>
<p><span class="math display"><strong>Σ</strong><sub><strong>D</strong></sub></span></p></td>
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
<th colspan="2">Selecting <span class="math inline"><strong>K</strong></span></th>
</tr>
</thead>
<tbody>
<tr>
<td>How Many Principal Components to Select</td>
<td><ul>
<li><p>look for the “<strong>elbow</strong>” in the <strong>curve</strong> of <strong>reconstructed</strong> <strong>error</strong> vs <strong>number</strong> of <strong>principal</strong> <strong>components</strong></p></li>
</ul>
<p>recombination error</p>
<p>select a <span class="math inline"><em>k</em></span> somewhere in this range</p>
<p># of principal components</p></td>
</tr>
</tbody>
</table>
