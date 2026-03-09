---
generated_at_utc: 2026-03-09T05:35:10+00:00
generated_from: notes/Spring_2026/DATA780/Week07/docx/DATA780_week07_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week07_notes.pdf](../DATA780_week07_notes.pdf)
> - DOCX: [DATA780_week07_notes.docx](DATA780_week07_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Neural Networks 2</th>
<th></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td style="text-align: right;"><em>23 Feb 2026</em></td>
</tr>
<tr>
<td>Terms</td>
<td colspan="3"><ul>
<li><p><strong>logits</strong></p>
<ul>
<li><p>the <a href="https://en.wikipedia.org/wiki/Quantile_function">quantile function</a> <strong>associated</strong> with the <strong>standard</strong> <a href="https://en.wikipedia.org/wiki/Logistic_distribution"><strong>logistic</strong> distribution</a></p></li>
</ul></li>
<li><p><strong>quantile</strong> function</p>
<ul>
<li><p> a <a href="https://en.wikipedia.org/wiki/Probability_distribution">probability <strong>distribution</strong></a><strong>'s</strong> quantile function is the <a href="https://en.wikipedia.org/wiki/Inverse_function"><strong>inverse</strong></a> of its <a href="https://en.wikipedia.org/wiki/Cumulative_distribution_function"><strong>cumulative</strong> <strong>distribution</strong> function</a></p></li>
</ul></li>
<li><p><strong>softmax</strong></p>
<ul>
<li><p>converts a <a href="https://en.wikipedia.org/wiki/Tuple"><strong>tuple</strong></a> of <span class="math inline"><strong>K</strong></span> <strong>real</strong> numbers into a <a href="https://en.wikipedia.org/wiki/Probability_distribution"><strong>probability</strong> <strong>distribution</strong></a> over <span class="math inline"><strong>K</strong></span> <strong>possible</strong> outcomes</p></li>
</ul></li>
<li><p><strong>attention</strong></p>
<ul>
<li><p>a method that <strong>determines</strong> the <strong>importance</strong> of each <strong>component</strong> in a sequence <strong>relative</strong> to the <strong>other</strong> <strong>components</strong> in that sequence</p></li>
</ul></li>
<li><p><strong>spatio</strong>-<strong>temporal</strong> data</p>
<ul>
<li><p><strong>data</strong> that shows both <strong>spatial</strong> and <strong>temporal</strong> <strong>patterning</strong></p></li>
</ul></li>
<li><p><strong>convolutional</strong> neural networks</p>
<ul>
<li><p>a type of <a href="https://en.wikipedia.org/wiki/Feedforward_neural_network"><strong>feedforward</strong> neural network</a> that <strong>learns</strong> <a href="https://en.wikipedia.org/wiki/Feature_engineering"><strong>features</strong></a> via filter (or <a href="https://en.wikipedia.org/wiki/Kernel_(image_processing)"><strong>kernel</strong></a>) <strong>optimization</strong></p></li>
</ul></li>
<li><p>multi-axes <strong>tensors</strong></p>
<ul>
<li><p>a <strong>multi</strong>-<strong>linear</strong> <strong>tensor</strong> is an <a href="https://en.wikipedia.org/wiki/Mathematical_object">algebraic <strong>object</strong></a> that <strong>describes</strong> a <a href="https://en.wikipedia.org/wiki/Multilinear_map">multilinear</a> <strong>relationship</strong> between sets of <a href="https://en.wikipedia.org/wiki/Algebraic_structure">algebraic <strong>objects</strong></a> associated with a <a href="https://en.wikipedia.org/wiki/Vector_space"><strong>vector</strong> <strong>space</strong></a></p></li>
</ul></li>
<li><p><strong>flat</strong> vectors</p>
<ul>
<li><p>a <a href="https://en.wikipedia.org/wiki/Vector_bundle"><strong>vector</strong> bundle</a> that is endowed with a <a href="https://en.wikipedia.org/wiki/Connection_(vector_bundle)"><strong>linear</strong> <strong>connection</strong></a> with <strong>vanishing</strong> <a href="https://en.wikipedia.org/wiki/Curvature"><strong>curvature</strong></a> (i.e. a <a href="https://en.wikipedia.org/wiki/Flat_connection"><strong>flat</strong> connection</a>)</p></li>
</ul></li>
<li><p><strong>recurrent</strong> neural networks</p>
<ul>
<li><p><strong>RNNs</strong> are designed for <strong>processing</strong> <strong>sequential</strong> data, such as <strong>text</strong>, <strong>speech</strong>, and <a href="https://en.wikipedia.org/wiki/Time_series"><strong>time</strong> <strong>series</strong></a> where the <strong>order</strong> of elements is <strong>important</strong></p></li>
</ul></li>
</ul>
<p><a href="https://en.wikipedia.org/">https://en.wikipedia.org/</a></p></td>
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
<th colspan="2">Readings</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><ol type="A">
<li><p>Convolutional Networks (pp. 326 through Section 9.3)</p></li>
</ol>
<ul>
<li><p><a href="https://www.deeplearningbook.org/contents/convnets.html">https://www.deeplearningbook.org/contents/convnets.html</a></p></li>
</ul>
<ol start="2" type="A">
<li><p>Sequence Modeling: Recurrent and Recursive Nets (Section 2.5 pp. 120-127)</p></li>
</ol>
<ul>
<li><p><a href="https://www.deeplearningbook.org/contents/rnn.html">https://www.deeplearningbook.org/contents/rnn.html</a></p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Convolutional Networks</td>
</tr>
<tr>
<td><p>Convolutional Networks</p>
<p>(CNNs)</p></td>
<td colspan="2"><ul>
<li><p>defined as a type of <strong>neural</strong> <strong>network</strong> with a <strong>grid</strong> structure, like <strong>images</strong> or <strong>time</strong> <strong>series</strong></p></li>
<li><p><strong>inspired</strong> by <strong>biological</strong> systems</p></li>
<li><p>foundational for <strong>image</strong> and <strong>pattern</strong> <strong>recognition</strong> tasks</p></li>
</ul></td>
</tr>
<tr>
<td>Convolutional Operation</td>
<td colspan="2"><ul>
<li><p>a mathematical way to <strong>combine</strong> input <strong>data</strong> with a small <strong>set</strong> of learned <strong>weights</strong> (a <strong>kernel</strong> or <strong>filter</strong>) to extract <strong>features</strong></p></li>
<li><p>the <strong>kernel</strong> <strong>slides</strong> across the <strong>input</strong> grid and produces <strong>feature maps</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Key Properties of Convolution</td>
<td colspan="2"><ul>
<li><p><strong>sparse</strong> interactions</p>
<ul>
<li><p><strong>depends</strong> on a small <strong>local</strong> <strong>region</strong> of the input</p></li>
<li><p><strong>limits</strong> the number of <strong>parameters</strong> dramatically <strong>compared</strong> to <strong>fully</strong> connected layers</p></li>
</ul></li>
<li><p>parameter <strong>sharing</strong></p>
<ul>
<li><p>the <strong>same</strong> kernel <strong>weights</strong> are <strong>reused</strong> across <strong>different</strong> input positions <strong>reducing</strong> the number of <strong>parameters</strong></p></li>
<li><p><strong>enables</strong> <strong>learning</strong> patterns that <strong>repeat</strong> across the <strong>data</strong></p></li>
</ul></li>
<li><p><strong>equivalence</strong> to <strong>translation</strong></p>
<ul>
<li><p>handles <strong>patterns</strong> that <strong>shift</strong> in space</p></li>
<li><p>if the <strong>input</strong> <strong>shifts</strong>, the <strong>output</strong> <strong>shifts</strong> in the <strong>same</strong> way</p></li>
<li><p>helps <strong>detect</strong> <strong>patterns</strong> anywhere in the <strong>input</strong></p></li>
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
<th>Pooling</th>
<th><ul>
<li><p>an operation applied after convolution to reduce the spatial size of feature maps</p></li>
<li><p>makes the network less sensitive to small shifts in the input and reduces computation</p></li>
<li><p>the most common form is max pooling</p>
<ul>
<li><p>picks the largest value from a small region</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Sequence Modeling: Recurrent and Recursive Nets</td>
</tr>
<tr>
<td>Sequence Modeling</td>
<td><ul>
<li><p>a <strong>sequence</strong> is a list of <strong>vectors</strong> <span class="math inline"><strong>x</strong><sup>(<strong>1</strong>)</sup><strong>,</strong> <strong>x</strong><sup>(<strong>2</strong>)</sup><strong>,</strong> <strong>x</strong><sup>(<strong>3</strong>)</sup><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>x</strong><sup>(<strong>τ</strong>)</sup></span>, where <strong>each</strong> <strong>element</strong> comes <strong>one</strong> <strong>after</strong> the <strong>other</strong> in <strong>time</strong> or <strong>order</strong></p></li>
<li><p><strong>sequence</strong> <strong>modeling</strong> is about <strong>processing</strong> data where <strong>order</strong> <strong>matters</strong> (like <strong>text</strong>, <strong>audio</strong>, time <strong>series</strong>)</p></li>
</ul></td>
</tr>
<tr>
<td><p>Recurrent Neural Networks</p>
<p>(RNNs)</p></td>
<td><ul>
<li><p><strong>process</strong> elements <strong>one at a time</strong></p></li>
<li><p>at <strong>each</strong> <strong>step</strong> the network <strong>updates</strong>:</p>
<ul>
<li><p>a <strong>hidden</strong> state <span class="math inline"><strong>h</strong><sup>(<strong>t</strong>)</sup></span>, which is its <strong>memory</strong>.</p></li>
<li><p>the hidden <strong>state</strong> <strong>combines</strong> the <strong>current</strong> input <span class="math inline"><strong>x</strong><sup>(<strong>t</strong>)</sup></span>and the <strong>previous</strong> state <span class="math inline"><strong>h</strong><sup><strong>t</strong><strong>−</strong><strong>1</strong></sup></span></p></li>
</ul></li>
<li><p><strong>shared</strong> <strong>processing</strong> lets the network <strong>handle</strong> sequences of <strong>variable</strong> <strong>length</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Why RNNs</td>
<td><ul>
<li><p><strong>traditional</strong> neural networks (like <strong>CNNs</strong> or fully <strong>connected</strong> nets) process <strong>fixed</strong>-<strong>length</strong> inputs</p></li>
<li><p>many tasks <strong>require</strong> understanding <strong>order</strong> and <strong>history</strong></p></li>
</ul>
<p><strong>h(t) = f(h(t−1), x(t))</strong></p>
<p><strong>o(t) = g(h(t))</strong></p>
<p>Where:</p>
<ul>
<li><p><strong>h(t)</strong>: current memory / hidden state</p></li>
<li><p><span class="math inline"><strong>x</strong><strong>(</strong><strong>t</strong><strong>)</strong></span>: current input</p></li>
<li><p><span class="math inline"><strong>o</strong><strong>(</strong><strong>t</strong><strong>)</strong></span>: output at time <span class="math inline"><strong>t</strong></span></p></li>
<li><p><span class="math inline"><strong>f</strong><strong>,</strong> <strong>g</strong></span>: learned functions</p></li>
</ul>
<p>output</p>
<p>new state</p></td>
</tr>
<tr>
<td>Unfolding the RNN</td>
<td><ul>
<li><p>to understand <strong>training</strong> and <strong>computation</strong>, we “<strong>unfold</strong>” the RNN <strong>through</strong> <strong>time</strong></p>
<ul>
<li><p>view the <strong>network</strong> at each <strong>step</strong> as a <strong>separate</strong> layer <strong>connected</strong> to the <strong>next</strong></p></li>
</ul></li>
<li><p>makes <strong>training</strong> <strong>easier</strong> to reason about</p></li>
</ul></td>
</tr>
<tr>
<td>Parameter Sharing in RNNs</td>
<td><ul>
<li><p>same <strong>weights</strong> are used at <strong>every</strong> time <strong>step</strong></p></li>
<li><p><strong>reduces</strong> the number of <strong>parameters</strong></p></li>
<li><p><strong>allows</strong> the network to <strong>generalize</strong> sequences of <strong>different</strong> <strong>length</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Types of RNN Processing</td>
<td><ul>
<li><p><strong>outputs</strong> at each time <strong>step</strong></p>
<ul>
<li><p><strong>predicting</strong> the word in a <strong>sequence</strong></p></li>
<li><p><strong>predicts</strong> something every step as it <strong>processes</strong> input</p></li>
</ul></li>
<li><p><strong>reads</strong> <strong>entire</strong> sequence then <strong>outputs</strong> <strong>once</strong></p>
<ul>
<li><p><strong>classifying</strong> a <strong>sentence</strong> after ingesting it <strong>fully</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Teacher Forcing</td>
<td><ul>
<li><p>in training, <strong>RNNs</strong> sometimes <strong>use</strong> the true <strong>output</strong> from the <strong>training</strong> data as <strong>input</strong> for the <strong>next</strong> step</p></li>
<li><p>this <strong>helps</strong> <strong>learning</strong> but it is <strong>different</strong> from how the network <strong>runs</strong> in <strong>practice</strong></p></li>
</ul></td>
</tr>
<tr>
<td>RNNs as Probabilistic Models</td>
<td><ul>
<li><p><strong>RNNs</strong> can be viewed as <strong>models</strong> that <strong>define</strong> a probability <strong>distribution</strong> over <strong>sequences</strong></p></li>
<li><p>model how <strong>likely</strong> a next <strong>element</strong> <span class="math inline"><strong>y</strong><sup>(<strong>t</strong>)</sup></span>is given <strong>previous</strong> inputs</p></li>
</ul></td>
</tr>
<tr>
<td>Conditional RNNs</td>
<td><ul>
<li><p><strong>RNNs</strong> can use <strong>another</strong> <strong>sequence</strong> as context to <strong>predict</strong> a <strong>target</strong> sequence</p></li>
<li><p>can <strong>generate</strong> an <strong>output</strong> sequence of the <strong>same</strong> <strong>length</strong> as the <strong>input</strong> sequence</p></li>
<li><p>ex: in <strong>image</strong> <strong>captioning</strong>, an image is input, and the <strong>RNN</strong> <strong>generates</strong> <strong>words</strong> about that image</p></li>
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
<th colspan="2">Async Materials</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">How to Speak the Neural Network Lingo</td>
</tr>
<tr>
<td>Strategies of Defining Neural Networks</td>
<td colspan="2"><ul>
<li><p>satisfy constraints with differential activations</p></li>
<li><p>make differential versions of common or useful operations (i.e. lookups) so networks can make use of them in a learnable fashion</p></li>
</ul></td>
</tr>
<tr>
<td>Constraints</td>
<td colspan="2"><ul>
<li><p>examples</p></li>
<li><p>all features must be between a particular range</p></li>
<li><p>all features must be non-negative</p></li>
<li><p>constrained features must be differentiable</p>
<ul>
<li><p>if constraint function is not differentiable, the chain rule cannot be applied to compute gradients</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Activation Base</td>
<td colspan="2"><ul>
<li><p>a non-linear mathematical operation is applied to the output of each node</p></li>
<li><p>the fundamental driver for learning complex patterns</p></li>
<li><p>core components</p>
<ul>
<li><p>introduction of non-linearity into the system</p></li>
<li><p>a firing decision determines if a neuronal output is relevant</p></li>
<li><p>gradient flow ensures that gradients remain large during backpropagation, allowing the model to train effectively</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Common Activation Functions</td>
<td colspan="2"><ul>
<li><p>SoftMax</p>
<ul>
<li><p>a mathematical function used in artificial intelligence to transform logits</p></li>
<li><p>each value is between 0 and 1</p></li>
<li><p>the sum of all values equals exactly 1</p></li>
</ul></li>
<li><p>one-hot vectors</p>
<ul>
<li><p>represents categorical data as binary vectors where only one element is hot, and the rest are cold</p></li>
</ul></li>
<li><p>negative log likelihood</p>
<ul>
<li><p>a loss function used to train classification models by minimizing the negative logarithm of the predicted probability</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Additional Activation Functions</td>
<td colspan="2"><ul>
<li><p>rectified linear unit (ReLU)</p>
<ul>
<li><p>returns <span class="math inline"><strong>i</strong><strong>n</strong><strong>p</strong><strong>u</strong><strong>t</strong></span> if positive, <span class="math inline"><strong>0</strong></span> if not</p></li>
</ul></li>
<li><p>sigmoid/logistic</p>
<ul>
<li><p>input values to a range between 0 and 1</p></li>
<li><p>frequently used in the output layer for binary classification</p></li>
</ul></li>
<li><p>hyperbolic tangent (tanh)</p>
<ul>
<li><p>maps inputs to a range between -1 and 1</p></li>
</ul></li>
<li><p>Leaky ReLU</p></li>
</ul>
<p>a variant of ReLU that allows a small negative value, helping to prevent "dying neurons"</p></td>
</tr>
<tr>
<td>SoftMax for Attention</td>
<td colspan="2"><ul>
<li><p>computes a probability distribution from raw, unnormalized attention scores ensuring they sum to 1</p></li>
<li><p>the resultant normalization allows the model to focus on relevant tokens (high values) and ignore other (low values)</p></li>
</ul>
<p><strong>keys</strong></p>
<p><strong>value vectors</strong></p>
<p><span class="math display">$$\sum_{j = 1}^{m}{\frac{\exp{sim(\overrightarrow{\phi(x)}},\ {\overrightarrow{\kappa}}^{(j)})}{{\sum_{c = 1}^{m}\exp}{sim(\overrightarrow{\phi(x)}},\ {\overrightarrow{\kappa}}^{(j)})}{\overrightarrow{v}}^{(j)}}$$</span></p></td>
</tr>
<tr>
<td colspan="3">Convolutional Neural Networks</td>
</tr>
<tr>
<td>Properties</td>
<td colspan="2"><ul>
<li><p><img src="generated_media\DATA780_week07_notes\media\image1.png" style="width:3.20246in;height:1.80208in" />low-level features are local</p></li>
<li><p>features are translational invariant</p></li>
<li><p>high-level features are composed of low-level features</p></li>
</ul>
<p>ChatGPT 5.2</p>
<ul>
<li><p><img src="generated_media\DATA780_week07_notes\media\image2.png" style="width:3.1875in;height:1.44444in" />modeled after biological analog</p></li>
</ul>
<p><strong>typical CNN</strong></p></td>
</tr>
</tbody>
</table>
