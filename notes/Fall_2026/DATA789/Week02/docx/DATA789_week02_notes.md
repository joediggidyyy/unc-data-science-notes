> Markdown version for convenient browsing. Original files:
> - PDF: [DATA789_week02_notes.pdf](../DATA789_week02_notes.pdf)
> - DOCX: [DATA789_week02_notes.docx](DATA789_week02_notes.docx)

---

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Setting Goals</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td colspan="2" style="text-align: right;"><em>01 Sept 2026</em></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>estimate the requirements to translate experimental notebooks and proof-of-concept models into scalable, maintainable production code</p></li>
<li><p>identify metrics for complete machine learning pipelines from data ingestion through model deployment</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Readings</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><p>Mitchell M, Wu S, Zaldivar A, et al. Model Cards for Model Reporting. In: Proceedings of the Conference on Fairness, Accountability, and Transparency. ACM; 2019:220-229. <a href="https://arxiv.org/pdf/1810.03993">https://arxiv.org/pdf/1810.03993</a></p>
<p>Brownlee, J. (2021, April 30). Tour of Evaluation Metrics for Imbalanced Classification. MachineLearningMastery.com. <a href="https://machinelearningmastery.com/tour-of-evaluation-metrics-for-imbalanced-classification/">https://machinelearningmastery.com/tour-of-evaluation-metrics-for-imbalanced-classification/</a></p></td>
</tr>
<tr>
<td colspan="5">Model Cards for Model Reporting</td>
</tr>
<tr>
<td>Central Idea</td>
<td colspan="4"><p><strong>Machine-learning models are increasingly used in high-impact areas such as:</strong></p>
<ul>
<li><p>healthcare</p></li>
<li><p>employment</p></li>
<li><p>education</p></li>
<li><p>law enforcement</p></li>
<li><p>criminal justice</p></li>
</ul>
<p><strong>However, released models often include little documentation about:</strong></p>
<ul>
<li><p>their intended applications</p></li>
<li><p>their performance limitations</p></li>
<li><p>the populations on which they were evaluated</p></li>
<li><p>the errors they are likely to make</p></li>
<li><p>the contexts in which they should not be used</p></li>
</ul>
<p><strong>The authors propose model cards as a standardized form of model documentation.</strong></p>
<ul>
<li><p>a model card is a short document—typically one or two pages—that accompanies a trained model</p>
<ul>
<li><p>it explains how the model was:</p>
<ul>
<li><p>developed</p></li>
<li><p>evaluated</p></li>
<li><p>intended to be used</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Why Model Cards Are Needed</td>
<td colspan="4"><p><strong>Overall performance metrics can conceal important differences between groups.</strong></p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>a classifier may achieve high aggregate accuracy while producing substantially higher error rates for:</p>
<ul>
<li><p>particular racial groups</p></li>
<li><p>particular gender groups</p></li>
<li><p>older or younger people</p></li>
<li><p>people with particular skin types</p></li>
<li><p>intersections of these categories</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>Many model failures have historically been discovered only after deployment, when affected users reported them.</strong></p>
<ul>
<li><p>model cards encourage developers to <strong>investigate</strong> and <strong>disclose</strong> these differences before a model is adopted.</p></li>
</ul></td>
</tr>
<tr>
<td>Disaggregated Evaluation</td>
<td colspan="4"><p><strong>A central recommendation is to report model performance separately across relevant factors.</strong></p>
<ul>
<li><p>these factors may include:</p>
<ul>
<li><p>cultural groups</p></li>
<li><p>demographic groups</p></li>
<li><p>phenotypic characteristics</p></li>
<li><p>environmental conditions</p></li>
<li><p>input-capture technologies</p></li>
<li><p>intersections of multiple characteristics</p></li>
<li><p>unitary analysis</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA789_week02_notes\media\image1.jpeg" style="width:4.79167in;height:3.59375in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p><strong>Unitary analysis examines one factor at a time.</strong></p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>performance by age</p></li>
<li><p>performance by gender</p></li>
<li><p>performance by geographic region</p></li>
<li><p>intersectional analysis</p></li>
</ul></li>
</ul>
<p><strong>Intersectional analysis examines combinations of factors.</strong></p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>age and gender</p></li>
<li><p>race and gender</p></li>
<li><p>gender and skin type</p></li>
<li><p>age, disability, and geographic location</p></li>
</ul></li>
</ul>
<p><strong>A model may perform adequately for each broad category while failing for a particular intersection.</strong></p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>aggregate results for women and Black users may appear acceptable even when results for Black women are poor</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Defining Sensitive Groups</td>
<td colspan="4"><p><strong>Group-based evaluation introduces ethical and methodological problems.</strong></p>
<ul>
<li><p>categories such as race and gender:</p>
<ul>
<li><p>are socially constructed</p></li>
<li><p>may not have objective ground-truth labels</p></li>
<li><p>can be incorrectly inferred from appearance</p></li>
<li><p>may not reflect how individuals identify themselves</p></li>
<li><p>can create privacy risks</p></li>
</ul></li>
</ul>
<p>ChatGPT 5.6 Sol</p>
<p><img src="generated_media\DATA789_week02_notes\media\image2.jpeg" style="width:4.64583in;height:3.48419in" /></p>
<p>ChatGPT 5.6 Sol</p>
<ul>
<li><p>where possible, the authors recommend using:</p>
<ul>
<li><p>self-identified labels</p></li>
<li><p>labels explicitly described as perceived rather than self-identified</p></li>
<li><p>public identity information when evaluating public figures</p></li>
</ul></li>
</ul>
<p><strong>Teams should collaborate with privacy, legal, policy, and domain experts before collecting or inferring sensitive attributes.</strong></p></td>
</tr>
<tr>
<td colspan="5">Proposed Model Card Structure</td>
</tr>
<tr>
<td>Model Details</td>
<td colspan="4"><p><strong>This section identifies the model and its origin.</strong></p>
<ul>
<li><p>it should include:</p>
<ul>
<li><p>developer or responsible organization</p></li>
<li><p>model date</p></li>
<li><p>model version</p></li>
<li><p>model type and architecture</p></li>
<li><p>training algorithms and important parameters</p></li>
<li><p>fairness constraints or mitigation methods</p></li>
<li><p>relevant papers or documentation</p></li>
<li><p>citation information</p></li>
<li><p>license</p></li>
<li><p>contact information for questions or feedback</p></li>
</ul></li>
</ul>
<p><strong>Version information is important because model behavior can change substantially between releases.</strong></p>
<ul>
<li><p>organizations are not expected to reveal protected intellectual property</p></li>
<li><p>they should still provide enough information for stakeholders to understand what the model represents</p></li>
</ul></td>
</tr>
<tr>
<td>Intended Use</td>
<td colspan="4"><p><strong>This section defines where and how the model should be used.</strong></p>
<ul>
<li><p>it should identify:</p>
<ul>
<li><p>primary intended applications</p></li>
<li><p>intended users</p></li>
<li><p>intended operating environments</p></li>
<li><p>supported input types</p></li>
<li><p>uses that are explicitly out of scope</p></li>
</ul></li>
</ul>
<p><strong>Out-of-scope uses function like warnings on physical products.</strong></p>
<ul>
<li><p>examples might include:</p>
<ul>
<li><p>not intended for emotion detection</p></li>
<li><p>not validated for medical diagnosis</p></li>
<li><p>not evaluated for text shorter than 100 tokens</p></li>
<li><p>designed only for black-and-white images</p></li>
<li><p>not appropriate for autonomous decision-making</p></li>
</ul></li>
</ul>
<p><strong>A technically functional model is not necessarily appropriate for every related task.</strong></p></td>
</tr>
<tr>
<td>Factors</td>
<td colspan="4"><p><strong>Factors are conditions under which model performance may vary.</strong></p>
<p><strong>Groups</strong></p>
<ul>
<li><p>relevant population characteristics may include:</p>
<ul>
<li><p>age</p></li>
<li><p>gender</p></li>
<li><p>race</p></li>
<li><p>disability</p></li>
<li><p>language</p></li>
<li><p>geographic location</p></li>
<li><p>Fitzpatrick skin type</p></li>
</ul></li>
<li><p>the relevant groups depend on the intended use and the populations most vulnerable to harm</p></li>
</ul>
<p><strong>Instrumentation</strong></p>
<ul>
<li><p>performance can vary according to the technology used to collect inputs</p></li>
<li><p>examples include:</p>
<ul>
<li><p>camera type</p></li>
<li><p>lens type</p></li>
<li><p>image stabilization</p></li>
<li><p>microphone type</p></li>
<li><p>recording software</p></li>
<li><p>sensor resolution</p></li>
<li><p>aperture, shutter speed, or ISO</p></li>
<li><p>environment</p></li>
</ul></li>
</ul>
<p><strong>Environmental conditions may also affect performance.</strong></p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>lighting</p></li>
<li><p>humidity</p></li>
<li><p>background noise</p></li>
<li><p>weather</p></li>
<li><p>network quality</p></li>
<li><p>physical location</p></li>
</ul></li>
</ul>
<p><strong>The model card should distinguish between:</strong></p>
<ul>
<li><p>relevant factors:</p>
<ul>
<li><p>conditions likely to affect performance</p></li>
</ul></li>
<li><p>evaluation factors:</p>
<ul>
<li><p>conditions actually included in testing</p></li>
</ul></li>
<li><p>any gap between these categories should be explained</p></li>
</ul></td>
</tr>
<tr>
<td>Metrics</td>
<td colspan="4"><p><strong>Metrics should reflect the model’s intended use and the consequences of different errors.</strong></p>
<ul>
<li><p>for classification systems, relevant measures may include:</p>
<ul>
<li><p>false-positive rate</p></li>
<li><p>false-negative rate</p></li>
<li><p>false-discovery rate</p></li>
<li><p>false-omission rate</p></li>
<li><p>precision</p></li>
<li><p>recall</p></li>
<li><p>decision thresholds</p></li>
</ul></li>
</ul>
<p><strong>The importance of each error depends on the application and stakeholder.</strong></p>
<ul>
<li><p>for example, in surveillance:</p>
<ul>
<li><p>operators may prioritize a low false-negative rate</p></li>
<li><p>people being surveilled may prioritize a low false-positive rate</p></li>
</ul></li>
</ul>
<p><strong>A model card should report multiple relevant metrics and explain which were prioritized.</strong></p></td>
</tr>
<tr>
<td>Thresholds and Uncertainty</td>
<td colspan="4"><p><strong>When a model converts scores into decisions, the model card should document:</strong></p>
<ul>
<li><p>the decision threshold</p></li>
<li><p>why the threshold was selected</p></li>
<li><p>how performance changes at other thresholds</p></li>
<li><p>statistical uncertainty in the reported results</p></li>
</ul>
<p><strong>Uncertainty measures may include:</strong></p>
<ul>
<li><p>standard deviation</p></li>
<li><p>variance</p></li>
<li><p>confidence intervals</p></li>
<li><p>results across repeated runs</p></li>
<li><p>cross-validation results</p></li>
</ul>
<p><strong>Confidence intervals are especially important for small subgroups.</strong></p>
<ul>
<li><p>an apparently large performance difference may be unreliable when few evaluation examples are available</p></li>
</ul></td>
</tr>
<tr>
<td>Evaluation Data</td>
<td colspan="4"><p><strong>The model card should document the data used to test the model.</strong></p>
<ul>
<li><p>this should include:</p>
<ul>
<li><p>evaluation datasets</p></li>
<li><p>reasons for selecting each dataset</p></li>
<li><p>dataset composition</p></li>
<li><p>preprocessing procedures</p></li>
<li><p>filtering or exclusion rules</p></li>
<li><p>known limitations</p></li>
</ul></li>
</ul>
<p><strong>Evaluation data should represent:</strong></p>
<ul>
<li><p>normal operating conditions</p></li>
<li><p>anticipated use cases</p></li>
<li><p>difficult or unusual cases</p></li>
<li><p>populations that may be especially vulnerable to errors</p></li>
</ul>
<p><strong>Public evaluation datasets are valuable because they allow independent verification and comparison.</strong></p>
<ul>
<li><p>synthetic data may be useful when real data does not adequately represent important cases</p></li>
<li><p>however, synthetic data can test only the patterns included in its design</p></li>
</ul></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr>
<th>Training Data</th>
<th><p>Ideally, the model card should provide training-data information comparable to the evaluation-data documentation.</p>
<ul>
<li><p>this may not always be possible because the data could be:</p>
<ul>
<li><p>proprietary</p></li>
<li><p>confidential</p></li>
<li><p>protected by nondisclosure agreements</p></li>
<li><p>subject to privacy restrictions</p></li>
</ul></li>
</ul>
<p>When full disclosure is impossible, developers should provide basic information about:</p>
<ul>
<li><p>data sources</p></li>
<li><p>population distributions</p></li>
<li><p>relevant group representation</p></li>
<li><p>known gaps</p></li>
<li><p>potential biases encoded in the data</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Quantitative Analysis</td>
<td><p><strong>Evaluation results should be separated by the factors defined earlier.</strong></p>
<ul>
<li><p>the card should include:</p>
<ul>
<li><p>unitary results for individual factors</p></li>
<li><p>intersectional results for combinations of factors</p></li>
<li><p>confidence intervals</p></li>
<li><p>error bars or other measures of variation</p></li>
</ul></li>
</ul>
<p><strong>Group parity in some metrics corresponds to formal definitions of fairness.</strong></p>
<ul>
<li><p>for example:</p></li>
<li><p>equal false-negative rates relate to equality of opportunity</p></li>
<li><p>equal false-positive and false-negative rates relate to equalized odds</p></li>
</ul>
<p><strong>However, no single fairness metric is appropriate for every application.</strong></p>
<ul>
<li><p>metric selection must reflect:</p>
<ul>
<li><p>deployment context</p></li>
<li><p>distribution of potential harms</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Ethical Considerations</td>
<td><p><strong>The model card should explain the ethical issues considered during development.</strong></p>
<ul>
<li><p>questions may include:</p></li>
<li><p>could the model cause harm?</p></li>
<li><p>which people or groups could be affected?</p></li>
<li><p>could harms differ across groups?</p></li>
<li><p>could the model be used in especially sensitive settings?</p></li>
<li><p>were affected communities consulted?</p></li>
<li><p>was the system reviewed by an external board?</p></li>
<li><p>what mitigation measures were applied?</p></li>
<li><p>which risks remain unknown?</p></li>
</ul>
<p><strong>Ethical analysis may not produce a complete solution.</strong></p>
<ul>
<li><p>its purpose is to make risks, assumptions, and unresolved questions visible</p></li>
</ul></td>
</tr>
<tr>
<td>Caveats and Recommendations</td>
<td><p><strong>This section documents remaining limitations.</strong></p>
<ul>
<li><p>it should identify:</p>
<ul>
<li><p>groups missing from the evaluation data</p></li>
<li><p>factors that were not tested</p></li>
<li><p>known performance weaknesses</p></li>
<li><p>additional testing requirements</p></li>
<li><p>conditions under which the model should not be used</p></li>
<li><p>recommendations for fine-tuning or further evaluation</p></li>
<li><p>characteristics of an improved evaluation dataset</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Who Benefits from Model Cards?</td>
<td><p><strong>ML</strong> <strong>practitioners</strong></p>
<ul>
<li><p>evaluate suitability for an intended application</p></li>
<li><p>compare candidate models</p></li>
<li><p>monitor performance across versions</p></li>
<li><p>identify areas requiring additional training</p></li>
</ul>
<p><strong>Software</strong> <strong>developers</strong></p>
<ul>
<li><p>understand model constraints</p></li>
<li><p>design appropriate interfaces and fallbacks</p></li>
<li><p>select decision thresholds</p></li>
<li><p>avoid unsupported applications</p></li>
</ul>
<p><strong>Organizations</strong></p>
<ul>
<li><p>make informed adoption decisions</p></li>
<li><p>compare vendors and models</p></li>
<li><p>evaluate operational and ethical risks</p></li>
</ul>
<p><strong>Policymakers and regulators</strong></p>
<ul>
<li><p>identify questions that should be asked before deployment</p></li>
<li><p>understand possible failure patterns</p></li>
<li><p>assess whether a model is appropriate for a high-impact setting</p></li>
</ul>
<p><strong>Affected individuals.</strong></p>
<ul>
<li><p>understand how a model may influence them</p></li>
<li><p>identify documented limitations</p></li>
<li><p>use disclosed information to challenge or seek remedies for harmful decisions</p></li>
</ul></td>
</tr>
<tr>
<td>Limitations of Model Cards</td>
<td><p><strong>Model cards do not guarantee responsible behavior.</strong></p>
<ul>
<li><p>their usefulness depends on:</p>
<ul>
<li><p>the honesty of their creators</p></li>
<li><p>the quality of the evaluation</p></li>
<li><p>the relevance of the selected groups and metrics</p></li>
<li><p>whether important limitations are disclosed</p></li>
<li><p>whether documentation is updated when the model changes</p></li>
</ul></li>
</ul>
<p><strong>A developer could unintentionally or deliberately present misleading results.</strong></p>
<ul>
<li><p>model cards should therefore complement:</p>
<ul>
<li><p>independent algorithmic audits</p></li>
<li><p>adversarial testing</p></li>
<li><p>qualitative evaluation</p></li>
<li><p>community consultation</p></li>
<li><p>inclusive feedback mechanisms</p></li>
<li><p>regulatory oversight</p></li>
</ul></li>
</ul>
<p><strong>They are one transparency mechanism, but not a substitute for governance or accountability.</strong></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Evaluation Metrics for Imbalanced Classification</th>
</tr>
</thead>
<tbody>
<tr>
<td>Central Idea</td>
<td><p><strong>A classification model is only as useful as the metric used to evaluate it.</strong></p>
<ul>
<li><p>this is especially important for imbalanced classification, where one class contains substantially fewer observations than another</p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>fraud detection</p></li>
<li><p>disease screening</p></li>
<li><p>equipment-failure prediction</p></li>
<li><p>cyberattack detection</p></li>
<li><p>customer-churn prediction</p></li>
<li><p>rare-event forecasting</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>In these problems, the minority class is often the class of greatest practical importance.</strong></p>
<ul>
<li><p>a poorly chosen metric can:</p>
<ul>
<li><p>make an ineffective model appear successful</p></li>
<li><p>hide poor minority-class performance</p></li>
<li><p>select the wrong model</p></li>
<li><p>encourage an unsuitable decision threshold</p></li>
<li><p>produce misleading conclusions about deployment performance</p></li>
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
<th><p>Why Accuracy</p>
<p>Can Be</p>
<p>Misleading</p></th>
<th><p>Accuracy measures the proportion of all predictions that are correct:</p>
<p><span class="math display">$$\text{Accuracy}\mathbf{=}\frac{\text{Correct}\text{~}\text{predictions}}{\text{Total~predictions}}$$</span></p>
<p>Suppose a dataset contains:</p>
<ul>
<li><p>990 negative cases</p></li>
<li><p>10 positive cases</p></li>
</ul>
<p>A model that predicts every case as negative achieves:</p>
<p><span class="math display">$$\mathbf{Accuracy}\mathbf{=}\frac{\mathbf{990}}{\mathbf{1000}}\mathbf{\  =}\mathbf{0.99}$$</span></p>
<ul>
<li><p>the model has 99% accuracy, but it detects none of the positive cases</p></li>
<li><p>therefore, accuracy can be dangerously misleading when:</p>
<ul>
<li><p>one class strongly dominates the dataset</p></li>
<li><p>the minority class is operationally important</p></li>
<li><p>different error types have different consequences</p></li>
</ul></li>
</ul>
<p>Model performance must instead be evaluated using metrics aligned with the application’s objectives and error costs.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Async</td>
</tr>
<tr>
<td colspan="2">Setting Goals and Defining Success Metrics in ML products</td>
</tr>
<tr>
<td>Overview</td>
<td><ul>
<li><p>machine learning products require success criteria that extend beyond model performance</p></li>
<li><p>effective goals connect technical metrics to business outcomes and operational constraints across the full ML system lifecycle</p></li>
</ul></td>
</tr>
<tr>
<td>From Prototype To Product</td>
<td><p><strong>ML product development should consider the full pipeline:</strong></p>
<ul>
<li><p>problem definition</p></li>
<li><p>data preparation</p></li>
<li><p>model building</p></li>
<li><p>deployment</p></li>
<li><p>monitoring</p></li>
</ul>
<p><strong>Cloud deployments introduce additional considerations:</strong></p>
<ul>
<li><p>scalability</p></li>
<li><p>cost</p></li>
<li><p>compliance</p></li>
<li><p>integration with other services</p></li>
</ul>
<p><strong>Success is multidimensional and includes:</strong></p>
<ul>
<li><p>technical performance</p></li>
<li><p>business outcomes</p></li>
<li><p>operational stability</p></li>
</ul></td>
</tr>
<tr>
<td>The Accuracy Trap</td>
<td><p><strong>A common ML project failure is optimizing model accuracy without determining whether higher accuracy supports the actual objective.</strong></p>
<ul>
<li><p>clear goals help ensure that:</p>
<ul>
<li><p>improvements in model metrics translate into useful outcomes</p></li>
<li><p>design choices reflect the intended objective</p></li>
<li><p>experiments are evaluated against appropriate benchmarks</p></li>
<li><p>teams focus on metrics that matter to project success</p></li>
<li><p>iteration remains measurable and purposeful</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Goal Alignment</td>
<td><p><strong>ML systems can be viewed as having three connected layers of goals.</strong></p>
<p><strong>Business Goals:</strong></p>
<ul>
<li><p>business goals describe the high-level outcomes the organization wants to achieve</p>
<ul>
<li><p>examples:</p>
<ul>
<li><p>increase customer retention</p></li>
<li><p>reduce costs</p></li>
<li><p>reduce financial losses</p></li>
<li><p>improve user satisfaction</p></li>
<li><p>increase engagement</p></li>
<li><p><img src="generated_media\DATA789_week02_notes\media\image3.jpeg" style="width:4.80208in;height:3.60139in" />improve safety</p></li>
</ul></li>
</ul></li>
</ul>
<p>ChatGPT 5.6 Sol</p>
<p><strong>ML Goals:</strong></p>
<ul>
<li><p>ML goals translate business objectives into measurable model objectives</p>
<ul>
<li><p>examples:</p>
<ul>
<li><p>recall for a churn model</p></li>
<li><p>precision for a fraud detector</p></li>
<li><p>classification accuracy</p></li>
<li><p>prediction quality associated with user activity</p></li>
</ul></li>
</ul></li>
<li><p>ML metrics often serve as proxies for outcomes that cannot be measured directly</p></li>
</ul>
<p><strong>System Goals:</strong></p>
<ul>
<li><p>system goals define the operational conditions required for the ML product to function effectively</p>
<ul>
<li><p>examples:</p>
<ul>
<li><p>response time</p></li>
<li><p>throughput</p></li>
<li><p>uptime</p></li>
<li><p>cost per prediction</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>All three layers should remain aligned.</strong></p>
<ul>
<li><p>a technically strong model provides little value if it does not:</p>
<ul>
<li><p>improve the relevant business outcome</p></li>
<li><p>cannot operate within the system's constraints</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Fraud Detection Example</td>
<td><p><strong>Business goal:</strong></p>
<ul>
<li><p>reduce financial losses caused by fraud</p></li>
</ul>
<p><strong>ML goal:</strong></p>
<ul>
<li><p>maximize recall</p></li>
<li><p>detect at least 90% of fraudulent transactions</p></li>
</ul>
<p><strong>System goal:</strong></p>
<ul>
<li><p>evaluate each transaction in under 200 milliseconds</p></li>
</ul>
<p><strong>The goals are aligned when higher recall reduces fraud losses while the system processes fraud checks quickly enough to avoid disrupting customer transactions.</strong></p></td>
</tr>
<tr>
<td>Using Proxy Metrics</td>
<td><p><strong>Business objectives are often qualitative and therefore require measurable proxies.</strong></p>
<ul>
<li><p>engagement proxies:</p>
<ul>
<li><p>average session length</p></li>
<li><p>daily active users</p></li>
</ul></li>
<li><p>safety proxy:</p>
<ul>
<li><p>incident rate per thousand hours</p></li>
</ul></li>
</ul>
<p><strong>These business proxies can then be connected to appropriate ML metrics, such as classification performance for incident detection or predictions associated with user activity.</strong></p></td>
</tr>
<tr>
<td>Monitoring Success</td>
<td><p><strong>Business proxies and ML metrics should be monitored together.</strong></p>
<ul>
<li><p>monitoring both levels helps determine whether improvements in model performance are producing meaningful improvements in the real-world objective.</p></li>
</ul>
<p><strong>Core Principle:</strong></p>
<ul>
<li><p>model metrics are useful:</p>
<ul>
<li><p>when they support the broader product objective</p></li>
</ul></li>
<li><p>successful ML products align:</p>
<ul>
<li><p>business goals</p></li>
<li><p>ML goals</p></li>
<li><p>system goals</p></li>
</ul></li>
<li><p>so that technical improvements translate into:</p>
<ul>
<li><p>measurable value under realistic operating constraints</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Machine Learning Evaluation Metrics</td>
</tr>
<tr>
<td>Classification Metrics</td>
<td><p><strong>Model evaluation metrics should be selected based on the type of:</strong></p>
<ul>
<li><p>machine learning task</p></li>
<li><p>real-world consequences of different errors</p></li>
<li><p>classification tasks include:</p>
<ul>
<li><p>spam detection</p></li>
<li><p>medical diagnosis</p></li>
<li><p>fraud detection</p></li>
</ul></li>
<li><p><strong>accuracy</strong></p>
<ul>
<li><p>fraction of all predictions that are correct</p></li>
</ul></li>
<li><p><strong>precision</strong></p>
<ul>
<li><p>fraction of predicted positive cases that are actually positive</p></li>
<li><p>high precision means fewer false positives or false alarms</p></li>
</ul></li>
<li><p><strong>recall</strong></p>
<ul>
<li><p>fraction of actual positive cases correctly identified</p></li>
<li><p>high recall means fewer false negatives or missed cases</p></li>
</ul></li>
<li><p><strong>F1 score</strong></p>
<ul>
<li><p>harmonic mean of precision and recall</p></li>
<li><p>provides a single measure that balances precision and recall</p></li>
</ul></li>
<li><p><strong>ROC-AUC</strong></p>
<ul>
<li><p>area under the Receiver Operating Characteristic curve</p></li>
<li><p>summarizes classifier performance across multiple decision thresholds</p></li>
</ul></li>
</ul>
<ul>
<li><p>applications can prioritize:</p>
<ul>
<li><p>minimizing false negatives</p></li>
<li><p>minimizing false positives</p></li>
</ul></li>
</ul>
<p><strong>Metric selection depends on which errors are most costly.</strong></p></td>
</tr>
<tr>
<td>Regression Metrics</td>
<td><p><strong>Regression models predict continuous values such as prices, demand, or quantities.</strong></p>
<p><strong>Root Mean Squared Error (RMSE)</strong></p>
<ul>
<li><p>square root of the average squared prediction error</p></li>
<li><p>penalizes large errors more strongly than small errors</p></li>
<li><p>useful when large prediction errors are especially costly</p></li>
</ul>
<p><strong>Mean Absolute Error (MAE)</strong></p>
<ul>
<li><p>average absolute difference between predicted and actual values</p></li>
<li><p>treats errors linearly</p></li>
<li><p>provides an intuitive measure of average error magnitude</p></li>
</ul>
<p><strong>R-squared</strong></p>
<ul>
<li><p>proportion of variance in the target variable explained by the model</p></li>
<li><p><span class="math inline"><em>R</em><em>s</em><em>q</em><em>u</em><em>a</em><em>r</em><em>e</em><em>d</em> = 1</span></p>
<ul>
<li><p>indicates a perfect fit</p></li>
</ul></li>
<li><p><span class="math inline"><em>R</em><em>s</em><em>q</em><em>u</em><em>a</em><em>r</em><em>e</em><em>d</em></span> near <span class="math inline">0</span></p>
<ul>
<li><p>indicates performance close to predicting the target mean</p></li>
</ul></li>
</ul>
<p><strong>RMSE and MAE are expressed in the same units as the target variable.</strong></p></td>
</tr>
<tr>
<td>Ranking Metrics</td>
<td><p><strong>Recommendation systems and search engines require metrics that evaluate the order in which results are presented.</strong></p>
<p><strong>Normalized Discounted Cumulative Gain (NDCG)</strong></p>
<ul>
<li><p>gives greater weight to relevant results appearing near the top of the ranking</p></li>
</ul>
<p><strong>Mean Average Precision (MAP)</strong></p>
<ul>
<li><p>averages precision values at relevant result positions across queries</p></li>
</ul>
<p><strong>Mean Reciprocal Rank (MRR)</strong></p>
<ul>
<li><p>focuses on the position of the first relevant result</p></li>
</ul>
<p><strong>Ranking metrics are especially useful when users need to encounter useful results quickly.</strong></p></td>
</tr>
<tr>
<td>Unsupervised Learning Metrics</td>
<td><p><strong>Unsupervised learning methods such as clustering also require evaluation.</strong></p>
<p><strong>Silhouette score</strong></p>
<ul>
<li><p>ranges from <span class="math inline">−1</span> to <span class="math inline">1</span></p></li>
<li><p>combines cluster cohesion and cluster separation</p></li>
<li><p>higher values:</p>
<ul>
<li><p>indicate better-defined clusters</p></li>
</ul></li>
<li><p>negative values:</p>
<ul>
<li><p>may indicate that observations are assigned to inappropriate clusters</p></li>
</ul></li>
</ul>
<p><strong>Cohesion</strong></p>
<ul>
<li><p>how close observations are within the same cluster</p></li>
</ul>
<p><strong>Separation</strong></p>
<ul>
<li><p>how far different clusters are from one another</p></li>
</ul>
<p><strong>Davies-Bouldin index</strong></p>
<ul>
<li><p>evaluates similarity between:</p>
<ul>
<li><p>clusters using within-cluster dispersion</p></li>
<li><p>between-cluster separation</p></li>
</ul></li>
<li><p>lower values:</p>
<ul>
<li><p>indicate better clustering</p></li>
</ul></li>
</ul>
<p><strong>Calinski-Harabasz index</strong></p>
<ul>
<li><p>ratio of between-cluster variance to within-cluster variance</p></li>
<li><p>higher values:</p>
<ul>
<li><p>indicate clusters that are more distinct and cohesive</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Metrics And Error Costs</td>
<td><p><strong>Choosing an evaluation metric is not only a technical decision; metrics should represent the practical cost of incorrect predictions.</strong></p>
<p><strong>Health care diagnosis:</strong></p>
<ul>
<li><p>false negatives:</p>
<ul>
<li><p>may be especially costly because a disease case could be missed</p></li>
</ul></li>
<li><p>recall or sensitivity:</p>
<ul>
<li><p>may therefore receive greater emphasis</p></li>
</ul></li>
</ul>
<p><strong>Spam filtering:</strong></p>
<ul>
<li><p>false positives:</p>
<ul>
<li><p>may be especially costly because</p></li>
</ul></li>
<li><p>legitimate messages:</p>
<ul>
<li><p>could be incorrectly removed</p></li>
</ul></li>
<li><p>precision:</p>
<ul>
<li><p>may therefore receive greater emphasis</p></li>
</ul></li>
</ul>
<p><strong>The appropriate metric depends on the application's objectives and the relative cost of each type of error.</strong></p></td>
</tr>
<tr>
<td>Avoiding Single-Metric Fixation</td>
<td><p><strong>Model evaluation should not rely on a single metric without considering its relationship to business or application objectives.</strong></p>
<ul>
<li><p>metrics should:</p>
<ul>
<li><p>align with relevant business KPIs</p></li>
<li><p>reflect the consequences of false positives and false negatives</p></li>
<li><p>support comparison between competing models</p></li>
<li><p>account for operational requirements</p></li>
<li><p>be interpreted alongside model complexity</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Fraud Detection Trade-Off</td>
<td><p><strong>Increasing recall causes the classifier to identify a larger proportion of fraudulent transactions.</strong></p>
<ul>
<li><p>high recall:</p>
<ul>
<li><p>fewer fraudulent transactions are missed</p></li>
<li><p>more legitimate transactions may be incorrectly flagged</p></li>
<li><p>precision may decrease</p></li>
<li><p>false positives may increase</p></li>
</ul></li>
</ul>
<p><strong>Increasing precision causes the classifier to flag transactions only when it has greater confidence that fraud is present.</strong></p>
<ul>
<li><p>high precision:</p>
<ul>
<li><p>fewer legitimate transactions are incorrectly flagged</p></li>
<li><p>more fraudulent transactions may be missed</p></li>
<li><p>recall may decrease</p></li>
<li><p>false negatives may increase</p></li>
</ul></li>
<li><p>false positive costs:</p>
<ul>
<li><p>customer inconvenience</p></li>
<li><p>blocked legitimate purchases</p></li>
<li><p>reduced user experience</p></li>
<li><p>potential lost revenue</p></li>
</ul></li>
<li><p>false negative costs:</p>
<ul>
<li><p>undetected fraudulent transactions</p></li>
<li><p>direct financial loss</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Decision Thresholds</td>
<td><p><strong>Classification models often produce scores or probabilities that must be converted into class predictions using a decision threshold.</strong></p>
<p><strong>Changing the threshold changes the balance between:</strong></p>
<ul>
<li><p>precision</p></li>
<li><p>recall</p></li>
<li><p>false positive rate</p></li>
<li><p>false negative rate</p></li>
</ul>
<p><img src="generated_media\DATA789_week02_notes\media\image4.png" style="width:4.75809in;height:3.18681in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p><strong>The appropriate threshold should reflect the real-world costs associated with each error type.</strong></p>
<ul>
<li><p>cost matrices and performance curves:</p>
<ul>
<li><p>can help identify an acceptable threshold</p></li>
</ul></li>
</ul>
<p><strong>Stakeholders such as finance teams and customer experience teams provide domain knowledge needed to determine the appropriate balance.</strong></p></td>
</tr>
<tr>
<td>ROC Curves</td>
<td><p><strong>ROC: Receiver Operating Characteristic.</strong></p>
<ul>
<li><p>evaluates binary classifier performance across possible decision thresholds</p></li>
</ul>
<p><strong>The curve compares:</strong></p>
<ul>
<li><p>true positive rate</p></li>
<li><p>false positive rate</p></li>
</ul>
<p><strong>A curve closer to the upper-left corner indicates that the model can achieve high recall while maintaining a low false positive rate.</strong></p></td>
</tr>
<tr>
<td>AUC</td>
<td><p><strong>AUC: Area Under the ROC Curve.</strong></p>
<ul>
<li><p>provides a single-number summary of ranking performance across thresholds.</p></li>
<li><p><span class="math inline"><em>A</em><em>U</em><em>C</em> = 1.0</span></p>
<ul>
<li><p>perfect discrimination between positive and negative examples</p></li>
</ul></li>
<li><p><span class="math inline"><em>A</em><em>U</em><em>C</em> = 0.5</span></p>
<ul>
<li><p>performance equivalent to random ranking</p></li>
</ul></li>
</ul>
<p><strong>AUC can also be interpreted as:</strong></p>
<ul>
<li><p>the probability that a randomly selected positive example receives a higher score than a randomly selected negative example</p></li>
</ul>
<p><strong>AUC should not be used in isolation.</strong></p>
<ul>
<li><p>model evaluation should also examine:</p>
<ul>
<li><p>threshold-specific behavior</p></li>
<li><p>application costs</p></li>
<li><p>operational constraints</p></li>
<li><p>model complexity</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Core Principle</td>
<td><p><strong>Evaluation metrics should be selected according to:</strong></p>
<ul>
<li><p>the machine learning task</p></li>
<li><p>the costs of different errors</p></li>
<li><p>the objectives of the broader system</p></li>
</ul>
<p><strong>Strong model evaluation requires balancing multiple metrics rather than optimizing a single value without considering its real-world consequences.</strong></p></td>
</tr>
<tr>
<td colspan="2">Rare Events and Adjusting Thresholds</td>
</tr>
<tr>
<td>Threshold Tuning, Operational Metrics, And Business Alignment</td>
<td><p><strong>Model evaluation in production requires more than choosing a standard accuracy metric.</strong></p>
<ul>
<li><p>rare events all affect whether a model is actually successful</p>
<ul>
<li><p>threshold selection</p></li>
<li><p>operational constraints</p></li>
<li><p>human feedback</p></li>
<li><p>business outcomes</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Rare Events And Precision-Recall Curves</td>
<td><p><strong>Rare-event problems include:</strong></p>
<ul>
<li><p>fraud detection</p></li>
<li><p>disease detection</p></li>
<li><p>network interruptions</p></li>
</ul>
<p><strong>ROC curves can be less informative when the positive class is rare.</strong></p>
<ul>
<li><p>performance may appear strong even when the model performs poorly on the minority class</p></li>
</ul>
<p><strong>Precision-recall curves.</strong></p>
<ul>
<li><p>often more informative for rare-event problems</p></li>
</ul>
<ul>
<li><p>plotted against recall as the classification threshold changes</p>
<ul>
<li><p>precision-recall curves emphasize performance on the positive class</p></li>
</ul></li>
<li><p>when positive cases are rare</p>
<ul>
<li><p>random or trivial models typically have very low precision</p></li>
<li><p>improvements over the baseline are therefore easier to observe</p></li>
</ul></li>
</ul>
<p><strong>The precision-recall curve can reveal where increasing recall begins to cause a substantial decline in precision.</strong></p>
<ul>
<li><p>this balance can be used to select a threshold that reflects application requirements</p>
<ul>
<li><p>example objective:</p>
<ul>
<li><p>maintain at least a specified level of precision while maximizing recall</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Threshold Tuning</td>
<td><p><strong>Binary classifiers commonly use</strong> <span class="math inline">0.5</span> <strong>as a default decision threshold.</strong></p>
<ul>
<li><p>this value should not automatically be treated as optimal</p></li>
</ul>
<p><strong>The threshold should be adjusted according to:</strong></p>
<ul>
<li><p>business objectives</p></li>
<li><p>error costs</p></li>
<li><p>precision requirements</p></li>
<li><p>recall requirements</p></li>
</ul>
<p><strong>When false negatives are especially costly:</strong></p>
<ul>
<li><p>lower the decision threshold</p></li>
<li><p>increase recall</p></li>
<li><p>capture more positive cases</p></li>
<li><p>accept more false positives</p></li>
</ul>
<p><strong>When false positives are especially costly:</strong></p>
<ul>
<li><p>raise the decision threshold</p></li>
<li><p>increase precision</p></li>
<li><p>reduce unnecessary alerts</p></li>
<li><p>accept more false negatives</p></li>
</ul>
<p><strong>Threshold tuning should be performed using:</strong></p>
<ul>
<li><p>validation data</p></li>
<li><p>cross-validation</p></li>
</ul>
<p><strong>Threshold tuning should not be performed directly on the training data because this can overfit the threshold to the training sample.</strong></p></td>
</tr>
<tr>
<td>Cost-Based Threshold Selection</td>
<td><p><strong>False positives and false negatives can sometimes be assigned explicit financial costs.</strong></p>
<ul>
<li><p>expected cost can be computed across possible thresholds</p></li>
<li><p>the selected threshold can then minimize the total expected cost</p></li>
</ul>
<p><strong>This approach directly connects classifier behavior to the economic consequences of prediction errors.</strong></p></td>
</tr>
<tr>
<td>Operational Metrics</td>
<td><p><strong>Production ML systems must also be evaluated using operational metrics.</strong></p>
<ul>
<li><p>important operational metrics include:</p>
<ul>
<li><p>latency</p></li>
<li><p>throughput</p></li>
<li><p>cost per prediction</p></li>
</ul></li>
</ul>
<p><strong>Latency.</strong></p>
<ul>
<li><p>measures how long a prediction takes</p>
<ul>
<li><p>example:</p>
<ul>
<li><p>required <span class="math inline"><em>r</em><em>e</em><em>s</em><em>p</em><em>o</em><em>n</em><em>s</em><em>e</em></span> <span class="math inline"><em>t</em><em>i</em><em>m</em><em>e</em> = 100 <em>m</em><em>i</em><em>l</em><em>l</em><em>i</em><em>s</em><em>e</em><em>c</em><em>o</em><em>n</em><em>d</em><em>s</em></span></p></li>
<li><p>actual <span class="math inline"><em>r</em><em>e</em><em>s</em><em>p</em><em>o</em><em>n</em><em>s</em><em>e</em></span> <span class="math inline"><em>t</em><em>i</em><em>m</em><em>e</em> = 500 <em>m</em><em>i</em><em>l</em><em>l</em><em>i</em><em>s</em><em>e</em><em>c</em><em>o</em><em>n</em><em>d</em><em>s</em></span></p></li>
</ul></li>
</ul></li>
<li><p>a model that exceeds the required latency may be unsuitable for deployment regardless of its predictive accuracy</p></li>
</ul>
<p><strong>Throughput.</strong></p>
<ul>
<li><p>measures how many predictions the system can process within a given period</p>
<ul>
<li><p>example:</p>
<ul>
<li><p><span class="math inline">1, 000 </span>predictions per second</p></li>
</ul></li>
</ul></li>
<li><p>the deployed system must support the expected volume of requests under realistic operating conditions</p></li>
</ul>
<p><strong>Cost Per Prediction.</strong></p>
<ul>
<li><p>measures the computational cost associated with generating each prediction</p></li>
</ul>
<p><strong>A highly accurate model may still be impractical if the required cloud or GPU resources make inference too expensive at scale.</strong></p></td>
</tr>
<tr>
<td>Operational Trade-Offs</td>
<td><p><strong>Operational metrics often trade off against model quality and against one another.</strong></p>
<ul>
<li><p>example:</p>
<ul>
<li><p>a larger neural network may improve predictive accuracy</p></li>
<li><p>inference may become slower</p></li>
<li><p>computational cost may increase</p></li>
</ul></li>
</ul>
<p><strong>Success criteria should therefore include both predictive and operational requirements.</strong></p></td>
</tr>
<tr>
<td>Multi-Metric Monitoring</td>
<td><p><strong>Production teams often monitor several metrics together.</strong></p>
<ul>
<li><p>a multi-metric dashboard may include:</p>
<ul>
<li><p>accuracy</p></li>
<li><p>precision</p></li>
<li><p>recall</p></li>
<li><p>latency</p></li>
<li><p>throughput</p></li>
<li><p>cost</p></li>
</ul></li>
</ul>
<p><strong>Monitoring these metrics together helps prevent optimization of one dimension at the expense of the overall system.</strong></p></td>
</tr>
<tr>
<td>Qualitative Success Metrics</td>
<td><p><strong>Not every important property of an ML system can be represented adequately by an automated numerical metric.</strong></p>
<ul>
<li><p>qualitative factors may include:</p>
<ul>
<li><p>user satisfaction</p></li>
<li><p>perceived relevance</p></li>
<li><p>ethical considerations</p></li>
<li><p>domain expert judgment</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Human Evaluation</td>
<td><p><strong>Human feedback can supplement automated metrics.</strong></p>
<ul>
<li><p>possible feedback sources include:</p>
<ul>
<li><p>structured user surveys</p></li>
<li><p>user ratings</p></li>
<li><p>domain expert review</p></li>
<li><p>internal moderators</p></li>
<li><p>sampled real-world interactions</p></li>
</ul></li>
</ul>
<p><strong>For some applications, human evaluation may provide the most meaningful measure of output quality.</strong></p></td>
</tr>
<tr>
<td>Human-In-The-Loop Evaluation</td>
<td><p><strong>Human-in-the-loop systems combine automated model evaluation with human judgment.</strong></p>
<ul>
<li><p>human feedback</p>
<ul>
<li><p>can be collected on a subset of interactions</p></li>
</ul></li>
<li><p>qualitative feedback</p>
<ul>
<li><p>can be compared with automated metrics over time</p></li>
</ul></li>
<li><p>large disagreements between the two may indicate an important problem</p>
<ul>
<li><p>example:</p>
<ul>
<li><p>model accuracy is high</p></li>
<li><p>user satisfaction is low</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>This divergence suggests that the automated metric may not fully capture the quality users actually experience.</strong></p></td>
</tr>
<tr>
<td>Closing The Loop</td>
<td><p><strong>Model improvements should ultimately produce measurable improvements in business outcomes.</strong></p>
<ul>
<li><p>a key evaluation question is:</p>
<ul>
<li><p>does improvement in the model metric produce improvement in the relevant business KPI?</p></li>
</ul></li>
<li><p>example:</p>
<ul>
<li><p>churn model recall increases from <span class="math inline">80%</span> to <span class="math inline">85%</span></p></li>
<li><p>customer churn does not decline</p></li>
</ul></li>
</ul>
<p><strong>Possible explanations include:</strong></p>
<ul>
<li><p>additional predictions may include more false positives</p></li>
<li><p>the model may identify customers who are unlikely to respond to intervention</p></li>
<li><p>the organization may lack an effective intervention strategy</p></li>
</ul>
<p><strong>Improved model performance does not automatically create business value.</strong></p>
<ul>
<li><p>business KPIs should therefore be monitored alongside model metrics</p></li>
</ul>
<p><strong>Production ML evaluation requires balancing:</strong></p>
<ul>
<li><p>predictive performance</p></li>
<li><p>threshold behavior</p></li>
<li><p>operational constraints</p></li>
<li><p>qualitative feedback</p></li>
<li><p>business outcomes.</p></li>
</ul>
<p><strong>A model improvement is meaningful only when it produces useful real-world results within acceptable technical and operational limits.</strong></p></td>
</tr>
<tr>
<td colspan="2">Data Validation</td>
</tr>
<tr>
<td>Data Validation, Drift, And Pipeline Monitoring</td>
<td><p><strong>Reliable ML metrics depend on reliable data.</strong></p>
<ul>
<li><p>production systems therefore require continuous validation of:</p>
<ul>
<li><p>incoming data</p></li>
<li><p>monitoring for drift</p></li>
<li><p>pipeline health checks</p></li>
<li><p>alerting</p></li>
<li><p>experiment tracking</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Data Validation At Scale</td>
<td><p><strong>Data validation checks whether incoming data matches the assumptions used during model development.</strong></p>
<ul>
<li><p>schema validation:</p>
<ul>
<li><p>confirm required fields are present</p></li>
<li><p>verify expected data types</p></li>
<li><p>detect upstream changes that could corrupt model inputs</p></li>
</ul></li>
<li><p>range and distribution checks:</p>
<ul>
<li><p>define plausible minimum and maximum values</p></li>
<li><p>compare incoming distributions with expected ranges</p></li>
<li><p>flag or filter values outside acceptable limits</p></li>
<li><p>examples:</p>
<ul>
<li><p>age must fall between 0 and 100</p></li>
<li><p>sensor readings should not be negative</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Missing Data</td>
<td><p><strong>Missing values require an explicit handling strategy.</strong></p>
<ul>
<li><p>possible approaches:</p>
<ul>
<li><p>drop affected rows</p></li>
<li><p>use default placeholders</p></li>
<li><p>apply data imputation techniques</p></li>
</ul></li>
</ul>
<p><strong>At minimum, the proportion of missing values should be monitored for every feature.</strong></p></td>
</tr>
<tr>
<td>Data Drift</td>
<td><p><strong>Data drift occurs when the distribution of model inputs changes after deployment.</strong></p>
<ul>
<li><p>examples:</p>
<ul>
<li><p>average user age changes</p></li>
<li><p>new slang appears in a text corpus</p></li>
<li><p>sensor values shift over time</p></li>
</ul></li>
</ul>
<p><strong>Data drift.</strong></p>
<ul>
<li><p>does not necessarily mean that the relationship between features and outcomes has changed</p></li>
<li><p>it can cause a model to encounter data that differs substantially from its training data</p></li>
<li><p>drift detection may compare:</p>
<ul>
<li><p>current production data</p></li>
<li><p>training data</p></li>
<li><p>historical production data</p></li>
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
<th>Population Stability Index</th>
<th><p>Population Stability Index, or PSI, can be used to compare the distribution of current input data with the training distribution.</p>
<ul>
<li><p>if drift exceeds an established threshold:</p>
<ul>
<li><p>generate an alert</p></li>
<li><p>investigate the affected features</p></li>
<li><p>consider retraining the model</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Concept Drift</td>
<td><p><strong>Concept drift occurs when the relationship between model inputs and the target outcome changes.</strong></p>
<p><img src="generated_media\DATA789_week02_notes\media\image5.jpeg" style="width:4.70422in;height:3.13615in" /></p>
<p>ChatGPT 5.6 Sol</p>
<ul>
<li><p>example:</p>
<ul>
<li><p>behavior that previously indicated customer churn</p>
<ul>
<li><p>no longer predicts churn</p></li>
<li><p>because market conditions have changed</p></li>
</ul></li>
</ul></li>
<li><p>possible causes:</p>
<ul>
<li><p>new competitors</p></li>
<li><p>competitors leaving the market</p></li>
<li><p>changes in customer behavior</p></li>
<li><p>changes in external conditions</p></li>
</ul></li>
</ul>
<p><strong>Concept drift can silently reduce model performance even when the incoming data still appears valid.</strong></p></td>
</tr>
<tr>
<td>Monitoring</td>
<td><p><strong>Concept drift can be detected by monitoring model performance over time.</strong></p>
<ul>
<li><p>possible indicators:</p>
<ul>
<li><p>accuracy declines</p></li>
<li><p>recall declines</p></li>
<li><p>precision declines</p></li>
<li><p>other production metrics fall below an established baseline</p></li>
</ul></li>
</ul>
<p><strong>Ground-truth labels.</strong></p>
<ul>
<li><p>may arrive after predictions are made</p></li>
<li><p>can be calculated over rolling windows once outcomes become available</p></li>
</ul></td>
</tr>
<tr>
<td>A/B Testing</td>
<td><p><strong>Can also help identify concept drift.</strong></p>
<ul>
<li><p>example:</p>
<ul>
<li><p>deploy a new model to a subset of traffic</p></li>
<li><p>compare its performance with the existing model</p></li>
</ul></li>
</ul>
<p><strong>Significantly better performance from the new model may indicate that the existing model has degraded.</strong></p></td>
</tr>
<tr>
<td>ML Pipeline Health</td>
<td><p><strong>A strong model is not useful if the surrounding pipeline fails to deliver reliable predictions.</strong></p>
<ul>
<li><p>production monitoring should therefore include the entire ML pipeline</p></li>
<li><p>job success and failure rates:</p>
<ul>
<li><p>monitor scheduled pipelines</p></li>
<li><p>detect failed ETL processes</p></li>
<li><p>identify incomplete data updates</p></li>
</ul></li>
<li><p>example:</p>
<ul>
<li><p>a nightly ETL job fails 10% of the time</p></li>
<li><p>approximately 10% of expected updates may be missing</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Component Runtime</td>
<td><p><strong>The duration of each pipeline component should be monitored.</strong></p>
<ul>
<li><p>example:</p>
<ul>
<li><p>stream preprocessing suddenly requires twice as much time</p></li>
</ul></li>
</ul>
<p><strong>An increase in processing time can create bottlenecks and threaten real-time prediction requirements.</strong></p></td>
</tr>
<tr>
<td>Resource Utilization</td>
<td><p><strong>Important resource metrics include:</strong></p>
<ul>
<li><p>CPU utilization</p></li>
<li><p>memory utilization</p></li>
<li><p>GPU utilization</p></li>
</ul>
<p><strong>High utilization may indicate:</strong></p>
<ul>
<li><p>insufficient capacity</p></li>
<li><p>need for scaling</p></li>
<li><p>inefficient code</p></li>
</ul>
<p><strong>Very low utilization may indicate:</strong></p>
<ul>
<li><p>overprovisioning</p></li>
<li><p>unnecessary infrastructure cost</p></li>
<li><p>underutilized test environments</p></li>
</ul></td>
</tr>
<tr>
<td>Alerts And Automated Responses</td>
<td><p><strong>Monitoring is useful only when detected problems trigger an appropriate response.</strong></p>
<ul>
<li><p>alert conditions may include:</p>
<ul>
<li><p>precision falls below 0.8</p></li>
<li><p>latency exceeds an operational threshold</p></li>
<li><p>daily cost exceeds a defined limit</p></li>
<li><p>pipeline jobs fail</p></li>
<li><p>resource utilization exceeds capacity</p></li>
</ul></li>
</ul>
<p><strong>Alerts can trigger:</strong></p>
<ul>
<li><p>human notifications</p></li>
<li><p>automated remediation</p></li>
<li><p>service scaling</p></li>
<li><p>service restarts</p></li>
<li><p>fallback model activation</p></li>
</ul>
<p><strong>Known and predictable failures should be automated when possible.</strong></p>
<ul>
<li><p>unknown failures or unsuccessful automated recovery should be escalated to humans</p></li>
</ul>
<p><strong>Automated remediation is an important MLOps capability because it reduces downtime and helps maintain consistent service quality.</strong></p></td>
</tr>
<tr>
<td>Experiment Tracking</td>
<td><p><strong>Model development may involve many training runs for:</strong></p>
<ul>
<li><p>hyperparameter tuning</p></li>
<li><p>feature engineering</p></li>
<li><p>model comparison</p></li>
<li><p>architecture changes</p></li>
</ul>
<p><strong>Experiment tracking records the configuration and results of each run.</strong></p>
<ul>
<li><p>commonly logged metrics include:</p>
<ul>
<li><p>accuracy</p></li>
<li><p>loss</p></li>
<li><p>precision</p></li>
<li><p>recall</p></li>
</ul></li>
</ul>
<p><strong>Runs can then be compared visually or programmatically.</strong></p></td>
</tr>
<tr>
<td>Additional Experiment Data</td>
<td><p><strong>Useful experiment metadata may include:</strong></p>
<ul>
<li><p>confusion matrices</p></li>
<li><p>feature importance</p></li>
<li><p>training time</p></li>
<li><p>hyperparameters</p></li>
<li><p>model configuration</p></li>
<li><p>software versions</p></li>
</ul>
<p><strong>Tracking more than the final evaluation metric makes model comparison, debugging, and reproducibility easier.</strong></p></td>
</tr>
<tr>
<td>Data And Model Versioning</td>
<td><p><strong>Production ML systems should maintain versions of:</strong></p>
<ul>
<li><p>datasets</p></li>
<li><p>models</p></li>
<li><p>code</p></li>
<li><p>training runs</p></li>
</ul>
<p><strong>Versioning makes it possible to trace exactly how a deployed model was produced.</strong></p>
<ul>
<li><p>example lineage:</p>
<ul>
<li><p>model version 5</p></li>
<li><p>training run 42</p></li>
<li><p>dataset version 3</p></li>
<li><p>code version ABC123</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Model Lineage</td>
<td><p><strong>Model lineage creates a traceable relationship between:</strong></p>
<ul>
<li><p>source data</p></li>
<li><p>training configuration</p></li>
<li><p>code</p></li>
<li><p>experiment</p></li>
<li><p>model artifact</p></li>
<li><p>deployment</p></li>
</ul>
<p><strong>This traceability supports:</strong></p>
<ul>
<li><p>reproducibility</p></li>
<li><p>debugging</p></li>
<li><p>governance</p></li>
<li><p>auditing</p></li>
</ul>
<p>ChatGPT 5.6 Sol</p>
<p><img src="generated_media\DATA789_week02_notes\media\image6.jpeg" style="width:4.73958in;height:3.55417in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p><strong>Months after deployment:</strong></p>
<ul>
<li><p>the team should still be able to determine how a specific model was trained</p></li>
</ul>
<p><strong>If a new model performs worse than a previous version, lineage also makes it easier to identify what changed.</strong></p></td>
</tr>
<tr>
<td>Unified Monitoring</td>
<td><p><strong>Technical and business metrics should be integrated into a shared monitoring environment.</strong></p>
<ul>
<li><p>a unified dashboard may include:</p>
<ul>
<li><p>model performance</p></li>
<li><p>data quality</p></li>
<li><p>drift metrics</p></li>
<li><p>pipeline health</p></li>
<li><p>latency</p></li>
<li><p>resource utilization</p></li>
<li><p>business KPIs</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA789_week02_notes\media\image7.jpeg" style="width:4.79653in;height:3.19792in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p><strong>Different stakeholders can examine the same underlying system from different perspectives.</strong></p>
<ul>
<li><p>executives may examine:</p>
<ul>
<li><p>sales</p></li>
<li><p>engagement</p></li>
<li><p>regional KPIs</p></li>
</ul></li>
<li><p>engineers may examine:</p>
<ul>
<li><p>API latency</p></li>
<li><p>resource utilization</p></li>
<li><p>pipeline failures</p></li>
</ul></li>
<li><p>data scientists may examine:</p>
<ul>
<li><p>feature distributions</p></li>
<li><p>data drift</p></li>
<li><p>model performance</p></li>
<li><p>prediction behavior</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Shared Source Of Truth</td>
<td><p><strong>A unified monitoring system allows business and technical teams to work from the same underlying information.</strong></p>
<ul>
<li><p>benefits include:</p>
<ul>
<li><p>faster diagnostics</p></li>
<li><p>earlier detection of problems</p></li>
<li><p>better collaboration</p></li>
<li><p>reduced dependence on delayed reports</p></li>
<li><p>consistent interpretation of system health</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Core Principle</td>
<td><p><strong>Production ML systems require continuous validation of:</strong></p>
<ul>
<li><p>data</p></li>
<li><p>models</p></li>
<li><p>pipelines</p></li>
<li><p>business outcomes</p></li>
</ul>
<p><strong>Effective monitoring combines:</strong></p>
<ul>
<li><p>data quality checks</p></li>
<li><p>drift detection</p></li>
<li><p>operational health</p></li>
<li><p>automated responses</p></li>
<li><p>experiment tracking</p></li>
<li><p>model lineage</p></li>
<li><p>shared dashboards</p></li>
</ul>
<p><strong>Problems can be:</strong></p>
<ul>
<li><p>detected</p></li>
<li><p>diagnosed</p></li>
<li><p>addressed quickly</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>
