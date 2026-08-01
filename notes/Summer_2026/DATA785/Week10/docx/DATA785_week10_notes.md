> Markdown version for convenient browsing. Original files:
> - PDF: [DATA785_week10_notes.pdf](../DATA785_week10_notes.pdf)
> - DOCX: [DATA785_week10_notes.docx](DATA785_week10_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 24%" />
<col style="width: 3%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Normalizing Flows and Diffusion Models</th>
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
<li><p>outline the basic principles of</p>
<ol type="1">
<li><p>Generative Modeling</p></li>
<li><p>Normalizing Flows</p></li>
<li><p>Diffusion Models</p></li>
</ol></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td>Introduction to Generative Modeling</td>
<td colspan="3"><ul>
<li><p>assume that we have samples from some distribution <span class="math inline"><em>p</em><sub><em>x</em></sub></span> defined on <span class="math inline">ℝ<sub><em>d</em></sub></span></p></li>
<li><p>what we want:</p>
<ul>
<li><p>design a model that can efficiently sample from <span class="math inline"><em>p</em>_<em>x</em></span></p></li>
<li><p>optionally: evaluate the likelihood <span class="math inline"><em>p</em><sub><em>x</em></sub>(<em>x</em>)</span> of a sample <span class="math inline"><em>x</em></span></p></li>
</ul></li>
<li><p>uses:</p>
<ul>
<li><p>generate novel samples</p></li>
<li><p>anomaly detection</p></li>
</ul></li>
<li><p>common methods:</p>
<ul>
<li><p>transformers</p></li>
<li><p>VAEs</p></li>
<li><p>GANs</p></li>
<li><p>normalizing flows</p></li>
<li><p>diffusion models</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>What are Normalizing Flows?</td>
<td colspan="3"><ul>
<li><p>normalizing flows (NFs)</p></li>
</ul>
<p><span class="math display"><em>z</em> ∼ <em>p</em><em>z</em> → <em>f</em><sub>1</sub> → <em>f</em><sub>2</sub>…<em>f</em><sub><em>n</em></sub> → <em>x</em> ∼ <em>p</em><em>x</em></span></p>
<p><span class="math display"><em>f</em> = <em>f</em><sub><em>n</em></sub> ∘ …  ∘ <em>f</em><sub>2</sub> ∘ <em>f</em><sub>1</sub></span></p>
<ul>
<li><p>for each layer <span class="math inline"><em>f</em><sub><em>i</em></sub></span></p>
<ul>
<li><p>efficiently compute its inverse</p></li>
<li><p>efficiently compute its Jacobian determinant</p></li>
</ul></li>
<li><p>example:</p>
<ul>
<li><p>invertible element-wise operations</p></li>
</ul></li>
</ul>
<p><span class="math display">$$\left\lbrack \begin{array}{r}
x_{1} \\
x_{2} \\
\ldots \\
x_{n}
\end{array} \right\rbrack \rightarrow \left\lbrack \begin{array}{r}
\sigma\left( x_{1} \right) \\
\sigma\left( x_{2} \right) \\
\sigma\left( x_{3} \right) \\
\sigma(x_{n})
\end{array} \right\rbrack$$</span></p>
<ul>
<li><p>the layer in invertible since the element-wise operation is invertible</p></li>
<li><p>the layer’s Jacobian is a diagonal matrix, so the determinant is the product of the diagonal</p></li>
</ul>
<ul>
<li><p>example:</p>
<ul>
<li><p>shuffling layers</p></li>
</ul></li>
</ul>
<p><span class="math display">$$\left\lbrack \begin{array}{r}
x_{1} \\
x_{2} \\
\ldots \\
x_{d} \\
x_{d + 1} \\
x_{d + 2} \\
\ldots \\
x_{n}
\end{array} \right\rbrack \rightarrow \left\lbrack \begin{array}{r}
x_{d + 1} \\
x_{d + 2} \\
\ldots \\
x_{n} \\
x_{1} \\
x_{2} \\
\ldots \\
x_{n - 1}
\end{array} \right\rbrack$$</span></p>
<ul>
<li><p>the layer is invertible since we can shuffle the elements</p></li>
<li><p>the layer’s Jacobian is a permutation matrix that has a determinant of 1</p></li>
</ul>
<ul>
<li><p>example:</p>
<ul>
<li><p>coupling layers</p></li>
</ul></li>
</ul>
<p>where <span class="math inline"><em>m</em></span> is some complex function</p>
<p><strong>m</strong></p>
<p><strong>+</strong></p>
<p>copy</p>
<p><span class="math inline">$\left\lbrack \begin{array}{r}
x_{1} \\
x_{2} \\
\ldots \\
x_{d} \\
x_{d + 1} \\
x_{d + 2} \\
\ldots \\
x_{n}
\end{array} \right\rbrack$</span> <span class="math inline">$\left\lbrack \begin{array}{r}
y_{1} \\
y_{2} \\
\ldots \\
y_{d} \\
y_{d + 1} \\
y_{d + 2} \\
\ldots \\
y_{n}
\end{array} \right\rbrack$</span></p>
<ul>
<li><p>the layer is invertible since</p></li>
</ul>
<blockquote>
<p><span class="math inline"><em>x</em><sub>1 : <em>d</em></sub> = <em>y</em><sub>1 : <em>d</em></sub></span> and <span class="math inline"><em>x</em><sub><em>d</em> + 1 : <em>n</em></sub> = <em>y</em><sub><em>d</em> + 1 : <em>n</em></sub> − <em>m</em>(<em>x</em><sub>1 : <em>d</em></sub>)</span></p>
</blockquote>
<ul>
<li><p>the Jacobian is lower triangular, so the determinant is the product of the diagonal</p></li>
</ul>
<ul>
<li><p>basic NF architectures interchange elementwise, shuffling, and coupling layers</p></li>
<li><p>NF pros:</p>
<ul>
<li><p>trained with maximum likelihood</p></li>
<li><p>can generate new samples and evaluate likelihood of samples</p></li>
</ul></li>
<li><p>NF cons:</p>
<ul>
<li><p>NF architectures are restricted to using layers designed to be invertible and have traceable Jacobian determinant</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Diffusion Processes</td>
<td colspan="3"><p><img src="generated_media\DATA785_week10_notes\media\image1.png" style="width:4.91309in;height:2.09118in" /></p>
<p>Gemini 3.6</p>
<ul>
<li><p>the diffusion process consists of several steps where we increasingly add small amounts of noise</p></li>
<li><p>an ML model can then look at each step in this process and reverse the diffusion process to create an image from the noise</p></li>
<li><p>diffusion can be defined as:</p></li>
</ul>
<p><span class="math display">$$q\left( x_{t + 1} \middle| x_{t} \right) = N\left( \sqrt{1 - \beta x_{t}},\beta I \right)$$</span></p>
<p><span class="math display"><em>w</em><em>h</em><em>e</em><em>r</em><em>e</em>, <em>β</em> <em>i</em><em>s</em> <em>a</em> <em>s</em><em>m</em><em>a</em><em>l</em><em>l</em> <em>a</em><em>m</em><em>o</em><em>u</em><em>n</em><em>t</em> <em>o</em><em>f</em> <em>G</em><em>a</em><em>u</em><em>s</em><em>s</em><em>i</em><em>a</em><em>n</em> <em>n</em><em>o</em><em>i</em><em>s</em><em>e</em></span></p>
<ul>
<li><p>generating data using the diffusion process involves just reversing the process using learned parameters from a NN</p></li>
</ul></td>
</tr>
<tr>
<td>Diffusion Models</td>
<td colspan="3"><ul>
<li><p>training diffusion models</p></li>
</ul>
<p><span class="math display"><em>q</em>(<em>x</em><sub>1</sub>|<em>x</em><sub>0</sub>)</span></p>
<p><span class="math display"><em>x</em><sub>0</sub></span></p>
<p><span class="math display"><em>x</em><sub>1</sub></span></p>
<p><span class="math display"><em>p</em><sub>0</sub>(<em>x</em><sub>0</sub>|<em>x</em><sub>1</sub>)</span></p>
<ul>
<li><p>the process involves creating a NN that would maximize the probability of the observed data, essentially what all generative models do (exactly the case with normalizing flows)</p></li>
<li><p>as is true with a lot of generative models, with diffusion models, rather than maximize the likelihood of the data, you maximize some lower bound of this data likelihood, or ELBO – evidence lower bound</p></li>
<li><p>so, we are not trying to maximize the likelihood of the data directly, we are attempting to maximize the lower bound, guaranteeing that the likelihood is, at the least, higher than the lower bound</p></li>
</ul>
<p><span class="math display"><em>l</em><em>o</em><em>g</em><em>p</em><sub><em>θ</em></sub>(<em>x</em>) = <em>l</em><em>o</em><em>g</em>∫<em>p</em><sub><em>θ</em></sub>(<em>x</em><sub>0</sub> |<em>x</em><sub>1</sub>) <em>p</em>(<em>x</em><sub>1</sub>) <em>d</em><em>x</em><sub>1</sub></span></p>
<p><span class="math display">$$\geq Ε\ (log\ p(x_{1})\  + \ log\frac{p_{\theta}\left( x_{0} \right|x_{1})}{q\left( x_{1} \right|x_{0})})$$</span></p>
<ul>
<li><p>this is then generalized to a multi-step process</p></li>
</ul>
<p><span class="math display">$$\log{p_{\theta}(x)} \leq Ε\ \lbrack logp(x_{T})\  + \ log\frac{p_{\theta}\left( x_{0} \right|x_{1})}{q\left( x_{1} \right|x_{0})}$$</span></p>
<p><span class="math display">$$+ log\frac{p_{\theta}\left( x_{1} \right|x_{2})}{q\left( x_{2} \right|x_{1})} + \ldots + log\frac{p_{\theta}\left( x_{T - 1} \right|x_{T})}{q\left( x_{T} \right|x_{T - 1})}\rbrack$$</span></p>
<ul>
<li><p>after some manipulation, optimizing ELBO is equivalent to the following training</p>
<ul>
<li><p>sample Gaussian noise <span class="math inline"><em>ϵ</em></span>, and use it to diffuse <span class="math inline"><em>x</em><sub>0</sub></span>to <span class="math inline"><em>x</em><sub><em>t</em></sub></span></p></li>
<li><p>use a NN to map (<span class="math inline"><em>x</em><sub><em>t</em></sub>, <em>t</em></span>) to a tensor with the same shape as <span class="math inline"><em>x</em><sub><em>t</em></sub></span></p></li>
<li><p>compute loss as the MSE between the output and <span class="math inline"><em>ϵ</em></span></p></li>
</ul></li>
<li><p>diffusion model architectures</p></li>
</ul>
<p>x_t =</p>
<p>noise_scheduler.add_noise(</p>
<p>x, t, noise)</p>
<p>noise_pred =</p>
<p>model(x_t, t)</p>
<p>loss = torch.mse(</p>
<p>noise_pred, noise)</p>
<p>loss.backward()</p>
<p># Pseudocode for a Single Training Step</p>
<p>x = sample_from_dataset()</p>
<p>t = torch.randint()</p>
<p>noise =</p>
<p>torch.randn_like(x)</p>
<p>x_t = noise_scheduler.add_noise(x, t, noise)</p>
<p>noise_pred = model(x_t, t)</p>
<p>loss = torch.mse(noise_pred, noise)</p>
<p>loss.backward()</p>
<p># Pseudocode for Generating Samples</p>
<p>x_t = torch.randn(shape)</p>
<p>for t in range(T, 0):</p>
<p>noise_pred = model(x_t, t)</p>
<p>x_t = noise_scheduler.step(</p>
<p>x_t, noise_pred)</p>
<ul>
<li><p>diffusion models are state-of-the-art for image generation</p></li>
<li><p>can be generalized to class-conditional or text-conditioned image generation</p></li>
<li><p>trained via ELBO instead of maximum likelihood</p></li>
<li><p>no architectural constraints on NN shape or structure</p></li>
</ul></td>
</tr>
<tr>
<td>Additional Readings</td>
<td colspan="3"><ul>
<li><p>What Are Diffusion Models? (Lillian Weng’s Blog)</p></li>
<li><p>Diffusion Models as a Kind of VAE (Angus Turner’s Blog)</p></li>
<li><p>Denoising Diffusion Probabilistic Models (Ho et. al. 2020)</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4"></td>
</tr>
</tbody>
</table>
