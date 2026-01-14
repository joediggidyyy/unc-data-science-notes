> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week1_notes.pdf](../DATA780_week1_notes.pdf)
> - DOCX: [DATA780_week1_notes.docx](DATA780_week1_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr>
<th colspan="4">An Introduction to Statistical Learning</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">What this is</td>
<td colspan="3" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>the following are notes from Ch1 from ISLRv2</p></li>
<li><p>Chapter 1: Introduction</p></li>
<li><p>pp 1-6</p></li>
<li><p>**/Spring_2026/DATA780/Unit1/ISLRv2_corrected_June_2023.pdf</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">An Overview of Statistical Learning</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5">Statistical learning is a collection of methods used to understand, discover patterns, and make predictions in data and is widely used in business, medicine, science [sic], and public policy applications.`</td>
</tr>
<tr>
<td colspan="5">What is Statistical Learning?</td>
</tr>
<tr>
<td>Supervised Learning</td>
<td colspan="4"><ul>
<li><p>used to <strong>predict</strong> or <strong>estimate</strong> the <strong>output</strong> (Y) using <strong>inputs</strong> (X)</p></li>
<li><p>Common tasks include predicting <strong>numerical</strong> and <strong>categorical</strong> values and classifications</p></li>
</ul></td>
</tr>
<tr>
<td>Unsupervised Learning</td>
<td colspan="4"><ul>
<li><p>only <strong>inputs</strong> are observed</p></li>
<li><p>there is <strong>no</strong> <strong>output</strong> variable</p></li>
<li><p>used to <strong>discover</strong> <strong>structure</strong> or <strong>relationships</strong> in the data</p></li>
<li><p>common tasks include <strong>clustering</strong> and <strong>dimension</strong> <strong>reduction</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Regression Example: Wage Data</td>
</tr>
<tr>
<td>Goal</td>
<td colspan="4"><ul>
<li><p><strong>predict</strong> a man’s <strong>wage</strong> using information such as age, education level, and calendar year</p></li>
</ul></td>
</tr>
<tr>
<td>Key Observations</td>
<td colspan="4"><ul>
<li><p>wages <strong>increase with age</strong> up to age 60, <strong>then decreases</strong></p></li>
<li><p>wages <strong>increase</strong> <strong>over</strong> <strong>time</strong></p></li>
<li><p>higher <strong>education</strong> is associated with <strong>higher</strong> <strong>wages</strong></p></li>
<li><p>there is <strong>substantial</strong> <strong>variability</strong> in wages</p></li>
</ul></td>
</tr>
<tr>
<td>Insights</td>
<td colspan="4"><ul>
<li><p>no single variable predicts wage well on its own</p></li>
<li><p>combining <strong>multiple variables improves prediction</strong></p></li>
<li><p>relationships can be non-linear (especially with age)</p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Classification Example: Stock Market Data</td>
</tr>
<tr>
<td>Goal</td>
<td colspan="4"><ul>
<li><p><strong>predict trends</strong> in stock market</p></li>
</ul></td>
</tr>
<tr>
<td>Data Used</td>
<td colspan="4"><ul>
<li><p>daily percentage changes in the S&amp;P 500</p></li>
<li><p>past 5 days of returns</p></li>
</ul></td>
</tr>
<tr>
<td>Key Considerations</td>
<td colspan="4"><ul>
<li><p>the <strong>output</strong> is <strong>categorical</strong>, not numerical</p></li>
<li><p>past returns show very weak predictive power</p></li>
</ul></td>
</tr>
<tr>
<td>Results</td>
<td colspan="4"><ul>
<li><p>prediction accuracy of ~60% using statistical learning methods</p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Unsupervised Learning Example: Gene Expression</td>
</tr>
<tr>
<td>Goal</td>
<td colspan="4"><ul>
<li><p>identify groups of similar cancer cell lines using gene expression data</p></li>
</ul></td>
</tr>
<tr>
<td>Data Used</td>
<td colspan="4"><ul>
<li><p>64 cancer cell lines</p></li>
<li><p>6,830 gene measurements per cell line</p></li>
<li><p>no output variable</p></li>
</ul></td>
</tr>
<tr>
<td>Approach</td>
<td colspan="4"><ul>
<li><p>Reduce thousands of variables to a small number (dimension reduction)</p></li>
<li><p>visualize the data in two dimensions</p></li>
<li><p>look for natural groupings/clusters</p></li>
</ul></td>
</tr>
<tr>
<td>Result</td>
<td colspan="4"><ul>
<li><p>cell lines form visible clusters</p></li>
<li><p>clusters tend to correspond to actual cancer types</p></li>
<li><p>cancer type information was not used to form the clusters</p></li>
<li><p>evidence provided that unsupervised learning can uncover real structure</p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Supervised Learning: A Brief History</td>
</tr>
<tr>
<td>Early Developments</td>
<td colspan="4"><ul>
<li><p>1800s: least squares &gt;&gt; linear regression</p></li>
<li><p>1936: linear discriminant analysis</p></li>
<li><p>1940s: logistic regression</p></li>
<li><p>1970s: generalized linear models</p></li>
</ul></td>
</tr>
<tr>
<td>Major Advancements</td>
<td colspan="4"><ul>
<li><p>early methods were restricted by computational limits</p></li>
<li><p>1980s onward computing power enabled non-linear methods</p></li>
</ul></td>
</tr>
<tr>
<td>Modern Era</td>
<td colspan="4"><ul>
<li><p>statistical learning is a distinct field</p></li>
<li><p>methods have become widely available through tools such as R</p></li>
<li><p>expanded far beyond statistics and computer science</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 0%" />
<col style="width: 3%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="3">NumPy: Broadcasting</th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">What this is</td>
<td colspan="3" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>the following are notes from the NumPy v2.4 manual</p></li>
<li><p>https://numpy.org/doc/stable/user/basics.broadcasting.html</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">An Overview of NumPy Broadcasting</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td>What Broadcasting is</td>
<td colspan="4"><ul>
<li><p>a rule NumPy uses to let you do <strong>arithmetic</strong> on <strong>arrays</strong> with <strong>different</strong> <strong>shapes</strong></p></li>
</ul></td>
</tr>
<tr>
<td>What Broadcasting does</td>
<td colspan="4"><ul>
<li><p>when NumPy sees two arrays that do <strong>not</strong> <strong>match</strong> <strong>shape</strong> exactly it attempts to <strong>expand</strong> the <strong>smaller</strong> <strong>array</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Result</td>
<td colspan="4"><ul>
<li><p>NumPy <strong>avoids</strong> <strong>loops</strong> and unnecessary data copying, making array math <strong>fast</strong> and <strong>efficient</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Why Broadcasting Matters</td>
</tr>
<tr>
<td>NumPy without Broadcasting</td>
<td colspan="4"><ul>
<li><p>normally NumPy does element-by-element operations which traditionally only work with array with the same shape</p></li>
<li><p><img src="generated_media\DATA780_week1_notes\media\image1.png" style="width:2.91707in;height:0.77094in" /></p></li>
</ul></td>
</tr>
<tr>
<td>NumPy with Broadcasting</td>
<td colspan="4"><ul>
<li><p>let’s NumPy <strong>relax</strong> the <strong>constraints</strong></p></li>
<li><p>facilitates <strong>scalar</strong> and <strong>non-conformable</strong> array arithmetic</p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Scalar Multiplication Example</td>
</tr>
<tr>
<td>Problem</td>
<td colspan="4"><ul>
<li><p>a problem requires <strong>multiplying</strong> a 3 x 1 array by a <strong>scalar</strong></p></li>
<li><p><img src="generated_media\DATA780_week1_notes\media\image2.png" style="width:2.93791in;height:0.87512in" /></p></li>
</ul></td>
</tr>
<tr>
<td>Solution</td>
<td colspan="4"><ul>
<li><p>NumPy conceptually “<strong>stretches”</strong> ‘b’ to <strong>match</strong> the shape of a</p></li>
<li><p>this is achieved <strong>without</strong> <strong>duplicating</strong> the scalar in <strong>memory</strong></p></li>
<li><p>essentially makes the operation:</p></li>
<li><p><img src="generated_media\DATA780_week1_notes\media\image3.png" style="width:2.84415in;height:0.46882in" /></p></li>
</ul></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr>
<th colspan="2">How Broadcasting Works</th>
</tr>
</thead>
<tbody>
<tr>
<td>Rules</td>
<td><ul>
<li><p>compare shapes from the <strong>trailing</strong> (rightmost) <strong>dimension</strong></p></li>
<li><p>two dimensions are <strong>compatible</strong> if</p>
<ul>
<li><p>they are <strong>equal</strong></p></li>
<li><p>one of them <strong>equals</strong> ‘<strong>1</strong>‘</p></li>
</ul></li>
<li><p>if <strong>neither</strong> condition is <strong>true</strong></p>
<ul>
<li><p>NumPy raises ‘<strong>ValueError’</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>What it does</td>
<td><ul>
<li><p>If <strong>one</strong> <strong>array</strong> has <strong>fewer</strong> <strong>dimensions</strong>, NumPy <strong>treats</strong> missing dimension sizes <strong>as ‘1’</strong></p></li>
<li><p>If a <strong>dimension</strong> is <strong>‘1’</strong> in one array but <strong>larger</strong> in the <strong>other</strong>, NumPy <strong>expands</strong> that dimension</p></li>
</ul></td>
</tr>
<tr>
<td>Resulting Array</td>
<td><ul>
<li><p>the resulting shape has the <strong>maximum</strong> number of <strong>dimensions</strong> from the <strong>input</strong> <strong>arrays</strong></p></li>
<li><p>each <strong>axis</strong> is the <strong>size</strong> of the <strong>larger</strong> of the two</p></li>
<li><p>if shapes <strong>cannot</strong> be <strong>aligned</strong> NumPy raises an <strong>error</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Examples</td>
<td><ul>
<li><p>NumPy <strong>expands</strong> the dimensions of ‘<strong>B</strong>’ so it is compatible with ‘A’</p></li>
<li><p><img src="generated_media\DATA780_week1_notes\media\image4.png" style="width:3.3338in;height:0.85429in" /></p></li>
<li><p>when operation is with scalar and array ‘<strong>b</strong>’ is <strong>broadcasted</strong> into ‘a’</p></li>
<li><p><img src="generated_media\DATA780_week1_notes\media\image5.png" style="width:3.84429in;height:0.95847in" /></p></li>
<li><p>when operation is with 1-D and 2-D arrays</p></li>
<li><p><img src="generated_media\DATA780_week1_notes\media\image6.png" style="width:3.76094in;height:2.09404in" /></p></li>
<li><p>a set of arrays are <strong>broadcast</strong>-<strong>able</strong> if all can be expanded to a <strong>common</strong> <strong>shape</strong> that <strong>meets</strong> the <strong>rules</strong></p></li>
<li><p><img src="generated_media\DATA780_week1_notes\media\image7.png" style="width:5.13613in;height:0.54174in" /></p></li>
<li><p>scalar shape ‘()’ acts like a shape of <strong>ones</strong></p></li>
<li><p>the <strong>1-D array</strong> ‘(6,) is treated like <strong>(1, 6)</strong></p></li>
<li><p>all <strong>arrays</strong> are conceptually <strong>expanded</strong> to (<strong>5, 6</strong>)</p></li>
<li><p>this is all achieved with <strong>minimal</strong> <strong>memory</strong> use by NumPy</p></li>
</ul></td>
</tr>
<tr>
<td>When Broadcasting Fails</td>
<td><ul>
<li><p>when two <strong>arrays</strong> do <strong>not</strong> satisfy the <strong>rules</strong> and broadcasting is <strong>not</strong> <strong>possible</strong> NumPy shows a broadcasting <strong>error</strong></p></li>
<li><p><img src="generated_media\DATA780_week1_notes\media\image8.png" style="width:5.56328in;height:0.6876in" /></p></li>
</ul></td>
</tr>
<tr>
<td><p>Broadcasting</p>
<p>Summary</p></td>
<td><ul>
<li><p>let’s NumPy <strong>combine</strong> arrays of <strong>different</strong> shapes avoiding loops and memory bloat</p></li>
<li><p><strong>compares</strong> shapes from <strong>trailing</strong> dimensions</p></li>
<li><p>dimensions must either <strong>match</strong> or be ‘<strong>1</strong>’</p></li>
<li><p>if conditions <strong>not</strong> <strong>met</strong> NumPy raises an <strong>error</strong></p></li>
</ul></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 23%" />
<col style="width: 49%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Async Materials</th>
<th style="text-align: right;"></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Machine Learning</td>
<td colspan="3"><img src="generated_media\DATA780_week1_notes\media\image9.png" style="width:5.29091in;height:4.42729in" /></td>
</tr>
<tr>
<td colspan="4">Machine Learning Terminology</td>
</tr>
<tr>
<td>Inputs to Models</td>
<td colspan="3"><ul>
<li><p><strong>features</strong> – the individual <strong>measurable</strong> <strong>properties</strong> in a model</p></li>
<li><p><strong>covariates –</strong> input variables that are <strong>statistically</strong> <strong>related</strong> to the output</p></li>
<li><p><strong>dimensions</strong> – <strong>number</strong> of input variables or <strong>axes</strong> in a feature space</p></li>
<li><p><strong>parameters –</strong> learnable <strong>variables</strong> <strong>needed</strong> to compute the model’s <strong>output</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Contents of a Dataset</td>
<td colspan="3" rowspan="2"><ul>
<li><p><strong>instances</strong> – a single <strong>unit</strong> <strong>of</strong> <strong>observation</strong> in a dataset</p></li>
<li><p><strong>samples</strong> – a <strong>single</strong> observed <strong>data</strong> <strong>point</strong></p></li>
<li><p><strong>examples</strong> – a <strong>training</strong> or <strong>testing</strong> data point</p></li>
</ul>
<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 27%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr>
<th><strong>Concept Type</strong></th>
<th><strong>Term</strong></th>
<th><strong>Emphasis</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">inputs</td>
<td><strong>feature</strong></td>
<td><strong>measurable</strong> input variable</td>
</tr>
<tr>
<td><strong>covariate</strong></td>
<td><strong>input</strong> related to <strong>outcome</strong></td>
</tr>
<tr>
<td><strong>dimension</strong></td>
<td><strong>number</strong> of input <strong>axes</strong></td>
</tr>
<tr>
<td rowspan="3">dataset unit</td>
<td><strong>instance</strong></td>
<td>one <strong>entity</strong> or <strong>case</strong></td>
</tr>
<tr>
<td><strong>sample</strong></td>
<td><strong>observed</strong> data point</td>
</tr>
<tr>
<td><strong>example</strong></td>
<td>labeled <strong>training</strong>/<strong>test</strong> case</td>
</tr>
</tbody>
</table>
<ul>
<li></li>
</ul></td>
</tr>
<tr>
<td>Quick Reference</td>
</tr>
<tr>
<td>Training</td>
<td colspan="3"><ul>
<li><p><strong>inference</strong> – using understood relationships to draw conclusions</p></li>
<li><p><strong>prediction</strong> – using data, machine learning, and statistical modeling to forecast future outcomes</p></li>
<li><p><strong>classification</strong> <strong>label</strong> – predefined category or class assigned to a data point correlating to output in supervised machine learning</p></li>
<li><p><strong>types of learning</strong></p>
<ul>
<li><p><strong>supervised</strong> – mapping input to output</p></li>
<li><p><strong>unsupervised</strong> – learn data characteristics</p></li>
<li><p><strong>reinforcement</strong> – learn how to interact with an environment through sequential ‘stacked’ learning</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Types of Machine Learning</td>
</tr>
<tr>
<td>Supervised Learning</td>
<td colspan="3"><ul>
<li><p><strong>inputs</strong> &gt; <strong>outputs</strong></p>
<ul>
<li><p>{example1, output1}</p></li>
<li><p>{example2, output2}</p></li>
</ul></li>
<li><p>speech &gt; text</p></li>
<li><p><strong>regression</strong></p></li>
<li><p><img src="generated_media\DATA780_week1_notes\media\image10.png" style="width:5.32706in;height:1.87813in" /></p></li>
</ul></td>
</tr>
<tr>
<td>Unsupervised Learning</td>
<td colspan="3"><ul>
<li><p>does <strong>not</strong> make use of <strong>prespecified</strong>/annotated <strong>examples</strong></p></li>
<li><p>{example1, example2, example3…}</p></li>
<li><p>{x<sub>i</sub>}<sup>n</sup><sub>i=1</sub></p></li>
<li><p><strong>clustering</strong></p>
<ul>
<li><p>attempting to <strong>discover</strong> the salient <strong>groups</strong> of the data</p></li>
</ul></li>
<li><p><strong>dimensionality</strong> <strong>reduction</strong></p>
<ul>
<li><p><strong>identifies</strong> the degrees of freedom or <strong>core</strong> <strong>descriptors</strong> of the data</p></li>
</ul></li>
<li><p><strong>generative models</strong></p>
<ul>
<li><p>given training data, generate new samples from same distribution</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Reinforcement Learning</td>
<td colspan="3"><ul>
<li><p>interact with an environment and assess the environment state to then output actions that change that state</p></li>
<li><p>predictions build on one another to maximize ‘rewards’ through iterative application of the assessment, action, change state, assess, …</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Keys to Success with Machine Learning</td>
</tr>
<tr>
<td>Three Pillars of Machine Learning</td>
<td colspan="3"><ul>
<li><p>big <strong>datasets</strong></p></li>
<li><p><strong>fast</strong> processing</p></li>
<li><p><strong>innovative</strong> methods</p></li>
</ul></td>
</tr>
<tr>
<td>Typical ML Model Lifecycle</td>
<td colspan="3"><ul>
<li><p><strong>select</strong> loss/<strong>model</strong>-<strong>type</strong> for data task</p></li>
<li><p><strong>optimize</strong> model with training <strong>data</strong></p></li>
<li><p><strong>evaluate</strong> on held-out data to <strong>validate</strong> choices</p></li>
<li><p>use with unseen <strong>future</strong> data</p></li>
</ul></td>
</tr>
<tr>
<td>Three Pillars to YOUR Success in Machine Learning</td>
<td colspan="3"><ul>
<li><p><strong>statistics</strong> and <strong>mathematics</strong></p></li>
<li><p>computer <strong>engineering</strong></p></li>
<li><p>data <strong>analytics</strong> acumen</p></li>
</ul></td>
</tr>
<tr>
<td>Philosophy: Intelligence Can Grow</td>
<td colspan="3"><img src="generated_media\DATA780_week1_notes\media\image11.png" style="width:5.78225in;height:3.52186in" /></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Mathematics Review</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Differentiation</td>
<td colspan="2"><p><strong>taking derivatives of functions</strong></p>
<p><img src="generated_media\DATA780_week1_notes\media\image12.png" style="width:3.55258in;height:1.08348in" /></p>
<p><img src="generated_media\DATA780_week1_notes\media\image13.png" style="width:5.8774in;height:3.29348in" /></p></td>
</tr>
<tr>
<td>Gradients</td>
<td colspan="2"><p><strong>derivatives that take in multiple variables and produce a real value output</strong></p>
<p><img src="generated_media\DATA780_week1_notes\media\image14.png" style="width:5.71495in;height:3.55109in" /></p>
<p><img src="generated_media\DATA780_week1_notes\media\image15.png" style="width:5.88843in;height:3.51355in" /></p></td>
</tr>
<tr>
<td>Derivatives as Approximators</td>
<td colspan="2"><img src="generated_media\DATA780_week1_notes\media\image16.png" style="width:5.87308in;height:1.66278in" /></td>
</tr>
<tr>
<td>Integration</td>
<td colspan="2"><img src="generated_media\DATA780_week1_notes\media\image17.png" style="width:5.78358in;height:3.26054in" /><img src="generated_media\DATA780_week1_notes\media\image18.png" style="width:5.84559in;height:3.45489in" /></td>
</tr>
<tr>
<td>Antiderivative</td>
<td colspan="2"><p><strong>integration and differentiation are inverse operations</strong></p>
<p><img src="generated_media\DATA780_week1_notes\media\image19.png" style="width:5.46942in;height:1.38575in" /></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr>
<th>Live Session</th>
<th></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Introduction</td>
<td style="text-align: right;"><strong>05 Jan 2026</strong></td>
</tr>
<tr>
<td>Instructor</td>
<td colspan="2">Rei Sanchez-Arias</td>
</tr>
<tr>
<td>Email</td>
<td colspan="2"><a href="mailto:[REDACTED_EMAIL]">[REDACTED_EMAIL]</a></td>
</tr>
<tr>
<td>Website</td>
<td colspan="2"><a href="https://www.reisanar.com/">https://www.reisanar.com/</a></td>
</tr>
<tr>
<td>Office Hours</td>
<td colspan="2">Mondays 12:00 pm to 1:00 pm</td>
</tr>
<tr>
<td colspan="2">What to expect</td>
<td style="text-align: right;"><strong>DATA780</strong></td>
</tr>
<tr>
<td>Meeting Time</td>
<td colspan="2">Monday 6:00 pm to 7:30 pm</td>
</tr>
<tr>
<td>Final Project</td>
<td colspan="2"><p>project deliverables:</p>
<ul>
<li><p>project writeup: ~8 pages NeruIPS format</p></li>
<li><p>open-source repository with executable code for methods developed</p></li>
<li><p>the github repo can be private or <strong>public</strong></p></li>
<li><p>spotlight presentation (last live session)</p>
<ul>
<li><p>6 to 7 minutes for presentation</p></li>
<li><p>2 minutes for Q&amp;A</p></li>
<li><p>prepared slide deck</p></li>
<li><p>optional live demo</p></li>
</ul></li>
<li><p>final project can be combined for DATA780 and DATA740 (if it applies to both)</p></li>
<li><p>your project may innovate some new LM methodology, or make an improvement to an existing methodology</p></li>
</ul></td>
</tr>
<tr>
<td>Final Project Proposal</td>
<td colspan="2"><ul>
<li><p>state the task, goals</p></li>
<li><p>what methods do you plan to use?</p></li>
<li><p>what datasets will you consider?</p></li>
<li><p>evaluations metrics you plan to use</p></li>
</ul></td>
</tr>
<tr>
<td>Assessments</td>
<td colspan="2">Quizzes will be weekly</td>
</tr>
<tr>
<td>Syllabus</td>
<td colspan="2"><a href="https://digitalcampus.instructure.com/courses/55373/assignments/syllabus">https://digitalcampus.instructure.com/courses/55373/assignments/syllabus</a></td>
</tr>
<tr>
<td>Live Session Summary</td>
<td colspan="2">Meeting Notes found at the top of the Modules page on canvas <a href="https://digitalcampus.instructure.com/courses/55373/pages/meeting-notes?module_item_id=9295727">https://digitalcampus.instructure.com/courses/55373/pages/meeting-notes?module_item_id=9295727</a></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr>
<th colspan="2">What to expect</th>
<th style="text-align: right;">DATA780</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Resources</p>
<p>(free pdf downloads available)</p></td>
<td colspan="2"><ul>
<li><p>Mathematics for Machine Learning</p>
<ul>
<li><p>https://mml-book.github.io/book/mml-book.pdf</p></li>
</ul></li>
<li><p>Data-Driven Science and Engineering</p>
<ul>
<li><p>https://databookuw.com/</p></li>
</ul></li>
<li><p>Introduction to Statistical Learning</p>
<ul>
<li><p>https://www.statlearning.com/</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Blogs/Websites</td>
<td colspan="2"><p><strong>3Blue1Brown Videos (by Grant Sanderson)</strong></p>
<ul>
<li><p>Linear Algebra Series</p>
<ul>
<li><p>https://www.3blue1brown.com/topics/linear-algebra</p></li>
</ul></li>
<li><p>Calculus Series</p>
<ul>
<li><p>https://www.3blue1brown.com/topics/calculus</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">TODO</td>
<td></td>
</tr>
<tr>
<td>High Priority</td>
<td colspan="2"><ul>
<li><p>review linear algebra terminology</p></li>
<li><p>finish CW-Data780-unit_01.ipynb</p></li>
</ul></td>
</tr>
<tr>
<td>Low Priority</td>
<td colspan="2"><ul>
<li><p>review assignments</p>
<ul>
<li><p>Homework 1</p></li>
<li><p>Final Project</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>
