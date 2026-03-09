---
generated_at_utc: 2026-03-09T20:38:56+00:00
generated_from: notes/Spring_2026/DATA780/Week09/docx/DATA780_week09_notes.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [DATA780_week09_notes.pdf](../DATA780_week09_notes.pdf)
> - DOCX: [DATA780_week09_notes.docx](DATA780_week09_notes.docx)

---

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Tree-Based Methods</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Overview</td>
<td colspan="2" style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>tree-based methods used for regression and classification</p></li>
<li><p>stratifying and segmenting the predictor space into simple regions</p></li>
<li><p>bagging, random forests, and boosting</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Reading</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><p>An Introduction to Statistical Learning: Chapter 8 (textbook)</p>
<p><a href="https://www.statlearning.com/">https://www.statlearning.com/</a></p>
<p>Decision Trees: Statistical Learning (slideshow)</p>
<p><a href="https://www.reisanar.com/slides/islr-ch_8-notes.pdf">https://www.reisanar.com/slides/islr-ch_8-notes.pdf</a></p></td>
</tr>
<tr>
<td colspan="3">Terms</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><p>tree-based methods</p>
<blockquote>
<p>family of supervised learning methods that make predictions by recursively splitting the predictor space</p>
</blockquote>
<p>decision tree</p>
<blockquote>
<p>model represented as a tree of sequential splitting rules where each path leads to a decision</p>
</blockquote>
<p>regression tree</p>
<blockquote>
<p>tree used when the response variable is quantitative</p>
<p>predictions are typically the mean response within a region</p>
</blockquote>
<p>classification tree</p>
<blockquote>
<p>tree used when the response variable is qualitative or categorical</p>
<p>predictions are the most common class within a region</p>
</blockquote>
<p>predictor/feature space</p>
<blockquote>
<p>space formed by the input variables</p>
<p>tree methods divide this space into separate regions</p>
</blockquote>
<p>region/box</p>
<blockquote>
<p>partitions of the predictor space created by the tree’s splits</p>
<p>each region gets its own prediction</p>
</blockquote>
<p>split</p>
<blockquote>
<p>rule that divides the data into two parts based on a predictor and a threshold</p>
<p>ex: <span class="math inline"><strong>X</strong><sub><strong>1</strong></sub> <strong>≤</strong> <strong>t</strong></span></p>
</blockquote>
<p>binary split</p>
<blockquote>
<p>creates exactly two child regions from one parent region</p>
</blockquote>
<p>recursive binary splitting</p>
<blockquote>
<p>top-down, greedy tree-building procedure that repeatedly chooses the split that most improves the fit at the current step</p>
</blockquote>
<p>top-down approach</p>
<blockquote>
<p>algorithm that begins with the full dataset and repeatedly divides it into smaller subsets</p>
</blockquote>
<p>greedy approach</p>
<blockquote>
<p>algorithm that chooses the best immediate split at each step rather than searching all possible full-tree structures</p>
</blockquote>
<p>terminal node (leaf node)</p>
<blockquote>
<p>end node of the tree</p>
<p>once an observation lands there, the model outputs that node’s prediction</p>
</blockquote>
<p>internal node</p>
<blockquote>
<p>non-terminal node where a split is made on one predictor</p>
</blockquote>
<p>stopping criterion</p>
<blockquote>
<p>rule for deciding when tree growth should stop</p>
<p>ex: when a node has too few observations remaining to split further</p>
</blockquote>
<p>prediction surface</p>
<blockquote>
<p>function implied by the tree over the feature space</p>
<p>for regression trees it is piecewise constant across regions</p>
</blockquote>
<p>Residual Sum of Squares (RSS)</p>
<blockquote>
<p>the criterion used to measure fit</p>
<p>splits are chosen to reduce RSS</p>
</blockquote>
<p>mean response in a region</p>
<blockquote>
<p>the prediction for a region is the average of the training responses inside that region</p>
</blockquote>
<p>overfitting</p>
<blockquote>
<p>training data is fit too closely and performs poorly on new data</p>
<p>large trees are especially prone to this</p>
</blockquote>
<p>pruning</p>
<blockquote>
<p>cutting back a large tree to a smaller subtree to improve generalization and interpretability</p>
</blockquote>
<p>cost-complexity pruning (weakest-link pruning)</p>
<blockquote>
<p>pruning method that balances training fit against tree size using a penalty term</p>
</blockquote>
<p>subtree</p>
<blockquote>
<p>smaller tree obtained by pruning branches from a larger tree</p>
</blockquote>
<p>tuning parameter (<span class="math inline"><strong>α</strong></span>)</p>
<blockquote>
<p>non-negative parameter in cost-complexity pruning that controls the trade-off between goodness of fit and tree complexity</p>
</blockquote>
<p>tree complexity</p>
<blockquote>
<p>generally measured by the number of terminal nodes or splits</p>
<p>more complex trees fit training data better but can overfit</p>
</blockquote>
<p>cross-validation</p>
<blockquote>
<p>resampling method used to estimate test error and choose the best tuning parameter</p>
<p>ex: <span class="math inline"><strong>α</strong></span></p>
</blockquote>
<p>k-fold cross-validation</p>
<blockquote>
<p>cross-validation procedure that splits data into <span class="math inline"><strong>K</strong> </span>folds, trains on <span class="math inline"><strong>K</strong> <strong>−</strong> <strong>1</strong></span>, tests on the held-out fold, and averages the error</p>
</blockquote>
<p>mean squared error (MSE)</p>
<blockquote>
<p>common regression error metric used to evaluate predictive performance</p>
</blockquote>
<p>qualitative response</p>
<blockquote>
<p>categorical target variable used in classification trees</p>
<p>ex: (yes/no)</p>
</blockquote>
<p>quantitative response</p>
<blockquote>
<p>numeric target variable, such as salary or price, used in regression trees</p>
</blockquote>
<p>classification error rate</p>
<blockquote>
<p>fraction of observations in a node that do not belong to the majority class</p>
</blockquote>
<p>class proportion (<span class="math inline">${\widehat{\mathbf{p}}}^{\mathbf{mk}}$</span>)</p>
<blockquote>
<p>estimated proportion of training observations in node <span class="math inline"><strong>m</strong></span> that belong to class <span class="math inline"><strong>k</strong></span></p>
</blockquote>
<p>node purity</p>
<blockquote>
<p>measure of how dominated a node is by a single class</p>
<p>purer nodes contain mostly one class</p>
</blockquote>
<p>Gini index</p>
<blockquote>
<p>classification-tree splitting criterion that measures node impurity</p>
<p>smaller values means more-pure nodes</p>
</blockquote>
<p>cross-entropy (deviance)</p>
<blockquote>
<p>impurity measure for classification trees</p>
<p>numerically similar to the Gini index in many settings</p>
</blockquote>
<p>training data</p>
<blockquote>
<p>observations used to build the tree and determine splits</p>
</blockquote>
<p>test set performance</p>
<blockquote>
<p>how well the tree predicts new unseen data</p>
<p>this is what pruning and cross-validation try to improve</p>
</blockquote></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 28%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Async</th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Bagging</td>
</tr>
<tr>
<td>Bootstrap Aggregating</td>
<td colspan="2"><ul>
<li><p>another name for ‘<strong>bagging’</strong></p></li>
</ul>
<p><span class="math inline"><strong>n</strong></span>: total number of instances</p>
<p><span class="math inline"><strong>n</strong><strong>’</strong></span>: number of instances in each bag</p>
<p>(<span class="math inline"><strong>n</strong><strong>′</strong> <strong>&lt;</strong> <strong>n</strong></span>)</p>
<p><span class="math inline"><strong>m</strong></span>: number of bags</p>
<ul>
<li><p>general-purpose procedure for <strong>reducing</strong> the <strong>variance</strong> of a statistical <strong>learning</strong> method</p></li>
<li><p>bootstrap <strong>samples</strong> are like independent <strong>realizations</strong> of the <strong>data</strong></p></li>
<li><p>amounts to <strong>averaging</strong> the <strong>fits</strong> from <strong>many</strong> independent <strong>datasets</strong>, which would <strong>reduce</strong> the <strong>variance</strong> by a <strong>factor</strong> of <span class="math inline">$\frac{\mathbf{1}}{\mathbf{Β}}$</span> where <span class="math inline"><strong>Β</strong></span> is the <strong>number</strong> of bootstrap <strong>samples</strong></p></li>
<li><p>when bootstrapping, we <strong>replace</strong> our dataset by <strong>sampling</strong> with <strong>replacement</strong></p></li>
<li><p>when bagging, we <strong>average</strong> the <strong>predictions</strong> of a model fit to many bootstrap <strong>samples</strong></p></li>
</ul></td>
</tr>
<tr>
<td>When to Use Bagging</td>
<td colspan="2"><ul>
<li><p>when other methods tend to <strong>overfit</strong>, bagging <strong>reduces</strong> the <strong>variance</strong> of the prediction</p></li>
<li><p>the empirical distribution is <strong>similar</strong> to the <strong>true</strong> distribution of the samples when <span class="math inline"><strong>n</strong></span> is <strong>large</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Bootstrapping with Decision Trees</td>
<td colspan="2"><ul>
<li><p>every time we fit a <strong>decision</strong> <strong>tree</strong> to a bootstrap <strong>sample</strong>, we get a <strong>different</strong> tree <span class="math inline"><strong>T</strong><strong>b</strong></span></p></li>
<li><p>may lead to <strong>loss</strong> of <strong>interpretability</strong></p></li>
<li><p>for each <strong>predictor</strong></p>
<ul>
<li><p><strong>add</strong> up the <strong>total</strong> amount by which the <strong>RSS</strong> (or <strong>Gini</strong> index) <strong>decreases</strong> every time we use the <strong>predictor</strong> in <span class="math inline"><strong>T</strong><sub><strong>b</strong></sub></span></p></li>
<li><p>then, <strong>average</strong> this total over each bootstrap <strong>estimate</strong> <span class="math inline"><strong>T</strong><sub><strong>1</strong></sub><strong>,</strong> <strong>…</strong><strong>,</strong> <strong>T</strong><sub><strong>B</strong></sub></span></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Out-of-Bag Error (OOB)</td>
<td colspan="2"><ul>
<li><p>every bootstrapped <strong>sample</strong> has a <strong>corresponding</strong> hold out or ‘<strong>out</strong>-of-<strong>bag’</strong> sample which is used to <strong>test</strong></p></li>
<li><p>to <strong>determine</strong> the test <strong>error</strong> of a bagging <strong>estimate</strong>, we could use cross-validation</p></li>
<li><p>each time we <strong>draw</strong> bootstrap <strong>sample</strong>, we only use <span class="math inline"><strong>63</strong><strong>%</strong></span> of the <strong>observations</strong></p></li>
<li><p>use the rest of the <strong>observations</strong> can be used as a <strong>test</strong> set</p></li>
</ul></td>
</tr>
<tr>
<td>Bagging for Regression Trees</td>
<td colspan="2"><ul>
<li><p>regression trees are <strong>grown deep,</strong> and are <strong>not pruned</strong></p></li>
<li><p>each individual tree has <strong>high</strong> <strong>variance</strong>, but <strong>low</strong> <strong>bias</strong></p></li>
<li><p>averaging <strong>these </strong><span class="math inline"><strong>B</strong></span><strong> trees</strong> reduces <strong>the</strong> variance</p></li>
</ul></td>
</tr>
<tr>
<td>Bagging for Classification Trees</td>
<td colspan="2"><ul>
<li><p>for a given test <strong>observation</strong>, we can record the class <strong>predicted</strong> by<br />
each of the <span class="math inline"><strong>B</strong> <strong>t</strong><strong>r</strong><strong>e</strong><strong>e</strong><strong>s</strong></span>, and take a <strong>majority</strong> vote</p></li>
<li><p>a majority vote is simply the <strong>overall</strong> <strong>prediction</strong> is the most <strong>commonly</strong> occurring <strong>class</strong> among the <span class="math inline"><strong>B</strong></span> predictions</p></li>
</ul></td>
</tr>
<tr>
<td>Variable Importance</td>
<td colspan="2"><ul>
<li><p>when we bag a <strong>large</strong> <strong>number</strong> of trees, it is <strong>no</strong> longer <strong>possible</strong> to <strong>represent</strong> the resulting statistical <strong>learning</strong> procedure using a <strong>single</strong> tree</p></li>
<li><p>it is no longer clear which <strong>variables</strong> are most <strong>important</strong> to the <strong>procedure</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Complexity of Interpretation</td>
<td colspan="2"><ul>
<li><p>the <strong>collection</strong> of bagged trees is much more <strong>difficult</strong> to <strong>interpret</strong> than a <strong>single</strong> tree</p></li>
<li><p>an overall <strong>summary</strong> of the <strong>importance</strong> of each <strong>predictor</strong> using</p>
<ul>
<li><p><strong>RSS</strong> (for bagging <strong>regression</strong> trees)</p></li>
<li><p><strong>Gini</strong> <strong>index</strong> (for bagging <strong>classification</strong> trees)</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Interpreting Bagging with Regression Trees</td>
<td colspan="2"><ul>
<li><p>we can record the total <strong>amount</strong> that the <strong>RSS</strong> has <strong>decreased</strong> due to <strong>splits</strong> over a given <strong>predictor</strong> averaged over all <span class="math inline"><strong>B</strong></span> trees</p></li>
<li><p>a <strong>large</strong> value indicates an <strong>important</strong> predictor</p></li>
</ul></td>
</tr>
<tr>
<td>Interpreting Bagging with Classification Trees</td>
<td colspan="2"><ul>
<li><p><strong>add</strong> up the total <strong>amount</strong> that the <strong>Gini</strong> index is decreased by splits over a given <strong>predictor</strong> <strong>averaged</strong> over all B trees</p></li>
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
<th colspan="2">Random Forests</th>
</tr>
</thead>
<tbody>
<tr>
<td>The Problem with Bagging</td>
<td><ul>
<li><p>the trees <strong>produced</strong> by different <strong>bootstrap</strong> samples can be very <strong>similar</strong></p></li>
<li><p>random <strong>forests</strong> provide an <strong>improvement</strong> over bagged trees by way of a small tweak that <strong>de</strong>-<strong>correlates</strong> the trees</p></li>
</ul></td>
</tr>
<tr>
<td>The “Small Tweak”</td>
<td><ul>
<li><p><strong>fit</strong> a decision tree to <strong>different</strong> bootstrap <strong>samples</strong></p></li>
<li><p>when growing the tree, we <strong>select</strong> a random <strong>sample</strong> of <span class="math inline"><strong>m</strong> <strong>&lt;</strong> <strong>p</strong></span> <strong>predictors</strong> to consider in each step</p></li>
<li><p>this will lead to very different (<strong>uncorrelated</strong>) <strong>trees</strong> from each <strong>sample</strong></p></li>
<li><p>then, <strong>average</strong> the <strong>prediction</strong> of each tree</p></li>
</ul></td>
</tr>
<tr>
<td>Interpretation</td>
<td><ul>
<li><p>the <strong>optimal</strong> <span class="math inline"><strong>m</strong></span> is usually around the <strong>square</strong> <strong>root</strong> of <span class="math inline"><strong>p</strong></span></p></li>
<li><p>this can be used as a <strong>tuning</strong> <strong>parameter</strong></p></li>
<li><p>the <strong>split</strong> uses only one of those <span class="math inline"><strong>m</strong></span> <strong>predictors</strong></p></li>
<li><p>a fresh <strong>sample</strong> of <span class="math inline"><strong>m</strong></span> <strong>predictors</strong> is taken at each <strong>split</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Why Limit Available Parameters?</td>
<td><ul>
<li><p><strong>assume</strong> that there is one very <strong>strong</strong> <strong>predictor</strong> in the data set <strong>along</strong> with a number of other <strong>moderately</strong> <strong>strong</strong> predictors</p></li>
<li><p>in the <strong>collection</strong> of bagged trees, <strong>most</strong> or <strong>all</strong> of the trees will use this <strong>strong</strong> predictor in the <strong>top</strong> <strong>split</strong></p></li>
<li><p><strong>all</strong> of the bagged <strong>trees</strong> will look quite <strong>similar</strong> to each other and the <strong>predictions</strong> from the bagged trees will be <strong>highly</strong> <strong>correlated</strong></p></li>
<li><p><strong>averaging</strong> many highly <strong>correlated</strong> <strong>quantities</strong> does <strong>not</strong> lead to as large of a <strong>reduction</strong> in <strong>variance</strong> as averaging many <strong>uncorrelated</strong> quantities</p></li>
<li><p>this means that <strong>bagging</strong> will <strong>not</strong> lead to a substantial <strong>reduction</strong> in <strong>variance</strong> over a <strong>single</strong> tree</p></li>
<li><p><strong>random</strong> <strong>forests</strong> overcome this problem by <strong>forcing</strong> each <strong>split</strong> to<br />
consider only a <strong>subset</strong> of the <strong>predictors</strong></p></li>
<li><p>take note if a <strong>random</strong> <strong>forest</strong> is built where <span class="math inline"><strong>m</strong> <strong>=</strong> <strong>p</strong></span>, then bagging is a <strong>special</strong> case of <strong>random</strong> forests</p></li>
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
<th colspan="2">Boosting</th>
</tr>
</thead>
<tbody>
<tr>
<td>General Approach</td>
<td><ul>
<li><p>similar to bagging, <strong>boosting</strong> is a general <strong>approach</strong> that can be applied to many <strong>statistical</strong> <strong>learning</strong> methods for <strong>regression</strong> or <strong>classification</strong> trees</p></li>
<li><p>booting <strong>learns</strong> <strong>slowly</strong></p></li>
</ul></td>
</tr>
<tr>
<td>Process</td>
<td><ul>
<li><p>use the <strong>samples</strong> that are <strong>easiest</strong> to <strong>predict</strong></p></li>
<li><p>slowly <strong>downweigh</strong> these cases</p></li>
<li><p>then move on to <strong>harder</strong> <strong>samples</strong></p></li>
<li><p><strong>fit</strong> <strong>small</strong> (low variance but high bias) <strong>trees</strong> in each round</p></li>
<li><p>boosting <strong>learns</strong> <strong>sequentially</strong> and <strong>trains</strong> on <strong>errors</strong></p></li>
<li><p>each <strong>iteration</strong> learns to <strong>predict</strong> the <strong>mistakes</strong> of the previous iteration</p></li>
<li><p>subsequent <strong>samples</strong> depend on <strong>weights</strong> given to records in the <strong>previous</strong> sample which did <strong>not</strong> <strong>predict</strong> correctly (<strong>weak</strong> <strong>learners</strong>)</p></li>
<li><p>the <strong>final</strong> prediction is a <strong>weighted</strong> <strong>average</strong></p></li>
</ul></td>
</tr>
<tr>
<td><p>AdaBoost</p>
<p>(Adaptive Boosting)</p></td>
<td><ul>
<li><p>influential ensemble <strong>machine</strong> <strong>learning</strong> <strong>method</strong> that sequentially <strong>combines</strong> many simple "<strong>weak</strong> learners" into a <strong>single</strong>, high-performing "<strong>strong</strong> classifier"</p>
<ul>
<li><p><strong>initialize</strong> weights</p></li>
<li><p><strong>train</strong> model in ‘usual way’</p></li>
<li><p>use training data to <strong>test</strong> model</p></li>
<li><p><strong>extract</strong> <strong>error</strong></p></li>
<li><p>again, randomly <strong>select</strong> from original <strong>data</strong> (separate bag)</p></li>
<li><p>each instance is <strong>weighted</strong> against <strong>error</strong></p></li>
<li><p>then, <strong>build</strong> and <strong>test</strong> model</p></li>
<li><p><strong>combine</strong> run <strong>outputs</strong></p></li>
<li><p><strong>iterate</strong> process through <span class="math inline"><strong>m</strong></span> <strong>bags</strong></p></li>
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
<th>R Programming</th>
<th><ul>
<li><p>implementation note: tree vs. rpart in R</p>
<ul>
<li><p>both packages build decision trees.</p></li>
<li><p>The main difference is how they handle missing values during splitting and scoring.</p></li>
</ul></li>
<li><p>tree package</p>
<ul>
<li><p>if an observation is missing the value for the primary split variable</p>
<ul>
<li><p>it is not sent further down the tree</p></li>
</ul></li>
</ul></li>
<li><p>rpart package</p>
<ul>
<li><p>missing values can be handled in different ways</p></li>
</ul></li>
</ul>
<p><strong>k</strong>ey takeaway</p>
<ul>
<li><p>usesurrogate = 0 in rpart behaves like tree()</p></li>
<li><p>usesurrogate = 2 is the default in rpart()</p></li>
<li><p><strong>t</strong>he default follows the recommendation of Breiman et al. (1984)</p>
<ul>
<li><p>controlled with the usesurrogate parameter in rpart.control</p></li>
</ul></li>
<li><p>usesurrogate options</p>
<ul>
<li><p>usesurrogate = <span class="math inline"><strong>0</strong></span></p>
<ul>
<li><p>display surrogates only</p></li>
<li><p>if the primary split value is missing, the observation is not split further</p></li>
<li><p>this matches the behavior of tree()</p></li>
</ul></li>
<li><p>usesurrogate = <span class="math inline"><strong>1</strong></span></p>
<ul>
<li><p>use surrogate split rules, in order</p></li>
<li><p>if all surrogate values are also missing, the observation is not split</p></li>
</ul></li>
<li><p>usesurrogate = 2</p>
<ul>
<li><p>use surrogate split rules, in order</p></li>
<li><p>if all surrogate values are missing, send the observation in the majority direction</p></li>
<li><p>this is the default in rpart()</p></li>
</ul></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>
