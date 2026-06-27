> Markdown version for convenient browsing. Original files:
> - PDF: [DATA735_week04_notes.pdf](../DATA735_week04_notes.pdf)
> - DOCX: [DATA735_week04_notes.docx](DATA735_week04_notes.docx)

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
<th colspan="2">Causal Graphs</th>
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
<li><p>Draw directed acyclic graphs (DAGs) to represent causal relationships.</p></li>
<li><p>Identify important types of nodes in causal graphs, including confounders, mediators, and colliders.</p></li>
<li><p>Express common challenges in causal attribution using causal graphs.</p></li>
<li><p>Test for conditional independence using d-separation criteria.</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Readings</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><a href="https://mixtape.scunning.com/03-directed_acyclical_graphs">https://mixtape.scunning.com/03-directed_acyclical_graphs</a></td>
</tr>
<tr>
<td colspan="5">Understanding Directed Acyclic Graphs (DAGs)</td>
</tr>
<tr>
<td>Introduction to DAG Notation</td>
<td colspan="4"><ul>
<li><p>a DAG is a visual map showing how different variables interact and cause one another</p></li>
<li><p>nodes (letters)</p>
<ul>
<li><p>represent random variables (e.g., <span class="math inline"><em>D</em>, <em>Y</em>, <em>X</em></span>)</p></li>
</ul></li>
<li><p>directed arrows (<span class="math inline">→</span>)</p>
<ul>
<li><p>represent a causal relationship</p></li>
<li><p>the arrow always points forward in time from cause to effect</p></li>
</ul></li>
<li><p>acyclic</p>
<ul>
<li><p>causality flows in one direction only</p></li>
<li><p>you cannot have paths that loop back into themselves</p></li>
<li><p>e.g., <span class="math inline"><em>A</em> → <em>B</em> → <em>A</em></span> is impossible</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>How They Are Used</td>
<td colspan="4"><ul>
<li><p>to map theory</p>
<ul>
<li><p>they force researchers to explicitly state what they believe causes what</p></li>
</ul></li>
<li><p>to show what is not happening</p>
<ul>
<li><p>leaving out an arrow between two nodes means you assume there is absolutely no direct causal relationship between them</p></li>
</ul></li>
<li><p>to identify bias</p>
<ul>
<li><p>DAGs expose hidden pathways that can corrupt statistical data</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Paths and the Backdoor Criterion</td>
</tr>
<tr>
<td>The Direct Path (<span class="math inline"><strong>D</strong> <strong>→</strong> <strong>Y</strong></span>)</td>
<td colspan="4"><ul>
<li><p>the actual <strong>causal effect</strong> that you want to measure</p></li>
</ul></td>
</tr>
<tr>
<td>Backdoor Paths (Spurious Connections)</td>
<td colspan="4"><ul>
<li><p>a backdoor path is any non-causal path that connects <span class="math inline"><em>D</em> <em>t</em><em>o</em> <em>Y</em> </span>by starting with an arrow pointing <em>at</em> <span class="math inline"><em>D</em></span> (e.g<span class="math inline">., <em>D</em> ← <em>X</em> → <em>Y</em></span>)</p></li>
<li><p>these paths create <strong>spurious correlations</strong> (false associations)</p></li>
</ul></td>
</tr>
<tr>
<td>How to Achieve the Backdoor Criterion</td>
<td colspan="4"><ul>
<li><p>to find the true causal effect, you must <strong>close all open backdoor paths</strong></p></li>
<li><p>you close a backdoor path by <strong>conditioning on (controlling for)</strong> the non-collider variables along that path</p></li>
<li><p><strong>confounder</strong> <span class="math inline"><em>X</em></span></p>
<ul>
<li><p>a variable that jointly causes both the treatment (<em>D</em>) and the outcome (<em>Y</em>)</p></li>
<li><p>controlling for it blocks the bias</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>The Phenomenon of Colliding (Collider Bias)</td>
<td colspan="4"><ul>
<li><p>a <strong>Collider</strong> is a variable along a path where two arrows <strong>collide head-to-head</strong> into it</p></li>
<li><p><em>Example Path:</em> <span class="math inline"><em>D</em> → <em>X</em> ← <em>Y</em></span></p></li>
<li><p>here, <span class="math inline"><em>X</em></span> is the collider because both <span class="math inline"><em>D</em></span> and <span class="math inline"><em>Y</em></span> point directly at it</p></li>
</ul></td>
</tr>
<tr>
<td>The Golden Rule of Colliders</td>
<td colspan="4"><ul>
<li><p>an unconditioned collider <strong>naturally blocks</strong> a backdoor path</p>
<ul>
<li><p>it acts like a closed gate</p></li>
</ul></li>
<li><p>CRITICAL ERROR</p>
<ul>
<li><p>if you control for (condition on) a collider, you open the gate</p></li>
<li><p>this introduces a new type of bias called Collider Bias (or Endogenous Selection Bias)</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Real-World Examples of Collider Bias</td>
<td colspan="4"><p>the "Bad Control" in Salary Data<strong>:</strong></p>
<ul>
<li><p>if you look at gender discrimination (<span class="math inline"><em>D</em></span>) on earnings (<span class="math inline"><em>Y</em></span>), controlling for occupation (<span class="math inline"><em>X</em></span>) can introduce collider bias if discrimination affects what occupations women can enter (<span class="math inline"><em>D</em> → <em>X</em></span>) and talent affects occupation and earnings (<span class="math inline"><em>Y</em> ← <em>X</em></span>)</p></li>
</ul>
<p>Sample Selection Bias (Police Use of Force)</p>
<ul>
<li><p>if researchers only analyze data collected after a police stop occurs, they are conditioning on a collider (the stop)</p></li>
<li><p>if race affects the probability of being stopped, and civilian behavior also affects the stop, analyzing only the stopped individuals creates a false statistical correlation between race and police severity</p></li>
</ul></td>
</tr>
<tr>
<td>Summary Cheat Sheet for Research Design</td>
<td colspan="4"><ul>
<li><p>to fix Confounding Bias</p>
<ul>
<li><p>locate the variables causing both <span class="math inline"><em>D</em></span> and <span class="math inline"><em>Y</em></span>, and control for them to close the backdoor path</p></li>
</ul></li>
<li><p>to avoid Collider Bias</p>
<ul>
<li><p>locate variables where two causal paths collide, and leave them alone</p></li>
<li><p>do not control for them</p></li>
</ul></li>
<li><p>data alone is not enough</p>
<ul>
<li><p>you cannot fix these biases with "big data"</p></li>
<li><p>you must use a theoretical model (a DAG) to understand how the data was generated in the first place</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="4"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>
