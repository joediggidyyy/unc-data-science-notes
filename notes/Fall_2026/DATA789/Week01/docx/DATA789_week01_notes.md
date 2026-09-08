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
<td><p><strong>Prototype.</strong></p>
<ul>
<li><p>answers “can this approach work?”</p></li>
</ul>
<p><strong>Production.</strong></p>
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
</ul></td>
</tr>
<tr>
<td>ML Lifecycle</td>
<td><p><strong>These stages form a cycle rather than a one-time workflow.</strong></p>
<p><img src="generated_media\DATA789_week01_notes\media\image1.png" style="width:4.47569in;height:2.9375in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p>ChatGPT 5.6 Sol</p>
<p>problem farming</p>
<ul>
<li><p>define the prediction or decision problem, business objective, success metrics, and operational constraint</p></li>
</ul>
<ul>
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
<td><p><strong>Machine learning introduces challenges that are less prominent in traditional software development.</strong></p>
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
</ul></td>
</tr>
<tr>
<td>Core Components of a Production ML System</td>
<td><p><strong>A typical ML system contains several interconnected components.</strong></p>
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
</ul>
<p><strong>Together, these components turn a trained model into a continuously operating system.</strong></p></td>
</tr>
<tr>
<td>Why Data Engineering Matters</td>
<td><p><strong>Production ML depends heavily on the quality and availability of data.</strong></p>
<ul>
<li><p>poor, incomplete, biased, or corrupted data can undermine even an excellent model.</p></li>
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
</ul>
<p><strong>Designing ML systems requires anticipating these failure modes instead of treating data as a fixed input.</strong></p></td>
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
<td><p><strong>Production machine learning is a systems engineering problem, not just a modeling problem.</strong></p>
<ul>
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
<td><p><strong>A useful ML system must be designed not only around model quality, but also around:</strong></p>
<ul>
<li><p>reliability</p></li>
<li><p>security</p></li>
<li><p>maintainability</p></li>
<li><p>data quality</p></li>
<li><p>infrastructure</p></li>
<li><p>integration with the surrounding application</p></li>
</ul>
<ul>
<li><p>in practice:</p>
<ul>
<li><p>the model itself may represent only a small portion of the overall system</p></li>
</ul></li>
<li><p>much of the work lies in:</p>
<ul>
<li><p>supporting pipelines</p></li>
<li><p>features</p></li>
<li><p>testing</p></li>
<li><p><img src="generated_media\DATA789_week01_notes\media\image2.png" style="width:4.77778in;height:3.58333in" />infrastructure</p></li>
</ul></li>
</ul>
<p>ChatGPT 5.6 Sol</p></td>
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
</ul>
<p><strong>The goal is to connect ML theory with practical implementation using modern cloud systems.</strong></p></td>
</tr>
<tr>
<td>Real-World Systems Have Different Requirements</td>
<td><p><strong>System requirements depend on the application:</strong></p>
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
</ul>
<ul>
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
<tr>
<td>The Lifecycle as an Iterative Process</td>
<td><p><strong>Building an ML system begins with problem framing:</strong></p>
<ul>
<li><p>defining the decision or prediction task</p></li>
<li><p>establishing meaningful measures of success</p></li>
<li><p>identifying constraints before selecting a model</p></li>
</ul>
<ul>
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
</ul></td>
</tr>
<tr>
<td colspan="2">Machine Learning Systems</td>
</tr>
<tr>
<td>Testing ML Systems</td>
<td><p><strong>Quality assurance for machine learning is broader than conventional software testing.</strong></p>
<ul>
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
</ul>
<p><strong>Because both data and models can evolve after deployment, production testing may also involve techniques such as data validation and shadow deployments for evaluating new models before fully replacing the existing one.</strong></p></td>
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
<th>Functional Components of an ML System</th>
<th style="text-align: center;"><p><img src="generated_media\DATA789_week01_notes\media\image3.jpeg" style="width:4.88889in;height:3.66667in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p>A production system can be decomposed into several connected layers:</p>
<blockquote>
<p>Data ingestion.</p>
</blockquote>
<ul>
<li><p>brings raw information into the system</p></li>
<li><p>depending on the application, ingestion may be:</p>
<ul>
<li><p>streaming</p></li>
<li><p>batch-based</p></li>
<li><p>triggered on demand</p></li>
</ul></li>
<li><p>its responsibility is to ensure that the system continuously receives the data needed for downstream processing</p></li>
</ul>
<blockquote>
<p>Feature engineering and storage.</p>
</blockquote>
<ul>
<li><p>convert raw data into model-ready representations production systems</p></li>
<li><p>may precompute and store frequently used features,</p></li>
<li><p>sometimes through a dedicated feature store so that identical feature definitions can be used during both training and inference</p></li>
</ul>
<blockquote>
<p>Training pipelines.</p>
</blockquote>
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
</ul>
<blockquote>
<p>Model serving.</p>
</blockquote>
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
</ul>
<blockquote>
<p>Monitoring and feedback loops.</p>
</blockquote>
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
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Data Engineering as the Foundation</td>
<td><p><strong>A model is only as dependable as the data pipeline supporting it.</strong></p>
<ul>
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
<td><p><strong>An additional production concern is understanding where data came from and how it is allowed to be used.</strong></p>
<ul>
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
<td><p><em><strong>Several problems can undermine model performance even when the modeling code itself is unchanged.</strong></em></p>
<ul>
<li><p><em><strong>data poisoning</strong></em></p>
<ul>
<li><p><em>occurs when harmful or misleading observations enter the training or inference pipeline, potentially intentionally</em></p></li>
<li><p><em>systems that learn from open or user-generated data are particularly exposed to this class of risk</em></p></li>
</ul></li>
<li><p><em><strong>poor label quality</strong></em></p>
<ul>
<li><p><em>supervised models trained on incorrect or inconsistent labels are effectively learning from noise</em></p></li>
<li><p><em>label errors</em></p>
<ul>
<li><p><em>reduce attainable performance</em></p></li>
<li><p><em>introduce unwanted bias</em></p></li>
</ul></li>
</ul></li>
</ul>
<p><em><strong>These issues reinforce the need to treat the training dataset itself as an engineered and monitored component of the system.</strong></em></p></td>
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
<td><p><strong>Production ML can be understood as a set of <em>interdependent engineering components</em>.</strong></p>
<ul>
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
<td><p><strong>Research testing is often centered on evaluation against a holdout dataset and a small number of sanity checks.</strong></p>
<ul>
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
<li><p>a production ML system must balance predictive quality with:</p>
<ul>
<li><p>changing data</p></li>
<li><p>operational constraints</p></li>
<li><p>continuous validation</p></li>
</ul></li>
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
<td>Machine Learning Prototypes</td>
<td><p><strong>A machine learning prototype is an early-stage demonstration of an idea. It is often a proof-of-concept model built by a data scientist.</strong></p>
<ul>
<li><p>a prototype typically:</p>
<ul>
<li><p>runs on a laptop or a single virtual machine</p></li>
<li><p>uses a clean sample of the available data</p></li>
<li><p>tests whether an ML approach is feasible</p></li>
<li><p>is evaluated internally rather than used by customers</p></li>
<li><p>prioritizes rapid experimentation over reliability</p></li>
<li><p>may require manual adjustments</p></li>
<li><p>may have limited testing, security, and code organization</p></li>
</ul></li>
<li><p>occasional crashes or manual intervention are usually acceptable because the prototype’s purpose is to answer one question</p></li>
</ul></td>
</tr>
<tr>
<td>Machine Learning Products</td>
<td><p><strong>An ML product incorporates a promising model into a live service, system, or application feature.</strong></p>
<ul>
<li><p>the model is no longer isolated in a notebook. It becomes one component within a larger production pipeline</p></li>
<li><p>a production ML product may need to:</p>
<ul>
<li><p>receive data continuously</p></li>
<li><p>generate predictions for users or automated processes</p></li>
<li><p>operate reliably at all times</p></li>
<li><p>serve predictions through an application or API</p></li>
<li><p>handle increasing numbers of users and requests</p></li>
</ul></li>
<li><p>the central question changes from:</p>
<ul>
<li><p>can the model work?</p></li>
</ul></li>
<li><p>to:</p>
<ul>
<li><p>can the complete system serve users reliably, securely, and at scale?</p></li>
</ul></li>
</ul>
<ul>
<li><p>a successful prototype may represent only about 10% of the journey. The remaining work involves converting the prototype into a dependable production system</p></li>
</ul></td>
</tr>
<tr>
<td>Production Engineering Requirements</td>
<td><p><strong>Model management.</strong></p>
<ul>
<li><p>teams need procedures and tools to:</p>
<ul>
<li><p>deploy updated models</p></li>
<li><p>maintain model versions</p></li>
<li><p>track which model is currently active</p></li>
<li><p>roll back to an earlier version when necessary</p></li>
<li><p>reproduce previous training runs</p></li>
</ul></li>
</ul>
<p><strong>Monitoring.</strong></p>
<ul>
<li><p>a production system must continuously monitor:</p>
<ul>
<li><p>prediction quality</p></li>
<li><p>model accuracy and other performance metrics</p></li>
<li><p>data quality</p></li>
<li><p>data-distribution changes</p></li>
<li><p>system errors and failures</p></li>
<li><p>latency and resource use</p></li>
</ul></li>
<li><p>a model can continue operating normally from a technical perspective while its predictions gradually become less useful.</p></li>
</ul>
<p><strong>Security and privacy.</strong></p>
<ul>
<li><p>production ML systems must protect both models and data</p></li>
<li><p>important controls include:</p>
<ul>
<li><p>restricting access to the model</p></li>
<li><p>encrypting data in transit</p></li>
<li><p>encrypting stored data</p></li>
<li><p>protecting sensitive inputs and predictions</p></li>
<li><p>meeting relevant privacy and compliance requirements</p></li>
</ul></li>
<li><p>for medical ML services, privacy, security, and regulatory compliance are essential rather than optional</p></li>
</ul>
<p><strong>Scalability.</strong></p>
<ul>
<li><p>the system must handle increasing demand</p></li>
<li><p>for example, if an API receives ten times its normal traffic, the architecture should:</p>
<ul>
<li><p>scale automatically, or</p></li>
<li><p>support the rapid addition of computing resources</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>ML Systems Versus Traditional Software</td>
<td><p><strong>Probabilistic rather than strictly deterministic.</strong></p>
<ul>
<li><p>traditional software is usually deterministic:</p>
<ul>
<li><p>the same input produces the same output</p></li>
<li><p>a sorting algorithm should always return the same ordered list for the same input</p></li>
</ul></li>
<li><p>machine learning models are different:</p>
<ul>
<li><p>training randomness can produce slightly different models</p></li>
<li><p>outputs often represent probabilities or predictions</p></li>
<li><p>predictions are not guaranteed to be correct</p></li>
<li><p>errors can occur even when the software contains no code defect</p></li>
</ul></li>
<li><p>this uncertainty must be treated as a normal property of the system</p></li>
</ul></td>
</tr>
<tr>
<td>Testing Machine Learning Systems</td>
<td><ul>
<li><p>traditional software tests may assert:</p></li>
</ul>
<p><span class="math display"><em>f</em><em>o</em><em>r</em> <em>i</em><em>n</em><em>p</em><em>u</em><em>t</em> (<em>x</em>), <em>t</em><em>h</em><em>e</em> <em>o</em><em>u</em><em>t</em><em>p</em><em>u</em><em>t</em> <em>m</em><em>u</em><em>s</em><em>t</em> <em>b</em><em>e</em> (<em>y</em>)</span></p>
<ul>
<li><p>this is often inappropriate for ML models because valid predictions are statistical rather than exact</p></li>
</ul>
<p><strong>ML testing therefore evaluates performance across many examples.</strong></p>
<ul>
<li><p>a test might require that:</p>
<ul>
<li><p>accuracy remains above a defined threshold</p></li>
<li><p>false-positive and false-negative rates remain acceptable</p></li>
<li><p>performance satisfies requirements across important subgroups</p></li>
<li><p>confidence scores are appropriately calibrated</p></li>
<li><p>predictions remain stable under expected input variations</p></li>
</ul></li>
</ul>
<p><strong>The surrounding system should also manage uncertain predictions.</strong></p>
<ul>
<li><p>possible strategies include:</p>
<ul>
<li><p>applying decision thresholds</p></li>
<li><p>rejecting low-confidence predictions</p></li>
<li><p>sending uncertain cases for human review</p></li>
<li><p>using a fallback model or rule-based process</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Three Sources of Change</td>
<td><p><strong>Traditional software primarily changes when its code changes.</strong></p>
<ul>
<li><p>an ML system has three major sources of change:</p></li>
</ul>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th><strong>Component</strong></th>
<th><strong>Example of change</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Code</strong></td>
<td>A developer updates the prediction service</td>
</tr>
<tr>
<td><strong>Model</strong></td>
<td>The model is retrained or replaced</td>
</tr>
<tr>
<td><strong>Data</strong></td>
<td>New user behavior, slang, hashtags, or market conditions appear</td>
</tr>
</tbody>
</table>
<p><strong>Model behavior can therefore change even when no code has been modified.</strong></p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>a model that identifies trending topics may become less accurate when new language or hashtags emerge</p></li>
<li><p>the incoming data distribution has changed</p>
<ul>
<li><p>even though the application code remains identical</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Data Drift</td>
<td><p><strong>Data drift occurs when production data becomes different from the data used to train the model.</strong></p>
<ul>
<li><p>drift can:</p>
<ul>
<li><p>change model behavior</p></li>
<li><p>reduce prediction quality</p></li>
<li><p>introduce new patterns that the model has never encountered</p></li>
<li><p>silently degrade performance without causing a software error</p></li>
</ul></li>
</ul>
<p><strong>Because drift may not produce crashes or warning messages, it must be detected through continuous monitoring and evaluation.</strong></p></td>
</tr>
<tr>
<td>Continuous Training and Delivery</td>
<td><p><strong>MLOps, or machine learning operations, extends software-engineering practices to ML systems.</strong></p>
<ul>
<li><p>a central MLOps principle is:</p>
<ul>
<li><p>continuous training</p></li>
<li><p>continuous evaluation</p></li>
<li><p>continuous delivery</p></li>
</ul></li>
<li><p>this resembles continuous integration and continuous delivery, or CI/CD, in traditional software engineering</p></li>
</ul>
<p><strong>MLOps must also account for changing data and retrained models.</strong></p>
<ul>
<li><p>model updates should be carefully evaluated before deployment</p></li>
<li><p>a newly trained model is not automatically better simply because it uses newer data</p></li>
</ul></td>
</tr>
<tr>
<td>Versioning and Reproducibility</td>
<td><p><strong>Traditional software projects usually version their source code with tools such as Git.</strong></p>
<ul>
<li><p>ML systems must manage additional artifacts:</p>
<ul>
<li><p>source code</p></li>
<li><p>training data</p></li>
<li><p>validation and test data</p></li>
<li><p>data-processing procedures</p></li>
<li><p>model configurations and hyperparameters</p></li>
<li><p>training-run records</p></li>
<li><p>learned model parameters</p></li>
<li><p>evaluation results</p></li>
<li><p>deployed model versions</p></li>
</ul></li>
<li><p>if a production model begins behaving unexpectedly, the team should be able to determine:</p>
<ul>
<li><p>which code produced it</p></li>
<li><p>which dataset was used</p></li>
<li><p>how the data was processed</p></li>
<li><p>which parameters were selected</p></li>
<li><p>which training run created the model</p></li>
<li><p>which evaluation results justified its deployment</p></li>
</ul></li>
</ul>
<p><strong>Without dataset and model versioning, reliable investigation and reproduction may be impossible.</strong></p></td>
</tr>
<tr>
<td>Ongoing Validation</td>
<td><p><strong>ML deployment is not the end of model development.</strong></p>
<ul>
<li><p>a production model requires ongoing validation because:</p>
<ul>
<li><p>real-world data changes</p></li>
<li><p>model performance can decline silently</p></li>
<li><p>user behavior changes</p></li>
<li><p>retraining can alter predictions</p></li>
<li><p>new security, fairness, or compliance risks may emerge</p></li>
</ul></li>
</ul>
<p><strong>As a result, the boundary between development and maintenance is less distinct in ML than in traditional software.</strong></p></td>
</tr>
<tr>
<td colspan="2">Brainstorming Time</td>
</tr>
<tr>
<td>Model and Algorithm Selection</td>
<td><p><strong>Research models are often selected primarily for predictive performance.</strong></p>
<ul>
<li><p>a complex ensemble may achieve the highest accuracy but be too slow or expensive for production</p></li>
<li><p>production suitability requires questions such as:</p>
<ul>
<li><p>how quickly must the model return a prediction?</p></li>
<li><p>can it process real-time inputs individually?</p></li>
<li><p>does it support batch processing when needed?</p></li>
<li><p>how much memory and computing power does it require?</p></li>
<li><p>can the system afford its operating costs at scale?</p></li>
<li><p>does the accuracy improvement justify the added complexity?</p></li>
<li><p>should the model be compressed, simplified, or distilled?</p></li>
<li><p>can it be updated and maintained reliably?</p></li>
</ul></li>
<li><p>model selection must balance:</p>
<ul>
<li><p>accuracy</p></li>
<li><p>latency</p></li>
<li><p>computational cost</p></li>
<li><p>scalability</p></li>
<li><p>interpretability</p></li>
<li><p>maintainability</p></li>
<li><p>environmental sustainability</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Production Data Pipelines</td>
<td><p><strong>Research data is often collected and cleaned manually. This may be acceptable for a one-time experiment.</strong></p>
<ul>
<li><p>production systems require automated pipelines that continuously:</p>
<ul>
<li><p>collect new data</p></li>
<li><p>validate its structure and quality</p></li>
<li><p>clean and transform it</p></li>
<li><p>store it securely</p></li>
<li><p>provide it to the model</p></li>
<li><p>monitor it for unexpected changes</p></li>
<li><p>support model retraining</p></li>
</ul></li>
<li><p>important questions include:</p>
<ul>
<li><p>where does new data originate?</p></li>
<li><p>how frequently does it arrive?</p></li>
<li><p>how is invalid or missing data handled?</p></li>
<li><p>what happens if an upstream data source changes?</p></li>
<li><p>should the model be retrained daily, weekly, or conditionally?</p></li>
<li><p>how will training and production data be versioned?</p></li>
<li><p>how will sensitive data be protected?</p></li>
</ul></li>
</ul>
<p><strong>Retraining frequency should be based on model performance, data drift, cost, and business requirements—not an arbitrary schedule alone.</strong></p></td>
</tr>
<tr>
<td>Systems Design and Engineering</td>
<td><p><strong>Research data is often collected and cleaned manually. This may be acceptable for a one-time experiment.</strong></p>
<ul>
<li><p>production systems require automated pipelines that continuously:</p>
<ul>
<li><p>collect new data</p></li>
<li><p>validate its structure and quality</p></li>
<li><p>clean and transform it</p></li>
<li><p>store it securely</p></li>
<li><p>provide it to the model</p></li>
<li><p>monitor it for unexpected changes</p></li>
<li><p>support model retraining</p></li>
</ul></li>
<li><p>important questions include:</p>
<ul>
<li><p>where does new data originate?</p></li>
<li><p>how frequently does it arrive?</p></li>
<li><p>how is invalid or missing data handled?</p></li>
<li><p>what happens if an upstream data source changes?</p></li>
<li><p>should the model be retrained daily, weekly, or conditionally?</p></li>
<li><p>how will training and production data be versioned?</p></li>
<li><p>how will sensitive data be protected?</p></li>
</ul></li>
</ul>
<p><strong>Retraining frequency should be based on model performance, data drift, cost, and business requirements—not an arbitrary schedule alone.</strong></p></td>
</tr>
<tr>
<td>Logging and Monitoring</td>
<td><p><strong>Logs have little value unless teams know what to collect and how to use them.</strong></p>
<ul>
<li><p>production monitoring may cover:</p>
<ul>
<li><p>service availability</p></li>
<li><p>response latency</p></li>
<li><p>error rates</p></li>
<li><p>resource consumption</p></li>
<li><p>input-data quality</p></li>
<li><p>data drift</p></li>
<li><p>prediction distributions</p></li>
<li><p>model accuracy</p></li>
<li><p>output quality</p></li>
<li><p>security events</p></li>
<li><p>user engagement</p></li>
<li><p>business outcomes</p></li>
</ul></li>
</ul>
<p><strong>Monitoring should connect technical metrics with business indicators.</strong></p>
<ul>
<li><p>a system can remain technically available while producing increasingly poor results</p></li>
<li><p>alerts should be tied to defined thresholds and response procedures</p></li>
</ul></td>
</tr>
<tr>
<td>Teams and Operational Processes</td>
<td><p><strong>A research prototype may be built by one data scientist or a small research team.</strong></p>
<ul>
<li><p>a production ML product may require collaboration among:</p>
<ul>
<li><p>data scientists</p></li>
<li><p>data engineers</p></li>
<li><p>software engineers</p></li>
<li><p>MLOps or DevOps engineers</p></li>
<li><p>IT operations staff</p></li>
<li><p>security and privacy specialists</p></li>
<li><p>product managers</p></li>
<li><p>legal and compliance teams</p></li>
<li><p>business stakeholders</p></li>
</ul></li>
<li><p>the team needs formal procedures for:</p>
<ul>
<li><p>storing code in a version-controlled repository</p></li>
<li><p>reviewing changes</p></li>
<li><p>running automated tests</p></li>
<li><p>evaluating candidate models</p></li>
<li><p>approving deployments</p></li>
<li><p>releasing updates</p></li>
<li><p>monitoring production behavior</p></li>
<li><p>responding to incidents</p></li>
<li><p>rolling back failed releases</p></li>
</ul></li>
</ul>
<p><strong>A rollback plan should exist before a new model is deployed.</strong></p></td>
</tr>
<tr>
<td>Business and Compliance Requirements</td>
<td><p><strong>Production failures can cause financial loss, reputational damage, regulatory violations, or user harm.</strong></p>
<ul>
<li><p>teams should define measurable service-level objectives, such as:</p>
<ul>
<li><p>at least 99.5% service availability</p></li>
<li><p>responses within 200 milliseconds at the 95th percentile</p></li>
<li><p>error rates below a specified threshold</p></li>
<li><p>model-quality metrics above an acceptable minimum</p></li>
</ul></li>
<li><p>teams must also identify relevant requirements involving:</p>
<ul>
<li><p>privacy</p></li>
<li><p>security</p></li>
<li><p>copyright</p></li>
<li><p>data retention</p></li>
<li><p>fairness and discrimination</p></li>
<li><p>accessibility</p></li>
<li><p>explainability</p></li>
<li><p>human oversight</p></li>
<li><p>industry-specific regulation</p></li>
</ul></li>
</ul>
<p><strong>These requirements should be incorporated during system design rather than added after deployment.</strong></p></td>
</tr>
<tr>
<td>Major ML Failure Modes</td>
<td><p><strong>Stale Models and Data Drift.</strong></p>
<ul>
<li><p>data drift occurs when the production-data distribution changes from the distribution used during training</p></li>
<li><p>a model may gradually lose accuracy because:</p>
<ul>
<li><p>user preferences change</p></li>
<li><p>new categories or behaviors emerge</p></li>
<li><p>language and cultural patterns evolve</p></li>
<li><p>economic or social conditions change</p></li>
<li><p>relationships between inputs and outcomes shift</p></li>
</ul></li>
<li><p>for example:</p>
<ul>
<li><p>a music-generation model may not understand a new genre that was absent from its training data</p></li>
<li><p>it may also become less relevant as user preferences change</p></li>
</ul></li>
</ul>
<p><strong>Mitigations.</strong></p>
<ul>
<li><p>monitor input and prediction distributions</p></li>
<li><p>track model quality over time</p></li>
<li><p>retrain periodically using recent data</p></li>
<li><p>trigger retraining when drift exceeds a threshold</p></li>
<li><p>test updated models before deployment</p></li>
<li><p>maintain a rollback-ready previous version</p></li>
</ul>
<p><strong>Drift is expected in long-running ML systems.</strong></p>
<p><strong>It should be planned for, rather than treated as an exceptional event.</strong></p></td>
</tr>
<tr>
<td>Feedback Loops</td>
<td><p><strong>ML systems can influence the environment from which they later collect data.</strong></p>
<ul>
<li><p>a recommendation system may create the following cycle:</p>
<ul>
<li><p>the model recommends particular content</p></li>
<li><p>that content receives more exposure</p></li>
<li><p>increased exposure produces more clicks</p></li>
<li><p>the system interprets those clicks as evidence of popularity</p></li>
<li><p>the model recommends the content even more frequently</p></li>
</ul></li>
<li><p>this can suppress alternative content and reduce diversity</p></li>
<li><p>in a music system</p>
<ul>
<li><p>repeatedly promoting safe, mainstream tracks may cause users to select those tracks more often</p></li>
</ul></li>
<li><p>if those interactions are used for retraining</p>
<ul>
<li><p>the model may become increasingly biased toward the same style</p></li>
</ul></li>
</ul>
<p><strong>Mitigations.</strong></p>
<ul>
<li><p>preserve exploration in recommendations</p></li>
<li><p>measure exposure separately from user preference</p></li>
<li><p>maintain diversity and novelty constraints</p></li>
<li><p>audit training data for model-generated effects</p></li>
<li><p>avoid treating all interaction data as independent evidence</p></li>
<li><p>use controlled experiments to evaluate recommendation policies</p></li>
<li><p>include human review or editorial input where appropriate</p></li>
</ul></td>
</tr>
<tr>
<td>System-Integration Failures</td>
<td><p><strong>Failures frequently occur at the boundaries between system components.</strong></p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>a data pipeline stops running</p></li>
<li><p>an upstream service changes its data format</p></li>
<li><p>a required field is removed or renamed</p></li>
<li><p>authentication credentials expire</p></li>
<li><p>a storage service becomes unavailable</p></li>
<li><p>network delays cause timeouts</p></li>
<li><p>a model receives malformed or incomplete data</p></li>
</ul></li>
</ul>
<p><strong>Mitigations.</strong></p>
<ul>
<li><p>validate schemas and inputs</p></li>
<li><p>use explicit interface contracts</p></li>
<li><p>test integrations automatically</p></li>
<li><p>monitor pipeline freshness</p></li>
<li><p>detect missing or malformed data</p></li>
<li><p>add retries, timeouts, and fallback behavior</p></li>
<li><p>maintain incident-response procedures</p></li>
</ul></td>
</tr>
<tr>
<td>Security Breaches and Abuse</td>
<td><p><strong>Prompt injection.</strong></p>
<ul>
<li><p>attackers may deliberately provide inputs designed to:</p>
<ul>
<li><p>crash or delay the model</p></li>
<li><p>exhaust computational resources</p></li>
<li><p>reveal sensitive information</p></li>
<li><p>bypass safety controls</p></li>
<li><p>produce harmful content</p></li>
<li><p>generate copyrighted material</p></li>
<li><p>create legal or reputational problems</p></li>
</ul></li>
</ul>
<p><strong>Mitigations.</strong></p>
<ul>
<li><p>authenticate and authorize users</p></li>
<li><p>validate and sanitize inputs</p></li>
<li><p>apply rate limits and resource limits</p></li>
<li><p>monitor suspicious activity</p></li>
<li><p>test the system against adversarial inputs</p></li>
<li><p>filter or review high-risk outputs</p></li>
<li><p>protect training data and model artifacts</p></li>
<li><p>maintain security-incident procedures</p></li>
</ul>
<p><strong>Security must cover the complete pipeline, not only the model.</strong></p></td>
</tr>
<tr>
<td>Silent Degradation</td>
<td><p><strong>Silent degradation occurs when system quality declines without producing clear errors.</strong></p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>a music model might gradually generate more repetitive tracks because of a training problem or software defect</p></li>
<li><p>the service may remain available, but users may slowly disengage</p></li>
<li><p>traditional uptime monitoring may not detect this problem</p></li>
</ul></li>
</ul>
<p><strong>Mitigations.</strong></p>
<ul>
<li><p>monitor both model quality and business outcomes, including:</p>
<ul>
<li><p>output diversity</p></li>
<li><p>repetition rates</p></li>
<li><p>user engagement</p></li>
<li><p>session duration</p></li>
<li><p>retention</p></li>
<li><p>abandonment rates</p></li>
<li><p>user complaints</p></li>
<li><p>conversion or task-completion rates</p></li>
<li><p>long-term changes in usage</p></li>
</ul></li>
</ul>
<p><strong>Business key performance indicators, or KPIs, can reveal problems that technical health metrics miss.</strong></p></td>
</tr>
<tr>
<td>Production-Readiness Checklist</td>
<td><p><strong>Before deployment, teams should verify that:</strong></p>
<ul>
<li><p>the model meets accuracy and latency requirements</p></li>
<li><p>operating costs are acceptable</p></li>
<li><p>data pipelines are automated and monitored</p></li>
<li><p>training data, code, and models are versioned</p></li>
<li><p>deployment and rollback procedures are tested</p></li>
<li><p>logs support debugging and auditing</p></li>
<li><p>drift and output quality are monitored</p></li>
<li><p>security and privacy controls are active</p></li>
<li><p>compliance requirements are documented</p></li>
<li><p>failure modes have defined mitigations</p></li>
<li><p>technical metrics are connected to business KPIs</p></li>
<li><p>ownership is assigned for incidents and maintenance</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Reliability in an ML System</td>
</tr>
<tr>
<td>Geographic Redundancy</td>
<td><p><strong>Redundancy means maintaining multiple instances of a service so that one failure does not stop the entire system.</strong></p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>an organization could deploy its ML service in two geographic regions:</p>
<ul>
<li><p>Eastern United States</p></li>
<li><p>Western United States</p></li>
</ul></li>
<li><p>if the eastern cluster becomes unavailable:</p>
<ul>
<li><p>traffic can be redirected automatically to the western cluster</p></li>
<li><p>eastern users may experience slightly higher latency</p></li>
<li><p><strong>the</strong> <strong>service remains available</strong></p></li>
</ul></li>
</ul></li>
<li><p>the main objective is to eliminate infrastructure-level single points of failure</p></li>
</ul>
<p><strong>Active-active deployment.</strong></p>
<ul>
<li><p>in an active-active configuration:</p>
<ul>
<li><p>both environments operate simultaneously</p></li>
<li><p>both receive normal production traffic</p></li>
<li><p>the workload is distributed between them</p></li>
<li><p>one environment can absorb additional traffic if the other fails</p></li>
</ul></li>
<li><p>this arrangement provides efficient resource use and rapid failover</p></li>
<li><p>however, coordinating data and system state across regions can be complex</p></li>
</ul>
<p><strong>Active-passive deployment.</strong></p>
<ul>
<li><p>in an active-passive configuration:</p>
<ul>
<li><p>one environment handles normal production traffic</p></li>
<li><p>a second environment remains on standby</p></li>
<li><p>traffic moves to the standby environment after a failure</p></li>
</ul></li>
<li><p>this approach may be simpler to manage, but the passive environment must be tested regularly to ensure that it can take over successfully</p></li>
</ul></td>
</tr>
<tr>
<td>Automatic Retries with Backoff</td>
<td><p><strong>Many service failures are temporary.</strong></p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>brief network interruptions</p></li>
<li><p>short periods of server overload</p></li>
<li><p>temporary API failures</p></li>
<li><p>intermittent connection errors</p></li>
</ul></li>
</ul>
<ul>
<li><p>clients can retry failed requests automatically</p>
<ul>
<li><p>the client may be a:</p>
<ul>
<li><p>user-facing application</p></li>
<li><p>backend service</p></li>
<li><p>data pipeline</p></li>
</ul></li>
</ul></li>
<li><p>however, immediate and repeated retries can:</p>
<ul>
<li><p>increase system load</p></li>
<li><p>worsen the original failure</p></li>
</ul></li>
</ul>
<p><strong>Backoff strategy.</strong></p>
<ul>
<li><p>a backoff strategy increases the delay between retry attempts</p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>the first retry occurs after 1 second</p></li>
<li><p>the second occurs after 2 seconds</p></li>
<li><p>the third occurs after 4 seconds</p></li>
<li><p>later attempts continue with increasing delays</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>Jitter.</strong></p>
<ul>
<li><p>a small random delay, called <strong>jitter</strong>, can also be added</p>
<ul>
<li><p>prevents many clients from retrying at exactly the same time</p></li>
</ul></li>
</ul>
<p><strong>Retries with backoff can reduce user-visible errors, although some requests may take longer to complete.</strong></p>
<ul>
<li><p>retries should be:</p>
<ul>
<li><p>limited to transient failures</p></li>
<li><p>restricted to a maximum number of attempts</p></li>
<li><p>combined with timeouts</p></li>
<li><p>designed to avoid repeating unsafe operations</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Circuit Breakers</td>
<td><p><strong>A software circuit breaker protects a system from repeatedly calling a service that is already failing.</strong></p>
<ul>
<li><p>the pattern resembles an electrical circuit breaker:</p>
<ul>
<li><p>the system monitors an operation</p></li>
<li><p>failures or latency exceed a defined threshold</p></li>
<li><p>the circuit breaker opens</p></li>
<li><p>new calls fail immediately or use a fallback</p></li>
<li><p>after a waiting period, the system tests whether the service has recovered</p></li>
<li><p>normal calls resume if the test succeeds</p></li>
</ul></li>
<li><p>circuit breakers prevent repeated failures from consuming resources or spreading through dependent services</p>
<ul>
<li><p>they are particularly useful when an ML service depends on:</p>
<ul>
<li><p>external APIs</p></li>
<li><p>feature stores</p></li>
<li><p>databases</p></li>
<li><p>model-serving endpoints</p></li>
<li><p>remote storage systems</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Graceful Degradation</td>
<td><p><strong>Graceful degradation means providing reduced functionality when the complete service is unavailable.</strong></p>
<ul>
<li><p>the principle is:</p>
<ul>
<li><p>if the system cannot provide everything, it should provide something useful rather than nothing</p></li>
</ul></li>
<li><p>for example:</p>
<ul>
<li><p>if a personalized recommendation model fails, the application might:</p>
<ul>
<li><p>display generally popular items</p></li>
<li><p>use cached recommendations</p></li>
<li><p>apply a simpler rule-based system</p></li>
<li><p>return results from a smaller backup model</p></li>
<li><p>disable optional personalization while preserving core functions</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>Fallback behavior should be designed and tested before a failure occurs.</strong></p></td>
</tr>
<tr>
<td>Monitoring and Automated Recovery</td>
<td><p><strong>Reliable systems require continuous monitoring at several levels.</strong></p>
<ul>
<li><p>infrastructure metrics:</p>
<ul>
<li><p>CPU utilization</p></li>
<li><p>Memory consumption</p></li>
<li><p>GPU utilization</p></li>
<li><p>Disk and network activity</p></li>
<li><p>Queue length</p></li>
<li><p>Container or server health</p></li>
</ul></li>
<li><p>service metrics:</p>
<ul>
<li><p>availability</p></li>
<li><p>request volume</p></li>
<li><p>response time</p></li>
<li><p>error count</p></li>
<li><p>timeout rate</p></li>
<li><p>retry frequency</p></li>
<li><p>circuit-breaker state</p></li>
</ul></li>
<li><p>ML metrics:</p></li>
<li><p>prediction distributions.</p></li>
<li><p>confidence scores.</p></li>
<li><p>model accuracy.</p></li>
<li><p>input-data quality.</p></li>
<li><p>data drift.</p></li>
<li><p>output quality.</p></li>
<li><p>business metrics</p></li>
<li><p>user engagement.</p></li>
<li><p>task-completion rates.</p></li>
<li><p>conversion.</p></li>
<li><p>retention.</p></li>
<li><p>abandonment.</p></li>
<li><p>user complaints.</p></li>
</ul>
<p><strong>Monitoring should be connected to alerts and recovery procedures.</strong></p>
<ul>
<li><p>automated responses may include:</p>
<ul>
<li><p>restarting a failed service</p></li>
<li><p>replacing an unhealthy container</p></li>
<li><p>scaling computing resources</p></li>
<li><p>redirecting traffic</p></li>
<li><p>activating a fallback model</p></li>
<li><p>rolling back a recent deployment</p></li>
</ul></li>
</ul>
<p><strong>Automation reduces recovery time, but recovery procedures must be tested to ensure that they do not create additional failures.</strong></p></td>
</tr>
<tr>
<td>Blue/Green Deployment</td>
<td><p><strong>Blue/green deployment is a release strategy designed to reduce downtime and deployment risk.</strong></p>
<ul>
<li><p>two production environments are maintained:</p></li>
</ul>
<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Environment</strong></th>
<th style="text-align: center;"><strong>Role</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Blue</strong></td>
<td>Current trusted version</td>
</tr>
<tr>
<td><strong>Green</strong></td>
<td>New candidate version</td>
</tr>
</tbody>
</table>
<ul>
<li><p>the blue environment continues serving users while the green environment is deployed and evaluated</p></li>
</ul>
<p><strong>Deployment process.</strong></p>
<ul>
<li><p>keep the existing blue version active</p></li>
<li><p>deploy the new model or service to green</p></li>
<li><p>verify that green starts and passes basic health checks</p></li>
<li><p>send a small percentage of real traffic to green</p></li>
<li><p>monitor technical, model, and business metrics</p></li>
<li><p>increase green traffic gradually if performance remains acceptable</p></li>
<li><p>complete the cutover by directing all traffic to green</p></li>
<li><p>retain blue temporarily for rapid rollback</p></li>
</ul>
<p><strong>Real traffic can reveal problems that offline testing does not detect.</strong></p>
<ul>
<li><p>including:</p>
<ul>
<li><p>unexpected input patterns</p></li>
<li><p>increased latency</p></li>
<li><p>resource bottlenecks</p></li>
<li><p>integration failures</p></li>
<li><p>changes in prediction quality</p></li>
<li><p>changes in user behavior</p></li>
</ul></li>
</ul>
<p><strong>Cutover.</strong></p>
<ul>
<li><p>a cutover transfers production traffic from one environment to another</p>
<ul>
<li><p>the cutover should occur only after the candidate model satisfies predefined requirements, such as:</p>
<ul>
<li><p>acceptable error rates</p></li>
<li><p>acceptable response latency</p></li>
<li><p>stable resource use</p></li>
<li><p>required predictive performance</p></li>
<li><p>no significant regression in business metrics</p></li>
<li><p>no new security or compliance concerns</p></li>
<li><p>a cutover may happen gradually or all at once, depending on the system’s risk and architecture</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>Rollback.</strong></p>
<ul>
<li><p>if the green environment performs poorly</p>
<ul>
<li><p>traffic can be returned immediately to blue</p></li>
</ul></li>
<li><p>this provides an important advantage:</p>
<ul>
<li><p>the trusted system is still running</p></li>
<li><p>the previous version does not need to be redeployed</p></li>
<li><p>recovery can occur with little or no downtime</p></li>
</ul></li>
<li><p>rollback criteria should be defined before deployment</p>
<ul>
<li><p>teams should not wait until a failure occurs to decide what qualifies as unacceptable performance</p></li>
</ul></li>
</ul>
<p><strong>Blue/Green Deployment and Canary Releases.</strong></p>
<ul>
<li><p>blue/green deployment and canary releases are related but distinct</p></li>
</ul>
<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Strategy</th>
<th style="text-align: center;">Main idea</th>
</tr>
</thead>
<tbody>
<tr>
<td>blue/green</td>
<td>maintain separate old and new environments for safe switching and rollback</td>
</tr>
<tr>
<td>canary release</td>
<td>expose a small percentage of traffic to the new version before expanding deployment</td>
</tr>
</tbody>
</table>
<ul>
<li><p>the two strategies can be combined</p>
<ul>
<li><p>a green environment can initially receive only a small share of traffic, creating a canary-style evaluation within a blue/green architecture</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>End-to-End ML Perspective</td>
<td><p><strong>A trained model is only one part of a production ML system.</strong></p>
<ul>
<li><p>the complete lifecycle includes:</p>
<ul>
<li><p>defining the problem</p></li>
<li><p>formulating appropriate questions</p></li>
<li><p>identifying and collecting data</p></li>
<li><p>validating and preparing the data</p></li>
<li><p>training and evaluating models</p></li>
<li><p>integrating the selected model</p></li>
<li><p>deploying the service</p></li>
<li><p>monitoring technical and model behavior</p></li>
<li><p>collecting feedback</p></li>
<li><p>retraining, updating, or retiring the model</p></li>
</ul></li>
<li><p>a successful notebook experiment does not demonstrate that the complete system is production-ready</p>
<ul>
<li><p>production ML also requires:</p>
<ul>
<li><p>data-engineering practices</p></li>
<li><p>software-engineering practices</p></li>
<li><p>scalable infrastructure</p></li>
<li><p>security and privacy controls</p></li>
<li><p>reliable deployment procedures</p></li>
<li><p>appropriate user experiences</p></li>
<li><p>continuous operational management</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>ML Systems as Sociotechnical Products</td>
<td><p><strong>Machine learning systems combine technology with human and organizational factors.</strong></p>
<ul>
<li><p>they involve:</p>
<ul>
<li><p>users</p></li>
<li><p>developers</p></li>
<li><p>operators</p></li>
<li><p>business stakeholders</p></li>
<li><p>domain experts</p></li>
<li><p>affected communities</p></li>
<li><p>policies and regulations</p></li>
<li><p>technical infrastructure</p></li>
</ul></li>
</ul>
<p><strong>A model can perform well statistically while the overall product still fails.</strong></p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>users may not understand its predictions</p></li>
<li><p>operators may lack an incident-response process</p></li>
<li><p>the interface may encourage inappropriate reliance</p></li>
<li><p>training data may not represent affected populations</p></li>
<li><p>the model may conflict with legal or organizational requirements</p></li>
</ul></li>
</ul>
<p><strong>Reliability must therefore include both technical performance and responsible interaction with people and institutions.</strong></p></td>
</tr>
<tr>
<td>MLOps and Continuous Management</td>
<td><p><strong>Machine Learning Operations, or MLOps, applies engineering and operational practices across the ML lifecycle.</strong></p>
<ul>
<li><p>MLOps supports:</p>
<ul>
<li><p>reproducible training</p></li>
<li><p>automated testing</p></li>
<li><p>controlled deployment</p></li>
<li><p>model and data versioning</p></li>
<li><p>continuous monitoring</p></li>
<li><p>drift detection</p></li>
<li><p>incident response</p></li>
<li><p>safe rollback</p></li>
<li><p>ongoing model improvement</p></li>
</ul></li>
</ul>
<p><strong>Organizations should treat an ML product as an iterative, continuously managed service—not as a one-time deliverable.</strong></p></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>
