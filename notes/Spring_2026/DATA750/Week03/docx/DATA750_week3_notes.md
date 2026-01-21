> Markdown version for convenient browsing. Original files:
> - PDF: [DATA750_week3_notes.pdf](../DATA750_week3_notes.pdf)
> - DOCX: [DATA750_week3_notes.docx](DATA750_week3_notes.docx)

---

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 1%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 52%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr>
<th colspan="3">Convolution</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4">Overview</td>
<td colspan="4" style="text-align: right;"><em>Class Meeting : 20 Jan 2026</em></td>
</tr>
<tr>
<td colspan="8"><ul>
<li><p>convolution</p>
<ul>
<li><p>analytical</p></li>
<li><p>discrete</p></li>
<li><p>numerical</p></li>
</ul></li>
<li><p>formulate in terms of convolution kernels</p></li>
<li><p>compute convolutions in one and higher dimension numerically</p></li>
<li><p>Gaussian convolution</p></li>
<li><p>box convolution</p></li>
<li><p>efficiency and benefit of separable kernels</p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Convolution</td>
<td colspan="3" style="text-align: right;">[optional]</td>
</tr>
<tr>
<td colspan="8"><ul>
<li><p>convolution is a mathematical technique used on two functions <span class="math inline"><strong>f</strong></span> and <span class="math inline"><strong>g</strong></span> that produces a third function <span class="math inline"><strong>f</strong> <strong>*</strong> <strong>g</strong></span></p></li>
<li><p><span class="math inline"><strong>f</strong> <strong>*</strong> <strong>g</strong></span> is the integral of the product of the two functions after one is reflected about the y-axis and shifted</p></li>
<li><p>uses an average of local-adjacent values based on kernel size</p></li>
</ul>
<p><a href="https://en.wikipedia.org/wiki/Convolution">https://en.wikipedia.org/wiki/Convolution</a></p></td>
</tr>
<tr>
<td colspan="5">Convolution in 1D</td>
<td colspan="3" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Applications of Convolution</td>
<td colspan="6"><ul>
<li><p><strong>signal processing</strong></p>
<ul>
<li><p><strong>filtering</strong> (noise reduction</p></li>
<li><p>system <strong>modeling</strong></p></li>
<li><p><strong>reverberation</strong> (simulating sound reflections</p></li>
</ul></li>
</ul>
<ul>
<li><p><strong>image processing</strong></p>
<ul>
<li><p><strong>sharpening</strong></p></li>
<li><p>edge <strong>detection</strong></p></li>
<li><p>feature <strong>extraction</strong></p></li>
</ul></li>
<li><p><strong>artificial intelligence</strong></p>
<ul>
<li><p>convolutional <strong>neural</strong> <strong>networks</strong></p></li>
</ul></li>
<li><p><strong>physics</strong> and <strong>engineering</strong></p></li>
</ul>
<p><a href="https://www.fieldbox.ai/seeing-through-computer-vision-convolution-101/">https://www.fieldbox.ai/seeing-through-computer-vision-convolution-101/</a></p></td>
</tr>
<tr>
<td>General Mathematical form</td>
<td colspan="7" style="text-align: center;"><img src="generated_media\DATA750_week3_notes\media\image1.png" style="width:4.87568in;height:0.82303in" /></td>
</tr>
<tr>
<td>Properties</td>
<td colspan="7"><ul>
<li><p><em><strong>f * g = g * f</strong></em></p></li>
<li><p><em><strong>f * (g * f) = (f*g) * h</strong></em></p></li>
<li><p><em><strong>f * (g + h) = (f * g) + (f * h)</strong></em></p></li>
</ul>
<p><a href="https://mathworld.wolfram.com/Convolution.html">https://mathworld.wolfram.com/Convolution.html</a></p></td>
</tr>
<tr>
<td>Discrete Convolution</td>
<td colspan="7" style="text-align: center;"><img src="generated_media\DATA750_week3_notes\media\image2.png" style="width:4.35477in;height:0.70843in" /></td>
</tr>
<tr>
<td>Layering</td>
<td colspan="7"><ul>
<li><p>a <strong>weighted</strong> <strong>sum</strong> of the convolution <strong>kernel</strong></p></li>
<li><p>can <strong>extract</strong> local <strong>features</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Convolution Kernel</td>
<td colspan="7"><ul>
<li><p>the <strong>filter</strong> of a matrix <strong>for</strong> <strong>feature</strong> <strong>extraction</strong></p></li>
<li><p><strong>each</strong> convolution <strong>process</strong> has its own <strong>kernel</strong></p></li>
<li><p><strong>image</strong> <strong>blurring</strong> example: for <strong>each</strong> <strong>pixel</strong> in an <strong>image</strong>, the inner <strong>product</strong> of the <strong>pixel</strong> within the local <strong>window</strong> centered on that pixel and the <strong>kernel</strong> is <strong>calculated</strong></p></li>
<li><p>some <strong>kernel types</strong></p>
<ul>
<li><p><strong>asymmetric</strong></p></li>
<li><p><strong>hat</strong></p></li>
<li><p><strong>box</strong></p></li>
<li><p><strong>exponential decay</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Padding</td>
<td colspan="7"><ul>
<li><p>for when the convolution <strong>range</strong> is <strong>not</strong> <strong>defined</strong> at edges</p></li>
<li><p><em><strong>f</strong></em> is <strong>padded</strong> with reasonable <strong>data</strong> there are <strong>multiple</strong> <strong>tactics</strong> available</p>
<ul>
<li><p><strong>zeros</strong></p></li>
<li><p><strong>mirror-copy</strong></p></li>
<li><p><strong>repeat</strong> closest <strong>value</strong></p></li>
<li><p><strong>trim</strong> the <strong>range</strong> (usually only with <strong>very</strong> <strong>large</strong> <strong>sets</strong>)</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="6">Convolution in 2D</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td>Overview</td>
<td colspan="7"><ul>
<li><p>two-dimensional convolution is mathematically the same as in 1D</p></li>
<li><p>produced 2D integral</p></li>
<li><p>often kernels are separable</p></li>
</ul></td>
</tr>
<tr>
<td>Kernel Separability</td>
<td colspan="7"><ul>
<li><p>a function g(x, y), that can be rewritten as a product such that:</p></li>
</ul>
<p>g( x, y ) = g<sup>x</sup>(x)*g<sup>y</sup>(y)</p>
<ul>
<li><p>the result is two 1D kernels</p></li>
<li><p>by separating the kernel, each dimension can be convoluted individually</p></li>
<li><p>continuous separable</p></li>
</ul>
<p><img src="generated_media\DATA750_week3_notes\media\image3.png" style="width:2.50035in;height:0.41672in" /></p>
<ul>
<li><p>discrete separable</p></li>
</ul>
<p><img src="generated_media\DATA750_week3_notes\media\image4.png" style="width:2.29199in;height:0.48965in" /></p></td>
</tr>
<tr>
<td>Sources</td>
<td colspan="7"><ul>
<li><p><a href="https://mathworld.wolfram.com/Convolution.html">https://mathworld.wolfram.com/Convolution.html</a></p></li>
<li><p><a href="https://evidentscientific.com/en/microscope-resource/tutorials/digital-imaging/processing/convolutionkernels">https://evidentscientific.com/en/microscope-resource/tutorials/digital-imaging/processing/convolutionkernels</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

https://evidentscientific.com/en/microscope-resource/tutorials/digital-imaging/processing/convolutionkernels

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 28%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Live Session Notes</th>
<th style="text-align: right;">30 Oct 2025</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
<tr>
<td>*</td>
<td colspan="2"><ul>
<li></li>
<li></li>
<li></li>
</ul></td>
</tr>
</tbody>
</table>
