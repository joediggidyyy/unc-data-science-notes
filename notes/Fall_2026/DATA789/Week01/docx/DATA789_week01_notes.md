> Markdown version for convenient browsing. Original files:
> - PDF: [DATA789_week01_notes.pdf](../DATA789_week01_notes.pdf)
> - DOCX: [DATA789_week01_notes.docx](DATA789_week01_notes.docx)

---

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Intro to ML Systems &amp; Data Engineering</th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td>Overview</td>
<td colspan="3" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>explain the gap between machine learning (ML) models and products</p></li>
<li><p>contrast engineering and data over just algorithms</p></li>
<li><p>identify how to leverage cloud technologies for hands-on practice</p></li>
<li><p>recognize the specifications and requirement on real-world enterprise ML scenarios</p></li>
</ul></td>
</tr>
<tr>
<td>Course Requirements</td>
<td colspan="3" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>python 3.9+ running in a virtual environment</p></li>
<li><p>git + github</p></li>
<li><p>VS Code, PyCharm, or equivalent IDE</p></li>
<li><p>jupyter notebook</p></li>
<li><p>azure account</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Readings</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><p>Sato, D. (n.d.). <em>Continuous delivery for machine learning</em>. martinfowler.com. <a href="https://martinfowler.com/articles/cd4ml.html">https://martinfowler.com/articles/cd4ml.html</a></p>
<p>Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., Chaudhary, V., Young, M., Crespo, J., &amp; Dennison, D. (2015). Hidden technical debt in machine learning systems. <a href="https://papers.nips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf">https://papers.nips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf</a></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Async</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Intro to ML Systems and Data Engineering</td>
</tr>
<tr>
<td>Prototype vs Production</td>
<td><ul>
<li><p>prototype</p>
<ul>
<li><p>answers “can this approach work?”</p></li>
</ul></li>
<li><p>production</p>
<ul>
<li><p>must continuously</p>
<ul>
<li><p>process data</p></li>
<li><p>save predictions</p></li>
<li><p>handle failures</p></li>
<li><p>scale with demand</p></li>
<li><p>protect secrets</p></li>
<li><p>remain maintainable</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>ML Lifecycle</td>
<td><p>these stages form a cycle rather than a one-time workflow</p>
<ul>
<li><p>problem farming</p>
<ul>
<li><p>define the prediction or decision problem, business objective, success metrics, and operational constraint</p></li>
</ul></li>
<li><p>data collection and preparation</p>
<ul>
<li><p>acquire, clean, transform, validate, and continuously process data</p></li>
</ul></li>
<li><p>model development</p>
<ul>
<li><p>select algorithms, train models, tune parameters, and evaluate performance</p></li>
</ul></li>
<li><p>deployment</p>
<ul>
<li><p>make predictions available through APIs, applications, cloud services, or other systems</p></li>
</ul></li>
<li><p>monitoring and maintenance</p>
<ul>
<li><p>track model and system performance, detect changes in data, respond to failures, and retrain when necessary</p></li>
<li><p>monitoring may reveal new problems that require revisiting the data, model, or even the original problem definition</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>ML Systems vs. Traditional Software</td>
<td><ul>
<li><p>machine learning introduces challenges that are less prominent in traditional software development</p>
<ul>
<li><p>model outputs are often probabilistic rather than deterministic</p></li>
<li><p>system behavior can change when the underlying data changes</p></li>
<li><p>production systems must manage multiple evolving artifacts—including:</p>
<ul>
<li><p>code</p></li>
<li><p>datasets</p></li>
<li><p>features</p></li>
<li><p>trained models</p></li>
</ul></li>
<li><p>testing therefore includes not only software correctness, but also:</p>
<ul>
<li><p>statistical model performance</p></li>
<li><p>data validation</p></li>
<li><p>latency</p></li>
<li><p>throughput</p></li>
<li><p>bias</p></li>
<li><p>other operational measures</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Core Components of a Production ML System</td>
<td><ul>
<li><p>a typical ML system contains several interconnected components:</p>
<ul>
<li><p>data ingestion pipelines</p>
<ul>
<li><p>batch</p></li>
<li><p>streaming</p></li>
<li><p>on-demand data</p></li>
</ul></li>
<li><p>feature engineering and storage for transforming raw data into usable model inputs</p></li>
<li><p>training pipelines that make model training repeatable and reproducible</p></li>
<li><p>model serving infrastructure</p>
<ul>
<li><p>APIs</p></li>
<li><p>containers</p></li>
<li><p>managed cloud endpoints</p></li>
</ul></li>
<li><p>monitoring and feedback loops</p>
<ul>
<li><p>detect problems</p></li>
<li><p>collect new information for future training</p></li>
</ul></li>
</ul></li>
<li><p>Together, these components turn a trained model into a continuously operating system.</p></li>
</ul></td>
</tr>
<tr>
<td>Why Data Engineering Matters</td>
<td><ul>
<li><p>production ML depends heavily on the quality and availability of data</p></li>
<li><p>poor, incomplete, biased, or corrupted data can undermine even an excellent model</p></li>
<li><p>data engineering therefore focuses on:</p>
<ul>
<li><p>reliable ingestion</p></li>
<li><p>validation</p></li>
<li><p>storage</p></li>
<li><p>transformation</p></li>
<li><p>scheduling</p></li>
<li><p>integration across potentially very large datasets</p></li>
</ul></li>
<li><p>important data-related risks include:</p>
<ul>
<li><p>distribution shift</p></li>
<li><p>data poisoning</p></li>
<li><p>poor label quality</p></li>
<li><p>privacy / compliance constraints</p></li>
</ul></li>
<li><p><strong>d</strong>esigning ML systems requires anticipating these failure modes instead of treating data as a fixed input</p></li>
</ul></td>
</tr>
<tr>
<td>The Role of Cloud Infrastructure</td>
<td><ul>
<li><p>cloud platforms make many production ML workloads easier to operate by providing:</p>
<ul>
<li><p>elastic computing resources</p></li>
<li><p>managed services</p></li>
<li><p>geographic distribution</p></li>
<li><p>autoscaling</p></li>
<li><p>integrated data ecosystems</p></li>
</ul></li>
<li><p>these capabilities allow teams accomplish within a common infrastructure:</p>
<ul>
<li><p>training large models</p></li>
<li><p>serving predictions at scale</p></li>
<li><p>connect:</p>
<ul>
<li><p>storage</p></li>
<li><p>analytics</p></li>
<li><p>ML workflows</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Key Takeaway</td>
<td><ul>
<li><p><strong>production machine learning is a systems engineering problem, not just a modeling problem</strong></p></li>
<li><p>model accuracy remains important, but a useful ML product must also be:</p>
<ul>
<li><p>reliable</p></li>
<li><p>scalable</p></li>
<li><p>maintainable</p></li>
<li><p>secure</p></li>
<li><p>supported by high-quality data</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">ML Success Hinges on Hidden Infrastructure</td>
</tr>
<tr>
<td>Engineering Mindset and Real-World ML Systems</td>
<td><ul>
<li><p>useful ML system must be designed not only around model quality, but also around:</p>
<ul>
<li><p>reliability</p></li>
<li><p>security</p></li>
<li><p>maintainability</p></li>
<li><p>data quality</p></li>
<li><p>infrastructure</p></li>
<li><p>integration with the surrounding application</p></li>
</ul></li>
<li><p>in practice:</p>
<ul>
<li><p>the model itself may represent only a small portion of the overall system</p></li>
</ul></li>
<li><p>much of the work lies in:</p>
<ul>
<li><p>supporting pipelines</p></li>
<li><p>features</p></li>
<li><p>testing</p></li>
<li><p>infrastructure</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>An Engineering Mindset</td>
<td><ul>
<li><p>this course encourages thinking beyond experimentation and asking questions such as:</p>
<ul>
<li><p>will this work reliably in production?</p></li>
<li><p>how will it be maintained?</p></li>
<li><p>is it secure?</p></li>
<li><p>what happens when the data or operating environment changes?</p></li>
<li><p>how will users or other systems interact with the model?</p></li>
</ul></li>
<li><p>the goal is to connect ML theory with practical implementation using modern cloud <strong>systems rather than treating deployment as an afterthought</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Real-World Systems Have Different Requirements</td>
<td><ul>
<li><p>system requirements depend on the application:</p>
<ul>
<li><p>recommendation systems combine:</p>
<ul>
<li><p>behavioral data pipelines</p></li>
<li><p>low-latency serving</p></li>
<li><p>feedback loops that adapt as user preferences change</p></li>
</ul></li>
<li><p>fraud detection requires:</p>
<ul>
<li><p>real-time streaming data</p></li>
<li><p>rapidly computed features</p></li>
<li><p>very low prediction latency</p></li>
<li><p>extremely high availability</p></li>
</ul></li>
<li><p>predictive maintenance often relies on:</p>
<ul>
<li><p>large-scale sensor data</p></li>
<li><p>batch processing</p></li>
<li><p>integration with operational workflows such as maintenance scheduling</p></li>
</ul></li>
<li><p>computer vision systems may require:</p>
<ul>
<li><p>large-scale storage</p></li>
<li><p>GPU inference</p></li>
<li><p>high throughput</p></li>
<li><p>in sensitive domains such as medicine—strong requirements for:</p>
<ul>
<li><p>accuracy</p></li>
<li><p>explainability</p></li>
<li><p>security</p></li>
<li><p>compliance</p></li>
</ul></li>
</ul></li>
</ul></li>
<li><p>there is no single definition of a “good” ML system</p></li>
<li><p>different applications prioritize different qualities</p>
<ul>
<li><p>latency</p></li>
<li><p>scale</p></li>
<li><p>availability</p></li>
<li><p>interpretability</p></li>
<li><p>regulatory compliance</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th>The Lifecycle as an Iterative Process</th>
<th><ul>
<li><p>building an ML system begins with problem framing</p>
<ul>
<li><p>defining the decision or prediction task</p></li>
<li><p>establishing meaningful measures of success</p></li>
<li><p>identifying constraints before selecting a model</p></li>
</ul></li>
<li><p>data must then be:</p>
<ul>
<li><p>collected</p></li>
<li><p>cleaned</p></li>
<li><p>transformed</p></li>
<li><p>converted into useful features</p></li>
</ul></li>
<li><p>in production, these transformations should become repeatable pipelines so that new data is processed consistently rather than prepared manually each time</p></li>
<li><p>model development</p>
<ul>
<li><p>remains important</p></li>
<li><p>but it is only one stage of the larger workflow.</p></li>
</ul></li>
<li><p>once a model is considered suitable it must be:</p>
<ul>
<li><p>deployed</p></li>
<li><p>integrated into a service or application</p></li>
<li><p>scaled appropriately</p></li>
<li><p>continuously monitored and maintained</p></li>
</ul></li>
<li><p>production systems also require a plan for changing conditions</p>
<ul>
<li><p>new user behavior</p></li>
<li><p>shifts in the environment</p></li>
<li><p>declining model performance</p></li>
<li><p>harmful predictions</p></li>
<li><p>which may require:</p>
<ul>
<li><p>retraining</p></li>
<li><p>new data</p></li>
<li><p>rollback procedures</p></li>
<li><p>possibly reframing the original problem</p></li>
</ul></li>
</ul></li>
<li><p>for this reason, the ML lifecycle is best understood as:</p>
<ul>
<li><p>a continuous feedback loop</p></li>
<li><p>NOT a linear sequence with a final endpoint</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Machine Learning Systems</td>
</tr>
<tr>
<td>Testing ML Systems</td>
<td><ul>
<li><p>quality assurance for machine learning is broader than conventional software testing</p></li>
<li><p>in addition to functional correctness, ML systems must be evaluated for:</p>
<ul>
<li><p>system performance:</p>
<ul>
<li><p>latency</p></li>
<li><p>throughput</p></li>
<li><p>resource usage</p></li>
<li><p>availability</p></li>
</ul></li>
<li><p>model performance:</p>
<ul>
<li><p>accuracy</p></li>
<li><p>false-positive rates</p></li>
<li><p>other task-specific metrics</p></li>
</ul></li>
<li><p>data quality:</p>
<ul>
<li><p>malformed</p></li>
<li><p>missing</p></li>
<li><p>unexpected</p></li>
<li><p>or changing inputs</p></li>
</ul></li>
<li><p>bias and edge cases:</p>
<ul>
<li><p>behavior that may not appear in ordinary functional tests</p></li>
</ul></li>
</ul></li>
<li><p>because both data and models can evolve after deployment, production testing may also involve techniques such as data validation and shadow deployments for evaluating new models before fully replacing the existing one</p></li>
</ul></td>
</tr>
<tr>
<td>Functional Components of an ML System</td>
<td><ul>
<li><p>a production system can be decomposed into several connected layers:</p>
<ul>
<li><p><strong>data ingestion</strong></p>
<ul>
<li><p>brings raw information into the system</p></li>
<li><p>depending on the application, ingestion may be:</p>
<ul>
<li><p>streaming</p></li>
<li><p>batch-based</p></li>
<li><p>triggered on demand</p></li>
</ul></li>
<li><p>its responsibility is to ensure that the system continuously receives the data needed for downstream processing</p></li>
</ul></li>
<li><p><strong>feature engineering and storage</strong></p>
<ul>
<li><p>convert raw data into model-ready representations production systems</p></li>
<li><p>may precompute and store frequently used features,</p></li>
<li><p>sometimes through a dedicated feature store so that identical feature definitions can be used during both training and inference</p></li>
</ul></li>
<li><p><strong>training pipelines</strong></p>
<ul>
<li><p>turn model development into an automated, repeatable process</p></li>
<li><p>they can include:</p>
<ul>
<li><p>dataset splitting</p></li>
<li><p>training</p></li>
<li><p>hyperparameter tuning</p></li>
<li><p>validation</p></li>
<li><p>eventually, continuous retraining as new data becomes available</p></li>
</ul></li>
</ul></li>
<li><p><strong>model serving</strong></p>
<ul>
<li><p>exposes the trained model to other applications</p>
<ul>
<li><p>commonly through an API</p></li>
</ul></li>
<li><p>serving infrastructure must be selected according to operational requirements such as:</p>
<ul>
<li><p>latency</p></li>
<li><p>scale</p></li>
<li><p>availability</p></li>
</ul></li>
</ul></li>
<li><p><strong>Monitoring and feedback loops</strong></p>
<ul>
<li><p>connect production behavior back to the development process</p></li>
<li><p>monitoring</p>
<ul>
<li><p>tracks both infrastructure health and changes in model or data behavior</p></li>
</ul></li>
<li><p>feedback</p>
<ul>
<li><p>supplies eventual outcomes or user responses that can support evaluation and retraining</p></li>
</ul></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Data Engineering as the Foundation</td>
<td><ul>
<li><p>a model is only as dependable as the data pipeline supporting it</p></li>
<li><p>production data engineering therefore includes</p>
<ul>
<li><p>validation rules</p></li>
<li><p>missing-data handling</p></li>
<li><p>anomaly detection</p></li>
<li><p>workflow scheduling</p></li>
<li><p>mechanisms for enforcing the quality requirements expected by ML models</p></li>
</ul></li>
<li><p>the model must also operate at realistic scale</p>
<ul>
<li><p>enterprise systems may process millions of events or hundreds of millions of records requiring</p>
<ul>
<li><p>distributed processing frameworks and cloud infrastructure</p></li>
<li><p>not achievable with single-machine workflows</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Data Lineage and Governance</td>
<td><ul>
<li><p>an additional production concern is understanding where data came from and how it is allowed to be used</p></li>
<li><p>data lineage</p>
<ul>
<li><p>records the origin and transformation history of data, making it easier to trace downstream problems back to their source</p></li>
</ul></li>
<li><p>data governance</p>
<ul>
<li><p>defines and enforces:</p>
<ul>
<li><p>rules around access</p></li>
<li><p>privacy</p></li>
<li><p>compliance</p></li>
<li><p>anonymization</p></li>
<li><p>appropriate use</p></li>
</ul></li>
</ul></li>
<li><p>these controls become particularly important when ML systems use sensitive or regulated information</p></li>
</ul></td>
</tr>
<tr>
<td>Data-Specific Failure Modes</td>
<td><ul>
<li><p>several problems can undermine model performance even when the modeling code itself is unchanged</p></li>
<li><p><strong>data poisoning</strong></p>
<ul>
<li><p>occurs when harmful or misleading observations enter the training or inference pipeline, potentially intentionally</p></li>
<li><p>systems that learn from open or user-generated data are particularly exposed to this class of risk</p></li>
</ul></li>
<li><p><strong>poor label quality</strong></p>
<ul>
<li><p>supervised models trained on incorrect or inconsistent labels are effectively learning from noise</p></li>
<li><p>label errors</p>
<ul>
<li><p>reduce attainable performance</p></li>
<li><p>introduce unwanted bias</p></li>
</ul></li>
</ul></li>
<li><p>these issues reinforce the need to treat the training dataset itself as an engineered and monitored component of the system</p></li>
</ul></td>
</tr>
<tr>
<td>Cloud Infrastructure</td>
<td><ul>
<li><p>benefits of cloud infrastructure:</p>
<ul>
<li><p>elastic compute for scaling resources on demand</p></li>
<li><p>managed ML services that reduce infrastructure overhead</p></li>
<li><p>global reach through geographically distributed infrastructure</p></li>
<li><p>unified data ecosystems that connect</p>
<ul>
<li><p>storage</p></li>
<li><p>warehouses</p></li>
<li><p>lakehouse architectures</p></li>
<li><p>analytics</p></li>
<li><p>ML tools</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Key Takeaways</td>
<td><ul>
<li><p>production ML can be understood as a set of <strong>interdependent engineering components</strong></p></li>
<li><p>reliability depends on how well data ingestion, feature computation, training, serving, monitoring, governance, and infrastructure work together—not on the model in isolation</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Requirements for Production ML</td>
</tr>
<tr>
<td>Static Data vs. Dynamic Data</td>
<td><ul>
<li><p>in research</p>
<ul>
<li><p>models are commonly developed on a fixed dataset with known boundaries</p></li>
<li><p>after the train/test split is created, the data environment is relatively stable</p></li>
</ul></li>
<li><p>production systems operate differently</p>
<ul>
<li><p>mew observations continue to arrive</p></li>
<li><p>user behavior changes</p></li>
<li><p>seasonality appears</p></li>
<li><p>the underlying data distribution may drift</p>
<ul>
<li><p>as a result, production ML requires plans for:</p>
<ul>
<li><p>periodic or continuous retraining</p></li>
<li><p>robust data ingestion pipelines</p></li>
<li><p>validation and cleaning of incoming data</p></li>
<li><p>handling missing or unavailable data sources</p></li>
<li><p>graceful degradation or fallback behavior when dependencies fail</p></li>
</ul></li>
</ul></li>
<li><p>the key distinction</p>
<ul>
<li><p>research</p>
<ul>
<li><p>often treats data as a snapshot</p></li>
</ul></li>
<li><p>production</p>
<ul>
<li><p>treats data as an ongoing stream that can change over time</p></li>
</ul></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Model Metrics Are Not Enough</td>
<td><ul>
<li><p>research workflows often judge models primarily using predictive metrics such as:</p>
<ul>
<li><p>accuracy</p></li>
<li><p>F1 score</p></li>
<li><p>RMSE</p></li>
<li><p>other task-specific evaluation measures</p></li>
</ul></li>
<li><p>production systems</p>
<ul>
<li><p>still care about these metrics</p></li>
<li><p>they must balance them against operational requirements</p></li>
</ul></li>
<li><p>important production criteria include:</p>
<ul>
<li><p>latency</p>
<ul>
<li><p>how quickly predictions are returned</p></li>
</ul></li>
<li><p>throughput</p>
<ul>
<li><p>how many requests the system can process</p></li>
</ul></li>
<li><p>scalability</p>
<ul>
<li><p>whether the system can handle increasing demand</p></li>
</ul></li>
<li><p>resource usage and cost</p></li>
<li><p>uptime and reliability</p></li>
</ul></li>
<li><p>a model with excellent offline accuracy may still be unsuitable if it is</p>
<ul>
<li><p>too slow</p></li>
<li><p>too expensive</p></li>
<li><p>or unreliable in deployment</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Continuous Testing and Quality Assurance</td>
<td><ul>
<li><p>research testing is often centered on evaluation against a holdout dataset and a small number of sanity checks</p></li>
<li><p>Production ML requires a broader and continuous testing process</p>
<ul>
<li><p>pre-production testing</p></li>
<li><p>canary or shadow deployments</p></li>
<li><p>continuous monitoring and alerting</p></li>
<li><p>security testing</p></li>
<li><p>ongoing checks of data and model behavior</p></li>
</ul></li>
<li><p>testing therefore continues after deployment rather than ending once a model passes offline evaluation</p></li>
</ul></td>
</tr>
<tr>
<td>Key Takeaways</td>
<td><ul>
<li><p>a production ML system must balance predictive quality with:</p></li>
<li><p>changing data</p></li>
<li><p>operational constraints</p></li>
<li><p>continuous validation</p></li>
<li><p>the important shift is from optimizing a model once on static data to operating a system that remains:</p>
<ul>
<li><p>accurate</p></li>
<li><p>responsive</p></li>
<li><p>reliable</p></li>
<li><p>testable as conditions change</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">ML Prototype, ML Product and ML System</td>
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
<tr>
<td></td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>
