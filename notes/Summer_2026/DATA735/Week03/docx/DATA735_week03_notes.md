> Markdown version for convenient browsing. Original files:
> - PDF: [DATA735_week03_notes.pdf](../DATA735_week03_notes.pdf)
> - DOCX: [DATA735_week03_notes.docx](DATA735_week03_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Causal Identification</th>
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
<td colspan="5"><p>Under what conditions can we confidently say something causes something else? This week, you will learn about causal identification, discover essential assumptions for valid causal claims, and explore how biases like selection and heterogeneity can threaten causal validity.</p>
<p>The following are our goals for the week:</p>
<ul>
<li><p>Understand the meaning of identification in the context of causal attribution.</p></li>
<li><p>Understand the key assumptions needed for causal attribution: positivity, SUTVA, and ignorability.</p></li>
<li><p>Identify common threats to internal validity, including selection, attrition, spillovers.</p></li>
<li><p>Identify threats to external validity and generalizability.</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Readings</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><p><a href="https://mixtape.scunning.com/04-potential_outcomes#simple-difference-in-means-decomposition">https://mixtape.scunning.com/04-potential_outcomes#simple-difference-in-means-decomposition</a></p>
<p><a href="https://mixtape.scunning.com/04-potential_outcomes#independence-assumption">https://mixtape.scunning.com/04-potential_outcomes#independence-assumption</a></p>
<p><a href="https://mixtape.scunning.com/04-potential_outcomes#4-1-5-sutva">https://mixtape.scunning.com/04-potential_outcomes#4-1-5-sutva</a></p></td>
</tr>
<tr>
<td colspan="5">Core Concepts in Causal Inference: Potential Outcomes</td>
</tr>
<tr>
<td>Simple Difference in Means (SDM) Decomposition</td>
<td colspan="4"><p>What is it?</p>
<ul>
<li><p>SDM is what you calculate when you look at the raw difference between the average outcome of a treated group D<span class="math inline"> = 1</span> and a control group <span class="math inline"><em>D</em> = 0</span></p></li>
<li><p>SDM does not usually show the true causal effect because it is made up of three separate parts</p></li>
</ul></td>
</tr>
<tr>
<td>3 Parts of the SDM Formula</td>
<td colspan="4"><p>Average Treatment Effect (ATE)</p>
<ul>
<li><p>this is the true causal effect you want to measure</p></li>
<li><p>it tells you the average impact if everyone in the population received the treatment vs. nobody receiving it</p></li>
</ul>
<p>Selection Bias</p>
<ul>
<li><p>the baseline difference between the groups</p></li>
<li><p>how the groups would naturally differ from each other even if neither group received the treatment</p></li>
</ul>
<p>Heterogeneous Treatment Effect Bias</p>
<ul>
<li><p>difference in how much each group benefits from the treatment</p></li>
<li><p>occurs when the group that chose to take the treatment benefits more (or less) from it than the other group would have</p></li>
</ul>
<p>Key Takeaways</p>
<ul>
<li><p><span class="math inline">SDM = ATE + Selection Bias + Heterogeneous Treatment Effect Bias</span></p></li>
<li><p>because of the biases, the raw difference in means rarely equals the true causal effect</p></li>
</ul></td>
</tr>
<tr>
<td>The Independence Assumption</td>
<td colspan="4"><p>What is it?</p>
<ul>
<li><p>independence means that the assignment of the treatment D is completely unrelated to the potential outcomes <span class="math inline"><em>Y</em><sup>1</sup><em>a</em><em>n</em><em>d</em><em>Y</em><sup>0</sup></span></p></li>
<li><p>it assumes that the groups being compared have the exact same average potential outcome in a large population</p></li>
</ul>
<p>The Problem in Real Life</p>
<ul>
<li><p>in the real world, independence is rarely true for observational data</p></li>
<li><p>people make rational choices based on what they think will happen to them (their potential outcomes)</p></li>
<li><p>example</p>
<ul>
<li><p>parents who choose to put their kids in private school do so because they think it will benefit their child</p></li>
<li><p>this breaks independence</p></li>
</ul></li>
</ul>
<p>How to Fix It</p>
<ul>
<li><p>physical randomization (like a coin flip) forces independence</p></li>
<li><p>when treatment is assigned completely at random, selection bias and heterogeneous treatment effect bias disappear</p></li>
<li><p>this leaves you with a clean measure of the ATE</p></li>
</ul></td>
</tr>
<tr>
<td>Stable Unit Treatment Value Assumption (SUTVA)</td>
<td colspan="4"><p>The 3 Rules of SUTVA</p>
<ul>
<li><p>Homogeneous Doses (Same Sized Dose)</p></li>
<li><p>every unit in the treatment group must receive the exact same version and intensity of the treatment</p></li>
<li><p>violation example:</p></li>
<li><p>if you are measuring the effect of surgery, but some doctors are much better surgeons than others, the treatment dose is not uniform</p></li>
</ul>
<p>No Spillovers (No Externalities)</p>
<ul>
<li><p>one person's treatment status cannot change or affect another person's outcome</p></li>
<li><p>violation example</p></li>
<li><p>if you give a vaccine to Person A, it protects them, but it also lowers the chance of Person B getting sick, even though Person B never got the vaccine</p></li>
</ul>
<p>No General Equilibrium Effects (Scaling Issues)</p>
<ul>
<li><p>the treatment shouldn't change the broader environment or market dynamics when scaled up</p></li>
<li><p>violation example</p></li>
<li><p>if a small experiment shows that going to college increases a person's salary, scaling it up so everyone goes to college might flood the job market and lower college graduate wages everywhere</p></li>
</ul></td>
</tr>
</tbody>
</table>
