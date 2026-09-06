> Markdown version for convenient browsing. Original files:
> - PDF: [DATA790_week02_notes.pdf](../DATA790_week02_notes.pdf)
> - DOCX: [DATA790_week02_notes.docx](DATA790_week02_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr>
<th colspan="4">Advanced Prompt Engineering Techniques</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Overview</td>
<td colspan="3" style="text-align: right;"><em>30 Aug 2026</em></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>design effective zero-shot and few-shot prompts for various tasks</p></li>
<li><p>implement chain-of-thought prompting for complex reasoning</p></li>
<li><p>apply structured prompting techniques for consistent outputs</p></li>
<li><p>identify basic prompt injection vulnerabilities</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Readings</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><p>Wei, J., et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models."</p>
<ul>
<li><p>the seminal CoT paper</p></li>
<li><p><a href="https://arxiv.org/pdf/2201.11903">https://arxiv.org/pdf/2201.11903</a></p></li>
</ul>
<p>Kojima, T., et al. (2022). "Large Language Models are Zero-Shot Reasoners."</p>
<ul>
<li><p>the magic of "Let's think step by step"</p></li>
<li><p><a href="https://arxiv.org/pdf/2205.11916">https://arxiv.org/pdf/2205.11916</a></p></li>
</ul>
<p>Zhou, D., et al. (2023). "Least-to-Most Prompting Enables Complex Reasoning."</p>
<ul>
<li><p>breaking down complex problems</p></li>
<li><p><a href="https://arxiv.org/pdf/2205.10625">https://arxiv.org/pdf/2205.10625</a></p></li>
</ul></td>
</tr>
<tr>
<td colspan="5"></td>
</tr>
<tr>
<td colspan="5">Chain-of-Thought Prompting Elicits Reasoning in Large Language Models</td>
</tr>
<tr>
<td>Core Idea</td>
<td colspan="4"><ul>
<li><p>large language models perform difficult reasoning tasks much better when they are prompted to produce intermediate reasoning steps before giving the final answer</p></li>
<li><p>called “<strong>Chain of Thought Prompting</strong>” (CoT)</p></li>
</ul></td>
</tr>
<tr>
<td>Key Insights</td>
<td colspan="4"><p><strong>Reasoning can be elicited through prompting.</strong></p>
<ul>
<li><p>a sufficiently large pretrained language model already appears to contain capabilities that ordinary prompting does not reveal</p></li>
<li><p>introducing the model to examples of step-by-step solutions can dramatically improve its performance</p></li>
<li><p>the authors therefore argue that standard prompting may substantially underestimate what a model can do</p></li>
</ul>
<p><strong>Breaking a problem into steps matters.</strong></p>
<ul>
<li><p>CoT lets the model decompose a difficult task into smaller intermediate problems</p></li>
<li><p>instead of trying to map a complicated question directly to an answer, it generates a sequence such as:</p>
<ul>
<li><p>understand → calculate → update → conclude</p></li>
</ul></li>
<li><p>this effectively gives difficult problems more intermediate computation</p></li>
</ul>
<p><strong>The effect appeared mainly in very large models.</strong></p>
<ul>
<li><p>in the models tested, smaller systems often produced reasoning that sounded fluent but was logically wrong</p></li>
<li><p>major benefits appeared only around the 100-billion-parameter scale and above</p></li>
<li><p>the authors describe CoT reasoning as an emergent ability of model scale</p></li>
</ul>
<p><strong>Hard problems benefit more than easy problems.</strong></p>
<ul>
<li><p>CoT provided little or sometimes negative improvement on simple one-step arithmetic</p></li>
<li><p>on difficult multi-step problems such as GSM8K, performance more than doubled for the largest GPT and PaLMs tested</p>
<ul>
<li><p>note: GSM8K (Grade School Math 8K) is a benchmark dataset of 8,500 high-quality, linguistically diverse grade-school math word problems created by OpenAI to evaluate multi-step mathematical reasoning in artificial intelligence</p>
<ul>
<li><p><a href="https://huggingface.co/datasets/openai/gsm8k">https://huggingface.co/datasets/openai/gsm8k</a></p></li>
</ul></li>
<li><p>note: PaLM (Pathways Language Model) is a family of large language models developed by Google AI designed for complex text, reasoning, and multimodal tasks</p>
<ul>
<li><p>original paper: <a href="https://arxiv.org/pdf/2204.02311">https://arxiv.org/pdf/2204.02311</a></p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>Natural-language reasoning is doing more than simply generating equations.</strong></p>
<ul>
<li><p>the authors tested whether the improvement came merely from asking the model to produce an equation before answering</p>
<ul>
<li><p>it did not</p></li>
</ul></li>
<li><p>on difficult GSM8K problems, equation-only prompting performed substantially worse than full natural-language reasoning</p></li>
</ul>
<p><strong>CoT works beyond mathematics.</strong></p>
<ul>
<li><p>improvements also appeared on commonsense reasoning, date reasoning, sports knowledge, robot-action planning, and symbolic tasks</p></li>
<li><p>for example, PaLM 540B with CoT reached 75.6% on StrategyQA, compared with the previous state of the art of 69.4%</p></li>
</ul>
<p><strong>CoT can improve generalization.</strong></p>
<ul>
<li><p>in symbolic experiments, models were shown short reasoning sequences and then tested on problems requiring more steps than appeared in the demonstrations</p></li>
<li><p>standard prompting largely failed, while sufficiently large models using CoT showed meaningful generalization to the longer sequences</p></li>
</ul>
<p><strong>The exact wording of the reasoning examples is not crucial.</strong></p>
<ul>
<li><p>different researchers wrote the demonstrations in different styles</p></li>
<li><p>different examples and example orders were also tested</p></li>
<li><p>performance varied, but CoT consistently beat ordinary prompting by a substantial margin</p></li>
<li><p>the effect therefore was not dependent on one specially engineered prompt</p></li>
</ul>
<p><strong>A reasoning-looking explanation is not necessarily genuine or correct reasoning.</strong></p>
<p>a model can produce a convincing sequence of steps that contains mistakes</p>
<p>the authors explicitly say that CoT does not prove that the neural network is "reasoning" in the human sense</p>
<p><strong>Correct-looking reasoning should not automatically be trusted.</strong></p>
<ul>
<li><p>in their error analysis, some incorrect answers came from nearly correct reasoning with small calculation or symbolic errors</p></li>
<li><p>others contained major failures of understanding or coherence</p></li>
<li><p>a generated explanation therefore gives useful diagnostic information, but it is not a guarantee of factual or logical correctness</p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Large Language Models are Zero-Shot Reasoners</td>
</tr>
<tr>
<td>Definitions</td>
<td colspan="4"><p><strong>Zero-Shot Prompting</strong></p>
<ul>
<li><p>give the AI a direct task or question with no examples</p></li>
<li><p>how it works:</p>
<ul>
<li><p>relies entirely on the AI's existing training and broad general knowledge</p></li>
</ul></li>
<li><p>best used for:</p>
<ul>
<li><p>simple and common tasks like translation, basic summarization, or simple sentiment analysis</p></li>
</ul></li>
<li><p>pros &amp; cons:</p>
<ul>
<li><p>fast and uses very few tokens (lower cost)</p></li>
<li><p>can lead to wrong or vague answers on complex tasks</p></li>
</ul></li>
</ul>
<p><strong>One-Shot Prompting</strong></p>
<ul>
<li><p>give the AI one example before your actual prompt or question</p></li>
<li><p>how it works:</p>
<ul>
<li><p>shows the model the exact style, tone, or format you want</p></li>
</ul></li>
<li><p>best used for:</p>
<ul>
<li><p>clarifying format ambiguities or matching a specific output style</p></li>
</ul></li>
<li><p>pros &amp; cons:</p>
<ul>
<li><p>more precise and consistent than zero-shot</p></li>
<li><p>takes a little more prep time and uses more tokens</p></li>
</ul></li>
</ul>
<p><strong>Few-Shot Prompting</strong></p>
<ul>
<li><p>give the AI a small handful of examples (usually two to ten) before your main request</p></li>
<li><p>how it works:</p>
<ul>
<li><p>creates a mini-dataset that helps the model spot patterns and rules quickly</p></li>
</ul></li>
<li><p>best used for:</p>
<ul>
<li><p>complex tasks, strict formatting rules, or tricky edge cases</p></li>
</ul></li>
<li><p>pros &amp; cons:</p>
<ul>
<li><p>yields the highest accuracy and reliability</p></li>
<li><p>uses the most tokens and costs slightly more per request.</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Core Idea</td>
<td colspan="4"><ul>
<li><p>takes the chain-of-thought result from the previous paper one step further</p></li>
</ul></td>
</tr>
<tr>
<td>Key Insights</td>
<td colspan="4"><p><strong>Chain-of-thought does not necessarily require examples.</strong></p>
<ul>
<li><p>the original CoT method used few-shot prompting:</p>
<ul>
<li><p>example problem</p>
<ul>
<li><p>→ example reasoning</p></li>
<li><p>→ example answer</p></li>
</ul></li>
<li><p>then the model received a new problem</p></li>
</ul></li>
<li><p>this paper introduces Zero-shot-CoT:</p>
<ul>
<li><p>new problem</p>
<ul>
<li><p>→ “Let’s think step by step.”</p></li>
<li><p>→ reasoning</p></li>
<li><p>→ answer</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>A tiny change to the prompt can produce a huge change in performance.</strong></p>
<ul>
<li><p>the most dramatic results came from multi-step arithmetic</p></li>
</ul>
<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 40%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Task</strong></th>
<th style="text-align: right;"><strong>Normal zero-shot</strong></th>
<th style="text-align: right;"><strong>Zero-shot-CoT</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>MultiArith</td>
<td style="text-align: right;">17.7%</td>
<td style="text-align: right;">78.7%</td>
</tr>
<tr>
<td>GSM8K</td>
<td style="text-align: right;">10.4%</td>
<td style="text-align: right;">40.7%</td>
</tr>
<tr>
<td>AQUA-RAT</td>
<td style="text-align: right;">22.4%</td>
<td style="text-align: right;">33.5%</td>
</tr>
<tr>
<td>SVAMP</td>
<td style="text-align: right;">58.8%</td>
<td style="text-align: right;">62.1%</td>
</tr>
</tbody>
</table>
<ul>
<li><p>the model itself did not change</p></li>
<li><p>only the prompting strategy changed</p></li>
</ul>
<p><strong>The improvement comes from encouraging intermediate reasoning.</strong></p>
<ul>
<li><p>ordinary zero-shot prompting effectively asks:</p>
<ul>
<li><p>Problem → Answer</p></li>
</ul></li>
<li><p>zero-shot-CoT encourages:</p></li>
</ul>
<p><span class="math display"><em>P</em><em>r</em><em>o</em><em>b</em><em>l</em><em>e</em><em>m</em></span></p>
<p><span class="math display">↓</span></p>
<p><span class="math display"><em>B</em><em>r</em><em>e</em><em>a</em><em>k</em> <em>p</em><em>r</em><em>o</em><em>b</em><em>l</em><em>e</em><em>m</em> <em>i</em><em>n</em><em>t</em><em>o</em> <em>s</em><em>t</em><em>e</em><em>p</em><em>s</em></span></p>
<p><span class="math display">↓</span></p>
<p><span class="math display"><em>R</em><em>e</em><em>a</em><em>s</em><em>o</em><em>n</em> <em>t</em><em>h</em><em>r</em><em>o</em><em>u</em><em>g</em><em>h</em> <em>s</em><em>t</em><em>e</em><em>p</em><em>s</em></span></p>
<p><span class="math display">↓</span></p>
<p><span class="math display"><em>A</em><em>n</em><em>s</em><em>w</em><em>e</em><em>r</em></span></p>
<ul>
<li><p>this matters most when the task genuinely requires multiple dependent operations</p></li>
</ul>
<p><strong>Easy problems do not benefit nearly as much.</strong></p>
<ul>
<li><p>zero-shot-CoT produced little improvement on simpler arithmetic problems such as SingleEq and AddSub</p>
<ul>
<li><p>if a problem can be solved in one obvious step, forcing the model to construct a long reasoning chain provides little benefit</p></li>
</ul></li>
<li><p>the technique is most useful when the problem requires:</p></li>
</ul>
<p><span class="math display"><em>A</em> → <em>B</em> → <em>C</em> → <em>D</em> → <em>a</em><em>n</em><em>s</em><em>w</em><em>e</em><em>r</em></span></p>
<p><strong>The effect is strongly dependent on model scale.</strong></p>
<ul>
<li><p>for smaller language models:</p>
<ul>
<li><p>CoT prompting → little or no improvement</p></li>
</ul></li>
<li><p>as models became larger:</p>
<ul>
<li><p>CoT prompting → rapidly increasing reasoning performance</p></li>
<li><p>without CoT:</p>
<ul>
<li><p>performance on some reasoning problems remained relatively flat even as model size increased</p></li>
</ul></li>
<li><p>with CoT:</p>
<ul>
<li><p>the scaling curve became much steeper</p></li>
</ul></li>
<li><p>conceptually:</p>
<ul>
<li><p>scaling alone did not reliably reveal reasoning ability</p></li>
</ul></li>
</ul></li>
<li><p>instead:</p>
<ul>
<li><p>large model + reasoning-oriented prompt was much more powerful than large model + ordinary prompt</p></li>
</ul></li>
</ul>
<p><strong>The capability appears to already exist inside the model.</strong></p>
<ul>
<li><p>zero-shot-CoT does not:</p>
<ul>
<li><p>retrain the model</p></li>
<li><p>fine-tune the model</p></li>
<li><p>provide examples</p></li>
<li><p>teach it a new algorithm</p></li>
</ul></li>
<li><p>it simply changes the instruction</p></li>
<li><p>the authors therefore argue</p>
<ul>
<li><p>large models may contain latent reasoning capabilities that ordinary prompting fails to elicit</p></li>
</ul></li>
<li><p>In simplified terms:</p>
<ul>
<li><p>the model may already possess a capability that its normal behavior does not reveal</p></li>
<li><p>prompting can act as a mechanism for eliciting that capability</p></li>
</ul></li>
</ul>
<p><strong>The prompt is surprisingly general.</strong></p>
<ul>
<li><p>the same basic instruction worked across several different categories</p></li>
<li><p>arithmetic</p>
<ul>
<li><p>MultiArith</p></li>
<li><p>GSM8K</p></li>
<li><p>AQUA-RAT</p></li>
<li><p>SVAMP</p></li>
</ul></li>
<li><p>symbolic reasoning</p>
<ul>
<li><p>Last Letter</p></li>
<li><p>Coin Flip</p></li>
</ul></li>
<li><p>logical reasoning</p>
<ul>
<li><p>Date Understanding</p></li>
<li><p>Tracking Shuffled Objects</p></li>
</ul></li>
<li><p>this is important because</p>
<ul>
<li><p>most prompt engineering before this work was relatively task-specific</p></li>
</ul></li>
</ul>
<p><strong>Symbolic reasoning improved dramatically.</strong></p>
<ul>
<li><p>the effect was not limited to mathematics</p></li>
<li><p>for example:</p></li>
</ul>
<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 22%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Task</strong></th>
<th style="text-align: right;"><strong>Zero-shot</strong></th>
<th style="text-align: right;"><strong>Zero-shot-CoT</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Last Letter</td>
<td style="text-align: center;">0.2%</td>
<td style="text-align: center;">57.6%</td>
</tr>
<tr>
<td>Coin Flip</td>
<td style="text-align: center;">12.8%</td>
<td style="text-align: center;">91.4%</td>
</tr>
<tr>
<td>Date Understanding</td>
<td style="text-align: center;">49.3%</td>
<td style="text-align: center;">67.5%</td>
</tr>
<tr>
<td>Shuffled Objects</td>
<td style="text-align: center;">31.3%</td>
<td style="text-align: center;">52.4%</td>
</tr>
</tbody>
</table>
<ul>
<li><p>this supports the idea that the prompt is activating something broader than a memorized mathematical procedure</p></li>
</ul>
<p><strong>It does not improve every kind of reasoning.</strong></p>
<ul>
<li><p>the results for commonsense reasoning were much weaker</p>
<ul>
<li><p>for CommonsenseQA, performance actually fell:</p>
<ul>
<li><p>68.8% → 64.6%</p></li>
</ul></li>
</ul></li>
<li><p>the authors found that models sometimes generated plausible reasoning but still selected the wrong answer</p>
<ul>
<li><p>more reasoning ≠ automatically more accuracy</p></li>
</ul></li>
</ul>
<p><strong>Models can reason themselves into a wrong answer.</strong></p>
<ul>
<li><p>the authors' error analysis found several failure modes</p>
<ul>
<li><p>a model might:</p>
<ul>
<li><p>begin with correct reasoning</p></li>
<li><p>add unnecessary steps</p></li>
<li><p>introduce an error later</p></li>
<li><p>change a previously correct conclusion</p></li>
</ul></li>
<li><p>sometimes the model simply restated the question instead of actually reasoning</p></li>
</ul></li>
<li><p>this highlights an important limitation:</p>
<ul>
<li><p>longer reasoning is not necessarily better reasoning</p></li>
</ul></li>
</ul>
<p><strong>The wording of the prompt matters.</strong></p>
<ul>
<li><p>the authors tested many different trigger phrases</p>
<ul>
<li><p>good prompts included:</p>
<ul>
<li><p>“Let’s think step by step.”</p></li>
<li><p>“First,”</p></li>
<li><p>“Let’s think about this logically.”</p></li>
<li><p>“Let’s solve this problem by splitting it into steps.”</p></li>
</ul></li>
<li><p>MultiArith: “Let’s think step by step.” → 78.7%</p></li>
<li><p>ordinary zero-shot → 17.7%</p></li>
</ul></li>
<li><p>irrelevant or misleading prompts produced little improvement</p></li>
<li><p>the result is not simply caused by adding extra words</p></li>
<li><p>the instruction needs to encourage the model to adopt a reasoning process</p></li>
</ul>
<p><strong>Few-shot CoT is still generally stronger.</strong></p>
<ul>
<li><p>zero-shot-CoT does not make carefully designed examples obsolete</p>
<ul>
<li><p>MultiArith:</p>
<ul>
<li><p>zero-shot: 17.7%</p></li>
<li><p>zero-shot-CoT: 78.7%</p></li>
<li><p>8-shot CoT: 93.0%</p></li>
</ul></li>
<li><p>GSM8K:</p>
<ul>
<li><p>Zero-shot: 10.4%</p></li>
<li><p>Zero-shot-CoT: 40.7%</p></li>
<li><p>8-shot CoT: 48.7%</p></li>
</ul></li>
</ul></li>
<li><p>the advantage of Zero-shot-CoT is therefore not necessarily maximum accuracy</p></li>
<li><p>Its advantage is:</p>
<ul>
<li><p>very little prompt engineering</p></li>
<li><p>broad applicability</p></li>
<li><p>large performance improvement</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Main Conceptual Takeaways</td>
<td colspan="4"><ul>
<li><p>large models may already contain useful multi-step reasoning capabilities, and a remarkably simple prompt can sometimes cause those capabilities to emerge without examples or additional training.</p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Least-to-Most Prompting Enables Complex Reasoning in Large Language Models</td>
</tr>
<tr>
<td>Core Idea</td>
<td colspan="4"><ul>
<li><p>this paper addresses a weakness of ordinary chain-of-thought (CoT) prompting:</p>
<ul>
<li><p>models often struggle when the new problem is harder than the examples shown in the prompt</p></li>
</ul></li>
<li><p>the authors introduce least-to-most prompting</p>
<ul>
<li><p>instead of asking the model to solve a difficult problem directly, the model first:</p></li>
</ul></li>
</ul>
<blockquote>
<p>1. Breaks the problem into easier subproblems</p>
<p>then:</p>
<p>2. Solves those subproblems in order</p>
</blockquote>
<ul>
<li><p>each solved subproblem becomes useful context for the next one</p></li>
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
<th>Basic Structure</th>
<th><p>Chain-of-thought.</p>
<ul>
<li><p>a typical CoT prompt encourages:</p></li>
</ul>
<p><span class="math display"><strong>P</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>l</strong><strong>e</strong><strong>m</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>r</strong><strong>e</strong><strong>a</strong><strong>s</strong><strong>o</strong><strong>n</strong> <strong>t</strong><strong>h</strong><strong>r</strong><strong>o</strong><strong>u</strong><strong>g</strong><strong>h</strong> <strong>t</strong><strong>h</strong><strong>e</strong> <strong>w</strong><strong>h</strong><strong>o</strong><strong>l</strong><strong>e</strong> <strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>l</strong><strong>e</strong><strong>m</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>A</strong><strong>n</strong><strong>s</strong><strong>w</strong><strong>e</strong><strong>r</strong></span></p>
<ul>
<li><p>this works well when the new problem resembles the examples</p></li>
<li><p>but performance often degrades when the test problem requires more reasoning steps than the demonstrations</p></li>
</ul>
<p>Least-to-most prompting.</p>
<ul>
<li><p>least-to-most prompting separates reasoning into two stages:</p>
<ul>
<li><p>Stage 1 — Decompose</p>
<ul>
<li><p>turn complex problem into:</p></li>
</ul></li>
</ul></li>
</ul>
<p><span class="math display"><strong>S</strong><strong>u</strong><strong>b</strong><strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>l</strong><strong>e</strong><strong>m</strong> <strong>1</strong></span></p>
<p><span class="math display"><strong>S</strong><strong>u</strong><strong>b</strong><strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>l</strong><strong>e</strong><strong>m</strong> <strong>2</strong></span></p>
<p><span class="math display"><strong>S</strong><strong>u</strong><strong>b</strong><strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>l</strong><strong>e</strong><strong>m</strong> <strong>3</strong></span></p>
<ul>
<li><p>Stage 2 — Solve sequentially</p>
<ul>
<li><p>then solve:</p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>S</strong><strong>u</strong><strong>b</strong><strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>l</strong><strong>e</strong><strong>m</strong> <strong>1</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>u</strong><strong>s</strong><strong>e</strong> <strong>i</strong><strong>t</strong><strong>s</strong> <strong>a</strong><strong>n</strong><strong>s</strong><strong>w</strong><strong>e</strong><strong>r</strong> <strong>t</strong><strong>o</strong> <strong>s</strong><strong>o</strong><strong>l</strong><strong>v</strong><strong>e</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>S</strong><strong>u</strong><strong>b</strong><strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>l</strong><strong>e</strong><strong>m</strong> <strong>2</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>u</strong><strong>s</strong><strong>e</strong> <strong>p</strong><strong>r</strong><strong>e</strong><strong>v</strong><strong>i</strong><strong>o</strong><strong>u</strong><strong>s</strong> <strong>r</strong><strong>e</strong><strong>s</strong><strong>u</strong><strong>l</strong><strong>t</strong><strong>s</strong> <strong>t</strong><strong>o</strong> <strong>s</strong><strong>o</strong><strong>l</strong><strong>v</strong><strong>e</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>S</strong><strong>u</strong><strong>b</strong><strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>l</strong><strong>e</strong><strong>m</strong> <strong>3</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>F</strong><strong>i</strong><strong>n</strong><strong>a</strong><strong>l</strong> <strong>a</strong><strong>n</strong><strong>s</strong><strong>w</strong><strong>e</strong><strong>r</strong></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Async</td>
</tr>
<tr>
<td colspan="2">Zero-Shot, Few-Shot, and Chain-of-Thought</td>
</tr>
<tr>
<td>Zero-Shot Prompting</td>
<td><ul>
<li><p>asks the model to perform a task without giving it any examples</p></li>
<li><p>example:</p>
<ul>
<li><p>classify this movie review as positive or negative</p></li>
</ul></li>
<li><p>the model must rely entirely on:</p>
<ul>
<li><p>its pretrained knowledge</p></li>
<li><p>its understanding of the instruction</p></li>
<li><p>its ability to generalize</p></li>
</ul></li>
<li><p>useful for testing the model's <strong>baseline capability</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Few-Shot Prompting</td>
<td><ul>
<li><p>gives the model a small number of examples before asking it to perform the new task</p></li>
<li><p>a typical prompt might contain:</p></li>
</ul>
<p><span class="math display"><strong>E</strong><strong>x</strong><strong>a</strong><strong>m</strong><strong>p</strong><strong>l</strong><strong>e</strong> <strong>1</strong> → <em>p</em><em>o</em><em>s</em><em>i</em><em>t</em><em>i</em><em>v</em><em>e</em></span></p>
<p><span class="math display"><strong>E</strong><strong>x</strong><strong>a</strong><strong>m</strong><strong>p</strong><strong>l</strong><strong>e</strong> <strong>2</strong> → <em>n</em><em>e</em><em>g</em><em>a</em><em>t</em><em>i</em><em>v</em><em>e</em></span></p>
<p><span class="math display"><strong>E</strong><strong>x</strong><strong>a</strong><strong>m</strong><strong>p</strong><strong>l</strong><strong>e</strong> <strong>3</strong> → <em>p</em><em>o</em><em>s</em><em>i</em><em>t</em><em>i</em><em>v</em><em>e</em></span></p>
<ul>
<li><p>then:</p></li>
</ul>
<p><span class="math display"><strong>N</strong><strong>e</strong><strong>w</strong> <strong>e</strong><strong>x</strong><strong>a</strong><strong>m</strong><strong>p</strong><strong>l</strong><strong>e</strong> <strong>→</strong> <strong>?</strong></span></p></td>
</tr>
<tr>
<td>Chain-of-Thought Prompting</td>
<td><ul>
<li><p>encourages the model to produce intermediate reasoning steps before reaching an answer</p></li>
<li><p>instead of:</p></li>
</ul>
<p><span class="math display"><strong>P</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>l</strong><strong>e</strong><strong>m</strong> <strong>→</strong> <strong>A</strong><strong>n</strong><strong>s</strong><strong>w</strong><strong>e</strong><strong>r</strong></span></p>
<p>the model follows:</p>
<p><span class="math display"><strong>P</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>l</strong><strong>e</strong><strong>m</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>I</strong><strong>n</strong><strong>t</strong><strong>e</strong><strong>r</strong><strong>m</strong><strong>e</strong><strong>d</strong><strong>i</strong><strong>a</strong><strong>t</strong><strong>e</strong> <strong>r</strong><strong>e</strong><strong>a</strong><strong>s</strong><strong>o</strong><strong>n</strong><strong>i</strong><strong>n</strong><strong>g</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>M</strong><strong>o</strong><strong>r</strong><strong>e</strong> <strong>r</strong><strong>e</strong><strong>a</strong><strong>s</strong><strong>o</strong><strong>n</strong><strong>i</strong><strong>n</strong><strong>g</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>F</strong><strong>i</strong><strong>n</strong><strong>a</strong><strong>l</strong> <strong>a</strong><strong>n</strong><strong>s</strong><strong>w</strong><strong>e</strong><strong>r</strong></span></p></td>
</tr>
<tr>
<td>Choosing a Prompting Strategy</td>
<td><p><strong>Use zero-shot when:</strong></p>
<ul>
<li><p>testing a new model</p></li>
<li><p>evaluating baseline capability</p></li>
<li><p>the task is simple</p></li>
<li><p>the instruction is already clear</p></li>
</ul>
<p><strong>Use few-shot when:</strong></p>
<ul>
<li><p>output formatting matters</p></li>
<li><p>classifications need consistency</p></li>
<li><p>the model needs examples of the desired behavior</p></li>
<li><p>the task follows a stable pattern</p></li>
</ul>
<p><strong>Use chain-of-thought when:</strong></p>
<ul>
<li><p>the task requires multiple reasoning steps</p></li>
<li><p>logic or mathematics is involved</p></li>
<li><p>several perspectives must be considered</p></li>
<li><p>the model needs to organize a complex problem</p></li>
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
<th>Main Takeaway</th>
<th><ul>
<li><p>prompting is a way of controlling how much structure and guidance a language model receives</p></li>
<li><p>the three techniques form a useful progression:</p>
<ul>
<li><p>zero-shot → test what the model already knows</p></li>
<li><p>few-shot → demonstrate the desired behavior</p></li>
<li><p>chain-of-thought → structure complex reasoning</p></li>
</ul></li>
<li><p>the more complex or specialized the task becomes, the more useful carefully designed prompt structure becomes</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Emotion Prompts and Structured Prompting</td>
</tr>
<tr>
<td>Emotional Priming</td>
<td><ul>
<li><p>adds emotional or psychological language to a prompt in order to influence how the model responds</p></li>
<li><p>examples:</p>
<ul>
<li><p>“Please help. This is very important for my presentation.”</p></li>
<li><p>“This is an urgent request.”</p></li>
</ul></li>
<li><p>the goal may be to encourage:</p>
<ul>
<li><p>greater thoroughness</p></li>
<li><p>urgency</p></li>
<li><p>attention to detail</p></li>
<li><p>a particular emotional tone</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Why Emotional Language Can Affect an LLM</td>
<td><ul>
<li><p>the model itself does not need to experience emotion for emotional language to affect its output</p></li>
<li><p>LLMs are trained on large amounts of human-written text containing:</p>
<ul>
<li><p>urgency</p></li>
<li><p>concern</p></li>
<li><p>excitement</p></li>
<li><p>importance</p></li>
<li><p>persuasion</p></li>
<li><p>emotional language</p></li>
</ul></li>
<li><p>as a result</p>
<ul>
<li><p>words associated with these contexts can influence the probability of what the model generates next</p></li>
</ul></li>
<li><p>conceptually:</p></li>
</ul>
<p><span class="math display"><strong>e</strong><strong>m</strong><strong>o</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong><strong>a</strong><strong>l</strong> <strong>w</strong><strong>o</strong><strong>r</strong><strong>d</strong><strong>i</strong><strong>n</strong><strong>g</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>d</strong><strong>i</strong><strong>f</strong><strong>f</strong><strong>e</strong><strong>r</strong><strong>e</strong><strong>n</strong><strong>t</strong> <strong>c</strong><strong>o</strong><strong>n</strong><strong>t</strong><strong>e</strong><strong>x</strong><strong>t</strong><strong>u</strong><strong>a</strong><strong>l</strong> <strong>s</strong><strong>i</strong><strong>g</strong><strong>n</strong><strong>a</strong><strong>l</strong><strong>s</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>d</strong><strong>i</strong><strong>f</strong><strong>f</strong><strong>e</strong><strong>r</strong><strong>e</strong><strong>n</strong><strong>t</strong> <strong>t</strong><strong>o</strong><strong>k</strong><strong>e</strong><strong>n</strong> <strong>p</strong><strong>r</strong><strong>o</strong><strong>b</strong><strong>a</strong><strong>b</strong><strong>i</strong><strong>l</strong><strong>i</strong><strong>t</strong><strong>i</strong><strong>e</strong><strong>s</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>d</strong><strong>i</strong><strong>f</strong><strong>f</strong><strong>e</strong><strong>r</strong><strong>e</strong><strong>n</strong><strong>t</strong> <strong>r</strong><strong>e</strong><strong>s</strong><strong>p</strong><strong>o</strong><strong>n</strong><strong>s</strong><strong>e</strong> <strong>b</strong><strong>e</strong><strong>h</strong><strong>a</strong><strong>v</strong><strong>i</strong><strong>o</strong><strong>r</strong></span></p></td>
</tr>
<tr>
<td>Emotional Priming can Signal Task Importance</td>
<td><ul>
<li><p>compare:</p>
<ul>
<li><p>“Create a presentation.”</p></li>
</ul></li>
<li><p>with:</p>
<ul>
<li><p>“Please help. This presentation is extremely important, and I need a complete result.”</p></li>
</ul></li>
<li><p>the second prompt provides additional contextual signals suggesting that:</p>
<ul>
<li><p>completeness matters</p></li>
<li><p>quality matters</p></li>
<li><p>the task should receive substantial attention</p></li>
</ul></li>
<li><p>the broader idea is that prompt wording changes the context from which the model predicts its response</p></li>
</ul></td>
</tr>
<tr>
<td>Structured Output Prompting</td>
<td><ul>
<li><p>tells the model exactly how its response should be organized</p></li>
<li><p>possible formats include:</p>
<ul>
<li><p>markdown</p></li>
<li><p>tables</p></li>
<li><p>lists</p></li>
<li><p>JSON</p></li>
<li><p>predefined schemas</p></li>
<li><p>combinations of structured formats</p></li>
</ul></li>
<li><p>this is particularly important when model output will be consumed by software rather than directly by a human</p></li>
</ul></td>
</tr>
<tr>
<td>JSON Mode</td>
<td><ul>
<li><p>a particularly useful structured-output technique is requiring the model to return <strong>valid JSON</strong></p></li>
</ul>
<p><img src="generated_media\DATA790_week02_notes\media\image1.png" style="width:2.26073in;height:1.31268in" /></p>
<ul>
<li><p>JSON is especially useful because software can easily parse it</p>
<ul>
<li><p>APIs</p></li>
<li><p>web applications</p></li>
<li><p>databases</p></li>
<li><p>automated workflows</p></li>
<li><p>front-end interfaces</p></li>
<li><p>back-end services</p></li>
</ul></li>
<li><p>instead of extracting information from prose, the application can directly access defined fields</p></li>
<li><p>structured outputs help manage nondeterminism</p>
<ul>
<li><p>LLMs are non-deterministic systems</p></li>
<li><p>the same prompt can produce somewhat different outputs across runs</p></li>
<li><p>this becomes a problem when downstream software requires a predictable format</p></li>
<li><p>a schema creates constraints such as:</p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>t</strong><strong>h</strong><strong>e</strong><strong>s</strong><strong>e</strong> <strong>f</strong><strong>i</strong><strong>e</strong><strong>l</strong><strong>d</strong><strong>s</strong> <strong>m</strong><strong>u</strong><strong>s</strong><strong>t</strong> <strong>e</strong><strong>x</strong><strong>i</strong><strong>s</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>t</strong><strong>h</strong><strong>e</strong><strong>s</strong><strong>e</strong> <strong>f</strong><strong>i</strong><strong>e</strong><strong>l</strong><strong>d</strong><strong>s</strong> <strong>m</strong><strong>u</strong><strong>s</strong><strong>t</strong> <strong>c</strong><strong>o</strong><strong>n</strong><strong>t</strong><strong>a</strong><strong>i</strong><strong>n</strong> <strong>p</strong><strong>a</strong><strong>r</strong><strong>t</strong><strong>i</strong><strong>c</strong><strong>u</strong><strong>l</strong><strong>a</strong><strong>r</strong> <strong>t</strong><strong>y</strong><strong>p</strong><strong>e</strong><strong>s</strong> <strong>o</strong><strong>f</strong> <strong>d</strong><strong>a</strong><strong>t</strong><strong>a</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>i</strong><strong>n</strong><strong>v</strong><strong>a</strong><strong>l</strong><strong>i</strong><strong>d</strong> <strong>r</strong><strong>e</strong><strong>s</strong><strong>p</strong><strong>o</strong><strong>n</strong><strong>s</strong><strong>e</strong><strong>s</strong> <strong>c</strong><strong>a</strong><strong>n</strong> <strong>b</strong><strong>e</strong> <strong>d</strong><strong>e</strong><strong>t</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>e</strong><strong>d</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>t</strong><strong>h</strong><strong>e</strong> <strong>r</strong><strong>e</strong><strong>q</strong><strong>u</strong><strong>e</strong><strong>s</strong><strong>t</strong> <strong>c</strong><strong>a</strong><strong>n</strong> <strong>b</strong><strong>e</strong> <strong>r</strong><strong>e</strong><strong>t</strong><strong>r</strong><strong>i</strong><strong>e</strong><strong>d</strong> <strong>o</strong><strong>r</strong> <strong>c</strong><strong>o</strong><strong>r</strong><strong>r</strong><strong>e</strong><strong>c</strong><strong>t</strong><strong>e</strong><strong>d</strong></span></p>
<ul>
<li><p>so structured output does not eliminate nondeterminism, but it makes it easier to control and validate</p></li>
</ul></td>
</tr>
<tr>
<td>Role-Based Prompting</td>
<td><ul>
<li><p>assigns the model a particular persona, profession, or perspective</p>
<ul>
<li><p>examples:</p>
<ul>
<li><p>“Act as a senior data scientist.”</p></li>
<li><p>“You are a travel agent.”</p></li>
<li><p>“Explain this as a kindergarten teacher.”</p></li>
</ul></li>
</ul></li>
<li><p>the assigned role provides context for how the model should answer</p>
<ul>
<li><p>roles influence several parts of the response</p>
<ul>
<li><p>a role can affect</p></li>
<li><p>vocabulary</p></li>
<li><p>technical depth</p></li>
<li><p>tone</p></li>
<li><p>assumptions</p></li>
<li><p>examples</p></li>
<li><p>priorities</p></li>
<li><p>style of explanation</p></li>
</ul></li>
<li><p>for example:</p>
<ul>
<li><p>senior data scientist</p>
<ul>
<li><p>likely response characteristics:</p>
<ul>
<li><p>technical terminology</p></li>
<li><p>statistical reasoning</p></li>
<li><p>methodological detail</p></li>
<li><p>more advanced explanations</p></li>
</ul></li>
</ul></li>
<li><p>kindergarten teacher</p>
<ul>
<li><p>likely response characteristics:</p>
<ul>
<li><p>simple vocabulary</p></li>
<li><p>short explanations</p></li>
<li><p>concrete examples</p></li>
<li><p>minimal jargon</p></li>
</ul></li>
</ul></li>
</ul></li>
</ul></li>
<li><p>role prompting works because the training data contains many examples of different professional and social forms of communication</p></li>
</ul></td>
</tr>
<tr>
<td>Comparing the Three Techniques</td>
<td><table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Technique</strong></th>
<th style="text-align: center;"><strong>Primarily controls</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Emotional priming</strong></td>
<td>Urgency, emphasis, tone</td>
</tr>
<tr>
<td><strong>Structured prompting</strong></td>
<td>Output format and consistency</td>
</tr>
<tr>
<td><strong>Role-based prompting</strong></td>
<td>Perspective, expertise, language</td>
</tr>
</tbody>
</table></td>
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
<th>Main Takeaway</th>
<th><ul>
<li><p>advanced prompting is not only about telling an LLM what task to perform</p></li>
<li><p>it can also shape the context, perspective, and format in which the model performs that task</p></li>
<li><p>the three techniques can be summarized as:</p>
<ul>
<li><p>emotional priming →</p></li>
</ul></li>
</ul>
<blockquote>
<p>influence response behavior</p>
</blockquote>
<ul>
<li><p>structured prompting →</p></li>
</ul>
<blockquote>
<p>control response format</p>
</blockquote>
<ul>
<li><p>role-based prompting →</p></li>
</ul>
<blockquote>
<p>control perspective and level of expertise</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Introduction to Prompt Injection Risks</td>
</tr>
<tr>
<td>Prompt Injection</td>
<td><ul>
<li><p>attempts to manipulate an LLM into ignoring its intended instructions</p></li>
<li><p>the attacker tries to make the model:</p>
<ul>
<li><p>reveal restricted information</p></li>
<li><p>ignore rules</p></li>
<li><p>perform unintended actions</p></li>
<li><p>generate prohibited output</p></li>
<li><p>follow malicious instructions</p></li>
</ul></li>
</ul>
<p><strong>Direct prompt injection.</strong></p>
<ul>
<li><p>common direct-injection patterns</p>
<ul>
<li><p>“Ignore previous instructions.”</p></li>
<li><p>“Forget your rules.”</p></li>
<li><p>“Do this instead.”</p></li>
<li><p>“Reveal your system prompt.”</p></li>
</ul></li>
<li><p>recognizing these patterns can help identify suspicious input</p></li>
<li><p>simple phrase blocking alone is not sufficient</p></li>
</ul>
<p><strong>Indirect prompt injection.</strong></p>
<ul>
<li><p>occurs when malicious instructions are hidden inside an external data source that the LLM processes</p>
<ul>
<li><p>possible sources include:</p>
<ul>
<li><p>webpages</p></li>
<li><p>PDFs</p></li>
<li><p>spreadsheets</p></li>
<li><p>documents</p></li>
<li><p>emails</p></li>
<li><p>retrieved database content</p></li>
<li><p>RAG knowledge sources</p></li>
</ul></li>
</ul></li>
<li><p>the user may not even know that the malicious instruction exists</p></li>
</ul>
<p><strong>RAG systems Create Another Attack Surface.</strong></p>
<ul>
<li><p>indirect injection is especially relevant to:</p>
<ul>
<li><p>Retrieval-Augmented Generation (RAG)</p>
<ul>
<li><p>retrieves external material and adds it to the model's context</p></li>
</ul></li>
<li><p>conceptually:</p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>U</strong><strong>s</strong><strong>e</strong><strong>r</strong> <strong>q</strong><strong>u</strong><strong>e</strong><strong>s</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>r</strong><strong>e</strong><strong>t</strong><strong>r</strong><strong>i</strong><strong>e</strong><strong>v</strong><strong>e</strong> <strong>d</strong><strong>o</strong><strong>c</strong><strong>u</strong><strong>m</strong><strong>e</strong><strong>n</strong><strong>t</strong><strong>s</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>a</strong><strong>d</strong><strong>d</strong> <strong>d</strong><strong>o</strong><strong>c</strong><strong>u</strong><strong>m</strong><strong>e</strong><strong>n</strong><strong>t</strong><strong>s</strong> <strong>t</strong><strong>o</strong> <strong>p</strong><strong>r</strong><strong>o</strong><strong>m</strong><strong>p</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>L</strong><strong>L</strong><strong>M</strong> <strong>g</strong><strong>e</strong><strong>n</strong><strong>e</strong><strong>r</strong><strong>a</strong><strong>t</strong><strong>e</strong><strong>s</strong> <strong>a</strong><strong>n</strong><strong>s</strong><strong>w</strong><strong>e</strong><strong>r</strong></span></p>
<ul>
<li><p>if retrieved documents contain malicious instructions, those instructions can become part of the model's context</p></li>
<li><p>this means the retrieval system can accidentally deliver an attack directly to the LLM</p></li>
</ul>
<p><strong>Direct and indirect attacks can be combined.</strong></p>
<ul>
<li><p>an attacker does not need to use only one technique</p></li>
<li><p>for example:</p></li>
</ul>
<p><span class="math display"><strong>m</strong><strong>a</strong><strong>l</strong><strong>i</strong><strong>c</strong><strong>i</strong><strong>o</strong><strong>u</strong><strong>s</strong> <strong>u</strong><strong>s</strong><strong>e</strong><strong>r</strong> <strong>p</strong><strong>r</strong><strong>o</strong><strong>m</strong><strong>p</strong><strong>t</strong> <strong>•</strong> <strong>p</strong><strong>o</strong><strong>i</strong><strong>s</strong><strong>o</strong><strong>n</strong><strong>e</strong><strong>d</strong> <strong>d</strong><strong>o</strong><strong>c</strong><strong>u</strong><strong>m</strong><strong>e</strong><strong>n</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>c</strong><strong>o</strong><strong>m</strong><strong>b</strong><strong>i</strong><strong>n</strong><strong>e</strong><strong>d</strong> <strong>a</strong><strong>t</strong><strong>t</strong><strong>a</strong><strong>c</strong><strong>k</strong></span></p>
<ul>
<li><p>this can make attacks more difficult to detect because malicious instructions may be distributed across several sources</p></li>
</ul></td>
</tr>
<tr>
<td>Defense strategy: Input and Output Filtering</td>
<td><p><strong>Input filtering.</strong></p>
<ul>
<li><p>input filters can look for:</p>
<ul>
<li><p>known malicious patterns</p></li>
<li><p>prohibited content</p></li>
<li><p>suspicious instructions</p></li>
<li><p>attempts to override system rules</p></li>
</ul></li>
<li><p>for example:</p>
<ul>
<li><p>a system might flag requests containing phrases similar to:</p>
<ul>
<li><p>“Ignore all previous instructions.”</p></li>
</ul></li>
<li><p>the request can then be:</p>
<ul>
<li><p>blocked</p></li>
<li><p>modified</p></li>
<li><p>sent for additional inspection</p></li>
</ul></li>
</ul></li>
</ul>
<blockquote>
<p>before reaching the model</p>
</blockquote>
<p><strong>Output filtering.</strong></p>
<ul>
<li><p>the model's response should also be checked</p>
<ul>
<li><p>this helps prevent:</p>
<ul>
<li><p>harmful content</p></li>
<li><p>restricted information</p></li>
<li><p>inappropriate language</p></li>
<li><p>sensitive data leakage</p></li>
<li><p>unexpected model behavior</p></li>
</ul></li>
</ul></li>
<li><p>the security pipeline therefore becomes:</p></li>
</ul>
<p><span class="math display"><strong>U</strong><strong>s</strong><strong>e</strong><strong>r</strong> <strong>i</strong><strong>n</strong><strong>p</strong><strong>u</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>I</strong><strong>n</strong><strong>p</strong><strong>u</strong><strong>t</strong> <strong>g</strong><strong>u</strong><strong>a</strong><strong>r</strong><strong>d</strong><strong>r</strong><strong>a</strong><strong>i</strong><strong>l</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>L</strong><strong>L</strong><strong>M</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>O</strong><strong>u</strong><strong>t</strong><strong>p</strong><strong>u</strong><strong>t</strong> <strong>g</strong><strong>u</strong><strong>a</strong><strong>r</strong><strong>d</strong><strong>r</strong><strong>a</strong><strong>i</strong><strong>l</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>U</strong><strong>s</strong><strong>e</strong><strong>r</strong></span></p></td>
</tr>
<tr>
<td>Defense Strategy: Structured Prompts</td>
<td><ul>
<li><p>clearly separate:</p>
<ul>
<li><p><strong>trusted instructions</strong> from <strong>untrusted data</strong></p></li>
</ul></li>
<li><p>this can be done using delimiters such as:</p>
<ul>
<li><p>XML tags</p></li>
<li><p>Markdown sections</p></li>
<li><p>quotation blocks</p></li>
<li><p>explicit separators</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr>
<th>Defense Strategy: Monitoring and Auditing</th>
<th><ul>
<li><p>LLM applications should also record and inspect interactions</p></li>
<li><p>monitoring can help detect:</p>
<ul>
<li><p>unusual prompts</p></li>
<li><p>repeated attack attempts</p></li>
<li><p>suspicious phrases</p></li>
<li><p>unexpected outputs</p></li>
<li><p>new attack patterns</p></li>
</ul></li>
<li><p>example:</p></li>
</ul>
<p><span class="math display">$$\mathbf{``ignore\ all\ instructions"\ detected}$$</span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>f</strong><strong>l</strong><strong>a</strong><strong>g</strong> <strong>i</strong><strong>n</strong><strong>t</strong><strong>e</strong><strong>r</strong><strong>a</strong><strong>c</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>l</strong><strong>o</strong><strong>g</strong> <strong>e</strong><strong>v</strong><strong>e</strong><strong>n</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>r</strong><strong>e</strong><strong>v</strong><strong>i</strong><strong>e</strong><strong>w</strong> <strong>o</strong><strong>r</strong> <strong>b</strong><strong>l</strong><strong>o</strong><strong>c</strong><strong>k</strong></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Input Sanitization</td>
<td><ul>
<li><p>modifies or rejects potentially dangerous input before it reaches the mode</p></li>
<li><p>similar in principle to preprocessing used against other software attacks</p></li>
<li><p>the workflow is:</p></li>
</ul>
<p><span class="math display"><strong>r</strong><strong>a</strong><strong>w</strong> <strong>u</strong><strong>s</strong><strong>e</strong><strong>r</strong> <strong>i</strong><strong>n</strong><strong>p</strong><strong>u</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>i</strong><strong>n</strong><strong>s</strong><strong>p</strong><strong>e</strong><strong>c</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>r</strong><strong>e</strong><strong>m</strong><strong>o</strong><strong>v</strong><strong>e</strong> <strong>/</strong> <strong>e</strong><strong>s</strong><strong>c</strong><strong>a</strong><strong>p</strong><strong>e</strong> <strong>/</strong> <strong>r</strong><strong>e</strong><strong>j</strong><strong>e</strong><strong>c</strong><strong>t</strong> <strong>s</strong><strong>u</strong><strong>s</strong><strong>p</strong><strong>i</strong><strong>c</strong><strong>i</strong><strong>o</strong><strong>u</strong><strong>s</strong> <strong>c</strong><strong>o</strong><strong>n</strong><strong>t</strong><strong>e</strong><strong>n</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>s</strong><strong>e</strong><strong>n</strong><strong>d</strong> <strong>c</strong><strong>l</strong><strong>e</strong><strong>a</strong><strong>n</strong><strong>e</strong><strong>d</strong> <strong>i</strong><strong>n</strong><strong>p</strong><strong>u</strong><strong>t</strong> <strong>t</strong><strong>o</strong> <strong>m</strong><strong>o</strong><strong>d</strong><strong>e</strong><strong>l</strong></span></p>
<ul>
<li><p>general security principle is essentially the same as defensive preprocessing used to defend against:</p>
<ul>
<li><p>SQL injection</p></li>
<li><p>cross-site scripting</p></li>
<li><p>other malicious user input</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>No Single Defense is Sufficient</td>
<td><ul>
<li><p>the strongest approach is <strong>defense in depth</strong></p></li>
<li><p>that means combining several controls:</p></li>
</ul>
<p><span class="math display"><strong>I</strong><strong>n</strong><strong>p</strong><strong>u</strong><strong>t</strong> <strong>s</strong><strong>a</strong><strong>n</strong><strong>i</strong><strong>t</strong><strong>i</strong><strong>z</strong><strong>a</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong></span></p>
<p><span class="math display"><strong>+</strong></span></p>
<p><span class="math display"><strong>c</strong><strong>l</strong><strong>e</strong><strong>a</strong><strong>r</strong> <strong>i</strong><strong>n</strong><strong>s</strong><strong>t</strong><strong>r</strong><strong>u</strong><strong>c</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong> <strong>b</strong><strong>o</strong><strong>u</strong><strong>n</strong><strong>d</strong><strong>a</strong><strong>r</strong><strong>i</strong><strong>e</strong><strong>s</strong></span></p>
<p><span class="math display"><strong>+</strong></span></p>
<p><span class="math display"><strong>g</strong><strong>u</strong><strong>a</strong><strong>r</strong><strong>d</strong><strong>r</strong><strong>a</strong><strong>i</strong><strong>l</strong><strong>s</strong></span></p>
<p><span class="math display"><strong>+</strong></span></p>
<p><span class="math display"><strong>o</strong><strong>u</strong><strong>t</strong><strong>p</strong><strong>u</strong><strong>t</strong> <strong>f</strong><strong>i</strong><strong>l</strong><strong>t</strong><strong>e</strong><strong>r</strong><strong>i</strong><strong>n</strong><strong>g</strong></span></p>
<p><span class="math display"><strong>+</strong></span></p>
<p><span class="math display"><strong>m</strong><strong>o</strong><strong>n</strong><strong>i</strong><strong>t</strong><strong>o</strong><strong>r</strong><strong>i</strong><strong>n</strong><strong>g</strong></span></p>
<p><strong>Comparing the defenses.</strong></p>
<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Defense</strong></th>
<th style="text-align: center;"><strong>Purpose</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Input sanitization</strong></td>
<td>Detect or remove suspicious input</td>
</tr>
<tr>
<td><strong>Structured prompts</strong></td>
<td>Separate instructions from untrusted data</td>
</tr>
<tr>
<td><strong>Guardrails</strong></td>
<td>Restrict acceptable inputs and outputs</td>
</tr>
<tr>
<td><strong>Output filtering</strong></td>
<td>Prevent unsafe responses from reaching users</td>
</tr>
<tr>
<td><strong>Monitoring &amp; auditing</strong></td>
<td>Detect attacks and identify patterns</td>
</tr>
</tbody>
</table>
<p><strong>Security workflow.</strong></p>
<ul>
<li><p>a robust LLM application can be thought of as:</p></li>
</ul>
<p><span class="math display"><strong>U</strong><strong>n</strong><strong>t</strong><strong>r</strong><strong>u</strong><strong>s</strong><strong>t</strong><strong>e</strong><strong>d</strong> <strong>i</strong><strong>n</strong><strong>p</strong><strong>u</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>S</strong><strong>a</strong><strong>n</strong><strong>i</strong><strong>t</strong><strong>i</strong><strong>z</strong><strong>e</strong> <strong>a</strong><strong>n</strong><strong>d</strong> <strong>v</strong><strong>a</strong><strong>l</strong><strong>i</strong><strong>d</strong><strong>a</strong><strong>t</strong><strong>e</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>S</strong><strong>e</strong><strong>p</strong><strong>a</strong><strong>r</strong><strong>a</strong><strong>t</strong><strong>e</strong> <strong>d</strong><strong>a</strong><strong>t</strong><strong>a</strong> <strong>f</strong><strong>r</strong><strong>o</strong><strong>m</strong> <strong>i</strong><strong>n</strong><strong>s</strong><strong>t</strong><strong>r</strong><strong>u</strong><strong>c</strong><strong>t</strong><strong>i</strong><strong>o</strong><strong>n</strong><strong>s</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>A</strong><strong>p</strong><strong>p</strong><strong>l</strong><strong>y</strong> <strong>s</strong><strong>y</strong><strong>s</strong><strong>t</strong><strong>e</strong><strong>m</strong> <strong>r</strong><strong>u</strong><strong>l</strong><strong>e</strong><strong>s</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>L</strong><strong>L</strong><strong>M</strong> <strong>p</strong><strong>r</strong><strong>o</strong><strong>c</strong><strong>e</strong><strong>s</strong><strong>s</strong><strong>i</strong><strong>n</strong><strong>g</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>V</strong><strong>a</strong><strong>l</strong><strong>i</strong><strong>d</strong><strong>a</strong><strong>t</strong><strong>e</strong> <strong>o</strong><strong>u</strong><strong>t</strong><strong>p</strong><strong>u</strong><strong>t</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>L</strong><strong>o</strong><strong>g</strong> <strong>a</strong><strong>n</strong><strong>d</strong> <strong>m</strong><strong>o</strong><strong>n</strong><strong>i</strong><strong>t</strong><strong>o</strong><strong>r</strong></span></p>
<p><span class="math display"><strong>↓</strong></span></p>
<p><span class="math display"><strong>R</strong><strong>e</strong><strong>t</strong><strong>u</strong><strong>r</strong><strong>n</strong> <strong>r</strong><strong>e</strong><strong>s</strong><strong>p</strong><strong>o</strong><strong>n</strong><strong>s</strong><strong>e</strong></span></p></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>
