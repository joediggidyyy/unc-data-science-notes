> Markdown version for convenient browsing. Original files:
> - PDF: [DATA785_week06_notes.pdf](../DATA785_week06_notes.pdf)
> - DOCX: [DATA785_week06_notes.docx](DATA785_week06_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr>
<th colspan="4">Batch-Layer Norms and Residual Connections</th>
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
<li><p>implement batch normalization to accelerate training</p></li>
<li><p>utilize residual connections to build deeper networks</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Async</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td>Training Really Deep NNs</td>
<td colspan="4"><p><img src="generated_media\DATA785_week06_notes\media\image1.png" style="width:4.79383in;height:2.61458in" /></p>
<p>Gemini 3.5</p>
<ul>
<li><p>NNs have been increasing in complexity and numbers of layers over time</p></li>
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
<th>Batch Normalization</th>
<th><p><img src="generated_media\DATA785_week06_notes\media\image2.png" style="width:4.82739in;height:2.21875in" /></p>
<p>Gemini 3.5</p>
<ul>
<li><p>the input batch is similar to a mini batch with stochastic gradient descent, essentially it is a set of examples along which we want to make an update in gradient descent</p></li>
<li><p>the output batch becomes the input batch for the next layer</p></li>
</ul>
<p><img src="generated_media\DATA785_week06_notes\media\image3.png" style="width:4.80208in;height:2.85787in" /></p>
<p>Gemini 3.5</p>
<ul>
<li><p>with batch normalization, once the data has been transformed linearly, a standardization operation is performed before being passed to the non-linear activation function</p></li>
<li><p>alternatively, batch normalization can be after NL activation</p></li>
<li><p>to compute batch normalization:</p>
<ul>
<li><p>compute the batch mean: </p></li>
</ul></li>
</ul>
<p>computes average vector input</p>
<p><span class="math display">$$\mathbf{\ }{\widehat{\mathbf{\mu}}}_{\mathcal{B}}\mathbf{=}\frac{\mathbf{1}}{\left| \mathcal{B} \right|}\sum_{\mathbf{x \in}\mathcal{B}}^{}\mathbf{x}$$</span></p>
<ul>
<li><p>compute the batch variance:</p></li>
</ul>
<p>computes variance of vectors</p>
<p><span class="math display">$${\widehat{\sigma}}_{\mathcal{B}}^{2} = \frac{1}{\left| \mathcal{B} \right|}\sum_{\mathbf{x \in}\mathcal{B}}^{}\left( \mathbf{x -}{\widehat{\mu}}_{\mathcal{B}} \right)^{\mathbf{2}}$$</span></p>
<ul>
<li><p>normalize each batch sample:</p></li>
</ul>
<p>normalization with mean = 0 and s.d. = 1</p>
<p><span class="math display">$$BN(x) = \frac{x - {\widehat{\mu}}_{\mathcal{B}}}{{\widehat{\sigma}}_{\mathcal{B}}}$$</span></p>
<ul>
<li><p>it is unclear if normalizing to mean = 0 and s.d. = 1 and can lead to division by zero in the third equation if the batch variance is zero</p></li>
<li><p>to avoid this, we add a small amount of noise (<span class="math inline"><em>ϵ</em></span>) to the second equation</p></li>
</ul>
<p><span class="math display">$${\widehat{\sigma}}_{\mathcal{B}}^{2} = \frac{1}{\left| \mathcal{B} \right|}\sum_{\mathbf{x \in}\mathcal{B}}^{}\left( \mathbf{x -}{\widehat{\mu}}_{\mathcal{B}} \right)^{\mathbf{2}}\mathbf{+ \epsilon}$$</span></p>
<ul>
<li><p>additionally, we add two parameters (vectors <span class="math inline"><em>γ</em></span> and <span class="math inline"><em>β</em></span>) to the third equation</p></li>
</ul>
<p><span class="math display">$$BN(x) = \gamma \odot \frac{x - {\widehat{\mu}}_{\mathcal{B}}}{{\widehat{\sigma}}_{\mathcal{B}}} + \beta$$</span></p>
<ul>
<li><p>we do an element-wise product of each batch normalized example with <span class="math inline"><em>γ</em></span> to re-scale and constant vector <span class="math inline"><em>β</em></span> which shifts the value of the normalized batch and redefines to a different mean and variance</p></li>
<li><p>during test time, this is done somewhat differently by using the values collected during training to estimate reasonable values for <span class="math inline"><em>μ</em></span> and <span class="math inline"><em>σ</em></span></p></li>
<li><p>batch normalization for images</p>
<ul>
<li><p>for each channel is <span class="math inline"><em>μ</em> </span>and <span class="math inline"><em>σ</em></span> are calculated and normalized separately</p></li>
</ul></li>
<li><p>benefits of batch normalization</p>
<ul>
<li><p>smooths the optimization landscape</p>
<ul>
<li><p>can use a larger learning rate – faster convergence</p></li>
</ul></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA785_week06_notes\media\image4.png" style="width:4.82292in;height:0.90856in" /></p>
<p>Gemini 3.5</p>
<ul>
<li><p>regularization from noisy estimates of mean and variance</p>
<ul>
<li><p>“sweet spot” for batch size</p></li>
<li><p>batch too small</p>
<ul>
<li><p>noisy mean and variance estimates</p></li>
</ul></li>
<li><p>batch too large</p>
<ul>
<li><p>mean and variance estimates not noisy enough</p></li>
</ul></li>
</ul></li>
</ul></th>
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
<th>Layer Normalization</th>
<th><ul>
<li><p>with layer normalization, we don’t compute aggregated statistics across a batch, each example in the batch is normalized independently</p></li>
<li><p>benefits of layer normalization</p>
<ul>
<li><p>inputs to layer never explode or vanish</p></li>
<li><p>no dependence on batch size</p></li>
<li><p>forward pass during training and testing are the same</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Residual Connections</td>
<td><ul>
<li><p>let <span class="math inline"><em>F</em></span> be the set of functions an NN architecture can represent</p></li>
<li><p><img src="generated_media\DATA785_week06_notes\media\image5.jpeg" style="width:4.71205in;height:3.04167in" />let <span class="math inline"><em>f</em><sup>*</sup></span> be the function we want to learn</p></li>
</ul>
<p>Gemini 3.5</p>
<ul>
<li><p>each layer is a set of functions that can be represented by out feed forward network and outputs to the next layer with each layers’ functions increasing in complexity</p></li>
<li><p>this leads to a situation where more complex layers become disjointed from the simpler architectures</p></li>
<li><p>ideally, the more complex architectures should already encapsulate the simpler architectures absorbing the horizons of the lower layers</p></li>
<li><p>to guarantee that the <span class="math inline"><em>n</em> + 1</span> layer NN can represent a superset of the functions that the <span class="math inline"><em>n</em></span> layer NN can represent, make sure that the <span class="math inline"><em>n</em> + 1</span> layer can represent the identity function</p></li>
</ul>
<p><img src="generated_media\DATA785_week06_notes\media\image6.png" style="width:4.41181in;height:5.66667in" /></p>
<p>Gemini 3.5</p>
<ul>
<li><p>several convolution layers, activation, and batch normalizations are used and at the end, you add a residual connection that bypasses this computation and adds x back into loop</p></li>
<li><p>this implies that with the residual connection, we can always implement the identity function ensuring that computations made by a smaller network can also be performed by any larger network</p></li>
<li><p><img src="generated_media\DATA785_week06_notes\media\image7.png" style="width:4.79257in;height:1.89583in" />additionally, a <span class="math inline">1<em>x</em>1</span> convolution can be added to the residual loop before it is passed</p></li>
</ul>
<p>Gemini 3.5</p>
<ul>
<li><p>many modern architectures for deep learning and specifically for computer vision have moved towards uniform computation layer blocks that repeat with ResNet connections across each block</p></li>
<li><p>benefits of residual connections</p>
<ul>
<li><p>expands the set of functions that a NN can represent</p></li>
<li><p><img src="generated_media\DATA785_week06_notes\media\image8.png" style="width:4.82486in;height:1.47917in" />prevents “shattering gradients”</p></li>
</ul></li>
</ul>
<p>Gemini 3.5</p>
<ul>
<li><p>in a shallow network, points close together on the x-axis have similar gradients</p></li>
<li><p>extending to deeper architectures, the pattern breaks and there is very little correlation between adjacent points resulting in a “spiky” network</p></li>
<li><p>by adding residual connections, this spiky-ness is normalized producing a better fitting model</p></li>
</ul></td>
</tr>
<tr>
<td>Summary</td>
<td><ul>
<li><p>increasing depth has proven to be a reliable way of improving NNS</p></li>
<li><p>bath normalization can layer normalization smooth the optimization landscape by normalizing activation/pre-activation</p></li>
<li><p>residual connections smooth the optimization landscape and ensure that adding layers expands the set of representable functions</p></li>
<li><p>normalization and residual connections are important components of sequence-modeling architectures such as RNNs transformers</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>
