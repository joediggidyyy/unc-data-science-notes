> Markdown version for convenient browsing. Original files:
> - PDF: [DATA790_week01_notes.pdf](docx/DATA790_week01_notes.pdf)
> - DOCX: [DATA790_week01_notes.docx](DATA790_week01_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr>
<th colspan="4">Foundations of LLMs &amp; Cloud Computing Basics</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Overview</td>
<td colspan="3" style="text-align: right;"><em>14 Aug 2026</em></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>establish foundation in LLM architecture</p>
<ol type="1">
<li><p>describe the key differences between major LLM providers</p>
<ol type="i">
<li><p>OpenAI</p></li>
<li><p>Anthropic</p></li>
<li><p>Google</p></li>
</ol></li>
</ol></li>
<li><p>set up and configure cloud development environments for AI development</p>
<ol type="1">
<li><p>make your first API calls through the UNC AI Gateway</p>
<ol type="i">
<li><p>Azure</p></li>
<li><p>OpenAI</p></li>
</ol></li>
</ol></li>
<li><p>reinforce understanding of transformers</p>
<ol type="1">
<li><p>explain the self-attention mechanism and its role in transformer architecture</p></li>
</ol></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Required Readings</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>Vaswani, A., et al. (2017). "Attention Is All You Need."</p>
<ul>
<li><p>the foundational transformer paper</p></li>
<li><p>focus on Sections 1-3 and the attention mechanism diagrams</p></li>
<li><p><a href="https://arxiv.org/abs/1706.03762">https://arxiv.org/abs/1706.03762</a></p></li>
</ul></li>
<li><p>Brown, T. B., et al. (2020). "Language Models are Few-Shot Learners."</p>
<ul>
<li><p>the GPT-3 paper that introduced modern prompting</p></li>
<li><p>read the introduction and emergent abilities section</p></li>
<li><p><a href="https://arxiv.org/abs/2005.14165">https://arxiv.org/abs/2005.14165</a></p></li>
</ul></li>
<li><p>OpenAI (2023). "GPT-4 Technical Report."</p>
<ul>
<li><p>understand current capabilities and limitations</p></li>
<li><p><a href="https://arxiv.org/abs/2303.08774">https://arxiv.org/abs/2303.08774</a></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Required Videos</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>Understanding Transformer Architecture (4 min)</p></li>
<li><p>Understanding Attention Mechanisms (4 min)</p></li>
<li><p>Introduction to Cloud Platforms (3 min)</p></li>
<li><p>Overview of Current Model Landscape (5 min)</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Supplementary Videos</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>Andrej Karpathy - "Let's build GPT: from scratch" (2 hours)</p>
<ul>
<li><p>Highly recommended for deep understanding</p></li>
<li><p><a href="https://www.youtube.com/watch?v=kCc8FmEb1nY">https://www.youtube.com/watch?v=kCc8FmEb1nY</a></p></li>
</ul></li>
<li><p>MIT 6.S191 - "Transformers and Attention" (58 minutes) <em>*404</em></p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Cloud Environment Setup</td>
</tr>
<tr>
<td>Environment Setup</td>
<td colspan="4"><ul>
<li><p>get your UNC AI Gateway API key</p>
<ul>
<li><p>sent via Canvas Inbox</p></li>
</ul></li>
<li><p>confirm access to the course models</p>
<ul>
<li><p>gpt-4.1-mini</p></li>
<li><p>gpt-5.6-sol</p></li>
<li><p>text-embedding-3-small</p></li>
</ul></li>
<li><p>configure API keys and environment variables</p></li>
</ul></td>
</tr>
<tr>
<td>First API Calls</td>
<td colspan="4"><ul>
<li><p>complete the provided Jupyter notebook</p></li>
<li><p>implement token counting and cost estimation</p></li>
<li><p>deploy basic LLM with security checks</p></li>
</ul></td>
</tr>
<tr>
<td>Documentation</td>
<td colspan="4"><ul>
<li><p>document your setup process</p></li>
<li><p>note any challenges encountered</p></li>
</ul></td>
</tr>
<tr>
<td colspan="5">Live Session Preparation</td>
</tr>
<tr>
<td>Planned Discussion Items</td>
<td colspan="4"><ul>
<li><p>transformer architecture</p></li>
<li><p>challenges from the lab</p></li>
<li><p>bring questions about the readings</p></li>
</ul></td>
</tr>
<tr>
<td>Key Concepts</td>
<td colspan="4"><ul>
<li><p>self-attention</p>
<ul>
<li><p>how models attend to different parts of the input simultaneously</p></li>
</ul></li>
<li><p>tokenization</p>
<ul>
<li><p>how text is converted to numerical representations</p></li>
</ul></li>
<li><p>context window</p>
<ul>
<li><p>maximum input size models can process</p></li>
</ul></li>
<li><p>temperature</p>
<ul>
<li><p>controls randomness in generation</p></li>
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
<col style="width: 25%" />
<col style="width: 27%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th colspan="4">Async</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4">Understanding Transformer Architecture</td>
</tr>
<tr>
<td>Encoder-Decoder Structure</td>
<td colspan="3"><ul>
<li><p>Encoder</p>
<ul>
<li><p>a stack of identical layers</p></li>
<li><p>reads input sequence and generates a rich contextual representation</p>
<ul>
<li><p>a set of context vectors</p></li>
</ul></li>
</ul></li>
<li><p>Decoder</p>
<ul>
<li><p>also a stack of layers</p></li>
<li><p>takes the encoders output</p></li>
<li><p>generates output sequence one token at a time</p></li>
<li><p>looks at what is already generated to inform the next word</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA790_week01_notes\media\image1.png" style="width:4.68446in;height:3.52083in" /></p>
<p>ChatGPT 5.6 Sol</p></td>
</tr>
<tr>
<td>Self-Attention Mechanism</td>
<td colspan="3"><ul>
<li><p>allows the model to look at all other words in the input sequence</p></li>
<li><p>provides added context for the current word</p></li>
<li><p>weighs the importance of all other words relative to a specific word</p></li>
<li><p>allows the model to capture complex, long-range dependencies and context</p></li>
</ul>
<p><img src="generated_media\DATA790_week01_notes\media\image2.png" style="width:4.78125in;height:3.5936in" /></p>
<p>ChatGPT 5.6 Sol</p></td>
</tr>
<tr>
<td colspan="4">Understanding Attention Mechanisms</td>
</tr>
<tr>
<td>Query, Key, Value Vectors</td>
<td colspan="3"><ul>
<li><p>Query (Q)</p>
<ul>
<li><p>the current word’s question</p></li>
<li><p>“what am I looking for?”</p></li>
</ul></li>
<li><p>Key (K)</p>
<ul>
<li><p>the “label” of all words in the sequence</p></li>
<li><p>“what information do I hold?”</p></li>
</ul></li>
<li><p>Value (V)</p>
<ul>
<li><p>the actual content / meaning of the words</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Score Calculation</td>
<td colspan="3"><ul>
<li><p>the mechanism calculates the score by matching the Q of each word with the K of another</p></li>
<li><p>similar to search engine matching your query (Q) string to a video title (K) to return a video (V)</p></li>
</ul></td>
</tr>
<tr>
<td>Scaled Dot-Product Attention</td>
<td colspan="3"><ul>
<li><p>score</p>
<ul>
<li><p>compute the dot product of the Query with all Keys</p></li>
</ul></li>
<li><p>scale</p>
<ul>
<li><p>divide scores by the square root of the key’s dimension (<span class="math inline"><em>d</em><sub><em>k</em></sub></span>) to stabilize gradients</p></li>
</ul></li>
<li><p>softmax</p>
<ul>
<li><p>normalizes all weights to sum to 1</p></li>
</ul></li>
<li><p>output</p>
<ul>
<li><p>multiply the weights by the Value vectors and sum</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA790_week01_notes\media\image3.png" style="width:4.87014in;height:3.65625in" /></p>
<p>ChatGPT 5.6 Sol</p></td>
</tr>
<tr>
<td colspan="4">Introduction to Cloud Platforms</td>
</tr>
<tr>
<td>IaaS</td>
<td colspan="3"><p><strong>Infrastructure</strong></p>
<ul>
<li><p>delivers on-demand infrastructure</p>
<ul>
<li><p>compute</p></li>
<li><p>storage</p></li>
<li><p>networking</p></li>
</ul></li>
<li><p>user manages</p>
<ul>
<li><p>OS</p></li>
<li><p>middleware</p></li>
<li><p>applications</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>PaaS</td>
<td colspan="3"><p><strong>Platform</strong></p>
<ul>
<li><p>provides development platform</p></li>
<li><p>the cloud provider manages</p>
<ul>
<li><p>underlying hardware</p></li>
<li><p>software resources</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>SaaS</td>
<td colspan="3"><p><strong>Software</strong></p>
<ul>
<li><p>delivers a complete, cloud-based application</p></li>
<li><p>provider manages everything</p></li>
</ul></td>
</tr>
<tr>
<td>Major Cloud Providers</td>
<td colspan="3"><ul>
<li><p>Amazon Web Services (<strong>AWS</strong>)</p>
<ul>
<li><p>the market leader</p></li>
<li><p>extensive and mature catalog of services</p></li>
</ul></li>
<li><p>Microsoft <strong>Azure</strong></p>
<ul>
<li><p>strong integration with Microsoft’s Enterprise ecosystem</p></li>
<li><p>powerful hybrid cloud story</p></li>
</ul></li>
<li><p>Google Cloud Platform (<strong>GCP</strong>)</p>
<ul>
<li><p>leader in AI, machine learning, and data analytics</p></li>
<li><p>leverages Google’s extensive infrastructure</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Model Landscape (video data is stale)</td>
</tr>
<tr>
<td rowspan="2">Model Capabilities</td>
<td style="text-align: center;"><strong>GPT-4.0</strong></td>
<td style="text-align: center;"><strong>Claude Sonnet 3.5</strong></td>
<td style="text-align: center;"><strong>Gemini 1.5 Pro</strong></td>
</tr>
<tr>
<td><ul>
<li><p>fast all-rounder</p></li>
<li><p>native multimodal</p>
<ul>
<li><p>text</p></li>
<li><p>audio</p></li>
<li><p>vision</p></li>
</ul></li>
<li><p>ideal for real-time conversational AI</p></li>
</ul></td>
<td><ul>
<li><p>reasoning specialist</p></li>
<li><p>leads in</p>
<ul>
<li><p>top-tier reasoning</p></li>
<li><p>instruction following</p></li>
<li><p>coding benchmarks</p></li>
</ul></li>
<li><p>excellent for complex tasks</p></li>
</ul></td>
<td><ul>
<li><p>“Context King”</p></li>
<li><p>good multimodal skills</p></li>
<li><p>its defining feature is its massive context window for large-scale analysis</p></li>
</ul></td>
</tr>
<tr>
<td>Context Windows</td>
<td>128K</td>
<td>200K</td>
<td>1M</td>
</tr>
<tr>
<td colspan="4"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Live Session</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Welcome to DATA790</td>
</tr>
<tr>
<td>Dr. Grant Glass</td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><p><img src="generated_media\DATA790_week01_notes\media\image4.png" style="width:6.03125in;height:2.716in" /></p>
<p><img src="generated_media\DATA790_week01_notes\media\image5.png" style="width:6in;height:3.21669in" /></p>
<p><img src="generated_media\DATA790_week01_notes\media\image6.png" style="width:5.92708in;height:2.69758in" /></p>
<p><img src="generated_media\DATA790_week01_notes\media\image7.png" style="width:6.11458in;height:3.9882in" /></p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"></td>
</tr>
</tbody>
</table>
