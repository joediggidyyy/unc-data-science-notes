---
generated_at_utc: 2026-03-10T16:44:04+00:00
generated_from: notes/Spring_2026/DATA780/StudyGuides/docx/Mid-Term_Study-Guide.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [Mid-Term_Study-Guide.pdf](../Mid-Term_Study-Guide.pdf)
> - DOCX: [Mid-Term_Study-Guide.docx](Mid-Term_Study-Guide.docx)

---

<table>
<caption>Cover page info</caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr>
<th></th>
<th><blockquote>
<p>Midterm Study Guide</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>UNC Chapel Hill - MADS</p>
<p>DATA780: Machine Learning</p>
<p>Spring 2026</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Table of Contents

[Foundations of statistical learning [2](#foundations-of-statistical-learning)](#foundations-of-statistical-learning)

[Quick definitions: [2](#quick-definitions)](#quick-definitions)

[• Statistical learning [2](#_Toc224038696)](#_Toc224038696)

[• Supervised learning [2](#_Toc224038697)](#_Toc224038697)

[• Unsupervised learning [2](#_Toc224038698)](#_Toc224038698)

[• Regression [2](#_Toc224038699)](#_Toc224038699)

[Core NumPy / computational foundations [3](#core-numpy-computational-foundations)](#core-numpy-computational-foundations)

[Quick definition: [3](#quick-definition)](#quick-definition)

[• Broadcasting [3](#_Toc224038702)](#_Toc224038702)

[Linear algebra background for machine learning [4](#linear-algebra-background-for-machine-learning)](#linear-algebra-background-for-machine-learning)

[• Know definitions and interpretations of: [4](#_Toc224038704)](#_Toc224038704)

[• Understand matrix operations and concepts: [4](#_Toc224038705)](#_Toc224038705)

[• Quick definitions: [5](#_Toc224038706)](#_Toc224038706)

[o Scalar [5](#_Toc224038707)](#_Toc224038707)

[o Vector [5](#_Toc224038708)](#_Toc224038708)

[o Basis [5](#_Toc224038709)](#_Toc224038709)

[o Span [5](#_Toc224038710)](#_Toc224038710)

[o Column [5](#_Toc224038711)](#_Toc224038711)

[o Null space [5](#_Toc224038712)](#_Toc224038712)

[o Orthonormal [5](#_Toc224038713)](#_Toc224038713)

[• Core equations: [5](#_Toc224038714)](#_Toc224038714)

[o Dot product [5](#_Toc224038715)](#_Toc224038715)

[o Euclidean norm [6](#_Toc224038716)](#_Toc224038716)

[o Euclidean distance [6](#_Toc224038717)](#_Toc224038717)

[o Rank-nullity [6](#_Toc224038718)](#_Toc224038718)

[o Eigenvector relation [6](#_Toc224038719)](#_Toc224038719)

[Linear regression [7](#linear-regression)](#linear-regression)

[Core equations: [7](#core-equations)](#core-equations)

[o Scalar form [7](#_Toc224038722)](#_Toc224038722)

[o Vector form [7](#_Toc224038723)](#_Toc224038723)

[o SSE / RSS objective [8](#_Toc224038724)](#_Toc224038724)

[o Matrix least squares solution [8](#_Toc224038725)](#_Toc224038725)

[o Ridge-regularized objective [8](#_Toc224038726)](#_Toc224038726)

[Helpful interpretations: [8](#helpful-interpretations)](#helpful-interpretations)

[o Design matrix $`\Phi`$ [8](#_Toc224038728)](#_Toc224038728)

[o Least squares [8](#_Toc224038729)](#_Toc224038729)

[o Probabilistic model [8](#_Toc224038730)](#_Toc224038730)

[Optimization concepts [9](#optimization-concepts)](#optimization-concepts)

[Core equations: [9](#core-equations-1)](#core-equations-1)

[o Gradient descent update [9](#_Toc224038733)](#_Toc224038733)

[o SGD update [9](#_Toc224038734)](#_Toc224038734)

[Key idea: [9](#key-idea)](#key-idea)

[o Closed-form solutions [9](#_Toc224038736)](#_Toc224038736)

[Logistic regression and classification [10](#logistic-regression-and-classification)](#logistic-regression-and-classification)

[Core equations: [10](#core-equations-2)](#core-equations-2)

[o Logit score [10](#_Toc224038739)](#_Toc224038739)

[o Sigmoid [10](#_Toc224038740)](#_Toc224038740)

[o Binary probability model [10](#_Toc224038741)](#_Toc224038741)

[o Sigmoid derivative [10](#_Toc224038742)](#_Toc224038742)

[o Negative log-likelihood / cross-entropy [11](#_Toc224038743)](#_Toc224038743)

[o Softmax for class $`k`$ [11](#_Toc224038744)](#_Toc224038744)

[Important note: [11](#important-note)](#important-note)

[o Logistic regression [11](#_Toc224038746)](#_Toc224038746)

[Discriminative vs generative models [12](#discriminative-vs-generative-models)](#discriminative-vs-generative-models)

[Core equation: [12](#core-equation)](#core-equation)

[o Bayes rule [12](#_Toc224038749)](#_Toc224038749)

[Decision rule: [12](#decision-rule)](#decision-rule)

[o Bayes classifier [12](#_Toc224038751)](#_Toc224038751)

[Gaussian Bayes / generative classification [13](#gaussian-bayes-generative-classification)](#gaussian-bayes-generative-classification)

[Core density: [13](#core-density)](#core-density)

[Key interpretation: [13](#key-interpretation)](#key-interpretation)

[o If classes have different covariance matrices [13](#_Toc224038755)](#_Toc224038755)

[Conditional independence and Naive Bayes [14](#conditional-independence-and-naive-bayes)](#conditional-independence-and-naive-bayes)

[Core definitions and equations: [14](#core-definitions-and-equations)](#core-definitions-and-equations)

[• Conditional independence [14](#_Toc224038758)](#_Toc224038758)

[• Naive Bayes assumption [14](#_Toc224038759)](#_Toc224038759)

[• Posterior up to proportionality: [14](#_Toc224038760)](#_Toc224038760)

[Neural networks: big picture and core building blocks [15](#neural-networks-big-picture-and-core-building-blocks)](#neural-networks-big-picture-and-core-building-blocks)

[Core equations: [15](#core-equations-3)](#core-equations-3)

[o One hidden layer network [15](#_Toc224038763)](#_Toc224038763)

[o For binary classification [15](#_Toc224038764)](#_Toc224038764)

[Key idea: [15](#key-idea-1)](#key-idea-1)

[o Without a nonlinear activation [15](#_Toc224038766)](#_Toc224038766)

[Neural networks: extended vocabulary and architectures [16](#neural-networks-extended-vocabulary-and-architectures)](#neural-networks-extended-vocabulary-and-architectures)

[Know terms such as: [16](#know-terms-such-as)](#know-terms-such-as)

[Understand convolutional neural networks (CNNs): [16](#understand-convolutional-neural-networks-cnns)](#understand-convolutional-neural-networks-cnns)

[Understand recurrent neural networks (RNNs): [16](#understand-recurrent-neural-networks-rnns)](#understand-recurrent-neural-networks-rnns)

[Quick definitions: [17](#quick-definitions-1)](#quick-definitions-1)

[o Logits [17](#_Toc224038772)](#_Toc224038772)

[o Tensor [17](#_Toc224038773)](#_Toc224038773)

[o Attention [17](#_Toc224038774)](#_Toc224038774)

[o CNNs [17](#_Toc224038775)](#_Toc224038775)

[o RNNs [17](#_Toc224038776)](#_Toc224038776)

[Validation, model assessment, and model selection [18](#validation-model-assessment-and-model-selection)](#validation-model-assessment-and-model-selection)

[Core concepts: [18](#core-concepts)](#core-concepts)

[o Model assessment [18](#_Toc224038779)](#_Toc224038779)

[o Model selection [18](#_Toc224038780)](#_Toc224038780)

[Important relationship: [19](#important-relationship)](#important-relationship)

[o In squared-error [19](#_Toc224038782)](#_Toc224038782)

[Cross-validation reminder: [19](#cross-validation-reminder)](#cross-validation-reminder)

[o LOOCV [19](#_Toc224038784)](#_Toc224038784)

[o k-fold CV [19](#_Toc224038785)](#_Toc224038785)

[Tree-based methods [20](#tree-based-methods)](#tree-based-methods)

[Core equations: [21](#core-equations-4)](#core-equations-4)

[o Regression tree node prediction [21](#_Toc224038788)](#_Toc224038788)

[o RSS for a split [21](#_Toc224038789)](#_Toc224038789)

[o Gini index [21](#_Toc224038790)](#_Toc224038790)

[o Cross-entropy / deviance [21](#_Toc224038791)](#_Toc224038791)

[o Cost-complexity criterion [21](#_Toc224038792)](#_Toc224038792)

[Key idea: [21](#key-idea-2)](#key-idea-2)

[o Larger trees [21](#_Toc224038794)](#_Toc224038794)

[Ensemble tree methods [22](#ensemble-tree-methods)](#ensemble-tree-methods)

[Quick definitions: [22](#quick-definitions-2)](#quick-definitions-2)

[o Bagging [22](#_Toc224038797)](#_Toc224038797)

[o Random forest [22](#_Toc224038798)](#_Toc224038798)

[o Boosting [22](#_Toc224038799)](#_Toc224038799)

[Core aggregation rules: [22](#core-aggregation-rules)](#core-aggregation-rules)

[o Regression bagging [22](#_Toc224038801)](#_Toc224038801)

[Conceptual comparisons that are especially exam-worthy [24](#conceptual-comparisons-that-are-especially-exam-worthy)](#conceptual-comparisons-that-are-especially-exam-worthy)

[Formulas / relationships worth knowing cold [25](#formulas-relationships-worth-knowing-cold)](#formulas-relationships-worth-knowing-cold)

[• Linear regression [25](#_Toc224038804)](#_Toc224038804)

[• Least squares [25](#_Toc224038805)](#_Toc224038805)

[• Normal equation [25](#_Toc224038806)](#_Toc224038806)

[• Sigmoid [25](#_Toc224038807)](#_Toc224038807)

[• Logistic regression loss [25](#_Toc224038808)](#_Toc224038808)

[• Gradient descent [25](#_Toc224038809)](#_Toc224038809)

[• Bayes rule [25](#_Toc224038810)](#_Toc224038810)

[• Naive Bayes [25](#_Toc224038811)](#_Toc224038811)

[• Bias-variance-noise [25](#_Toc224038812)](#_Toc224038812)

[• Tree impurity [25](#_Toc224038813)](#_Toc224038813)

[Practical interpretation / short-answer themes likely to appear [26](#practical-interpretation-short-answer-themes-likely-to-appear)](#practical-interpretation-short-answer-themes-likely-to-appear)

**
**

# Foundations of statistical learning

- Define statistical learning and explain its goals: prediction, pattern discovery, and inference from data.

- Distinguish **supervised learning** from **unsupervised learning**.

- Recognize common task types:

  - regression for quantitative outputs

  - classification for categorical outputs

  - clustering and dimensionality reduction for unlabeled data

- Explain why combining multiple predictors can improve prediction over using a single variable.

- Interpret examples such as wage prediction, stock-market direction, and gene-expression clustering.

## Quick definitions:

- <span id="_Toc224038696" class="anchor"></span>Statistical learning = using data to estimate relationships between predictors $`X`$ and an outcome $`Y`$.

- <span id="_Toc224038697" class="anchor"></span>Supervised learning = learn from labeled pairs $`\left( x_{i},y_{i} \right)`$.

- <span id="_Toc224038698" class="anchor"></span>Unsupervised learning = learn structure from unlabeled data $`x_{i}`$ only.

- <span id="_Toc224038699" class="anchor"></span>Regression predicts a numeric response; **classification** predicts a class label; **clustering** groups similar observations without labels.

- Core idea: we often want a rule $`f`$ such that $`Y \approx f(X)`$, where $`X`$ may be a single predictor or a vector of many predictors.

# Core NumPy / computational foundations

- Explain **broadcasting** and why it matters for efficient array computation.

- State the broadcasting compatibility rules:

  - compare shapes from the right

  - dimensions are compatible if equal or one equals 1

  - otherwise NumPy raises an error

- Understand scalar expansion and shape matching without unnecessary copying.

## Quick definition:

- <span id="_Toc224038702" class="anchor"></span>Broadcasting lets NumPy perform elementwise operations on arrays of different shapes when dimensions are compatible.

  - Useful shape examples:

    - $`\left( n,p) + (p,) \rightarrow (n,p \right)`$

    - $`\left( n,1) + (1,p) \rightarrow (n,p \right)`$

    - scalar $`c`$ can broadcast to any array shape

**
**

# Linear algebra background for machine learning

- <span id="_Toc224038704" class="anchor"></span>Know definitions and interpretations of:

  - scalar

  - vector

  - vector space

  - subspace

  - basis

  - span

  - column space / column rank

  - null space / nullity

  - orthonormality

- <span id="_Toc224038705" class="anchor"></span>Understand matrix operations and concepts:

  - matrix multiplication

  - transpose

  - inner product / dot product

  - outer product

  - Hadamard product

  - determinant

  - trace

  - norm and distance

  - Euclidean distance

- Be able to explain **rank-nullity**.

- Know the role of **eigenvalues**, **eigenvectors**, and **eigendecomposition**.

- Understand why these ideas matter for ML representations and optimization.

- <span id="_Toc224038706" class="anchor"></span>Quick definitions:

  - <span id="_Toc224038707" class="anchor"></span>Scalar: a single number.

  - <span id="_Toc224038708" class="anchor"></span>Vector: an ordered list of numbers, often viewed as a point or direction in space.

  - <span id="_Toc224038709" class="anchor"></span>Basis: a linearly independent set that spans a vector space.

  - <span id="_Toc224038710" class="anchor"></span>Span: all linear combinations of a set of vectors.

  - <span id="_Toc224038711" class="anchor"></span>Column space: all linear combinations of a matrix's columns.

  - <span id="_Toc224038712" class="anchor"></span>Null space: all vectors $`x`$ such that $`Ax = 0`$.

  - <span id="_Toc224038713" class="anchor"></span>Orthonormal: vectors are mutually orthogonal and each has norm 1.

- <span id="_Toc224038714" class="anchor"></span>Core equations:

  - <span id="_Toc224038715" class="anchor"></span>Dot product: $`x^{T}y = \sum_{j = 1}^{p}x_{j}y_{j}`$

  - <span id="_Toc224038716" class="anchor"></span>Euclidean norm: $`\parallel x \parallel_{2} = \sqrt{\sum_{j = 1}^{p}x_{j}^{2}}`$

  - <span id="_Toc224038717" class="anchor"></span>Euclidean distance: $`d(x,y) = \parallel x - y \parallel_{2}`$

  - <span id="_Toc224038718" class="anchor"></span>Rank-nullity: $`{rank}(A) + {nullity}(A) = p`$ for an $`m \times p`$ matrix $`A`$

  - <span id="_Toc224038719" class="anchor"></span>Eigenvector relation: $`Av = \lambda v`$

**
**

# Linear regression

- Define linear regression as a supervised learning model for predicting real-valued outputs.

- Write the linear model with weights and intercept.

- Explain the sum of squared errors loss.

- Derive or interpret the least-squares solution.

- Understand the design matrix and the closed-form solution:

- $`w^{*} = (\Phi^{T}\Phi)^{- 1}\Phi^{T}t`$

- Explain the geometric interpretation of least squares as projection onto the column space.

- Understand basis functions and how they allow nonlinear structure to be modeled in transformed space.

- Explain the probabilistic interpretation:

- Gaussian noise assumption

- least squares as maximum likelihood estimation

- Interpret the predictive distribution and prediction uncertainty.

- Explain overfitting and the purpose of regularization.

## Core equations:

- <span id="_Toc224038722" class="anchor"></span>Scalar form: $`\widehat{y} = w_{0} + w_{1}x_{1} + \cdots + w_{p}x_{p}`$

- <span id="_Toc224038723" class="anchor"></span>Vector form: $`\widehat{y} = w^{T}x + b`$

- <span id="_Toc224038724" class="anchor"></span>SSE / RSS objective: $`{RSS}(w) = \sum_{i = 1}^{n}(t_{i} - w^{T}\phi\left( x_{i} \right))^{2}`$

- <span id="_Toc224038725" class="anchor"></span>Matrix least squares solution: $`w^{*} = (\Phi^{T}\Phi)^{- 1}\Phi^{T}t`$

- <span id="_Toc224038726" class="anchor"></span>Ridge-regularized objective: $`\sum_{i = 1}^{n}(t_{i} - w^{T}\phi\left( x_{i} \right))^{2} + \lambda \parallel w \parallel_{2}^{2}`$

## Helpful interpretations:

- <span id="_Toc224038728" class="anchor"></span>Design matrix $`\Phi`$ has one row per observation and one column per feature or basis function.

- <span id="_Toc224038729" class="anchor"></span>Least squares chooses the projection of $`t`$ onto the column space of $`\Phi`$.

- <span id="_Toc224038730" class="anchor"></span>Probabilistic model: $`t_{i} = w^{T}\phi\left( x_{i} \right) + \varepsilon_{i}`$ with $`\varepsilon_{i}\mathcal{\sim N}\left( 0,\sigma^{2} \right)`$.

**
**

# Optimization concepts

- Understand why optimization appears in model fitting.

- Distinguish:

  - analytic / closed-form solutions

  - iterative optimization

- Explain **gradient descent**:

  - initialization

  - gradient updates

  - learning rate / step size

  - convergence intuition

- Explain **stochastic gradient descent** and mini-batch reasoning.

- Know when iterative methods are needed instead of closed-form solutions.

## Core equations:

- <span id="_Toc224038733" class="anchor"></span>Gradient descent update: $`w^{\left( k+1 \right)} = w^{(k)} - \eta\nabla L\left( w^{(k)} \right)`$

- <span id="_Toc224038734" class="anchor"></span>SGD update: $`w \leftarrow w - \eta\nabla\mathcal{l}_{i}(w)`$ using one observation (or a mini-batch) at a time

## Key idea:

- <span id="_Toc224038736" class="anchor"></span>Closed-form solutions are exact algebraic formulas; iterative methods repeatedly improve parameters when no simple formula exists or when the data are too large for direct matrix methods.

**
**

# Logistic regression and classification

- Define logistic regression as a supervised classification method.

- Understand binary classification with the **sigmoid** / logistic function.

- Explain how logistic regression models $`P\left( Y = 1\mid X = x \right)`$.

- Understand **likelihood**, **log-likelihood**, and **negative log-likelihood**.

- Know that logistic regression is often trained by minimizing cross-entropy / logistic loss.

- Explain why logistic regression generally does **not** have a simple closed-form analytic solution.

- Connect logistic regression training to gradient-based optimization.

- Understand the derivative identity for the sigmoid.

- Explain issues with **linearly separable data** and why **regularization** is needed.

- Recognize one-vs-all / one-vs-rest classification and **softmax** multiclass classification.

## Core equations:

- <span id="_Toc224038739" class="anchor"></span>Logit score: $`z = w^{T}x + b`$

- <span id="_Toc224038740" class="anchor"></span>Sigmoid: $`\sigma(z) = \frac{1}{1 + e^{- z}}`$

- <span id="_Toc224038741" class="anchor"></span>Binary probability model: $`P\left( Y = 1\mid X = x \right) = \sigma\left( w^{T}x + b \right)`$

- <span id="_Toc224038742" class="anchor"></span>Sigmoid derivative: $`\sigma^{'}(z) = \sigma(z)\left( 1 - \sigma(z) \right)`$

- <span id="_Toc224038743" class="anchor"></span>Negative log-likelihood / cross-entropy:
  ``` math
  L(w,b) = - \sum_{i = 1}^{n}\left\lbrack y_{i}\log p_{i} + \left( 1 - y_{i} \right)\log\left( 1 - p_{i} \right) \right\rbrack,p_{i} = \sigma\left( w^{T}x_{i} + b \right)
  ```

- <span id="_Toc224038744" class="anchor"></span>Softmax for class $`k`$: $`P\left( Y = k\mid X = x \right) = \frac{e^{z_{k}}}{\sum_{j}^{}e^{z_{j}}}`$

## Important note:

- <span id="_Toc224038746" class="anchor"></span>Logistic regression usually has no closed-form minimizer for the cross-entropy loss, so it is fit numerically.

**
**

# Discriminative vs generative models

- Distinguish **discriminative** models from **generative** models.

- Understand:

  - discriminative models target $`P\left( Y\mid X \right)`$ directly

  - generative models work through joint or class-conditional structure such as $`P(X,Y)`$ or $`P\left( X\mid Y \right)P(Y)`$

- Use **Bayes rule** to connect class priors, class-conditionals, and posterior classification.

- Explain the **Bayes classifier** as the optimal classifier under the assumed model.

## Core equation:

- <span id="_Toc224038749" class="anchor"></span>Bayes rule: $`P\left( Y = k\mid X = x \right) = \frac{P\left( X = x\mid Y = k \right)P(Y = k)}{P(X = x)}`$

## Decision rule:

- <span id="_Toc224038751" class="anchor"></span>Bayes classifier predicts the class with the largest posterior probability:
  ``` math
  \widehat{y}(x) = \arg{\max_{k}P\left( Y = k\mid X = x \right)}
  ```

**
**

# Gaussian Bayes / generative classification

- Understand how Gaussian class-conditionals are used in classification.

- Explain class priors and class-conditional densities.

- Know that each class may have its own mean and covariance.

- Understand why decision boundaries can be quadratic in Gaussian Bayes classifiers.

- Recognize the parameter-estimation burden for generative models.

## Core density:

- If class $`k`$ is Gaussian, then
  ``` math
  p\left( x\mid Y = k \right) = \frac{1}{\left( 2\pi)^{\frac{p}{2}} \mid \Sigma_{k} \mid^{\frac{1}{2}} \right.\ }\exp\left( - \frac{1}{2}(x - \mu_{k})^{T}\Sigma_{k}^{- 1}(x - \mu_{k}) \right)
  ```

## Key interpretation:

- <span id="_Toc224038755" class="anchor"></span>If classes have different covariance matrices $`\Sigma_{k}`$, the discriminant function generally becomes quadratic in $`x`$.

**
**

# Conditional independence and Naive Bayes

- Define **conditional independence**.

- Explain the Naive Bayes assumption that features are independent given the class.

- Show how this simplifies the class-conditional probability into a product over features.

- Understand why Naive Bayes needs fewer parameters than a full generative model.

- Be prepared to discuss tradeoffs:

  - lower variance / less data demand

  - stronger assumptions that may be violated in practice

## Core definitions and equations:

- <span id="_Toc224038758" class="anchor"></span>Conditional independence means that given $`Y`$, knowing one feature gives no extra information about another feature.

- <span id="_Toc224038759" class="anchor"></span>Naive Bayes assumption:
  ``` math
  P(X_{1},\ldots,X_{p} \mid Y = k) = \prod_{j = 1}^{p}{P(}X_{j} \mid Y = k)
  ```

- <span id="_Toc224038760" class="anchor"></span>Posterior up to proportionality:
  ``` math
  P(Y = k \mid X = x) \propto P(Y = k)\prod_{j = 1}^{p}{P(}X_{j} = x_{j} \mid Y = k)
  ```

# Neural networks: big picture and core building blocks

- Explain how modern neural networks relate to earlier models like logistic regression.

- Understand neural nets as learning **feature maps** and then applying linear or logistic prediction on top.

- Explain why **nonlinearities** are essential.

- Understand **layers**, **units**, **weights**, **biases**, and **hierarchical feature learning**.

- Explain function composition and why stacking purely linear maps is not enough.

- Interpret layer computations in matrix form.

- Understand neural networks as nonlinear, hierarchical function approximators.

## Core equations:

- <span id="_Toc224038763" class="anchor"></span>One hidden layer network: $`h = g\left( W_{1}x + b_{1} \right)`$, then $`\widehat{y} = W_{2}h + b_{2}`$

- <span id="_Toc224038764" class="anchor"></span>For binary classification, often $`\widehat{p} = \sigma\left( W_{2}h + b_{2} \right)`$

## Key idea:

- <span id="_Toc224038766" class="anchor"></span>Without a nonlinear activation $`g`$, multiple layers collapse to one linear transformation, so depth would not buy you anything.

**
**

# Neural networks: extended vocabulary and architectures

## Know terms such as:

- logits

- softmax

- tensors

- attention

- spatio-temporal data

## Understand convolutional neural networks (CNNs):

- grid-structured inputs

- kernels / filters

- feature maps

- sparse interactions

- parameter sharing

- translation equivariance / shift handling

- pooling and its role

## Understand recurrent neural networks (RNNs):

- sequence modeling

- hidden state / memory

- parameter sharing across time

- unfolding through time

- teacher forcing

- outputs at each step vs one output after the full sequence

- why order matters for sequential data

## Quick definitions:

- <span id="_Toc224038772" class="anchor"></span>Logits are raw scores before sigmoid or softmax is applied.

- <span id="_Toc224038773" class="anchor"></span>Tensor is a multidimensional array.

- <span id="_Toc224038774" class="anchor"></span>Attention is a mechanism that lets a model weight which parts of the input are most relevant.

- <span id="_Toc224038775" class="anchor"></span>CNNs exploit local spatial structure through shared filters.

- <span id="_Toc224038776" class="anchor"></span>RNNs reuse the same parameters across time and update a hidden state sequentially.

**
**

# Validation, model assessment, and model selection

- Distinguish **training error** from **test / future prediction error**.

- Understand the goals of:

  - **model assessment**

  - **model selection**

- Explain the **bias-variance-noise** decomposition conceptually.

- Understand how model complexity affects bias and variance.

- Know the major validation methods:

  - test-set validation

  - leave-one-out cross-validation (LOOCV)

  - k-fold cross-validation

- Compare their pros and cons:

  - variance

  - computational cost

  - data efficiency

- Be able to explain why cross-validation is widely used.

## Core concepts:

- <span id="_Toc224038779" class="anchor"></span>Model assessment asks: how well does the chosen model generalize?

- <span id="_Toc224038780" class="anchor"></span>Model selection asks: which model complexity or tuning parameter should we choose?

## Important relationship:

- <span id="_Toc224038782" class="anchor"></span>In squared-error settings, a common conceptual decomposition is
  ``` math
  E\left\lbrack \left( Y - \widehat{f}(X) \right)^{2} \right\rbrack = {{Bias}\left( \widehat{f}(X) \right)}^{2} + {Var}\left( \widehat{f}(X) \right) + \sigma^{2}
  ```

  where $`\sigma^{2}`$ is irreducible noise.

## Cross-validation reminder:

- <span id="_Toc224038784" class="anchor"></span>LOOCV uses $`n`$ folds of size 1.

- <span id="_Toc224038785" class="anchor"></span>k-fold CV splits data into $`k`$ parts, trains on $`k - 1`$, validates on the held-out fold, and averages the results.

**
**

# Tree-based methods

- Understand decision trees for both **regression** and **classification**.

- Define:

  - predictor space / feature space

  - regions / boxes

  - splits

  - recursive binary splitting

  - terminal nodes / leaves

  - internal nodes

- Explain the top-down greedy tree-building process.

- For regression trees, understand use of **RSS** and mean response within a region.

- For classification trees, understand:

  - classification error rate

  - class proportions

  - node purity

  - **Gini index**

  - **cross-entropy / deviance**

- Explain **overfitting** in trees and the role of **pruning**.

- Understand **cost-complexity pruning** and the tuning parameter $`\alpha`$.

- Explain how **cross-validation** is used to choose tree complexity.

## Core equations:

- <span id="_Toc224038788" class="anchor"></span>Regression tree node prediction: average response in the region, $`{\widehat{y}}_{R} = \frac{1}{\mid R \mid}\sum_{i:x_{i} \in R}^{}y_{i}`$

- <span id="_Toc224038789" class="anchor"></span>RSS for a split: $`\sum_{m = 1}^{M}{\sum_{i:x_{i} \in R_{m}}^{}(}y_{i} - {\widehat{y}}_{R_{m}})^{2}`$

- <span id="_Toc224038790" class="anchor"></span>Gini index: $`G = 1 - \sum_{k = 1}^{K}{\widehat{p}}_{k}^{2}`$

- <span id="_Toc224038791" class="anchor"></span>Cross-entropy / deviance: $`D = - \sum_{k = 1}^{K}{\widehat{p}}_{k}\log{\widehat{p}}_{k}`$

- <span id="_Toc224038792" class="anchor"></span>Cost-complexity criterion: $`\sum_{m = 1}^{\mid T \mid}{\sum_{i:x_{i} \in R_{m}}^{}(}y_{i} - {\widehat{y}}_{R_{m}})^{2} + \alpha \mid T \mid`$

## Key idea:

- <span id="_Toc224038794" class="anchor"></span>Larger trees usually reduce training error but may increase test error, so pruning is used to control complexity.

**
**

# Ensemble tree methods

- Understand **bagging** as bootstrap aggregating.

- Explain bootstrap samples and why averaging many high-variance trees can reduce variance.

- Distinguish bagging behavior for:

  - regression trees (averaging predictions)

  - classification trees (majority vote)

- Understand **out-of-bag (OOB) error** as an internal estimate of test error.

- Recognize the tradeoff between predictive power and interpretability in ensembles.

- Expect **random forests** and **boosting** to be fair game conceptually, since they are explicitly named in the Week 9 overview.

## Quick definitions:

- <span id="_Toc224038797" class="anchor"></span>Bagging = fit many trees on bootstrap samples, then aggregate predictions.

- <span id="_Toc224038798" class="anchor"></span>Random forest = bagging plus random feature subsampling at each split.

- <span id="_Toc224038799" class="anchor"></span>Boosting = sequentially fit weak learners so later ones focus on earlier errors.

## Core aggregation rules:

- <span id="_Toc224038801" class="anchor"></span>Regression bagging: $`{\widehat{f}}_{\text{bag}}(x) = \frac{1}{B}\sum_{b = 1}^{B}{\widehat{f}}^{(b)}(x)`$

- Classification bagging: predict by majority vote across trees.

#  Conceptual comparisons that are especially exam-worthy

- supervised vs unsupervised learning

- regression vs classification

- linear vs nonlinear models

- analytic solution vs gradient-based optimization

- discriminative vs generative modeling

- Gaussian Bayes vs Naive Bayes

- logistic regression vs neural networks

- CNNs vs RNNs

- training error vs test error

- test-set validation vs LOOCV vs k-fold CV

- single decision trees vs bagging / random forests / boosting

**
**

# Formulas / relationships worth knowing cold

- <span id="_Toc224038804" class="anchor"></span>Linear regression: $`\widehat{y} = w^{T}x + b`$

- <span id="_Toc224038805" class="anchor"></span>Least squares: $`\sum_{i = 1}^{n}(y_{i} - {\widehat{y}}_{i})^{2}`$

- <span id="_Toc224038806" class="anchor"></span>Normal equation: $`w^{*} = (X^{T}X)^{- 1}X^{T}y`$

- <span id="_Toc224038807" class="anchor"></span>Sigmoid: $`\sigma(z) = \frac{1}{1 + e^{- z}}`$

- <span id="_Toc224038808" class="anchor"></span>Logistic regression loss:
  ``` math
  - \sum_{i = 1}^{n}\left\lbrack y_{i}\log p_{i} + \left( 1 - y_{i} \right)\log\left( 1 - p_{i} \right) \right\rbrack
  ```

- <span id="_Toc224038809" class="anchor"></span>Gradient descent: $`w \leftarrow w - \eta\nabla L(w)`$

- <span id="_Toc224038810" class="anchor"></span>Bayes rule: $`P\left( Y\mid X \right) = \frac{P\left( X\mid Y \right)P(Y)}{P(X)}`$

- <span id="_Toc224038811" class="anchor"></span>Naive Bayes: $`P(X \mid Y) = \prod_{j = 1}^{p}{P(}X_{j} \mid Y)`$

- <span id="_Toc224038812" class="anchor"></span>Bias-variance-noise: $`\mathbb{E}\lbrack(Y - \widehat{f}(X))^{2}\rbrack = \text{Bias}^{2} + \text{Var} + \sigma^{2}`$

- <span id="_Toc224038813" class="anchor"></span>Tree impurity:

  - RSS for regression trees

  - $`G = 1 - \sum_{k}^{}{\widehat{p}}_{k}^{2}`$ for Gini

  - $`D = - \sum_{k}^{}{\widehat{p}}_{k}\log{\widehat{p}}_{k}`$ for cross-entropy

**
**

# Practical interpretation / short-answer themes likely to appear

- when a method is appropriate

- what assumptions a method makes

- what kind of output it predicts

- how model complexity affects generalization

- how to evaluate predictive performance honestly

- how regularization helps prevent overfitting

- why neural networks need nonlinear activations

- why Naive Bayes can still work even when its independence assumption is imperfect

- why ensemble methods often outperform a single tree
