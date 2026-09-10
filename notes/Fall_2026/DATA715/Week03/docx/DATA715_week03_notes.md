> Markdown version for convenient browsing. Original files:
> - PDF: [DATA715_week03_notes.pdf](../DATA715_week03_notes.pdf)
> - DOCX: [DATA715_week03_notes.docx](DATA715_week03_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 15%" />
<col style="width: 8%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Advanced SQL Functionality 1</th>
<th></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Overview</td>
<td style="text-align: right;"><em>9 Sept 2026</em></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>apply advanced SQL functions</p></li>
<li><p>practice the basics of regular expressions</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
</tr>
<tr>
<td colspan="4">Subqueries and Aggregate Functions</td>
</tr>
<tr>
<td>Aggregate Functions With Group By</td>
<td colspan="3"><p><img src="generated_media\DATA715_week03_notes\media\image1.jpeg" style="width:4.84722in;height:3.63542in" /><strong>Aggregate functions summarize values across rows, and</strong> <span class="math inline"><strong>G</strong><strong>R</strong><strong>O</strong><strong>U</strong><strong>P</strong> <strong>B</strong><strong>Y</strong></span> <strong>allows the same calculation to be performed separately for defined groups.</strong></p>
<p>ChatGPT 5.6 Sol</p>
<ul>
<li><p>aggregate functions can calculate values for an entire table or for groups within a table</p></li>
<li><p>common aggregate functions:</p>
<ul>
<li><p><span class="math inline"><em>C</em><em>O</em><em>U</em><em>N</em><em>T</em>()</span></p></li>
<li><p><span class="math inline"><em>M</em><em>I</em><em>N</em>()</span></p></li>
<li><p><span class="math inline"><em>M</em><em>A</em><em>X</em>()</span></p></li>
<li><p><span class="math inline"><em>S</em><em>U</em><em>M</em>()</span></p></li>
<li><p><span class="math inline"><em>A</em><em>V</em><em>G</em>()</span></p></li>
</ul></li>
</ul>
<p><span class="math inline"><strong>G</strong><strong>R</strong><strong>O</strong><strong>U</strong><strong>P</strong> <strong>B</strong><strong>Y</strong></span><strong>:</strong></p>
<ul>
<li><p>divides rows into groups based on one or more specified columns</p></li>
<li><p>the aggregate function is then calculated independently for each group</p></li>
<li><p>example use case:</p>
<ul>
<li><p>count patients separately by gender rather than running a separate COUNT query for every gender</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Labeling Grouped Results</td>
<td colspan="3"><p><strong>Grouped aggregate results are easier to interpret when the grouping column is included in the</strong> <span class="math inline"><strong>S</strong><strong>E</strong><strong>L</strong><strong>E</strong><strong>C</strong><strong>T</strong></span> <strong>clause.</strong></p>
<ul>
<li><p>selecting only <span class="math inline"><em>C</em><em>O</em><em>U</em><em>N</em><em>T</em>(): </span></p>
<ul>
<li><p>returns the counts without identifying which group produced each value</p></li>
</ul></li>
<li><p>include the column used for grouping in <span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em></span> to label each result</p></li>
</ul>
<p><strong>Multiple columns can be included in</strong> <span class="math inline"><strong>G</strong><strong>R</strong><strong>O</strong><strong>U</strong><strong>P</strong> <strong>B</strong><strong>Y</strong></span><strong>.</strong></p>
<ul>
<li><p>grouping by gender and race produces one result for each existing gender-race combination</p></li>
</ul>
<p><span class="math inline"><strong>S</strong><strong>E</strong><strong>L</strong><strong>E</strong><strong>C</strong><strong>T</strong></span> <strong>And</strong> <span class="math inline"><strong>G</strong><strong>R</strong><strong>O</strong><strong>U</strong><strong>P</strong> <strong>B</strong><strong>Y</strong></span> <strong>Requirements.</strong></p>
<ul>
<li><p>when aggregate functions are combined with ordinary columns:</p>
<ul>
<li><p>the non-aggregate columns in <span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em></span> must also appear in <span class="math inline"><em>G</em><em>R</em><em>O</em><em>U</em><em>P</em> <em>B</em><em>Y</em></span></p></li>
</ul></li>
</ul>
<p><span class="math inline"><strong>G</strong><strong>R</strong><strong>O</strong><strong>U</strong><strong>P</strong> <strong>B</strong><strong>Y</strong></span> <strong>is not required when</strong> <span class="math inline"><strong>S</strong><strong>E</strong><strong>L</strong><strong>E</strong><strong>C</strong><strong>T</strong></span> <strong>contains only aggregate functions.</strong></p>
<ul>
<li><p>if SELECT contains an aggregate function and another column:</p>
<ul>
<li><p>that additional column must also appear in GROUP BY</p></li>
</ul></li>
</ul>
<p><strong>A common aggregate-query error is forgetting to match non-aggregate</strong> <span class="math inline"><strong>S</strong><strong>E</strong><strong>L</strong><strong>E</strong><strong>C</strong><strong>T</strong></span> <strong>columns with the</strong> <span class="math inline"><strong>G</strong><strong>R</strong><strong>O</strong><strong>U</strong><strong>P</strong> <strong>B</strong><strong>Y</strong></span> <strong>clause,</strong></p></td>
</tr>
<tr>
<td>Distinct Values</td>
<td colspan="3"><p><span class="math inline"><strong>D</strong><strong>I</strong><strong>S</strong><strong>T</strong><strong>I</strong><strong>N</strong><strong>C</strong><strong>T</strong></span> <strong>allows aggregate functions to operate on unique values rather than simply counting every row.</strong></p>
<ul>
<li><p><span class="math inline"><em>C</em><em>O</em><em>U</em><em>N</em><em>T</em>(*)</span>:</p>
<ul>
<li><p>counts rows regardless of duplicated values</p></li>
</ul></li>
<li><p><span class="math inline"><em>C</em><em>O</em><em>U</em><em>N</em><em>T</em>(<strong>D</strong><strong>I</strong><strong>S</strong><strong>T</strong><strong>I</strong><strong>N</strong><strong>C</strong><strong>T</strong> <em>c</em><em>o</em><em>l</em><em>u</em><em>m</em><em>n</em>)</span>:</p>
<ul>
<li><p>counts the number of unique values in the specified column</p></li>
</ul></li>
</ul>
<p><span class="math inline"><strong>D</strong><strong>I</strong><strong>S</strong><strong>T</strong><strong>I</strong><strong>N</strong><strong>C</strong><strong>T</strong></span> <strong>is useful when the question concerns unique entities or values rather than total records.</strong></p></td>
</tr>
<tr>
<td>Limitations Of Grouping</td>
<td colspan="3"><p><strong><em>GROUP BY</em> can become restrictive when the desired output includes a value associated with an aggregate result.</strong></p>
<ul>
<li><p>example:</p>
<ul>
<li><p>finding a patient's most recent weight</p></li>
</ul></li>
<li><p><span class="math inline"><em>M</em><em>A</em><em>X</em>(<em>w</em><em>e</em><em>i</em><em>g</em><em>h</em><em>t</em>_<em>d</em><em>a</em><em>t</em><em>e</em>)</span>:</p>
<ul>
<li><p>can identify the most recent measurement date</p></li>
</ul></li>
<li><p>Including patient_id is possible by grouping on patient_id</p></li>
<li><p>including the corresponding weight value:</p>
<ul>
<li><p>creates a problem because weight would also need to be added to <span class="math inline"><em>G</em><em>R</em><em>O</em><em>U</em><em>P</em> <em>B</em><em>Y</em></span></p></li>
</ul></li>
<li><p>grouping by weight:</p>
<ul>
<li><p>changes the grouping structure and no longer answers the original question</p></li>
</ul></li>
</ul>
<p><strong>The requirement is not merely to find the maximum date but to retrieve the row associated with that date.</strong></p></td>
</tr>
<tr>
<td>Subqueries</td>
<td colspan="3"><p><strong>A subquery, also called a nested query, places one SQL query inside another query.</strong></p>
<ul>
<li><p>the result of a SQL query:</p>
<ul>
<li><p>a table</p></li>
<li><p>or relation</p></li>
</ul></li>
<li><p>query results:</p>
<ul>
<li><p>usually temporary</p></li>
<li><p>exist only while the query is being executed</p></li>
</ul></li>
</ul>
<p><strong>A temporary query result can still be used as a data source within another query.</strong></p>
<ul>
<li><p>the inner query:</p>
<ul>
<li><p>enclosed in parentheses</p></li>
</ul></li>
<li><p>the subquery result:</p>
<ul>
<li><p>assigned a name or alias</p></li>
<li><p>allows the outer query to reference it like another table</p></li>
</ul></li>
<li><p>once named</p>
<ul>
<li><p>the subquery result can participate in operations such as joins</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Most Recent Weight Example</td>
<td colspan="3"><p><strong>The solution separates the problem into two logical stages.</strong></p>
<ul>
<li><p>inner query:</p>
<ul>
<li><p>calculate <span class="math inline"><em>M</em><em>A</em><em>X</em>(<em>w</em><em>e</em><em>i</em><em>g</em><em>h</em><em>t</em>_<em>d</em><em>a</em><em>t</em><em>e</em>)</span> for each patient</p></li>
<li><p>group the calculation by patient_id</p></li>
<li><p>return patient_id and the corresponding maximum date</p></li>
<li><p>assign the resulting temporary table a name such as patient_max_date</p></li>
</ul></li>
</ul>
<p>SELECT</p>
<p>PATIENT_ID,</p>
<p>WEIGHT,</p>
<p>WEIGHT_DATE</p>
<p>FROM</p>
<p>PatientWt wt,</p>
<p>(SELECT</p>
<p>PATIENT_ID,</p>
<p>MAX(WEIGHT_DATE) AS MaxDt</p>
<p>FROM</p>
<p>PatientWt</p>
<p>GROUP BY</p>
<p>PATIENT_ID) PatMaxDt</p>
<p>WHERE</p>
<p>wt.PATIENT_ID = PatMaxDt.PATIENT_ID</p>
<p>AND wt.WEIGHT_DATE = PatMaxDt.MaxDt</p>
<p>outer query</p>
<p>inner query</p>
<ul>
<li><p>outer query:</p>
<ul>
<li><p>use the original patient-weight table together with patient_max_date</p></li>
<li><p>join the temporary result back to the original table</p></li>
<li><p>retrieve the weight value associated with the maximum date</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Join Conditions</td>
<td colspan="3"><p><strong>The outer query must match the subquery result to the correct row in the original table.</strong></p>
<ul>
<li><p>join on patient_id to ensure the result belongs to the correct patient</p></li>
<li><p>join on weight_date and the calculated maximum date to identify the patient's most recent measurement row</p></li>
<li><p>both conditions are necessary because many patients and many measurement dates may exist in the original table</p></li>
</ul></td>
</tr>
<tr>
<td>Why The Approach Works</td>
<td colspan="3"><p><strong>The aggregation is completed inside the subquery before the outer query retrieves the remaining values.</strong></p>
<ul>
<li><p>the subquery:</p>
<ul>
<li><p>reduces each patient's measurements to the relevant maximum date</p></li>
</ul></li>
<li><p>the outer query:</p>
<ul>
<li><p>no longer needs to perform the aggregation</p></li>
<li><p>can therefore select patient_id, weight_date, and weight without adding weight to GROUP BY</p></li>
</ul></li>
</ul>
<p><strong>This allows the query to return values from the specific row identified by the aggregate calculation.</strong></p></td>
</tr>
<tr>
<td>Subquery Tradeoff</td>
<td colspan="3"><p><strong>Subqueries provide a powerful way to break complex SQL problems into intermediate results, but deeply nested queries can become difficult to read.</strong></p>
<ul>
<li><p>multiple nested subqueries:</p>
<ul>
<li><p>can produce many layers of parentheses and temporary results</p></li>
</ul></li>
<li><p>later techniques:</p>
<ul>
<li><p>can provide cleaner ways to organize queries containing many intermediate calculations</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Key Ideas</td>
<td colspan="3"><p><strong>Aggregate functions summarize sets of rows.</strong></p>
<ul>
<li><p><span class="math inline"><strong>G</strong><em>R</em><em>O</em><em>U</em><em>P</em> <em>B</em><em>Y</em> </span></p>
<ul>
<li><p>determines the groups over which aggregate functions operate</p></li>
</ul></li>
<li><p>subqueries</p>
<ul>
<li><p>allow the result of one query to become an intermediate relation used by another query</p></li>
<li><p>especially useful when an aggregate identifies a row and additional values from that same row must be retrieved</p></li>
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
<th colspan="2">Set Operations</th>
</tr>
</thead>
<tbody>
<tr>
<td>Boolean Logic Refresher</td>
<td><p><strong>Boolean logic determines whether each tuple satisfies the conditions in a query.</strong></p>
<p><span class="math inline"><strong>A</strong><strong>N</strong><strong>D</strong></span><strong>:</strong></p>
<ul>
<li><p>true only when both conditions are true</p></li>
</ul>
<p><span class="math inline"><strong>O</strong><strong>R</strong></span><strong>:</strong></p>
<ul>
<li><p>true when either condition or both conditions are true</p></li>
</ul>
<p><span class="math inline"><strong>N</strong><strong>O</strong><strong>T</strong></span><strong>:</strong></p>
<ul>
<li><p>reverses the result of a condition</p></li>
</ul>
<p><strong>During selection, each tuple is evaluated and retained only when the condition evaluates to true.</strong></p></td>
</tr>
<tr>
<td>Core Set Operations</td>
<td><p><strong>Set operations combine the results of multiple relational queries.</strong></p>
<p><span class="math inline"><strong>U</strong><strong>N</strong><strong>I</strong><strong>O</strong><strong>N</strong></span> <strong>:</strong></p>
<ul>
<li><p>combines all tuples from both result sets</p></li>
</ul>
<p><span class="math inline"><strong>I</strong><strong>N</strong><strong>T</strong><strong>E</strong><strong>R</strong><strong>S</strong><strong>E</strong><strong>C</strong><strong>T</strong></span><strong>:</strong></p>
<ul>
<li><p>keeps only tuples that appear in both result sets</p></li>
</ul>
<p><span class="math inline"><strong>E</strong><strong>X</strong><strong>C</strong><strong>E</strong><strong>P</strong><strong>T</strong></span> <strong>or</strong> <span class="math inline"><strong>M</strong><strong>I</strong><strong>N</strong><strong>U</strong><strong>S</strong></span><strong>:</strong></p>
<ul>
<li><p>keeps tuples from the first result set that do not appear in the second</p></li>
</ul>
<p><strong>These operations correspond closely to Boolean</strong> <span class="math inline"><strong>O</strong><strong>R</strong></span><strong>,</strong> <span class="math inline"><strong>A</strong><strong>N</strong><strong>D</strong></span><strong>, and</strong> <span class="math inline"><strong>N</strong><strong>O</strong><strong>T</strong></span> <strong>logic,</strong></p></td>
</tr>
<tr>
<td>Relational Algebra Connection</td>
<td><p><strong>Relational algebra provides the mathematical foundation for the relational model and can represent the same operations expressed in SQL.</strong></p>
<ul>
<li><p>projection operator:</p>
<ul>
<li><p>represents selecting attributes or columns</p></li>
</ul></li>
<li><p>selection conditions:</p>
<ul>
<li><p>correspond to filtering performed by a <span class="math inline"><em>W</em><em>H</em><em>E</em><em>R</em><em>E</em></span> clause</p></li>
</ul></li>
<li><p>relation inside the expression:</p>
<ul>
<li><p>represents the source table</p></li>
</ul></li>
</ul>
<p><strong>Set operators can then combine the results of complete relational expressions.</strong></p></td>
</tr>
<tr>
<td>UNION</td>
<td><p><span class="math inline"><strong>U</strong><strong>N</strong><strong>I</strong><strong>O</strong><strong>N</strong></span> <strong>is used when rows satisfying either of two query conditions should appear in the final result.</strong></p>
<ul>
<li><p>example question:</p>
<ul>
<li><p>find patients who are age 18 or older or have an overdue billing status</p></li>
</ul></li>
</ul>
<p><strong>First query:</strong></p>
<ul>
<li><p>select the desired patient attributes from the patient table where age is at least 18</p></li>
</ul>
<p><strong>Second query:</strong></p>
<ul>
<li><p>select the same attributes from the billing table where billing status is overdue</p></li>
</ul>
<p><span class="math inline"><strong>U</strong><strong>N</strong><strong>I</strong><strong>O</strong><strong>N</strong></span><strong>:</strong></p>
<ul>
<li><p>combines the two result sets into one final relation</p></li>
<li><p>a tuple is retained if it appears in:</p>
<ul>
<li><p>the first result</p></li>
<li><p>the second result</p></li>
<li><p>both</p></li>
</ul></li>
</ul>
<p><strong>More than two query results can be combined with</strong> <span class="math inline"><strong>U</strong><strong>N</strong><strong>I</strong><strong>O</strong><strong>N</strong></span><strong>.</strong></p></td>
</tr>
<tr>
<td>UNION And Duplicate Rows</td>
<td><p><span class="math inline"><strong>U</strong><strong>N</strong><strong>I</strong><strong>O</strong><strong>N</strong></span> <strong>removes duplicate tuples automatically.</strong></p>
<ul>
<li><p>if the same tuple appears in both result sets:</p>
<ul>
<li><p>it appears only once in the <span class="math inline"><em>U</em><em>N</em><em>I</em><em>O</em><em>N</em></span> result</p></li>
</ul></li>
</ul>
<p><span class="math inline"><strong>U</strong><strong>N</strong><strong>I</strong><strong>O</strong><strong>N</strong> <strong>A</strong><strong>L</strong><strong>L</strong></span><strong>:</strong></p>
<ul>
<li><p>preserves duplicate tuples</p></li>
</ul>
<p><strong>Use</strong> <span class="math inline"><strong>U</strong><strong>N</strong><strong>I</strong><strong>O</strong><strong>N</strong> <strong>A</strong><strong>L</strong><strong>L</strong> </span><strong>when duplicate rows are meaningful and should remain in the result.</strong></p></td>
</tr>
<tr>
<td>Union Compatibility</td>
<td><p><strong>Queries must be union compatible before their results can be combined.</strong></p>
<ul>
<li><p>each query must return the same number of columns</p></li>
<li><p>corresponding columns must have compatible data types</p></li>
<li><p>column names do not have to be identical</p></li>
<li><p>the position and type of the returned attributes must align</p></li>
</ul>
<p><strong>Mismatched column counts or incompatible types are common causes of</strong> <span class="math inline"><strong>U</strong><strong>N</strong><strong>I</strong><strong>O</strong><strong>N</strong></span> <strong>errors.</strong></p></td>
</tr>
<tr>
<td>INTERSECT</td>
<td><p><span class="math inline"><strong>I</strong><strong>N</strong><strong>T</strong><strong>E</strong><strong>R</strong><strong>S</strong><strong>E</strong><strong>C</strong><strong>T</strong></span> <strong>returns only tuples that appear in both query results.</strong></p>
<ul>
<li><p>example question:</p>
<ul>
<li><p>find patients who are age 18 or older and also have an overdue billing status</p></li>
</ul></li>
</ul>
<p><strong>First query:</strong></p>
<ul>
<li><p>identifies patients meeting the age condition</p></li>
</ul>
<p><strong>Second query:</strong></p>
<ul>
<li><p>identifies patients meeting the billing condition</p></li>
</ul>
<p><span class="math inline"><strong>I</strong><strong>N</strong><strong>T</strong><strong>E</strong><strong>R</strong><strong>S</strong><strong>E</strong><strong>C</strong><strong>T</strong></span><strong>:</strong></p>
<ul>
<li><p>retains only patients present in both result sets</p></li>
</ul>
<p><span class="math inline"><strong>I</strong><strong>N</strong><strong>T</strong><strong>E</strong><strong>R</strong><strong>S</strong><strong>E</strong><strong>C</strong><strong>T</strong></span> <strong>therefore corresponds to Boolean</strong> <span class="math inline"><strong>A</strong><strong>N</strong><strong>D</strong></span> <strong>logic.</strong></p></td>
</tr>
<tr>
<td>EXCEPT And MINUS</td>
<td><p><span class="math inline"><strong>E</strong><strong>X</strong><strong>C</strong><strong>E</strong><strong>P</strong><strong>T</strong></span> <strong>or</strong> <span class="math inline"><strong>M</strong><strong>I</strong><strong>N</strong><strong>U</strong><strong>S</strong></span> <strong>returns tuples from the first result set that are not present in the second result set.</strong></p>
<ul>
<li><p>example question:</p>
<ul>
<li><p>find patients who are age 18 or older and do not have an overdue billing status</p></li>
</ul></li>
</ul>
<p><strong>First query:</strong></p>
<ul>
<li><p>identifies patients meeting the age condition</p></li>
</ul>
<p><strong>Second query:</strong></p>
<ul>
<li><p>identifies patients with overdue bills</p></li>
</ul>
<p><strong>EXCEPT:</strong></p>
<ul>
<li><p>removes tuples from the first result that also appear in the second</p></li>
<li><p>rows that exist only in the second result do not affect the final output</p></li>
</ul>
<p><strong>The order of the result sets matters because subtraction is directional.</strong></p></td>
</tr>
<tr>
<td>Set Operations In SQL</td>
<td><p><strong>Set operations can be placed directly between compatible SQL queries.</strong></p>
<ul>
<li><p>general pattern:</p>
<ul>
<li><p>first <span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em></span> query</p></li>
<li><p><em>UNION</em>, <em>INTERSECT</em>, or <em>EXCEPT</em></p></li>
<li><p>second <em>SELECT</em> query</p></li>
</ul></li>
</ul>
<p><strong>The operator determines how the two result sets are combined.</strong></p></td>
</tr>
<tr>
<td>Set Operations Versus Joins</td>
<td><p><strong>Set operations and joins combine relational data in different ways.</strong></p>
<ul>
<li><p>joins:</p>
<ul>
<li><p>primarily combine columns from different tables</p></li>
</ul></li>
<li><p>set operations:</p>
<ul>
<li><p>primarily combine rows from different query results</p></li>
</ul></li>
<li><p><span class="math inline"><em>I</em><em>N</em><em>T</em><em>E</em><em>R</em><em>S</em><em>E</em><em>C</em><em>T</em></span>:</p>
<ul>
<li><p>can often express logic similar to an <em>INNER</em> <em>JOIN</em></p></li>
</ul></li>
<li><p><em>EXCEPT</em> or <em>MINUS</em>:</p>
<ul>
<li><p>can often be represented using an anti-join</p></li>
</ul></li>
<li><p><em>UNION</em>:</p>
<ul>
<li><p>has no equivalent join operation because its purpose is to append compatible rows from separate result sets</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Key Relationships</td>
<td><ul>
<li><p><span class="math inline"><em>U</em><em>N</em><em>I</em><em>O</em><em>N</em></span> corresponds to <em>OR</em></p></li>
<li><p><em>INTERSECT</em> corresponds to <em>AND</em></p></li>
<li><p><em>EXCEPT</em> or <em>MINUS</em> corresponds to <em>NOT</em> or set subtraction</p></li>
<li><p><em>UNION</em> combines rows from either result</p></li>
<li><p><em>INTERSECT</em> keeps rows common to both results</p></li>
<li><p><em>EXCEPT</em> keeps rows from the first result that are absent from the second</p></li>
</ul>
<p><img src="generated_media\DATA715_week03_notes\media\image2.jpeg" style="width:4.84375in;height:3.22917in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p><strong>Set operations require compatible result structures and operate on complete query result sets.</strong></p></td>
</tr>
<tr>
<td colspan="2">CASE Statements</td>
</tr>
<tr>
<td>Purpose Of CASE Statements</td>
<td><p><strong>CASE statements allow SQL to transform existing values into derived categories.</strong></p>
<ul>
<li><p>continuous or highly specific values can be converted into broader categorical variables</p>
<ul>
<li><p>individual ages can be grouped into ranges</p>
<ul>
<li><p>for instance:</p>
<ul>
<li><p><span class="math inline">0 − 18</span></p></li>
<li><p><span class="math inline">19 − 35</span></p></li>
<li><p><span class="math inline">36 − 50</span></p></li>
</ul></li>
</ul></li>
</ul></li>
<li><p>common applications include analyzing age groups associated with:</p>
<ul>
<li><p>clinic visits</p></li>
<li><p>diseases</p></li>
<li><p>procedures</p></li>
<li><p>other outcomes</p></li>
</ul></li>
</ul>
<p><strong>Categorical age groups can make analysis easier when the goal is to compare populations rather than individual ages.</strong></p>
<p><strong>Step 1: Calculate Age</strong></p>
<ul>
<li><p>before creating age categories:</p>
<ul>
<li><p>the patient's age must first be calculated from the date of birth</p></li>
<li><p>age is derived by comparing the person's birth date with the current date</p></li>
<li><p>the exact calculation syntax depends on the database management system</p></li>
<li><p>date and datetime values may require conversion so that compatible data types are used in the calculation</p></li>
</ul></li>
<li><p>the resulting age:</p>
<ul>
<li><p>should represent completed years rather than conventional numerical rounding</p></li>
<li><p>a person remains age <span class="math inline">64</span> until their 65th birthday even when their calculated age is <span class="math inline">64.9</span></p></li>
<li><p>the lecture uses <span class="math inline"><em>F</em><em>L</em><em>O</em><em>O</em><em>R</em>()</span> to remove the decimal portion and round the calculated value downward</p></li>
</ul></li>
<li><p>the calculated field can be assigned an alias such as age</p></li>
</ul>
<p>Step 2: Examine The Age Distribution</p>
<ul>
<li><p>category boundaries should be informed by the underlying data</p>
<ul>
<li><p>calculate age for the full population</p></li>
</ul></li>
<li><p><span class="math inline"><strong>C</strong><strong>O</strong><strong>U</strong><strong>N</strong><strong>T</strong><strong>(</strong><strong>)</strong></span><strong>:</strong></p>
<ul>
<li><p>the number of people at each age</p></li>
</ul></li>
<li><p><span class="math inline"><strong>G</strong><strong>R</strong><strong>O</strong><strong>U</strong><strong>P</strong> <strong>B</strong><strong>Y</strong></span><strong>:</strong></p>
<ul>
<li><p>the calculated age so each age receives its own count</p></li>
</ul></li>
<li><p><span class="math inline"><strong>O</strong><strong>R</strong><strong>D</strong><strong>E</strong><strong>R</strong> <strong>B</strong><strong>Y</strong></span><strong>:</strong></p>
<ul>
<li><p>age to make the distribution easier to inspect</p></li>
</ul></li>
<li><p>review the distribution before deciding where meaningful category boundaries should be placed</p></li>
<li><p>real datasets may contain:</p>
<ul>
<li><p>peaks</p></li>
<li><p>gaps</p></li>
<li><p>uneven concentrations across different ages</p></li>
</ul></li>
</ul>
<p><strong>Step 3: Define Categories With</strong> <span class="math inline"><strong>C</strong><strong>A</strong><strong>S</strong><strong>E</strong></span></p>
<ul>
<li><p><span class="math inline"><em>C</em><em>A</em><em>S</em><em>E</em></span> statement:</p>
<ul>
<li><p>evaluates conditions in sequence</p></li>
<li><p>returns a specified value when a condition is satisfied</p></li>
</ul></li>
<li><p>general structure:</p></li>
</ul>
<p>CASE</p>
<p>WHEN condition THEN result</p>
<p>WHEN condition THEN result</p>
<p>ELSE result</p>
<p>END</p>
<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th><strong>WHEN</strong></th>
<th>defines a condition to test</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>THEN</strong></td>
<td>specifies the value assigned when that condition is true</td>
</tr>
<tr>
<td><strong>additional WHEN clauses</strong></td>
<td>define additional categories</td>
</tr>
<tr>
<td><strong>ELSE</strong></td>
<td>provides a value for records that do not satisfy any previous condition</td>
</tr>
<tr>
<td><strong>END</strong></td>
<td>closes the CASE statement</td>
</tr>
</tbody>
</table>
<ul>
<li><p>the complete <span class="math inline"><strong>C</strong><strong>A</strong><strong>S</strong><strong>E</strong></span> expression can be assigned an alias such as age_group</p></li>
<li><p>Why <span class="math inline"><em>E</em><em>L</em><em>S</em><em>E</em></span> Matters</p>
<ul>
<li><p><em>ELSE</em> acts as the catch-all condition in a <em>CASE</em> statement</p></li>
<li><p>records that do not satisfy any <em>WHEN</em> condition still need a valid outcome</p></li>
<li><p>without an appropriate catch-all category, some values may not receive the intended classification</p></li>
</ul></li>
</ul>
<p><strong>Step 4: Count Records Within Each Category</strong></p>
<ul>
<li><p>once the categorical variable has been created</p>
<ul>
<li><p><strong>aggregate functions</strong> can summarize the new groups</p></li>
</ul></li>
<li><p>when individual records are no longer needed</p>
<ul>
<li><p>remove person_id</p></li>
</ul></li>
<li><p>use <em>COUNT(*)</em></p>
<ul>
<li><p>to calculate the number of people assigned to each age group</p></li>
</ul></li>
<li><p>retain the <em>CASE</em> expression</p>
<ul>
<li><p>it defines the categorical variable being analyzed</p></li>
</ul></li>
<li><p><em>GROUP</em> <em>BY</em> the age group</p>
<ul>
<li><p>ensures one count is returned for each category</p></li>
</ul></li>
</ul>
<p><strong>The result provides a frequency distribution across the newly created categorical variable.</strong></p></td>
</tr>
<tr>
<td>Grouping By A SELECT Position</td>
<td><p><strong>SQL can sometimes reference expressions by their position in the</strong> <span class="math inline"><strong>S</strong><strong>E</strong><strong>L</strong><strong>E</strong><strong>C</strong><strong>T</strong></span> <strong>list.</strong></p>
<ul>
<li><p><span class="math inline"><strong>G</strong><strong>R</strong><strong>O</strong><strong>U</strong><strong>P</strong> <strong>B</strong><strong>Y</strong> <strong>1</strong> </span></p>
<ul>
<li><p>group by the first expression in <span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em></span></p></li>
<li><p>this can avoid repeating a long <span class="math inline"><em>C</em><em>A</em><em>S</em><em>E</em></span> expression inside the <span class="math inline"><em>G</em><em>R</em><em>O</em><em>U</em><em>P</em> <em>B</em><em>Y</em> </span>clause</p></li>
</ul></li>
<li><p><span class="math inline"><strong>O</strong><strong>R</strong><strong>D</strong><strong>E</strong><strong>R</strong> <strong>B</strong><strong>Y</strong> </span></p>
<ul>
<li><p>can use the same positional shorthand</p></li>
</ul></li>
<li><p><span class="math inline"><strong>G</strong><strong>R</strong><strong>O</strong><strong>U</strong><strong>P</strong> <strong>B</strong><strong>Y</strong> <strong>1</strong></span></p>
<ul>
<li><p>is especially convenient when the first selected value is a complex calculated expression</p></li>
</ul></li>
<li><p><strong>positional references</strong></p>
<ul>
<li><p>improve brevity but require awareness of the <span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em></span> column order</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Overall Transformation</td>
<td><p><strong>The workflow converts raw data into an analysis-ready categorical variable.</strong></p>
<p><img src="generated_media\DATA715_week03_notes\media\image3.jpeg" style="width:4.84306in;height:3.63194in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p>begin with a continuous or detailed source value</p>
<ul>
<li><p>derive the value needed for analysis, such as age</p></li>
<li><p>inspect its distribution</p></li>
<li><p>define meaningful category boundaries</p></li>
<li><p>use <span class="math inline"><em>C</em><em>A</em><em>S</em><em>E</em></span> to assign each record to a category</p></li>
<li><p>use <span class="math inline"><em>G</em><em>R</em><em>O</em><em>U</em><em>P</em> <em>B</em><em>Y</em></span> and <span class="math inline"><em>C</em><em>O</em><em>U</em><em>N</em><em>T</em>()</span> to summarize the categories</p></li>
</ul>
<p><strong>The result is a categorical representation that can be used for further analysis.</strong></p></td>
</tr>
<tr>
<td>Key Ideas</td>
<td><ul>
<li><p><span class="math inline"><strong>C</strong><strong>A</strong><strong>S</strong><strong>E</strong></span> provides conditional logic within a SQL query</p></li>
<li><p><span class="math inline"><strong>C</strong><strong>A</strong><strong>S</strong><strong>E</strong></span> can transform continuous or detailed data into categorical variables</p></li>
<li><p><span class="math inline"><strong>W</strong><strong>H</strong><strong>E</strong><strong>N</strong></span> and <em><strong>THEN</strong></em> define individual classification rules</p></li>
<li><p><em><strong>ELSE</strong></em> handles values that do not match earlier conditions</p></li>
<li><p><em><strong>END</strong></em> completes the <em><strong>CASE</strong></em> expression</p></li>
<li><p><em><strong>category</strong></em> <em><strong>design</strong></em> should be informed by the distribution and purpose of the data</p></li>
<li><p><em><strong>aggregate</strong></em> <em><strong>functions</strong></em> can summarize records after <em><strong>CASE</strong></em> creates the categories</p></li>
<li><p><em><strong>GROUP</strong></em> <em><strong>BY</strong></em> <em><strong>1</strong></em> can provide shorthand for grouping by a complex first <em><strong>SELECT</strong></em> expression</p></li>
</ul></td>
</tr>
<tr>
<td>CASTing</td>
<td><p><strong>Sometimes you want to work with data in a format other than its native format.</strong></p>
<ul>
<li><p><span class="math inline"><em>C</em><em>A</em><em>S</em><em>T</em></span></p>
<ul>
<li><p>convert from one datatype to another on the fly</p></li>
</ul></li>
<li><p>example:</p></li>
</ul>
<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th><strong>Field1</strong></th>
<th><strong>Field2</strong></th>
<th><strong>Field3</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>varchar</td>
<td>integer</td>
<td>numeric</td>
</tr>
<tr>
<td>123</td>
<td>987</td>
<td>5.6523</td>
</tr>
<tr>
<td>456</td>
<td>654</td>
<td>9.6701</td>
</tr>
<tr>
<td>789</td>
<td>321</td>
<td>10.8711</td>
</tr>
</tbody>
</table>
<ul>
<li><p>the concatenate function is not designed to work with numeric data types</p>
<ul>
<li><p><strong>Field1</strong> is varchar datatype</p></li>
<li><p><strong>Field2</strong> is an integer</p></li>
</ul></li>
</ul>
<p>--this query would error out<br />
SELECT Field1 || Field2 FROM TABLE;<br />
<br />
--this query would run successfully<br />
SELECT Field1 || CAST(Field2 AS VARCHAR) FROM TABLE;</p>
<ul>
<li><p>casting may also have unintended consequences, so be cautious</p></li>
<li><p>Field3</p>
<ul>
<li><p>numeric datatype</p></li>
<li><p>four digits to the right of the decimal</p></li>
</ul></li>
<li><p>What would happen if I CAST Field3 as an integer, which by definition has no floating point?</p></li>
</ul>
<p>--casting Field3 to an integer</p>
<p>SELECT CAST</p>
<p>Field3 AS INTEGER) AS Field3_int</p>
<p>FROM TABLE</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><strong>Field3_int</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>integer</td>
</tr>
<tr>
<td>5</td>
</tr>
<tr>
<td>9</td>
</tr>
<tr>
<td>10</td>
</tr>
</tbody>
</table>
<ul>
<li><p>note that the digits after the decimals have dropped off after the cast is performed</p></li>
<li><p>so, if you perform a cast like this, just make sure that this is the behavior you want!</p></li>
</ul>
<p><strong>There is a shortcut for the cast function--these two statements are equivalent:</strong></p>
<p>--use two colons to replace the full cast syntax</p>
<p>SELECT CAST</p>
<p>(Field3 AS INTEGER) AS Field3_int</p>
<p>FROM TABLE ;</p>
<p>SELECT</p>
<p>Field3::INTEGER AS Field3_int</p>
<p>FROM TABLE ;</p>
<ul>
<li><p>Note: you cannot cast whatever you want</p>
<ul>
<li><p>cast('ABC' as integer) will always result in an error</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>MariaDB Note</td>
<td><p><strong>The lecture demonstrates a PostgreSQL-specific method for calculating age, so that portion should not be copied directly into MariaDB.</strong></p>
<ul>
<li><p>in MariaDB, completed age in years can be calculated directly with TIMESTAMPDIFF()</p>
<ul>
<li><p><span class="math inline"><em>T</em><em>I</em><em>M</em><em>E</em><em>S</em><em>T</em><em>A</em><em>M</em><em>P</em><em>D</em><em>I</em><em>F</em><em>F</em>(<em>Y</em><em>E</em><em>A</em><em>R</em>, <em>b</em><em>i</em><em>r</em><em>t</em><em>h</em>_<em>d</em><em>a</em><em>t</em><em>e</em><em>t</em><em>i</em><em>m</em><em>e</em>, <em>C</em><em>U</em><em>R</em><em>D</em><em>A</em><em>T</em><em>E</em>())</span></p></li>
</ul></li>
<li><p>this already returns the number of completed year boundaries</p></li>
<li><p>the FLOOR() and division-by-365.25 approach from the PostgreSQL demonstration is unnecessary for the MariaDB version</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Fun With Dates</td>
</tr>
<tr>
<td>Why Dates Are Complicated</td>
<td><p><strong>Dates can be difficult to work with because the same date can be represented in many different formats.</strong></p>
<ul>
<li><p>examples:</p>
<ul>
<li><p>June 1, 2023</p></li>
<li><p>2023-01-06</p></li>
<li><p>6/1/2023</p></li>
<li><p>1 June 2023</p></li>
</ul></li>
<li><p>different relational database management systems may use different default date formats</p>
<ul>
<li><p>common default format</p>
<ul>
<li><p>YYYY-MM-DD</p></li>
</ul></li>
<li><p>Oracle commonly uses</p>
<ul>
<li><p>DD-Mon-YY</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>Differences in date formatting can create interoperability problems when data moves between systems.</strong></p></td>
</tr>
<tr>
<td>Importing Data With Dates</td>
<td><p><strong>Date values may need to be transformed or cleaned before they can be imported successfully.</strong></p>
<ul>
<li><p>if the source date format matches the target database format:</p>
<ul>
<li><p>choose the appropriate date datatype</p></li>
<li><p>import the data directly</p></li>
</ul></li>
<li><p>if the source and target formats do not match:</p>
<ul>
<li><p>transform the dates before import</p></li>
<li><p>transform the dates with a function during import</p></li>
</ul></li>
</ul>
<p><strong>Import the dates as strings, convert them after loading, then remove the original string values.</strong></p></td>
</tr>
<tr>
<td>Choosing A Date Datatype</td>
<td><p><strong>The target column should use a datatype appropriate for the information being stored.</strong></p>
<ul>
<li><p>PostgreSQL date-related datatypes include:</p>
<ul>
<li><p>timestamp with time zone</p></li>
<li><p>timestamp without time zone</p></li>
<li><p>date</p></li>
<li><p>time with time zone</p></li>
<li><p>time without time zone</p></li>
<li><p>interval</p></li>
</ul></li>
</ul>
<p><strong>The correct datatype depends on whether the data represents a date, time, datetime, time zone, or duration.</strong></p></td>
</tr>
<tr>
<td>Converting Date Formats</td>
<td><p><strong>Date conversion is often necessary when source data uses a different format from the database.</strong></p>
<ul>
<li><p>example source format:</p>
<ul>
<li><p>MM/DD/YYYY</p></li>
</ul></li>
</ul>
<p>ChatGPT 5.6 Sol</p>
<ul>
<li><p>PostgreSQL provides TO_DATE()</p>
<ul>
<li><p>formats text into a date value</p></li>
<li><p>general form:</p>
<ul>
<li><p>to_date(&lt;date field&gt;, &lt;formatting hint&gt;)</p></li>
</ul></li>
<li><p>example:</p>
<ul>
<li><p>to_date(birth_date, 'MM/DD/YYYY')</p></li>
</ul></li>
<li><p>the formatting hint tells PostgreSQL how the source string is structured</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA715_week03_notes\media\image4.jpeg" style="width:4.86389in;height:2.77917in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p><strong>The exact conversion function and syntax depend on the RDBMS.</strong></p></td>
</tr>
<tr>
<td>Using CAST For Date Conversion</td>
<td><p><span class="math inline"><strong>C</strong><strong>A</strong><strong>S</strong><strong>T</strong></span> <strong>may be sufficient when the source value can be converted directly into the desired date datatype.</strong></p>
<ul>
<li><p>CAST can be simpler than a formatting function when the source data is already close to a recognized database format</p></li>
<li><p>messier or nonstandard date strings may require a dedicated date-formatting function</p></li>
<li><p>the best conversion method depends on the source data and database dialect</p></li>
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
<th>Date Functions</th>
<th><p>Once dates are stored correctly, date functions can be used to manipulate and analyze them.</p>
<ul>
<li><p>date-function syntax differs substantially across database systems</p></li>
<li><p>the course examples use PostgreSQL syntax</p></li>
<li><p>similar operations in another RDBMS may require different functions or syntax</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Common Date Operations</td>
<td><p><strong>SQL date functions can support several types of operations.</strong></p>
<ul>
<li><p>date arithmetic:</p>
<ul>
<li><p>add units of time to a date or time</p></li>
<li><p>subtract units of time from a date or time</p></li>
</ul></li>
<li><p>date differences:</p>
<ul>
<li><p>calculate the distance between two dates or times</p></li>
</ul></li>
<li><p>current date and time:</p>
<ul>
<li><p>retrieve the current date or datetime from the database system</p></li>
</ul></li>
<li><p>date-part extraction:</p>
<ul>
<li><p>extract an individual component such as year, month, or day</p></li>
<li><p>example:</p>
<ul>
<li><p>extract the year from 2023-06-01</p></li>
</ul></li>
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
<th>Key Ideas</th>
<th><ul>
<li><p>date formatting varies across source data and database systems</p></li>
<li><p>format mismatches commonly require conversion during data import or transfer</p></li>
<li><p>the appropriate date datatype should be selected before loading data</p></li>
<li><p>dates can be transformed before import, during import, or after temporary string-based loading</p></li>
<li><p>PostgreSQL provides <span class="math inline"><strong>T</strong><strong>O</strong><strong>_</strong><strong>D</strong><strong>A</strong><strong>T</strong><strong>E</strong><strong>(</strong><strong>)</strong></span> for parsing formatted date strings</p></li>
<li><p><span class="math inline"><strong>C</strong><strong>A</strong><strong>S</strong><strong>T</strong></span> may work when values are already compatible with the target datatype</p></li>
<li><p>date functions support arithmetic, differences, current datetime values, and extraction of date components</p></li>
<li><p>date syntax is highly database-specific, so functions often need to be adapted when changing RDBMSs</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Basic String Functions</td>
</tr>
<tr>
<td>Purpose Of String Functions</td>
<td><p><strong>String functions allow SQL to inspect, combine, extract, and transform text stored in database fields.</strong></p>
<ul>
<li><p>common uses include:</p>
<ul>
<li><p>combining text from multiple values</p></li>
<li><p>measuring text length</p></li>
<li><p>locating patterns within text</p></li>
<li><p>extracting portions of strings</p></li>
<li><p>retrieving characters from either end of a string</p></li>
<li><p>replacing text patterns</p></li>
</ul></li>
<li><p>the lecture uses a table containing sections of the story Peter and the Wolf to demonstrate these operations</p></li>
<li><p>each row contains an identifier, an index describing the section, and a text field containing part of the story</p></li>
</ul></td>
</tr>
<tr>
<td>Concatenation</td>
<td><p><strong>Concatenation combines two or more strings into a single string.</strong></p>
<ul>
<li><p>in PostgreSQL, the concatenation operator is <span class="math inline">||</span></p></li>
<li><p>multiple text values can be joined together in sequence</p></li>
<li><p>complete <span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em></span> queries can also be placed inside parentheses and concatenated after their results are returned</p></li>
<li><p>the outer <em>SELECT</em> evaluates the completed concatenation expression</p></li>
<li><p>a <em>FROM</em> clause is not required when the outer <em>SELECT</em> is operating only on values or completed expressions rather than directly reading another table</p></li>
<li><p>example concept:</p>
<ul>
<li><p>first text value <em>||</em> second text value</p></li>
<li><p>concatenated values are placed directly next to one another</p></li>
<li><p>spaces or other separators must be added explicitly when needed</p></li>
</ul></li>
<li><p>example concept:</p>
<ul>
<li><p>first text value <em>|| ' ' ||</em> second text value</p></li>
<li><p>the literal space becomes part of the resulting string</p></li>
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
<th>LENGTH()</th>
<th><p><span class="math inline"><strong>L</strong><strong>E</strong><strong>N</strong><strong>G</strong><strong>T</strong><strong>H</strong><strong>(</strong><strong>)</strong></span> measures the length of a string.</p>
<ul>
<li><p>general form:</p>
<ul>
<li><p><span class="math inline"><strong>L</strong><strong>E</strong><strong>N</strong><strong>G</strong><strong>T</strong><strong>H</strong><strong>(</strong><strong>t</strong><strong>e</strong><strong>x</strong><strong>t</strong><strong>)</strong></span></p></li>
</ul></li>
<li><p>the function can be applied to a text column for every row in a table</p></li>
<li><p>the result can be assigned an alias such as text_length</p></li>
<li><p>text length can be useful for identifying unusually long or short values</p></li>
<li><p>the result can also support data-quality checks and later filtering or analysis</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>POSITION()</td>
<td><p><span class="math inline"><strong>P</strong><strong>O</strong><strong>S</strong><strong>I</strong><strong>T</strong><strong>I</strong><strong>O</strong><strong>N</strong><strong>(</strong><strong>)</strong></span> <strong>identifies where a specified pattern first occurs within a string.</strong></p>
<ul>
<li><p>general PostgreSQL form:</p>
<ul>
<li><p><span class="math inline"><em>P</em><em>O</em><em>S</em><em>I</em><em>T</em><em>I</em><em>O</em><em>N</em>(′<em>P</em><em>e</em><em>t</em><em>e</em><em>r</em>′ <em>I</em><em>N</em> <em>t</em><em>e</em><em>x</em><em>t</em>)</span></p></li>
</ul></li>
<li><p>the function searches the text field for the requested pattern</p></li>
<li><p>the returned value identifies the starting position of the first match</p></li>
<li><p>only the first occurrence is returned when the pattern appears multiple times</p></li>
<li><p>a result of 0 indicates that the pattern was not found</p></li>
<li><p>POSITION() can therefore be used both to locate text and to determine whether a pattern exists at all</p></li>
</ul></td>
</tr>
<tr>
<td>SUBSTRING()</td>
<td><p><span class="math inline"><strong>S</strong><strong>U</strong><strong>B</strong><strong>S</strong><strong>T</strong><strong>R</strong><strong>I</strong><strong>N</strong><strong>G</strong><strong>(</strong><strong>)</strong></span> <strong>extracts part of a larger string.</strong></p>
<ul>
<li><p>the function requires:</p>
<ul>
<li><p>the source string</p></li>
<li><p>the starting position</p></li>
<li><p>the number of characters to retrieve</p></li>
</ul></li>
<li><p>the starting position can be calculated dynamically with another function</p></li>
<li><p>example workflow:</p>
<ul>
<li><p>use <span class="math inline"><em>P</em><em>O</em><em>S</em><em>I</em><em>T</em><em>I</em><em>O</em><em>N</em>()</span> to find the first occurrence of Peter</p></li>
<li><p>use that position as the starting point for <span class="math inline"><em>S</em><em>U</em><em>B</em><em>S</em><em>T</em><em>R</em><em>I</em><em>N</em><em>G</em>()</span></p></li>
<li><p>return a fixed number of characters beginning at that location</p></li>
</ul></li>
</ul>
<p><strong>Functions can therefore be nested so that the result of one function becomes an argument to another.</strong></p></td>
</tr>
<tr>
<td>Combining POSITION() And SUBSTRING()</td>
<td><p><span class="math inline"><strong>P</strong><strong>O</strong><strong>S</strong><strong>I</strong><strong>T</strong><strong>I</strong><strong>O</strong><strong>N</strong><strong>(</strong><strong>)</strong></span> <strong>and <em>SUBSTRING()</em> can work together to extract text surrounding a known pattern.</strong></p>
<ul>
<li><p>first locate the target pattern</p></li>
<li><p>use the returned position as the starting point for extraction</p></li>
<li><p>specify how many characters should be returned</p>
<ul>
<li><p>this allows extraction to begin at a location that may differ from row to row</p></li>
</ul></li>
<li><p>special handling is needed when the search pattern does not exist</p></li>
<li><p>if <span class="math inline"><em>P</em><em>O</em><em>S</em><em>I</em><em>T</em><em>I</em><em>O</em><em>N</em>()</span> returns <span class="math inline">0</span>:</p>
<ul>
<li><p><span class="math inline"><em>S</em><em>U</em><em>B</em><em>S</em><em>T</em><em>R</em><em>I</em><em>N</em><em>G</em>()</span> may still attempt to extract characters from the beginning of the string</p></li>
</ul></li>
<li><p>filtering out rows where the position equals <span class="math inline">0</span> prevents misleading results</p></li>
<li><p>example condition:</p>
<ul>
<li><p><span class="math inline"><em>W</em><em>H</em><em>E</em><em>R</em><em>E</em> <em>P</em><em>O</em><em>S</em><em>I</em><em>T</em><em>I</em><em>O</em><em>N</em>(′<em>P</em><em>e</em><em>t</em><em>e</em><em>r</em>′ <em>I</em><em>N</em> <em>t</em><em>e</em><em>x</em><em>t</em>)  &lt; &gt; 0</span></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>LEFT() And RIGHT()</td>
<td><p><span class="math inline"><strong>L</strong><strong>E</strong><strong>F</strong><strong>T</strong><strong>(</strong><strong>)</strong></span> <strong>and <em>RIGHT()</em> extract a fixed number of characters from either end of a string.</strong></p>
<ul>
<li><p>general forms:</p>
<ul>
<li><p><span class="math inline"><em>L</em><em>E</em><em>F</em><em>T</em>(<em>t</em><em>e</em><em>x</em><em>t</em>, 12)</span></p></li>
<li><p><span class="math inline"><em>R</em><em>I</em><em>G</em><em>H</em><em>T</em>(<em>t</em><em>e</em><em>x</em><em>t</em>, 12)</span></p></li>
</ul></li>
<li><p><em>LEFT():</em></p>
<ul>
<li><p>returns the specified number of characters beginning at the left side of the string</p></li>
</ul></li>
<li><p><em>RIGHT():</em></p>
<ul>
<li><p>returns the specified number of characters beginning at the right side of the string</p></li>
</ul></li>
</ul>
<p><strong>These functions are useful when relevant information consistently appears at a known end of a text value.</strong></p></td>
</tr>
<tr>
<td>REPLACE()</td>
<td><p><strong>REPLACE() substitutes one text pattern for another.</strong></p>
<ul>
<li><p>general form:</p>
<ul>
<li><p><span class="math inline"><em>R</em><em>E</em><em>P</em><em>L</em><em>A</em><em>C</em><em>E</em>(<em>t</em><em>e</em><em>x</em><em>t</em>, ′<em>P</em><em>e</em><em>t</em><em>e</em><em>r</em>′, ′<em>E</em><em>m</em><em>i</em><em>l</em><em>y</em>′)</span></p></li>
</ul></li>
<li><p>first argument:</p>
<ul>
<li><p>identifies the source string</p></li>
</ul></li>
<li><p>second argument:</p>
<ul>
<li><p>identifies the text to find</p></li>
</ul></li>
<li><p>third argument:</p>
<ul>
<li><p>specifies the replacement text</p></li>
</ul></li>
<li><p>all matching occurrences within the processed string are replaced</p></li>
<li><p><span class="math inline"><em>R</em><em>E</em><em>P</em><em>L</em><em>A</em><em>C</em><em>E</em>():</span></p>
<ul>
<li><p>provides functionality similar to search-and-replace in a text editor</p></li>
<li><p>it can be used for:</p></li>
<li><p>cleaning</p></li>
<li><p>standardizing</p></li>
<li><p>transforming stored text</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Nested String Operations</td>
<td><p><strong>String functions can be combined to perform more complex transformations.</strong></p>
<ul>
<li><p>one function can generate an input value for another function</p></li>
<li><p><span class="math inline"><em>P</em><em>O</em><em>S</em><em>I</em><em>T</em><em>I</em><em>O</em><em>N</em>():</span></p>
<ul>
<li><p>can determine where SUBSTRING() should begin</p></li>
</ul></li>
<li><p>concatenation:</p>
<ul>
<li><p>can combine values returned from multiple expressions</p></li>
</ul></li>
<li><p>filtering conditions:</p>
<ul>
<li><p>can remove rows where a string operation would not produce a meaningful result</p></li>
</ul></li>
<li><p>complex string manipulation:</p>
<ul>
<li><p>often built by combining several simple functions rather than relying on one large operation</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Key Functions</td>
<td><p><img src="generated_media\DATA715_week03_notes\media\image5.jpeg" style="width:4.83241in;height:3.62431in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p>concatenation:</p>
<ul>
<li><p>combine multiple strings into one value</p></li>
</ul>
<p><em>LENGTH():</em></p>
<ul>
<li><p>measure string length</p></li>
</ul>
<p><em>POSITION():</em></p>
<ul>
<li><p>find the first occurrence of a pattern</p></li>
</ul>
<p><em>SUBSTRING():</em></p>
<ul>
<li><p>extract a specified portion of a string</p></li>
</ul>
<p><em>LEFT():</em></p>
<ul>
<li><p>extract characters from the beginning of a string</p></li>
</ul>
<p><em>RIGHT():</em></p>
<ul>
<li><p>extract characters from the end of a string</p></li>
</ul>
<p><span class="math display"><em>R</em><em>E</em><em>P</em><em>L</em><em>A</em><em>C</em><em>E</em>():</span></p>
<ul>
<li><p>substitute one text pattern for another</p></li>
</ul></td>
</tr>
<tr>
<td>Key Ideas</td>
<td><p><strong>SQL provides functions for both examining and transforming text data.</strong></p>
<ul>
<li><p>string functions can be used individually or nested together</p></li>
<li><p>literal spaces and separators must be explicitly included when concatenating values</p></li>
<li><p><span class="math inline"><em>P</em><em>O</em><em>S</em><em>I</em><em>T</em><em>I</em><em>O</em><em>N</em>()</span> returns only the first matching location</p></li>
<li><p>missing search patterns should be handled before using their position in another string operation</p></li>
<li><p>string manipulation is useful for data cleaning, transformation, validation, and feature preparation</p></li>
</ul></td>
</tr>
<tr>
<td>MariaDB Adaptation</td>
<td><p><strong>The lecture demonstrates PostgreSQL syntax, but most of these operations have direct MariaDB equivalents.</strong></p>
<ul>
<li><p>MariaDB normally uses <span class="math inline"><em>C</em><em>O</em><em>N</em><em>C</em><em>A</em><em>T</em>()</span> rather than<span class="math inline"> ||</span> for portable string concatenation</p></li>
<li><p>example:</p>
<ul>
<li><p><span class="math inline"><em>C</em><em>O</em><em>N</em><em>C</em><em>A</em><em>T</em>(<em>f</em><em>i</em><em>r</em><em>s</em><em>t</em>_<em>t</em><em>e</em><em>x</em><em>t</em>, ′ ′, <em>s</em><em>e</em><em>c</em><em>o</em><em>n</em><em>d</em>_<em>t</em><em>e</em><em>x</em><em>t</em>)</span></p></li>
</ul></li>
<li><p><span class="math inline"><em>P</em><em>O</em><em>S</em><em>I</em><em>T</em><em>I</em><em>O</em><em>N</em>()</span> is available in MariaDB with similar syntax</p></li>
<li><p>example:</p>
<ul>
<li><p><span class="math inline"><em>P</em><em>O</em><em>S</em><em>I</em><em>T</em><em>I</em><em>O</em><em>N</em>(′<em>P</em><em>e</em><em>t</em><em>e</em><em>r</em>′ <em>I</em><em>N</em> <em>t</em><em>e</em><em>x</em><em>t</em>)</span></p></li>
</ul></li>
<li><p><span class="math inline"><em>L</em><em>O</em><em>C</em><em>A</em><em>T</em><em>E</em>()</span> provides another common MariaDB form</p></li>
<li><p>example:</p>
<ul>
<li><p><span class="math inline"><em>L</em><em>O</em><em>C</em><em>A</em><em>T</em><em>E</em>(′<em>P</em><em>e</em><em>t</em><em>e</em><em>r</em>′, <em>t</em><em>e</em><em>x</em><em>t</em>)</span></p></li>
</ul></li>
<li><p><span class="math inline"><em>S</em><em>U</em><em>B</em><em>S</em><em>T</em><em>R</em><em>I</em><em>N</em><em>G</em>(), <em>L</em><em>E</em><em>F</em><em>T</em>(), <em>R</em><em>I</em><em>G</em><em>H</em><em>T</em>(),</span> and <span class="math inline"><em>R</em><em>E</em><em>P</em><em>L</em><em>A</em><em>C</em><em>E</em>()</span> are also available in MariaDB</p></li>
<li><p>MariaDB <span class="math inline"><em>L</em><em>E</em><em>N</em><em>G</em><em>T</em><em>H</em>()</span> returns the string length in bytes rather than necessarily the number of characters</p></li>
<li><p><span class="math inline"><em>C</em><em>H</em><em>A</em><em>R</em>_<em>L</em><em>E</em><em>N</em><em>G</em><em>T</em><em>H</em>()</span> should be used when the desired measurement is the number of characters</p></li>
<li><p>example:</p>
<ul>
<li><p><span class="math inline"><em>C</em><em>H</em><em>A</em><em>R</em>_<em>L</em><em>E</em><em>N</em><em>G</em><em>T</em><em>H</em>(<em>t</em><em>e</em><em>x</em><em>t</em>)</span></p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">LIKE</td>
</tr>
<tr>
<td>Purpose Of LIKE</td>
<td><p><span class="math inline"><strong>L</strong><strong>I</strong><strong>K</strong><strong>E</strong></span> <strong>is used when a query needs to match a text pattern instead of an exact value.</strong></p>
<ul>
<li><p>LIKE</p>
<ul>
<li><p>useful for filtering messy or inconsistent text data</p></li>
<li><p>can also be used for fuzzy joins when two values are similar enough to match by pattern</p></li>
</ul></li>
<li><p>common use cases include:</p>
<ul>
<li><p>synonyms</p></li>
<li><p>partial names</p></li>
<li><p>inconsistent descriptions</p></li>
<li><p>text values where the target word may appear at the beginning, middle, or end</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Filtering With LIKE</td>
<td><p><span class="math inline"><strong>L</strong><strong>I</strong><strong>K</strong><strong>E</strong></span> <strong>can be used in the</strong> <span class="math inline"><strong>W</strong><strong>H</strong><strong>E</strong><strong>R</strong><strong>E</strong></span> <strong>clause to keep rows that match a pattern.</strong></p>
<ul>
<li><p>example problem:</p>
<ul>
<li><p>multiple lab test names may refer to a COVID test</p></li>
</ul></li>
<li><p>example values:</p>
<ul>
<li><p>SARS-CoV-2 PCR</p></li>
<li><p>COVID-19 and flu panel</p></li>
<li><p>SARS-CoV-2 antigen</p></li>
<li><p>Influenza panel</p></li>
</ul></li>
<li><p>the first three values refer to COVID-related testing</p></li>
<li><p>they do not use the same exact text</p></li>
<li><p>if COVID tests are known to include either COVID or SARS-CoV-2, <span class="math inline"><em>L</em><em>I</em><em>K</em><em>E</em></span> can match both patterns</p></li>
<li><p>example:</p></li>
</ul>
<blockquote>
<p>SELECT *</p>
<p>FROM patient_labs</p>
<p>WHERE lab_test_name LIKE '%SARS-CoV-2%'</p>
<p>OR lab_test_name LIKE '%COVID%'</p>
</blockquote>
<ul>
<li><p>this returns rows where the lab test name contains either SARS-CoV-2 or COVID</p></li>
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
<th>Wildcards</th>
<th><p>Wildcards define how flexible the LIKE pattern should be.</p>
<ul>
<li><p><span class="math inline"><strong>%</strong></span> means any sequence of zero or more characters</p></li>
<li><p><em>_</em> means exactly one character</p></li>
<li><p><em>%</em> is useful when the target pattern may appear anywhere in the value</p></li>
<li><p>example:</p>
<ul>
<li><p><img src="generated_media\DATA715_week03_notes\media\image6.jpeg" style="width:4.875in;height:3.25in" />'<span class="math inline"><strong>%</strong></span>COVID<span class="math inline"><strong>%</strong></span>' matches COVID at the beginning, middle, or end of the text</p></li>
</ul></li>
</ul>
<p>ChatGPT 5.6 Sol</p>
<p>A pattern without wildcards is much closer to an exact match.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Handling Case Sensitivity</td>
<td><p><span class="math inline"><strong>L</strong><strong>I</strong><strong>K</strong><strong>E</strong></span> <strong>matching can be affected by differences in capitalization depending on the database and settings.</strong></p>
<ul>
<li><p>messy data may contain inconsistent case</p></li>
<li><p>example variations:</p>
<ul>
<li><p>COVID</p></li>
<li><p>Covid</p></li>
<li><p>covid</p></li>
</ul></li>
<li><p>case can be standardized during comparison by applying LOWER() or <span class="math inline"><em>U</em><em>P</em><em>P</em><em>E</em><em>R</em>()</span></p></li>
<li><p>lowercase example:</p></li>
</ul>
<blockquote>
<p>SELECT *</p>
<p>FROM patient_labs</p>
<p>WHERE LOWER(lab_test_name) LIKE '%sars-cov-2%'</p>
<p>OR LOWER (lab_test_name) LIKE '%covid%'</p>
</blockquote>
<ul>
<li><p>uppercase example:</p></li>
</ul>
<blockquote>
<p>SELECT *</p>
<p>FROM patient_labs</p>
<p>WHERE upper(lab_test_name) LIKE '%SARS-COV-2%'</p>
<p>OR upper(lab_test_name) LIKE '%COVID%'</p>
</blockquote>
<p><strong>The key idea is to transform both the column value and the search pattern into the same case before matching.</strong></p></td>
</tr>
<tr>
<td>Joining With LIKE</td>
<td><p><span class="math inline"><strong>L</strong><strong>I</strong><strong>K</strong><strong>E</strong></span> <strong>can also be used in a join condition when two tables need to be matched by a pattern rather than exact equality.</strong></p>
<ul>
<li><p>standard join logic expects exact matches</p></li>
<li><p>standard pattern:</p></li>
</ul>
<blockquote>
<p>FROM table1</p>
<p>JOIN table2</p>
<p>ON table1.foo = table2.bar</p>
</blockquote>
<ul>
<li><p>LIKE join logic allows one value to contain another value as part of a larger string</p></li>
<li><p>example idea:</p>
<ul>
<li><p>brown cow can match cow</p></li>
<li><p>striped cat can match cat</p></li>
<li><p>large elephant can match elephant</p></li>
</ul></li>
<li><p>the join condition must build a wildcard pattern around the value being matched</p></li>
<li><p>PostgreSQL example:</p></li>
</ul>
<blockquote>
<p>FROM table1</p>
<p>JOIN table2</p>
<p>ON table1.foo LIKE '%' || table2.bar || '%'</p>
</blockquote>
<ul>
<li><p>the wildcard symbols are concatenated onto the value from table2.bar</p></li>
</ul>
<p><strong>The resulting pattern checks whether table1.foo contains the value from table2.bar.</strong></p></td>
</tr>
<tr>
<td>Casting Before Pattern Matching</td>
<td><p><span class="math inline"><strong>L</strong><strong>I</strong><strong>K</strong><strong>E</strong></span> <strong>requires string-compatible values.</strong></p>
<ul>
<li><p>if the value being matched is not stored as a string, it may need to be cast to a string type first</p></li>
<li><p>casting allows the value to participate in concatenation and pattern matching</p></li>
<li><p>this is especially relevant when matching numeric or coded values stored in non-text columns</p></li>
</ul></td>
</tr>
<tr>
<td>Performance Caution</td>
<td><p><span class="math inline"><strong>L</strong><strong>I</strong><strong>K</strong><strong>E</strong></span> <strong>joins can be slow.</strong></p>
<ul>
<li><p>pattern matching is more expensive than exact matching</p></li>
<li><p>joining with wildcard patterns can become especially slow on large tables</p></li>
<li><p>this approach is usually not ideal for clean or well-structured data</p></li>
<li><p>it may still be useful when messy data prevents exact joins</p></li>
<li><p>LIKE joins should be treated as a practical fallback rather than the preferred design</p></li>
</ul></td>
</tr>
<tr>
<td>MariaDB Note</td>
<td><p><strong>The filtering examples work similarly in MariaDB.</strong></p>
<ul>
<li><p>MariaDB example:</p></li>
</ul>
<blockquote>
<p>SELECT *</p>
<p>FROM patient_labs</p>
<p>WHERE LOWER (lab_test_name) LIKE '%sars-cov-2%'</p>
<p>OR LOWER (lab_test_name) LIKE '%covid%'</p>
</blockquote>
<ul>
<li><p>the PostgreSQL join example uses || for concatenation</p></li>
<li><p>MariaDB normally uses CONCAT() instead</p></li>
<li><p>MariaDB example:</p></li>
</ul>
<blockquote>
<p>FROM table1</p>
<p>JOIN table2</p>
<p>ON table1.foo LIKE CONCAT ('%', table2.bar, '%')</p>
</blockquote>
<ul>
<li><p>if table2.bar is not already text, convert it before using it in the pattern</p></li>
</ul></td>
</tr>
<tr>
<td>Key Ideas</td>
<td><ul>
<li><p><span class="math inline"><em>L</em><em>I</em><em>K</em><em>E</em></span> supports inexact text matching</p></li>
<li><p><em>%</em> matches any sequence of characters</p></li>
<li><p><em>_</em> matches one character</p></li>
<li><p><em>LIKE</em> in <em>WHERE</em> filters rows based on a pattern</p></li>
<li><p><em>LOWER()</em> or <em>UPPER()</em> can reduce case-related matching problems</p></li>
<li><p><em>LIKE</em> can be used in join conditions for fuzzy matching</p></li>
<li><p><em>wildcards</em> can be concatenated around column values to build dynamic patterns</p></li>
<li><p><em>LIKE</em> <em>joins</em> can be slow and should be used carefully with large tables</p></li>
<li><p>when possible, <em>clean</em> <em>and</em> <em>standardize</em> <em>data</em> before relying on fuzzy pattern joins</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Regular Expressions</td>
</tr>
<tr>
<td>Purpose Of Regular Expressions</td>
<td><p><strong>Regular expressions (regex) are used for pattern matching when exact matching is not flexible enough.</strong></p>
<ul>
<li><p>can identify whether a value follows a particular structure</p></li>
<li><p>useful when a column contains messy, inconsistent, or mixed-format data</p></li>
<li><p>allows a query to search for patterns rather than exact values</p></li>
</ul></td>
</tr>
<tr>
<td>Why Pattern Matching Matters</td>
<td><p><strong>Some data cannot be reliably queried with simple equality comparisons.</strong></p>
<ul>
<li><p>example problem:</p>
<ul>
<li><p>identify which values in a messy text column could be United States phone numbers</p></li>
</ul></li>
<li><p>some values may look valid</p></li>
<li><p>some values may be too long</p></li>
<li><p>some values may be too short</p></li>
<li><p>some values may contain letters or invalid characters</p></li>
<li><p>a human can visually inspect a few rows</p></li>
<li><p>but this does not scale to millions or billions of records</p></li>
</ul>
<p><strong>SQL needs a formal way to express the idea of looks like a phone number.</strong></p></td>
</tr>
<tr>
<td>Regex As A Boolean Test</td>
<td><p><strong>A regular expression can be used in a WHERE clause to test whether each value matches a pattern.</strong></p>
<ul>
<li><p>the database evaluates each row against the regex pattern</p></li>
<li><p>if the value matches the pattern, the test returns true</p></li>
<li><p>if the value does not match the pattern, the test returns false</p></li>
<li><p>the query keeps only the rows where the regex test is true</p></li>
</ul>
<p><strong>This makes regex useful for filtering messy data based on structure.</strong></p></td>
</tr>
<tr>
<td>Phone Number Pattern Example</td>
<td><p><strong>A United States phone number has a recognizable structure, but it may appear in several formats.</strong></p>
<ul>
<li><p>core structure:</p>
<ul>
<li><p>three-digit area code</p></li>
<li><p>three-digit prefix</p></li>
<li><p>four-digit line number</p></li>
</ul></li>
<li><p>possible optional elements:</p>
<ul>
<li><p>country code such as +1</p></li>
<li><p>parentheses around the area code</p></li>
<li><p>hyphens between number groups</p></li>
<li><p>dots between number groups</p></li>
<li><p>spaces between number groups</p></li>
<li><p>no separators at all</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA715_week03_notes\media\image7.jpeg" style="width:4.84375in;height:3.22917in" /></p>
<p>ChatGPT 5.6 Sol</p>
<p><strong>A useful phone-number regex must allow expected variation without becoming so loose that it matches invalid data.</strong></p></td>
</tr>
<tr>
<td>Balancing Flexibility And Precision</td>
<td><p><strong>Regex design often requires balancing what should match against what should be rejected.</strong></p>
<ul>
<li><p>a strict pattern may miss valid values written in an unexpected format</p></li>
<li><p>a loose pattern may capture values that are not actually valid</p></li>
<li><p>a phone-number regex can match most United States phone numbers</p></li>
<li><p>a regex that handles every international phone-number format would be much more complex</p></li>
<li><p>the pattern should be designed around the data and the purpose of the query</p></li>
</ul></td>
</tr>
<tr>
<td>Basic Regex Concepts</td>
<td><p><strong>Regex syntax uses special symbols to describe patterns.</strong></p>
<ul>
<li><p><span class="math inline">∖<em>d</em></span> matches any digit</p></li>
<li><p><em>\D</em> matches any non-digit</p></li>
<li><p>word-related patterns can match letters, numbers, or word boundaries</p></li>
<li><p>space-related patterns can match whitespace</p></li>
<li><p>quantifiers can describe how many times something should appear</p></li>
<li><p>optional elements can allow a pattern to match values with or without certain characters</p></li>
</ul>
<p><strong>Regex can represent almost any character or text structure that can appear in computer-readable text.</strong></p></td>
</tr>
<tr>
<td>Learning Regex</td>
<td><p><img src="generated_media\DATA715_week03_notes\media\image8.jpeg" style="width:4.91667in;height:3.27778in" /><strong>Regex syntax can look dense at first, but it is learned best through practice.</strong></p>
<p>ChatGPT 5.6 Sol</p>
<ul>
<li><p>regex expressions often look confusing before the symbols are understood</p></li>
<li><p>cheat sheets are useful references while building patterns</p></li>
<li><p>regex is usually learned by experimentation rather than memorization</p></li>
</ul>
<p><strong>Building small patterns and testing them against example strings is the most practical way to learn.</strong></p></td>
</tr>
<tr>
<td>Testing And Debugging Regex</td>
<td><p><strong>Online regex editors help construct, test, and debug patterns.</strong></p>
<ul>
<li><p>regex101 is one example of an online regex testing tool</p></li>
<li><p>test strings can be entered into the editor</p></li>
<li><p>the regex pattern highlights values that match</p></li>
<li><p>non-highlighted values reveal cases the pattern did not capture</p></li>
<li><p>the editor can explain pieces of the regex syntax</p></li>
</ul>
<p><strong>This makes it easier to understand why a pattern does or does not match.</strong></p></td>
</tr>
<tr>
<td>Password Validation Example</td>
<td><p><strong>Regex can validate whether a string satisfies several structural rules.</strong></p>
<ul>
<li><p>example password rules:</p>
<ul>
<li><p>at least one capital letter</p></li>
<li><p>at least one lowercase letter</p></li>
<li><p>at least one number</p></li>
<li><p>at least one symbol</p></li>
<li><p>a weak password such as password1 may fail because it does not satisfy all rules</p></li>
<li><p>a stronger password may match when it contains all required character types</p></li>
</ul></li>
</ul>
<p><strong>This demonstrates how regex can test multiple pattern requirements at once.</strong></p></td>
</tr>
<tr>
<td>Why Regex Is Needed In SQL</td>
<td><p><strong>SQL returns exactly what the query asks for.</strong></p>
<ul>
<li><p>exact equality only finds values that match exactly</p></li>
<li><p>messy data often requires fuzzier matching</p></li>
<li><p>regex provides a way to describe that fuzziness precisely</p></li>
</ul>
<p><strong>Regex is especially useful when the desired data shares a structure but not an exact value.</strong></p></td>
</tr>
<tr>
<td>Common Use Cases</td>
<td><p><strong>Regex is useful when data must be identified by pattern rather than exact content.</strong></p>
<ul>
<li><p>phone-number detection</p></li>
<li><p>email-format validation</p></li>
<li><p>password-format validation</p></li>
<li><p>searching messy text fields</p></li>
<li><p>finding values that look like lab results</p></li>
<li><p>finding date-like values inside paragraphs</p></li>
</ul>
<p><strong>Identifying structured information inside unstructured or semi-structured text,</strong></p></td>
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
<th>Regex In Text Columns</th>
<th><p>Databases can store long text values such as sentences or paragraphs.</p>
<ul>
<li><p>regex can search those text values for embedded structures</p></li>
<li><p>example:</p>
<ul>
<li><p>find paragraphs that contain any date-like value</p></li>
</ul></li>
<li><p>dates can appear in many formats with different punctuation</p></li>
<li><p>a regex can describe those possible formats and return matching text</p></li>
</ul>
<p>This makes regex useful for extracting structured signals from larger text fields.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Key Ideas</td>
<td><ul>
<li><p>regular expressions support pattern matching</p></li>
<li><p>regex is useful when equality matching is too rigid</p></li>
<li><p>a regex test can return true or false for each row</p></li>
<li><p>regex can filter messy data by structure</p></li>
<li><p>regex patterns must balance flexibility and precision</p></li>
<li><p>complex patterns should be tested against realistic examples</p></li>
<li><p>online editors can help build and debug regex expressions</p></li>
<li><p>regex is a powerful skill for querying, validating, and cleaning database text</p></li>
</ul></td>
</tr>
<tr>
<td>MariaDB Note</td>
<td><p><strong>MariaDB supports regular-expression matching, but the syntax may differ from PostgreSQL.</strong></p>
<ul>
<li><p>common MariaDB operators:</p>
<ul>
<li><p><span class="math inline"><em>R</em><em>E</em><em>G</em><em>E</em><em>X</em><em>P</em></span></p></li>
<li><p><span class="math inline"><em>R</em><em>L</em><em>I</em><em>K</em><em>E</em></span></p></li>
</ul></li>
<li><p>example concept:</p>
<ul>
<li><p>column_name <em>REGEXP</em> 'pattern'</p></li>
</ul></li>
<li><p>MariaDB regex behavior depends on the version and regular-expression engine</p></li>
<li><p>patterns should be tested directly in MariaDB before relying on them for cleaning or validation</p></li>
<li><p>when translating from PostgreSQL examples, verify both the matching operator and the regex syntax before running the query</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Using Regular Expressions in SQL</td>
</tr>
<tr>
<td>Regex As Flexible Pattern Matching</td>
<td><p><strong>Regular expressions provide a more flexible form of pattern matching than LIKE.</strong></p>
<ul>
<li><p><em>LIKE</em> supports simple pattern matching with wildcards</p></li>
<li><p>regex supports more complex and sophisticated patterns</p></li>
<li><p>regex is useful when the target pattern cannot be described clearly with only <em>%</em> and <em>_</em></p></li>
</ul>
<p><strong>Regex can identify patterns inside strings, count pattern matches, test whether a pattern exists, or replace matching text.</strong></p></td>
</tr>
<tr>
<td>Database-Specific Syntax</td>
<td><p><strong>Regex syntax and function support vary by relational database management system.</strong></p>
<ul>
<li><p>the exact regex functions depend on the RDBMS</p></li>
<li><p>the examples in this material use PostgreSQL</p></li>
<li><p>when moving between databases, regex syntax and available functions should be checked before reuse</p></li>
</ul></td>
</tr>
<tr>
<td>PostgreSQL Regex Functions</td>
<td><p><strong>PostgreSQL provides several functions that can use regular expressions.</strong></p>
<ul>
<li><p>substring(string from pattern)</p></li>
<li><p>extracts a substring that matches the regex pattern</p></li>
<li><p>returns the matching substring when a match exists</p></li>
<li><p>useful when the goal is to pull out the matching portion of a larger string</p></li>
<li><p>regexp_count(string, pattern)</p>
<ul>
<li><p>counts the number of times a regex pattern appears within a string</p></li>
<li><p>useful when the goal is to measure how often a pattern occurs</p></li>
<li><p>can support text analysis, validation, or data-quality checks</p></li>
</ul></li>
<li><p>regexp_like(string, pattern)</p>
<ul>
<li><p>returns true or false depending on whether the regex pattern is found in the string</p></li>
<li><p>similar in purpose to <em>LIKE</em></p></li>
<li><p>more flexible than <em>LIKE</em> because the pattern is defined with regex rather than simple wildcards</p></li>
<li><p>useful in <span class="math inline"><em>W</em><em>H</em><em>E</em><em>R</em><em>E</em></span> clauses when filtering rows by complex text patterns</p></li>
</ul></li>
<li><p>regexp_replace(source, pattern, replacement)</p>
<ul>
<li><p>replaces text that matches a regex pattern with a specified replacement string</p></li>
<li><p>useful for cleaning or standardizing text</p></li>
<li><p>can transform strings when the values to be replaced follow a pattern rather than one exact value</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Regex Documentation</td>
<td><p><strong>PostgreSQL documentation provides more detail on regex functions and syntax.</strong></p>
<ul>
<li><p>the documentation includes additional regex functions</p></li>
<li><p>the documentation includes usage examples</p></li>
<li><p>PostgreSQL also provides a regex syntax reference or cheat sheet</p></li>
<li><p>regex cheat sheets are useful because regex patterns can become dense and difficult to memorize</p></li>
</ul></td>
</tr>
<tr>
<td>Key Ideas</td>
<td><ul>
<li><p>regex extends pattern matching beyond the simpler LIKE expression</p></li>
<li><p><span class="math inline"><em>L</em><em>I</em><em>K</em><em>E</em></span> is useful for basic wildcard matching</p></li>
<li><p>regex is useful for complex text patterns</p></li>
<li><p>PostgreSQL supports regex functions for extracting, counting, testing, and replacing pattern matches</p></li>
<li><p>regex syntax is database-specific</p></li>
<li><p>documentation and cheat sheets are important references when writing or debugging regex patterns</p></li>
</ul></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>
