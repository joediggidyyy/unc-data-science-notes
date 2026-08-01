> Markdown version for convenient browsing. Original files:
> - PDF: [DATA785_week09_notes.pdf](../DATA785_week09_notes.pdf)
> - DOCX: [DATA785_week09_notes.docx](DATA785_week09_notes.docx)

---

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 3%" />
<col style="width: 23%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Transformers</th>
<th></th>
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
<li><p>outline the insights and applications of Transformer models</p></li>
<li><p>implement pre-training and fine-tuning</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Looking Back at RNNs</td>
<td colspan="3"><ul>
<li><p>form of <span class="math inline"><em>f</em><sub><em>R</em><em>N</em><em>N</em></sub></span></p></li>
</ul>
<p><span class="math display"><em>h</em><sub><em>t</em></sub> = <em>σ</em>[<em>W</em><sub>1</sub><em>h</em><sub><em>t</em> − 1</sub> + <em>W</em><sub>2</sub><em>x</em><sub>1</sub> + <em>b</em><sub>1</sub>]</span></p>
<ul>
<li><p>RNN is defined by ‘<span class="math inline"><em>W</em><sub>1</sub>, <em>W</em><sub>2</sub>, <em>a</em><em>n</em><em>d</em> <em>b</em><sub>1</sub></span>’</p></li>
</ul>
<ul>
<li><p>form of <span class="math inline"><em>f</em><sub><em>p</em><em>r</em><em>e</em><em>d</em></sub></span></p></li>
</ul>
<p><span class="math display"><em>o</em><sub><em>t</em></sub> = <em>s</em><em>o</em><em>f</em><em>t</em><em>m</em><em>a</em><em>x</em>[<em>W</em><sub>3</sub><em>h</em><sub><em>t</em></sub>]</span></p>
<ul>
<li><p>encoder-decoder RNNs</p>
<ul>
<li><p>two RNNs paired together</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Design Hyper-Parameters</td>
<td colspan="3"><ul>
<li><p><span class="math inline"><em>L</em></span>: number of layers</p></li>
<li><p><span class="math inline"><em>H</em></span>:number of attention heads</p></li>
<li><p><span class="math inline"><em>d</em><sub><em>q</em><em>k</em></sub></span>: dimensionality of query and key vectors “<em>(</em><span class="math inline">$d_{qk}is\ d')"$</span></p></li>
<li><p><span class="math inline"><em>d</em><sub><em>v</em></sub></span>: dimensionality of value vectors (usually the same as <span class="math inline"><em>d</em><sub><em>q</em><em>k</em></sub></span> <span class="math inline">$"(d)"$</span></p></li>
<li><p><span class="math inline"><em>d</em><sub><em>m</em><em>o</em><em>d</em><em>e</em><em>l</em></sub></span>: dimensionality along residual path</p></li>
<li><p><span class="math inline"><em>d</em><sub><em>f</em><em>f</em></sub></span>: dimensionality inside FNN</p></li>
<li><p>Usually:</p></li>
</ul>
<p><span class="math display"><em>d</em><sub><em>m</em><em>o</em><em>d</em><em>e</em><em>l</em></sub> = <em>H</em><em>d</em><sub><em>v</em></sub></span></p>
<p><span class="math display"><em>d</em><sub><em>f</em><em>f</em></sub> = 4 <em>d</em><sub><em>m</em><em>o</em><em>d</em><em>e</em><em>l</em></sub></span></p></td>
</tr>
<tr>
<td colspan="2">Encoder Only Transformers</td>
<td colspan="3"><ul>
<li><p>process input sequences without generating outputs</p></li>
<li><p>excel in tasks such as text classification and sentiment analysis</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Bidirectional Encoder Representations From Transformers (BERT)</td>
<td colspan="3"><ul>
<li><p>earlier language models (like the original GPT) read text sequentially—either left-to-right or right-to-left</p></li>
<li><p>this created limitations when the meaning of a word depended on the words following it</p></li>
<li><p>BERT solves this by analyzing words from both sides using a self-attention mechanism, providing a deeper, human-like understanding of context</p></li>
<li><p>pre-training tasks</p>
<ul>
<li><p>masked language modeling (MLM)</p>
<ul>
<li><p>model randomly masks a portion of the input words and is trained to predict the missing words</p></li>
</ul></li>
<li><p>next sentence prediction (NSP)</p>
<ul>
<li><p>predicts whether two sentences appear sequentially in a document, helping the model grasp long-range dependencies and relationships between texts</p></li>
</ul></li>
</ul></li>
<li><p>architecture</p>
<ul>
<li><p>unlike models that use both encoders and decoders for text generation, BERT uses an encoder-only transformer stack</p></li>
</ul></li>
<li><p>fine tuning</p>
<ul>
<li><p>task selection</p>
<ul>
<li><p>choose whether your downstream task requires sequence-level outputs (e.g., classifying a whole email as spam) or token-level outputs</p></li>
</ul></li>
<li><p>architecture adjustment</p>
<ul>
<li><p>remove the pre-training heads and attach a minimal, task-specific output layer (such as a multi-layer perceptron) directly on top of BERT's encoder outputs</p></li>
</ul></li>
<li><p>training</p>
<ul>
<li><p>feed your labeled dataset into the model</p></li>
<li><p>during this phase, you update the newly added output layer and adjust (fine-tune) the pre-trained BERT weights to minimize prediction error</p></li>
</ul></li>
<li><p>learning rate</p>
<ul>
<li><p>fine-tuning generally requires much smaller learning rates (e.g., 2 × 10⁻⁵ to 5 × 10⁻⁵) than pre-training to prevent "catastrophic forgetting" of the previously learned language knowledge</p></li>
</ul></li>
<li><p>batch size</p>
<ul>
<li><p>using slightly larger batch sizes (like 16 or 32) can stabilize gradient updates on smaller datasets</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Decoder Only Transformers</td>
<td colspan="3"><ul>
<li><p>focus on generating output sequences</p></li>
<li><p>most suitable for language modelling tasks such as text generation and completion</p></li>
<li><p>GPT is a decoder-only transformer model</p></li>
<li><p>analysis is of generated words only, differing from the bidirectionality of BERT</p></li>
<li><p>uses transformer stack for language generation</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">How to Train a Decoder-Only Transformer Stack</td>
<td colspan="3"><ul>
<li><p>ignore attention scores for future tokens in self-attention</p></li>
<li><p>set upper-triangular portion of the <span class="math inline"><em>Q</em><em>K</em><sup><em>T</em></sup></span> matrix to <span class="math inline">−∞</span></p></li>
</ul>
<p>this is called “causal masking”</p>
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
<th style="text-align: center;"><span class="math display"><em>q</em><sub>1</sub> • <em>k</em><sub>1</sub></span></th>
<th style="text-align: center;"><span class="math display">−∞</span></th>
<th style="text-align: center;"><span class="math display">−∞</span></th>
<th style="text-align: center;"><span class="math display">−∞</span></th>
<th style="text-align: center;"><span class="math display">−∞</span></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>2</sub> • <em>k</em><sub>1</sub></span></td>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>2</sub> • <em>k</em><sub>2</sub></span></td>
<td style="text-align: center;"><span class="math display">−∞</span></td>
<td style="text-align: center;"><span class="math display">−∞</span></td>
<td style="text-align: center;"><span class="math display">−∞</span></td>
</tr>
<tr>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>3</sub> • <em>k</em><sub>1</sub></span></td>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>3</sub> • <em>k</em><sub>2</sub></span></td>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>3</sub> • <em>k</em><sub>3</sub></span></td>
<td style="text-align: center;"><span class="math display">−∞</span></td>
<td style="text-align: center;"><span class="math display">−∞</span></td>
</tr>
<tr>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>4</sub> • <em>k</em><sub>1</sub></span></td>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>4</sub> • <em>k</em><sub>2</sub></span></td>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>4</sub> • <em>k</em><sub>3</sub></span></td>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>4</sub> • <em>k</em><sub>4</sub></span></td>
<td style="text-align: center;"><span class="math display">−∞</span></td>
</tr>
<tr>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>5</sub> • <em>k</em><sub>1</sub></span></td>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>5</sub> • <em>k</em><sub>2</sub></span></td>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>5</sub> • <em>k</em><sub>3</sub></span></td>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>5</sub> • <em>k</em><sub>4</sub></span></td>
<td style="text-align: center;"><span class="math display"><em>q</em><sub>5</sub> • <em>k</em><sub>5</sub></span></td>
</tr>
</tbody>
</table>
<ul>
<li><p>apart from causal masking, no difference from the encoder-only architecture</p></li>
<li><p><strong>IMPORTANT</strong>: unlike RNN LMs, this training can be completely parallelized</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Advantages of Transformer-Based Generation</td>
<td colspan="3"><ul>
<li><p>parallelized training can enable larger models and training sets</p></li>
<li><p>training is stable compared to RNNs</p>
<ul>
<li><p>dur to layer normalization and residual connections</p></li>
<li><p>no vanishing or exploding gradients, “path length” is always = 1</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">GPT Series of LMs</td>
<td colspan="3"><ul>
<li><p>GPT = Generative Pretrained Transformers</p></li>
</ul>
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
<th>Model</th>
<th style="text-align: center;">Parameters</th>
<th style="text-align: center;">Decoder Layers</th>
<th style="text-align: center;">Context Window Size</th>
<th style="text-align: center;">Hidden Layer Size</th>
</tr>
</thead>
<tbody>
<tr>
<td>GPT-1</td>
<td style="text-align: center;">117 M</td>
<td style="text-align: center;">12</td>
<td style="text-align: center;">512</td>
<td style="text-align: center;">768</td>
</tr>
<tr>
<td>GPT-2</td>
<td style="text-align: center;">1.5 B</td>
<td style="text-align: center;">48</td>
<td style="text-align: center;">1024</td>
<td style="text-align: center;">1600</td>
</tr>
<tr>
<td>GPT-3</td>
<td style="text-align: center;">175 B</td>
<td style="text-align: center;">96</td>
<td style="text-align: center;">2048</td>
<td style="text-align: center;">12288</td>
</tr>
<tr>
<td>GPT-4</td>
<td style="text-align: center;">Unknown</td>
<td style="text-align: center;">Unknown</td>
<td style="text-align: center;">Unknown</td>
<td style="text-align: center;">Unknown</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td colspan="2">Encoder-Decoder Transformers</td>
<td colspan="3"><ul>
<li><p>this was the original transformer architecture</p>
<ul>
<li><p>machine translation / summarization</p></li>
</ul></li>
<li><p>example</p>
<ul>
<li><p>“even when <strong>he</strong> was a young boy, Rich Sanchez…”</p></li>
<li><p>identifies the pronoun precedes the subject that it references</p></li>
</ul></li>
<li><p>T5 (Text-to-Text Transfer Transformer)</p>
<ul>
<li><p>unified approach where all NLP tasks are reformulated as text-to-test tasks</p></li>
<li><p>example</p>
<ul>
<li><p>“classify sentiment: the movie was horrendous…”</p></li>
</ul></li>
</ul></li>
<li><p>BART (Bidirectional and Auto-Regressive Transform)</p>
<ul>
<li><p>combines bidirectional and auto-regressive training objective</p></li>
<li><p>good with both generation and sequence-to-sequence tasks</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="5"></td>
</tr>
</tbody>
</table>
