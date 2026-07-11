> Markdown version for convenient browsing. Original files:
> - PDF: [DATA785_week04_notes.pdf](../DATA785_week04_notes.pdf)
> - DOCX: [DATA785_week04_notes.docx](DATA785_week04_notes.docx)

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
<th colspan="2">Word Embeddings</th>
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
<li><p>outline the concept of representation learning and its importance in deep learning</p></li>
<li><p>implement and apply word embeddings for natural language processing tasks</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td>Text Representations and Distance Functions</td>
<td colspan="4"><ul>
<li><p>bag of words</p>
<ul>
<li><p>represents text as a vector of counts of vocabulary words or binary values</p></li>
</ul></li>
<li><p>effective text representation models</p>
<ul>
<li><p>leads to good task performance</p></li>
<li><p>results in semantically similar texts having similar representations</p></li>
</ul></li>
<li><p>distance functions</p>
<ul>
<li><p>Euclidian Distance</p></li>
</ul></li>
</ul>
<p><span class="math display">$$for\ a,b \in \mathbb{R}^{d}\ \ \ \ \ \ d(a,b) = \sqrt{\sum_{i = 2}^{d}\left( a_{i} - b_{i} \right)^{2}}$$</span></p>
<ul>
<li><p>Cosine Similarity</p></li>
</ul>
<p><span class="math display">$$for\ a,b \in \mathbb{R}^{d}\ \ \ \ \ sim(a,b) = \frac{a.b}{\left| |a| \right|\left| |b| \right|} = \cos a$$</span></p>
<ul>
<li><p>small <span class="math inline"><em>α</em></span>: high similarity</p></li>
<li><p>-1: opposing direction</p></li>
<li><p>+1: same direction</p></li>
<li><p>0: orthogonal vectors</p></li>
</ul></td>
</tr>
<tr>
<td><p>Word Embeddings/</p>
<p>Word2vec</p></td>
<td colspan="4"><ul>
<li><p>map each word to a vector in <span class="math inline">ℝ<sup><em>d</em></sup></span> such that similar words also have similar word vectors</p></li>
<li><p>this is used heavily in polymath applications such as OraCode</p></li>
</ul></td>
</tr>
<tr>
<td>Skip-Gram Model</td>
<td colspan="4"><ul>
<li><p>given a word, predict its neighboring words within a window</p></li>
<li><p>example: is the word ‘brown’ likely to fall in the context window with ‘fox’</p></li>
<li><p>objective to maximize: likelihood is product of <span class="math inline"><em>P</em>(<em>c</em><em>o</em><em>n</em><em>t</em><em>e</em><em>x</em><em>t</em>|<em>w</em><em>o</em><em>r</em><em>d</em>)</span> looping over all words in training data and their context words within a window of m</p></li>
</ul>
<p><span class="math display">$$\mathcal{L}(\theta)\  = \ \prod_{t = 1}^{T}{\prod_{\begin{array}{r}
 - m\  \leq j\  \leq m;\  \\
j\  \neq 0
\end{array}}^{}{P\left( w_{t + j}\  \right|w_{t}\ ;\ \theta)}}\ \ $$</span></p>
<ul>
<li><p>we will maximize the log likelihood</p></li>
</ul>
<p><span class="math display">$$J(\theta) = \ \sum_{t = 1}^{T}{\sum_{\begin{array}{r}
 - m\  \leq j\  \leq m;\  \\
j\  \neq 0
\end{array}}^{}{\log{P\left( w_{t + j}\  \right|}w_{t}\ ;\ \theta)}\ } = \ \sum_{t = 1}^{T}{\sum_{\begin{array}{r}
 - m\  \leq j\  \leq m;\  \\
j\  \neq 0
\end{array}}^{}{\log\left( \frac{\exp\left( u_{w_{t}}^{T}\ v_{w_{t + j}} \right)}{\sum_{w \in V}^{}{\exp\left( u_{w_{t}}^{T}\ v_{w_{t + j}} \right)}} \right)}}\ $$</span></p>
<p><span class="math display">$$= \ \sum_{t = 1}^{T}{\sum_{\begin{array}{r}
 - m\  \leq j\  \leq m;\  \\
j\  \neq 0
\end{array}}^{}{u_{w_{t}}^{T}v_{w_{t + j}}}} - \log{\sum_{w \in V}^{}{\exp\left( u_{w_{t}}^{T}v_{w_{t + j}} \right)}}$$</span></p>
<ul>
<li><p>gradient descent would be inefficient here, so:</p>
<ul>
<li><p>set up task binary classification (positive and negative)</p>
<ul>
<li><p>is ‘brown’ likely to appear with ‘fox’?</p></li>
<li><p>is ‘computer’ likely to appear with ‘fox’?</p></li>
</ul></li>
<li><p>construct example pairs</p>
<ul>
<li><p>consider a large text source – like Wikipedia - and set up positive examples by pairing target words</p></li>
<li><p>create negative examples by randomly pairing other words</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Continuous Bag of Words (CBOW) Model</td>
<td colspan="4"><ul>
<li><p>given the context, predict the word in the middle</p></li>
<li><p>model <span class="math inline"><em>P</em>(<em>f</em><em>o</em><em>x</em>|<em>q</em><em>u</em><em>i</em><em>c</em><em>k</em> <em>b</em><em>r</em><em>o</em><em>w</em><em>n</em> <em>j</em><em>u</em><em>m</em><em>p</em><em>s</em> <em>o</em><em>v</em><em>e</em><em>r</em>)</span></p></li>
<li><p>implementation similar to skip-gram</p></li>
<li><p>instead of pairs token, we have a token and a context consisting of multiple tokens</p></li>
<li><p>we handle this by representing the context with the sum of representations of all tokens in the context</p></li>
</ul></td>
</tr>
<tr>
<td>Properties of Word Embeddings</td>
<td colspan="4"><ul>
<li><p>size of window affects the type of similarity</p></li>
<li><p>shorter window produces syntactically similar words</p>
<ul>
<li><p>ex: Hogwarts -&gt; Sunnydale (fictional school)</p></li>
</ul></li>
<li><p>longer window produces topically related words</p>
<ul>
<li><p>ex: Hogwarts -&gt; Dumbledore</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>
