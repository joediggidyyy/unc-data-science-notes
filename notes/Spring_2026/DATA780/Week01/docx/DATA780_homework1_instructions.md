> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_homework1_instructions.pdf](../DATA780_homework1_instructions.pdf)
> - DOCX: [DATA780_homework1_instructions.docx](DATA780_homework1_instructions.docx)

---

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 4%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 1%" />
<col style="width: 8%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr>
<th colspan="3">Homework 1</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4">Overview</td>
<td colspan="3" style="text-align: right;"><em>Due: 21 Jan 2026</em></td>
</tr>
<tr>
<td colspan="7"><ul>
<li><p>Unless otherwise directed, please derive and show your work.</p></li>
<li><p>Do not try to search directly for the answers.</p></li>
<li><p>You may speak to other students about the assignment at a high-level (e.g. sharing related references/slides).</p></li>
<li><p>However, sharing complete or partial answers is strictly prohibited.</p></li>
<li><p>Please see the <em>UNC Student <a href="https://catalog.unc.edu/policies-procedures/student-code-conduct/">_Code of Conduct_</a></em> for additional details on maintaining academic integrity</p></li>
</ul></td>
</tr>
<tr>
<td colspan="6">Part 1: Documentation of ML Implementation</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="7"><ul>
<li><p>For this problem you are welcome to choose documentation from any programming language (<em>R, Python, Julia, MATLAB</em>, etc.) in which an implementation of a machine learning (ML) method is discussed</p></li>
<li><p>During the first units of the course, you have been exploring a variety of concepts from calculus, probability, statistics, and linear algebra that support multiple methods in machine learning methods and algorithms</p></li>
<li><p>In this problem you are asked to compare documentation from two different implementations of any ML method or algorithm related to any of the fundamental concepts discussed in <em>Units 1 and 2</em></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol type="A">
<li><p>(10 pts)</p></li>
</ol></td>
<td colspan="5"><ul>
<li><p><strong>Include</strong> a direct <strong>link</strong> to the <strong>documentation</strong> for the <strong>two</strong> <strong>implementations</strong> you selected</p></li>
<li><p>These two <strong>implementations</strong> may come from <strong>different</strong> programming <strong>languages</strong>, or <strong>different</strong> library/<strong>packages</strong> in the <strong>same</strong> programming <strong>language</strong></p></li>
<li><p>Please <strong>summarize</strong> in <strong>2</strong> <strong>–</strong> <strong>3</strong> <strong>sentences</strong> some high-level <strong>differences</strong> that you notice between the <strong>two</strong> <strong>implementations</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol start="2" type="A">
<li><p>(6 pts)</p></li>
</ol></td>
<td colspan="5"><ul>
<li><p>Frem the <strong>method</strong> you selected in <strong>part</strong> ‘<strong>A’</strong>, list a research <strong>article</strong> from <strong>any</strong> <strong>domain</strong>) in which the <strong>ML</strong> <strong>method</strong> of your choice has <strong>been</strong> <strong>used</strong></p></li>
<li><p>Include <strong>title</strong>, <strong>authors</strong>, <strong>abstract</strong>, and a direct <strong>link</strong> to the specific <strong>article</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="6">Part 2: Eigendecomposition</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="7"><ul>
<li><p>For this problem you can create a sample matrix (following the stated properties) of your choice to solve problems numerically, OR write down the mathematical expression(s) for solutions/proofs in each case</p></li>
<li><p>Suppose that <em>A ∈ R<sup>nxn</sup></em> can be written down as <em>A = QDQ<sup>T</sup></em> where <em>D ∈ R<sup>nxn</sup></em> is a diagonal matrix and <em>Q<sup>-1</sup> = Q<sup>T</sup></em></p></li>
<li><p>If you want to solve this problem computationally, you could use this sample matrix:</p></li>
</ul>
<p><img src="generated_media\DATA780_homework1_instructions\media\image1.png" style="width:2.02112in;height:0.89596in" /></p>
<ul>
<li><p>Confirm that the matrix decomposition below returns <em>A</em> (that is, verify that the product of <em>QDQ<sup>T</sup></em>:</p></li>
</ul>
<p><img src="generated_media\DATA780_homework1_instructions\media\image2.png" style="width:5.30282in;height:1.07307in" /></p></td>
</tr>
<tr>
<td colspan="2"><ol type="A">
<li><p>(8 pts)</p></li>
</ol></td>
<td colspan="5"><ul>
<li><p>show that <em><strong>A</strong></em> is <strong>symmetric</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol start="2" type="A">
<li><p>(8 pts)</p></li>
</ol></td>
<td colspan="5"><ul>
<li><p>show that <strong>QDQ<sup>T</sup></strong> is the <strong>Eigendecomposition</strong> of <em><strong>A</strong></em></p></li>
<li><p>That is, <strong>show</strong> that the <strong>columns</strong> of <em><strong>Q</strong></em> are <strong>eigenvectors</strong> of <em><strong>A</strong></em> (and <strong>specify</strong> corresponding <strong>eigenvalues</strong>)</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol start="3" type="A">
<li><p>(8 pts)</p></li>
</ol></td>
<td colspan="5"><ul>
<li><p>write out the <strong>Eigendecomposition</strong> of <em><strong>A + λI</strong></em> for some <em><strong>λ &gt; 0</strong></em></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol start="4" type="A">
<li><p>(8 pts)</p></li>
</ol></td>
<td colspan="5"><ul>
<li><p><strong>read</strong> the <strong>data</strong> stored in the <a href="https://raw.githubusercontent.com/reisanar/datasets/refs/heads/master/Advertising.csv"><em>Advertising,csv</em></a> in a matrix <em><strong>B</strong></em></p></li>
<li><p><strong>compute</strong> <em><strong>B<sup>T</sup>B</strong></em> and <strong>report</strong> any two <strong>properties</strong> of the resulting <strong>matrix</strong> (e.g. <strong>eigenvalues,</strong> trace<strong>, determinant,</strong> singular value <strong>decomposition,</strong> largest eigenvalue<strong>, etc.)`</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="6">Part 3: Probability of Statistics Basics</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><ol type="A">
<li><p>(12pts)</p></li>
</ol></td>
<td colspan="5"><ul>
<li><p><strong>assume</strong> that you are <strong>tasked</strong> with <strong>building</strong> a simple <strong>binary</strong> <strong>classifier</strong> that will eventually <strong>predict</strong> whether a user will <strong>click</strong> on an <strong>ad</strong> (<em><strong>yes/no</strong></em>)</p></li>
<li><p>right now, you do <strong>not</strong> have a <strong>model</strong> but only <strong>historical</strong> <strong>click</strong> rates.</p></li>
<li><p>suppose that the <strong>historical</strong> <strong>click</strong>-through <strong>rate</strong> (<em><strong>CTR</strong></em>) is <em><strong>0.3</strong></em></p></li>
<li><p>in <strong>this</strong> <strong>problem</strong> you will <strong>simulate</strong> user <strong>behavior</strong> and <strong>observe</strong> how the <strong>estimated</strong> <em><strong>CTR</strong></em> <strong>varies</strong> across <strong>samples</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol type="i">
<li></li>
</ol></td>
<td colspan="5"><ul>
<li><p><strong>simulate</strong> <em><strong>1000</strong></em> <strong>users</strong> using the <em><strong>binomial</strong></em> <em><strong>distribution</strong></em></p></li>
<li><p>each <strong>user</strong> has a <em><strong>0.3</strong></em> <strong>probability</strong> of <strong>clicking</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol start="2" type="i">
<li></li>
</ol></td>
<td colspan="5"><ul>
<li><p>now, <strong>simulate</strong> <em><strong>1000</strong></em> <strong>experiments</strong>, each with <em><strong>100</strong></em> <strong>users</strong></p></li>
<li><p><strong>plot</strong> the <strong>distribution</strong> of <strong>estimated</strong> <em><strong>CTRs</strong></em> to see the <strong>variability</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol start="3" type="i">
<li></li>
</ol></td>
<td colspan="5"><ul>
<li><p><strong>comment</strong> on your <strong>results</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol start="2" type="A">
<li><p>(12 pts)</p></li>
</ol></td>
<td colspan="5"><ul>
<li><p><strong>suppose</strong> that a medical <strong>test</strong> for a <strong>disease</strong> has the <strong>following</strong> <strong>characteristics</strong>:</p>
<ul>
<li><p><strong>sensitivity</strong> (true <strong>positive</strong> rate): <em><strong>P(test+|disease+) = 0.95</strong></em></p></li>
<li><p><strong>specificity</strong> (true <strong>negative</strong> rate): <em><strong>P(test-|disease-) = 0.90</strong></em></p></li>
<li><p><strong>prevalence</strong>: <em><strong>P(disease+) = 0.02</strong></em></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol type="i">
<li></li>
</ol></td>
<td colspan="5"><ul>
<li><p><strong>calculate</strong> the <strong>probability</strong> that a person <strong>has</strong> the <strong>disease</strong> given that they <strong>test</strong> <strong>positive</strong>: <em><strong>P(disease+|test-)</strong></em></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol start="2" type="i">
<li></li>
</ol></td>
<td colspan="5"><ul>
<li><p><strong>calculate</strong> the <strong>probability</strong> that a <strong>person</strong> does not have the <strong>disease</strong> given that they test <strong>negative</strong> <em><strong>P(disease-|test-)</strong></em></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol start="3" type="i">
<li></li>
</ol></td>
<td colspan="5"><ul>
<li><p><strong>simulate</strong> a <strong>population</strong> of <em><strong>100,000</strong></em> people and <strong>empirically</strong> <strong>estimate</strong> these probabilities</p></li>
<li><p><strong>compare</strong> your <strong>results</strong> to the theoretical <strong>calculations</strong></p></li>
<li><p><em>the <strong>theoretical</strong> and <strong>empirical</strong> <strong>results</strong> should <strong>closely</strong> <strong>match</strong></em></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"><ol start="3" type="A">
<li><p>(8 pts)</p></li>
</ol></td>
<td colspan="5"><ul>
<li><p>let <em><strong>N( x | μ, ∑ ) = ( 2π )<sup>-k/2</sup> det( ∑ )<sup>-1/2</sup> exp( -1/2 ( x - μ )<sup>T</sup> ∑<sup>-1</sup> ( x – μ ))</strong></em> be the <strong>multivariate</strong> <strong>normal</strong> for <em><strong>x<sup>2</sup> ∈ R<sup>d</sup></strong></em> with <strong>mean</strong> <em><strong>μ</strong></em> and <strong>covariance</strong> <em><strong>∑</strong></em></p></li>
<li><p><strong>suppose</strong> further that <em><strong>∑</strong></em> is a <strong>diagonal</strong></p></li>
<li><p>show, for <strong>diagonal</strong> <strong>covariance</strong>, that <em><strong>N ( x | μ, ∑ )</strong></em> is an <strong>independent</strong> <strong>distribution</strong> over the <strong>dimensions</strong> of <em><strong>x</strong></em></p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">if solving the problem numerically</td>
<td colspan="5"><ul>
<li><p>Define the <strong>multivariate</strong> <strong>normal</strong> <strong>distribution</strong> with a <strong>diagonal</strong> <strong>covariance</strong> matrix using <em><strong>`np.diag()`</strong></em></p></li>
<li><p>Show that the <strong>distribution</strong> is <strong>independent</strong> over the <strong>dimensions</strong> by <strong>demonstrating</strong> that the <strong>joint</strong> <strong>PDF</strong> can be <strong>written</strong> as the <strong>product</strong> of the <strong>individual</strong> <strong>PDFs</strong> for each <strong>dimension</strong></p></li>
<li><p><strong>Create</strong> a <strong>function</strong> to <strong>calculate</strong> the <strong>multivariate</strong> <strong>normal</strong> <strong>PDF</strong> and use a <strong>loop</strong> to <strong>evaluate</strong> it for different <strong>values</strong> of the <strong>variable</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Part 4: Gradients</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td><ol type="A">
<li><p>(8 pts)</p></li>
</ol></td>
<td colspan="6"><ul>
<li><p>suppose there is a function <em><strong>ƒ (θ)</strong></em> with gradient <em><strong>∇ <sub>0</sub> ƒ</strong></em></p></li>
<li><p>based on some current <strong>value</strong> of the <strong>input</strong>, <em><strong>θ<sub>0</sub>,</strong> what is</em> an update that will <strong>yield</strong> a <em><strong>θ<sub>1</sub></strong></em> such that <em><strong>ƒ (θ<sub>0</sub>) ≥ ƒ (θ<sub>1</sub>)</strong></em>?</p></li>
</ul></td>
</tr>
<tr>
<td><ol start="2" type="A">
<li><p>(4 pts)</p></li>
</ol></td>
<td colspan="6"><ul>
<li><p>using ‘<em><strong>A’</strong></em>, <strong>derive</strong> an iterative <strong>algorithm</strong> to <strong>minimize</strong> <em><strong>ƒ</strong> with</em> respect <em>to <strong>θ</strong></em> when starting <em>with <strong>θ<sub>0</sub></strong></em></p></li>
</ul></td>
</tr>
<tr>
<td><ol start="3" type="A">
<li><p>(12 pts</p></li>
</ol></td>
<td colspan="6"><ul>
<li><p>consider the code-block below</p></li>
<li><p>use the <strong>algorithm</strong> in ‘<em><strong>B’</strong></em> to minimize <em><strong>ƒ (θ) = || θ||<sup>2</sup><sub>2</sub> – 2v<sup>T</sup> θ</strong></em>, where <em><strong>θ ∈ R<sup>3</sup></strong></em> and <em><strong>v = [ 0.2, 0.1, 0.3 ]<sup>T</sup></strong></em></p></li>
</ul></td>
</tr>
<tr>
<td></td>
<td colspan="6" style="text-align: center;"><p><img src="generated_media\DATA780_homework1_instructions\media\image3.png" style="width:5.03195in;height:1.39603in" /></p>
<p><img src="generated_media\DATA780_homework1_instructions\media\image4.png" style="width:5.07362in;height:1.31268in" /></p>
<p><img src="generated_media\DATA780_homework1_instructions\media\image5.png" style="width:4.95903in;height:0.78136in" /></p></td>
</tr>
</tbody>
</table>
