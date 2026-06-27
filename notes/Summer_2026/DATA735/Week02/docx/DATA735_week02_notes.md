> Markdown version for convenient browsing. Original files:
> - PDF: [DATA735_week02_notes.pdf](../DATA735_week02_notes.pdf)
> - DOCX: [DATA735_week02_notes.docx](DATA735_week02_notes.docx)

---

<table style="width:100%;">
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">The Potential Outcomes Framework</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td colspan="2" style="text-align: right;"><em>[date]</em></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>learn the notation of potential outcomes and define individual-level effects using potential outcomes</p></li>
<li><p>formulate average causal effects using potential outcomes notation, including average treatment effects (ATEs), average treatment effects on the treated, and conditional ATEs</p></li>
<li><p>understand common challenges in causal attribution using the potential outcomes framework</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Readings</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p><a href="https://mixtape.scunning.com/04-potential_outcomes#statistical-inference">https://mixtape.scunning.com/04-potential_outcomes#statistical-inference</a></p></li>
<li><p><a href="https://mixtape.scunning.com/04-potential_outcomes#physical-randomization">https://mixtape.scunning.com/04-potential_outcomes#physical-randomization</a></p></li>
<li><p><a href="https://mixtape.scunning.com/04-potential_outcomes#potential-outcomes">https://mixtape.scunning.com/04-potential_outcomes#potential-outcomes</a></p></li>
<li><p><a href="https://mixtape.scunning.com/04-potential_outcomes#average-treatment-effect">https://mixtape.scunning.com/04-potential_outcomes#average-treatment-effect</a></p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><p>Setting the Stage: From Urn Models to Box Models</p>
<p><a href="https://www.degruyterbrill.com/document/doi/10.1515/jci-2023-0073/html">https://www.degruyterbrill.com/document/doi/10.1515/jci-2023-0073/html</a></p></td>
</tr>
<tr>
<td>Summary</td>
<td colspan="4"><ul>
<li><p>Q: how can we explain Neyman’s 1923 ideas about causal inference in a way that students can actually understand?</p></li>
<li><p>A: use simple physical models, especially:</p>
<ul>
<li><p>urns</p></li>
<li><p>boxes</p></li>
<li><p>tickets</p></li>
<li><p>random draws</p></li>
<li><p>two possible outcomes per subject</p></li>
</ul></li>
<li><p>the article argues that Neyman’s ideas are still underused in introductory statistics education, even though they are central to modern causal inference</p></li>
</ul></td>
</tr>
<tr>
<td>Neyman’s 1923 Framework</td>
<td colspan="4"><ul>
<li><p>in an experiment, each unit has <strong>potential outcomes</strong></p>
<ul>
<li><p>example:</p>
<ul>
<li><p>a person in a medical trial has</p>
<ul>
<li><p>one outcome <strong>if treated</strong></p></li>
<li><p>one outcome <strong>if not treated</strong></p></li>
</ul></li>
</ul></li>
<li><p>but we can only observe <strong>one</strong> of those outcomes</p></li>
<li><p>that is the core causal-inference problem</p></li>
<li><p>the missing outcome is called the <strong>counterfactual</strong> outcome</p></li>
</ul></li>
<li><p>the authors explain that Neyman’s setup treats the actual experimental units as the population of interest</p></li>
<li><p>the randomness comes from</p>
<ul>
<li><p><strong>random treatment assignment</strong></p></li>
<li><p>not from assuming the subjects were randomly sampled from some larger imaginary population</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Potential Outcome</td>
<td colspan="4"><ul>
<li><p>a possible result for one unit under one treatment condition</p></li>
<li><p>for unit i:</p>
<ul>
<li><p><span class="math inline"><em>y</em><sub><em>i</em></sub>(1)</span> = outcome if treated</p></li>
<li><p><span class="math inline"><em>y</em><sub><em>i</em></sub>(0)</span> = outcome if untreated / control</p></li>
</ul></li>
<li><p>only one can be observed for each unit</p></li>
<li><p>the appendix uses exactly this setup:</p>
<ul>
<li><p><span class="math inline"><em>y</em><sub><em>i</em></sub>(1)</span> and <span class="math inline"><em>y</em><sub><em>i</em></sub>(0)</span> are fixed quantities, while treatment assignment indicators are random</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Average Treatment Affect (ATE)</td>
<td colspan="4"><ul>
<li><p><span class="math inline"><em>ŷ</em>(1) </span>= average outcome if everyone were treated =</p></li>
<li><p><span class="math inline"><em>ŷ</em>(0) </span>= average outcome if everyone were untreated</p></li>
<li><p><span class="math inline"><em>A</em><em>T</em><em>E</em> = <em>ŷ</em>(1) − <em>ŷ</em>(0)</span></p></li>
<li><p><span class="math inline">$\widehat{ATE} = mean\ observed\ outcome\ in\ treatment\ group - mean\ observed\ outcome\ in\ control\ group$</span></p></li>
</ul></td>
</tr>
<tr>
<td>Randomization-Based Inference</td>
<td colspan="4"><ul>
<li><p>the uncertainty comes from which units were randomly assigned to which treatment</p></li>
<li><p>it does not require imagining that the experiment’s subjects are a random sample from a huge external population</p></li>
<li><p>this is different from the common textbook approach, where two-sample tests are often justified by assuming two independent samples from two infinite or hypothetical populations</p></li>
</ul></td>
</tr>
<tr>
<td>Conservative Standard Error</td>
<td colspan="4"><ul>
<li><p>a standard error is conservative when it is too large, or tends to overstate uncertainty</p></li>
<li><p>that is usually safer than being too small</p></li>
<li><p>the article emphasizes that the usual standard error in randomized experiments is often conservative because of two mistakes that partly cancel each other</p></li>
</ul></td>
</tr>
<tr>
<td>Neyman’s First Major Result</td>
<td colspan="4"><ul>
<li><p>difference in group means is an unbiased estimator of the average treatment effect</p></li>
<li><p>so, for a randomly assigned treatment</p></li>
</ul>
<p><span class="math display">$$E\lbrack\widehat{ATE}\rbrack\  = \ ATE$$</span></p>
<ul>
<li><p>so, the observed treatment-control difference is correct <strong>on average over repeated random assignments</strong></p></li>
<li><p>this works because the treatment group and control group are random samples from the finite set of experimental units</p></li>
</ul></td>
</tr>
<tr>
<td>The Surprising Standard-Error Result</td>
<td colspan="4"><ul>
<li><p>the usual variance estimator for a difference in means is based on:</p></li>
</ul>
<p><span class="math display">$$\frac{s_{1}^{2}}{n_{1}}\  + \frac{s_{0}^{2}}{n_{0}}$$</span></p>
<ul>
<li><p>where:</p></li>
</ul>
<p><span class="math display"><em>s</em><sub>1</sub>² = <em>s</em><em>a</em><em>m</em><em>p</em><em>l</em><em>e</em> <em>v</em><em>a</em><em>r</em><em>i</em><em>a</em><em>n</em><em>c</em><em>e</em> <em>i</em><em>n</em> <em>t</em><em>h</em><em>e</em> <em>t</em><em>r</em><em>e</em><em>a</em><em>t</em><em>m</em><em>e</em><em>n</em><em>t</em> <em>g</em><em>r</em><em>o</em><em>u</em><em>p</em></span></p>
<p><span class="math display"><em>s</em><sub>0</sub>² = <em>s</em><em>a</em><em>m</em><em>p</em><em>l</em><em>e</em> <em>v</em><em>a</em><em>r</em><em>i</em><em>a</em><em>n</em><em>c</em><em>e</em> <em>i</em><em>n</em> <em>t</em><em>h</em><em>e</em> <em>c</em><em>o</em><em>n</em><em>t</em><em>r</em><em>o</em><em>l</em> <em>g</em><em>r</em><em>o</em><em>u</em><em>p</em></span></p>
<p><span class="math display"><em>n</em><sub>1</sub> = <em>t</em><em>r</em><em>e</em><em>a</em><em>t</em><em>m</em><em>e</em><em>n</em><em>t</em> − <em>g</em><em>r</em><em>o</em><em>u</em><em>p</em> <em>s</em><em>i</em><em>z</em><em>e</em></span></p>
<p><span class="math display"><em>n</em><sub>0</sub> = <em>c</em><em>o</em><em>n</em><em>t</em><em>r</em><em>o</em><em>l</em> − <em>g</em><em>r</em><em>o</em><em>u</em><em>p</em> <em>s</em><em>i</em><em>z</em><em>e</em></span></p>
<ul>
<li><p>traditional textbooks often justify this formula by pretending there are:</p>
<ul>
<li><p>two independent samples</p></li>
<li><p>from two infinite populations</p></li>
</ul></li>
<li><p>but, in Neyman’s randomized experiment setup:</p>
<ul>
<li><p>the population is finite</p></li>
<li><p>the treatment and control groups are not independent</p></li>
<li><p>if one subject is in treatment, that same subject cannot also be in control</p></li>
</ul></li>
<li><p>so, the usual textbook justification is technically wrong for randomized experiments</p></li>
</ul></td>
</tr>
<tr>
<td>The “Minor Miracle”</td>
<td colspan="4"><ul>
<li><p>Freedman, Pisani, and Purves explain the result using a box-of-tickets model</p>
<ul>
<li><p>each ticket represents one subject</p></li>
<li><p>each ticket has two numbers</p></li>
</ul></li>
</ul>
<p><span class="math display"><em>A</em> = <em>o</em><em>u</em><em>t</em><em>c</em><em>o</em><em>m</em><em>e</em> <em>u</em><em>n</em><em>d</em><em>e</em><em>r</em> <em>t</em><em>r</em><em>e</em><em>a</em><em>t</em><em>m</em><em>e</em><em>n</em><em>t</em> <em>A</em></span></p>
<p><span class="math display"><em>B</em> = <em>o</em><em>u</em><em>t</em><em>c</em><em>o</em><em>m</em><em>e</em> <em>u</em><em>n</em><em>d</em><em>e</em><em>r</em> <em>t</em><em>r</em><em>e</em><em>a</em><em>t</em><em>m</em><em>e</em><em>n</em><em>t</em> <em>B</em></span></p>
<ul>
<li><p>but, once a subject is assigned to one treatment, only one number is visible</p></li>
<li><p>the other is hidden</p></li>
<li><p>this model makes potential outcomes easier to see visually</p></li>
</ul>
<ul>
<li><p>the usual standard error makes <strong>two mistakes</strong>:</p></li>
</ul>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr>
<th><strong>Mistake</strong></th>
<th><strong>What it does</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>treats sampling as if it were <strong>with replacement</strong></td>
<td>makes the SE too big</td>
</tr>
<tr>
<td>treats the two sample means as <strong>independent</strong></td>
<td>makes the SE smaller</td>
</tr>
</tbody>
</table>
<ul>
<li><p>the surprising result is that these two mistakes partly cancel</p></li>
<li><p>this is why the ordinary two-sample standard-error formula can still be usable for randomized experiments</p></li>
<li><p>Freedman, Pisani, and Purves describe this as a “minor miracle”</p></li>
</ul></td>
</tr>
<tr>
<td>When the Usual Variance Estimator Works</td>
<td colspan="4"><ul>
<li><p><strong>Case 1: Constant additive treatment effect</strong></p>
<ul>
<li><p>this means every unit is affected by the same amount</p></li>
<li><p>example:</p>
<ul>
<li><p>‘everyone improves by exactly 5 points under treatment’</p></li>
</ul></li>
<li><p>then the usual variance estimator is <strong>unbiased</strong></p></li>
<li><p>so, it estimates the variance correctly on average</p></li>
</ul></li>
<li><p><strong>Case 2: Heterogeneous treatment effects</strong></p>
<ul>
<li><p>this means treatment effects vary across units</p></li>
<li><p>example:</p>
<ul>
<li><p>some people improve a lot</p></li>
<li><p>some improve a little</p></li>
<li><p>some may get worse</p></li>
</ul></li>
<li><p>then, the usual variance estimator is generally <strong>conservative</strong></p></li>
<li><p>it tends to overestimate variance by an amount related to the finite-population variance of individual treatment effects:</p></li>
</ul></li>
</ul>
<blockquote>
<p><span class="math display">$$conservative\ bias\  \approx \ \frac{\sigma_{\Delta}^{2}}{N}$$</span></p>
</blockquote>
<ul>
<li><p>where:</p></li>
</ul>
<blockquote>
<p><span class="math display">$$\sigma\tilde{}²\_\Delta\ measures\ how\ much\ treatment\ effects\ vary\ across\ units\ $$</span></p>
</blockquote>
<p><span class="math display"><em>N</em> <em>i</em><em>s</em> <em>t</em><em>h</em><em>e</em> <em>n</em><em>u</em><em>m</em><em>b</em><em>e</em><em>r</em> <em>o</em><em>f</em> <em>s</em><em>u</em><em>b</em><em>j</em><em>e</em><em>c</em><em>t</em><em>s</em> <em>i</em><em>n</em> <em>t</em><em>h</em><em>e</em> <em>f</em><em>i</em><em>n</em><em>i</em><em>t</em><em>e</em> <em>p</em><em>o</em><em>p</em><em>u</em><em>l</em><em>a</em><em>t</em><em>i</em><em>o</em><em>n</em></span></p>
<ul>
<li><p>if N is much larger than the treatment and control sample sizes, this bias becomes negligible</p></li>
</ul></td>
</tr>
<tr>
<td>Important Warning About Pooled Variance</td>
<td colspan="4"><ul>
<li><p>the article also notes a technical caution:</p>
<ul>
<li><p>Neyman did not study the pooled variance estimator</p></li>
<li><p>the pooled estimator can behave differently</p></li>
</ul></li>
<li><p>if treatment and control group sizes are unequal and treatment effects are heterogeneous, the pooled estimator may be:</p>
<ul>
<li><p>conservative</p></li>
<li><p>anticonservative</p></li>
</ul></li>
<li><p>Anticonservative means it can underestimate uncertainty which is dangerous because it can make results look more precise than they really are</p></li>
</ul></td>
</tr>
<tr>
<td>The Article’s Broader Argument</td>
<td colspan="4"><ul>
<li><p>most introductory statistics textbooks still explain two-sample tests using independent samples from hypothetical populations</p></li>
<li><p>the authors think this misses an important opportunity</p></li>
<li><p>in randomized experiments, we often do not need to imagine hypothetical superpopulations.</p></li>
<li><p>we can instead say:</p>
<ul>
<li><p>the experimental units are the population</p></li>
<li><p>random assignment creates the uncertainty</p></li>
<li><p>causal inference is hard because each unit has missing potential outcomes</p></li>
</ul></li>
<li><p>the authors do not claim randomization-based inference is always better than superpopulation inference</p></li>
<li><p>their claim is narrower:</p></li>
<li><p>Students should learn both frameworks.</p>
<ul>
<li><p>randomization-based causal inference is currently underemphasized</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Conceptual Diagram</td>
<td colspan="4"><p>Finite population of N units</p>
<p>each unit has two potential outcomes</p>
<p><span class="math inline"> <em>y</em><sub><em>i</em></sub>(1)</span> and <span class="math inline"><em>y</em><sub><em>i</em></sub>(0)</span></p>
<p>Random assignment</p>
<p>Treatment group: observe <span class="math inline"><em>y</em><sub><em>i</em></sub>(1)</span></p>
<p>Control group: observe <span class="math inline"><em>y</em><sub><em>i</em></sub>(0)</span></p>
<p>But for each unit:</p>
<p>one potential outcome is observed</p>
<p>one potential outcome is missing</p>
<p>Estimate:</p>
<p>ATE_hat = treatment mean − control mean</p>
<p>Core result:</p>
<p>ATE_hat is unbiased for ATE</p>
<p>Standard-error result:</p>
<p>usual SE formula often works</p>
<p>because two errors partly cancel</p></td>
</tr>
<tr>
<td>Most Important Takeaway</td>
<td colspan="4"><ul>
<li><p>Neyman’s 1923 contribution is not just historical, it gives a clean way to understand randomized experiments:</p>
<ul>
<li><p>causal uncertainty comes from random assignment</p></li>
<li><p>each unit has multiple potential outcomes</p></li>
<li><p>only one outcome is observed</p></li>
<li><p>the difference in means is unbiased for the average treatment effect</p></li>
<li><p>the usual standard error can be justified in a finite-population framework</p></li>
<li><p>but its behavior depends on treatment-effect heterogeneity</p></li>
</ul></li>
<li><p>the authors’ educational point is that these ideas do not have to be hidden behind advanced notation</p></li>
<li><p>they can be taught with boxes, tickets, diagrams, and careful explanation</p></li>
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
<th colspan="2">Introduction to the Potential Outcomes Framework</th>
</tr>
</thead>
<tbody>
<tr>
<td>Notation and Definitions</td>
<td><p>Treatment assignment:</p>
<ul>
<li><p>Binary treatment: <span class="math inline"><em>D</em><sub><em>i</em></sub> ∈ {0, 1}</span></p></li>
<li><p>Framework can be extended to continuous treatments (or doses)</p></li>
</ul>
<p>Potential outcome:</p>
<ul>
<li><p><span class="math inline"><em>Y</em><sub><em>i</em></sub>(1)</span>: outcome if unit i receives treatment</p></li>
<li><p><span class="math inline"><em>Y</em><sub><em>i</em></sub>(0)</span>: outcome if unit i does not receive treatment</p></li>
</ul>
<p>Observed outcome:</p>
<p><span class="math display"><em>Y</em><sub><em>i</em></sub> = <em>D</em><sub><em>i</em></sub> ⋅ <em>Y</em><sub><em>i</em></sub>(1) + (1 − <em>D</em><sub><em>i</em></sub>) ⋅ <em>Y</em><sub><em>i</em></sub>(0)</span></p></td>
</tr>
<tr>
<td>Neyman’s Urn Model</td>
<td><img src="generated_media\DATA735_week02_notes\media\image1.png" style="width:4.51736in;height:3.27147in" /></td>
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
<th>Example: Get Out the Vote Campaign</th>
<th><table>
<colgroup>
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th><strong>Voter<br />
</strong></th>
<th colspan="2"><strong>Treatment (received GOTV call?)</strong></th>
<th><strong>Y_i(1) (turnout with call)</strong></th>
<th><strong>Y_i(0) (turnout without call)</strong></th>
<th><strong>Observed turnout (Y_i)<br />
</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><strong>Alice</strong></td>
<td>1</td>
<td>1 (votes)</td>
<td>0 (doesn’t vote)</td>
<td>1</td>
</tr>
<tr>
<td colspan="2"><strong>Bob</strong></td>
<td>0</td>
<td>0 (doesn’t vote)</td>
<td>0 (doesn’t vote)</td>
<td>0</td>
</tr>
<tr>
<td colspan="2"><strong>Carol</strong></td>
<td>1</td>
<td>1 (votes)</td>
<td>1 (votes anyway)</td>
<td>1</td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr>
<td>Individual Treatment Effects (ITEs)</td>
<td><p>individual treatment effect (ITE):</p>
<p><span class="math display"><em>τ</em><sub><em>i</em></sub> = <em>Y</em><sub><em>i</em></sub>(1) − <em>Y</em><sub><em>i</em></sub>(0)</span></p>
<p>alternative definitions are possible:</p>
<p><span class="math display">$$\frac{Y_{i(1)}}{Y_{i}(0)}\ \ (less\ common)$$</span></p>
<p>F_{Y_i(1)}^{-1}(p) - F_{Y_i(0)}^{-1}(p) (quantile p effect)</p>
<p>the causal effect captures what would happen to the same individual under two alternative scenarios:</p>
<p>treated vs. untreated</p>
<p>counterfactual by definition!</p></td>
</tr>
</tbody>
</table>
