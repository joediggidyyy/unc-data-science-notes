> Markdown version for convenient browsing. Original files:
> - PDF: [DATA735_week01_notes.pdf](../DATA735_week01_notes.pdf)
> - DOCX: [DATA735_week01_notes.docx](DATA735_week01_notes.docx)

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
<th colspan="2">Causal Inference</th>
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
<li><p>what is Causality, and how is it different from correlation?</p></li>
<li><p>foundational concepts of causal inference</p></li>
<li><p>avoiding common pitfalls</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">This Week’s Goals</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>distinguish between descriptive, predictive, and causal analyses</p></li>
<li><p>the notion of confounding</p></li>
<li><p>the role of un-observables in causal attribution</p></li>
<li><p>the notion of balance</p></li>
<li><p>the value of randomization in causal attribution</p></li>
<li><p>packages needed</p>
<ol type="1">
<li><p>R: tidyverse</p></li>
<li><p>R: gridExtra</p></li>
</ol></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Readings</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><p>Causal Inference: Chapter 1</p>
<blockquote>
<p>Scott Cunningham</p>
<p>ISBN 9780300251685</p>
</blockquote>
<p><a href="https://mixtape.scunning.com/01-introduction">https://mixtape.scunning.com/01-introduction</a></p></td>
</tr>
<tr>
<td>Chapter 1 Summary</td>
<td colspan="4">this chapter argues that <strong>causal</strong> <strong>inference</strong> is <strong>necessary</strong> because real-world <strong>data</strong> often <strong>contain</strong> strategic human <strong>choices</strong>, hidden <strong>confounders</strong>, and <strong>misleading</strong> <strong>correlations</strong>, so researchers need <strong>theory</strong>, <strong>assumptions</strong>, and <strong>careful</strong> research <strong>designs</strong> to <strong>estimate</strong> <strong>causal</strong> <strong>effects</strong> credibly</td>
</tr>
<tr>
<td>Introduction</td>
<td colspan="4"><ul>
<li><p>this chapter explains <strong>why</strong> <strong>causal</strong> <strong>inference</strong> <strong>matters</strong></p>
<ul>
<li><p><strong>we</strong> often <strong>want</strong> to <strong>know</strong> whether <span class="math inline"><strong>X</strong></span> <strong>causes</strong> <span class="math inline"><strong>Y</strong></span></p></li>
<li><p><strong>most</strong> <strong>data</strong> only <strong>show</strong> that <span class="math inline"><strong>X</strong></span> and <span class="math inline"><strong>Y</strong></span> <strong>move</strong> <strong>together</strong></p></li>
<li><p><strong>correlation</strong> may (or may not) <strong>suggest</strong> <strong>causality</strong></p></li>
</ul></li>
<li><p>causal inference gives <strong>researchers</strong> <strong>tools</strong> for <strong>estimating</strong> <strong>causal</strong> <strong>effects</strong> when <strong>randomized</strong> <strong>experiments</strong> are <strong>not</strong> <strong>available</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Core Concepts Glossary</td>
<td colspan="4"><p><strong>causal inference</strong></p>
<blockquote>
<p><strong>estimating</strong> whether one thing <strong>causes</strong> <strong>another</strong> thing</p>
</blockquote>
<p><strong>correlation</strong></p>
<blockquote>
<p><strong>two</strong> variables <strong>move</strong> <strong>together</strong></p>
<p><strong>correlation</strong> alone does <strong>not</strong> prove <strong>causation</strong></p>
</blockquote>
<p><strong>causation</strong></p>
<blockquote>
<p>one <strong>variable</strong> <strong>directly</strong> <strong>affects</strong> another <strong>variable</strong></p>
</blockquote>
<p><strong>observational data</strong></p>
<blockquote>
<p><strong>data</strong> where the <strong>researcher</strong> <strong>observes</strong> what happened</p>
<p>does <strong>not</strong> <strong>control</strong> <strong>treatment</strong> assignment</p>
</blockquote>
<p><strong>experimental data</strong></p>
<blockquote>
<p><strong>data</strong> where the <strong>researcher</strong> has some <strong>control</strong> over <strong>treatment</strong> <strong>assignment</strong></p>
</blockquote>
<p><strong>endogeneity</strong></p>
<blockquote>
<p>a <strong>variable</strong> is <strong>connected</strong> to <strong>hidden</strong> <strong>factors</strong> that also <strong>affect</strong> the <strong>outcome</strong></p>
<p>this <strong>makes</strong> causal <strong>interpretation</strong> <strong>difficult</strong></p>
</blockquote>
<p><strong>exogeneity</strong></p>
<blockquote>
<p>a variable <strong>changes</strong> <strong>independently</strong> of <strong>hidden</strong> <strong>factors</strong> that <strong>affect</strong> the <strong>outcome</strong></p>
<p>this <strong>makes</strong> causal <strong>interpretation</strong> more <strong>credible</strong></p>
</blockquote>
<p><strong>identification</strong></p>
<blockquote>
<p>process of <strong>showing</strong> that a <strong>research</strong> <strong>design</strong> can <strong>recover</strong> the <strong>causal</strong> <strong>effect</strong> of interest</p>
</blockquote>
<p><strong>ceteris paribus</strong> “All else equal.”</p>
<blockquote>
<p>a <strong>causal</strong> <strong>claim</strong> usually <strong>asks</strong> what <strong>happens</strong> when one thing <strong>changes</strong> while relevant <strong>other</strong> things <strong>stay</strong> <strong>fixed</strong></p>
</blockquote>
<p><strong>price elasticity of demand</strong></p>
<p><strong>measure</strong> of how much <strong>quantity</strong> <strong>demanded</strong> <strong>changes</strong> when <strong>price</strong> <strong>changes</strong></p></td>
</tr>
<tr>
<td>What is causal inference?</td>
<td colspan="4"><p><strong>causal</strong> <strong>inference</strong> is the <strong>process</strong> of using</p>
<ul>
<li><p><strong>theory</strong></p></li>
<li><p>institutional <strong>knowledge</strong></p></li>
<li><p><strong>research</strong> design</p></li>
<li><p><strong>data</strong></p></li>
<li><p>statistical <strong>methods</strong></p></li>
</ul>
<p>to <strong>estimate</strong> the <strong>effect</strong> of one thing on another</p>
<p>example</p>
<ul>
<li><p>does <strong>education</strong> increase <strong>income</strong>?</p></li>
<li><p>does a <strong>policy</strong> reduce <strong>crime</strong>?</p></li>
<li><p>does <strong>price</strong> affect <strong>demand</strong>?</p></li>
<li><p>does a <strong>medical</strong> <strong>treatment</strong> improve <strong>health</strong>?</p></li>
</ul>
<p>the author defines <strong>causal</strong> <strong>inference</strong> as</p>
<ul>
<li><p>using <strong>theory</strong> and <strong>deep</strong> <strong>contextual</strong> <strong>knowledge</strong> to <strong>estimate</strong> how <strong>events</strong> or <strong>choices</strong> <strong>affect</strong> an <strong>outcome</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Why this book exists</td>
<td colspan="4"><p>the author argues that <strong>many</strong> causal inference <strong>books</strong> are <strong>valuable</strong> but <strong>incomplete</strong> for <strong>applied</strong> <strong>learners</strong></p>
<ul>
<li><p>some <strong>books</strong> <strong>emphasize</strong></p>
<ul>
<li><p><strong>theory</strong></p></li>
<li><p><strong>potential</strong> <strong>outcomes</strong></p></li>
<li><p><strong>DAGs</strong></p></li>
<li><p><strong>econometrics</strong></p></li>
</ul></li>
</ul>
<p>the author wanted a <strong>book</strong> that <strong>combines</strong></p>
<ul>
<li><p>readable <strong>explanation</strong></p></li>
<li><p><strong>research</strong> <strong>design</strong></p></li>
<li><p>programming <strong>examples</strong></p></li>
<li><p><strong>real</strong> <strong>data</strong></p></li>
<li><p><strong>replication</strong></p></li>
<li><p>and <strong>practical</strong> <strong>implementation</strong></p></li>
</ul>
<p>the book is written for</p>
<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><ul>
<li><p><strong>practitioners</strong></p></li>
</ul></th>
<th><ul>
<li><p>social scientists</p></li>
</ul></th>
<th><ul>
<li><p><strong>industry</strong></p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td><ul>
<li><p>policymakers</p></li>
</ul></td>
<td><ul>
<li><p><strong>students</strong></p></li>
</ul></td>
<td><ul>
<li><p>usable tools</p></li>
</ul></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>Correlation is not Causation</td>
<td colspan="4"><p>common sense tells us</p>
<ul>
<li><p><strong>correlation</strong> does <strong>not</strong> mean <strong>causation</strong></p></li>
<li><p><strong>two</strong> things can <strong>move</strong> <strong>together</strong> <strong>without</strong> one <strong>causing</strong> the <strong>other</strong></p></li>
</ul>
<p>example</p>
<ul>
<li><p>rooster <strong>crows</strong> <span class="math inline">→</span> sun <strong>rises</strong></p></li>
<li><p><strong>rooster</strong> did <strong>not</strong> <strong>cause</strong> <strong>sunrise</strong>!</p></li>
</ul>
<p>conclusion</p>
<ul>
<li><p>simple <strong>correlation</strong> does <strong>not</strong> <strong>prove</strong> causal <strong>relationships</strong></p></li>
</ul></td>
</tr>
<tr>
<td>No Correlation does not mean No Causation</td>
<td colspan="4"><p>sometimes <strong>causality</strong> <strong>exists</strong> even when <strong>correlation</strong> is <strong>hard</strong> to <strong>see</strong></p>
<p>example</p>
<ul>
<li><p>imagine a <strong>sailor</strong> <strong>crossing</strong> a <strong>lake</strong></p>
<ul>
<li><p><strong>wind</strong> <strong>pushes</strong> the <strong>boat</strong></p></li>
<li><p><strong>sailor</strong> <strong>moves</strong> the <strong>rudder</strong> to <strong>cancel</strong> the <strong>wind</strong></p></li>
<li><p>the <strong>boat</strong> <strong>travels</strong> in a <strong>straight</strong> line</p></li>
</ul></li>
<li><p>an <strong>observer</strong> might <strong>think</strong></p>
<ul>
<li><p>“<em>the rudder has <strong>no</strong> <strong>effect</strong></em>”</p></li>
</ul></li>
</ul>
<ul>
<li><p>that would be <strong>wrong</strong></p>
<ul>
<li><p>the <strong>rudder</strong> is <strong>working</strong></p></li>
<li><p>its <strong>effect</strong> is <strong>hidden</strong> because the <strong>sailor</strong> <strong>adjusts</strong> it in <strong>response</strong> to the <strong>wind</strong></p></li>
</ul></li>
</ul>
<ul>
<li><p><strong>causal</strong> effect <strong>exists</strong>, but the <strong>observed</strong> <strong>correlation</strong> is <strong>canceled</strong> <strong>out</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Why Randomization Matters</td>
<td colspan="4"><p>the <strong>sailboat</strong> <strong>example</strong> shows why <strong>randomization</strong> is <strong>powerful</strong></p>
<ul>
<li><p>if the sailor <strong>randomly</strong> <strong>moved</strong> the rudder</p>
<ul>
<li><p><strong>observer</strong> would <strong>see</strong> the <strong>boat</strong> <strong>zigzag</strong></p></li>
<li><p><strong>relationship</strong> <strong>between</strong> rudder <strong>movement</strong> and boat <strong>direction</strong> would become <strong>visible</strong></p></li>
</ul></li>
<li><p>key <strong>idea</strong></p>
<ul>
<li><p><strong>randomness</strong> helps <strong>reveal</strong> causal <strong>effects</strong></p></li>
</ul></li>
<li><p>when <strong>people</strong> <strong>choose</strong> actions <strong>strategically</strong></p>
<ul>
<li><p>the <strong>data</strong> can <strong>hide</strong> causal <strong>relationships</strong></p></li>
</ul></li>
<li><p>when <strong>treatment</strong> is <strong>randomized</strong></p>
<ul>
<li><p>the <strong>researcher</strong> has a better <strong>chance</strong> of <strong>isolating</strong> the <strong>effect</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Optimization Makes Causal Inference Difficult</td>
<td colspan="4"><ul>
<li><p><strong>people</strong> make <strong>choices</strong> based on</p>
<ul>
<li><p><strong>goals</strong></p></li>
<li><p>constraints</p></li>
<li><p><strong>incentives</strong></p></li>
<li><p>expectations</p></li>
<li><p>private <strong>information</strong></p></li>
<li><p>and <strong>predicted</strong> <strong>outcomes</strong></p></li>
</ul></li>
<li><p>because of this</p>
<ul>
<li><p>many <strong>choices</strong> are <strong>endogenous</strong></p></li>
</ul></li>
<li><p>that <strong>means</strong></p>
<ul>
<li><p>the <strong>choice</strong> is <strong>connected</strong> to the <strong>outcome</strong> we are trying to <strong>study</strong></p></li>
</ul></li>
<li><p>this <strong>creates</strong> a major <strong>problem</strong></p>
<ul>
<li><p>if <strong>people</strong> <strong>choose</strong> <strong>treatment</strong> based on <strong>expected</strong> <strong>outcomes</strong></p>
<ul>
<li><p>treatment is <strong>not</strong> <strong>independent</strong> of the <strong>outcome</strong></p></li>
</ul></li>
</ul></li>
<li><p>meaning</p>
<ul>
<li><p>a simple <strong>correlation</strong> between <strong>choice</strong> and <strong>outcome cannot</strong> be <strong>assumed</strong> as <strong>causal</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Experimental Data vs. Observational Data</td>
<td colspan="4"><p>example</p>
<ul>
<li><p>a <strong>randomized</strong> medical <strong>experiment</strong></p></li>
<li><p>a <strong>field</strong> <strong>experiment</strong></p></li>
<li><p>a <strong>policy</strong> <strong>experiment</strong> with <strong>random</strong> <strong>assignment</strong></p></li>
</ul>
<p>this is often <strong>stronger</strong> for <strong>causal</strong> <strong>inference</strong> because</p>
<ul>
<li><p>the <strong>researcher</strong> has more <strong>control</strong> over <strong>how</strong> treatment is <strong>assigned</strong></p></li>
</ul>
<p>in <strong>observational</strong> data</p>
<ul>
<li><p>the <strong>researcher</strong></p>
<ul>
<li><p>usually does <strong>not</strong> <strong>control</strong> what <strong>happens</strong></p></li>
<li><p><strong>observes</strong> <strong>choices</strong> and <strong>outcomes</strong> <strong>after</strong> they occur</p></li>
</ul></li>
<li><p>examples</p>
<ul>
<li><p><strong>surveys</strong></p></li>
<li><p>administrative <strong>records</strong></p></li>
<li><p><strong>business</strong> data</p></li>
<li><p><strong>web</strong>-<strong>scraped</strong> data</p></li>
<li><p><strong>historical</strong> data</p></li>
</ul></li>
<li><p>most <strong>social</strong> <strong>science</strong> and <strong>business</strong> <strong>data</strong> are</p>
<ul>
<li><p><strong>observational</strong></p></li>
</ul></li>
<li><p><strong>observational</strong> <strong>data</strong> are</p>
<ul>
<li><p><strong>harder</strong> to use for <strong>causal</strong> <strong>claims</strong> because</p></li>
<li><p><strong>choices</strong> are often <strong>endogenous</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Causal Inference Needs Assumptions</td>
<td colspan="4"><ul>
<li><p><strong>causal</strong> <strong>inference</strong></p>
<ul>
<li><p><strong>not</strong> just <strong>mechanical</strong> <strong>statistics</strong></p></li>
</ul></li>
<li><p><strong>good</strong> causal <strong>research</strong> <strong>requires</strong></p>
<ul>
<li><p><strong>clear</strong> <strong>assumptions</strong></p></li>
<li><p><strong>theory</strong></p></li>
<li><p><strong>local</strong> <strong>knowledge</strong></p></li>
<li><p><strong>research</strong> <strong>design</strong></p></li>
<li><p><strong>honesty</strong> about <strong>uncertainty</strong></p></li>
<li><p><strong>process</strong>-<strong>oriented</strong> <strong>scientific</strong> <strong>attitude</strong></p></li>
</ul></li>
</ul>
<p>the <strong>author</strong> <strong>warns</strong> against</p>
<ul>
<li><p>trying to <strong>force</strong> <strong>results</strong> to <strong>match</strong> what the <strong>researcher</strong> <strong>wants</strong></p></li>
<li><p>causal <strong>methods</strong> are only <strong>credible</strong> when</p>
<ul>
<li><p>the <strong>researcher</strong> <strong>prioritizes</strong> correct <strong>method</strong> over desired <strong>outcome</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Example: Price Elasticity of Demand</td>
<td colspan="4"><ul>
<li><p>price <strong>elasticity</strong> of <strong>demand</strong> to show why <strong>causal</strong> <strong>inference</strong> is <strong>hard</strong></p></li>
<li><p>researchers <strong>want</strong> to <strong>know</strong></p>
<ul>
<li><p>if <strong>price</strong> <strong>changes</strong>, how much does <strong>quantity</strong> <strong>demanded</strong> <strong>change</strong>?</p></li>
</ul></li>
<li><p><strong>elasticity</strong> <strong>formula</strong></p></li>
</ul>
<p><span class="math display">$$\mathbf{\epsilon =}\frac{\mathbf{\partial logP}}{\mathbf{\partial logQ}}\ \ \ \ \ \ \ \ \ where,$$</span></p>
<p><span class="math display"><strong>Q</strong> = <em>q</em><em>u</em><em>a</em><em>n</em><em>t</em><em>i</em><em>t</em><em>y</em></span></p>
<p><span class="math display"><strong>P</strong> = <em>p</em><em>r</em><em>i</em><em>c</em><em>e</em></span></p>
<p><span class="math display"><strong>ϵ</strong> = <strong>p</strong><strong>r</strong><strong>i</strong><strong>c</strong><strong>e</strong> <strong>e</strong><strong>l</strong><strong>a</strong><strong>s</strong><strong>t</strong><strong>i</strong><strong>c</strong><strong>i</strong><strong>t</strong><strong>y</strong> <em>o</em><em>f</em> <em>d</em><em>e</em><em>m</em><em>a</em><em>n</em><em>d</em></span></p>
<ul>
<li><p>this <strong>measures</strong></p>
<ul>
<li><p>the percentage <strong>change</strong> in <strong>quantity</strong> associated with a percentage <strong>change</strong> in <strong>price</strong></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Why price and quantity data are not enough</td>
<td colspan="4"><ul>
<li><p>we do <strong>not</strong> <strong>directly</strong> <strong>observe</strong> a full <strong>demand</strong> <strong>curve</strong></p></li>
<li><p>instead we usually <strong>observe</strong> <strong>market</strong> <strong>equilibrium</strong> <strong>points</strong></p>
<ul>
<li><p><strong>one</strong> price</p></li>
<li><p><strong>one</strong> quantity</p></li>
</ul></li>
<li><p>those <strong>points</strong> may <strong>come</strong> <strong>from</strong></p>
<ul>
<li><p><strong>supply</strong> shifts</p></li>
<li><p><strong>demand</strong> shifts</p></li>
</ul></li>
<li><p><strong>connecting</strong> observed <strong>price</strong>-<strong>quantity</strong> points</p>
<ul>
<li><p>may <strong>not</strong> trace demand curve</p></li>
</ul></li>
<li><p>result</p>
<ul>
<li><p>a simple <strong>correlation</strong> between <strong>price</strong>-<strong>quantity</strong> may <strong>not</strong> estimate <strong>demand</strong> <strong>elasticity</strong></p></li>
</ul></li>
<li><p>to estimate <strong>demand</strong> <strong>elasticity</strong></p>
<ul>
<li><p>price <strong>variation</strong> must be <strong>independent</strong> of</p>
<ul>
<li><p><strong>supply</strong></p></li>
<li><p><strong>demand</strong></p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="5"><p>Causal Inference: Chapter 2</p>
<blockquote>
<p>Scott Cunningham</p>
<p>ISBN 9780300251685</p>
</blockquote>
<p><a href="https://mixtape.scunning.com/02-probability_and_regression">https://mixtape.scunning.com/02-probability_and_regression</a></p></td>
</tr>
<tr>
<td>Chapter 2 Summary</td>
<td colspan="4">Chapter 2 teaches the <strong>probability</strong>, <strong>expectation</strong>, <strong>variance</strong>, <strong>covariance</strong>, <strong>OLS</strong>, <strong>standard</strong> <strong>error</strong>, and <strong>regression</strong> anatomy <strong>tools</strong> needed for <strong>causal</strong> <strong>inference</strong>, while repeatedly <strong>emphasizing</strong> that regression only supports causal claims when the key assumption <span class="math inline"><strong>E</strong><strong>(</strong><strong>u</strong> <strong>∣</strong> <strong>x</strong><strong>)</strong> <strong>=</strong> <strong>0</strong></span><strong>is</strong> credible</td>
</tr>
<tr>
<td>Introduction</td>
<td colspan="4"><ul>
<li><p>this chapter reviews the probability and regression tools needed for causal inference</p>
<ul>
<li><p>regression can estimate useful relationships</p></li>
<li><p>causal interpretation depends on assumptions</p></li>
</ul></li>
<li><p>the most important assumption in the chapter is</p></li>
</ul>
<p><span class="math display"><em>E</em>(<em>u</em> ∣ <em>x</em>) = 0</span></p>
<ul>
<li><p>this means</p>
<ul>
<li><p>the unobserved causes of <span class="math inline"><em>y</em></span> must not systematically change with <span class="math inline"><em>x</em></span></p></li>
</ul></li>
<li><p>if this fails</p>
<ul>
<li><p>regression may still produce a number</p></li>
<li><p>that number may not be causal</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Why Probability Comes First</td>
<td colspan="4"><p>causal inference uses statistical models</p>
<ul>
<li><p>those models depend on probability concepts like</p>
<ul>
<li><p>random processes</p></li>
<li><p>sample spaces</p></li>
<li><p>independence</p></li>
<li><p>conditional probability</p></li>
<li><p>expected value</p></li>
<li><p>variance</p></li>
<li><p>covariance</p></li>
<li><p>regression</p></li>
</ul></li>
<li><p>a random process</p>
<ul>
<li><p>can be repeated</p></li>
<li><p>may produce different outcomes each time</p></li>
</ul></li>
<li><p>sample space</p>
<ul>
<li><p>the set of all possible outcomes</p></li>
</ul></li>
<li><p>examples</p>
<ul>
<li><p>discrete</p>
<ul>
<li><p>coin flip</p></li>
<li><p>die roll</p></li>
<li><p>card draw</p></li>
</ul></li>
<li><p>continuous</p>
<ul>
<li><p>gas price</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Independence</td>
<td colspan="4"><ul>
<li><p>two events are statistically independent if</p>
<ul>
<li><p>knowing one happened does not change the probability that the other happened</p></li>
</ul></li>
</ul>
<p><span class="math display"><em>P</em><em>r</em>(<em>A</em> ∣ <em>B</em>) = <em>P</em><em>r</em>(<em>A</em>)</span></p>
<ul>
<li><p>meaning</p>
<ul>
<li><p>the probability of <span class="math inline"><em>A</em></span>, given <span class="math inline"><em>B</em></span>, is the same as the probability of <span class="math inline"><em>A</em></span> alone</p></li>
</ul></li>
</ul>
<ul>
<li><p>example</p>
<ul>
<li><p>independent</p>
<ul>
<li><p>rolling a 3 on one die does not affect rolling a 5 on another die</p></li>
</ul></li>
<li><p>not independent</p>
<ul>
<li><p>drawing cards without replacement</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Joint Probability</td>
<td colspan="4"><ul>
<li><p>joint probability</p>
<ul>
<li><p>the probability that two events both happen</p></li>
</ul></li>
<li><p>for independent events</p></li>
</ul>
<p><span class="math display"><em>P</em><em>r</em>(<em>A</em>, <em>B</em>) = <em>P</em><em>r</em>(<em>A</em>)<em>P</em><em>r</em>(<em>B</em>)</span></p>
<ul>
<li><p>example</p>
<ul>
<li><p>if</p>
<ul>
<li><p>Cleveland must win 3 games in a row</p></li>
<li><p>each game has probability 0.5</p></li>
</ul></li>
<li><p>then</p></li>
</ul></li>
</ul>
<p><span class="math display">$$\mathbf{(0.5)\hat{}3 = 0.125}$$</span></p>
<ul>
<li><p>so, the probability is</p></li>
</ul>
<p><span class="math display"><strong>12.5</strong><strong>%</strong></span></p>
<ul>
<li><p>key idea</p>
<ul>
<li><p>when independent events must all occur</p>
<ul>
<li><p>multiply probabilities</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Conditional Probability</td>
<td colspan="4"><p>conditional probability asks:</p>
<ul>
<li><p>what is the probability of one event, given that another event already happened?</p></li>
<li><p>Formula:</p></li>
</ul>
<p><span class="math display"><strong>P</strong><strong>r</strong><strong>(</strong><strong>B</strong><strong>∣</strong><strong>A</strong><strong>)</strong> <strong>=</strong> <strong>P</strong><strong>r</strong><strong>(</strong><strong>A</strong><strong>)</strong><strong>P</strong><strong>r</strong><strong>(</strong><strong>A</strong><strong>,</strong> <strong>B</strong><strong>)</strong></span></p>
<ul>
<li><p>example from the chapter</p>
<ul>
<li><p>A: Texas makes a great bowl game</p></li>
<li><p>B: the coach is rehired</p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>Pr</strong> (<strong>A</strong>) <strong>=</strong> <strong>0.6</strong>             <strong>P</strong><strong>r</strong><strong>(</strong><strong>B</strong><strong>)</strong> <strong>=</strong> <strong>0.8</strong></span></p>
<p><span class="math display"><strong>P</strong><strong>r</strong><strong>(</strong><strong>A</strong><strong>,</strong> <strong>B</strong><strong>)</strong> <strong>=</strong> <strong>0.5</strong></span></p>
<ul>
<li><p>then</p></li>
</ul>
<p><span class="math display">$$\mathbf{\Pr}\left( \mathbf{B}\mid\mathbf{A} \right)\mathbf{=}\frac{\mathbf{0.6}}{\mathbf{0.5}}\mathbf{= 0.83}$$</span></p>
<ul>
<li><p>so</p>
<ul>
<li><p>if Texas made a great bowl game</p></li>
<li><p>the probability the coach is rehired is about 83%</p></li>
<li><p>but:</p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>P</strong><strong>r</strong><strong>(</strong><strong>A</strong><strong>∣</strong><strong>B</strong><strong>)</strong> <strong>=</strong> <strong>0.8</strong> <strong>0.5</strong>  <strong>=</strong> <strong>0.625</strong></span></p>
<ul>
<li><p>so</p></li>
<li><p>if the coach was rehired</p></li>
<li><p>the probability Texas made a great bowl game is about 63%</p></li>
<li><p>important</p></li>
</ul>
<p><span class="math display"><strong>Pr</strong> (<strong>B</strong> ∣ <strong>A</strong>) <strong>≠</strong> <strong>P</strong><strong>r</strong><strong>(</strong><strong>A</strong><strong>∣</strong><strong>B</strong><strong>)</strong></span></p></td>
</tr>
<tr>
<td>Bayes’ Rule</td>
<td colspan="4"><p>lets us update beliefs after receiving new information</p>
<ul>
<li><p>basic form</p></li>
</ul>
<p><span class="math display">$$\mathbf{Pr(A}\mathbf{\mid}\mathbf{B) =}\frac{\mathbf{Pr(B}\mathbf{\mid}\mathbf{A)Pr(A)}}{\mathbf{Pr(B)}}$$</span></p>
<ul>
<li><p>expanded form</p></li>
</ul>
<p><span class="math display">$$\mathbf{P}\mathbf{r}\left( \mathbf{A}\mid\mathbf{B} \right)\mathbf{=}\frac{\mathbf{Pr(B}\mathbf{\mid}\mathbf{A)Pr(A)}}{\mathbf{\Pr}\left( \mathbf{B}\mid\mathbf{A} \right)\mathbf{\Pr}\left( \mathbf{A} \right)\mathbf{+ Pr(B}\mathbf{\mid \sim}\mathbf{A)Pr(\sim A)}}\mathbf{\ }$$</span></p>
<ul>
<li><p>meaning</p></li>
</ul>
<p><span class="math display"><strong>p</strong><strong>o</strong><strong>s</strong><strong>t</strong><strong>e</strong><strong>r</strong><strong>i</strong><strong>o</strong><strong>r</strong> <strong>b</strong><strong>e</strong><strong>l</strong><strong>i</strong><strong>e</strong><strong>f</strong> <strong>=</strong> <strong>u</strong><strong>p</strong><strong>d</strong><strong>a</strong><strong>t</strong><strong>e</strong><strong>d</strong> <strong>b</strong><strong>e</strong><strong>l</strong><strong>i</strong><strong>e</strong><strong>f</strong> <strong>a</strong><strong>f</strong><strong>t</strong><strong>e</strong><strong>r</strong> <strong>s</strong><strong>e</strong><strong>e</strong><strong>i</strong><strong>n</strong><strong>g</strong> <strong>e</strong><strong>v</strong><strong>i</strong><strong>d</strong><strong>e</strong><strong>n</strong><strong>c</strong><strong>e</strong></span></p>
<p>Bayes’ rule helps us reason from an observed effect back toward possible causes</p></td>
</tr>
<tr>
<td>Monty Hall Example</td>
<td colspan="4"><p>the Monty Hall problem shows why conditional probability is unintuitive</p>
<p>the problem</p>
<ul>
<li><p>there are 3 doors</p>
<ul>
<li><p>one has money</p></li>
<li><p>two have goats</p></li>
</ul></li>
<li><p>you choose one door</p></li>
<li><p>Monty opens another door and shows a goat</p>
<ul>
<li><p>you can stay or switch</p></li>
</ul></li>
<li><p>many people think</p></li>
</ul>
<p>“Now there are two doors, so it must be 50–50.”</p>
<ul>
<li><p>that is wrong</p>
<ul>
<li><p>your original door still has probability <span class="math inline">$\frac{\mathbf{1}}{\mathbf{3}}$</span></p></li>
<li><p>the other unopened door has probability <span class="math inline">$\frac{2}{3}$</span></p></li>
</ul></li>
<li><p>you should switch</p>
<ul>
<li><p>because Monty’s action gives information</p></li>
<li><p>he does not open doors randomly</p></li>
<li><p>he opens a door he knows has a goat</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Summation Notation</td>
<td colspan="4"><ul>
<li><p>summation symbol</p></li>
</ul>
<p><span class="math display">∑</span></p>
<ul>
<li><p>example</p></li>
</ul>
<p><span class="math display">$$\sum_{i = 1}^{n}{x_{i} = x_{1} + x_{2} + \ldots + x_{n}}$$</span></p>
<ul>
<li><p>the sample mean is</p></li>
</ul>
<p><span class="math display">$$\overline{x} = \frac{1}{n}\sum_{i = 1}^{n}x_{i}$$</span></p>
<ul>
<li><p>a key property</p></li>
</ul>
<p><span class="math display">$$\sum_{i = 1}^{n}{(x_{i} - \overline{x}) = 0}$$</span></p>
<ul>
<li><p>this implies</p>
<ul>
<li><p>deviations from the mean always sum to zero</p></li>
</ul></li>
<li><p>this matters because</p>
<ul>
<li><p>regression uses deviations from means to estimate slopes</p></li>
</ul></li>
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
<th>Expected Value</th>
<th><ul>
<li><p>the probability-weighted average of possible outcomes</p></li>
</ul>
<p><span class="math display">$$\mathbf{E}\left( \mathbf{X} \right)\mathbf{=}\sum_{\mathbf{j = 1}}^{\mathbf{k}}{\mathbf{x}_{\mathbf{j}}\mathbf{\ f(}\mathbf{x}_{\mathbf{j}}\mathbf{)}}$$</span></p>
<ul>
<li><p>example</p>
<ul>
<li><p>if <span class="math inline"><strong>X</strong></span> can be:</p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>−</strong><strong>1</strong>   <strong>w</strong><strong>i</strong><strong>t</strong><strong>h</strong> <strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>a</strong><strong>b</strong><strong>i</strong><strong>l</strong><strong>i</strong><strong>t</strong><strong>y</strong>    <strong>0.3</strong></span></p>
<p><span class="math display"><strong>0</strong>      <strong>w</strong><strong>i</strong><strong>t</strong><strong>h</strong> <strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>a</strong><strong>b</strong><strong>i</strong><strong>l</strong><strong>i</strong><strong>t</strong><strong>y</strong>    <strong>0.3</strong></span></p>
<p><span class="math display"><strong>2</strong>     <strong>w</strong><strong>i</strong><strong>t</strong><strong>h</strong> <strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>a</strong><strong>b</strong><strong>i</strong><strong>l</strong><strong>i</strong><strong>t</strong><strong>y</strong>    <strong>0.4</strong></span></p>
<ul>
<li><p>then</p></li>
</ul>
<p><span class="math display"><strong>E</strong><strong>(</strong><strong>X</strong><strong>)</strong> <strong>=</strong> <strong>(</strong><strong>−</strong><strong>1</strong><strong>)</strong><strong>(</strong><strong>0.3</strong><strong>)</strong> <strong>+</strong> <strong>(</strong><strong>0</strong><strong>)</strong><strong>(</strong><strong>0.3</strong><strong>)</strong> <strong>+</strong> <strong>(</strong><strong>2</strong><strong>)</strong><strong>(</strong><strong>0.4</strong><strong>)</strong> <strong>=</strong> <strong>0.5</strong></span></p>
<ul>
<li><p>so, the expected value, <span class="math inline"><strong>0.5</strong></span></p>
<ul>
<li><p>is a population concept</p></li>
<li><p>describes the average value across the full probability distribution</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Variance</td>
<td><p>variance measures spread</p>
<ul>
<li><p>population variance</p></li>
</ul>
<p><span class="math display"><strong>V</strong><strong>(</strong><strong>W</strong><strong>)</strong> <strong>=</strong> <strong>E</strong><strong>[</strong>(<strong>W</strong> <strong>−</strong> <strong>E</strong>(<strong>W</strong>))<sup><strong>2</strong></sup><strong>]</strong></span></p>
<ul>
<li><p>equivalent formula</p></li>
</ul>
<p><span class="math display">$$\mathbf{V(W) = E(W\hat{}2) - E(W)\hat{}2}$$</span></p>
<ul>
<li><p>sample variance</p></li>
</ul>
<p><span class="math display">$${\widehat{\mathbf{S}}}^{\mathbf{2}}\mathbf{=}\frac{\mathbf{1}}{\mathbf{n - 1}}\sum_{\mathbf{i = 1}}^{\mathbf{n}}{\mathbf{}\left( \mathbf{x}_{\mathbf{i}}\mathbf{ - x} \right)^{\mathbf{2}}}$$</span></p></td>
</tr>
<tr>
<td>Covariance and Correlation</td>
<td><ul>
<li><p>measures whether two variables move together</p></li>
</ul>
<p><span class="math display"><strong>C</strong><strong>(</strong><strong>X</strong><strong>,</strong> <strong>Y</strong><strong>)</strong> <strong>=</strong> <strong>E</strong><strong>(</strong><strong>X</strong> <strong>Y</strong><strong>)</strong> <strong>−</strong> <strong>E</strong><strong>(</strong><strong>X</strong><strong>)</strong><strong>E</strong><strong>(</strong><strong>Y</strong><strong>)</strong></span></p>
<ul>
<li><p>if covariance is positive</p>
<ul>
<li><p><span class="math inline"><strong>X</strong></span> and <span class="math inline"><strong>Y</strong></span> tend to move in the same direction</p></li>
</ul></li>
<li><p>if covariance is negative</p>
<ul>
<li><p><span class="math inline"><strong>X</strong></span> and <span class="math inline"><strong>Y</strong></span> tend to move in opposite directions</p></li>
</ul></li>
<li><p>but covariance is hard to interpret</p>
<ul>
<li><p>its size depends on the units of the variables</p></li>
</ul></li>
<li><p>correlation standardizes covariance</p></li>
</ul>
<p><span class="math display">$$\mathbf{Corr(X,Y) = \ \ }\frac{\mathbf{C(X,Y)}}{\sqrt{\mathbf{V(X)V(Y)}}}$$</span></p>
<p>​</p>
<ul>
<li><p>correlation is always between</p></li>
</ul>
<p><span class="math display"><strong>−</strong><strong>1</strong> <strong>a</strong><strong>n</strong><strong>d</strong> <strong>1</strong></span></p>
<p>important warning</p>
<ul>
<li><p>zero covariance does not always mean two variables are unrelated</p></li>
<li><p>they may have a nonlinear relationship</p></li>
</ul></td>
</tr>
<tr>
<td>Population Regression Model</td>
<td><p>the basic population model is:</p>
<p>the error term <span class="math inline"><strong>u</strong></span> contains other causes of <span class="math inline"><strong>y</strong></span> that are not included in the model</p>
<p><span class="math display"><strong>y</strong><strong>=</strong><strong>β</strong><sub><strong>0</strong></sub><strong>+</strong><strong>β</strong><sub><strong>1</strong></sub> <strong>x</strong> <strong>+</strong> <strong>u</strong><strong>,</strong>      <em>w</em><em>h</em><em>e</em><em>r</em><em>e</em></span></p>
<p><span class="math display"><strong>y</strong> = <em>o</em><em>u</em><em>t</em><em>c</em><em>o</em><em>m</em><em>e</em></span></p>
<p><span class="math display"><strong>x</strong> = <em>e</em><em>x</em><em>p</em><em>l</em><em>a</em><em>n</em><em>a</em><em>t</em><em>o</em><em>r</em><em>y</em> <em>v</em><em>a</em><em>r</em><em>i</em><em>a</em><em>b</em><em>l</em><em>e</em></span></p>
<p><span class="math display"><strong>β</strong><sub><strong>0</strong></sub> = <em>i</em><em>n</em><em>t</em><em>e</em><em>r</em><em>c</em><em>e</em><em>p</em><em>t</em></span></p>
<p><span class="math display"><strong>β</strong><sub><strong>1</strong></sub> = <em>s</em><em>l</em><em>o</em><em>p</em><em>e</em></span></p>
<p><span class="math display"><strong>u</strong> = <em>e</em><em>r</em><em>r</em><em>o</em><em>r</em> <em>t</em><em>e</em><em>r</em><em>m</em></span></p>
<ul>
<li><p>example</p>
<ul>
<li><p>if <span class="math inline"><strong>y</strong></span> is wages and <span class="math inline"><strong>x</strong></span> is schooling</p></li>
<li><p>then <span class="math inline"><strong>u</strong></span> may include</p>
<ul>
<li><p>ability</p></li>
<li><p>family background</p></li>
<li><p>motivation</p></li>
<li><p>school quality</p></li>
<li><p>luck</p></li>
<li><p>social networks</p></li>
</ul></li>
<li><p>the researcher</p>
<ul>
<li><p>observes <span class="math inline"><strong>x</strong></span> and <span class="math inline"><strong>y</strong></span></p></li>
<li><p>does not observe <span class="math inline"><strong>u</strong></span></p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Mean Independence and Zero Conditional Mean</td>
<td><ul>
<li><p>mean independence says</p></li>
</ul>
<p><span class="math display"><strong>E</strong>(<strong>u</strong>|<strong>x</strong>) <strong>=</strong> <strong>E</strong><strong>(</strong><strong>u</strong><strong>)</strong></span></p>
<ul>
<li><p>if we normalize</p></li>
</ul>
<p><span class="math display"><strong>E</strong>(<strong>u</strong>) <strong>=</strong> <strong>0</strong></span></p>
<p>zero conditional mean assumption</p>
<ul>
<li><p>we get</p></li>
</ul>
<p><span class="math display"><strong>E</strong>(<strong>u</strong>|<strong>x</strong>) <strong>=</strong> <strong>0</strong></span></p>
<ul>
<li><p>meaning</p>
<ul>
<li><p>the average value of the unobserved error is the same for every value of <span class="math inline"><strong>x</strong></span></p></li>
</ul></li>
<li><p>example</p>
<ul>
<li><p>if studying schooling and wages</p></li>
<li><p>this assumption would require average unobserved ability to be the same across schooling levels</p></li>
<li><p>that is a strong assumption and may fail because people choose schooling partly based on</p>
<ul>
<li><p>ability</p></li>
<li><p>ambition</p></li>
<li><p>family resources</p></li>
<li><p>expectations</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Ordinary Least Squares</td>
<td><ul>
<li><p>OLS estimates the line</p></li>
</ul>
<p><span class="math display">$$\mathbf{y}\mathbf{}\mathbf{=}\widehat{\mathbf{\beta}}\mathbf{}_{\mathbf{0}}\mathbf{}\mathbf{+}\widehat{\mathbf{\beta}}\mathbf{}_{\mathbf{1}}\mathbf{}\mathbf{x}$$</span></p>
<ul>
<li><p>slope estimate</p></li>
</ul>
<p><span class="math display">$${\widehat{\mathbf{\beta}}}_{\mathbf{1}}\mathbf{=}\frac{\sum_{\mathbf{i = 1}}^{\mathbf{n}}{\mathbf{(}\mathbf{x}_{\mathbf{i}}\mathbf{-}\overline{\mathbf{x}}\mathbf{)(}\mathbf{y}_{\mathbf{i}}\mathbf{-}\overline{\mathbf{y}}\mathbf{)}}}{\sum_{\mathbf{i = 1}}^{\mathbf{n}}\left( \mathbf{x}_{\mathbf{i}}\mathbf{-}\overline{\mathbf{x}} \right)^{\mathbf{2}}}$$</span></p>
<ul>
<li><p>can also be described</p></li>
</ul>
<p><span class="math display">$${\widehat{\mathbf{\beta}}}_{\mathbf{1}}\mathbf{=}\frac{\mathbf{Sample\ covariance\ of\ x\ and\ y}}{\mathbf{Sample\ variance\ of\ x}}$$</span></p>
<ul>
<li><p>OLS needs variation in <span class="math inline"><strong>x</strong></span></p></li>
<li><p>if everyone has the same value of <span class="math inline"><strong>x</strong></span><strong>,</strong> the slope cannot be estimated</p></li>
</ul></td>
</tr>
<tr>
<td>Fitted Values and Residuals</td>
<td><ul>
<li><p>a fitted value is the model’s prediction</p></li>
</ul>
<p><span class="math display">$${\widehat{\mathbf{y}}}_{\mathbf{i}}\mathbf{=}{\widehat{\mathbf{\beta}}}_{\mathbf{0}}\mathbf{+}{\widehat{\mathbf{\beta}}}_{\mathbf{1}}\mathbf{x}_{\mathbf{i}}$$</span></p>
<p>​</p>
<ul>
<li><p>a residual is the prediction mistake</p></li>
</ul>
<p><span class="math display">$${\widehat{\mathbf{u}}}_{\mathbf{i}}\mathbf{=}\mathbf{y}_{\mathbf{i}}\mathbf{-}{\widehat{\mathbf{y}}}_{\mathbf{i}}$$</span></p>
<ul>
<li><p>error term: <span class="math inline"><strong>u</strong><sub><strong>i</strong></sub></span></p>
<ul>
<li><p>unobserved</p></li>
<li><p>part of the population model</p></li>
<li><p>contains omitted causes of y</p></li>
</ul></li>
</ul>
<p>the error term and the residual are not the same thing</p>
<ul>
<li><p>residual: <span class="math inline">${\widehat{\mathbf{u}}}_{\mathbf{i}}$</span></p>
<ul>
<li><p>observed after regression</p></li>
<li><p>calculated from data</p></li>
<li><p>equals the model’s prediction error</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>What OLS Minimizes</td>
<td><ul>
<li><p>OLS chooses the intercept and slope that minimize the sum of squared residuals</p></li>
</ul>
<p><span class="math display">$$\sum_{\mathbf{i = 1}}^{\mathbf{n}}{\widehat{\mathbf{u}}}_{\mathbf{i}}^{\mathbf{2}}$$</span></p>
<p>it is called least squares because it chooses the line that makes squared prediction errors as small as possible among linear fits</p></td>
</tr>
<tr>
<td></td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td></td>
<td><ul>
<li></li>
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
<th><p>Demand Model</p>
<p>without both the estimate may be misleading</p></th>
<th><ul>
<li><p>possible econometric demand model</p></li>
</ul>
<p><span class="math inline"><strong>l</strong><strong>o</strong><strong>g</strong><strong>Q</strong><strong>d</strong> <strong>=</strong> <strong>α</strong> <strong>+</strong> <strong>δ</strong><strong>l</strong><strong>o</strong><strong>g</strong><strong>P</strong> <strong>+</strong> <strong>γ</strong><strong>X</strong> <strong>+</strong> <strong>u</strong></span>​, <span class="math inline"><strong>w</strong><strong>h</strong><strong>e</strong><strong>r</strong><strong>e</strong></span></p>
<p>examples</p>
<ul>
<li><p>income</p></li>
<li><p>prices of other goods</p></li>
</ul>
<p><span class="math display"><strong>Q</strong><strong>_</strong><strong>d</strong> <strong>=</strong> <strong>q</strong><strong>u</strong><strong>a</strong><strong>n</strong><strong>t</strong><strong>i</strong><strong>t</strong><strong>y</strong> <strong>d</strong><strong>e</strong><strong>m</strong><strong>a</strong><strong>n</strong><strong>d</strong><strong>e</strong><strong>d</strong></span></p>
<p><span class="math display"><strong>α</strong> <strong>=</strong> <strong>i</strong><strong>n</strong><strong>t</strong><strong>e</strong><strong>r</strong><strong>c</strong><strong>e</strong><strong>p</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>δ</strong> <strong>=</strong> <strong>d</strong><strong>e</strong><strong>m</strong><strong>a</strong><strong>n</strong><strong>d</strong> <strong>e</strong><strong>l</strong><strong>a</strong><strong>s</strong><strong>t</strong><strong>i</strong><strong>c</strong><strong>i</strong><strong>t</strong><strong>y</strong></span></p>
<p><span class="math display"><strong>P</strong> <strong>=</strong> <strong>p</strong><strong>r</strong><strong>i</strong><strong>c</strong><strong>e</strong></span></p>
<p><span class="math display"><strong>X</strong> <strong>=</strong> <strong>o</strong><strong>t</strong><strong>h</strong><strong>e</strong><strong>r</strong> <strong>d</strong><strong>e</strong><strong>m</strong><strong>a</strong><strong>n</strong><strong>d</strong> <strong>f</strong><strong>a</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong><strong>s</strong></span></p>
<p><span class="math display"><strong>γ</strong> <strong>=</strong> <strong>e</strong><strong>f</strong><strong>f</strong><strong>e</strong><strong>c</strong><strong>t</strong> <strong>o</strong><strong>f</strong> <strong>t</strong><strong>h</strong><strong>o</strong><strong>s</strong><strong>e</strong> <strong>o</strong><strong>t</strong><strong>h</strong><strong>e</strong><strong>r</strong> <strong>f</strong><strong>a</strong><strong>c</strong><strong>t</strong><strong>o</strong><strong>r</strong><strong>s</strong></span></p>
<p><span class="math display"><strong>u</strong> <strong>=</strong> <strong>e</strong><strong>r</strong><strong>r</strong><strong>o</strong><strong>r</strong> <strong>t</strong><strong>e</strong><strong>r</strong><strong>m</strong></span></p>
<p>this independence is called: exogeneity</p>
<ul>
<li><p>the goal is to estimate <span class="math inline"><strong>δ</strong></span></p>
<ul>
<li><p>to do that</p></li>
<li><p>price must vary independently of the error term u</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Key Takeaway</td>
<td><ul>
<li><p>to estimate price elasticity we need</p>
<ul>
<li><p>many observations of</p>
<ul>
<li><p>price</p></li>
</ul></li>
</ul></li>
</ul>
<p>must be independent of unobserved demand factors</p>
<ul>
<li><p>quantity</p></li>
</ul>
<ul>
<li><p>price variation</p></li>
</ul>
<p>this is the same general problem causal inference tries to solve</p>
<ul>
<li><p>we need either</p>
<ul>
<li><p>variation in treatment that is as good as random</p></li>
<li><p>research design that makes a credible causal comparison possible</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>
