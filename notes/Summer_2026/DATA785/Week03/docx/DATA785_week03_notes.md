> Markdown version for convenient browsing. Original files:
> - PDF: [DATA785_week03_notes.pdf](../DATA785_week03_notes.pdf)
> - DOCX: [DATA785_week03_notes.docx](DATA785_week03_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 2%" />
<col style="width: 21%" />
<col style="width: 4%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Backpropagation</th>
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
<li><p>apply the backpropagation algorithm for training MLPs</p></li>
<li><p>utilize Autograd systems for automatic differentiation</p></li>
<li><p>implement strategies for effective neural network initialization, regularization, and learning rate adaptation</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5">Backpropagation and the Chain Rule</td>
</tr>
<tr>
<td>The Chain Rule of Differentiation</td>
<td colspan="4"><ul>
<li><p>common version</p></li>
</ul>
<p><span class="math display">$$\frac{d\ z(y)}{dx} = \frac{dz}{dy} \bullet \frac{dy}{dx}$$</span></p>
<ul>
<li><p>less-common version</p></li>
</ul>
<p><span class="math display"><em>s</em><em>u</em><em>p</em><em>p</em><em>o</em><em>s</em><em>e</em> <em>z</em> = <em>z</em>(<em>y</em><sub>1</sub>(<em>x</em>), <em>y</em><sub>2</sub>(<em>x</em>), …, <em>y</em><sub><em>n</em></sub>(<em>x</em>))</span></p>
<p><span class="math display">$$\frac{d\ z(y)}{dx} = \sum_{i = 1}^{N}{\frac{dz}{dy_{i}} \bullet \frac{dy_{i}}{dx}}$$</span></p>
<p><img src="generated_media\DATA785_week03_notes\media\image1.png" style="width:2.80208in;height:1.95996in" /></p></td>
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
<th>Math Derivation for Backpropagation</th>
<th><ul>
<li><p>terminology</p>
<ul>
<li><p><span class="math inline"><strong>L</strong></span>: # of layers</p></li>
<li><p><span class="math inline"><strong>N</strong><sup><strong>l</strong></sup></span>: dimensionality of layer <span class="math inline"><strong>l</strong></span></p></li>
<li><p><span class="math inline"><strong>W</strong><sup><strong>l</strong></sup></span>: weight of matrix for layer <span class="math inline"><strong>l</strong></span></p></li>
<li><p><span class="math inline"><strong>b</strong><sup><strong>l</strong></sup></span>: bias vector for layer <span class="math inline"><strong>l</strong></span></p></li>
<li><p><span class="math inline"><strong>z</strong><sup><strong>l</strong></sup></span>: linear pre-activations for layer <span class="math inline"><strong>l</strong></span></p>
<ul>
<li><p>(<span class="math inline">$\mathbf{z}^{\mathbf{l}}\mathbf{=}\mathbf{W}^{\mathbf{l}}\mathbf{a}^{\mathbf{l - 1}}\mathbf{+ b\hat{}l)}$</span></p></li>
</ul></li>
<li><p><span class="math inline"><strong>σ</strong><sup><strong>l</strong></sup></span>: activation function for layer <span class="math inline"><strong>l</strong></span></p></li>
<li><p><span class="math inline"><strong>a</strong><sup><strong>l</strong></sup></span>: nonlinear activations for layer <span class="math inline"><strong>l</strong></span></p>
<ul>
<li><p><span class="math inline">(<strong>a</strong><sup><strong>l</strong></sup><strong>=</strong><strong>σ</strong><sup><strong>l</strong></sup>(<strong>z</strong><sup><strong>l</strong></sup>))</span></p></li>
</ul></li>
<li><p><span class="math inline"><strong>a</strong><sup><strong>0</strong></sup></span>and <span class="math inline"><strong>a</strong><sup><strong>L</strong></sup></span>: refer to the model inputs (x) and model predictions (<span class="math inline">$\widehat{\mathbf{y}}\mathbf{(x))}$</span>, respectively</p></li>
</ul></li>
<li><p>backpropagation preliminaries</p>
<ul>
<li><p>for training NNs with gradient descent, we want <span class="math inline">$\frac{\mathbf{dL}}{\mathbf{d}\mathbf{W}^{\mathbf{l}}}$</span></p></li>
<li><p>we can compute this if we have <span class="math inline">$\frac{\mathbf{dL}}{\mathbf{d}\mathbf{a}^{\mathbf{L}}}$</span> and <span class="math inline">$\frac{\mathbf{d}\mathbf{a}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}$</span></p></li>
</ul></li>
</ul>
<p>derivative of nonlinear activations</p>
<p>derivative of loss</p>
<ul>
<li><p>using the chain rule, we have:</p></li>
</ul>
<p><span class="math display">$$\frac{\mathbf{d}\mathbf{\ L}}{\mathbf{d}\mathbf{W}_{\mathbf{ij}}^{\mathbf{l}}}\mathbf{=}\sum_{\mathbf{k = 1}}^{\mathbf{N}^{\mathbf{l}}}{\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{l}}}\mathbf{\bullet}\frac{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{l}}}{\mathbf{d}\mathbf{W}_{\mathbf{ij}}^{\mathbf{l}}}}$$</span></p>
<p>=</p>
<ul>
<li><p>in matrix notation:</p></li>
</ul>
<p><span class="math display">$$\frac{\mathbf{dL}}{\mathbf{d}\mathbf{W}^{\mathbf{l}}}\mathbf{=}\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}\mathbf{a}^{\mathbf{l -}\mathbf{1}^{\mathbf{T}}}$$</span></p>
<ul>
<li><p>we can calculate these iteratively, starting from <span class="math inline"><strong>l</strong> <strong>=</strong> <strong>L</strong></span> and going down to <span class="math inline"><strong>l</strong> <strong>=</strong> <strong>1</strong></span></p></li>
<li><p>when: <span class="math inline"><strong>l</strong> <strong>=</strong> <strong>L</strong><strong>:</strong></span></p></li>
</ul>
<blockquote>
<p><span class="math display">$$\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{L}}}\mathbf{=}\frac{\mathbf{dL}}{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{L}}}\mathbf{\bullet}\frac{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{L}}}$$</span></p>
</blockquote>
<ul>
<li><p>for: <span class="math inline"><strong>l</strong> <strong>=</strong> <strong>L</strong> <strong>−</strong> <strong>1</strong><strong>,</strong> <strong>L</strong> <strong>−</strong> <strong>2</strong><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>1</strong><strong>:</strong></span></p></li>
</ul>
<p><span class="math display">$$\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{l}}}\mathbf{=}\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{l}}}\mathbf{\cdot}\frac{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{l}}}\mathbf{= \ }\left\{ \mathbf{\ }\sum_{\mathbf{m = 1}}^{\mathbf{N}^{\mathbf{l + 1}}}\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{z}_{\mathbf{m}}^{\mathbf{l + 1}}}\mathbf{\cdot}\frac{\mathbf{d}\mathbf{z}_{\mathbf{m}}^{\mathbf{l + 1}}}{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{l}}} \right\}\mathbf{\cdot}\frac{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{l}}}$$</span></p>
<ul>
<li><p>so:</p></li>
</ul>
<p>element-wise multiplication</p>
<p><span class="math display">$$\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{l}}}\mathbf{= \ }\left\{ \mathbf{\ }\sum_{\mathbf{m = 1}}^{\mathbf{N}^{\mathbf{l + 1}}}\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{z}_{\mathbf{m}}^{\mathbf{l + 1}}}\mathbf{\cdot}\mathbf{W}_{\mathbf{mk}}^{\mathbf{l + 1}} \right\}\mathbf{\cdot}\frac{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{l}}}$$</span></p>
<ul>
<li><p>compact notation:</p></li>
</ul>
<p><span class="math display">$$\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}\mathbf{= \ }\left( \mathbf{W}^{\left( \mathbf{l + 1} \right)^{\mathbf{T}}}\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}^{\mathbf{l + 1}}} \right)\mathbf{\circ}\frac{\mathbf{d}\mathbf{a}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}$$</span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Procedure for Backpropagation</td>
<td><ul>
<li><p>the goal of backpropagation is to calculate the derivative of the loss function with respect to model parameters <span class="math inline"><em>d</em><em>W</em></span> for any weight <span class="math inline"><em>W</em></span></p></li>
<li><p>how to compute <span class="math inline">$\frac{dL}{dW}$</span> for any weight <span class="math inline"><em>W</em></span>:</p></li>
</ul>
<ol type="1">
<li><p>compute <span class="math inline">$\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{L}}}\mathbf{=}\frac{\mathbf{dL}}{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{L}}}\mathbf{\bullet}\frac{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{L}}}$</span></p></li>
<li><p>iteratively compute <span class="math inline">$\frac{dL}{dz^{l}}$</span> for <span class="math inline"><em>l</em> = <em>L</em> − 1, <em>L</em> − 2, …, 3, 2, 1</span></p>
<ol type="a">
<li><p><span class="math inline">$\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}\mathbf{= \ }\left( \mathbf{W}^{\left( \mathbf{l + 1} \right)^{\mathbf{T}}}\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}^{\mathbf{l + 1}}} \right)\mathbf{\circ}\frac{\mathbf{d}\mathbf{a}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}$</span></p></li>
</ol></li>
<li><p>from (2), compute <span class="math inline">$\frac{\mathbf{dL}}{\mathbf{d}\mathbf{W}^{\mathbf{l}}}\mathbf{=}\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}\mathbf{\bullet}\mathbf{a}^{\mathbf{l -}\mathbf{1}^{\mathbf{T}}}$</span></p></li>
</ol></td>
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
<th>Backpropagation Example</th>
<th><ul>
<li><p>consider a FFT for a binary classification task</p></li>
</ul>
<p><span class="math display"><em>a</em><sup><em>l</em></sup>= (1  + exp (−<em>z</em><sup><em>l</em></sup>))<sup>−1</sup> ∀<em>l</em>∈ {1 .. <em>L</em>}</span></p>
<ul>
<li><p>assume sigmoid (like LR)</p></li>
</ul>
<blockquote>
<p>in the prediction and intermediate layers</p>
</blockquote>
<p><span class="math display">$$\frac{a^{L} - y}{a^{L}(1 - a^{L})}$$</span></p>
<p>derivative of binary cross-entropy (CE) loss</p>
<ul>
<li><p>compute <span class="math inline">$\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{L}}}\mathbf{=}\frac{\mathbf{dL}}{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{L}}}\mathbf{\bullet}\frac{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{L}}}$</span></p></li>
</ul>
<p><span class="math display"><em>a</em><sup><em>L</em></sup>(1 − <em>a</em><sup><em>L</em></sup>)</span></p>
<p>derivative of sigmoid activation</p>
<ul>
<li><p>you are left with</p></li>
</ul>
<blockquote>
<p><span class="math display"><strong>a</strong><sup><strong>L</strong></sup><strong>−</strong><strong>y</strong></span></p>
</blockquote>
<ul>
<li><p>iteratively compute <span class="math inline">$\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}\mathbf{for\ l = L - 1,L - 2,\ldots,3,2,1}$</span></p></li>
</ul>
<p><span class="math display">$$\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}\mathbf{= \ }\left( \mathbf{W}^{\left( \mathbf{l + 1} \right)^{\mathbf{T}}}\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}^{\mathbf{l + 1}}} \right)\mathbf{\circ}\frac{\mathbf{d}\mathbf{a}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}\mathbf{\ \ }\mathbf{\rightarrow}$$</span></p>
<p><span class="math display">$$\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{z}^{\mathbf{L - 1}}}\mathbf{= \ }\mathbf{W}^{\mathbf{L}^{\mathbf{T}}\left( \mathbf{a}^{\mathbf{L}}\mathbf{- \ y} \right)}\mathbf{\circ}\mathbf{a}^{\mathbf{L - 1}}\left( \mathbf{1\  - \ }\mathbf{a}^{\mathbf{L - 1}} \right)\mathbf{\ \ }\mathbf{\rightarrow}$$</span></p>
<p><span class="math display">$$\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{z}^{\mathbf{L - 2}}}\mathbf{= \ }\mathbf{W}^{\mathbf{L}^{\mathbf{T}}\left( \mathbf{a}^{\mathbf{L}}\mathbf{- \ y} \right)}\mathbf{\circ}\mathbf{a}^{\mathbf{L - 1}}\left( \mathbf{1\  - \ }\mathbf{a}^{\mathbf{L - 1}} \right)\mathbf{a}^{\mathbf{L -}\mathbf{2}^{\mathbf{T}}}\mathbf{\ \ }\mathbf{\rightarrow}$$</span></p>
<p><span class="math display"><strong>a</strong><strong>n</strong><strong>d</strong> <strong>s</strong><strong>o</strong> <strong>o</strong><strong>n</strong><strong>…</strong></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Vanishing and Exploding Gradients</td>
<td><ul>
<li><p>in the backpropagation step, we have</p></li>
</ul>
<p><strong>R</strong></p>
<p><strong>L</strong></p>
<p><span class="math display">$$\frac{\mathbf{d}\mathcal{L}}{\mathbf{d}\mathbf{z}^{\mathbf{l}}}\mathbf{= \ }\left( \mathbf{W}^{\left( \mathbf{l + 1} \right)^{\mathbf{T}}}\frac{\mathbf{dL}}{\mathbf{d}\mathbf{z}^{\mathbf{l + 1}}} \right)\mathbf{\circ}\frac{\mathbf{d}\mathbf{a}_{\mathbf{k}}^{\mathbf{l}}}{\mathbf{d}\mathbf{z}_{\mathbf{k}}^{\mathbf{l}}}$$</span></p>
<ul>
<li><p>for networks with many layers, the weight matrices computed iteratively to the left and the activation derivative computed to the right, can cause gradients to blow up, or shrink to approaching zero</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>
