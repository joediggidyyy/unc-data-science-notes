> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week2_notes.pdf](../DATA780_week2_notes.pdf)
> - DOCX: [DATA780_week2_notes.docx](DATA780_week2_notes.docx)

---

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr>
<th>Linear Algebra Background</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">What this is</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>recap of Linear Algebra concepts</p></li>
<li><p>tools to apply toward ML implementation and methodology</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Linear Algebra</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr>
<th><strong>scalar</strong></th>
<th><p>a <strong>value</strong> having <strong>only</strong> <strong>magnitude</strong> and <strong>not</strong> <strong>direction</strong></p>
<p>https://languages.oup.com/google-dictionary-en/</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>vector</strong></td>
<td><p>a <strong>quantity</strong> with both <strong>magnitude</strong> and <strong>direction</strong></p>
<p>https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)</p></td>
</tr>
<tr>
<td><strong>subspace</strong></td>
<td><p>A subset of <em><strong>W</strong></em> of <em><strong>n-space</strong></em> is a subspace if:</p>
<ol type="1">
<li><p>the zero vector is in <em><strong>W</strong></em></p></li>
<li><p><strong><em>x</em> + <em>y</em></strong> is in <em><strong>W</strong></em> whenever <em><strong>x</strong></em> and <em><strong>y</strong></em> are in <em><strong>W</strong></em></p></li>
<li><p><strong><em>a</em>*<em>x</em></strong> is in <em><strong>W</strong></em> whenever <em><strong>x</strong></em> is in <em><strong>W</strong></em> and <em><strong>a</strong></em> is any scalar</p></li>
</ol>
<p><a href="https://www.math.kent.edu/~reichel/glossary">https://www.math.kent.edu/~reichel/glossary</a></p></td>
</tr>
<tr>
<td><strong>basis</strong></td>
<td><p>A basis for a <strong>subspace</strong> <em><strong>W</strong></em> is a se of <strong>vectors</strong> <em><strong>v<sub>1</sub></strong></em>, …, <em><strong>v<sub>k</sub></strong></em> in <em><strong>W</strong></em> such that:</p>
<ol type="1">
<li><p><em><strong>v<sub>1</sub></strong></em>, …, <em><strong>v<sub>k</sub></strong></em> are linearly independent</p></li>
<li><p><em><strong>v<sub>1</sub></strong></em>, …, <em><strong>v<sub>k</sub></strong></em> span <em><strong>W</strong></em></p></li>
</ol>
<p><a href="https://www.math.kent.edu/~reichel/glossary">https://www.math.kent.edu/~reichel/glossary</a></p></td>
</tr>
<tr>
<td><strong>system of equations</strong></td>
<td><p>a <em><strong>linear</strong> <strong>system</strong></em> is a collection of two or more <strong>linear</strong> <strong>equations</strong> involving the <strong>same</strong> <strong>variables</strong>. For example:</p>
<p><img src="generated_media\DATA780_week2_notes\media\image1.png" style="width:2.46909in;height:0.94805in" /></p>
<p>https://en.wikipedia.org/wiki/System_of_</p></td>
</tr>
<tr>
<td><strong>vector spaces</strong></td>
<td><p>a <em><strong>linear</strong></em> <em><strong>space</strong></em> is a set whose <strong>elements</strong> (i.e. <strong>vectors</strong>) can be <strong>added</strong> together and <strong>multiplied</strong> by <strong>scalars</strong></p>
<p><a href="https://www.math.kent.edu/~reichel/glossary">https://www.math.kent.edu/~reichel/glossary</a></p></td>
</tr>
<tr>
<td><strong>outer product</strong></td>
<td><em><strong>u ⊗ v = uv<sup>T : </sup></strong></em>the <strong>tensor product</strong> is the <strong>matrix</strong> whose entries are all <strong>products</strong> of an <strong>element</strong> in the <strong>first</strong> <strong>vector</strong> with an <strong>element</strong> in the <strong>second</strong> vector so that taking the <strong>outer</strong> <strong>product</strong> of <strong>two</strong> <strong>vectors</strong> of <strong>length</strong> <em><strong>n</strong></em> and <em><strong>m</strong></em> will result in an <em><strong>n</strong></em> <strong>x</strong> <em><strong>m</strong></em> <strong>matrix</strong></td>
</tr>
<tr>
<td><strong>inner product</strong></td>
<td><p>a <strong>generalization</strong> of the <strong>dot</strong> <strong>product</strong> and is a way to <strong>multiply</strong> <strong>vectors</strong> together <strong>resulting</strong> in a <strong>scalar</strong> and <strong>satisfies</strong> the <strong>following</strong> properties:</p>
<p><img src="generated_media\DATA780_week2_notes\media\image2.png" style="width:2.5682in;height:1.20026in" /></p>
<p>https://mathworld.wolfram.com/InnerProdu</p></td>
</tr>
<tr>
<td><strong>Hadamar product</strong></td>
<td>the <strong>element</strong>-<strong>wise</strong> <strong>product</strong> of <strong>two</strong> <strong>matrices</strong></td>
</tr>
<tr>
<td><strong>matrix multiplication</strong></td>
<td><p>if <em><strong>A</strong></em> is an <em><strong>m</strong></em> <strong>x</strong> <em><strong>n</strong></em> matrix and <em><strong>B</strong></em> is an <em><strong>n</strong></em> <strong>x</strong> <em><strong>p</strong></em> matrix, the matrix product <em><strong>C = AB</strong></em> is defined to be an <em><strong>m</strong></em> <strong>x</strong> <em><strong>p</strong></em> matrix such that:</p>
<p><img src="generated_media\DATA780_week2_notes\media\image3.png" style="width:3.11967in;height:0.49287in" /></p></td>
</tr>
<tr>
<td><strong>norm</strong></td>
<td><p>given a <strong>vector</strong> <strong>space</strong> <em><strong>X</strong></em> over a <strong>subfield</strong> <em><strong>F</strong></em> of the <strong>complex</strong> <strong>numbers</strong> <em><strong>C</strong></em>, a <strong>norm</strong> on <em><strong>X</strong></em> is a real-valued <strong>function</strong> <em><strong>p</strong></em> : <em><strong>X -&gt; R</strong></em> with the <strong>following</strong> properties:</p>
<p>(where |s| denotes the usual absolute value of a scalar s)</p>
<ol type="1">
<li><p><img src="generated_media\DATA780_week2_notes\media\image4.png" style="width:3.02126in;height:0.31254in" /></p></li>
<li><p><img src="generated_media\DATA780_week2_notes\media\image5.png" style="width:3.46923in;height:0.29171in" /></p></li>
<li><p>positive definiteness for all <img src="generated_media\DATA780_week2_notes\media\image6.png" style="width:2.35449in;height:0.26045in" /></p></li>
</ol>
<p>https://en.wikipedia.org/wiki/Norm_(math</p></td>
</tr>
<tr>
<td><strong>transpose</strong></td>
<td><p>an operator that <strong>flips</strong> a <strong>matrix</strong> over its <strong>diagonal</strong> denoted <strong>A<sup>T</sup></strong></p>
<p><em>https://en.wikipedia.org/wiki/Transpose</em></p></td>
</tr>
<tr>
<td><strong>Eigenvalue</strong></td>
<td><p>an <strong>eigenvalue</strong> of a <em><strong>n-by-n</strong></em> <strong>matrix</strong> A is a <strong>scalar</strong> <em><strong>c</strong></em> such that <em><strong>A*x =</strong></em> <em><strong>c*x</strong></em> holds for some nonzero <strong>vector</strong> <em><strong>x</strong></em> (where <em><strong>x</strong></em> is an <em><strong>n-tuple</strong></em>)</p>
<p><a href="https://www.math.kent.edu/~reichel/glossary">https://www.math.kent.edu/~reichel/glossary</a></p></td>
</tr>
<tr>
<td><strong>Eigenvector</strong></td>
<td><p>an <strong>eigenvector</strong> of an <em><strong>n-by-b</strong></em> <strong>matrix</strong> <em><strong>A</strong></em> is a nonzero <strong>vector</strong> <em><strong>x</strong></em> such that <em><strong>A*x = c*x</strong></em> holds for some <strong>scalar</strong></p>
<p><a href="https://www.math.kent.edu/~reichel/glossary">https://www.math.kent.edu/~reichel/glossary</a></p></td>
</tr>
<tr>
<td><strong>Eigendecomposition</strong></td>
<td><p>the <strong>factorization</strong> of a <strong>matrix</strong> into a canonical form, whereby the <strong>matrix</strong> is represented in <strong>terms</strong> of its <strong>eigenvalues</strong> and <strong>eigenvectors</strong></p>
<p><a href="https://www.math.kent.edu/~reichel/glossary">https://www.math.kent.edu/~reichel/glossary</a></p></td>
</tr>
<tr>
<td><strong>trace</strong></td>
<td><p>the <strong>sum</strong> of its <strong>eigenvalues</strong> counted with multiplicities such that:</p>
<ol type="1">
<li><p><em><strong>tr(AB) = tr(BA)</strong></em> for any same-sized <strong>matrices</strong> <em><strong>A</strong></em> and <em><strong>B</strong></em></p></li>
<li><p>thus, <strong>similar</strong> <strong>matrices</strong> have the <strong>same</strong> <strong>trace</strong></p></li>
<li><p><img src="generated_media\DATA780_week2_notes\media\image7.png" style="width:3.3338in;height:0.62509in" /></p></li>
</ol>
<p>https://en.wikipedia.org/wiki/Trace_(lin</p></td>
</tr>
<tr>
<td><strong>norm to distance</strong></td>
<td><em><strong>d(x, y) = ||x – y||</strong></em>, where ‘|| . ||’ denotes <strong>magnitude</strong> and ‘ – ‘ denotes <strong>difference</strong></td>
</tr>
<tr>
<td><strong>Euclidean Distance</strong></td>
<td><p><em><strong>d(p, q)<sup>2</sup> = (q<sub>1</sub> – p<sub>1</sub>)<sup>2</sup> + (q<sub>2</sub> – p<sub>2</sub>)<sup>2</sup></strong></em></p>
<p><img src="generated_media\DATA780_week2_notes\media\image8.png" style="width:1.66047in;height:0.51948in" /></p>
<p><img src="generated_media\DATA780_week2_notes\media\image9.png" style="width:2.49583in;height:0.45965in" /></p></td>
</tr>
<tr>
<td><strong>Holder’s Inequality</strong></td>
<td><img src="generated_media\DATA780_week2_notes\media\image10.png" style="width:1.96156in;height:0.87013in" /> <img src="generated_media\DATA780_week2_notes\media\image11.png" style="width:0.83117in;height:0.45857in" /></td>
</tr>
<tr>
<td><strong>vector space axioms</strong></td>
<td><table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr>
<th><strong>associativity</strong></th>
<th><em><strong>u + (v + w) = (u + v) + w</strong></em></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>commutativity</strong></td>
<td><em><strong>u + v = v + u</strong></em></td>
</tr>
<tr>
<td><strong>identity element</strong></td>
<td>there exists an element <em><strong>0 ∈ V,</strong></em> called the <em><strong>zero vector</strong></em> such that <em><strong>v + 0 = v</strong></em> for all <em><strong>v ∈ V</strong></em></td>
</tr>
<tr>
<td><strong>inverse elements</strong></td>
<td>for every <em><strong>v ∈ V</strong></em> there <strong>exists</strong> an element <em><strong>-v ∈ V</strong></em>, called the <em><strong>additive inverse</strong></em> of <em><strong>v</strong></em>, such that <em><strong>v + (-v) = 0</strong></em></td>
</tr>
<tr>
<td><strong>scalar-multiplication / field-multiplication compatibility</strong></td>
<td><em><strong>a(bv) = (ab)v</strong></em></td>
</tr>
<tr>
<td><strong>identity element of scalar multiplication</strong></td>
<td><em><strong>I🞗 v = v</strong></em>, where <em><strong>I</strong></em> denotes the <strong>multiplicative</strong> <strong>identity</strong> in <em><strong>F</strong></em></td>
</tr>
<tr>
<td><strong>distributivity</strong></td>
<td><em><strong>a(u + v) = au + av</strong></em></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><strong>spatial vectors</strong></td>
<td><strong>vectors</strong> in an <strong>n</strong>-<strong>dimensional</strong> <strong>vector</strong> <strong>space</strong></td>
</tr>
<tr>
<td><strong>vectorization</strong></td>
<td>turns a <strong>matrix</strong> into a <strong>vector</strong> so that an <strong><em>n x m</em> matrix</strong> will <strong>produce</strong> a <strong><em>n*m</em></strong> length <strong>vector</strong></td>
</tr>
<tr>
<td><strong>submatrix</strong></td>
<td>a grouped <strong>subset</strong> of a <strong>matrix</strong></td>
</tr>
<tr>
<td><strong>block matrix</strong></td>
<td>a subset of <strong>non</strong>-<strong>overlapping</strong> <strong>submatrices</strong></td>
</tr>
<tr>
<td><strong>determinant</strong></td>
<td><p>the product of the eigenvectors of a matrix</p>
<p><img src="generated_media\DATA780_week2_notes\media\image12.png" style="width:2.40449in;height:0.56443in" /></p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th><strong>neural networks</strong></th>
<th><p><img src="generated_media\DATA780_week2_notes\media\image13.png" style="width:2.49606in;height:0.25974in" /></p>
<p><img src="generated_media\DATA780_week2_notes\media\image14.png" style="width:2.7013in;height:0.44069in" /></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>losses</strong></td>
<td><img src="generated_media\DATA780_week2_notes\media\image15.png" style="width:1.37676in;height:0.43674in" /></td>
</tr>
<tr>
<td><strong>multivariate normal pdf</strong></td>
<td><img src="generated_media\DATA780_week2_notes\media\image16.png" style="width:3.64935in;height:0.43356in" /></td>
</tr>
<tr>
<td><strong>dimensionality reduction</strong></td>
<td><p>simplifies <strong>complex</strong>, <strong>high</strong>-<strong>dimensional</strong> data by <strong>transforming</strong> it into a</p>
<p><strong>lower</strong>-<strong>dimensional</strong> space</p></td>
</tr>
<tr>
<td><strong>span of set</strong></td>
<td><p><img src="generated_media\DATA780_week2_notes\media\image17.png" style="width:1.30903in;height:0.32431in" />all the <strong>vectors</strong> obtained by <strong>linearly</strong> <strong>combining</strong> a set of vectors</p>
<p><strong>S</strong> <strong>= {v<sub>1</sub>, v<sub>2</sub>, …, v<sub>n</sub>},</strong> such that</p></td>
</tr>
<tr>
<td><strong>column span</strong></td>
<td><em><strong>colsp(A)</strong> = <strong>span({v<sub>1</sub>, v<sub>2</sub>, …, a<sub>n</sub>})</strong></em></td>
</tr>
<tr>
<td><strong>column rank</strong></td>
<td><em><strong>rank(A)</strong> = <strong>dim(colsp(A))</strong></em></td>
</tr>
<tr>
<td><strong>null space</strong></td>
<td><strong>set</strong> of all <strong>vectors</strong> <strong>x</strong> of a <strong>matrix</strong> <strong>A</strong> for which <strong>Ax = 0</strong></td>
</tr>
<tr>
<td><strong>nullity</strong></td>
<td>the <strong>dimension</strong> of the <strong>null</strong> <strong>space</strong></td>
</tr>
<tr>
<td><strong>rank-nullity relationship</strong></td>
<td><p>for <strong>matrix</strong> <em><strong>A</strong></em> with <em><strong>n</strong></em> <strong>columns</strong>:</p>
<p><em><strong>rank(A) + nullity(A) = n</strong></em></p></td>
</tr>
<tr>
<td><strong>orthonormality</strong></td>
<td><p>a set of vectors {u<sub>1</sub>, u<sub>2</sub>, …, un} is orthonormal iff:</p>
<p><img src="generated_media\DATA780_week2_notes\media\image18.png" style="width:2.74943in;height:0.43588in" /></p></td>
</tr>
<tr>
<td><strong>Kronecker delta</strong></td>
<td><p><strong>𝛿<em><sub>ij</sub> </em></strong>is a mathematical <strong>function</strong> that acts as a discrete "<strong>switch</strong>," returning <strong>1</strong></p>
<p>if its two indices <em><strong>i</strong></em> and <em><strong>j</strong></em> are the <strong>same</strong>, and <em><strong>0</strong></em> if they are <strong>different</strong></p></td>
</tr>
<tr>
<td><strong>Gram-Schmidt theorem</strong></td>
<td><p>if <strong>{v<sub>1</sub>, v<sub>2</sub>, …, v<sub>n</sub>}</strong> is a <strong>linearly</strong> <strong>independent</strong> list of <strong>vectors</strong> in an <strong>inner</strong>-<strong>product</strong></p>
<p><strong>space</strong> <strong>V,</strong> then there exists an <strong>orthonormal</strong> <strong>list</strong> <strong>{e<sub>1</sub>, e<sub>2</sub>, …, e<sub>n</sub>}</strong> of vectors <strong>V</strong></p>
<p>such that <strong>span(e<sub>1</sub>, e<sub>2</sub>, …, e<sub>n</sub>)</strong> = <strong>span(v<sub>1</sub>, v<sub>2</sub>, …, v<sub>3</sub>)</strong></p></td>
</tr>
<tr>
<td><strong>matrix inverse</strong></td>
<td><p>an <strong>n-by-n</strong> square <strong>matrix</strong> <strong>A</strong> is <strong>invertible</strong>, if there exists an <strong>n-by-n</strong> square</p>
<p><strong>matrix</strong> <strong>B</strong> such that <strong>AB = BA = I<sub>n</sub></strong> where In denotes the <strong>n-by-n</strong> identity matrix</p></td>
</tr>
<tr>
<td><strong>matrix inverse equivalent statements</strong></td>
<td><p>Let <strong>A</strong> be a square <strong>matrix</strong></p>
<ul>
<li><p>there is an <em><strong>n-by-n</strong></em> matrix <strong>B</strong> such that <em><strong>AB = I<sub>n</sub> = BA</strong></em></p></li>
<li><p>matrix <strong>A</strong> has a <strong>left</strong> <strong>inverse</strong> and a <strong>right</strong> <strong>inverse</strong>, in which case <strong>both</strong></p></li>
</ul>
<p>left and right <strong>inverses</strong> <strong>exist</strong> and <em><strong>B = C = A<sup>-1</sup></strong></em></p>
<ul>
<li><p>A has full rand; that is, rank A = n</p></li>
<li><p>A is invertible, that is, A has an inverse, is nonsingular, and is</p></li>
</ul>
<p>nondegenerate</p></td>
</tr>
<tr>
<td colspan="2"><table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Probability and Statistics</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td><strong>discrete distribution</strong></td>
<td><p>describes the <strong>probabilities</strong> of <strong>outcomes</strong> for <strong>discrete</strong> random <strong>variables</strong></p>
<p>where each <strong>outcome</strong> has a specific <strong>probability</strong> between <strong>0 and 1</strong> and all</p>
<p>probabilities <strong>sum</strong> to <strong>1</strong></p>
<p><a href="https://en.wikipedia.org/wiki/Probability_distribution">https://en.wikipedia.org/wiki/Probability_distribution</a></p></td>
</tr>
<tr>
<td><strong>continuous distribution</strong></td>
<td><p>describes <strong>probability</strong> for <strong>variables</strong> that can take <strong>any</strong> <strong>value</strong> within a <strong>range</strong></p>
<p><a href="https://en.wikipedia.org/wiki/Probability_distribution">https://en.wikipedia.org/wiki/Probability_distribution</a></p></td>
</tr>
<tr>
<td><strong>discrete random variable</strong></td>
<td><p>a random <strong>variable</strong> that has a <strong>countable</strong> range and <strong>assumes</strong> each <strong>value</strong></p>
<p>in this <strong>range</strong> with a <strong>positive</strong> <strong>probability</strong></p>
<p><a href="https://gwthomas.github.io/docs/math4ml.pdf">https://gwthomas.github.io/docs/math4ml.pdf</a></p></td>
</tr>
<tr>
<td><strong>continuous random variable</strong></td>
<td><p>a random <strong>variable</strong> that has an <strong>uncountable</strong> range and <strong>assumes</strong> each</p>
<p><strong>value</strong> in this <strong>range</strong> with <strong>probability</strong> <strong>zero</strong></p>
<p><a href="https://gwthomas.github.io/docs/math4ml.pdf">https://gwthomas.github.io/docs/math4ml.pdf</a></p></td>
</tr>
<tr>
<td><strong>probability mass function</strong></td>
<td><p>gives the <strong>probability</strong> that a <strong>discrete</strong> random <strong>variable</strong> is exactly <strong>equal</strong> to a</p>
<p>specific <strong>value</strong></p>
<p><img src="generated_media\DATA780_week2_notes\media\image19.png" style="width:1.57698in;height:0.58173in" /> <img src="generated_media\DATA780_week2_notes\media\image20.png" style="width:1.79008in;height:0.42621in" /></p>
<p>https://en.wikipedia.org/wiki/Probability_mass_function#:~:text=In%%20and%20statistics%2C%20a</p>
<p><a href="https://en.wikipedia.org/wiki/Probability_mass_function#:~:text=In%20probability%20and%20statistics%2C%20a,mass%20is%20called%20the%20mode">,mass%20is%20called%20the%20mode</a>.</p></td>
</tr>
<tr>
<td><strong>probability density function</strong></td>
<td><p>describes the <strong>likelihood</strong> of a <strong>continuous</strong> random <strong>variable</strong> falling <strong>within</strong></p>
<p>specific <strong>range</strong>, represented as a <strong>curve</strong> where the total <strong>area</strong> under it <strong>equals</strong></p>
<p><strong>1</strong>, and the <strong>area</strong> over an interval <strong>gives</strong> the <strong>probability</strong></p>
<p><a href="https://en.wikipedia.org/wiki/Probability_density_function#:~:text=In%20probability%20theory%2C">https://en.wikipedia.org/wiki/Probability_density_function#:~:text=In%20probability%20theory%2C</a></p>
<p>%20a%20probability,possible%20values%20to%20begin%20with.</p></td>
</tr>
<tr>
<td><strong>joint distribution</strong></td>
<td><p>a <strong>distribution</strong> over some <strong>combination</strong> of several random <strong>variables</strong></p>
<p><a href="https://gwthomas.github.io/docs/math4ml.pdf">https://gwthomas.github.io/docs/math4ml.pdf</a></p></td>
</tr>
<tr>
<td><strong>independence</strong></td>
<td><p>the likelihood of one random variable X<sub>i</sub> is not a condition of X<sub>j</sub></p>
<p><img src="generated_media\DATA780_week2_notes\media\image21.png" style="width:1.55655in;height:0.43369in" /></p></td>
</tr>
<tr>
<td><strong>Bayes Rule</strong></td>
<td><p>connects <strong>conditionals</strong> in one <strong>direction</strong> to <strong>conditionals</strong> in another <strong>direction</strong></p>
<p><img src="generated_media\DATA780_week2_notes\media\image22.png" style="width:2.09669in;height:0.59692in" /></p></td>
</tr>
<tr>
<td><strong>Bayes Theorem</strong></td>
<td><img src="generated_media\DATA780_week2_notes\media\image23.png" style="width:5.08986in;height:2.10325in" /></td>
</tr>
<tr>
<td><strong>conditional likelihood</strong></td>
<td><p>the <strong>probability</strong> that <strong>Y</strong>, given <strong>X = x</strong></p>
<p><img src="generated_media\DATA780_week2_notes\media\image24.png" style="width:1.69799in;height:0.54069in" /></p></td>
</tr>
<tr>
<td><strong>conditional independence</strong></td>
<td><p>shows that X<sub>i</sub> is independent of X<sub>j</sub> given X<sub>k</sub></p>
<p><img src="generated_media\DATA780_week2_notes\media\image25.png" style="width:1.23429in;height:0.29214in" /></p>
<p><img src="generated_media\DATA780_week2_notes\media\image26.png" style="width:3.24995in;height:0.30659in" /></p></td>
</tr>
<tr>
<td><strong>parameters</strong></td>
<td>list of specific values needed to calculate a parametric distribution</td>
</tr>
<tr>
<td><strong>parametric distributions</strong></td>
<td><p>calculated probability given a list of parametric values</p>
<p><img src="generated_media\DATA780_week2_notes\media\image27.png" style="width:2.17595in;height:0.34118in" /></p></td>
</tr>
<tr>
<td><strong>parametric families</strong></td>
<td><p>all the possible distributions that can be calculated by adjusting parametric</p>
<p>values. some examples of parametric families:</p>
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr>
<th><p>normal</p>
<p>(Gaussian)</p></th>
<th><img src="generated_media\DATA780_week2_notes\media\image28.png" style="width:2.46018in;height:0.44179in" /></th>
</tr>
</thead>
<tbody>
<tr>
<td>truncated normal</td>
<td><img src="generated_media\DATA780_week2_notes\media\image29.png" style="width:2.99954in;height:0.55641in" /></td>
</tr>
<tr>
<td>multivariate normal</td>
<td><img src="generated_media\DATA780_week2_notes\media\image30.png" style="width:3.27126in;height:0.46867in" /></td>
</tr>
<tr>
<td>logistic</td>
<td><img src="generated_media\DATA780_week2_notes\media\image31.png" style="width:2.4838in;height:0.61963in" /></td>
</tr>
<tr>
<td>beta</td>
<td><img src="generated_media\DATA780_week2_notes\media\image32.png" style="width:2.49205in;height:0.486in" /></td>
</tr>
<tr>
<td><p>binomial</p>
<p>(parametric pmf)</p></td>
<td><img src="generated_media\DATA780_week2_notes\media\image33.png" style="width:2.98059in;height:0.44199in" /></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><strong>conditional distribution</strong></td>
<td><p>show the <strong>probability</strong> of <strong>outcomes</strong> for one <strong>variable</strong>, given that another <strong>variable</strong></p>
<p>is <strong>fixed</strong> at a specific <strong>value</strong> or falls within a certain <strong>category</strong>, essentially</p>
<p>focusing on a <strong>sub</strong>-<strong>population</strong></p>
<p><a href="https://www.khanacademy.org/math/ap-statistics/analyzing-categorical-ap/distributions-two-way-">https://www.khanacademy.org/math/ap-statistics/analyzing-categorical-ap/distributions-two-way-</a></p>
<p>tables/v/marginal-distribution-and-conditional-distribution#:~:text=On%20the%20other%20hand%</p>
<p>2C%20the,of%20car%20origin%20and%20color.</p></td>
</tr>
<tr>
<td><strong>marginalization</strong></td>
<td><p>the <strong>probability</strong> of the <strong>variables</strong> contained in a <strong>subset</strong> of a <strong>collection</strong> of</p>
<p>random <strong>variables</strong> is <strong>determined</strong> by <strong>integrating</strong> out additional variables</p>
<p>https://en.wikipedia.org/wiki/Marginal_distribution</p></td>
</tr>
<tr>
<td><strong>statistical expectations</strong></td>
<td><p><strong>E[X]</strong> is the long-run <strong>average</strong> <strong>outcome</strong> of a random <strong>variable</strong>, calculated as</p>
<p><strong>weighted</strong> <strong>average</strong> of its <strong>possible</strong> <strong>values</strong> where each <strong>value</strong> is <strong>weighted</strong> by its</p>
<p><strong>probability</strong></p></td>
</tr>
<tr>
<td><strong>expected value</strong></td>
<td><p>an <strong>expected</strong> value <strong>E<sub>X</sub></strong> from a random <strong>distribution</strong> <strong>p</strong> taken as a function <strong>f(X)</strong></p>
<p><img src="generated_media\DATA780_week2_notes\media\image34.png" style="width:1.28453in;height:0.28463in" /> <img src="generated_media\DATA780_week2_notes\media\image35.png" style="width:1.03686in;height:0.35472in" /></p></td>
</tr>
<tr>
<td><strong>KL Divergence</strong></td>
<td><p>a <strong>Kullback–Leibler</strong>  <strong>divergence</strong> is a statistical <strong>distance</strong>: a measure of how</p>
<p>much an <strong>approximating</strong> probability <strong>distribution</strong> <em><strong>Q</strong></em> differs from the <strong>true</strong> <strong>value</strong></p>
<p><strong>KL</strong> <strong>properties</strong>:</p>
<ol type="1">
<li><p><strong>measure</strong> of how <strong>different</strong> two probability <strong>distributions</strong> are</p></li>
<li><p><em><strong>D(p||q) ≥ 0; D(p||q)</strong></em> = 0 iff <em><strong>p = q</strong></em></p></li>
<li><p><strong>not</strong> a <strong>metric</strong>; not <strong>commutative</strong>, does not <strong>satisfy</strong> <strong>triangle</strong> <strong>equality</strong></p></li>
<li><p>the <strong>average</strong> number of <strong>bits</strong> that are <strong>wasted</strong> by <strong>encoding</strong> <strong>events</strong> from</p></li>
</ol>
<p>a <strong>distribution</strong> <em><strong>p</strong></em> with a code based on a <strong>not</strong>-<strong>quite</strong>-<strong>right</strong> <strong>distribution</strong> of <em><strong>q</strong></em></p>
<p><img src="generated_media\DATA780_week2_notes\media\image36.png" style="width:2.25433in;height:0.53797in" /></p>
<p><a href="https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence">https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence</a></p></td>
</tr>
<tr>
<td><strong>estimating expectations</strong></td>
<td><p>given samples <strong>{x<sub>1</sub>, x<sub>2</sub>, .., x<sub>n</sub>}</strong> of <strong>p</strong>, an <strong>empirical</strong> <strong>average</strong> of <strong>f(x)</strong> is calculated to</p>
<p><strong>approximate</strong> the true <strong>value</strong> of <em><strong>f(x)</strong></em></p>
<p><img src="generated_media\DATA780_week2_notes\media\image37.png" style="width:2.35829in;height:0.7279in" /></p></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**

**

| Live Session |                             |                 |
|--------------|-----------------------------|----------------:|
| Introduction |                             | **12 Jan 2026** |
| Instructor   | Rei Sanchez-Arias           |                 |
| Email        | <[REDACTED_EMAIL]>          |                 |
| Website      | <https://www.reisanar.com/> |                 |
| Office Hours | Mondays 12:00 pm to 1:00 pm |                 |
| Live Session | Monday 6:00 pm to 7:30 pm   |                 |

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 33%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Linear Algebra and Probability</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td>Look up Terms</td>
<td colspan="2"><ul>
<li><p><strong>Hessian</strong> <strong>matrix</strong></p>
<ul>
<li><p>the <strong>Hessian</strong> matrix of a <strong>scalar</strong> <strong>function</strong> of several <strong>variables</strong> describes the <strong>curvature</strong> of that function</p></li>
<li><p>by taking the <strong>determinant</strong> of the <strong>Hessian</strong> matrix at a critical point, we can <strong>test</strong> whether that <strong>point</strong> is a local <strong>min</strong>, <strong>max</strong>, or <strong>saddle</strong> point</p></li>
</ul></li>
</ul>
<blockquote>
<p><img src="generated_media\DATA780_week2_notes\media\image38.png" style="width:2.50035in;height:0.55168in" /></p>
</blockquote>
<p>https://www.mit.edu/~ashrstnv/hessian-ma</p>
<ul>
<li><p><strong>Jacobian</strong> <strong>matrix</strong></p>
<ul>
<li><p>a matrix of all the <strong>first</strong>-<strong>order</strong> partial <strong>derivatives</strong> of a <strong>vector</strong>-<strong>valued</strong> function, acting as a <strong>multivariable</strong> function’s <strong>derivative</strong>, showing how <strong>changes</strong> in input <strong>variables</strong> affect <strong>output</strong> variables locally</p></li>
<li><p>Essential for <strong>gradient</strong> <strong>descent</strong> in <strong>training</strong> neural <strong>networks</strong>, calculating <strong>sensitivity</strong>, and <strong>backpropagation</strong></p></li>
</ul></li>
</ul>
<blockquote>
<p><img src="generated_media\DATA780_week2_notes\media\image39.png" style="width:1.94472in;height:0.63445in" /></p>
</blockquote>
<p>https://math.etsu.edu/multicalc/prealpha</p>
<ul>
<li><p><strong>covariant</strong> matrix</p>
<ul>
<li><p>a <strong>square</strong> <strong>matrix</strong> giving the <strong>covariance</strong> between each <strong>pair</strong> of <strong>elements</strong> of a given <strong>random</strong> vector</p></li>
<li><p>in the <strong>matrix</strong> <strong>diagonal</strong> there are <strong>variances</strong>, i.e., the <strong>covariance</strong> of each <strong>element</strong> with <strong>itself</strong></p></li>
<li><p><strong>generalizes</strong> the notion of <strong>variance</strong> to <strong>multiple</strong> <strong>dimensions</strong></p></li>
</ul></li>
</ul>
<blockquote>
<p><em>https://ise.ncsu.edu/wp-content/uploads/sites/9/2022/01/Covariance-matrix-Wikipedia-1.pdf</em></p>
</blockquote>
<ul>
<li><p><strong>gradient</strong></p>
<ul>
<li><p>(<strong>∇f)</strong> a <strong>vector</strong> that points in the <strong>direction</strong> of the function’s <strong>steepest</strong> <strong>increase</strong> and whose <strong>magnitude</strong> represents the <strong>rate</strong> of that <strong>increase</strong></p></li>
<li><p>calculated by <strong>collecting</strong> <strong>partial</strong> <strong>derivatives</strong> into a <strong>vector</strong></p></li>
</ul></li>
</ul>
<blockquote>
<p><img src="generated_media\DATA780_week2_notes\media\image40.png" style="width:3.7922in;height:0.44798in" /></p>
</blockquote>
<p>https://byjus.com/maths/gradient/#:~:tex</p></td>
</tr>
<tr>
<td>Look up on SciKitLearn</td>
<td colspan="2"><ul>
<li><p><strong>QuadraticDiscriminantAnalysis</strong></p>
<ul>
<li><p>Quadratic Discriminant Analysis.</p></li>
<li><p>A <strong>classifier</strong> with a <strong>quadratic</strong> <strong>decision</strong> <strong>boundary</strong>, generated by <strong>fitting</strong> class <strong>conditional</strong> <strong>densities</strong> to the <strong>data</strong> and using <strong>Bayes’s</strong> <strong>rule</strong>.</p></li>
<li><p>The model <strong>fits</strong> a <strong>Gaussian</strong> <strong>density</strong> to each <strong>class</strong>.</p></li>
</ul></li>
<li><p><strong>BernoulliNB</strong></p>
<ul>
<li><p>Naive <strong>Bayes</strong> classifier for <strong>multivariate</strong> <strong>Bebrnoulli</strong> <strong>models</strong>.</p></li>
<li><p>Like <strong>MultinomialNB</strong>, this classifier is <strong>suitable</strong> for <strong>discrete</strong> <strong>data</strong>. The <strong>difference</strong> is that while <strong>MultinomialNB</strong> works with occurrence counts, <strong>BernoulliNB</strong> is designed for <strong>binbary</strong>/<strong>boolean</strong> features.</p></li>
</ul></li>
<li><p><strong>MultinomialNB</strong></p>
<ul>
<li><p>Naive <strong>Bayes</strong> classifier for <strong>multinomial</strong> <strong>models</strong>.</p></li>
<li><p>The <strong>multinomial</strong> Naive <strong>Bayes</strong> classifier is suitable for <strong>classification</strong> with <strong>discrete</strong> features (e.g., <strong>word</strong> <strong>counts</strong> for text <strong>classification</strong>). The <strong>multinomial</strong> <strong>distribution</strong> normally <strong>requires</strong> integer feature <strong>counts</strong>. However, in practice, <strong>fractional</strong> <strong>counts</strong> such as <strong>tf</strong>-<strong>idf</strong> may also work.</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Class Work Exercises</td>
</tr>
<tr>
<td>Class Work Notebooks</td>
<td colspan="2" style="text-align: center;"><img src="generated_media\DATA780_week2_notes\media\image41.emf" /> <img src="generated_media\DATA780_week2_notes\media\image42.emf" /> <img src="generated_media\DATA780_week2_notes\media\image43.emf" /></td>
</tr>
<tr>
<td>CW Notebook Solutions</td>
<td colspan="2" style="text-align: center;"><img src="generated_media\DATA780_week2_notes\media\image44.emf" /> <img src="generated_media\DATA780_week2_notes\media\image45.emf" /> <img src="generated_media\DATA780_week2_notes\media\image46.emf" /></td>
</tr>
<tr>
<td>Solution</td>
<td colspan="2" style="text-align: center;"><strong>DATA780\Week2\&lt;fname_lname&gt;_DATA780_week2_ProbStatML.docx"</strong></td>
</tr>
</tbody>
</table>
