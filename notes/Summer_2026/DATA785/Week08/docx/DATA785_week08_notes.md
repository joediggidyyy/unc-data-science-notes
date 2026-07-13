> Markdown version for convenient browsing. Original files:
> - PDF: [DATA785_week08_notes.pdf](../DATA785_week08_notes.pdf)
> - DOCX: [DATA785_week08_notes.docx](DATA785_week08_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 5%" />
<col style="width: 18%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Advanced RNN Topics</th>
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
<li><p>enumerate advanced RNN architectures including GRUs and LSTMs for handling long-term dependencies</p></li>
<li><p>implement sampling and beam search strategies for generating sequences</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td>Advanced Topics with RNNs</td>
<td colspan="4"><ul>
<li><p>using RNNs for classification</p>
<ul>
<li><p>take the last token’s hidden representation (<span class="math inline"><em>h</em><sub><em>n</em></sub></span>) as the representation of the sequence</p></li>
<li><p>loss computed at the FFN’s softmax layer</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA785_week08_notes\media\image1.png" style="width:4.79167in;height:3.18197in" /></p>
<p>Gemini 3.5</p>
<p><span class="math display"><em>F</em><em>N</em><em>N</em></span></p>
<p><span class="math display"><em>R</em><em>N</em><em>N</em>→</span></p>
<ul>
<li><p>errors flow back to RNN (end to end training)</p></li>
</ul>
<ul>
<li><p>alternative:</p>
<ul>
<li><p>element-wise mean or max over states</p></li>
<li><p>example: <span class="math inline">$h_{seq} ≔ \frac{1}{n}\sum_{}^{}h_{i}$</span></p></li>
</ul></li>
<li><p>RNN Training</p>
<ul>
<li><p>use a text corpus – make the RNN model predict the next word at each time step <span class="math inline"><em>t</em></span></p>
<ul>
<li><p>RNN does not predict the word directly</p></li>
<li><p>at each time step <span class="math inline"><em>t</em></span>, it predicts a probability distribution over vocab: <span class="math inline"><em>ŷ</em><sub><em>t</em></sub></span></p></li>
<li><p>next word is sampled from this probability distribution: <span class="math inline"><em>ŷ</em><sub><em>t</em></sub> </span></p></li>
</ul></li>
</ul></li>
</ul>
<p><span class="math display"><em>h</em><sub><em>t</em></sub> = <em>σ</em>(<em>W</em><sub>1</sub><em>h</em><sub><em>t</em> − 1</sub> + <em>W</em><sub>2</sub><em>x</em> + <em>b</em>)</span></p>
<p><span class="math display"><em>ŷ</em><sub><em>t</em></sub> = <em>λ</em>(<em>W</em><sub>3</sub><em>h</em><sub><em>t</em></sub>)</span></p>
<ul>
<li><p>objective function is to minimize the error in predicting the next word using <em>cross-entropy</em> as the loss function</p></li>
</ul>
<ul>
<li><p>Cross-Entropy Loss for Sequence Modeling</p>
<ul>
<li><p>measures the difference between a predicted probability distribution and the correct distribution</p>
<ul>
<li><p>correct distribution (over full vocabulary): <span class="math inline"><em>y</em><sub><em>t</em></sub></span></p></li>
<li><p>predicted distribution (over full vocabulary): <span class="math inline"><em>ŷ</em><sub><em>t</em></sub></span></p></li>
</ul></li>
</ul></li>
</ul>
<p><span class="math display">$$L_{CE} = - \sum_{w \in V}^{}{y_{t}\lbrack w\rbrack\log{{\widehat{y}}_{t}\lbrack w\rbrack}}$$</span></p>
<ul>
<li><p>probability of a word <span class="math inline"><em>w</em></span> under a distribution:</p></li>
</ul>
<p><span class="math display"><em>y</em><sub><em>t</em></sub> = <em>y</em><sub><em>t</em></sub>[<em>w</em>]</span></p>
<ul>
<li><p>in language modeling</p>
<ul>
<li><p>we know the next word (<span class="math inline"><em>y</em><sub><em>t</em></sub></span>) is a one-hot vector with <span class="math inline"><em>d</em><em>i</em><em>m</em> = |<em>V</em>|</span> where the entry for the next word is 1 and the rest are 0</p></li>
<li><p>cross-entropy loss at time <span class="math inline"><em>t</em></span> is:</p></li>
</ul></li>
</ul>
<p><span class="math display"><em>L</em><sub><em>C</em><em>E</em></sub>(<em>ŷ</em><sub><em>t</em></sub>, <em>y</em><sub><em>t</em></sub>) = −log <em>ŷ</em><sub><em>t</em></sub>[<em>w</em><sub><em>t</em> + 1</sub>]</span></p>
<ul>
<li><p><img src="generated_media\DATA785_week08_notes\media\image2.png" style="width:4.69722in;height:2.625in" />Teacher Forcing</p></li>
</ul>
<p>Gemini 3.5</p>
<ul>
<li><p>at train time, feed the initial input word at <span class="math inline"><em>t</em></span> irrespective of what the model predicted at <span class="math inline"><em>t</em> − 1</span></p></li>
<li><p>embeddings <span class="math inline"><em>e</em><sub><em>t</em></sub></span> can be obtained by multiplying input (one-hot) vector of <span class="math inline"><em>x</em><sub><em>t</em></sub></span> with matrix <span class="math inline">$E_{d_{h} \times |\widetilde{V|}}$</span>, where <span class="math inline"><em>Ṽ</em> = <em>v</em><em>o</em><em>c</em><em>a</em><em>b</em><em>u</em><em>l</em><em>a</em><em>r</em><em>y</em></span></p></li>
<li><p><span class="math inline"><em>E</em></span> is the input embedding matrix</p>
<ul>
<li><p>columns of <span class="math inline"><em>E</em></span> are the embeddings for words in <span class="math inline"><em>Ṽ</em></span></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Gradient Computation</td>
<td colspan="4"><ul>
<li><p>Gradient Computation with RNNs</p>
<ul>
<li><p>RNNs can still be trained with backpropagation</p></li>
<li><p>gradient involved repeated multiplications of <span class="math inline"><em>W</em></span>s</p></li>
</ul></li>
</ul>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><p><span class="math display"><em>h</em><sub><em>t</em></sub> = tanh (<em>U</em><em>x</em><sub><em>t</em></sub> + <em>W</em><em>h</em><sub><em>t</em> − 1</sub>)</span></p>
<p><span class="math display"><em>z</em><sub><em>t</em></sub> = <em>U</em><em>x</em><sub><em>t</em></sub> + <em>W</em><em>h</em><sub><em>t</em> − 1</sub></span></p>
<p><span class="math display"><em>h</em><sub><em>t</em></sub> = tanh (<em>z</em><sub><em>t</em></sub>)</span></p></th>
<th style="text-align: center;"><p><span class="math display">$$\frac{\partial E_{k}}{\partial W} = \frac{\partial E_{k}}{\partial h_{k}}\frac{\partial h_{k}}{\partial W}$$</span></p>
<p><span class="math display">$$\frac{\partial h_{k}}{\partial W} = \frac{\partial h_{k}}{\partial z_{k}}\frac{\partial z_{k}}{\partial W}$$</span></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p><span class="math display">$$\frac{\partial z_{k}}{\partial W} = h_{k - 1} + W\frac{\partial h_{k - 1}}{\partial W}$$</span></p>
<ul>
<li><p>the issue with W being continually propagated through this chain is, depending on the state of W, the gradient will likely either vanish or explode</p></li>
</ul>
<ul>
<li><p>solutions:</p>
<ul>
<li><p>special activations</p>
<ul>
<li><p>gradient of ReLU activation avoids this</p></li>
</ul></li>
<li><p>normalization techniques</p>
<ul>
<li><p>batch and layer normalization to normalize the activations of a network</p></li>
</ul></li>
<li><p>gradient clipping</p>
<ul>
<li><p>clipping to a max value avoids gradient explosion</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Greedy and Beam Search</td>
<td colspan="4"><ul>
<li><p>greedy decoding:</p>
<ul>
<li><p>at any time step, generate the most likely word<span class="math inline">:</span></p></li>
</ul></li>
</ul>
<p><span class="math display"><em>ŵ</em><sub><em>t</em></sub> = <em>a</em><em>r</em><em>g</em><em>m</em><em>a</em><em>x</em><sub><em>w</em>∈ <em>V</em> </sub><em>P</em>(<em>w</em>|<em>w</em><sub> &lt; <em>t</em></sub>)</span></p>
<ul>
<li><p>locally optimal</p></li>
<li><p>leads to extremely predictable results</p>
<ul>
<li><p>output is generic and repetitive</p></li>
</ul></li>
<li><p>not commonly used in practice</p></li>
</ul>
<ul>
<li><p>beam search is a good alternative</p>
<ul>
<li><p>common in very constrained tasks like machine translation</p></li>
</ul></li>
<li><p>alternatives commonly used in LMs</p>
<ul>
<li><p>top-k sampling</p></li>
<li><p>top-p/nucleus sampling</p></li>
<li><p>temperature sampling</p></li>
</ul></li>
<li><p>greedy search tree</p>
<ul>
<li><p>representation of the search space for the output</p></li>
<li><p><img src="generated_media\DATA785_week08_notes\media\image3.png" style="width:4.83333in;height:3.743in" />branches represent possible actions</p></li>
</ul></li>
</ul>
<p>Gemini 3.5</p>
<ul>
<li><p>the greedy output (taking argmax)</p>
<ul>
<li><p><span class="math inline"><em>y</em><em>e</em><em>s</em>, <em>y</em><em>e</em><em>s</em>,  &lt; /<em>s</em>&gt;</span></p></li>
<li><p><span class="math inline"><em>p</em><em>r</em><em>o</em><em>b</em><em>a</em><em>b</em><em>i</em><em>l</em><em>i</em><em>t</em><em>y</em> = 0.5 * 0.4 * 1.0= 0.2</span></p></li>
</ul></li>
<li><p>highest probability output</p>
<ul>
<li><p><span class="math inline"><em>o</em><em>k</em>, <em>o</em><em>k</em>,  &lt; /<em>s</em>&gt;</span></p></li>
<li><p><span class="math inline"><em>p</em><em>r</em><em>o</em><em>b</em><em>a</em><em>b</em><em>i</em><em>l</em><em>i</em><em>t</em><em>y</em> = 0.4 * 0.7 * 1.0 = 0.28</span></p></li>
</ul></li>
<li><p>greedy search may not uncover the global optimal output</p>
<ul>
<li><p>to obtain, execute exhaustive search of all possible sequences</p></li>
<li><p>for a vocabulary of size <span class="math inline"><em>V</em></span> and an output of length <span class="math inline"><em>T</em></span></p>
<ul>
<li><p>you must explore <span class="math inline"><em>V</em><sub><em>T</em></sub></span> sequences</p></li>
</ul></li>
</ul></li>
</ul>
<ul>
<li><p>Beam Search</p>
<ul>
<li><p>keep track of the <span class="math inline"><em>K</em></span> best possibilities at each step</p>
<ul>
<li><p><span class="math inline"><em>K</em></span> would be called the beam width</p>
<ul>
<li><p>generally ~5 or 10</p></li>
</ul></li>
</ul></li>
<li><p>at <span class="math inline"><em>i</em> = 1</span></p>
<ul>
<li><p>given <span class="math inline"><em>x</em></span> (source text), obtain probability distribution over entire vocabulary</p></li>
<li><p>keep the top <span class="math inline"><em>K</em></span> (highest probability) tokens</p></li>
</ul></li>
<li><p>for <span class="math inline"><em>i</em> = 2</span> onwards</p>
<ul>
<li><p>obtain probability distributions over entire vocabulary given the <span class="math inline"><em>K</em></span> possibilities from <span class="math inline"><em>i</em> – 1</span></p>
<ul>
<li><p><span class="math inline"><em>K</em>  × <em>V</em></span> options</p></li>
</ul></li>
<li><p>compute probability score for each of the <span class="math inline"><em>K</em>× <em>V</em></span> options</p>
<ul>
<li><p><span class="math inline"><em>P</em>(<em>y</em><sub><em>i</em></sub>|<em>x</em>, <em>y</em><sub>1</sub>, <em>y</em><sub>2</sub>, …, <em>y</em><sub><em>i</em> − 1</sub>)</span></p></li>
</ul></li>
<li><p>keep the top <span class="math inline"><em>K</em></span> highest scoring options out of the <span class="math inline"><em>K</em>× <em>V</em></span> options</p>
<ul>
<li><p><span class="math inline"><em>s</em></span></p></li>
</ul></li>
</ul></li>
<li><p><img src="generated_media\DATA785_week08_notes\media\image4.png" style="width:4.84474in;height:3.14151in" />result:</p></li>
</ul></li>
</ul>
<p>Gemini 3.5</p>
<ul>
<li><p><span class="math inline"><em>K</em></span> paths, now pick the highest scoring among them</p></li>
</ul></td>
</tr>
<tr>
<td>Advanced Sampling Methods</td>
<td colspan="4"><ul>
<li><p>by only generating the highest probability words, you can end up with grammatical, but predictable and repetitive sentences</p></li>
<li><p>sometimes picking the 2<sup>nd</sup>, 3<sup>rd</sup>, or 4<sup>th</sup> word might be more interesting</p></li>
<li><p>two important factors</p>
<ul>
<li><p>quality</p>
<ul>
<li><p>highest probability words</p></li>
</ul></li>
<li><p>diversity</p>
<ul>
<li><p>high, not highest probability words</p></li>
</ul></li>
</ul></li>
<li><p>top-k sampling</p>
<ul>
<li><p>simple generalization of greedy decoding</p>
<ul>
<li><p>choose in advance a number of words <span class="math inline"><em>k</em></span></p></li>
<li><p>truncate the distribution to the top <span class="math inline"><em>k</em></span> most likely words</p></li>
<li><p>renormalize to produce a legitimate probability distribution</p></li>
<li><p>randomly sample from within these k words according to their renormalized probabilities</p></li>
</ul></li>
<li><p>when <span class="math inline"><em>k</em> = 1:</span></p>
<ul>
<li><p>top-k sampling = greedy decoding</p></li>
</ul></li>
<li><p><span class="math inline"><em>k</em> &gt; 1</span>:</p>
<ul>
<li><p>select a word which is not the most probable, but still probable enough</p></li>
<li><p>results in generating more diverse but still high-quality text</p></li>
</ul></li>
</ul></li>
<li><p>top-p / nucleus sampling</p>
<ul>
<li><p>for top-k, k is fixed</p>
<ul>
<li><p>for some contexts, original probability distribution can be flat</p></li>
<li><p>top-k words can cover most of the original probability mass</p></li>
<li><p>for other contexts, original probability distribution can be flat</p></li>
<li><p>top-k words will convert only a small part of the original probability mass</p></li>
</ul></li>
<li><p>solution</p>
<ul>
<li><p>use percent instead of absolute <span class="math inline"><em>k</em></span> value</p></li>
</ul></li>
</ul></li>
</ul>
<p><span class="math display">$$\sum_{w \in V^{p}}^{}{P(w|w_{&lt; t}) \geq p}$$</span></p>
<ul>
<li><p>temperature sampling</p>
<ul>
<li><p>don’t truncate the distribution</p></li>
<li><p>reshape it instead</p></li>
<li><p>intuition from thermodynamics</p>
<ul>
<li><p>a system at high temperature is flexible and can explore many possible states</p></li>
<li><p>while the system is at a lower temperature, it is likely to explore a subset of lower energy (better) states</p></li>
</ul></li>
<li><p>low-temperature sampling</p>
<ul>
<li><p>smoothly increase the probability of the most probable “common” words and decrease the probability of the “rare” words</p></li>
</ul></li>
<li><p>reminder: with RNNs</p>
<ul>
<li><p>hidden states from the last layer used to obtain scores (logits, V-dimensional) via a linear layer</p></li>
<li><p>logits converted to a probability distribution using a softmax function</p></li>
</ul></li>
<li><p>in temperature sampling</p>
<ul>
<li><p>divide the logits by a temperature, <span class="math inline"><em>τ</em> ∈ (0, 1]</span> before doing softmax</p></li>
</ul></li>
</ul></li>
</ul>
<p><span class="math display"><em>y</em> = <em>s</em><em>o</em><em>f</em><em>t</em><em>m</em><em>a</em><em>x</em>(<em>u</em> / <em>τ</em>)</span></p></td>
</tr>
<tr>
<td>Summary</td>
<td colspan="4"><ul>
<li><p>greedy decoding</p>
<ul>
<li><p>leads to extremely predictable results</p>
<ul>
<li><p>output is generic and repetitive</p></li>
</ul></li>
</ul></li>
<li><p>beam search is a good alternative</p></li>
<li><p>alternatives commonly used in LLMs</p>
<ul>
<li><p>top-k sampling</p></li>
<li><p>top-p / nucleus sampling</p></li>
<li><p>temperature sampling</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="5"></td>
</tr>
</tbody>
</table>
