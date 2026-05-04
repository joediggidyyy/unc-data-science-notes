> Markdown version for convenient browsing. Original files:
> - DOCX: [DATA785_week01_notes.docx](DATA785_week01_notes.docx)

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
<th colspan="2">Linear and Logistic Regression</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Course Facilitators</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>Course Instructor: <a href="https://www.jonathanschlosser.com/">Jonathan Schlosser</a>, Adjunct Professor</p></li>
</ul>
<ul>
<li><p><a href="mailto:[REDACTED_EMAIL]">[REDACTED_EMAIL]</a></p></li>
<li><p>Office Hours: Mondays 5PM – 6PM</p></li>
<li><p>PhD in Media and Communication from Chapel Hill</p></li>
<li><p>Lead Data Scientist – Generative AI, AlignAI</p></li>
<li><p>Research Interests</p>
<ul>
<li><p>LLMs, MLOps, and Generative AI</p></li>
<li><p>Applied AI Development</p></li>
<li><p>Generative Documentation Systems</p></li>
</ul></li>
<li><p>Recent Projects</p>
<ul>
<li><p><a href="https://www.jonathanschlosser.com/projects/formbot">https://www.jonathanschlosser.com/projects/formbot</a></p></li>
<li><p>https://www.jonathanschlosser.com/projects/automated-pipeline-monitoring</p></li>
<li><p>Course Designer: <a href="https://www.ssriva.com/">Shashank Srivastava</a>, Asst. Professor</p></li>
</ul></li>
<li><p><a href="mailto:[REDACTED_EMAIL]">[REDACTED_EMAIL]</a></p></li>
<li><p>PhD in Machine Learning from Carnagie Mellon University</p></li>
<li><p>Leads the “Learning from Language Lab” at UNC Chapel Hill</p></li>
<li><p>Research Interests</p>
<ul>
<li><p>Language, intelligence, and Interactivity</p></li>
<li><p>Explanation &amp; Alignment</p></li>
<li><p>Social &amp; Cognitive Applications</p></li>
</ul></li>
<li><p>Recent Publications</p>
<ul>
<li><p>Is Chain-of-Thought Really Not Explainability? Chain-of-Thought Can Be Faithful without Hint Verbalization</p>
<ul>
<li><p><a href="https://arxiv.org/abs/2512.23032">https://arxiv.org/abs/2512.23032</a></p></li>
</ul></li>
<li><p>DiffVax: Optimization-Free Image Immunization Against Diffusion-Based Editing</p>
<ul>
<li><p><a href="https://diffvax.github.io/">https://diffvax.github.io/</a></p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Course Overview</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>What is Deep Learning?</p>
<ul>
<li><p>a subset of machine learning that has to do with building machine learning models that are large, complex, and differentiable</p></li>
</ul></li>
</ul>
<p>Data Science</p>
<p>Machine Learning</p>
<p>Deep Learning</p>
<p>you are here</p>
<ul>
<li><p>Applications of Deep Learning</p>
<ul>
<li><p>Healthcare: from early disease detection to robotic surgeries</p></li>
<li><p>Transport and automation: powering autonomy in self-driving cars</p></li>
<li><p>Entertainment: personalizing streaming content</p></li>
<li><p>Science: predicting protein structures, creating new molecules</p></li>
<li><p>Technology and information: ChatGPT, Bard, and other language technologies</p></li>
</ul></li>
<li><p>Impact on Daily Life</p>
<ul>
<li><p>Facial recognition in your phones</p></li>
<li><p>Speech technology in Siri and Alexa</p></li>
<li><p>Automated customer service and chatbots</p></li>
<li><p>Real-time translation apps</p></li>
<li><p>Home automation and the Internet of Things (IoT)</p></li>
<li><p>Fraud detection with credit cards</p></li>
</ul></li>
<li><p>Breakthroughs and Innovations</p>
<ul>
<li><p>AlphaGo defeats human champions (2016)</p></li>
<li><p>Insilico Medicine identifies a new molecule for accelerated treatment of fibrosis in 46 days (2019)</p></li>
<li><p>Discover of exoplanets: Kepler-90i and Kepler-80g (2017)</p></li>
<li><p>Early detection of diabetic retinopathy (2021)</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>What to Expect</td>
<td colspan="4"><p><img src="generated_media\DATA785_week01_notes\media\image1.png" style="width:1.58333in;height:1.05139in" /><img src="generated_media\DATA785_week01_notes\media\image2.png" style="width:1.41667in;height:0.94444in" /></p>
<p>images: ChatGPT 5.4</p>
<p>not</p>
<ul>
<li><p>heavy emphasis on <strong>linear</strong> <strong>algebra</strong> and <strong>calculus</strong></p></li>
<li><p><strong>drudgery</strong> and <strong>hard</strong> <strong>work</strong></p></li>
<li><p><strong>principles</strong> and <strong>methods</strong> underlying <strong>modern</strong> <strong>tools</strong>, but <strong>not</strong> the <strong>tools</strong> or <strong>libraries</strong> <strong>themselves</strong></p></li>
<li><p>“unless we grossly mess it up, <strong>this course is going to be hard</strong>”</p></li>
</ul></td>
</tr>
<tr>
<td>Unit 1 Overview</td>
<td colspan="4"><ul>
<li><p><strong>distinguish</strong> between <strong>traditional</strong> machine learning <strong>pipelines</strong> and <strong>deep</strong> <strong>learning</strong> <strong>models</strong> </p></li>
<li><p>design <strong>linear</strong> <strong>models</strong> for <strong>predictive</strong> <strong>modeling</strong></p></li>
<li><p>implement <strong>gradient</strong> <strong>descent</strong> to <strong>train</strong> linear regression </p></li>
<li><p><strong>understand</strong> the <strong>classification</strong> approach <strong>presented</strong> in <strong>logistic</strong> <strong>regression</strong></p></li>
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
<td colspan="3">Linear Regression</td>
</tr>
<tr>
<td>Week 1 Outline</td>
<td colspan="2"><ul>
<li><p><strong>form</strong> and <strong>model</strong> <strong>parameters</strong></p></li>
<li><p><strong>loss</strong> function</p></li>
<li><p><strong>training</strong> with <strong>gradient</strong> <strong>descent</strong></p></li>
<li><p><strong>mini</strong>-<strong>batch</strong> <strong>stochastic</strong> <strong>gradient</strong> <strong>descent</strong></p></li>
<li><p><strong>hyper</strong>-<strong>parameters</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Form and Model Parameters</td>
</tr>
<tr>
<td>Regression</td>
<td colspan="2"><ul>
<li><p><strong>predicting</strong> a real-value (<strong>scalar</strong>) <strong>output</strong> based on a <strong>set</strong> of <strong>input</strong> <strong>features</strong></p></li>
</ul>
<p><span class="math display"><strong>f</strong> <strong>:</strong> <strong>x</strong><strong>∈</strong>ℝ<sup><strong>d</strong></sup> <strong>→</strong> <strong>y</strong> ∈ ℝ</span></p>
<ul>
<li><p>e.g. <strong>estimate</strong> the <strong>energy</strong> <strong>consumption</strong> of a home from</p>
<ul>
<li><p><span class="math inline"><strong>s</strong><strong>i</strong><strong>z</strong><strong>e</strong></span>: floorspace (<span class="math inline"><em>s</em><em>q</em> <em>f</em><em>t</em></span>)</p></li>
<li><p><span class="math inline"><strong>t</strong><strong>e</strong><strong>m</strong><strong>p</strong></span>: avg temperature (<span class="math inline"><em>F</em></span>)</p></li>
<li><p><span class="math inline"><strong>p</strong><strong>r</strong><strong>e</strong><strong>v</strong></span>: consumption in previous month (<span class="math inline"><em>K</em><em>w</em></span>)</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Linear Regression</td>
<td colspan="2"><ul>
<li><p>when the <strong>function</strong> <span class="math inline"><strong>f</strong></span> is <strong>linear</strong> in the <strong>inputs</strong> <span class="math inline"><strong>x</strong></span></p></li>
</ul>
<p><span class="math display"><strong>y</strong> <strong>:</strong> <strong>c</strong><strong>o</strong><strong>n</strong><strong>s</strong><strong>u</strong><strong>m</strong><strong>p</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong></span></p>
<p><span class="math display"><strong>x</strong><strong>:</strong> <strong>[</strong><strong>s</strong><strong>i</strong><strong>z</strong><strong>e</strong><strong>,</strong> <strong>t</strong><strong>e</strong><strong>m</strong><strong>p</strong><strong>,</strong> <strong>p</strong><strong>r</strong><strong>e</strong><strong>v</strong><strong>]</strong></span></p>
<p><span class="math display"><strong>w</strong><strong>:</strong> <strong>[</strong><strong>w</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>w</strong><sub><strong>2</strong></sub><strong>,</strong> <strong>w</strong><sub><strong>3</strong></sub><strong>]</strong></span></p>
<ul>
<li><p>that is<strong>:</strong> <span class="math inline"><strong>c</strong><strong>o</strong><strong>n</strong><strong>s</strong><strong>u</strong><strong>m</strong><strong>p</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong><strong>=</strong><strong>w</strong><sub><strong>1</strong></sub><strong>s</strong><strong>i</strong><strong>z</strong><strong>e</strong><strong>+</strong><strong>w</strong><sub><strong>2</strong></sub><strong>t</strong><strong>e</strong><strong>m</strong><strong>p</strong><strong>+</strong><strong>w</strong><sub><strong>3</strong></sub><strong>p</strong><strong>r</strong><strong>e</strong><strong>v</strong><strong>i</strong><strong>o</strong><strong>u</strong><strong>s</strong> <strong>+</strong> <strong>b</strong></span></p></li>
</ul>
<p><img src="generated_media\DATA785_week01_notes\media\image3.png" style="width:2.26476in;height:1.7096in" /></p>
<p><span class="math display"><strong>y</strong><strong>=</strong><strong>w</strong><sup><strong>T</strong></sup><strong>x</strong> <strong>+</strong> <strong>b</strong></span></p>
<ul>
<li><p>training set:</p></li>
</ul>
<p><span class="math inline"><strong>X</strong><sub><strong>t</strong><strong>r</strong><strong>a</strong><strong>i</strong><strong>n</strong></sub><strong>,</strong> <strong>Y</strong><sub><strong>t</strong><strong>r</strong><strong>a</strong><strong>i</strong><strong>n</strong></sub> <strong>≔</strong> <strong>{</strong>(<strong>x</strong><sup><strong>k</strong></sup><strong>,</strong> <strong>y</strong><sup><strong>k</strong></sup>)<sub><strong>n</strong></sub><strong>}</strong></span></p>
<p><span class="math display"><em>n</em> × 1</span></p>
<p>ChatGPT 5.4</p>
<p>(bias)</p>
<p><span class="math display"><strong>s</strong><strong>c</strong><strong>a</strong><strong>l</strong><strong>a</strong><strong>r</strong></span></p>
<p><span class="math display">$$\widehat{\mathbf{Y}}\mathbf{= Xw + b}$$</span></p>
<p><span class="math display"><strong>d</strong> <strong>×</strong> <strong>1</strong></span></p>
<p><span class="math display"><strong>n</strong> <strong>×</strong> <strong>d</strong></span></p></td>
</tr>
<tr>
<td>Linear Regression as a Neural Net</td>
<td colspan="2"><ul>
<li><p><strong>linear</strong> <strong>regression</strong> can be thought of as a <strong>single</strong>-<strong>layer</strong> <strong>neural</strong> <strong>net</strong> (also called a <strong>perceptron</strong>)</p></li>
</ul>
<p><img src="generated_media\DATA785_week01_notes\media\image4.png" style="width:2.14151in;height:1.60527in" /></p>
<p><span class="math display"><em>ŷ</em> = <em>w</em><sup><em>T</em></sup><em>x</em></span></p>
<p>ChatGPT 5.4</p></td>
</tr>
<tr>
<td colspan="3">Loss Function</td>
</tr>
<tr>
<td>Loss Function for Linear Regression</td>
<td colspan="2"><ul>
<li><p>describes “<strong>how</strong> <strong>well</strong>” your <strong>model</strong> is <strong>performing</strong></p></li>
<li><p><img src="generated_media\DATA785_week01_notes\media\image5.png" style="width:2.22545in;height:1.65094in" /><strong>loss</strong> <strong>function</strong>:</p></li>
</ul>
<blockquote>
<p><span class="math display">$$\mathbf{L}\left( \mathbf{w} \right)\mathbf{≔}\frac{\mathbf{1}}{\mathbf{2}}\sum_{\mathbf{k}}^{}\left( \mathbf{y}^{\mathbf{k}}\mathbf{-}{\widehat{\mathbf{y}}}^{\mathbf{k}} \right)^{\mathbf{2}}$$</span></p>
<p><span class="math inline">$\mathbf{=}\mathbf{L}\left( \mathbf{w} \right)\mathbf{≔}\frac{\mathbf{1}}{\mathbf{2}}\sum_{\mathbf{k}}^{}\left( \mathbf{y}^{\mathbf{k}}\mathbf{-}\mathbf{w}^{\mathbf{T}}\mathbf{x}^{\mathbf{k}} \right)^{\mathbf{2}}$</span></p>
</blockquote>
<p>ChatGPT 5.4</p>
<blockquote>
<p><span class="math display"> <strong>=</strong> <strong>s</strong><strong>u</strong><strong>m</strong><strong>(</strong><strong>s</strong><strong>q</strong><strong>u</strong><strong>a</strong><strong>r</strong><strong>e</strong><strong>d</strong> <strong>e</strong><strong>r</strong><strong>r</strong><strong>o</strong><strong>r</strong><strong>s</strong><strong>)</strong></span></p>
</blockquote></td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</tbody>
</table>
