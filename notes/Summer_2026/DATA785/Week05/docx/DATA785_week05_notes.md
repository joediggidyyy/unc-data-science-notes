> Markdown version for convenient browsing. Original files:
> - PDF: [DATA785_week05_notes.pdf](../DATA785_week05_notes.pdf)
> - DOCX: [DATA785_week05_notes.docx](DATA785_week05_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 15%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Convolutional Neural Networks</th>
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
<li><p>design and implement Convolutional Neural Networks (CNNs)</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td>Neural Networks for Images</td>
<td colspan="4"><ul>
<li><p>complexity issue with processing images with a NN</p>
<ul>
<li><p>for a 1024 x 1024 image and a NN with 100 neuron input layer: 1024 x 3 (RGB channels) x 100 <span class="math inline">≈</span> 300 million parameters</p></li>
</ul></li>
<li><p>locality</p>
<ul>
<li><p>many useful features are local</p></li>
<li><p>can be computed from small patches of the image</p></li>
<li><p>ex: is Mr. Poopybutthole in this picture?</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA785_week05_notes\media\image1.png" style="width:4.46736in;height:2.77921in" /></p>
<ul>
<li><p>you would not generally process the image all at once, but you would scan zone by zone classifying each edged object</p></li>
</ul>
<p><img src="generated_media\DATA785_week05_notes\media\image1.png" style="width:4.16924in;height:2.59375in" /></p>
<ul>
<li><p>until you identify the target object or run out of searchable objects / zones</p></li>
</ul>
<ul>
<li><p>translation invariance</p>
<ul>
<li><p>the exact coordinates of the feature in the image is irrelevant</p></li>
</ul></li>
<li><p>solution:</p>
<ul>
<li><p><img src="generated_media\DATA785_week05_notes\media\image2.png" style="width:3.83333in;height:2.38437in" />look at 3 x 3 patches of the image</p></li>
<li><p>we still get a different output at each patch location</p></li>
<li><p>as abstract example: assuming each patch is 3 x 3</p>
<ul>
<li><p>full image: 27 x 18 x 3 x 100 <span class="math inline">≈</span> 146,000</p></li>
<li><p>single patch: 3 x 3 x 3 x 100 <span class="math inline">≈</span> 3,000</p></li>
</ul></li>
<li><p>the features extracted from each patch is then combined to construct a feature map for the full image</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Convolutions in Image Processing</td>
<td colspan="4"><ul>
<li><p>convolution</p>
<ul>
<li><p>achieved through a “sliding dot product”</p></li>
<li><p>defined by weight matrix <span class="math inline"><em>W</em><sub><em>F</em></sub></span> (filter)</p></li>
<li><p>optionally an additive bias term</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>CNNs</td>
<td colspan="4"><ul>
<li><p>using the sliding window to calculate the dot product value for each pixel</p>
<ul>
<li><p>the representation is still large (e.g., 1024 x 1024 x <span class="math inline"><em>n</em><sub><em>F</em></sub></span>)</p></li>
<li><p>to compress, “pool” features form non-overlapping segments</p></li>
<li><p>example: take a <strong>max</strong> or <strong>average</strong> over each 2 x 2 region for each channel</p>
<ul>
<li><p>no learnable parameters here</p></li>
<li><p>introduces spatial invariance</p></li>
<li><p>produces: 512 x 512 x <span class="math inline"><em>n</em><sub><em>F</em></sub></span></p></li>
</ul></li>
</ul></li>
<li><p>example CNN</p></li>
</ul>
<p><img src="generated_media\DATA785_week05_notes\media\image3.png" style="width:4.74892in;height:2.29097in" /></p></td>
</tr>
<tr>
<td>Paddings and Edges</td>
<td colspan="4"><ul>
<li><p>stride</p>
<ul>
<li><p>the number of spaces the sliding-window travels in a single sliding action</p></li>
<li><p>suppose an image is 7 x 7 and has a sliding window with no padding</p>
<ul>
<li><p>a stride of one produces: 5 x 5</p></li>
<li><p>a stride of two produces: 3 x 3</p></li>
<li><p>we cannot apply a stride of 3 or more to this size matrix</p></li>
</ul></li>
</ul></li>
<li><p>padding</p>
<ul>
<li><p>add ‘0 pad border’ around the image</p></li>
<li><p>this ensures that the output is the same size as the input (for stride = 1)</p></li>
</ul></li>
<li><p>output size formula</p></li>
</ul>
<p><span class="math display">$$Output\ Size = \frac{X_{side} + 2P - f}{stride} + 1$$</span></p>
<ul>
<li><p>pooling layer summary</p>
<ul>
<li><p>input</p>
<ul>
<li><p>tensor with dimensions <span class="math inline"><em>W</em><sub>1</sub> × <em>H</em><sub>1</sub> × <em>C</em></span></p></li>
<li><p>number of filters <span class="math inline"><em>n</em><sub><em>F</em></sub></span></p></li>
<li><p>length of filter: <span class="math inline"><em>F</em></span></p></li>
<li><p>length of strides: <span class="math inline"><em>S</em></span></p></li>
<li><p>zero padding: <span class="math inline"><em>P</em></span></p></li>
</ul></li>
<li><p>output</p>
<ul>
<li><p>tensor with dimensions <span class="math inline"><em>W</em><sub>2</sub> × <em>H</em><sub>2</sub> × <em>n</em><sub><em>F</em></sub></span>,</p></li>
</ul></li>
</ul></li>
</ul>
<blockquote>
<p>where, <span class="math inline">$W_{2} = \frac{W_{1} - F + 2P}{S} + 1$</span> and <span class="math inline">$H_{2} = \frac{H_{1} - F + 2P}{S + 1}$</span></p>
</blockquote>
<ul>
<li><p>number of learnable parameters:</p>
<ul>
<li><p><span class="math inline"><em>n</em><sub><em>F</em></sub> × <em>F</em> × <em>F</em> × <em>C</em></span> weights and <span class="math inline"><em>n</em><sub><em>F</em></sub></span> bias terms</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Examples of CNN Architectures</td>
<td colspan="4"><ul>
<li><p>LeNet for Handwritten Digit Recognition (1988: Yann LeCun!)</p>
<ul>
<li><p>well-known 30+ year old handwriting reading tool</p></li>
</ul></li>
<li><p>AlexNet (2012)</p>
<ul>
<li><p>revolutionary model in terms of performance (16.4% error rate)</p></li>
<li><p>one of the real first deep learning successes</p></li>
<li><p>classic deep CNN architecture</p></li>
<li><p>first use of ReLU activations</p></li>
<li><p>trained with L2 regularization and dropout</p></li>
</ul></li>
<li><p>VGG Net (2014)</p>
<ul>
<li><p>large increase in depth over previous models</p></li>
<li><p>homogeneous stacks of smaller filters rather than layer-specific hyper-parameters</p></li>
<li><p>3 x 3 convolution filters with stride 1, padding 1</p></li>
<li><p>2 x 2 pooling filters with stride 2</p></li>
</ul></li>
<li><p>ResNet (2015)</p>
<ul>
<li><p>152 layers</p></li>
<li><p>no giant fully connected networks</p></li>
<li><p>all positions averaged (single layer)</p></li>
<li><p>skip and residual connections to provide better gradient optimization (enables training of really deep models)</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="5"></td>
</tr>
</tbody>
</table>
