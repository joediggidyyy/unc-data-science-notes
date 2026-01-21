> Markdown version for convenient browsing. Original files:
> - PDF: [DATA740_week3_notes.pdf](../DATA740_week3_notes.pdf)
> - DOCX: [DATA740_week3_notes.docx](DATA740_week3_notes.docx)

---

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 0%" />
<col style="width: 10%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr>
<th>Measurement and Metadata</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Overview</td>
<td colspan="2" style="text-align: right;"><em>Week 3: 21 Jan 2026</em></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>what is a variable</p></li>
<li><p>what gets counted and why</p></li>
<li><p>how this is tied to measurement</p></li>
<li><p>differentiate between variables and metadata</p></li>
<li><p>how they are bound to ethical dilemmas</p></li>
<li><p>how the operationalization of variables complicates equity and justice</p></li>
<li><p>introduction to frameworks to test for bias</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Readings</td>
<td style="text-align: right;">[optional]</td>
</tr>
<tr>
<td colspan="4"><p>Buolamwini, J., &amp; Gebru, T. (2018). Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classiﬁcation. <em>Proceedings of Machine Learning Research</em>, <em>81</em>, 1–15.</p>
<ul>
<li><p><a href="https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf">https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf</a></p></li>
</ul>
<p>D’Ignazio, C., &amp; Klein, L. (2020). 4 - “What Gets Counted Counts.” In <em>Data Feminism</em>. MIT Press.</p>
<ul>
<li><p><a href="https://data-feminism.mitpress.mit.edu/pub/h1w0nbqp/release/3">https://data-feminism.mitpress.mit.edu/pub/h1w0nbqp/release/3</a></p></li>
</ul>
<p>Feinberg, M. (2023). Labels. In <em>Everyday Adventures with Unruly Data</em> (pp. 159–189). MIT Press.</p>
<ul>
<li><p><a href="https://mitpress.mit.edu/9780262544405/everyday-adventures-with-unruly-data/">https://mitpress.mit.edu/9780262544405/everyday-adventures-with-unruly-data/</a></p></li>
</ul>
<p>Jacobs, A. Z., &amp; Wallach, H. (2021). Measurement and Fairness. <em>Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency</em>, 375–385.</p>
<ul>
<li><p><a href="https://doi.org/10.1145/3442188.3445901">https://doi.org/10.1145/3442188.3445901</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 4%" />
<col style="width: 13%" />
<col style="width: 1%" />
<col style="width: 10%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr>
<th colspan="5">Definitions</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">performance model</td>
<td colspan="4"><p><strong>measures</strong> how well an <strong>AI/ML</strong> <strong>model</strong> achieves its <strong>intended</strong> <strong>task</strong></p>
<p>https://www.ibm.com/think/topics/model-performance</p></td>
</tr>
<tr>
<td colspan="2">conceptualization</td>
<td colspan="4"><p>the <strong>action</strong> or <strong>process</strong> of <strong>forming</strong> a <strong>concept</strong> or <strong>idea</strong> of something</p>
<p>https://languages.oup.com/google-dictionary-en/</p></td>
</tr>
<tr>
<td colspan="2">operationalization</td>
<td colspan="4"><p>the <strong>process</strong> of <strong>transforming</strong> abstract <strong>concepts</strong> into specific, <strong>measurable</strong>, and <strong>observable</strong> <strong>variables</strong></p>
<p>https://trainual.com/manual/operationalization</p></td>
</tr>
<tr>
<td colspan="2">intersectional identities</td>
<td colspan="4"><p>how different <strong>aspects</strong> of a person’s identity <strong>overlap</strong> and <strong>interact</strong>, creating unique <strong>experiences</strong> of <strong>privilege</strong> and <strong>disadvantage</strong></p>
<p>https://www.oregon.gov/deiconference/Documents/</p></td>
</tr>
<tr>
<td colspan="2">confounding variables</td>
<td colspan="4"><p>an <strong>external</strong>, unmeasured <strong>factor</strong> that <strong>influences</strong> both <strong>independent</strong> and <strong>dependent</strong> <strong>variables</strong></p>
<p><a href="https://amplitude.com/explore/experiment/confounding-variables">https://amplitude.com/explore/experiment/confounding-variables</a></p></td>
</tr>
<tr>
<td colspan="5">Variables</td>
<td></td>
</tr>
<tr>
<td>Variable Definition</td>
<td colspan="5"><ul>
<li><p><strong>placeholders</strong> for a value</p></li>
<li><p><strong>quantifiable</strong> <strong>concepts</strong> used to represent <strong>attributes</strong> or <strong>features</strong> in the <strong>data</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Uses of Variables</td>
<td colspan="5"><ul>
<li><p>calculate <strong>statistics</strong></p></li>
<li><p>provide <strong>summary</strong> of the central <strong>tendency</strong></p></li>
<li><p>provide <strong>dispersion</strong> of the <strong>data</strong></p></li>
<li><p>formulate <strong>hypotheses</strong></p></li>
<li><p>conduct <strong>tests</strong></p></li>
<li><p>determine <strong>significant</strong> <strong>relationships</strong> in the <strong>data</strong></p></li>
<li><p>evaluate <strong>performance</strong> <strong>models</strong></p></li>
</ul></td>
</tr>
<tr>
<td rowspan="2">Types of Variables</td>
<td colspan="3"><p><strong>discrete</strong></p>
<p><strong>nominal</strong></p>
<p><strong>ordinal</strong></p></td>
<td colspan="2"><p>represent <strong>characteristics</strong> that are not inherently <strong>quantifiable</strong></p>
<ul>
<li><p><strong>lack</strong> intrinsic <strong>order</strong></p></li>
<li><p><strong>colors</strong>, gender, <strong>location</strong></p></li>
<li><p>allow for <strong>ranking</strong></p></li>
<li><p>possess <strong>quantifiable</strong> <strong>distance</strong> between units</p></li>
<li><p><strong>low</strong> med <strong>high</strong>, first <strong>second</strong> third</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3"><p><strong>continuous</strong></p>
<p>interval</p>
<p>ratio</p></td>
<td colspan="2"><p>bound to a <strong>numerical</strong> <strong>system</strong></p>
<ul>
<li><p><strong>lack</strong> a true <strong>zero</strong></p></li>
<li><p><strong>scaled</strong> variable</p></li>
<li><p><strong>temperature</strong>, distance <strong>measurement</strong></p></li>
<li><p>has a <strong>true</strong> <strong>zero</strong> representing <strong>absence</strong> of <strong>variable</strong></p></li>
<li><p>exclusively <strong>positive</strong> values</p></li>
<li><p><strong>age</strong>, weight</p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Conceptualization and Operationalization</td>
<td></td>
</tr>
<tr>
<td>Conceptualization</td>
<td colspan="5">takes the idea and <strong>gives</strong> the <strong>variable</strong> an <strong>abstract</strong>, <strong>conceptual</strong>, or <strong>theoretical</strong> definition</td>
</tr>
<tr>
<td>Operationalization</td>
<td colspan="5">links the conceptual <strong>definition</strong> to a specific set of <strong>measurement</strong> <strong>techniques</strong> and <strong>procedures</strong></td>
</tr>
<tr>
<td colspan="6">Example: Intelligence</td>
</tr>
<tr>
<td>Conceptualization</td>
<td colspan="5"><ul>
<li><p><strong>intelligence</strong> is doing <strong>well</strong> in <strong>school</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Operationalization</td>
<td colspan="5"><ul>
<li><p><strong>GPA</strong> or standardized <strong>test</strong> <strong>scores</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Metadata</td>
<td colspan="5"><ul>
<li><p>related to <strong>conceptualization</strong> and <strong>operationalization</strong></p></li>
<li><p><strong>distinct</strong> in <strong>form</strong> and <strong>function</strong> from a <strong>variable</strong></p></li>
<li><p>helps <strong>describe</strong>, <strong>classify</strong>, and <strong>categorize</strong> data</p></li>
<li><p>enables <strong>users</strong> and <strong>systems</strong> to <strong>understand</strong> and interpret <strong>data</strong></p></li>
<li><p>makes it <strong>easier</strong> to <strong>organize</strong> and <strong>locate</strong> information</p></li>
</ul></td>
</tr>
<tr>
<td>Structural Metadata</td>
<td colspan="5"><ul>
<li><p>subject <strong>metadata</strong>, keywords</p></li>
<li><p><strong>not</strong> necessarily <strong>observable</strong></p></li>
<li><p><strong>ex</strong>: last <strong>file</strong> access <strong>time</strong></p></li>
<li><p>inferred through <strong>concepts</strong> which often involve <strong>human</strong> <strong>allocation</strong> and/or <strong>understanding</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Variables</td>
<td colspan="5"><ul>
<li><p>a <strong>variable</strong> that is <strong>not</strong> well <strong>conceptualized</strong> and <strong>operationalized</strong> <strong>cannot</strong> <strong>measure</strong> anything</p></li>
<li><p>a <strong>tag</strong> must conceptually <strong>describe</strong> the <strong>content</strong> to be retrieve</p></li>
</ul></td>
</tr>
<tr>
<td>Categorization</td>
<td colspan="5"><ul>
<li><p>allows <strong>researchers</strong> to <strong>conduct</strong> rigorous <strong>research</strong></p></li>
<li><p>facilitates <strong>efficient</strong> and <strong>effective</strong> data <strong>analysis</strong></p></li>
<li><p><strong>improves</strong> model <strong>accuracy</strong></p></li>
<li><p>creates <strong>robust</strong> <strong>databases</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Limitations</td>
<td colspan="5"><ul>
<li><p>many of the <strong>variables</strong> we rely on to create <strong>automated</strong> decision-making <strong>tools</strong> are <strong>inferred</strong> <strong>variables</strong> that rely on <strong>proxies</strong> that might <strong>not</strong> have an <strong>established</strong> <strong>tool</strong> for measurement</p></li>
<li><p><strong>cultural</strong> and <strong>social</strong> <strong>constructs</strong> can <strong>obscure</strong>, under-represent, and <strong>misrepresent</strong> <strong>data</strong> and <strong>demographics</strong></p></li>
<li><p>when <strong>tools</strong> to <strong>operationalize</strong> conceptual <strong>variables</strong> are <strong>absent</strong>, <strong>existing</strong> and often <strong>flawed</strong> <strong>power</strong> structures <strong>fill</strong> the <strong>vacuum</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Examples of Limitations</td>
<td colspan="5"><ul>
<li><p><strong>gender</strong> <strong>classification</strong> across <strong>cultural</strong> and <strong>ideological</strong> complexities</p></li>
<li><p><strong>racial</strong> <strong>classification</strong> and <strong>dehumanization</strong> based on <strong>tribalistic</strong> genetic <strong>memory</strong></p></li>
<li><p>clothing <strong>designers</strong> reinforce social <strong>expectations</strong> creating a second order <strong>effect</strong> for gender-social <strong>norms</strong> (<strong>no</strong> <strong>pockets</strong> for women = <strong>sell</strong> <strong>more</strong> purses)</p></li>
</ul></td>
</tr>
<tr>
<td>Classifications</td>
<td colspan="5"><ul>
<li><p><strong>classifications</strong> can <strong>serve</strong> many <strong>purposes</strong></p></li>
<li><p>the <strong>type</strong> of data <strong>stored</strong> in a <strong>variable</strong></p></li>
<li><p><strong>reductive</strong> by design</p></li>
</ul></td>
</tr>
<tr>
<td><p>The Matrix of Domination</p>
<p><a href="https://www.youtube.com/watch?v=6SN3yS02D1c"><u>Patricia Hill Collins: Black Feminist Thought</u></a></p></td>
<td colspan="2"><p><strong>structural</strong></p>
<p><strong>disciplinary</strong></p>
<p><strong>hegemonic</strong></p>
<p><strong>interpersonal</strong></p></td>
<td colspan="3"><ul>
<li><p>encompasses the <strong>laws</strong> and social <strong>structures</strong> that perpetuate <strong>oppression</strong></p></li>
<li><p>bureaucratic <strong>processes</strong> and <strong>hierarchies</strong> that are used to <strong>uphold</strong> <strong>inequity</strong> even after laws are <strong>changed</strong></p></li>
<li><p>the consolidated <strong>ideas</strong> about who has <strong>power</strong> and who does <strong>not</strong> are often <strong>passed</strong> through <strong>media</strong>, <strong>art</strong>, and <strong>group</strong> <strong>think</strong></p></li>
<li><p>latent systemic <strong>inequities</strong> in daily <strong>interactions</strong> <strong>reinforce</strong> power <strong>balances</strong></p></li>
</ul></td>
</tr>
<tr>
<td colspan="6">Models, Audits, and Accounts</td>
</tr>
<tr>
<td>Measurement Modeling</td>
<td colspan="5"><ul>
<li><p>ensure that the model is performing as designed</p></li>
<li><p>ensure model variables are being operationalized</p></li>
</ul></td>
</tr>
<tr>
<td>Audit Studies</td>
<td colspan="5"><ul>
<li><p>gauging the <strong>consistency</strong> of measured <strong>processes</strong></p></li>
<li><p><strong>routing</strong> part of <strong>civic</strong> <strong>infrastructure</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Audit Algorithms</td>
<td colspan="5"><ul>
<li><p>investigation of algorithms to uncover inherent or situationally derived biases and potential discrimination</p></li>
<li><p>designed to repeatedly and systematically validate algorithmic inputs and ensure verifiability and objectivity of outputs</p></li>
<li><p>determine if intersectional identities impact results</p></li>
</ul></td>
</tr>
<tr>
<td colspan="6">Considerations for Construct Validity</td>
</tr>
<tr>
<td>Construct Validity</td>
<td colspan="5"><ul>
<li><p>ensuring that measurements are accurately represented</p></li>
<li><p>ensuring the intended construct will consider the impact of these measurements</p></li>
<li><p>ensuring the measurements align with known hypotheses</p></li>
<li><p>assessing consequences of their usage</p></li>
<li><p>inherently nuanced and relies on critical reasoning to establish a degree of validity</p></li>
</ul></td>
</tr>
<tr>
<td>Face Validity</td>
<td colspan="5"><ul>
<li><p>gauge plausibility of measurements</p></li>
</ul></td>
</tr>
<tr>
<td>Content Validity</td>
<td colspan="5"><ul>
<li><p>ensure that operationalization fully captures the construct of what is being measured</p></li>
</ul></td>
</tr>
<tr>
<td>Convergent Validity</td>
<td colspan="5"><ul>
<li><p>assesses whether the measurements align with those other established models</p></li>
<li><p>identify potential overlaps and discriminatory patterns</p></li>
</ul></td>
</tr>
<tr>
<td>Discriminant Validity</td>
<td colspan="5"><ul>
<li><p>determine if operationalization could capture other constructs</p></li>
<li><p>determine if there are confounding variables</p></li>
</ul></td>
</tr>
<tr>
<td>Predictive Validity</td>
<td colspan="5"><ul>
<li><p>highlights how proxies may relate to various observable properties not always factored into models</p></li>
</ul></td>
</tr>
<tr>
<td><p>Hypothesis/</p>
<p>Consequential Validity</p></td>
<td colspan="5"><ul>
<li><p>explore how the world is shaped by the measurements</p></li>
<li><p>determine if measurements inadvertently perpetuate inequality</p></li>
<li><p>considers broader implications</p></li>
</ul></td>
</tr>
<tr>
<td>Consequential Validity</td>
<td colspan="5"><ul>
<li><p>investigates the consequences of using the measurements obtained from the model</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Live Session Preparation</th>
<th style="text-align: right;"><em>Week 3: 30 Oct 2025</em></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><em>Consider an object that you use every day. Who do you think this object was designed for? How do you know? Who can’t use this object? What might inclusive design look like?</em></td>
</tr>
<tr>
<td colspan="2"><p><em>I spend most of my day at this computer for one reason or another, so I am choosing as my object my keyboard. To limit the scope, I am going to narrow this specifically to the QWERTY keyboard.</em></p>
<p><em>The QWERTY keyboard was invented in 1870 by Christopher Latham Sholes. Sholes, a Pennsylvania native, moved to the newly established Wisconsin Territory in 1837 to take on training as a printer’s apprentice at his elder brother’s newspaper. He quickly advanced in the realm of periodical publication to run several newspapers in different frontier towns to eventually receive an appointment to federal office by President Lincoln. This shift in vocation granted Sholes with unprecedented free time to pursue his interests as an engineer and inventor. Adapting a page numbering device invented by his friend John Pratt, Sholes invented the typewriter receiving a patent in June of 1968. He continued to work on and make improvements to his device throughout the rest of his life. In response to recurring jamming issues with adjacent frequently-used keys in his current design, he began to formulate what would eventually, in 1870, become the QWERTY keyboard. Sholes sold his patent in 1873 to the Remington Arms Company, a company uniquely suited to mass-produce his design, and the well-recognized result was the iconic Remington Typewriter.</em></p>
<p><em>The typewriter was not-surprisingly initially intended for commercial printing. As literacy rates rose through the 19<sup>th</sup> century, commercial publication moved from a smattering of fringe hobbyist, into a network of powerful economic and cultural leaders. As the familiar pattern of cultural adoption of new technologies, the ability to create printed documentation spread through the business and eventually the private sectors. As the use of typewriters accelerated to become staple in the workplace by 1910 in the United States, typing was a skill initially dominated by women. Though, by 1915, typing became a core skill taught in most American high schools with widespread use peaking in the mid-20<sup>th</sup> century.</em></p>
<p><em>Some of the limitations of the keyboard are realized when adapting for physically handicapped users. The QWERTY keyboard, in particular, reveals its limitations with its Anglo-Latin-centric layout and character-set. Much effort has been made to adapt the QWERTY keyboard to cater to users with physical, visual, or cognitive disabilities. ‘Large Keycap’ keyboards featuring larger, spaced keys, single-handed layouts, ergonomic designs, high-contrast designs, and on-screen keyboards that can be controlled by mouse click, touch, and even neural interface, are all efforts that have successfully brought this technology to those previously excluded. One design idea that could make the keyboard more universal and globally accessible would be a dynamic keyboard that stores and renders various layouts. This could be achieved through a capacitive touch screen with a customizable layout, or a physical-key-based design with kindle-paper-like key faces that facilitate preprogrammed and customizable layouts.</em></p></td>
</tr>
<tr>
<td colspan="2"><p>References</p>
<p><a href="https://www.britannica.com/biography/Christopher-Latham-Sholes">https://www.britannica.com/biography/Christopher-Latham-Sholes</a></p>
<p><a href="https://www.opticjam.com/the-history-of-publishing-from-ancient-tablets-to-digital-media">https://www.opticjam.com/the-history-of-publishing-from-ancient-tablets-to-digital-media</a></p>
<p><a href="https://www.youtube.com/watch?v=X8yZy2-ex8E&amp;t=134">https://www.youtube.com/watch?v=X8yZy2-ex8E&amp;t=134</a></p>
<p><a href="https://www.wati.org/wp-content/uploads/2017/10/Ch4-ComputerAccess.pdf">https://www.wati.org/wp-content/uploads/2017/10/Ch4-ComputerAccess.pdf</a></p></td>
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
<th colspan="2">Live Session Notes</th>
<th style="text-align: right;"><em>Class Meeting: 21 Jan 2026</em></th>
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
