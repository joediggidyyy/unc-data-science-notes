> Markdown version for convenient browsing. Original files:
> - PDF: [DATA789_week03_notes.pdf](../DATA789_week03_notes.pdf)
> - DOCX: [DATA789_week03_notes.docx](DATA789_week03_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr>
<th colspan="4">Requirements Engineering &amp; Planning</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Overview</td>
<td colspan="3" style="text-align: right;"><em>6 Sept 2026</em></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>translate goals into machine learning engineering requirements</p></li>
<li><p>explain the main characteristics of training pipeline, inference pipeline, and patterns for serving models</p></li>
<li><p>examine approaches to design ML systems to handle the inevitable mistakes and failures that occur in real-world AI applications</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Readings</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><p>How We Built Infrastructure to Run User Forecasts at Spotify</p>
<p>Molly Zhu, Insights Manager. (n.d.). <em>How we built infrastructure to run user forecasts at Spotify | Spotify Engineering</em>. Spotify Engineering. <a href="https://engineering.atspotify.com/2022/6/how-we-built-infrastructure-to-run-user-forecasts-at-spotify">https://engineering.atspotify.com/2022/6/how-we-built-infrastructure-to-run-user-forecasts-at-spotify</a></p>
<p>Common pitfalls when building generative AI applications</p>
<p>Huyen, C. (2025, January 16). Common pitfalls when building generative AI applications. Chip Huyen. <a href="https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html">https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html</a></p>
<p>Tools Needed This Week:</p>
<p>Apache Airflow</p>
<p><a href="https://airflow.apache.org/docs/apache-airflow/stable/index.html">https://airflow.apache.org/docs/apache-airflow/stable/index.html</a></p>
<p>PyTest</p>
<p><a href="https://docs.pytest.org/en/stable/">https://docs.pytest.org/en/stable/</a></p></td>
</tr>
<tr>
<td colspan="5">How We Built Infrastructure to Run User Forecasts at Spotify</td>
</tr>
<tr>
<td>Overview</td>
<td colspan="4"><p><strong>Scaling User Forecasting Infrastructure At Spotify.</strong></p>
<p>Spotify redesigned its user forecasting infrastructure to support automated, high-quality forecasts that could run weekly or on demand across a rapidly expanding global business.</p></td>
</tr>
<tr>
<td>Purpose And Context</td>
<td colspan="4"><p><strong>Spotify needed a forecasting system that could support rapid international growth.</strong></p>
<ul>
<li><p>the company operated across more than 180 countries</p></li>
<li><p>user forecasts were important for:</p>
<ul>
<li><p>business planning</p></li>
<li><p>measuring company health</p></li>
</ul></li>
<li><p>older forecasting processes were too slow and difficult to scale</p></li>
<li><p>the goal was to generate reliable forecasts for individual markets</p></li>
<li><p>forecasts needed to run automatically each week</p></li>
<li><p>analysts also needed the ability to generate forecasts on demand</p></li>
</ul></td>
</tr>
<tr>
<td>Core Design Idea</td>
<td colspan="4"><p><strong>Forecasting was treated as a production system rather than only a statistical modeling problem.</strong></p>
<ul>
<li><p>the system combined:</p>
<ul>
<li><p>automated modeling</p></li>
<li><p>large-scale computation</p></li>
<li><p>data quality checks</p></li>
<li><p>model validation</p></li>
<li><p>visualization</p></li>
<li><p>business knowledge</p></li>
<li><p>human review</p></li>
</ul></li>
</ul>
<p><strong>Work that could previously take months on one machine could be completed within hours.</strong></p></td>
</tr>
<tr>
<td>Forecasting Architecture</td>
<td colspan="4"><p><strong>Spotify divided markets into three main forecasting categories:</strong></p>
<ul>
<li><p>mature markets</p></li>
<li><p>new markets</p></li>
<li><p><img src="generated_media\DATA789_week03_notes\media\image1.jpeg" style="width:4.81181in;height:2.70833in" />custom models</p></li>
</ul>
<p>ChatGPT 5.6 Sol</p>
<ul>
<li><p>different market conditions required different modeling strategies</p></li>
<li><p>the amount of historical data determined which approach was most appropriate</p></li>
</ul>
<p><strong>Mature Markets.</strong></p>
<ul>
<li><p>mature markets had enough historical data for traditional time-series forecasting</p></li>
<li><p>models could learn:</p>
<ul>
<li><p>long-term trends</p></li>
<li><p>seasonal patterns</p></li>
<li><p>holiday effects</p></li>
<li><p>changes in growth</p></li>
<li><p>data was cleaned before training</p></li>
<li><p>unusual one-time events were removed when they were unlikely to repeat</p></li>
</ul></li>
<li><p>this prevented exceptional historical events from being treated as normal future patterns</p></li>
</ul>
<p><strong>Mature Market Pipeline.</strong></p>
<ul>
<li><p>the mature-market workflow included:</p>
<ul>
<li><p>data preparation</p></li>
<li><p>model training</p></li>
<li><p>hyperparameter tuning</p></li>
<li><p>cross-validation</p></li>
<li><p>model selection</p></li>
<li><p>holdout evaluation</p></li>
<li><p>forecast generation</p></li>
<li><p>quality control</p></li>
<li><p>publication</p></li>
</ul></li>
<li><p>this was the most computationally expensive part of the system</p></li>
</ul>
<p><strong>Model Selection.</strong></p>
<ul>
<li><p>Spotify evaluated many combinations of:</p>
<ul>
<li><p>markets</p></li>
<li><p>models</p></li>
<li><p>hyperparameters</p></li>
<li><p>validation periods</p></li>
</ul></li>
<li><p>candidate models were tested in parallel</p>
<ul>
<li><p>each configuration produced an error measurement</p></li>
<li><p>the strongest models were selected using weighted error</p></li>
<li><p>final candidates were evaluated against a holdout dataset</p></li>
<li><p>the holdout data was not used during model tuning</p></li>
</ul></li>
<li><p>this reduced the risk of choosing models that only performed well on data already used during development</p></li>
</ul>
<p><strong>New Markets.</strong></p>
<ul>
<li><p>new markets had little or no historical user data</p></li>
<li><p>this created a cold-start forecasting problem</p></li>
<li><p>traditional time-series models could not be used effectively</p></li>
<li><p>Spotify instead used proxy markets</p></li>
</ul>
<p><strong>Proxy-Based Forecasting.</strong></p>
<ul>
<li><p>external information was used to identify existing markets that resembled a new market</p></li>
<li><p>data included:</p>
<ul>
<li><p>macroeconomic information</p></li>
<li><p>music-related information</p></li>
<li><p>market characteristics</p></li>
</ul></li>
<li><p>clustering models identified similar markets</p>
<ul>
<li><p>these existing markets became proxies for the new market</p></li>
</ul></li>
<li><p>Spotify then used historical behavior from the proxy markets to estimate likely growth in the new market</p></li>
</ul>
<p><strong>Cold-Start Lesson.</strong></p>
<ul>
<li><p>when historical data is insufficient:</p>
<ul>
<li><p>the problem may need to be reformulated</p></li>
</ul></li>
<li><p>Spotify did not force a traditional time-series model onto limited data</p></li>
<li><p>instead, the system transferred information from similar markets with known histories</p></li>
</ul>
<p><strong>Custom Models.</strong></p>
<ul>
<li><p>some markets did not fit the mature-market or new-market workflows</p></li>
<li><p>these markets required custom handling</p></li>
<li><p>custom cases could include:</p>
<ul>
<li><p>experimental models</p></li>
<li><p>direct data scientist review</p></li>
<li><p>special business information</p></li>
<li><p>major upcoming campaigns</p></li>
<li><p>unusual market conditions</p></li>
</ul></li>
<li><p>this preserved human judgment when automated models did not contain enough context</p></li>
</ul></td>
</tr>
<tr>
<td>Infrastructure And Scaling</td>
<td colspan="4"><p><strong>Spotify used different infrastructure for different computational workloads.</strong></p>
<ul>
<li><p>Google Cloud Dataflow and Apache Beam:</p>
<ul>
<li><p>used for large parallel workloads</p></li>
</ul></li>
<li><p>containerized Python jobs on Kubernetes were used for smaller tasks</p></li>
<li><p>the system did not parallelize every operation</p></li>
</ul></td>
</tr>
<tr>
<td>When Parallelization Helps</td>
<td colspan="4"><p><strong>Distributed computing reduces runtime for large workloads.</strong></p>
<ul>
<li><p>distributed systems:</p>
<ul>
<li><p>introduce overhead and complexity</p></li>
</ul></li>
<li><p>parallelization:</p>
<ul>
<li><p>most useful when the workload is large enough to justify the added infrastructure</p></li>
</ul></li>
<li><p>Spotify found that better modeling decisions could sometimes reduce computation more effectively than adding more hardware</p></li>
</ul></td>
</tr>
<tr>
<td>Reducing Computational Cost</td>
<td colspan="4"><p><strong>Computational cost could be reduced by:</strong></p>
<ul>
<li><p>narrowing the hyperparameter search space</p></li>
<li><p>choosing models appropriate for the problem</p></li>
<li><p>avoiding unnecessary combinations</p></li>
<li><p>using parallel infrastructure only when beneficial</p></li>
<li><p>modeling efficiency and infrastructure efficiency were treated as related problems</p></li>
</ul></td>
</tr>
<tr>
<td>Quality Control</td>
<td colspan="4"><p><strong>Forecast generation was followed by automated quality checks.</strong></p>
<ul>
<li><p>results were distributed through internal systems</p></li>
<li><p>new forecasts could be compared with previous official forecasts</p></li>
<li><p>visualizations helped identify unusual changes or trends</p></li>
<li><p>visual inspection remained important because some problems are easier to recognize visually than through numerical metrics alone</p></li>
</ul></td>
</tr>
<tr>
<td>Human Intervention</td>
<td colspan="4"><p><strong>Historical data cannot represent every future event.</strong></p>
<ul>
<li><p>business stakeholders may know about future conditions that the model cannot observe</p></li>
<li><p>examples include:</p>
<ul>
<li><p>marketing campaigns</p></li>
<li><p>sales campaigns</p></li>
<li><p>product changes</p></li>
<li><p>market-specific events</p></li>
</ul></li>
<li><p>the system allowed this information to influence the final forecast</p></li>
<li><p>automation therefore supported human judgment rather than completely replacing it</p></li>
</ul></td>
</tr>
<tr>
<td>Engineering Lessons</td>
<td colspan="4"><p><strong>Core Logic Requires Strong Controls.</strong></p>
<ul>
<li><p>critical forecasting logic received:</p>
<ul>
<li><p>testing</p></li>
<li><p>peer review</p></li>
<li><p>documentation</p></li>
<li><p>release controls</p></li>
<li><p>integration testing</p></li>
</ul></li>
<li><p>less critical components could remain more flexible</p>
<ul>
<li><p>examples included:</p>
<ul>
<li><p>visualization</p></li>
<li><p>email-generation code</p></li>
</ul></li>
</ul></li>
<li><p>this allowed faster iteration without weakening the reliability of the core forecasting system</p></li>
</ul></td>
</tr>
<tr>
<td>Scaling Is Not Always The Best Solution</td>
<td colspan="4"><p><strong>More computing resources do not automatically produce a better system.</strong></p>
<ul>
<li><p>distributed infrastructure adds complexity</p></li>
<li><p>a smaller hyperparameter space may reduce runtime more effectively</p></li>
<li><p>a better model choice may reduce computation more effectively</p></li>
<li><p>engineering decisions should balance:</p>
<ul>
<li><p>speed</p></li>
<li><p>cost</p></li>
<li><p>complexity</p></li>
</ul></li>
</ul>
<p><strong>Simplicity Matters.</strong></p>
<ul>
<li><p>small improvements in predictive accuracy may not justify major increases in system complexity</p></li>
<li><p>new functionality does not always need to become part of the core infrastructure</p></li>
<li><p>some features can remain separate extensions</p></li>
<li><p>production systems should prioritize:</p>
<ul>
<li><p>reliability</p></li>
<li><p>maintainability</p></li>
<li><p>clarity</p></li>
<li><p>scalability</p></li>
<li><p>reasonable predictive performance</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Common Pitfalls When Building Generative AI Applications</td>
</tr>
<tr>
<td>Overview</td>
<td colspan="4">Chip Huyen identifies six recurring mistakes that appear when teams build generative AI products. The central argument is that building a successful AI application requires much more than choosing a capable model. Many failures come from product design, engineering decisions, evaluation methods, and organizational strategy. Generative AI should be treated as one possible tool for solving a problem. It should not become the problem-solving strategy itself. The easiest stage is often building an impressive demonstration. The difficult stage is creating a reliable product that users actually need.</td>
</tr>
<tr>
<td>Core Idea</td>
<td colspan="4"><p><strong>Building a convincing AI demo is relatively easy.</strong></p>
<ul>
<li><p>building a reliable and useful AI product is much harder</p></li>
<li><p>many failures come from:</p>
<ul>
<li><p>product design</p></li>
<li><p>evaluation,</p></li>
<li><p>engineering complexity</p></li>
<li><p>poor use-case selection</p></li>
</ul></li>
</ul>
<p><strong>The central principle is to start with the problem, not with generative AI.</strong></p></td>
</tr>
<tr>
<td>Pitfall 1: Using Generative AI When It Is Not Needed</td>
<td colspan="4"><p><strong>Problem.</strong></p>
<ul>
<li><p>teams sometimes choose generative AI before deciding whether it is the best solution</p></li>
<li><p>a task may already have a simpler statistical, optimization, or rule-based solution</p></li>
<li><p>an LLM can solve a problem without being the most efficient way to solve it</p></li>
</ul>
<p><strong>Example.</strong></p>
<ul>
<li><p>an energy scheduling system used an LLM to decide when household activities should occur</p></li>
<li><p>a conventional scheduling or optimization method might have produced similar results with less complexity</p></li>
</ul>
<p><strong>Lesson.</strong></p>
<ul>
<li><p>first determine what the problem requires</p></li>
<li><p>then decide whether generative AI provides a meaningful advantage</p></li>
</ul></td>
</tr>
<tr>
<td>Pitfall 2: Blaming The Model For A Bad Product</td>
<td colspan="4"><p><strong>Problem.</strong></p>
<ul>
<li><p>a technically capable model can still produce an unsuccessful product</p></li>
<li><p>model quality is only one part of the user experience</p></li>
<li><p>users may want something different from what developers initially expect</p></li>
</ul>
<p><strong>Examples.</strong></p>
<ul>
<li><p>meeting-summary users cared more about identifying action items than about receiving the perfect summary</p></li>
<li><p>job-search users wanted guidance on how to improve their fit, not only a prediction of whether they matched a role</p></li>
<li><p>chatbot users often responded better when the interface suggested useful questions instead of presenting an empty text box</p></li>
</ul>
<p><strong>Lesson.</strong></p>
<ul>
<li><p>product design should be based on real user behavior</p></li>
<li><p>model accuracy does not automatically create user value</p></li>
</ul></td>
</tr>
<tr>
<td>Pitfall 3: Starting With Too Much Complexity</td>
<td colspan="4"><p><strong>Problem.</strong></p>
<ul>
<li><p>AI teams often introduce advanced infrastructure before proving that it is necessary</p></li>
<li><p>common examples include:</p>
<ul>
<li><p>agent frameworks</p></li>
<li><p>vector databases</p></li>
<li><p>fine-tuning</p></li>
<li><p>complex caching systems</p></li>
<li><p>large orchestration frameworks</p></li>
</ul></li>
</ul>
<p><strong>Why This Matters.</strong></p>
<ul>
<li><p>additional abstractions make systems harder to understand and debug</p></li>
<li><p>frameworks can also hide prompts, internal logic, and unexpected behavior</p></li>
<li><p>when something fails, the source of the problem becomes harder to identify</p></li>
</ul>
<p><strong>Lesson.</strong></p>
<ul>
<li><p>start with the simplest architecture that can test the idea</p></li>
<li><p>add complexity only when a specific limitation justifies it</p></li>
</ul></td>
</tr>
<tr>
<td>Pitfall 4: Overestimating Early Success</td>
<td colspan="4"><p><strong>Problem.</strong></p>
<ul>
<li><p>AI prototypes can reach apparently strong performance very quickly</p></li>
<li><p>the final improvements needed for production are much harder</p></li>
<li><p>Huyen describes teams reaching roughly 80 percent of the desired experience quickly, then spending much longer pushing toward production quality</p></li>
</ul>
<p><strong>The Difficult Final Stage.</strong></p>
<ul>
<li><p>remaining problems often include:</p>
<ul>
<li><p>hallucinations</p></li>
<li><p>edge cases</p></li>
<li><p>latency</p></li>
<li><p>incorrect tool use</p></li>
<li><p>misunderstood user intent</p></li>
<li><p>inconsistent outputs</p></li>
<li><p>security and privacy</p></li>
<li><p>provider failures</p></li>
<li><p>model changes</p></li>
<li><p>safety and compliance</p></li>
</ul></li>
</ul>
<p><strong>Lesson.</strong></p>
<ul>
<li><p>prototype success does not mean production readiness</p></li>
<li><p>the last portion of system quality may require more engineering effort than the initial prototype</p></li>
</ul></td>
</tr>
<tr>
<td>Pitfall 5: Replacing Human Evaluation Too Early</td>
<td colspan="4"><p><strong>Problem.</strong></p>
<ul>
<li><p>automated evaluation is useful, but it cannot fully replace human judgment</p></li>
<li><p>LLM-as-a-judge systems can evaluate large numbers of responses</p></li>
<li><p>however, the evaluator is also a model</p></li>
<li><p>its decisions depend on prompts, criteria, and model behavior</p></li>
</ul>
<p><strong>Human Review.</strong></p>
<ul>
<li><p>strong teams still inspect real outputs manually</p></li>
<li><p>human evaluation can reveal:</p>
<ul>
<li><p>unexpected failure patterns</p></li>
<li><p>new user behavior</p></li>
<li><p>changes that metrics do not capture</p></li>
<li><p>cases where automated evaluation disagrees with human judgment</p></li>
</ul></li>
</ul>
<p><strong>Lesson.</strong></p>
<ul>
<li><p>automated evaluation should scale human evaluation rather than eliminate it</p></li>
<li><p>evaluation should continue throughout the life of the system</p></li>
</ul></td>
</tr>
<tr>
<td>Pitfall 6: Choosing Use Cases Without A Strategy</td>
<td colspan="4"><p><strong>Problem.</strong></p>
<ul>
<li><p>organizations can build many AI applications without creating meaningful business value</p></li>
<li><p>employees often identify problems from their own daily workflows</p></li>
<li><p>those problems may be real, but they are not necessarily the highest-value opportunities for the organization</p></li>
</ul>
<p><strong>Common Result.</strong></p>
<ul>
<li><p>companies may create many:</p>
<ul>
<li><p>chatbots</p></li>
<li><p>text-to-SQL tools</p></li>
<li><p>coding assistants</p></li>
<li><p>internal productivity tools</p></li>
</ul></li>
<li><p>individual projects may work while the overall AI investment produces little measurable return</p></li>
</ul>
<p><strong>Lesson.</strong></p>
<ul>
<li><p>use cases should be evaluated according to:</p>
<ul>
<li><p>business impact</p></li>
<li><p>cost</p></li>
<li><p>technical feasibility</p></li>
<li><p>expected return</p></li>
<li><p>strategic importance</p></li>
</ul></li>
</ul>
<p><strong>AI adoption needs an organizational strategy, not simply a collection of experiments.</strong></p></td>
</tr>
<tr>
<td>The Demo-To-Product Gap</td>
<td colspan="4"><p><strong>Foundation models make prototypes unusually easy to build.</strong></p>
<ul>
<li><p>a small amount of code and prompting can produce an impressive demonstration</p></li>
<li><p>production systems face a much larger set of requirements</p></li>
<li><p>they must remain reliable across different:</p>
<ul>
<li><p>users</p></li>
<li><p>inputs,</p></li>
<li><p>environments</p></li>
<li><p>failure conditions</p></li>
</ul></li>
<li><p>they must also handle:</p>
<ul>
<li><p>security</p></li>
<li><p>privacy</p></li>
<li><p>latency</p></li>
<li><p>safety</p></li>
<li><p>compliance</p></li>
<li><p>model changes</p></li>
<li><p>unexpected behavior</p></li>
</ul></li>
</ul>
<p><strong>This creates a large gap between showing that an AI system can work and proving that it can work reliably.</strong></p></td>
</tr>
<tr>
<td>Recommended Engineering Approach</td>
<td colspan="4"><p><strong>Start With The Problem.</strong></p>
<ul>
<li><p>understand the user need before selecting the technology</p></li>
</ul>
<p><strong>Use The Simplest Viable System.</strong></p>
<ul>
<li><p>avoid adding infrastructure until there is evidence that it is required</p></li>
</ul>
<p><strong>Evaluate With Real Users.</strong></p>
<ul>
<li><p>user behavior often reveals needs that initial requirements miss</p></li>
</ul>
<p><strong>Keep Humans In The Evaluation Loop.</strong></p>
<ul>
<li><p>automated metrics should be checked against human judgment</p></li>
</ul>
<p><strong>Expect The Final Improvements To Be Expensive.</strong></p>
<ul>
<li><p>production reliability requires substantial work beyond the prototype</p></li>
</ul>
<p><strong>Choose Use Cases Strategically.</strong></p>
<ul>
<li><p>AI projects should be selected for their potential value rather than for technological novelty</p></li>
</ul></td>
</tr>
<tr>
<td>Key Takeaway</td>
<td colspan="4"><p><strong>The main challenge in AI engineering is not getting a model to produce an impressive response.</strong></p>
<ul>
<li><p><strong>the real challenge is building a system that is:</strong></p>
<ul>
<li><p><strong>useful</strong></p></li>
<li><p><strong>reliable</strong></p></li>
<li><p><strong>understandable</strong></p></li>
<li><p><strong>worth maintaining</strong></p></li>
</ul></li>
<li><p><strong>successful teams begin with the problem</strong></p>
<ul>
<li><p><strong>they keep the architecture simple</strong></p></li>
<li><p><strong>they evaluate with humans and real users</strong></p></li>
<li><p><strong>they expect production quality to require significant additional work</strong></p></li>
<li><p><strong>they choose AI projects according to value rather than novelty</strong></p></li>
</ul></li>
</ul>
<p>G<strong>enerative AI is therefore best treated as one engineering tool within a broader product and systems strategy</strong>.</p></td>
</tr>
<tr>
<td colspan="5">Async</td>
</tr>
<tr>
<td colspan="5">Requirements Engineering and Planning for Mistakes</td>
</tr>
<tr>
<td>Overview</td>
<td colspan="4"><p><strong>This unit moves from model development toward production engineering.</strong></p>
<ul>
<li><p>the main goal:</p>
<ul>
<li><p>translate business and system goals into clear engineering requirements</p></li>
</ul></li>
<li><p>the unit also focuses on designing systems that can tolerate:</p>
<ul>
<li><p>mistakes</p></li>
<li><p>failures</p></li>
<li><p>unexpected conditions</p></li>
</ul></li>
<li><p>the central idea:</p>
<ul>
<li><p>production ML systems should assume that failures will occur</p></li>
</ul></li>
</ul>
<p><strong>The engineering task is to detect those failures early, limit their impact, and recover safely.</strong></p></td>
</tr>
<tr>
<td>Requirements, Assumptions, And Specifications</td>
<td colspan="4"><p><img src="generated_media\DATA789_week03_notes\media\image2.jpeg" style="width:4.8125in;height:3.20833in" /><strong>ML systems can be designed using the classic requirements, assumptions, and specifications framework.</strong></p>
<p>ChatGPT 5.6 Sol</p>
<p><strong>Requirements.</strong></p>
<ul>
<li><p>define what the system must achieve</p></li>
<li><p>examples include:</p>
<ul>
<li><p>acceptable prediction quality</p></li>
<li><p>maximum latency</p></li>
<li><p>reliability targets</p></li>
<li><p>business constraints</p></li>
<li><p>safety requirements</p></li>
</ul></li>
</ul>
<p><strong>Assumptions.</strong></p>
<ul>
<li><p>describe conditions that the system expects to remain true</p></li>
<li><p>examples include:</p>
<ul>
<li><p>input data follows expected distributions</p></li>
<li><p>features are available</p></li>
<li><p>upstream services remain operational</p></li>
<li><p>users behave within expected patterns</p></li>
</ul></li>
</ul>
<p><strong>Specifications.</strong></p>
<ul>
<li><p>translate requirements and assumptions into technical behavior</p></li>
<li><p>examples include:</p>
<ul>
<li><p>data validation rules</p></li>
<li><p>deployment procedures</p></li>
<li><p>monitoring thresholds</p></li>
<li><p>rollback conditions</p></li>
<li><p>model performance limits</p></li>
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
<th>Why This Matters</th>
<th><p>Many production failures occur when assumptions are treated as permanent facts,</p>
<ul>
<li><p>an ML system should make important assumptions explicit</p></li>
<li><p>those assumptions can then be monitored and tested</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Training And Inference Pipelines</td>
<td><p><strong>Production ML systems usually contain separate training and inference pipelines.</strong></p>
<p>Training Pipeline.</p>
<ul>
<li><p>responsible for creating and updating models</p></li>
<li><p>common stages include:</p>
<ul>
<li><p>data collection</p></li>
<li><p>data validation</p></li>
<li><p>feature preparation</p></li>
<li><p>model training</p></li>
<li><p>evaluation</p></li>
<li><p>model registration</p></li>
</ul></li>
</ul>
<p><strong>Inference Pipeline.</strong></p>
<ul>
<li><p>responsible for serving predictions to users or downstream systems</p></li>
<li><p>common stages include:</p>
<ul>
<li><p>receiving input</p></li>
<li><p>validating input</p></li>
<li><p>creating features</p></li>
<li><p>running the model</p></li>
<li><p>returning predictions</p></li>
<li><p>logging results</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Key Difference</td>
<td><p><strong>The training pipeline determines how models are created.</strong></p>
<ul>
<li><p>the inference pipeline determines how models behave in production</p></li>
<li><p>a model can perform well during training while still fail during inference because of:</p>
<ul>
<li><p>data changes</p></li>
<li><p>serving problems</p></li>
<li><p>infrastructure failures</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Safe Model Deployment</td>
<td><p><strong>New model versions should not immediately replace the current production system without testing.</strong></p>
<ul>
<li><p>deployment patterns allow teams to reduce the risk of introducing failures</p></li>
</ul></td>
</tr>
<tr>
<td>Blue-Green Deployment</td>
<td><p>T<strong>wo production environments are maintained</strong>.</p>
<ul>
<li><p><strong>one environment serves the current model</strong></p></li>
<li><p><strong>the second environment contains the new model version</strong></p></li>
<li><p><strong>traffic can be switched between environments</strong></p></li>
<li><p><strong>if the new model fails, traffic can quickly return to the previous environment</strong></p></li>
</ul>
<p><strong>Main Benefit</strong>.</p>
<ul>
<li><p><strong>fast rollback with minimal disruption</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Canary Release</td>
<td><p><strong>A small percentage of production traffic is routed to the new model.</strong></p>
<ul>
<li><p>most users continue using the existing version</p></li>
<li><p>engineers monitor the new model before increasing traffic</p></li>
</ul>
<p><strong>Main Benefit.</strong></p>
<ul>
<li><p>limits the number of users affected by an unexpected failure</p></li>
</ul></td>
</tr>
<tr>
<td>Shadow Testing</td>
<td><p><strong>The new model processes real production inputs in parallel with the existing model.</strong></p>
<ul>
<li><p>users continue receiving predictions from the existing system</p></li>
<li><p>the new model's outputs are recorded but not shown to users</p></li>
</ul>
<p><strong>Main Benefit.</strong></p>
<ul>
<li><p>allows testing with realistic traffic without affecting production behavior</p></li>
</ul></td>
</tr>
<tr>
<td>Experimentation Strategies</td>
<td><p><strong>Production changes should be evaluated before full deployment.</strong></p>
<ul>
<li><p><strong>two important approaches are online experiments and simulated or offline experiments</strong></p></li>
</ul></td>
</tr>
<tr>
<td>A/B Testing</td>
<td><p><strong>Users are divided between different system versions.</strong></p>
<ul>
<li><p>one group may receive predictions from the current model</p></li>
<li><p>another group receives predictions from the new model</p></li>
<li><p>outcomes can then be compared using selected metrics</p></li>
</ul>
<p><strong>Possible Metrics.</strong></p>
<ul>
<li><p>prediction quality</p></li>
<li><p>user engagement</p></li>
<li><p>conversion</p></li>
<li><p>latency</p></li>
<li><p>business outcomes</p></li>
<li><p>error rates</p></li>
</ul>
<p><strong>Main Purpose.</strong></p>
<ul>
<li><p>measure whether a model change produces meaningful improvement in the real system</p></li>
</ul></td>
</tr>
<tr>
<td>Offline And Simulated Testing</td>
<td><p><strong>Online experimentation is not always appropriate.</strong></p>
<ul>
<li><p>it may be:</p>
<ul>
<li><p>too risky</p></li>
<li><p>too expensive</p></li>
<li><p>too slow</p></li>
<li><p>ethically inappropriate</p></li>
<li><p>operationally difficult</p></li>
</ul></li>
<li><p>offline experiments can evaluate new behavior using historical or simulated data before exposing users to the change</p></li>
</ul>
<p><strong>Main Purpose.</strong></p>
<ul>
<li><p>reduce risk before production deployment</p></li>
</ul></td>
</tr>
<tr>
<td>Planning For Mistakes</td>
<td><p><strong>Reliable ML systems are designed around the expectation that problems will occur.</strong></p>
<ul>
<li><p>the objective is not to eliminate every possible failure</p></li>
<li><p>the objective is to anticipate likely failures and respond safely</p></li>
</ul></td>
</tr>
<tr>
<td>Common Failure Modes</td>
<td><p><strong>Bad Data.</strong></p>
<ul>
<li><p>inputs may be:</p>
<ul>
<li><p>missing</p></li>
<li><p>malformed,</p></li>
<li><p>corrupted</p></li>
<li><p>outside expected ranges</p></li>
</ul></li>
<li><p>data validation can detect many of these problems before predictions are produced</p></li>
</ul>
<p><strong>Data Drift.</strong></p>
<ul>
<li><p>the statistical distribution of input data may change over time</p></li>
<li><p>the model may begin receiving data that differs from its training data</p></li>
</ul>
<p><strong>Concept Drift.</strong></p>
<ul>
<li><p>the relationship between inputs and outcomes may change</p></li>
<li><p>even valid input data may produce less accurate predictions because the real-world process has changed</p></li>
</ul>
<p><strong>Model Errors.</strong></p>
<ul>
<li><p>models can produce incorrect or unexpected outputs</p></li>
<li><p>performance should therefore be monitored after deployment</p></li>
</ul>
<p><strong>Adversarial Inputs.</strong></p>
<ul>
<li><p>users or external systems may intentionally provide unusual inputs designed to manipulate model behavior</p></li>
<li><p>systems should include:</p>
<ul>
<li><p>validation</p></li>
<li><p>monitoring</p></li>
<li><p>security controls</p></li>
</ul></li>
</ul>
<p><strong>Infrastructure Failures.</strong></p>
<ul>
<li><p>models depend on:</p>
<ul>
<li><p>databases</p></li>
<li><p>APIs</p></li>
<li><p>networks</p></li>
<li><p>compute resources</p></li>
<li><p>other services</p></li>
</ul></li>
</ul>
<p><strong>An outage in any of these components can interrupt inference.</strong></p></td>
</tr>
<tr>
<td>Failure Mitigation</td>
<td><p><strong>Production systems should include mechanisms for both detection and recovery.</strong></p>
<p><strong>Detection.</strong></p>
<ul>
<li><p>monitor data quality</p></li>
<li><p>track model performance</p></li>
<li><p>watch latency and error rates</p></li>
<li><p>detect changes in input distributions</p></li>
<li><p>log abnormal behavior</p></li>
</ul>
<p><strong>Mitigation.</strong></p>
<ul>
<li><p>roll back problematic models</p></li>
<li><p>route traffic to a stable version</p></li>
<li><p>reject invalid inputs</p></li>
<li><p>use fallback behavior</p></li>
<li><p>retrain models when conditions change</p></li>
<li><p>isolate failures before they spread</p></li>
</ul></td>
</tr>
<tr>
<td>Engineering Principle</td>
<td><p><strong>A production ML system should be designed for failure rather than assuming ideal conditions.</strong></p>
<ul>
<li><p>new models should be introduced gradually</p></li>
<li><p>changes should be tested before full deployment</p></li>
<li><p>critical assumptions should be monitored</p></li>
<li><p>failures should have defined recovery procedures</p></li>
</ul></td>
</tr>
<tr>
<td>Key Takeaway</td>
<td><p><strong>Requirements engineering connects ML goals to concrete production behavior.</strong></p>
<ul>
<li><p>requirements:</p>
<ul>
<li><p>define what the system must accomplish</p></li>
</ul></li>
<li><p>assumptions:</p>
<ul>
<li><p>define the conditions the system expects</p></li>
</ul></li>
<li><p>specifications:</p>
<ul>
<li><p>define how those expectations are implemented and tested</p></li>
</ul></li>
<li><p>training and inference pipelines:</p>
<ul>
<li><p>should be treated as separate engineering concerns</p></li>
</ul></li>
<li><p>blue-green deployments, canary releases, and shadow testing:</p>
<ul>
<li><p>reduce deployment risk</p></li>
</ul></li>
<li><p>A/B testing and offline experiments:</p>
<ul>
<li><p>help determine whether changes are beneficial before full adoption</p></li>
</ul></li>
<li><p>production systems should also anticipate:</p>
<ul>
<li><p>bad data</p></li>
<li><p>drift</p></li>
<li><p>model errors</p></li>
<li><p>adversarial inputs</p></li>
<li><p>infrastructure outages</p></li>
</ul></li>
</ul>
<p><strong>The broader lesson is that reliable ML engineering is not based on preventing every mistake.</strong></p>
<ul>
<li><p>it is based on detecting problems quickly, limiting their impact, and recovering safely</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">REQ-ASM-SPEC Model</td>
</tr>
<tr>
<td>Core Idea</td>
<td><blockquote>
<p>Requirements engineering converts ML goals into production requirements. Reliable systems are designed with the expectation that failures will occur.</p>
</blockquote></td>
</tr>
<tr>
<td>Requirements Framework</td>
<td><p><strong>Requirements.</strong></p>
<ul>
<li><p>define what the system must accomplish</p></li>
</ul>
<p>Assumptions.</p>
<ul>
<li><p>define the conditions expected to remain true</p></li>
</ul>
<p><strong>Specifications.</strong></p>
<ul>
<li><p>translate requirements and assumptions into technical rules that can be implemented and tested</p></li>
</ul></td>
</tr>
<tr>
<td>Production Pipelines</td>
<td><p><strong>Training Pipeline.</strong></p>
<ul>
<li><p>creates and updates the model</p></li>
</ul>
<p><strong>Inference Pipeline.</strong></p>
<ul>
<li><p>serves predictions in production</p></li>
</ul>
<p><strong>The two pipelines have different risks and should be engineered separately.</strong></p></td>
</tr>
<tr>
<td>Safe Deployment</td>
<td><p><strong>Blue-Green Deployment.</strong></p>
<ul>
<li><p>maintains two production environments for rapid rollback</p></li>
</ul>
<p><strong>Canary Release.</strong></p>
<ul>
<li><p>routes a small amount of traffic to a new model before wider deployment</p></li>
</ul>
<p><strong>Shadow Testing.</strong></p>
<ul>
<li><p>runs a new model on live traffic without exposing its predictions to users</p></li>
</ul></td>
</tr>
<tr>
<td>Safe Experimentation</td>
<td><p><strong>A/B Testing.</strong></p>
<ul>
<li><p>compares model versions using real users and production metrics</p></li>
</ul>
<p><strong>Offline Or Simulated Testing.</strong></p>
<ul>
<li><p>tests changes without exposing users when online experimentation is too risky or expensive</p></li>
</ul></td>
</tr>
<tr>
<td>Planning For Failure</td>
<td><p><strong>Production systems should anticipate:</strong></p>
<ul>
<li><p>bad or malformed data</p></li>
<li><p>data and concept drift</p></li>
<li><p>model errors</p></li>
<li><p>adversarial inputs</p></li>
<li><p>infrastructure outages</p></li>
</ul></td>
</tr>
<tr>
<td>Detection And Recovery</td>
<td><p><strong>Detection.</strong></p>
<ul>
<li><p>monitor data</p></li>
<li><p>model performance</p></li>
<li><p>latency</p></li>
<li><p>errors</p></li>
<li><p>changing distributions</p></li>
</ul>
<p><strong>Recovery.</strong></p>
<ul>
<li><p>roll back models</p></li>
<li><p>use stable fallbacks</p></li>
<li><p>reject invalid inputs</p></li>
<li><p>retrain when conditions change</p></li>
<li><p>isolate failures before they spread</p></li>
</ul></td>
</tr>
<tr>
<td>Key Takeaway</td>
<td><p><strong>Reliable ML engineering does not depend on preventing every failure.</strong></p>
<ul>
<li><p>it depends on anticipating:</p>
<ul>
<li><p>failure</p></li>
<li><p>detecting problems quickly</p></li>
<li><p>limiting their impact</p></li>
<li><p>recovering safely</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Training and Inference Pipelines</td>
</tr>
<tr>
<td>Core Difference</td>
<td><p><strong>Training and inference pipelines serve different purposes and have different engineering requirements.</strong></p>
<ul>
<li><p>training builds the model</p></li>
<li><p>inference uses the model to make predictions</p></li>
<li><p>keeping both pipelines consistent is a major production challenge</p></li>
</ul></td>
</tr>
<tr>
<td>Training Pipeline</td>
<td><p><strong>Purpose.</strong></p>
<ul>
<li><p>process large amounts of historical data and build models offline</p></li>
</ul>
<p><strong>Typical Workloads.</strong></p>
<ul>
<li><p>reading terabytes of data</p></li>
<li><p>distributed training across clusters</p></li>
<li><p>large batch computations</p></li>
<li><p>model evaluation</p></li>
</ul>
<p><strong>Primary Priorities.</strong></p>
<ul>
<li><p>throughput</p></li>
<li><p>cost efficiency</p></li>
<li><p>model quality</p></li>
<li><p>completion within the required training schedule</p></li>
</ul>
<p><strong>Latency.</strong></p>
<ul>
<li><p>training usually does not require millisecond response times</p></li>
<li><p>a job taking three hours instead of two may be acceptable if it still completes within the required cadence</p></li>
</ul></td>
</tr>
<tr>
<td>Inference Pipeline</td>
<td><p><strong>Purpose.</strong></p>
<ul>
<li><p>produce predictions when new data arrives</p></li>
</ul>
<p><strong>Typical Workloads.</strong></p>
<ul>
<li><p>fetch input data</p></li>
<li><p>preprocess features</p></li>
<li><p>run model inference</p></li>
<li><p>postprocess predictions</p></li>
<li><p>return results</p></li>
</ul>
<p><strong>Primary Priorities.</strong></p>
<ul>
<li><p>low latency</p></li>
<li><p>high reliability</p></li>
<li><p>consistent performance</p></li>
<li><p>scalability under load</p></li>
</ul>
<p><strong>Latency.</strong></p>
<ul>
<li><p>inference may be part of the application's critical path</p></li>
<li><p>users may be waiting directly for the result</p></li>
<li><p>response times are often measured in milliseconds</p></li>
</ul></td>
</tr>
<tr>
<td>Training Versus Inference</td>
<td><p><strong>Training.</strong></p>
<ul>
<li><p>offline</p></li>
<li><p>large-scale computation</p></li>
<li><p>optimized for throughput and cost</p></li>
</ul>
<p><strong>Inference.</strong></p>
<ul>
<li><p>online or production-facing</p></li>
<li><p>serves new requests</p></li>
<li><p>optimized for latency and reliability</p></li>
</ul></td>
</tr>
<tr>
<td>Feature Parity</td>
<td><p><strong>Training and inference must process features in the same way.</strong></p>
<ul>
<li><p>if training calculates a user's average spending over previous months, inference must reproduce that calculation using information available at prediction time</p></li>
</ul></td>
</tr>
<tr>
<td>Train-Serve Skew</td>
<td><p><strong>Train-serve skew occurs when features are computed differently during training and inference.</strong></p>
<ul>
<li><p>the model then receives production inputs that differ from what it learned during training</p></li>
<li><p>this effectively causes the model to solve a different problem at serving time</p></li>
</ul></td>
</tr>
<tr>
<td>Reducing Train-Serve Skew</td>
<td><p><strong>Shared Transformation Code.</strong></p>
<ul>
<li><p>use the same feature-processing logic in both pipelines</p></li>
</ul>
<p><strong>Feature Stores.</strong></p>
<ul>
<li><p>store and serve consistent feature definitions for training and inference</p></li>
</ul></td>
</tr>
<tr>
<td>Data Leakage</td>
<td><p><strong>Training data must not include information that would be unavailable when a real prediction is made.</strong></p>
<ul>
<li><p>future information can artificially improve training results</p></li>
<li><p>the deployed model will not have access to that information</p></li>
<li><p>preventing leakage must therefore be part of training pipeline design</p></li>
</ul></td>
</tr>
<tr>
<td>Model Serving Patterns</td>
<td><p><strong>Online Serving.</strong></p>
<p>ChatGPT 5.6 Sol</p>
<ul>
<li><p>provides predictions through a real-time API</p></li>
<li><p>best suited for:</p>
<ul>
<li><p>interactive applications</p></li>
<li><p>immediate decisions</p></li>
<li><p>user-facing predictions</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA789_week03_notes\media\image3.jpeg" style="width:4.75in;height:3.5625in" /></p>
<p>ChatGPT 5.6 Sol</p>
<blockquote>
<p><strong>Main Requirements.</strong></p>
</blockquote>
<ul>
<li><p>low latency</p></li>
<li><p>high availability</p></li>
<li><p>reliable scaling</p></li>
</ul>
<p><strong>Streaming Serving.</strong></p>
<ul>
<li><p>processes a continuous flow of incoming data</p></li>
<li><p>common examples include:</p>
<ul>
<li><p>sensor feeds</p></li>
<li><p>click streams</p></li>
<li><p>IoT telemetry</p></li>
<li><p>application logs</p></li>
</ul></li>
</ul>
<blockquote>
<p><strong>Main Requirements.</strong></p>
</blockquote>
<ul>
<li><p>continuous processing</p></li>
<li><p>integration with streaming infrastructure</p></li>
<li><p>rapid response to incoming events</p></li>
</ul>
<p><strong>Batch Serving.</strong></p>
<ul>
<li><p>processes many predictions asynchronously</p></li>
<li><p>common examples include:</p>
<ul>
<li><p>daily user scoring</p></li>
<li><p>periodic reports</p></li>
<li><p>scheduled analytics</p></li>
</ul></li>
</ul>
<blockquote>
<p><strong>Main Benefits.</strong></p>
</blockquote>
<ul>
<li><p>lower cost</p></li>
<li><p>efficient processing of large workloads</p></li>
<li><p>no strict real-time latency requirement</p></li>
</ul></td>
</tr>
<tr>
<td>Choosing A Serving Pattern</td>
<td><p><strong>Online.</strong></p>
<ul>
<li><p>use when an immediate response is required</p></li>
</ul>
<p><strong>Batch.</strong></p>
<ul>
<li><p>use when predictions can be produced periodically</p></li>
<li><p>often simpler and less expensive</p></li>
</ul>
<p><strong>Streaming.</strong></p>
<ul>
<li><p>use when data arrives continuously and must be processed as events occur</p></li>
</ul>
<p><strong>Hybrid Systems.</strong></p>
<ul>
<li><p>some systems combine multiple serving patterns</p></li>
<li><p>for example:</p>
<ul>
<li><p>an online model provides an immediate prediction</p></li>
<li><p>a nightly batch process performs deeper analysis</p></li>
</ul></li>
</ul>
<p><strong>The appropriate architecture depends on application requirements, cost, and latency needs.</strong></p></td>
</tr>
<tr>
<td>Online Inference Requirements</td>
<td><p><strong>Service Level Objectives.</strong></p>
<ul>
<li><p>latency requirements should be defined as a distribution rather than only as a single average value</p></li>
<li><p>the system must account for both typical and slower requests</p></li>
</ul>
<p><strong>Operational Planning.</strong></p>
<ul>
<li><p>online systems should plan for:</p>
<ul>
<li><p>timeouts</p></li>
<li><p>traffic spikes</p></li>
<li><p>back pressure</p></li>
<li><p>slow dependencies</p></li>
<li><p>overloaded services</p></li>
</ul></li>
</ul>
<p><strong>Fallbacks.</strong></p>
<ul>
<li><p>systems should define what happens when latency or reliability requirements cannot be met</p></li>
<li><p>possible responses include:</p>
<ul>
<li><p>returning a cached result</p></li>
<li><p>using a simpler model</p></li>
<li><p>using a default prediction</p></li>
<li><p>failing safely instead of waiting indefinitely</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Key Takeaway</td>
<td><p><strong>Training and inference pipelines optimize for different goals.</strong></p>
<ul>
<li><p><strong>training</strong> emphasizes:</p>
<ul>
<li><p>large-scale data processing</p></li>
<li><p>throughput</p></li>
<li><p>cost efficiency</p></li>
</ul></li>
<li><p><strong>inference</strong> emphasizes:</p>
<ul>
<li><p>latency</p></li>
<li><p>reliability</p></li>
<li><p>scalability</p></li>
</ul></li>
<li><p><strong>feature processing</strong>:</p>
<ul>
<li><p>must remain consistent between both pipelines</p></li>
</ul></li>
<li><p><strong>shared transformations</strong> and <strong>feature stores</strong>:</p>
<ul>
<li><p>can reduce train-serve skew</p></li>
</ul></li>
<li><p><strong>training</strong>:</p>
<ul>
<li><p>must also prevent data leakage from future information</p></li>
</ul></li>
<li><p><strong>online</strong>, <strong>streaming</strong>, and <strong>batch serving</strong>:</p>
<ul>
<li><p>each support different application needs</p></li>
</ul></li>
<li><p><strong>reliable production systems</strong> choose the serving pattern that matches the required:</p>
<ul>
<li><p>latency</p></li>
<li><p>workload</p></li>
<li><p>cost</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Right-Sizing, Batching Requests, Autoscaling</td>
</tr>
<tr>
<td>Core Idea</td>
<td><p><strong>Production ML systems must balance performance, cost, and deployment risk.</strong></p>
<ul>
<li><p>inference should use hardware efficiently</p></li>
<li><p>new models should be introduced gradually</p></li>
<li><p>experiments should have predefined metrics and decision rules</p></li>
<li><p>important ML components should also have written requirements</p></li>
</ul></td>
</tr>
<tr>
<td>Managing Inference Cost</td>
<td><p><strong>Cost Per Prediction.</strong></p>
<ul>
<li><p>cloud inference consumes:</p>
<ul>
<li><p>CPU</p></li>
<li><p>GPU</p></li>
<li><p>memory</p></li>
<li><p>network resources</p></li>
</ul></li>
<li><p>cost should therefore be tracked as a production metric</p></li>
<li><p>a useful measure is:</p>
<ul>
<li><p>cost per <span class="math inline">1, 000</span> predictions</p></li>
<li><p>a new model may cost more if it provides enough additional value</p></li>
</ul></li>
<li><p>the important point is that the tradeoff should be visible and intentional</p></li>
</ul>
<p><strong>Right-Sizing Hardware.</strong></p>
<ul>
<li><p>not every model requires a GPU</p></li>
<li><p>smaller workloads may run more cheaply on CPUs</p></li>
<li><p>large transformer models may require one or more GPUs</p></li>
<li><p>hardware should match:</p>
<ul>
<li><p>model size</p></li>
<li><p>traffic volume</p></li>
<li><p>latency requirements</p></li>
<li><p>cost constraints</p></li>
</ul></li>
</ul>
<p><strong>Batching Requests.</strong></p>
<ul>
<li><p>multiple inference requests can sometimes be processed together</p></li>
<li><p>deep learning models are especially efficient when processing batches through vectorized operations</p></li>
</ul>
<p><strong>Tradeoff.</strong></p>
<ul>
<li><p>batching increases throughput and lowers cost</p></li>
<li><p>but requests may wait briefly while a batch is formed</p></li>
<li><p>this can slightly increase latency</p></li>
</ul>
<p><strong>Autoscaling.</strong></p>
<ul>
<li><p>traffic changes over time</p></li>
<li><p>cloud systems can automatically:</p>
<ul>
<li><p>add instances when demand increases</p></li>
<li><p>remove instances when demand falls</p></li>
</ul></li>
<li><p>autoscaling improves resource efficiency</p>
<ul>
<li><p>but it can also create cold-start problems</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Latency Optimization</td>
<td><p><strong>Warm Pools.</strong></p>
<ul>
<li><p>new instances may take time to start and load a model</p></li>
<li><p>this creates a cold start</p></li>
</ul>
<p><strong>Common Solutions.</strong></p>
<ul>
<li><p>keep a minimum number of containers running</p></li>
<li><p>preload models before traffic arrives</p></li>
<li><p>periodically keep serverless services active</p></li>
</ul>
<p><strong>Caching.</strong></p>
<ul>
<li><p>repeated computations do not always need to be performed again</p></li>
</ul>
<p><strong>Feature Cache.</strong></p>
<ul>
<li><p>stores expensive feature-engineering results</p></li>
<li><p>useful when user or entity features change slowly</p></li>
</ul>
<p><strong>Prediction Cache.</strong></p>
<ul>
<li><p>stores recent model outputs</p></li>
<li><p>useful when identical or similar requests occur repeatedly</p></li>
</ul></td>
</tr>
<tr>
<td>Model Optimization</td>
<td><p><strong>Models can sometimes be made faster without significant accuracy loss.</strong></p>
<p><strong>Quantization.</strong></p>
<ul>
<li><p>reduces numerical precision</p></li>
<li><p>can reduce model size and speed up inference</p></li>
</ul>
<p><strong>Distillation.</strong></p>
<ul>
<li><p>trains a smaller model to imitate a larger model</p></li>
</ul>
<p><strong>The smaller model is then deployed for cheaper and faster inference.</strong></p></td>
</tr>
<tr>
<td colspan="2">Autonomous Driving</td>
</tr>
<tr>
<td>Core Idea</td>
<td><p><strong>Requirements engineering makes ML system behavior explicit before deployment.</strong></p>
<ul>
<li><p>the framework separates:</p>
<ul>
<li><p>requirements</p></li>
<li><p>specifications</p></li>
<li><p>assumptions</p></li>
</ul></li>
</ul>
<p><strong>The autonomous driving example shows how each part defines a different aspect of system behavior.</strong></p></td>
</tr>
<tr>
<td>Autonomous Driving Example</td>
<td><p><strong>Requirement.</strong></p>
<ul>
<li><p>prevent the vehicle from leaving its lane unless the movement is intentional</p></li>
<li><p>intentional movement may include:</p>
<ul>
<li><p>turn signal use</p></li>
<li><p>driver input</p></li>
</ul></li>
</ul>
<p><strong>Specification.</strong></p>
<ul>
<li><p>define exactly how the system should achieve the requirement</p></li>
<li><p>possible specifications include:</p>
<ul>
<li><p>detect lane markings using computer vision</p></li>
<li><p>measure deviation from the lane center</p></li>
<li><p>apply corrective steering</p></li>
<li><p>respond within a defined amount of time</p></li>
<li><p>operate under defined conditions such as highway driving above 60 miles per hour</p></li>
</ul></li>
</ul>
<p><strong>Assumptions.</strong></p>
<ul>
<li><p>define what must remain true for the system to work</p></li>
<li><p>examples include:</p>
<ul>
<li><p>camera is functioning</p></li>
<li><p>lane markings are visible</p></li>
<li><p>road conditions allow lane detection</p></li>
</ul></li>
<li><p>if heavy snow covers the lane markings, an important assumption fails</p></li>
<li><p>the system may then be unable to satisfy the original requirement</p></li>
</ul></td>
</tr>
<tr>
<td>Applying The Framework To ML</td>
<td><p><strong>The same structure can be applied to ordinary machine learning systems.</strong></p>
<p><strong>Churn Prediction Example.</strong></p>
<p><strong>Requirement.</strong></p>
<ul>
<li><p>proactively retain customers who are likely to churn</p></li>
</ul>
<p><strong>Specification.</strong></p>
<ul>
<li><p>predict churn with a defined performance threshold</p></li>
<li><p>trigger an intervention after a high-risk prediction</p></li>
<li><p>possible interventions include:</p>
<ul>
<li><p>email</p></li>
<li><p>special offer</p></li>
<li><p>sales follow-up</p></li>
</ul></li>
<li><p>the intervention should occur within a defined period after prediction</p></li>
</ul>
<p><strong>Assumptions.</strong></p>
<ul>
<li><p>customers respond to offers similarly to past customers</p></li>
<li><p>customer activity data is updated reliably</p></li>
<li><p>sales teams follow up when required</p></li>
<li><p>these assumptions include both technical and human components</p></li>
</ul>
<p><strong>Why Assumptions Matter.</strong></p>
<ul>
<li><p>a system can fail even when the model itself works correctly</p></li>
<li><p>the model may depend on:</p>
<ul>
<li><p>data availability</p></li>
<li><p>user behavior</p></li>
<li><p>business processes</p></li>
<li><p>human follow-up</p></li>
<li><p>external systems</p></li>
</ul></li>
<li><p>changes in any of these can break the connection between prediction and intended outcome</p></li>
</ul></td>
</tr>
<tr>
<td>Common Requirements Anti-Patterns</td>
<td><p><strong>Imprecise Goals.</strong></p>
<ul>
<li><p>requirements should not be vague</p></li>
<li><p>example of a weak requirement:</p></li>
<li><p>use AI to enhance engagement</p></li>
<li><p>this does not define:</p>
<ul>
<li><p>what engagement means</p></li>
<li><p>how improvement will be measured</p></li>
<li><p>what level of improvement is acceptable</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Better Requirements</td>
<td><p><strong>Define measurable outcomes.</strong></p>
<ul>
<li><p>identify useful metrics or proxies</p></li>
<li><p>connect the model goal to the actual system or business goal</p></li>
</ul></td>
</tr>
<tr>
<td>Metrics Without Context</td>
<td><p><strong>A strong metric does not automatically mean that a system is useful.</strong></p>
<ul>
<li><p>teams can become focused on metrics such as:</p>
<ul>
<li><p>accuracy</p></li>
<li><p>AUC</p></li>
<li><p>recall</p></li>
<li><p>precision</p></li>
</ul></li>
<li><p>these metrics must be interpreted in the context of the problem</p>
<ul>
<li><p>example:</p>
<ul>
<li><p>a churn model with 99% accuracy may still be useless</p></li>
<li><p>if 99% of customers were not going to churn, a model that predicts everyone as non-churn could appear highly accurate</p></li>
<li><p>the important customers may still be missed</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>Lesson.</strong></p>
<ul>
<li><p>avoid treating isolated model metrics as success</p></li>
<li><p>evaluate whether the metric reflects the real objective</p></li>
</ul>
<p><strong>Implicit Assumptions.</strong></p>
<ul>
<li><p>unwritten assumptions create hidden failure points</p></li>
<li><p>projects often fail because:</p>
<ul>
<li><p>data changes</p></li>
<li><p>user behavior changes</p></li>
<li><p>business processes change</p></li>
<li><p>external systems behave differently</p></li>
</ul></li>
<li><p>nobody notices because the assumptions were never documented or monitored</p></li>
</ul>
<p><strong>Recommended Practice.</strong></p>
<ul>
<li><p>record important assumptions explicitly</p></li>
<li><p>identify how each assumption will be checked</p></li>
<li><p>involve domain experts when identifying assumptions</p></li>
</ul>
<p><strong>Domain knowledge can expose risks that the ML team may not recognize.</strong></p></td>
</tr>
<tr>
<td>Rollback Planning</td>
<td><p><strong>Requirements thinking should include what happens when the system fails.</strong></p>
<ul>
<li><p>teams should define:</p>
<ul>
<li><p>how to disable the new model</p></li>
<li><p>how to restore a previous version</p></li>
<li><p>what fallback behavior should occur</p></li>
<li><p>how users will be protected during failure</p></li>
</ul></li>
</ul>
<p><strong>Main Principle.</strong></p>
<ul>
<li><p>a production system needs a safe path backward</p></li>
<li><p>rollback should be planned before deployment rather than invented during an incident</p></li>
</ul></td>
</tr>
<tr>
<td>Checking Requirements</td>
<td><p><strong>Before finalizing requirements.</strong></p>
<ul>
<li><p>teams should ask:</p>
<ul>
<li><p>is anything vague</p></li>
<li><p>can success be measured</p></li>
<li><p>are useful proxies available</p></li>
<li><p>are assumptions explicit</p></li>
<li><p>can assumptions be monitored</p></li>
<li><p>is there a rollback plan</p></li>
</ul></li>
<li><p>these questions help expose weak requirements before implementation</p></li>
</ul></td>
</tr>
<tr>
<td>Data Assumptions</td>
<td><p><strong>Many important ML assumptions exist in the training data.</strong></p>
<ul>
<li><p>three major areas include:</p>
<ul>
<li><p>representativeness</p></li>
<li><p>label quality</p></li>
<li><p>privacy and compliance</p></li>
</ul></li>
</ul>
<p><strong>Representativeness:</strong></p>
<ul>
<li><p>training data should reflect the population or environment where the model will operate</p></li>
<li><p>teams can compare distributions across important groups</p></li>
</ul>
<p><strong>Data profiling can help determine whether expected populations are represented.</strong></p>
<p><strong>Example Checks.</strong></p>
<ul>
<li><p>compare proportions across important groups</p></li>
<li><p>inspect feature distributions</p></li>
<li><p>identify underrepresented populations</p></li>
<li><p>compare training data with current production data</p></li>
</ul></td>
</tr>
<tr>
<td>Label Quality</td>
<td><p><strong>Poor labels limit model quality regardless of the algorithm used.</strong></p>
<ul>
<li><p>label quality should therefore be treated as an explicit assumption</p></li>
<li><p>one approach is to have experts independently label a smaller sample</p></li>
<li><p>agreement between expert labels can help estimate label reliability</p></li>
</ul></td>
</tr>
<tr>
<td>Privacy And Compliance</td>
<td><p><strong>Data use must satisfy legal and policy requirements.</strong></p>
<ul>
<li><p>privacy and compliance should be evaluated early</p></li>
<li><p>teams should involve legal or compliance experts when necessary</p></li>
<li><p>these requirements should not be treated as assumptions that will automatically hold</p></li>
</ul></td>
</tr>
<tr>
<td>Cross-Disciplinary Work</td>
<td><p><strong>Reliable ML requirements cannot be created by data scientists alone.</strong></p>
<ul>
<li><p>important contributors may include:</p>
<ul>
<li><p>domain experts</p></li>
<li><p>software engineers</p></li>
<li><p>product teams</p></li>
<li><p>operations teams</p></li>
<li><p>legal teams</p></li>
<li><p>compliance teams</p></li>
</ul></li>
<li><p>each group can identify assumptions or failure modes that others may miss</p></li>
</ul></td>
</tr>
<tr>
<td>Training Data As A View Of Reality</td>
<td><p><strong>Training data represents the model's limited view of the world.</strong></p>
<ul>
<li><p>missing populations, poor labels, and outdated patterns create blind spots</p></li>
<li><p>those blind spots become implicit assumptions about reality</p></li>
<li><p>if those assumptions do not hold in production, model performance can degrade</p></li>
</ul></td>
</tr>
<tr>
<td>Key Takeaway</td>
<td><p><strong>Requirements engineering separates what the system should achieve from how it will behave and what conditions it depends on.</strong></p>
<ul>
<li><p>requirements:</p>
<ul>
<li><p>define the desired outcome</p></li>
</ul></li>
<li><p>specifications:</p>
<ul>
<li><p>define measurable system behavior</p></li>
</ul></li>
<li><p>assumptions:</p>
<ul>
<li><p>define the conditions required for success</p></li>
</ul></li>
<li><p>strong ML requirements avoid vague goals and vanity metrics</p></li>
<li><p>important assumptions should be:</p>
<ul>
<li><p>documented</p></li>
<li><p>monitored</p></li>
</ul></li>
<li><p>rollback plans should exist before deployment</p></li>
<li><p>data assumptions should address:</p>
<ul>
<li><p>representativeness</p></li>
<li><p>label quality</p></li>
<li><p>privacy</p></li>
</ul></li>
</ul>
<p><strong>The broader lesson is that reliable ML systems require teams to identify hidden assumptions before those assumptions become production failures.</strong></p></td>
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
<th colspan="2">Train and Serve</th>
</tr>
</thead>
<tbody>
<tr>
<td>Train-Serve Consistency</td>
<td><p><strong>Train-serve skew occurs when features are processed differently during model training and production inference.</strong></p>
<p><img src="generated_media\DATA789_week03_notes\media\image4.jpeg" style="width:4.72222in;height:3.54167in" /></p>
<p>ChatGPT 5.6 Sol</p>
<ul>
<li><p>the model may receive data in production that differs from the data it learned from</p>
<ul>
<li><p>effectively causing it to solve a different problem</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Feature Contracts</td>
<td><p><strong>A feature contract defines how features must behave across the training and inference pipelines.</strong></p>
<ul>
<li><p>the goal is to implement feature extraction once and reuse the same logic for both training and serving</p></li>
<li><p>shared feature processing may include:</p>
<ul>
<li><p>tokenization</p></li>
<li><p>normalization</p></li>
<li><p>transformations</p></li>
<li><p>encoding</p></li>
<li><p>feature construction</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Shared Feature Logic</td>
<td><p><strong>Feature processing should avoid duplicated implementations whenever possible.</strong></p>
<ul>
<li><p>in Python, training code and the API service:</p>
<ul>
<li><p>can import the same shared feature-processing module</p></li>
</ul></li>
<li><p>Spark pipelines:</p>
<ul>
<li><p>may allow transformation logic to be exported and reused</p></li>
</ul></li>
<li><p>feature stores:</p>
<ul>
<li><p>can define features once and materialize them for offline training and online serving</p></li>
</ul></li>
<li><p>shared implementations:</p>
<ul>
<li><p>reduce the possibility that training and serving logic gradually diverge</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Feature Versioning</td>
<td><p><strong>Feature definitions can change as an ML system evolves.</strong></p>
<ul>
<li><p>features should therefore be versioned and associated with compatible model versions</p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>changing how age values are bucketed changes the meaning of the resulting feature</p></li>
</ul></li>
</ul></li>
<li><p>a model trained using the new age-bucketing definition:</p>
<ul>
<li><p>may no longer be compatible with the previous feature-processing code</p></li>
</ul></li>
</ul>
<p><strong>Feature versions help preserve reproducibility and backward compatibility.</strong></p></td>
</tr>
<tr>
<td>Backfills And Late Data</td>
<td><p><strong>Training and serving pipelines may have different access to historical information.</strong></p>
<ul>
<li><p>batch systems:</p>
<ul>
<li><p>can often incorporate data that arrives late by reconstructing historical features after the fact</p></li>
</ul></li>
<li><p>an online inference system:</p>
<ul>
<li><p>generally, must make predictions using whatever data is available at that moment</p></li>
<li><p>for example:</p>
<ul>
<li><p>logs from yesterday may arrive one day late because of a pipeline delay</p></li>
</ul></li>
</ul></li>
<li><p>the training pipeline:</p>
<ul>
<li><p>can eventually reconstruct the complete user history</p></li>
<li><p>the production system may not have accessed that information at prediction time</p></li>
</ul></li>
</ul>
<p><strong>This creates a potential difference between training conditions and real-world serving conditions.</strong></p></td>
</tr>
<tr>
<td>Train-Serve Assumptions</td>
<td><p><strong>ML systems often implicitly assume that serving data is as complete and current as the data used during training.</strong></p>
<ul>
<li><p>this assumption should be documented and tested because production data may not satisfy it</p></li>
<li><p>differences between offline and online feature computation should be explicitly identified</p></li>
</ul></td>
</tr>
<tr>
<td>Feature Contract Documentation</td>
<td><p><strong>A feature contract should document:</strong></p>
<ul>
<li><p>each feature used by the model</p></li>
<li><p>the definition of each feature</p></li>
<li><p>how the feature is computed</p></li>
<li><p>the expected relationship between:</p>
<ul>
<li><p>training</p></li>
<li><p>serving implementations</p></li>
</ul></li>
<li><p>known differences between offline and online computation</p></li>
<li><p>any approximations required for real-time processing</p></li>
<li><p>the expected error introduced by those approximations</p></li>
</ul></td>
</tr>
<tr>
<td>Train-Serve Parity Testing</td>
<td><p><strong>Training and serving pipelines should be tested for feature parity.</strong></p>
<ul>
<li><p>representative real examples:</p>
<ul>
<li><p>can be passed independently through the training feature pipeline and the serving feature pipeline</p></li>
</ul></li>
<li><p>the resulting feature values:</p>
<ul>
<li><p>should then be compared</p></li>
</ul></li>
<li><p>unexpected differences:</p>
<ul>
<li><p>indicate train-serve skew</p></li>
<li><p>should be investigated before deployment</p></li>
</ul></li>
</ul>
<p><strong>Feature consistency should be treated with the same rigor as a software API contract.</strong></p></td>
</tr>
<tr>
<td>Nonfunctional Requirements</td>
<td><p><strong>ML requirements include more than predictive accuracy and model selection.</strong></p>
<ul>
<li><p>nonfunctional requirements:</p>
<ul>
<li><p>describe the broader quality characteristics expected from the production system</p></li>
</ul></li>
<li><p>important categories include:</p>
<ul>
<li><p>performance</p></li>
<li><p>availability and reliability</p></li>
<li><p>security and privacy</p></li>
<li><p>maintainability</p></li>
<li><p>fairness and transparency</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Fairness And Transparency</td>
<td><p><strong>ML systems should include requirements for identifying and mitigating bias.</strong></p>
<ul>
<li><p>fairness and transparency:</p>
<ul>
<li><p>should be considered during system design</p></li>
</ul></li>
</ul>
<p><strong>These requirements become especially important when model decisions affect people or high-impact processes.</strong></p></td>
</tr>
<tr>
<td>Service-Level Objectives</td>
<td><p><strong>ML systems can borrow service-level objectives, or SLOs, from site reliability engineering.</strong></p>
<ul>
<li><p>defines a measurable reliability or quality target for a service</p></li>
<li><p>traditional SLOs commonly focus on:</p>
<ul>
<li><p>availability</p></li>
<li><p>latency</p></li>
</ul></li>
</ul>
<p><strong>ML services can extend the concept to model quality.</strong></p>
<ul>
<li><p>for example:</p></li>
<li><p>precision should remain above <span class="math inline">0.80 </span>on live data</p>
<ul>
<li><p>based on periodic evaluation against observed labels</p></li>
</ul></li>
<li><p>a sustained drop below the threshold:</p>
<ul>
<li><p>represents a violation of the quality SLO</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>ML Quality SLOs</td>
<td><p><strong>ML failures are not always binary.</strong></p>
<ul>
<li><p>a service:</p>
<ul>
<li><p>can remain technically available while the quality of its predictions deteriorates</p></li>
</ul></li>
<li><p>quality SLOs may therefore monitor:</p>
<ul>
<li><p>accuracy on rolling evaluation data</p></li>
<li><p>precision or recall</p></li>
<li><p>model calibration</p></li>
<li><p>business KPI correlation</p></li>
<li><p>other application-specific measures of prediction quality</p></li>
</ul></li>
<li><p>a significant quality decline:</p>
<ul>
<li><p>can be operationally similar to an outage because it reduces confidence in the system</p></li>
</ul></li>
</ul>
<p><strong>This is particularly important in high-impact domains such as healthcare and finance.</strong></p></td>
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
<th>Error Budgets</th>
<th><p>An error budget represents the amount of deviation from an SLO that is acceptable during a defined period.</p>
<p>ChatGPT 5.6 Sol</p>
<p><img src="generated_media\DATA789_week03_notes\media\image5.jpeg" style="width:4.86111in;height:3.64583in" /></p>
<ul>
<li><p>error budgets:</p>
<ul>
<li><p>provide a quantitative way to balance reliability against the introduction of new features or system changes</p></li>
</ul></li>
<li><p>deploying new functionality:</p>
<ul>
<li><p>can increase the risk of instability</p></li>
</ul></li>
<li><p>the error budget:</p>
<ul>
<li><p>establishes how much reliability risk the organization is willing to tolerate</p></li>
</ul></li>
<li><p>SLOs and error budgets:</p>
<ul>
<li><p>should be defined during the requirements stage</p></li>
</ul></li>
</ul>
<p>Both engineering and product management should understand and agree on the expected reliability threshold.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Failure Modes</td>
<td><p><strong>ML systems should be designed with the expectation that failures will occur.</strong></p>
<ul>
<li><p>teams:</p>
<ul>
<li><p>should identify potential failure modes before deployment</p></li>
<li><p>define how each will be detected and mitigated</p></li>
</ul></li>
<li><p>a failure-mode taxonomy may include:</p>
<ul>
<li><p>data faults</p></li>
<li><p>model faults</p></li>
<li><p>system faults</p></li>
<li><p>abuse or adversarial attacks</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Mitigation Planning</td>
<td><p><strong>Each important failure mode should have a corresponding response plan.</strong></p>
<ul>
<li><p>the system:</p>
<ul>
<li><p>should define how failures are detected</p></li>
</ul></li>
<li><p>the team:</p>
<ul>
<li><p>should determine what mitigation is appropriate for each type of failure</p></li>
</ul></li>
<li><p>the appropriate response:</p>
<ul>
<li><p>may depend on the application and the severity of the problem</p></li>
</ul></li>
<li><p>possible responses can include:</p>
<ul>
<li><p>degraded operation</p></li>
<li><p>fallback behavior</p></li>
<li><p>model rollback</p></li>
<li><p>human review</p></li>
<li><p>temporarily disabling affected functionality</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Key Principle</td>
<td><p><strong>A model is only reliable when the data and assumptions used during production remain consistent with those used during training.</strong></p>
<ul>
<li><p>core ML system requirements:</p>
<ul>
<li><p>train-serve consistency</p></li>
<li><p>measurable service-level objectives</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Detection Hooks and Guardrails</td>
</tr>
<tr>
<td>Overview</td>
<td><p><strong>Detection hooks and guardrails help identify problems before they become larger system failures.</strong></p>
<ul>
<li><p>they should be:</p>
<ul>
<li><p>placed throughout the ML system</p></li>
<li><p>connected to the failure modes identified during:</p>
<ul>
<li><p>requirements</p></li>
<li><p><img src="generated_media\DATA789_week03_notes\media\image6.jpeg" style="width:4.83333in;height:3.625in" />risk analysis</p></li>
</ul></li>
</ul></li>
</ul>
<p>ChatGPT 5.6 Sol</p>
<ul>
<li><p>common guardrails include:</p>
<ul>
<li><p>input validation and sanitation</p></li>
<li><p>drift detection</p></li>
<li><p>golden set testing</p></li>
<li><p>rate limiting</p></li>
<li><p>content filtering</p></li>
<li><p>dependency monitoring</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Rate Limiting</td>
<td><p><strong>Rate limiting protects public or user-facing ML APIs from excessive traffic.</strong></p>
<ul>
<li><p>it prevents overwhelming the service by:</p>
<ul>
<li><p>single user</p></li>
<li><p>account</p></li>
<li><p>IP address</p></li>
</ul></li>
</ul>
<p><strong>Rate limiting is primarily a systems control rather than an ML technique, but it protects the ML components from misuse and resource exhaustion.</strong></p></td>
</tr>
<tr>
<td>Content Filtering</td>
<td><p><strong>Content filtering can prevent problematic inputs from reaching the primary model.</strong></p>
<ul>
<li><p>before invoking the main model, LLM-based systems commonly use:</p>
<ul>
<li><p>moderation rules</p></li>
<li><p>moderation model</p></li>
</ul></li>
<li><p>requests containing disallowed content:</p>
<ul>
<li><p>may be rejected before they reach the primary model</p></li>
</ul></li>
<li><p>output filtering:</p>
<ul>
<li><p>can also be used when potentially dangerous responses need additional review or restriction</p></li>
</ul></li>
</ul>
<p><strong>These controls act as guardrails around the ML system.</strong></p></td>
</tr>
<tr>
<td>Dependency Guardrails</td>
<td><p><strong>ML services often depend on external databases, feature stores, APIs, and other services.</strong></p>
<ul>
<li><p>a dependency failure:</p>
<ul>
<li><p>should not necessarily cause the entire ML request to fail</p></li>
</ul></li>
<li><p>for example:</p>
<ul>
<li><p>if a feature database exceeds a defined timeout, the system may:</p>
<ul>
<li><p>skip the unavailable feature</p></li>
<li><p>use a default feature value</p></li>
<li><p>use cached data</p></li>
<li><p>return a less personalized result</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>Partial functionality is often preferable to a complete system failure.</strong></p></td>
</tr>
<tr>
<td>Resilience Through Degradation</td>
<td><p><strong>Guardrails may intentionally reduce functionality under abnormal conditions.</strong></p>
<ul>
<li><p>returning a generic recommendation:</p>
<ul>
<li><p>may provide a worse user experience than personalization</p></li>
<li><p>it is usually preferable to:</p>
<ul>
<li><p>crash</p></li>
<li><p>unreliable decision</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>The goal is to preserve safe and predictable behavior even when part of the system is unavailable.</strong></p></td>
</tr>
<tr>
<td>Detection And Mitigation</td>
<td><p><strong>Detection identifies that a problem is occurring.</strong></p>
<ul>
<li><p>mitigation:</p>
<ul>
<li><p>determines what the system should do in real time to reduce the impact of that problem</p></li>
</ul></li>
<li><p>every important failure mode should have:</p>
<ul>
<li><p>detection mechanism</p></li>
<li><p>mitigation strategy</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Fallback Strategies</td>
<td><p><strong>ML systems should define a backup behavior for situations where the primary model cannot perform its intended task.</strong></p>
<ul>
<li><p>for a personalized recommendation system:</p>
<ul>
<li><p>the fallback might be a list of popular products</p></li>
</ul></li>
<li><p>for an NLP system receiving an unsupported language the fallback might be:</p>
<ul>
<li><p>a template response</p></li>
<li><p>another simpler processing method</p></li>
</ul></li>
<li><p>some systems maintain a lightweight backup model such as:</p>
<ul>
<li><p>logistic regression</p></li>
<li><p>an older stable model version</p></li>
<li><p>a simpler deterministic system</p></li>
</ul></li>
</ul>
<p><strong>The backup can be activated when the primary model fails or when monitoring detects unacceptable behavior.</strong></p></td>
</tr>
<tr>
<td>Circuit Breakers</td>
<td><p><strong>A circuit breaker stops repeatedly calling a dependency that is consistently failing.</strong></p>
<ul>
<li><p>if a feature service repeatedly times out:</p></li>
<li><p>the system may temporarily stop requesting that service and instead use:</p>
<ul>
<li><p>cached feature values</p></li>
<li><p>default feature values</p></li>
</ul></li>
<li><p>the system periodically checks:</p>
<ul>
<li><p>whether the dependency has recovered before restoring normal operation</p></li>
</ul></li>
<li><p>circuit breakers prevent a failing component from:</p>
<ul>
<li><p>consuming resources</p></li>
<li><p>causing failures throughout the larger system</p></li>
</ul></li>
</ul>
<p><strong>Model Deployment Circuit Breakers.</strong></p>
<ul>
<li><p>circuit breaker concepts can also be applied to model deployments</p></li>
<li><p>if monitoring during a canary deployment shows unacceptable model or system behavior:</p>
<ul>
<li><p>the deployment can automatically roll back to the previous stable version</p></li>
</ul></li>
<li><p>this allows monitoring signals to directly trigger mitigation</p></li>
</ul></td>
</tr>
<tr>
<td>Graceful UI Degradation</td>
<td><p><strong>Some failures can be mitigated through the way predictions are presented to users.</strong></p>
<ul>
<li><p>when model confidence is low:</p>
<ul>
<li><p>the interface may avoid acting strongly on the prediction</p></li>
</ul></li>
<li><p>examples include:</p>
<ul>
<li><p>a voice assistant asking the user to clarify an uncertain command</p></li>
<li><p>a search engine presenting more diverse results when ranking confidence is low</p></li>
<li><p>a website showing generic content when personalized content cannot be generated</p></li>
</ul></li>
</ul>
<p><strong>Graceful degradation prevents uncertainty in the ML system from becoming an unnecessary user-facing failure.</strong></p></td>
</tr>
<tr>
<td>Incident Response</td>
<td><p><strong>Prevention and guardrails cannot eliminate every incident.</strong></p>
<ul>
<li><p>teams should prepare playbooks or runbooks:</p>
<ul>
<li><p>describe how to respond when failures occur</p></li>
</ul></li>
</ul>
<p><strong>A runbook provides predefined steps that reduce confusion and response time during an incident.</strong></p></td>
</tr>
<tr>
<td>Runbooks</td>
<td><p><strong>A runbook may contain:</strong></p>
<ul>
<li><p>the steps for diagnosing a specific failure</p></li>
<li><p>links to monitoring dashboards</p></li>
<li><p>relevant log queries</p></li>
<li><p>rollback procedures</p></li>
<li><p>fallback procedures</p></li>
<li><p>contact information</p></li>
<li><p>escalation procedures</p></li>
</ul>
<p><strong>Team members should be familiar with runbooks before an incident occurs.</strong></p></td>
</tr>
<tr>
<td>On-Call Responsibilities</td>
<td><p><strong>Traditional software teams commonly maintain an engineering on-call rotation.</strong></p>
<ul>
<li><p>ML incidents may require additional expertise because:</p>
<ul>
<li><p>a service can fail due to model behavior</p></li>
<li><p>even when the infrastructure remains operational</p></li>
</ul></li>
<li><p>data scientists or ML engineers:</p>
<ul>
<li><p>may need to participate in incident response</p></li>
</ul></li>
<li><p>possible approaches include:</p>
<ul>
<li><p>training infrastructure engineers on ML monitoring</p></li>
<li><p>maintaining a dedicated ML on-call rotation</p></li>
<li><p>creating an escalation path for model-specific incidents</p></li>
</ul></li>
</ul>
<p><strong>On-call personnel should understand how to interpret ML-specific monitoring signals.</strong></p></td>
</tr>
<tr>
<td>Postmortems</td>
<td><p><strong>Significant incidents should be followed by a blameless postmortem.</strong></p>
<ul>
<li><p>the purpose is to understand why the system failed and improve the system rather than assign blame</p></li>
<li><p>ML postmortems:</p>
<ul>
<li><p>can map incidents back to previously identified failure categories</p></li>
</ul></li>
<li><p>questions may include:</p>
<ul>
<li><p>was an important assumption incorrect</p></li>
<li><p>was a failure mode overlooked</p></li>
<li><p>did a requirement fail to hold in production</p></li>
<li><p>was monitoring insufficient</p></li>
<li><p>did mitigation activate correctly</p></li>
</ul></li>
</ul>
<p><strong>The results should be used to update requirements, monitoring, guardrails, and mitigation strategies.</strong></p></td>
</tr>
<tr>
<td>Data Contracts</td>
<td><p><strong>A data contract defines the expected characteristics of data supplied to an ML system.</strong></p>
<ul>
<li><p>contracts can identify:</p>
<ul>
<li><p>data sources</p></li>
<li><p>schemas</p></li>
<li><p>field definitions</p></li>
<li><p>data types</p></li>
<li><p>versioning rules</p></li>
<li><p>freshness expectations</p></li>
<li><p>late data policies</p></li>
<li><p>backfill procedures</p></li>
</ul></li>
</ul>
<p><strong>These expectations help maintain consistency between data producers and the ML systems consuming their data.</strong></p></td>
</tr>
<tr>
<td>Schema Contracts</td>
<td><p><strong>Each important data source should have an explicitly defined schema.</strong></p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>a customer profile database may contain fields that the model expects to receive for every user</p></li>
</ul></li>
<li><p>the system should verify:</p>
<ul>
<li><p>incoming data continues to match the expected schema</p></li>
</ul></li>
</ul>
<p><strong>Unexpected schema changes should trigger alerts or errors rather than silently changing model behavior.</strong></p></td>
</tr>
<tr>
<td>Schema Drift</td>
<td><p>Schema drift occurs when the structure or meaning of incoming data changes.</p>
<ul>
<li><p>automated validation:</p>
<ul>
<li><p>can compare the current schema against the schema expected by the ML system</p></li>
</ul></li>
</ul>
<p><strong>A mismatch can be detected before corrupted or incompatible data propagates through the pipeline.</strong></p></td>
</tr>
<tr>
<td>Late Data Policies</td>
<td><p><strong>Data contracts should define how the system handles delayed or incomplete data.</strong></p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>transaction logs may arrive one day late because an ETL job failed</p></li>
</ul></li>
<li><p>the team should determine in advance whether retraining should:</p>
<ul>
<li><p>wait until the missing data arrives</p></li>
<li><p>continue using the available data</p></li>
<li><p>use an alternative or partial data source</p></li>
</ul></li>
</ul>
<p><strong>The appropriate policy depends on the consequences of incomplete training data.</strong></p></td>
</tr>
<tr>
<td>Backfill Planning</td>
<td><p><strong>New data sources may require historical data to be reconstructed.</strong></p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>introducing a new type of user interaction may create a feature that has no historical values</p></li>
</ul></li>
<li><p>the team should determine whether and how historical values can be backfilled</p></li>
</ul>
<p><strong>Backfill policies help ensure that newly introduced features remain compatible with model training and evaluation.</strong></p></td>
</tr>
<tr>
<td>Personalized Offer Case Study</td>
<td><p><strong>Consider an e-commerce website where users can see up to three personalized discounts or product offers.</strong></p>
<ul>
<li><p>the goal is to increase the probability that a user completes a purchase</p></li>
</ul>
<p><strong>This probability of purchase is commonly measured as conversion.</strong></p></td>
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
<th>Business Goal</th>
<th><p>The business objective may be to increase conversion by approximately 8% compared with generic offers.</p>
<ul>
<li><p>the ML system therefore needs to demonstrate measurable business improvement rather than only good offline prediction metrics</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Ranking Approach</td>
<td><p><strong>The model may score a collection of candidate offers and select the three most relevant for a user.</strong></p>
<ul>
<li><p>candidate offers might include:</p>
<ul>
<li><p><span class="math inline">10%</span> off electronics</p></li>
<li><p>free shipping above a purchase threshold</p></li>
<li><p>category-specific discounts</p></li>
<li><p>other promotional offers</p></li>
</ul></li>
</ul>
<p><strong>The ranking system estimates which offers are most likely to influence a particular user's purchasing behavior.</strong></p></td>
</tr>
<tr>
<td>Evaluation</td>
<td><p><strong>An A/B test can compare personalized offers with a generic baseline.</strong></p>
<ul>
<li><p>a primary metric might be conversion lift</p></li>
<li><p>conversion can be measured as:</p>
<ul>
<li><p>the percentage of sessions that result in a purchase</p></li>
</ul></li>
</ul>
<p><strong>Offline model metrics may still be useful, but the business objective ultimately depends on real user behavior.</strong></p></td>
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
<th>Latency Requirements</th>
<th><p>The personalized offers must load quickly enough to appear naturally within the webpage.</p>
<ul>
<li><p>the offer service may need to:</p>
<ul>
<li><p>retrieve user profile features</p></li>
<li><p>retrieve candidate offers</p></li>
<li><p>score dozens of candidates</p></li>
<li><p>rank the candidates</p></li>
<li><p>return the top three offers</p></li>
</ul></li>
</ul>
<p>All of these operations must remain within the application's latency requirement.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Fairness Requirements</td>
<td><p><strong>Personalization can create fairness concerns.</strong></p>
<ul>
<li><p>the system should monitor whether certain groups consistently receive better or worse promotional offers</p></li>
<li><p>fairness requirements should therefore be included alongside performance and conversion requirements</p></li>
</ul></td>
</tr>
<tr>
<td>Operational Assumptions</td>
<td><p><strong>The recommendation system may depend on assumptions that are outside the model itself.</strong></p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>recommended products are actually in stock</p></li>
<li><p>pricing information is correct</p></li>
<li><p>discount rules are current</p></li>
<li><p>customer profile data is available</p></li>
<li><p>candidate offers remain valid</p></li>
</ul></li>
</ul>
<p><strong>These assumptions should be monitored because a correct model prediction can still produce a bad user experience when surrounding data is incorrect.</strong></p></td>
</tr>
<tr>
<td>Key Principle</td>
<td><p><strong>Reliable ML systems require more than accurate models.</strong></p>
<ul>
<li><p>detection hooks identify:</p>
<ul>
<li><p>problems</p></li>
<li><p>guardrails limit unsafe behavior</p></li>
<li><p>mitigation strategies preserve useful functionality</p></li>
<li><p>incident procedures organize recovery</p></li>
<li><p>data contracts protect the assumptions that models depend on</p></li>
</ul></li>
</ul>
<p><strong>These mechanisms should be designed together as part of the ML system specification.</strong></p></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>
