---
generated_at_utc: 2026-02-11T05:13:43+00:00
generated_from: notes/Spring_2026/DATA750/Week06/docx/DATA750_week06_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA750_week06_notes.pdf](../DATA750_week06_notes.pdf)
> - DOCX: [DATA750_week06_notes.docx](DATA750_week06_notes.docx)

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
<th colspan="2">Location Approximation</th>
<th></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td style="text-align: right;"><em>10 Feb 2026</em></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>how to extend linear least squares to multivariable and multidimensional fits</p></li>
<li><p>how to use a local least squares fit to create LOESS fits to come up with a non-parametrized least squares approximation</p></li>
<li><p>how to interpolate data in higher dimensions onto a uniform grid for analysis and visualization</p></li>
<li><p>how to compute eigenvalues and eigenvectors and diagonalize matrices using numerical libraries. Discuss the power method to find the largest eigenvalue</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">LOESS: Locally estimated scatterplot smoothing</td>
</tr>
<tr>
<td colspan="4">Multiple Variables</td>
</tr>
<tr>
<td>Multivariable Fit</td>
<td colspan="3"><ul>
<li><p>so far <strong>fits</strong> have been of the <strong>form</strong></p></li>
</ul>
<p><span class="math display"><strong>y</strong><sub><strong>i</strong></sub> = <strong>f</strong><sub><strong>p</strong></sub>(<strong>x</strong><sub><strong>i</strong></sub>)</span></p>
<ul>
<li><p>where <strong>(x, y)</strong> is the <strong>input</strong> <strong>data</strong> and <strong>p</strong> is a <strong>vector</strong> of <strong>parameters</strong>.</p></li>
</ul>
<p><span class="math display"><strong>y</strong><sub><strong>i</strong></sub> ∈ <strong>R</strong>,  <strong>x</strong><sub><strong>i</strong></sub> ∈ <strong>R</strong>,  <strong>p</strong> ∈ <strong>R</strong><sup><strong>r</strong></sup></span></p>
<ul>
<li><p>the functional <strong>form</strong> has been a <strong>function</strong> of <strong>x only</strong></p></li>
</ul>
<p><span class="math display"><strong>f</strong><sub><strong>p</strong></sub>(<strong>x</strong>) = <strong>a</strong> + <strong>b</strong><strong>x</strong></span></p>
<p><span class="math display"><strong>p</strong> = (<strong>a</strong>, <strong>b</strong>)</span></p>
<p><span class="math display"><strong>f</strong><sub><strong>p</strong></sub>(<strong>x</strong>) = <strong>a</strong> + <strong>b</strong><strong>x</strong> + <strong>c</strong><strong>x</strong><sup><strong>2</strong></sup></span></p>
<p><span class="math display"><strong>p</strong> = (<strong>a</strong>, <strong>b</strong>, <strong>c</strong>)</span></p>
<ul>
<li><p><strong>multi</strong>-<strong>variable</strong> functions are <strong>fitting</strong> functions of the form</p></li>
</ul>
<p><span class="math display"><strong>z</strong> = <strong>f</strong><sub><strong>p</strong></sub>(<strong>x</strong>, <strong>y</strong>) = <strong>a</strong> + <strong>b</strong><strong>x</strong> + <strong>c</strong><strong>y</strong></span></p></td>
</tr>
<tr>
<td>Formulation</td>
<td colspan="3" style="text-align: center;"><p><img src="generated_media\DATA750_week06_notes\media\image1.png" style="width:2.68575in;height:2.72334in" /></p>
<p>ChatGPT 5.2 1</p>
<ul>
<li><p>linear model</p></li>
</ul>
<p><span class="math display">Cost = <strong>b</strong> + <strong>a</strong><sub><strong>1</strong></sub> Cattle + <strong>a</strong><sub><strong>2</strong></sub> Calves + <strong>a</strong><sub><strong>3</strong></sub> Hogs + <strong>a</strong><sub><strong>4</strong></sub> Sheep</span></p>
<ul>
<li><p>in terms of a vector input with five parameters</p></li>
</ul>
<p><span class="math display"><strong>f</strong>(<strong>x</strong>) = <strong>b</strong> + <strong>a</strong><sub><strong>1</strong></sub><strong>x</strong><sub><strong>1</strong></sub> + <strong>a</strong><sub><strong>2</strong></sub><strong>x</strong><sub><strong>2</strong></sub> + <strong>a</strong><sub><strong>3</strong></sub><strong>x</strong><sub><strong>3</strong></sub> + <strong>a</strong><sub><strong>4</strong></sub><strong>x</strong><sub><strong>4</strong></sub></span></p>
<ul>
<li><p>handled the same way as if you had a polynomial fit</p></li>
</ul>
<p><span class="math display"><strong>f</strong>(<strong>x</strong>) = <strong>b</strong> + <strong>a</strong><sub><strong>1</strong></sub><strong>x</strong><sup><strong>1</strong></sup> + <strong>a</strong><sub><strong>2</strong></sub><strong>x</strong><sup><strong>2</strong></sup> + <strong>a</strong><sub><strong>3</strong></sub><strong>x</strong><sup><strong>3</strong></sup> + <strong>a</strong><sub><strong>4</strong></sub><strong>x</strong><sup><strong>4</strong></sup></span></p></td>
</tr>
<tr>
<td>Julia</td>
<td colspan="3"><p><strong>julia&gt; D</strong></p>
<p><strong>19×5 Matrix{Float64}:</strong></p>
<p><strong>3.437 5.791 3.268 10.649 27.698</strong></p>
<p><strong>12.801 4.558 5.751 14.375 57.634</strong></p>
<p><strong>6.136 6.223 3.175 2.811 47.172</strong></p>
<p><strong>11.685 3.212 0.639 0.694 49.295</strong></p>
<p><strong>5.733 3.222 0.534 2.052 24.115</strong></p>
<p><strong>3.021 4.348 0.839 2.356 33.612</strong></p>
<p><strong>1.689 0.634 0.318 2.209 9.512</strong></p>
<p><strong>2.339 1.895 0.610 0.605 14.755</strong></p>
<p><strong>1.025 0.834 0.734 2.825 10.57</strong></p>
<p><strong>2.936 1.419 0.331 0.231 15.394</strong></p>
<p><strong>5.049 4.195 1.589 1.957 27.843</strong></p>
<p><strong>1.693 3.602 0.837 1.582 17.717</strong></p>
<p><strong>1.187 2.679 0.459 18.837 20.253</strong></p>
<p><strong>9.733 3.951 3.78 0.524 37.465</strong></p>
<p><strong>14.325 4.3 10.781 36.863 101.334</strong></p>
<p><strong>7.737 9.043 1.394 1.524 47.427</strong></p>
<p><strong>7.538 4.538 2.565 5.109 45.944</strong></p>
<p><strong>9.211 4.994 3.081 3.681 45.945</strong></p>
<p><strong>8.697 3.005 1.378 3.138 48.494</strong></p>
<p><strong>julia&gt; A = [ones(19,1) D[:,1:4]];</strong></p>
<p>Here, <strong>A</strong> is the <strong>design</strong> <strong>matrix</strong> with a <strong>bias</strong> <strong>column</strong> and <strong>four</strong> <strong>predictors</strong>,</p>
<p><strong>p</strong> is the <strong>response</strong> <strong>vector</strong>, and <strong>c</strong> contains the <strong>least</strong>-<strong>squares</strong> regression <strong>coefficients</strong>.</p>
<p><strong>julia&gt; p = D[:,5];</strong></p>
<p><strong>julia&gt; c = A \ p</strong></p>
<p><strong>5-element Vector{Float64}:</strong></p>
<p><strong>2.28842457684378</strong></p>
<p><strong>3.215524802749412</strong></p>
<p><strong>1.6131476138283969</strong></p>
<p><strong>0.8148494909933895</strong></p>
<p><strong>0.8025786215025017</strong></p></td>
</tr>
<tr>
<td>Residual</td>
<td colspan="3"><ul>
<li><p><strong>residual</strong> is <strong>computed</strong> the <strong>same</strong> way</p></li>
</ul>
<p><span class="math display"><strong>y</strong> <strong>≈</strong><strong>A</strong><strong>c</strong>  <strong>⇒</strong>  <strong>r</strong> <strong>=</strong> <strong>y</strong> <strong>–</strong> <strong>A</strong><strong>c</strong></span></p>
<ul>
<li><p>input <strong>data</strong> is <strong>four</strong> <strong>dimensional</strong> but can be <strong>projected</strong> onto <strong>one</strong> <strong>axis</strong> at a time <strong>for</strong> <strong>display</strong> purposes</p></li>
<li><p><strong>dark</strong> <strong>points</strong> are data, <strong>white</strong> <strong>fit</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week06_notes\media\image2.png" style="width:3.3494in;height:1.6285in" /></p>
<p>ChatGPT 5.2 2</p></td>
</tr>
<tr>
<td>Spatial</td>
<td colspan="3"><ul>
<li><p><strong>values</strong> given in <strong>space</strong>, <strong>fit</strong> with</p></li>
</ul>
<p><span class="math display"><strong>z</strong>(<strong>x</strong><strong>,</strong> <strong>y</strong>)<strong>=</strong><strong>a</strong><sub><strong>0</strong></sub><strong>+</strong><strong>b</strong><sub><strong>1</strong></sub><strong>x</strong><strong>+</strong><strong>b</strong><sub><strong>2</strong></sub><strong>y</strong><strong>+</strong><strong>c</strong><sub><strong>1</strong></sub><strong>x</strong><sup><strong>2</strong></sup><strong>+</strong><strong>c</strong><sub><strong>2</strong></sub><strong>x</strong><strong>y</strong><strong>+</strong><strong>c</strong><sub><strong>3</strong></sub><strong>y</strong><sup><strong>2</strong></sup></span></p>
<ul>
<li><p><strong>test</strong> on data with <strong>known</strong> <strong>coefficients</strong> and <strong>added</strong> <strong>noise</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week06_notes\media\image3.png" style="width:3.29669in;height:2.43045in" /></p>
<p>ChatGPT 5.2 3</p>
<p>Here, <strong>A</strong> is the <strong>quadratic</strong> design <strong>matrix</strong> <strong>constructed</strong> from <strong>x</strong> and <strong>y</strong>,</p>
<p>and the <strong>vector</strong> returned by <strong>A \ val</strong> <strong>contains</strong> the <strong>least</strong>-<strong>squares</strong> <strong>estimates</strong></p>
<p>of the <strong>coefficients</strong> for the <strong>quadratic</strong> <strong>surface</strong> model.</p></td>
</tr>
<tr>
<td>Julia</td>
<td colspan="3"><p><strong>julia&gt; D</strong></p>
<p><strong>100×3 Matrix{Float64}:</strong></p>
<p><strong>0.798487 0.692338 -6.78094</strong></p>
<p><strong>-0.388154 -0.325195 -0.200116</strong></p>
<p><strong>0.780487 0.693793 2.52178</strong></p>
<p><strong>0.305096 -0.99705 6.87936</strong></p>
<p><strong>⋮</strong></p>
<p><strong>-0.869882 0.406619 1.99625</strong></p>
<p><strong>0.589563 0.109922 2.85972</strong></p>
<p><strong>0.22768 0.474297 3.69185</strong></p>
<p><strong>julia&gt; X = D[:,1]; y = D[:,2]; val = D[:,3];</strong></p>
<p><strong>julia&gt; A = [ones(size(X)) x y x.^2 y.^2];</strong></p>
<p><strong>julia&gt; A \ val</strong></p>
<p><strong>6-element Vector{Float64}:</strong></p>
<p><strong>-1.0624840106609321</strong></p>
<p><strong>2.072135382571392</strong></p>
<p><strong>3.045593968296301</strong></p>
<p><strong>0.502595092034594</strong></p>
<p><strong>1.885286192068896</strong></p>
<p><strong>0.992137812166206</strong></p></td>
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
<th colspan="2">Local Approximations</th>
</tr>
</thead>
<tbody>
<tr>
<td>Simplifying for Complicated Function</td>
<td><ul>
<li><p>when dealing with <strong>large</strong> <strong>functions</strong>, it is <strong>difficult</strong> to <strong>find</strong> parametrized <strong>fit</strong> that <strong>works</strong> well <strong>globally</strong></p></li>
<li><p><strong>3<sup>rd</sup></strong> and <strong>6<sup>th</sup></strong> <strong>degree</strong> <strong>polynomial</strong> fit</p></li>
</ul>
<p><img src="generated_media\DATA750_week06_notes\media\image4.png" style="width:3.33091in;height:2.21334in" /></p>
<p>ChatGPT 5.2</p>
<ul>
<li><p>this <strong>pattern</strong> only <strong>gets</strong> <strong>worse</strong> as polynomial <strong>degrees</strong> <strong>rise</strong></p></li>
</ul></td>
</tr>
<tr>
<td><p>Local Regression</p>
<p>Scatterplot Smoothing</p></td>
<td><ul>
<li><p><strong>separate</strong> <strong>graph</strong> into chunks that can be <strong>graphed</strong> with <strong>lower</strong> <strong>degree</strong> polynomials</p></li>
</ul>
<p><img src="generated_media\DATA750_week06_notes\media\image5.png" style="width:3.38424in;height:2.2558in" /></p>
<p>ChatGPT 5.2</p>
<ul>
<li><p><strong>concatenate</strong> smaller-range, lower-degree <strong>graphs</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Details</td>
<td><ul>
<li><p>for <strong>every x</strong> value, we do a <strong>linear</strong> <strong>fit</strong> of a <strong>windowed</strong> <strong>portion</strong> of the data</p></li>
<li><p><strong>apply</strong> a <strong>weight</strong> to that <strong>window</strong>, tapered down to <strong>0</strong></p></li>
<li><p>do a <strong>least</strong> <strong>squares</strong> fit of that <strong>sub</strong>-<strong>set</strong> of the <strong>data</strong></p></li>
<li><p><strong>evaluate</strong> the <strong>fit</strong> at the <strong>point</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week06_notes\media\image6.png" style="width:3.15205in;height:2.0256in" /></p>
<p>ChatGPT 5.2</p></td>
</tr>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; D</strong></p>
<p><strong>67×3 Matrix{Float64}:</strong></p>
<p><strong>0.67 0.80302 8.58312e-5</strong></p>
<p><strong>0.68 0.75711 0.00211704</strong></p>
<p><strong>⋮</strong></p>
<p><strong>1.32 1.2837 0.00211704</strong></p>
<p><strong>1.33 1.3288 8.58312e-5</strong></p>
<p><strong>julia&gt; x = D[:,1]; y = D[:,2]; w = D[:,3];</strong></p>
<p>This <strong>computes</strong> a <strong>locally</strong> <strong>weighted</strong> linear <strong>regression</strong> using a <strong>tapered</strong> <strong>weight</strong> function</p>
<p><strong>centered</strong> at <strong>x = 1</strong>, and evaluates the <strong>fitted</strong> <strong>model</strong> at that <strong>point</strong></p>
<p><strong>julia&gt; W = Diagonal(sqrt.(w));</strong></p>
<p><strong>julia&gt; A = [ones(size(x)) x];</strong></p>
<p><strong>julia&gt; c = (W*A)\(W*y)</strong></p>
<p><strong>2-element Vector{Float64}:</strong></p>
<p><strong>0.2330148228976884</strong></p>
<p><strong>0.85783827542484</strong></p>
<p><strong>julia&gt; c[1] + c[2]*1</strong></p>
<p><strong>1.0917536504401724</strong></p></td>
</tr>
<tr>
<td>Weight Function</td>
<td><ul>
<li><p><strong>not</strong> a <strong>unique</strong> weight <strong>function</strong>, but a <strong>common</strong> one is the <strong>cubic</strong></p></li>
</ul>
<p><span class="math display">$$\left( \mathbf{1 -}\left( \frac{\left| \mathbf{x - c} \right|}{\mathbf{w}} \right)^{\mathbf{3}} \right)^{\mathbf{3}}$$</span></p>
<ul>
<li><p><strong>w</strong> is a <strong>parameter</strong></p></li>
</ul>
<p><img src="generated_media\DATA750_week06_notes\media\image7.png" style="width:3.18098in;height:2.05242in" /></p>
<p>ChatGPT 5.2</p></td>
</tr>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; x = D[:,1]; y = D[:,2];</strong></p>
<p><strong>julia&gt; w = ((1) .- abs.((x .- 1)./0.335).^3).^1.5;</strong></p>
<p><strong>julia&gt; W = Diagonal(w);</strong></p>
<p>This <strong>computes</strong> a <strong>locally</strong> <strong>weighted</strong> linear <strong>regression</strong> using a <strong>tapered</strong> <strong>weight</strong> function</p>
<p><strong>centered</strong> at <strong>x = 1</strong>, and <strong>evaluates</strong> the <strong>fitted</strong> <strong>model</strong> at that <strong>point</strong></p>
<p><strong>julia&gt; A = [ones(size(x)) x];</strong></p>
<p><strong>julia&gt; c = (W*A)\(W*y)</strong></p>
<p><strong>2-element Vector{Float64}:</strong></p>
<p><strong>0.2330148228976884</strong></p>
<p><strong>0.8587388275424834</strong></p>
<p><strong>julia&gt; c[1] + c[2]*1</strong></p>
<p><strong>1.091753650440172</strong></p></td>
</tr>
<tr>
<td colspan="2">Multiple Dimensions</td>
</tr>
<tr>
<td>Two Dimensions</td>
<td><ul>
<li><p><strong>spatial</strong> <strong>data</strong> is a special case of <strong>multivariable</strong> <strong>input</strong> data consisting of a list of (x, y) points with a value v at each point</p></li>
<li><p>first <strong>approximation</strong> is a <strong>linear</strong> fit</p></li>
</ul>
<p><span class="math display"><strong>f</strong>(<strong>x</strong><strong>,</strong> <strong>y</strong>) <strong>=</strong> <strong>a</strong> <strong>+</strong> <strong>b</strong><strong>x</strong> <strong>+</strong> <strong>c</strong><strong>y</strong></span></p>
<ul>
<li><p>this is a <strong>standard</strong> <strong>multivariate</strong> fit</p></li>
</ul>
<p><img src="generated_media\DATA750_week06_notes\media\image8.png" style="width:3.21447in;height:2.01048in" /></p>
<p>ChatGPT 5.2</p></td>
</tr>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; D</strong></p>
<p><strong>100×3 Matrix{Float64}:</strong></p>
<p><strong>0.89652 0.69851 2.22423</strong></p>
<p><strong>0.16441 0.47566 1.55573</strong></p>
<p><strong>0.68489 0.23571 0.59624</strong></p>
<p><strong>0.88108 0.15748 1.17562</strong></p>
<p><strong>⋮</strong></p>
<p><strong>0.44704 0.93056 0.27164</strong></p>
<p><strong>0.20344 0.47266 1.47501</strong></p>
<p><strong>0.56538 0.99248 2.11564</strong></p>
<p><strong>0.34011 0.74739 1.09583</strong></p>
<p><strong>julia&gt; x = D[:,1]; y = D[:,2]; v = D[:,3];</strong></p>
<p><strong>julia&gt; A = [ones(size(x)) x y];</strong></p>
<p><strong>julia&gt; A \ v</strong></p>
<p><strong>3-element Vector{Float64}:</strong></p>
<p><strong>0.82242157222637813</strong></p>
<p><strong>0.988772946529357</strong></p>
<p>This is the <strong>tricube</strong> <strong>weight</strong> <strong>function</strong> expressed in terms of <strong>distance</strong> <strong>d</strong> and <strong>window width w</strong></p>
<p>Typically <strong>used</strong> with the <strong>implicit</strong> <strong>condition |d| &lt; w</strong> (weight = 0 outside the window)</p>
<p><strong>1.2541980858432</strong></p></td>
</tr>
<tr>
<td>Local Fit</td>
<td><ul>
<li><p>use a local fit to get a value for a point</p></li>
</ul>
<p>based on the surrounding points</p>
<ul>
<li><p>the width function</p></li>
</ul>
<p><span class="math display">$$\left( \mathbf{1 -}\left( \frac{\mathbf{d}}{\mathbf{w}} \right)^{\mathbf{3}} \right)^{\mathbf{3}}$$</span></p>
<ul>
<li><p>d is the distance from the center, w is the radius of the region</p></li>
</ul>
<p><img src="generated_media\DATA750_week06_notes\media\image9.png" style="width:2.87192in;height:1.77645in" /></p>
<p>ChatGPT 5.2</p></td>
</tr>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; D</strong></p>
<p><strong>146×3 Matrix{Float64}:</strong></p>
<p><strong>-0.386386 -0.880319 -7.8</strong></p>
<p><strong>-0.392838 -0.61673 -1.9</strong></p>
<p><strong>0.273446 0.582663 -14.8</strong></p>
<p><strong>⋮</strong></p>
<p><strong>0.49234 0.419114 -15.5</strong></p>
<p><strong>0.463917 0.374538 -13.8</strong></p>
<p><strong>julia&gt; x = D[:,1]; y = D[:,2]; val = D[:,3];</strong></p>
<p>Here, <strong>d</strong> is the <strong>radial</strong> <strong>distance</strong> from the <strong>origin</strong>, <strong>w</strong> is a <strong>tricube</strong></p>
<p><strong>weight</strong> function with window <strong>width 0.8</strong>, <strong>A</strong> is the local <strong>planar</strong> <strong>design</strong> <strong>matrix</strong>, and</p>
<p>the <strong>final</strong> <strong>vector</strong> gives the weighted <strong>least</strong>-<strong>squares</strong> <strong>surface</strong> <strong>fit</strong> coefficients</p>
<p><strong>julia&gt; d = norm.(x, y);</strong></p>
<p><strong>julia&gt; w = (1 .- abs.(d ./ 0.8).^3).^1.5;</strong></p>
<p><strong>julia&gt; W = Diagonal(w);</strong></p>
<p><strong>julia&gt; A = [ones(size(x)) x y];</strong></p>
<p><strong>julia&gt; (W*A) \ (W*val)</strong></p>
<p><strong>3-element Vector{Float64}:</strong></p>
<p><strong>-9.673136939747274</strong></p>
<p><strong>-4.650837446286345</strong></p>
<p><strong>-7.950323134280955</strong></p></td>
</tr>
<tr>
<td>Overlay the Function</td>
<td style="text-align: center;"><span class="math inline"><strong>f</strong>(<strong>x</strong><strong>,</strong> <strong>y</strong>) <strong>=</strong> <strong>−</strong><strong>9.67</strong> <strong>−</strong> <strong>4.61</strong><strong>x</strong> <strong>−</strong> <strong>7.95</strong><strong>y</strong></span><img src="generated_media\DATA750_week06_notes\media\image10.png" style="width:2.854in;height:1.6811in" /></td>
</tr>
<tr>
<td>Other Weights</td>
<td><p><span class="math display">$$\mathbf{w}\left( \mathbf{r} \right)\mathbf{=}\frac{\mathbf{1}}{\mathbf{r}^{\mathbf{2}}\mathbf{+}\mathbf{r}^{\mathbf{4}}}\mathbf{=}\frac{\mathbf{1}}{\mathbf{r}^{\mathbf{2}}\left( \mathbf{1 +}\mathbf{r}^{\mathbf{2}} \right)}$$</span></p>
<p><img src="generated_media\DATA750_week06_notes\media\image11.png" style="width:2.83276in;height:1.44222in" /></p></td>
</tr>
<tr>
<td>2D Fit</td>
<td style="text-align: center;"><p><strong>render 3-D surface on a 2-D plane</strong></p>
<p><img src="generated_media\DATA750_week06_notes\media\image12.png" style="width:3.32558in;height:1.24176in" /></p></td>
</tr>
<tr>
<td colspan="2">Eigenvalues and Eigenvectors</td>
</tr>
<tr>
<td>Mathematical Statement</td>
<td><ul>
<li><p>the mathematical statement is pretty straight forward</p></li>
</ul>
<p><span class="math display"><strong>A</strong> <strong>x</strong> <strong>=</strong> <strong>λ</strong><strong>x</strong><strong>,</strong>   <strong>x</strong> <strong>≠</strong><strong>0</strong></span></p>
<ul>
<li><p><strong>x</strong> is an <strong>eigenvector</strong> of the <strong>matrix A</strong></p></li>
<li><p><strong>λ</strong> is an <strong>eigenvalue</strong></p></li>
<li><p><strong>A</strong> has to be a <strong>square</strong> <strong>matrix</strong> (<strong>A</strong> and <strong>x</strong> <strong>might</strong> be <strong>complex</strong> numbers)</p></li>
</ul></td>
</tr>
<tr>
<td>Geometric Interpretation</td>
<td><ul>
<li><p>geometrically, <strong>A</strong> <strong>scales</strong> x <strong>by</strong> the <strong>number</strong> λ</p></li>
</ul>
<p><strong>λx</strong></p>
<p><strong>x</strong></p></td>
</tr>
<tr>
<td>Quick Refresh</td>
<td><ul>
<li><p>the <strong>standard</strong> mathematical <strong>approach</strong> to <strong>find</strong> <strong>eigenvalues</strong> and <strong>eigenvectors</strong></p>
<ul>
<li><p><strong>define</strong> the characteristic <strong>equation</strong></p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>p</strong>(<strong>λ</strong>)<strong>=</strong><strong>det</strong> (<strong>A</strong><strong>−</strong><strong>λ</strong><strong>I</strong>)</span></p>
<p><span class="math inline">$\left( \mathbf{\lambda} \right)\mathbf{=}\mathbf{de}\mathbf{t}\left( \begin{bmatrix}
\mathbf{- 4} &amp; \mathbf{- 2} \\
\mathbf{- 3} &amp; \mathbf{1}
\end{bmatrix} \right)\mathbf{-}\mathbf{\lambda}\begin{bmatrix}
\mathbf{1} &amp; \mathbf{0} \\
\mathbf{0} &amp; \mathbf{1}
\end{bmatrix}\mathbf{=}\mathbf{\det}\left( \begin{bmatrix}
\mathbf{- 4 - \lambda} &amp; \mathbf{- 2} \\
\mathbf{- 3} &amp; \mathbf{1 - \lambda}
\end{bmatrix} \right)\mathbf{=}\mathbf{\lambda}^{\mathbf{2}}\mathbf{+}\mathbf{\lambda}\mathbf{- 10}$</span></p>
<ul>
<li><p>If <strong>A</strong> is an <span class="math inline"><strong>n</strong> <strong>×</strong> <strong>n</strong></span> <strong>matrix</strong>, this is an <strong>n-th</strong> degree <strong>polynomial</strong> in <strong>λ</strong>.</p></li>
<li><p>The <strong>eigenvalues</strong> are the <strong>roots</strong> of this <strong>polynomial</strong>.</p></li>
</ul>
<p><span class="math display"><strong>λ</strong><sup><strong>2</strong></sup><strong>+</strong><strong>3</strong><strong>λ</strong> <strong>−</strong> <strong>10</strong><strong>=</strong>(<strong>λ</strong> <strong>+</strong> <strong>5</strong>)(<strong>λ</strong> <strong>−</strong> <strong>2</strong>)<strong>→</strong><strong>λ</strong><sub><strong>1</strong></sub> <strong>=</strong> <strong>−</strong><strong>5</strong><strong>,</strong> <strong>λ</strong><sub><strong>2</strong></sub> <strong>=</strong> <strong>2</strong></span></p>
<ul>
<li><p>the <strong>eigenvector</strong> is a <strong>solution</strong> to the <strong>linear</strong> <strong>system</strong></p></li>
</ul>
<p><span class="math display">(<strong>A</strong> <strong>−</strong> <strong>λ</strong><strong>I</strong>)<strong>x</strong> <strong>=</strong> <strong>0</strong></span></p>
<p><span class="math display">$$\mathbf{0 =}\begin{bmatrix}
\mathbf{- 4 -}\left( \mathbf{- 5} \right) &amp; \mathbf{- 2} \\
\mathbf{- 3} &amp; \mathbf{1 -}\left( \mathbf{- 5} \right)
\end{bmatrix}\mathbf{x =}\begin{bmatrix}
\mathbf{1} &amp; \mathbf{- 2} \\
\mathbf{- 3} &amp; \mathbf{6}
\end{bmatrix}\mathbf{x}\mathbf{\rightarrow x =}\genfrac{[}{]}{0pt}{}{\mathbf{2}}{\mathbf{1}}$$</span></p>
<ul>
<li><p>the <strong>second</strong> <strong>eigenvector</strong> is similar</p></li>
</ul>
<p><span class="math display">$$\mathbf{0 =}\begin{bmatrix}
\mathbf{- 4 -}\left( \mathbf{2} \right) &amp; \mathbf{- 2} \\
\mathbf{- 3} &amp; \mathbf{1 -}\left( \mathbf{2} \right)
\end{bmatrix}\mathbf{x =}\begin{bmatrix}
\mathbf{- 6} &amp; \mathbf{- 2} \\
\mathbf{- 3} &amp; \mathbf{- 1}
\end{bmatrix}\mathbf{x}\mathbf{\rightarrow x =}\genfrac{[}{]}{0pt}{}{\mathbf{1}}{\mathbf{- 3}}$$</span></p>
<ul>
<li><p>the <strong>eigenvector</strong> is <strong>not</strong> <strong>unique</strong>; you can <strong>scale</strong> <strong>by</strong> any <strong>constant</strong></p></li>
<li><p>all <strong>eigenvectors</strong> that <strong>match</strong> the <strong>dimension</strong> are placed <strong>in</strong> the <strong>matrix</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{S =}\begin{bmatrix}
\mathbf{2} &amp; \mathbf{1} \\
\mathbf{1} &amp; \mathbf{- 3}
\end{bmatrix}$$</span></p>
<ul>
<li><p>this <strong>matrix</strong> has the following <strong>property</strong></p></li>
</ul>
<blockquote>
<p><span class="math inline"><strong>A</strong><strong>S</strong> <strong>=</strong> <strong>S</strong></span><em><strong>Λ</strong></em> <span class="math inline"> </span><img src="generated_media\DATA750_week06_notes\media\image13.gif" /><span class="math inline">$\mathbf{\ }\bigwedge_{}^{}\mathbf{=}\begin{bmatrix}
\mathbf{- 5} &amp; \mathbf{0} \\
\mathbf{0} &amp; \mathbf{2}
\end{bmatrix}$</span></p>
</blockquote></td>
</tr>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; A = [-4 -2; -3 1]</strong></p>
<p><strong>2×2 Matrix{Int64}:</strong></p>
<p>These <strong>computations</strong> <strong>verify</strong> that <strong>[2,1]</strong> and <strong>[1,-3]</strong> are <strong>eigenvectors</strong></p>
<p>of <strong>A</strong> with <strong>eigenvalues</strong> <strong>−5</strong> and <strong>2</strong>, respectively, and that <strong>A = SΛS⁻¹</strong></p>
<p><strong>-4 -2</strong></p>
<p><strong>-3 1</strong></p>
<p><strong>julia&gt; A*[2,1] - (-5)*[2,1]</strong></p>
<p><strong>2-element Vector{Int64}:</strong></p>
<p><strong>0</strong></p>
<p><strong>0</strong></p>
<p><strong>julia&gt; A*[1,-3] - 2*[1,-3]</strong></p>
<p><strong>2-element Vector{Int64}:</strong></p>
<p><strong>0</strong></p>
<p><strong>0</strong></p></td>
</tr>
<tr>
<td>(Quick?) Refresh Cont.</td>
<td><ul>
<li><p><strong>most</strong> of the <strong>time</strong> this <strong>matrix</strong> <strong>S</strong> is <strong>invertible</strong></p></li>
</ul>
<p><span class="math display"><strong>A</strong><strong>S</strong> <strong>=</strong> <strong>S</strong><strong>Λ</strong> <strong>⇒</strong> <strong>A</strong> <strong>=</strong> <strong>S</strong><strong>Λ</strong><strong>S</strong><sup><strong>−</strong><strong>1</strong></sup></span></p>
<p><span class="math display"><strong>Λ</strong><strong>=</strong><strong>S</strong><sup><strong>−</strong><strong>1</strong></sup><strong>A</strong><strong>S</strong></span></p>
<ul>
<li><p>you will <strong>often</strong> get <strong>complex</strong> <strong>numbers</strong> and sometimes the <strong>matrix</strong> is <strong>not</strong> <strong>diagonalizable</strong></p>
<ul>
<li><p>you can <strong>still</strong> <strong>find</strong> <strong>eigenvalues</strong></p></li>
<li><p>but <strong>not</strong> an <strong>invertible</strong> <strong>matrix</strong> <strong>S</strong> of <strong>eigenvectors</strong>.</p></li>
</ul></li>
<li><p><strong>numerically</strong>, that last <strong>case</strong> is very <strong>hard</strong> to <strong>detect</strong> and handle.</p></li>
</ul></td>
</tr>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; A</strong></p>
<p><strong>2×2 Matrix{Int64}:</strong></p>
<p><strong>-4 -2</strong></p>
<p><strong>-3 1</strong></p>
<p>The <strong>first</strong> <strong>example</strong> verifies real <strong>diagonalization</strong> <strong>A = SΛS⁻¹.</strong></p>
<p>The <strong>second</strong> <strong>example</strong> illustrates a <strong>matrix</strong> with <strong>complex</strong> <strong>eigenvalues</strong>,</p>
<p><strong>requiring</strong> complex <strong>eigenvectors</strong> and a <strong>complex</strong> diagonal <strong>matrix Λ</strong></p>
<p><strong>julia&gt; S \ A / inv(S)</strong></p>
<p><strong>2×2 Matrix{Float64}:</strong></p>
<p><strong>-4.0 -2.0</strong></p>
<p><strong>-3.0 1.0</strong></p>
<p><strong>julia&gt; inv(S)*A*S</strong></p>
<p><strong>2×2 Matrix{Float64}:</strong></p>
<p><strong>-5.0 4.44089e-16</strong></p>
<p><strong>0.0 2.0</strong></p>
<p><strong>julia&gt; A = [-1 5; -2 5]</strong></p>
<p><strong>2×2 Matrix{Int64}:</strong></p>
<p><strong>-1 5</strong></p>
<p><strong>-2 5</strong></p>
<p><strong>julia&gt; S = [5 5-3im; 5+3im 3+1im]</strong></p>
<p><strong>2×2 Matrix{Complex{Int64}}:</strong></p>
<p><strong>5+0im 5-3im</strong></p>
<p><strong>5+3im 3+1im</strong></p>
<p><strong>julia&gt; Lambda = diagm([2-im, 2+im])</strong></p>
<p><strong>2×2 Matrix{Complex{Int64}}:</strong></p>
<p><strong>2-im 0+0im</strong></p>
<p><strong>0+0im 2+im</strong></p></td>
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
<th>(Quick!) Refresh Cont.</th>
<th><ul>
<li><p>previous approach will not give numerical solution</p></li>
<li><p>it is very difficult to compute the determinant of</p></li>
</ul>
<p><strong>the characteristic polynomial.</strong></p>
<p><span class="math inline"><strong>A</strong> <strong>−</strong> <strong>λ</strong><strong>I</strong></span></p>
<ul>
<li><p>analytical solutions</p>
<ul>
<li><p>exists for: <span class="math inline"><em>n</em> = 2, 3, 4</span></p></li>
</ul></li>
</ul>
<p>need <strong>iterative</strong> <strong>methods</strong></p>
<ul>
<li><p>none exist for: <span class="math inline"><em>n</em> &gt; 4</span></p></li>
</ul>
<ul>
<li><p>high degree polynomials are numerically very tricky</p></li>
</ul>
<p><span class="math display">(<strong>A</strong> <strong>−</strong> <strong>λ</strong><strong>I</strong>)<strong>x</strong> <strong>=</strong> <strong>0</strong></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Basix Idea for Computing</td>
<td><ul>
<li><p>pick any <strong>x</strong>, call it: <span class="math inline"><strong>x</strong><sup><strong>0</strong></sup></span></p></li>
<li><p>apply <strong>A</strong> <strong>over</strong> and <strong>over</strong></p></li>
</ul>
<p><span class="math display"><strong>x</strong><sub><strong>1</strong></sub> <strong>=</strong> <strong>A</strong><strong>x</strong><sub><strong>0</strong></sub><strong>,</strong><strong>x</strong><sub><strong>2</strong></sub> <strong>=</strong> <strong>A</strong><strong>x</strong><sub><strong>1</strong></sub><strong>,</strong><strong>x</strong><sub><strong>3</strong></sub> <strong>=</strong> <strong>A</strong><strong>x</strong><sub><strong>2</strong></sub><strong>,</strong> <strong>…</strong></span></p>
<ul>
<li><p>if you start with an eigenvector you get</p></li>
</ul>
<p><span class="math display"><strong>x</strong><sub><strong>n</strong></sub><strong>=</strong><strong>λ</strong><sup><strong>n</strong></sup><strong>x</strong><sub><strong>0</strong></sub></span></p>
<ul>
<li><p>if <strong>|λ|</strong> is small this <strong>goes</strong> to <strong>0</strong></p></li>
<li><p>if <strong>|λ|</strong> is <strong>larger</strong> than <strong>1</strong> this <strong>goes</strong> to <strong>infinity</strong></p></li>
</ul>
<ul>
<li><p><strong>direction</strong> is <strong>relevant</strong> here, <strong>not</strong> the <strong>magnitude,</strong> so we <strong>normalize</strong> each step.</p></li>
</ul>
<p><span class="math display">$$\mathbf{x}_{\mathbf{1}}\mathbf{=}\frac{\mathbf{A}\mathbf{x}_{\mathbf{0}}}{\textit{\textbf{|}}\left| \mathbf{A}\mathbf{x}_{\mathbf{0}} \right|\textit{\textbf{|}}}\mathbf{,}\mathbf{\quad}\mathbf{x}_{\mathbf{2}}\mathbf{=}\frac{\mathbf{A}\mathbf{x}_{\mathbf{1}}}{\left| \textit{\textbf{|}}\mathbf{A}\mathbf{x}_{\mathbf{1}} \right|\textit{\textbf{|}}}\mathbf{,}\mathbf{\quad}\mathbf{x}_{\mathbf{3}}\mathbf{=}\frac{\mathbf{A}\mathbf{x}_{\mathbf{2}}}{\left| \textit{\textbf{|}}\mathbf{A}\mathbf{x}_{\mathbf{2}} \right|\textit{\textbf{|}}}\mathbf{,}\mathbf{\ }\mathbf{\ldots}$$</span></p></td>
</tr>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; A = [19 -6; 45 -14];</strong></p>
<p><strong>julia&gt; x = [1,1];</strong></p>
<p>This <strong>demonstrates</strong> the <strong>power</strong> <strong>method</strong>. Repeated <strong>normalization</strong> of <strong>A*x</strong> causes</p>
<p><strong>x</strong> to <strong>converge</strong> in <strong>direction</strong> to the <strong>dominant</strong> <strong>eigenvector</strong> of <strong>A</strong>, with the <strong>ratio</strong></p>
<p><strong>x₂/x</strong>₁ approaching the <strong>eigenvector</strong> <strong>slope</strong>.</p>
<p><strong>julia&gt; v = A*x; x = v/norm(v)</strong></p>
<p><strong>2-element Vector{Float64}:</strong></p>
<p><strong>0.3867266762507425</strong></p>
<p><strong>0.922194381828531</strong></p>
<p><strong>julia&gt; x/x[1]</strong></p>
<p><strong>2-element Vector{Float64}:</strong></p>
<p><strong>1.0</strong></p>
<p><strong>2.3846153846153846</strong></p>
<p><strong>julia&gt; v = A*x; x = v/norm(v)</strong></p></td>
</tr>
<tr>
<td>How to Call</td>
<td><ul>
<li><p>function ‘<em><strong>eigen’</strong></em> finds <strong>eigenvalues</strong> and <strong>eigenvectors</strong> returns<strong>:</strong></p>
<ul>
<li><p><strong>list</strong> of <strong>eigenvalues</strong></p></li>
<li><p><strong>eigenvectors</strong></p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>S</strong><strong>Λ</strong><strong>S</strong><sup><strong>−</strong><strong>1</strong></sup> <strong>=</strong> <strong>A</strong></span></p>
<ul>
<li><p><strong>computation scales</strong> like: <span class="math inline"><strong>O</strong>(<strong>n</strong><sup><strong>2.7</strong></sup>)</span></p></li>
</ul></td>
</tr>
<tr>
<td rowspan="2">Julia</td>
<td><p><strong>julia&gt; A = rand(2000,2000); @time B = A*A;</strong></p>
<p>shows <strong>eigenvalue</strong> <strong>computation</strong> is <strong>significantly</strong></p>
<p>more <strong>expensive</strong> than <strong>matrix</strong> <strong>multiplication</strong>.</p>
<p><strong>0.074313 seconds (2 allocations: 30.518 MiB)</strong></p>
<p><strong>julia&gt; A = rand(4000,4000); @time B = A*A;</strong></p>
<p><strong>0.423728 seconds (2 allocations: 122.070 MiB)</strong></p>
<p><strong>julia&gt; A = rand(2000,2000); @time f = eigen(A);</strong></p>
<p><strong>2.222281 seconds (22 allocations: 124.208 MiB)</strong></p>
<p><strong>julia&gt; A = rand(4000,4000); @time f = eigen(A);</strong></p>
<p><strong>13.800373 seconds (28 allocations: 492.555 MiB, 0.05% gc time)</strong></p></td>
</tr>
<tr>
<td><p><strong>julia&gt; using LinearAlgebra</strong></p>
<p><strong>julia&gt; A = [19 -6; 45 -14];</strong></p>
<p><strong>julia&gt; factor = eigen(A)</strong></p>
<p><strong>Eigen{Float64, Float64, Matrix{Float64}, Vector{Float64}}</strong></p>
<p><strong>values:</strong></p>
<p>The <strong>second</strong> <strong>example</strong> verifies <strong>diagonalization</strong>:</p>
<p><strong>A = SΛS⁻¹</strong>, with <strong>small</strong> numerical <strong>error</strong> due to <strong>floating</strong>-<strong>point</strong> <strong>arithmetic</strong></p>
<p><strong>2-element Vector{Float64}:</strong></p>
<p><strong>1.0000000000000053</strong></p>
<p><strong>3.9999999999999993</strong></p>
<p><strong>vectors:</strong></p>
<p><strong>2×2 Matrix{Float64}:</strong></p>
<p><strong>0.316228 0.371391</strong></p>
<p><strong>0.948683 0.928477</strong></p>
<p><strong>julia&gt; Lambda = diagm(factor.values)</strong></p>
<p><strong>2×2 Matrix{Float64}:</strong></p>
<p><strong>1.0 0.0</strong></p>
<p><strong>0.0 4.0</strong></p>
<p><strong>julia&gt; S = factor.vectors;</strong></p>
<p><strong>julia&gt; S*Lambda*inv(S) – A</strong></p>
<p><strong>2×2 Matrix{Float64}:</strong></p>
<p><strong>7.10543e-15 -3.55271e-15</strong></p>
<p><strong>2.84217e-14 -1.06581e-14</strong></p></td>
</tr>
<tr>
<td>What Can Happen</td>
<td><ul>
<li><p>For a <strong>non</strong>-<strong>symmetric</strong> matrix, <strong>eigenvalues</strong> and <strong>eigenvectors</strong> can be <strong>complex</strong></p></li>
<li><p>For <strong>matrices</strong> that are <strong>not</strong> <strong>diagonalizable</strong>, the <strong>return</strong> is <strong>invalid</strong></p></li>
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
<th rowspan="2">Julia</th>
<th><p>julia&gt; A = [2 1; 0 2]</p>
<p>2×2 Matrix{Int64}:</p>
<p>2 1</p>
<ol type="1">
<li><p>2</p></li>
</ol>
<p>julia&gt; eigen(A)</p>
<p><strong>matrix</strong> is <strong>defective</strong>: it has <strong>repeated</strong> <strong>eigenvalues</strong> (λ = 2) and does</p>
<p><strong>not</strong> have <strong>two</strong> <strong>independent</strong> <strong>eigenvectors</strong></p>
<p>Eigen{Float64, Float64, Matrix{Float64}, Vector{Float64}}</p>
<p>values:</p>
<p>2-element Vector{Float64}:</p>
<p>2.0</p>
<p>2.0</p>
<p>vectors:</p>
<p>2×2 Matrix{Float64}:</p>
<p>1.0 -1.0</p>
<p>0.0 4.44089e-16</p></th>
</tr>
<tr>
<th><p><strong>julia&gt; A = rand(5,5)</strong></p>
<p><strong>5×5 Matrix{Float64}:</strong></p>
<p><strong>0.896989 0.928842 0.194495 0.56745 0.445895</strong></p>
<p><strong>0.833862 0.817736 0.784447 0.956141 0.757149</strong></p>
<p><strong>0.089797 0.585985 0.951922 0.342448 0.593538</strong></p>
<p><strong>0.283555 0.569285 0.15656 0.917266 0.58781</strong></p>
<p><strong>0.865177 0.415104 0.207601 0.759322 0.454219</strong></p>
<p><strong>julia&gt; eigen(A)</strong></p>
<p><strong>Eigen{ComplexF64, ComplexF64, Matrix{ComplexF64}, Vector{ComplexF64}}</strong></p>
<p><strong>values:</strong></p>
<p>illustrates that a <strong>general</strong> <strong>non</strong>-<strong>symmetric</strong> <strong>matrix</strong></p>
<p>may have <strong>complex</strong> <strong>eigenvalues</strong> and <strong>complex</strong> <strong>eigenvectors</strong></p>
<p><strong>5-element Vector{ComplexF64}:</strong></p>
<p><strong>-0.0630614639921762 + 0.0im</strong></p>
<p><strong>0.21491356519522642 - 0.18293391221310967im</strong></p>
<p><strong>0.21491356519522642 + 0.18293391221310967im</strong></p>
<p><strong>0.8447011083491994 + 0.0im</strong></p>
<p><strong>2.7393605534814863 + 0.0im</strong></p>
<p><strong>vectors:</strong></p>
<p><strong>5×5 Matrix{ComplexF64}:</strong></p>
<p><strong>0.383351+0.0im 0.192263+0.141744im 0.258763+0.0im 0.515498+0.0im ...</strong></p>
<p><strong>-0.335414+0.0im -0.626591-0.297367im -0.105868+0.0im 0.646038+0.0im</strong></p>
<p><strong>0.032539+0.0im -0.146977+0.140434im -0.875045+0.0im 0.320683+0.0im</strong></p>
<p><strong>0.498739+0.0im 0.558948-0.210011im 0.358323+0.0im 0.389948+0.0im</strong></p>
<p><strong>-0.700528+0.0im -0.735823-0.0im 0.166535+0.0im 0.248999+0.0im</strong></p>
<p><strong>julia&gt; eigen(A)</strong></p>
<p><strong>Eigen{ComplexF64, ComplexF64, Matrix{ComplexF64}, Vector{ComplexF64}}</strong></p>
<p><strong>values:</strong></p>
<p><strong>5-element Vector{ComplexF64}:</strong></p>
<p><strong>-0.0630614639921762 + 0.0im</strong></p>
<p><strong>0.21491356519522642 - 0.18293391221310967im</strong></p>
<p><strong>0.21491356519522642 + 0.18293391221310967im</strong></p>
<p><strong>0.8447011083491994 + 0.0im</strong></p>
<p><strong>2.7393605534814863 + 0.0im</strong></p>
<p><strong>vectors:</strong></p>
<p><strong>5×5 Matrix{ComplexF64}:</strong></p>
<p><strong>0.383351+0.0im 0.192263+0.141744im 0.258763+0.0im 0.515498+0.0im ...</strong></p>
<p><strong>-0.335414+0.0im -0.626591-0.297367im -0.105868+0.0im 0.646038+0.0im</strong></p>
<p><strong>0.032539+0.0im -0.146977+0.140434im -0.875045+0.0im 0.320683+0.0im</strong></p>
<p><strong>0.498739+0.0im 0.558948-0.210011im 0.358323+0.0im 0.389948+0.0im</strong></p>
<p><strong>-0.700528+0.0im -0.735823-0.0im 0.166535+0.0im 0.248999+0.0im</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Symmetric Matrices</td>
<td><ul>
<li><p><strong>symmetric</strong> <strong>matrices</strong> are</p>
<ul>
<li><p>always <strong>diagonalizable</strong></p></li>
<li><p>always <strong>real</strong></p></li>
<li><p><strong>orthogonal</strong> to each other</p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>S</strong><sup><strong>−</strong><strong>1</strong></sup><strong>=</strong><strong>S</strong><sup><strong>T</strong></sup></span></p>
<ul>
<li><p><strong>normalize the vectors</strong> <span class="math inline"><strong>=</strong> <strong>m</strong><strong>a</strong><strong>t</strong><strong>r</strong><strong>i</strong><strong>x</strong> <strong>′</strong><strong>Q</strong><strong>′</strong></span></p></li>
</ul></td>
</tr>
<tr>
<td>Julia</td>
<td><p><strong>julia&gt; B = rand(5,5); A = B + B'</strong></p>
<p><strong>5×5 Matrix{Float64}:</strong></p>
<p><strong>1.46841 0.217176 1.14759 1.77643 1.84304</strong></p>
<p><strong>0.217176 1.0952 1.14557 0.673613 1.22555</strong></p>
<p><strong>1.14759 1.14557 1.1925 0.83276 1.10775</strong></p>
<p><strong>1.77643 0.673613 0.83276 0.31743 1.02043</strong></p>
<p><strong>1.84304 1.22555 1.10775 1.02043 0.311548</strong></p>
<p><strong>julia&gt; factors = eigen(A)</strong></p>
<p><strong>Eigen{Float64, Float64, Matrix{Float64}, Vector{Float64}}</strong></p>
<p><strong>values:</strong></p>
<p>Because A is symmetric, the eigenvalues are real and the eigenvectors</p>
<p>form an orthonormal basis, so QᵀQ = I up to floating-point error.</p>
<p><strong>5-element Vector{Float64}:</strong></p>
<p><strong>-1.479744357061945</strong></p>
<p><strong>-0.7384718547725923</strong></p>
<p><strong>-0.018271356454782802</strong></p>
<p><strong>1.2357763366272927</strong></p>
<p><strong>5.385759909664219</strong></p>
<p><strong>vectors:</strong></p>
<p><strong>5×5 Matrix{Float64}:</strong></p>
<p><strong>-0.59091 -0.200388 0.0384984 0.552359 -0.551442</strong></p>
<p><strong>-0.358851 -0.676396 0.462094 -0.730869 -0.343058</strong></p>
<p><strong>0.037868 0.0585515 -0.089259 -0.326998 -0.447297</strong></p>
<p><strong>0.339562 0.791801 0.198595 0.231927 -0.405452</strong></p>
<p><strong>0.636644 -0.568774 0.239608 -0.0035335 -0.462338</strong></p>
<p><strong>julia&gt; Q = factors.vectors;</strong></p>
<p><strong>julia&gt; Q' * Q</strong></p>
<p><strong>5×5 Matrix{Float64}:</strong></p>
<p><strong>1.0 1.71193e-16 -3.53161e-17 -3.18443e-17 ...</strong></p>
<p><strong>1.71193e-16 1.0 -2.86422e-17 2.47198e-17</strong></p>
<p><strong>-3.53161e-17 -2.86422e-17 1.0 4.60241e-17</strong></p>
<p><strong>-3.18443e-17 2.47198e-17 4.60241e-17 1.0</strong></p>
<p><strong>...</strong></p></td>
</tr>
</tbody>
</table>
