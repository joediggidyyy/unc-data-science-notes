> Markdown version for convenient browsing. Original files:
> - PDF: [DATA785_week07_notes.pdf](../DATA785_week07_notes.pdf)
> - DOCX: [DATA785_week07_notes.docx](DATA785_week07_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Sequence Modeling and RNNs</th>
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
<li><p>evaluate and critique techniques for modeling sequential data with N-grams and Recurrent Neural Networks (RNNs)</p></li>
<li><p>identify and describe the probabilistic basis of Language Models</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td>Modeling Sequential Data</td>
<td colspan="4"><ul>
<li><p>examples of sequence modeling</p>
<ul>
<li><p>weather forecasting</p></li>
<li><p>stock market trends</p></li>
<li><p>autocomplete for texting</p></li>
<li><p>genetic sequencing</p></li>
<li><p>speech recognition</p></li>
<li><p>video frame projection</p></li>
<li><p>music composition</p></li>
</ul></li>
<li><p>sequences can be thought about as a list and can span many scopes and formats</p>
<ul>
<li><p>bytes</p></li>
<li><p>letters (words)</p></li>
<li><p>words (sentences)</p></li>
<li><p>sentences (documents)</p></li>
<li><p>frames (video)</p></li>
<li><p>amino-acids (genetic code)</p></li>
</ul></li>
<li><p>the goal of sequence modeling is to compute the probability of a sequence of items</p></li>
</ul>
<p><span class="math display"><em>P</em>(<em>X</em>) = <em>P</em>(<em>x</em><sub>1</sub>, <em>x</em><sub>2</sub>, <em>x</em><sub>3</sub>, …, <em>x</em><sub><em>n</em></sub>)</span></p>
<ul>
<li><p>what it the next item in the sequence?</p></li>
</ul>
<p><span class="math display"><em>P</em>(<em>x</em><sub>5</sub>|<em>x</em><sub>1</sub>, <em>x</em><sub>2</sub>, <em>x</em><sub>3</sub>, <em>x</em><sub>4</sub>)</span></p>
<ul>
<li><p>recall the chain rule:</p>
<ul>
<li><p>definition of conditional probabilities</p></li>
</ul></li>
</ul>
<p><span class="math display"><em>P</em>(<em>A</em>, <em>B</em>) = <em>P</em>(<em>A</em>)<em>P</em>(<em>B</em>|<em>A</em>)</span></p>
<ul>
<li><p>with &gt; 2 variables</p></li>
</ul>
<p><span class="math display"><em>P</em>(<em>A</em>, <em>B</em>, <em>C</em>, <em>D</em>) = <em>P</em>(<em>A</em>)<em>P</em>(<em>B</em>|<em>A</em>)<em>P</em>(<em>C</em>|<em>B</em>, <em>A</em>)<em>P</em>(<em>D</em>|<em>A</em>, <em>B</em>, <em>C</em>)</span></p>
<ul>
<li><p>history-based models</p></li>
</ul>
<p>implication: <em>each token is dependent on all previous tokens</em></p>
<p><span class="math display"><em>P</em>(<em>x</em><sub>1</sub>…<em>x</em><sub><em>n</em></sub>) = <em>P</em>(<em>x</em><sub>1</sub>)<em>P</em>(<em>x</em><sub>2</sub>|<em>x</em><sub>1</sub>)<em>P</em>(<em>x</em><sub>3</sub>…<em>x</em><sub><em>n</em></sub>|<em>x</em><sub>1</sub>, <em>x</em><sub>2</sub>)</span></p>
<p><span class="math display">$$= \prod_{i = 1}^{n}{P(x_{i}|x_{1},x_{2}\ldots x_{i - 1})}$$</span></p>
<ul>
<li><p>this presents a complexity issue as the number of parameters scales with length of sequence</p></li>
</ul></td>
</tr>
<tr>
<td>Markov Models</td>
<td colspan="4"><ul>
<li><p>the complexity issue can be mitigated by limiting the history with Markov Assumption</p>
<ul>
<li><p>state is independent of history given previous state</p></li>
</ul></li>
</ul>
<p>ignore older history</p>
<p><span class="math display"><em>P</em>(<em>x</em><sub><em>i</em></sub>|<em>x</em><sub>1</sub>, <em>x</em><sub>2</sub>…<em>x</em><sub><em>i</em> − 1</sub>) = <em>P</em>(<em>x</em><sub><em>i</em></sub>|<em>x</em><sub><em>i</em> − 1</sub>)</span></p>
<p><span class="math display">$$P\left( x_{1}\ldots x_{n} \right) = \prod_{i = 1}^{n}{P\left( x_{i} \middle| x_{1},x_{2}\ldots x_{i - 1} \right) = \prod_{i = 1}^{n}{P(x_{i}|x_{i - 1})}}$$</span></p>
<ul>
<li><p>first order MM:</p>
<ul>
<li><p>maintain history of last state</p></li>
<li><p>bigram model</p></li>
</ul></li>
<li><p>second order MM:</p>
<ul>
<li><p>maintain history of last two states</p></li>
<li><p>trigram model</p></li>
</ul></li>
</ul>
<ul>
<li><p>Examples:</p>
<ul>
<li><p>Bigram model trained on "The Legend of Sleepy Hollow"</p>
<ul>
<li><p>"But it were grunting in former times of the battle in the quietest places which last was found favor in with snow which he heard in a knot of doors of the fence Ichabod stole forth now came to look behind"</p></li>
</ul></li>
<li><p>Trigram model</p>
<ul>
<li><p>"As Ichabod jogged slowly on his haunches and unskillful rider that he was according to the lot of a snowy night, with what wistful look did he shrink with curdling awe at the mention of the screech owl"</p></li>
</ul></li>
<li><p>Five-gram model</p>
<ul>
<li><p>"About two hundred yards from the tree a small brook crossed the road and ran into a marshy and thickly wooded glen known by the name of the Headless Horseman of Sleepy Hollow"</p></li>
</ul></li>
</ul></li>
<li><p>clearly the quality increases quickly with the 5-gram generation being completely intelligible</p></li>
<li><p>limitations of Markov models</p>
<ul>
<li><p>finite context</p>
<ul>
<li><p>Markov models are constrained by their fixed order, which limits their ability to capture long-term dependencies</p></li>
</ul></li>
<li><p>lack of memory</p>
<ul>
<li><p>do not possess memory of past states or events</p></li>
</ul></li>
<li><p>stationarity</p>
<ul>
<li><p>assume that the data-generating processes remain fixed over time</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>RNNs: Form and Parameters</td>
<td colspan="4"><ul>
<li><p>Recurrent Neural Networks recursively update hidden state to handle varying context sizes</p></li>
<li><p>often context changes, branches, and runs in parallel, with articles near the end of the prompt referencing information presented anywhere in the earlier text up to the very beginning</p></li>
<li><p>the notion of state in the RNN can be expressed:</p></li>
</ul>
<p><span class="math display"><em>h</em><sub><em>t</em></sub> = <em>σ</em>(<em>W</em><sub>1</sub><em>h</em><sub><em>t</em> − 1</sub> + <em>W</em><sub>2</sub><em>x</em><sub><em>t</em></sub> + <em>b</em>)</span></p>
<p><img src="generated_media\DATA785_week07_notes\media\image1.png" style="width:4.82292in;height:2.26181in" /></p>
<p>Gemini 3.5</p>
<p>=</p>
<p>t</p></td>
</tr>
<tr>
<td></td>
<td colspan="4"><p><img src="generated_media\DATA785_week07_notes\media\image2.png" style="width:4.65625in;height:2.32632in" /></p>
<p>Gemini 3.5</p>
<ul>
<li><p>recursively combine new input with old state to handle varying context sizes</p></li>
<li><p><span class="math inline"><em>λ</em></span> is a transformational function to get output form state:</p>
<ul>
<li><p>binary classification</p>
<ul>
<li><p>sigmoid</p></li>
<li><p>if desired output = {+1,1}</p></li>
</ul></li>
<li><p>multi-class classification</p>
<ul>
<li><p>softmax</p></li>
<li><p>if desired output = {1, 2, 3 … K}</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>RNNs in Action</td>
<td colspan="4"><ul>
<li><p>generating sequences using RNNs</p>
<ul>
<li><p>assume we currently have observation <span class="math inline"><em>x</em><sub>1</sub></span> and want to predict <span class="math inline"><em>x</em><sub>2</sub></span></p></li>
<li><p>we compute hidden state <span class="math inline"><em>h</em><sub>1</sub></span> first</p></li>
</ul></li>
</ul>
<p><span class="math display"><em>h</em><sub>1</sub> = <em>σ</em>(<em>W</em><sub>1</sub><em>h</em><sub>0</sub> + <em>W</em><sub>2</sub><em>x</em><sub>1</sub> + <em>b</em>)</span></p>
<ul>
<li><p>then, predict next token <span class="math inline"><em>x̂</em><sub>2</sub></span> by:</p>
<ul>
<li><p>first, computing <span class="math inline"><em>W</em><sub>3</sub><em>h</em><sub>1</sub></span> and applying <span class="math inline"><em>λ</em></span> to get a distribution <span class="math inline"><em>ŷ</em><sub>1</sub></span> (e.g., over a vocabulary)</p></li>
<li><p>then, sampling <span class="math inline"><em>x̂</em><sub>2</sub></span> from the distribution <span class="math inline"><em>ŷ</em><sub>1</sub></span></p></li>
</ul></li>
</ul>
<p><span class="math display"><em>x̂</em><sub>2</sub> ∼ <em>ŷ</em><sub>1</sub> = <em>λ</em>(<em>W</em><sub>3</sub><em>h</em><sub>1</sub>)</span></p>
<ul>
<li><p>an RNNs is a type of NN that has a recurrence structure</p>
<ul>
<li><p>each hidden unit (<span class="math inline"><em>h</em><sub><em>t</em></sub></span>)</p>
<ul>
<li><p>encodes information from previous unit (<span class="math inline"><em>h</em><sub><em>t</em> − 1</sub></span>)</p></li>
<li><p>which in turn encodes information from its previous unit (<span class="math inline"><em>h</em><sub><em>t</em> − 2</sub></span>)</p></li>
<li><p>and so on...</p></li>
</ul></li>
<li><p>can model long range dependencies</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA785_week07_notes\media\image3.png" style="width:4.875in;height:1.73933in" /></p>
<p>Gemini 3.5</p>
<ul>
<li><p>FNNs vs RNNs</p>
<ul>
<li><p>FNNs:</p>
<ul>
<li><p>number of inputs is fixed (fixed context)</p></li>
<li><p>each hidden unit is dependent on all inputs but not on other hidden units</p></li>
</ul></li>
<li><p>RNNs:</p>
<ul>
<li><p>unlimited number of inputs (flexible context and long-range dependencies)</p></li>
<li><p>each hidden unit is dependent only on the previous hidden unit and current input</p></li>
</ul></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA785_week07_notes\media\image4.png" style="width:4.82558in;height:2in" /></p>
<p>Gemini 3.5</p>
<ul>
<li><p>RNNs are Auto-Regressive Models</p>
<ul>
<li><p>an ARM predicts value at time t based on a function of the previous values at times <span class="math inline"><em>t</em> − 1, <em>t</em> − 2,</span> and so on…</p></li>
<li><p>therefore, an RNN-based LM is also called an auto-regressive generation model</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA785_week07_notes\media\image5.png" style="width:4.89583in;height:1.32914in" /></p>
<p>Gemini 3.5</p></td>
</tr>
<tr>
<td colspan="5"></td>
</tr>
</tbody>
</table>
