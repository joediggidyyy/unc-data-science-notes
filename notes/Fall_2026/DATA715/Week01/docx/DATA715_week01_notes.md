> Markdown version for convenient browsing. Original files:
> - PDF: [DATA715_week01_notes.pdf](../DATA715_week01_notes.pdf)
> - DOCX: [DATA715_week01_notes.docx](DATA715_week01_notes.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 16%" />
<col style="width: 7%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Review of Relational Databases</th>
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
<li><p>Describe the relational database model</p></li>
<li><p>Explain basic SQL functions</p></li>
<li><p>Recognize the OMOP database</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Async</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5">The Relational Model</td>
</tr>
<tr>
<td>Data Models</td>
<td colspan="4"><ul>
<li><p>a collection of concepts used to describe:</p>
<ul>
<li><p>structure of a database</p></li>
<li><p>relationships between data elements</p></li>
</ul></li>
<li><p>the history of databases is closely tied to the development of different data models</p>
<ul>
<li><p>conceptual data model</p>
<ul>
<li><p>high-level</p></li>
<li><p>describes how users understand relationships between data</p></li>
<li><p>main focus of this course</p></li>
</ul></li>
<li><p>physical data model</p>
<ul>
<li><p>more technical</p></li>
<li><p>describes how data is physically stored on computer hardware</p></li>
<li><p><em>not a major focus of this course</em></p></li>
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
<th>Hierarchical Model – 1960s</th>
<th><ul>
<li><p>organizes data in a top-down tree structure</p></li>
<li><p>primarily supports one-to-many relationships</p>
<ul>
<li><p>a department</p>
<ul>
<li><p>can have many employees</p></li>
</ul></li>
<li><p>an employee</p>
<ul>
<li><p>belongs to only one department</p></li>
<li><p>can have many projects</p></li>
<li><p>can have many computers</p></li>
</ul></li>
<li><p>a project</p>
<ul>
<li><p>belongs to only one employee</p></li>
</ul></li>
<li><p>a computer</p>
<ul>
<li><p><img src="generated_media\DATA715_week01_notes\media\image1.png" style="width:4.21875in;height:3.88966in" />belongs to only one person</p></li>
</ul></li>
</ul></li>
</ul>
<p>Gemini 3.7 Flash</p>
<ul>
<li><p>key rule</p>
<ul>
<li><p>every child can only have one parent</p></li>
</ul></li>
<li><p>query limitation</p>
<ul>
<li><p>must begin at the top of the hierarchy</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Network Model – 1960s</td>
<td><ul>
<li><p>the network model expanded the hierarchical model</p></li>
<li><p>its major improvement was support for many-to-many relationships</p></li>
<li><p>advantages</p>
<ul>
<li><p>more flexible than the hierarchical model</p></li>
</ul></li>
<li><p>problems</p>
<ul>
<li><p>difficult to maintain</p></li>
<li><p>structural changes can be complicated</p></li>
<li><p>not every real-world relationship fits naturally into a parent-child structure</p></li>
</ul></li>
<li><p>a more flexible model is still needed</p></li>
</ul></td>
</tr>
<tr>
<td>Relational Model – 1970s</td>
<td><ul>
<li><p>the relational model was developed primarily through the work of <a href="https://en.wikipedia.org/wiki/Edgar_F._Codd">E. F. Codd</a></p></li>
<li><p>it became the foundation of modern relational databases</p></li>
<li><p>a major improvement was separating physical data storage from conceptual presentation of data</p></li>
<li><p>this makes databases easier to:</p>
<ul>
<li><p>query</p></li>
<li><p>update</p></li>
<li><p>manage</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Properties of Relational Databases</td>
<td><ul>
<li><p>data Is stored in tables of rows and columns</p></li>
<li><p>primary keys (or <em>unique key</em>)</p>
<ul>
<li><p>a unique identifier for a row in a table</p></li>
</ul></li>
<li><p>relations have no inherent order</p></li>
<li><p>columns have no inherent order</p></li>
<li><p>attributes must be atomic (can only contain one value)</p></li>
<li><p>NULL values</p>
<ul>
<li><p>literally “nothing” – not “zero”</p></li>
<li><p>NULL <span class="math inline">≠</span> NULL</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">Relational Model: Constraints</td>
</tr>
<tr>
<td>Constraints</td>
<td><ul>
<li><p>a rule used when designing and working with a relational database</p></li>
<li><p>help control:</p>
<ul>
<li><p>what data can be stored</p></li>
<li><p>which values are valid</p></li>
<li><p>how records are uniquely identified</p></li>
<li><p>how different tables may reference one another</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Three Types of Constraints</td>
<td><ul>
<li><p>implicit</p>
<ul>
<li><p>built into the relational database system</p></li>
<li><p>the user does not normally choose or manage these</p></li>
</ul></li>
<li><p>explicit</p>
<ul>
<li><p>rules deliberately defined by the database designer</p></li>
</ul></li>
<li><p>business rules</p>
<ul>
<li><p>usually more complex rules associated with the application using the database</p></li>
<li><p>instead of allowing invalid data to reach the database, the application layer (ex: a web form) can enforce these rules first</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Domain Constraints</td>
<td><ul>
<li><p>defines what kind of data can appear in an attribute or column</p></li>
<li><p>commonly enforced using data types that are normally defined when the table is created</p></li>
<li><p>values stored in that column must follow the defined domain</p></li>
</ul></td>
</tr>
<tr>
<td>Key Constraints</td>
<td><ul>
<li><p>primary key uniquely identifies one row in a relation</p></li>
<li><p>each value must be unique</p></li>
</ul></td>
</tr>
<tr>
<td>Key Design Must Account for Future Data</td>
<td><ul>
<li><p>a key may work with the database's current data but fail when new records are added late</p></li>
<li><p>therefore, database designers should consider</p>
<ul>
<li><p>existing records</p></li>
<li><p>expected future records</p></li>
<li><p>whether the chosen key will remain unique</p></li>
</ul></li>
<li><p>a poor key design can prevent legitimate future data from being stored</p></li>
</ul></td>
</tr>
<tr>
<td>Composite Keys</td>
<td><ul>
<li><p>uses multiple attributes together to uniquely identify a row</p></li>
</ul></td>
</tr>
<tr>
<td>Database Schema</td>
<td><ul>
<li><p>a map of the database</p></li>
<li><p>every relation has a schema, and the schemas of all relations together describe the overall database structure</p></li>
<li><p>looking at the complete schema helps designers make decisions based on the <strong>entire database</strong>, rather than designing each table independently</p></li>
</ul></td>
</tr>
<tr>
<td>Entity Integrity</td>
<td><ul>
<li><p>an entity integrity constraint is an implicit database constraint</p>
<ul>
<li><p>example: a primary key can never be null</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Referential Integrity</td>
<td><ul>
<li><p>r<strong>eferential integrity</strong> controls relationships between different relations</p>
<ul>
<li><p>example: if a record in Table B refers to a record in Table A, the referenced record must actually exist in Table A</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Foreign Keys</td>
<td><ul>
<li><p>a foreign key</p>
<ul>
<li><p>is an attribute that references the primary key of another relation</p></li>
<li><p>does not have to be the primary key of its own table</p></li>
<li><p>only needs to reference the appropriate primary key in another table</p></li>
</ul></li>
<li><p>foreign keys are essential because they allow relational databases to:</p>
<ul>
<li><p>connect tables</p></li>
<li><p>query information across tables</p></li>
<li><p>represent relationships between entities</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">SQL Basics</td>
</tr>
<tr>
<td>FROM, SELECT, and WHERE</td>
<td><ul>
<li><p>SQL queries are built from three fundamental clauses</p>
<ul>
<li><p>required clauses:</p>
<ul>
<li><p>FROM</p>
<ul>
<li><p>which table(s) provide the data</p></li>
</ul></li>
<li><p>SELECT</p>
<ul>
<li><p>which columns appear in the output</p></li>
</ul></li>
</ul></li>
<li><p>optional clause:</p>
<ul>
<li><p>WHERE</p>
<ul>
<li><p>which rows are returned</p></li>
</ul></li>
</ul></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image2.png" style="width:2.70871in;height:0.80219in" /></p></td>
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
<th>FROM: Choose the Table</th>
<th><ul>
<li><p>tells the database which table contains the data</p></li>
<li><p>table aliases</p>
<ul>
<li><p>a table can be given a shorter temporary name called an alias</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image3.png" style="width:1.81275in;height:0.43756in" /></p>
<ul>
<li><p>now <span class="math inline"><strong>′</strong><strong>p</strong><strong>′</strong></span> represents ‘table_patient‘ for the rest of the query</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>SELECT: Choose the Columns</td>
<td><ul>
<li><p>determines which columns appear in the query output</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image4.png" style="width:1.93777in;height:1.27101in" /></p>
<ul>
<li><p>the table may contain many more columns, but only these three will appear</p></li>
</ul>
<ul>
<li><p>qualifying column names</p>
<ul>
<li><p>with its table name</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image5.png" style="width:2.1253in;height:0.40631in" /></p>
<ul>
<li><p>with the table's alias</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image6.png" style="width:1.35436in;height:0.36463in" /></p></td>
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
<th>SQL Functions in SELECT</th>
<th><ul>
<li><p>transform or calculate values before they appear in the output</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image7.png" style="width:2.36491in;height:0.58341in" /></p>
<ul>
<li><p>UPPER() converts to uppercase</p></li>
<li><p>so ‘Joe Waller’ becomes ‘JOE WALLER’</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Renaming Output Columns</td>
<td><ul>
<li><p>a calculated or transformed column can be given an alias using AS</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image8.png" style="width:3.22962in;height:0.88554in" /></p>
<ul>
<li><p>does not rename the column in the original database</p></li>
<li><p>only changes the name shown in the query output</p></li>
</ul></td>
</tr>
<tr>
<td>Combining Column Values</td>
<td><ul>
<li><p>SQL functions can also combine values from multiple columns</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image9.png" style="width:3.86458in;height:0.32329in" /></p></td>
</tr>
<tr>
<td>Core Functions</td>
<td><p>String Functions</p>
<ul>
<li><p>UPPER()</p>
<ul>
<li><p>converts text to uppercase</p></li>
</ul></li>
<li><p>LOWER()</p>
<ul>
<li><p>converts text to lowercase</p></li>
</ul></li>
<li><p>concatenation</p>
<ul>
<li><p>combines two or more string values into a single value</p></li>
</ul></li>
</ul>
<p>Aggregate Functions</p>
<ul>
<li><p>COUNT()</p>
<ul>
<li><p>counts the number of returned records or values</p></li>
</ul></li>
<li><p>AVG()</p>
<ul>
<li><p>calculates the average of numeric values</p></li>
</ul></li>
</ul>
<p>Mathematical Functions</p>
<ul>
<li><p>FLOOR()</p>
<ul>
<li><p>rounds a number down</p></li>
</ul></li>
<li><p>CEILING()</p>
<ul>
<li><p>rounds a number up</p></li>
</ul></li>
<li><p>Standard mathematical functions</p>
<ul>
<li><p>perform common arithmetic calculations</p></li>
</ul></li>
</ul>
<p>Date Functions</p>
<ul>
<li><p>date-difference functions</p>
<ul>
<li><p>calculate the amount of time between dates</p></li>
</ul></li>
<li><p>age/date calculations</p>
<ul>
<li><p>calculate values such as a person's age from stored dates</p></li>
</ul></li>
<li><p>Notes</p>
<ul>
<li><p>functions can be used in both SELECT and WHERE clauses</p></li>
<li><p>exact function syntax can vary between relational database management systems</p></li>
<li><p>this course uses PostgreSQL (Postgres) syntax</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2">----</td>
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
<tr>
<td></td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>
