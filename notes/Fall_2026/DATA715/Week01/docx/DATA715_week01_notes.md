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
<col style="width: 0%" />
</colgroup>
<thead>
<tr>
<th><h2 id="hierarchical-model-1960s">Hierarchical Model – 1960s</h2></th>
<th colspan="2"><h2 id="organizes-data-in-a-top-down-tree-structure.">Organizes data in a top-down tree structure.</h2>
<h2 id="primarily-supports-one-to-many-relationships">primarily supports one-to-many relationships</h2>
<h2 id="a-department">a department </h2>
<h2 id="can-have-many-employees">can have many employees</h2>
<h2 id="an-employee">an employee</h2>
<h2 id="belongs-to-only-one-department">belongs to only one department</h2>
<h2 id="can-have-many-projects">can have many projects</h2>
<h2 id="can-have-many-computers">can have many computers</h2>
<h2 id="a-project">a project</h2>
<h2 id="belongs-to-only-one-employee">belongs to only one employee</h2>
<h2 id="a-computer">a computer</h2>
<h2 id="belongs-to-only-one-person"><img src="generated_media\DATA715_week01_notes\media\image1.png" style="width:4.21875in;height:3.88958in" />belongs to only one person</h2>
<h2 id="section"></h2>
<h2 id="section-1"></h2>
<h2 id="section-2"></h2>
<h2 id="section-3"></h2>
<h2 id="section-4"></h2>
<h2 id="section-5"></h2>
<p>Gemini 3.7 Flash</p>
<h2 id="key-rule">key rule</h2>
<h2 id="every-child-can-only-have-one-parent">every child can only have one parent </h2>
<h2 id="query-limitation">query limitation</h2>
<h2 id="must-begin-at-the-top-of-the-hierarchy">must begin at the top of the hierarchy</h2></th>
</tr>
</thead>
<tbody>
<tr>
<td>Network Model – 1960s</td>
<td colspan="2"><p><strong>The network model expanded the hierarchical model.</strong></p>
<ul>
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
<td colspan="2"><p><strong>The relational model was developed primarily through the work of <a href="https://en.wikipedia.org/wiki/Edgar_F._Codd">E. F. Codd</a>.</strong></p>
<ul>
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
<td colspan="2"><p><strong>Data Is stored in tables of rows and columns.</strong></p>
<ul>
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
<td colspan="3">Relational Model: Constraints</td>
</tr>
<tr>
<td>Constraints</td>
<td colspan="2"><p><strong>A rule used when designing and working with a relational database.</strong></p>
<ul>
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
<td colspan="2"><ul>
<li><p><strong>implicit</strong></p>
<ul>
<li><p>built into the relational database system</p></li>
<li><p>the user does not normally choose or manage these</p></li>
</ul></li>
<li><p><strong>explicit</strong></p>
<ul>
<li><p>rules deliberately defined by the database designer</p></li>
</ul></li>
<li><p><strong>business rules</strong></p>
<ul>
<li><p>usually more complex rules associated with the application using the database</p></li>
<li><p>instead of allowing invalid data to reach the database, the application layer (ex: a web form) can enforce these rules first</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Domain Constraints</td>
<td colspan="2"><p><strong>Defines what kind of data can appear in an attribute or column.</strong></p>
<ul>
<li><p>commonly enforced using data types that are normally defined when the table is created</p></li>
<li><p>values stored in that column must follow the defined domain</p></li>
</ul></td>
</tr>
<tr>
<td>Key Constraints</td>
<td colspan="2"><p><strong>Primary key uniquely identifies one row in a relation.</strong></p>
<ul>
<li><p>each value must be unique</p></li>
</ul></td>
</tr>
<tr>
<td>Key Design Must Account for Future Data</td>
<td colspan="2"><p><strong>A key may work with the database's current data but fail when new records are added late.</strong></p>
<ul>
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
<td colspan="2"><strong>Uses multiple attributes together to uniquely identify a row.</strong></td>
</tr>
<tr>
<td>Database Schema</td>
<td colspan="2"><p><strong>A map of the database.</strong></p>
<ul>
<li><p>every relation has a schema, and the schemas of all relations together describe the overall database structure</p></li>
<li><p>looking at the complete schema helps designers make decisions based on the <strong>entire database</strong>, rather than designing each table independently</p></li>
</ul></td>
</tr>
<tr>
<td>Entity Integrity</td>
<td colspan="2"><p><strong>An entity integrity constraint is an implicit database constraint.</strong></p>
<ul>
<li><p>example: a primary key can never be null</p></li>
</ul></td>
</tr>
<tr>
<td>Referential Integrity</td>
<td colspan="2"><p><strong>Referential integrity controls relationships between different relations.</strong></p>
<ul>
<li><p>example:</p>
<ul>
<li><p>if a record in Table B refers to a record in Table A, the referenced record must actually exist in Table A</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Foreign Keys</td>
<td colspan="2"><p><strong>A foreign key :</strong></p>
<ul>
<li><p>is an attribute that references the primary key of another relation</p>
<ul>
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
<td colspan="3">SQL Basics</td>
</tr>
<tr>
<td>FROM, SELECT, and WHERE</td>
<td colspan="2"><p><strong>SQL queries are built from three fundamental clauses.</strong></p>
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
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image2.png" style="width:2.70871in;height:0.80219in" /></p></td>
</tr>
<tr>
<td>FROM: Choose the Table</td>
<td colspan="2"><p><strong>Tells the database which table contains the data.</strong></p>
<ul>
<li><p>table aliases</p>
<ul>
<li><p>a table can be given a shorter temporary name called an alias</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image3.png" style="width:1.81275in;height:0.43756in" /></p>
<ul>
<li><p>now <span class="math inline"><strong>′</strong><strong>p</strong><strong>′</strong></span> represents ‘table_patient‘ for the rest of the query</p></li>
</ul></td>
</tr>
<tr>
<td>SELECT: Choose the Columns</td>
<td colspan="2"><p><strong>Determines which columns appear in the query output.</strong></p>
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
<tr>
<td>SQL Functions in SELECT</td>
<td colspan="2"><p><strong>Transform or calculate values before they appear in the output.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image7.png" style="width:2.36491in;height:0.58341in" /></p>
<ul>
<li><p>UPPER() converts to uppercase</p></li>
<li><p>so ‘Joe Waller’ becomes ‘JOE WALLER’</p></li>
</ul></td>
</tr>
<tr>
<td>Renaming Output Columns</td>
<td colspan="2"><p><strong>A calculated or transformed column can be given an alias using AS.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image8.png" style="width:3.22962in;height:0.88554in" /></p>
<ul>
<li><p>does not rename the column in the original database</p></li>
<li><p>only changes the name shown in the query output</p></li>
</ul></td>
</tr>
<tr>
<td>Combining Column Values</td>
<td colspan="2"><p><strong>SQL functions can also combine values from multiple columns.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image9.png" style="width:3.86458in;height:0.32329in" /></p></td>
</tr>
<tr>
<td>Core Functions</td>
<td colspan="2"><p><strong>String Functions.</strong></p>
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
<p><strong>Aggregate Functions.</strong></p>
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
<p><strong>Mathematical Functions.</strong></p>
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
<p><strong>Date Functions.</strong></p>
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
<td colspan="3">Data Manipulation</td>
</tr>
<tr>
<td>Manipulating Tables and Data with SQL</td>
<td colspan="2"><p><strong>SQL can do more than retrieve data.</strong></p>
<ul>
<li><p>it can also:</p>
<ul>
<li><p>create and modify tables</p></li>
<li><p>insert new rows</p></li>
<li><p>update existing values</p></li>
<li><p>delete selected rows</p></li>
<li><p>remove all rows</p></li>
<li><p>remove entire tables</p></li>
</ul></li>
</ul>
<ul>
<li><p>these operations can permanently alter a database</p>
<ul>
<li><p>for this reason:</p>
<ul>
<li><p>database administrators usually restrict them to authorized users</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Two Types of Modification</td>
<td colspan="2"><table>
<colgroup>
<col style="width: 23%" />
<col style="width: 39%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Target</strong></th>
<th style="text-align: center;"><strong>Purpose</strong></th>
<th style="text-align: center;"><strong>Main commands</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Database structure</strong></td>
<td>Change tables, columns, and constraints</td>
<td>CREATE, ALTER, DROP</td>
</tr>
<tr>
<td><strong>Stored data</strong></td>
<td>Add, change, or remove rows</td>
<td>INSERT, UPDATE, DELETE, TRUNCATE</td>
</tr>
<tr>
<td colspan="3"><p><strong>The distinction between structure and data is important:</strong></p>
<ul>
<li><p>ALTER</p>
<ul>
<li><p>changes the table’s definition</p></li>
</ul></li>
<li><p>UPDATE</p>
<ul>
<li><p>changes values stored inside the table</p></li>
</ul></li>
<li><p>DROP</p>
<ul>
<li><p>removes the table itself</p></li>
</ul></li>
<li><p>TRUNCATE</p>
<ul>
<li><p>removes its rows but preserves the table</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>
<ul>
<li></li>
</ul></td>
</tr>
<tr>
<td>Creating a Table</td>
<td colspan="2"><p><strong>The CREATE TABLE statement defines a new table.</strong></p>
<ul>
<li><p>a table definition normally specifies:</p>
<ul>
<li><p>the table name</p></li>
<li><p>column names</p></li>
<li><p>data types</p></li>
<li><p>nullability rules</p></li>
<li><p>keys and other constraints</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image10.png" style="width:2.77988in;height:1.58621in" /></p></td>
</tr>
<tr>
<td>Column Names</td>
<td colspan="2"><p><strong>Each column must have a name.</strong></p>
<ul>
<li><p>a consistent naming convention improves:</p>
<ul>
<li><p>readability</p></li>
<li><p>maintainability</p></li>
</ul></li>
</ul>
<p><strong>Common conventions include:</strong></p>
<ul>
<li><p>using one consistent letter case</p></li>
<li><p>separating words with underscores</p></li>
<li><p>giving related columns similar names</p></li>
<li><p>avoiding ambiguous abbreviations</p></li>
<li><p>following the same convention across all tables</p></li>
</ul>
<p><strong>The specific convention matters less than applying it consistently.</strong></p></td>
</tr>
<tr>
<td>Data Types</td>
<td colspan="2"><ul>
<li><p>A column’s data type controls which values it can store.</p></li>
</ul>
<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Data type</strong></th>
<th style="text-align: center;"><strong>Typical purpose</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>INT</strong></td>
<td>Whole numbers</td>
</tr>
<tr>
<td><strong>VARCHAR(n)</strong></td>
<td>Variable-length text</td>
</tr>
<tr>
<td><strong>DATE</strong></td>
<td>Calendar dates</td>
</tr>
<tr>
<td><strong>TIMESTAMP</strong></td>
<td>Dates and times</td>
</tr>
<tr>
<td><strong>DECIMAL(p,s)</strong></td>
<td>Fixed-precision numeric values</td>
</tr>
<tr>
<td><strong>BOOLEAN</strong></td>
<td>True-or-false values</td>
</tr>
<tr>
<td colspan="2"><p><strong>The exact data types and syntax vary among database systems.</strong></p>
<ul>
<li><p>choosing appropriate data types improves:</p>
<ul>
<li><p>data validation</p></li>
<li><p>storage efficiency</p></li>
<li><p>query performance</p></li>
<li><p>consistency</p></li>
</ul></li>
</ul>
<p><strong>Compatibility with database functions.</strong></p></td>
</tr>
</tbody>
</table>
<ul>
<li></li>
</ul></td>
</tr>
<tr>
<td>Null Values</td>
<td colspan="2"><p><strong>A NULL value represents missing, unknown, or unavailable information.</strong></p>
<ul>
<li><p>by default, many columns permit null values</p></li>
<li><p>the NOT NULL constraint requires a value</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image11.png" style="width:1.98986in;height:0.47923in" /></p>
<ul>
<li><p>whether a column should permit NULL depends on the meaning of the data</p>
<ul>
<li><p>for example:</p></li>
<li><p>a patient identifier may always be required</p></li>
<li><p>a patient’s religion may be unknown or intentionally unreported</p></li>
</ul></li>
<li><p>a column omitted from an INSERT statement must either:</p>
<ul>
<li><p>permit NULL, or</p></li>
<li><p>have a default value</p></li>
<li><p>otherwise, the insertion will fail</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Primary-Key Constraints</td>
<td colspan="2"><p><strong>A primary key uniquely identifies each row.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image12.png" style="width:2.68788in;height:0.62509in" /></p>
<ul>
<li><p>this definition includes:</p>
<ul>
<li><p>a constraint name:</p>
<ul>
<li><p>PATIENT_DIMENSION_PK</p></li>
</ul></li>
<li><p>a constraint type:</p>
<ul>
<li><p>PRIMARY KEY</p></li>
</ul></li>
<li><p>a key column:</p>
<ul>
<li><p>PATIENT_NUM</p></li>
</ul></li>
</ul></li>
</ul>
<ul>
<li><p>naming constraints is useful because a constraint may later need to be:</p>
<ul>
<li><p>modified</p></li>
<li><p>removed</p></li>
<li><p>referenced in an error message</p></li>
<li><p>examined during maintenance</p></li>
</ul></li>
<li><p>a primary key normally enforces:</p>
<ul>
<li><p>uniqueness</p></li>
<li><p>non-null values</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Altering a Table</td>
<td colspan="2"><p><strong>The ALTER TABLE statement changes an existing table’s structure.</strong></p>
<ul>
<li><p>it does not modify values stored in existing rows unless the structural change causes a database-specific conversion</p></li>
</ul></td>
</tr>
<tr>
<td>Adding a Column</td>
<td colspan="2"><p><strong>This adds DATE_OF_BIRTH to the table.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image13.png" style="width:2.43784in;height:0.65634in" /></p>
<ul>
<li><p>existing rows will generally receive NULL for the new column unless:</p>
<ul>
<li><p>a default value is supplied, or</p></li>
<li><p>the database applies another defined rule</p></li>
</ul></li>
</ul>
<p><strong>Adding a NOT NULL column to a populated table may require a default value or a staged migration.</strong></p></td>
</tr>
<tr>
<td>Changing a Column</td>
<td colspan="2"><p><strong>This changes the column’s data type.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image14.png" style="width:3.02126in;height:0.67718in" /></p>
<ul>
<li><p>the exact syntax differs across database systems</p></li>
<li><p>a type change may fail if existing values cannot be converted safely</p></li>
<li><p>before changing a type, consider whether:</p>
<ul>
<li><p>current values are compatible</p></li>
<li><p>precision could be lost</p></li>
<li><p>applications depend on the current type</p></li>
<li><p>indexes or constraints use the column</p></li>
<li><p>a backup or rollback plan exists</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Removing a Column</td>
<td colspan="2"><p><strong>This removes the column and its stored values.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image15.png" style="width:2.19822in;height:0.65634in" /></p>
<ul>
<li><p>dropping a column may also affect:</p>
<ul>
<li><p>constraints</p></li>
<li><p>indexes</p></li>
<li><p>views</p></li>
<li><p>stored procedures</p></li>
<li><p>reports</p></li>
<li><p>application code</p></li>
</ul></li>
</ul>
<p><strong>Dependencies should be identified before the change is applied.</strong></p></td>
</tr>
<tr>
<td>Dropping a Table</td>
<td colspan="2"><p><strong>The DROP TABLE statement removes an entire table.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image16.png" style="width:1.72941in;height:0.44798in" /></p>
<ul>
<li><p><strong>This may remove:</strong></p>
<ul>
<li><p><strong>all rows</strong></p></li>
<li><p><strong>column definitions</strong></p></li>
<li><p><strong>constraints</strong></p></li>
<li><p><strong>indexes</strong></p></li>
<li><p><strong>associated metadata</strong></p></li>
</ul></li>
<li><p><strong>recovery depends on:</strong></p>
<ul>
<li><p><strong>database system</strong></p></li>
<li><p><strong>transaction configuration</strong></p></li>
<li><p><strong>backups</strong></p></li>
<li><p><strong>administrative policies</strong></p></li>
</ul></li>
</ul>
<p><strong>DROP TABLE should therefore be treated as a potentially destructive operation.</strong></p></td>
</tr>
<tr>
<td>SQL Injection Connection</td>
<td colspan="2"><p><strong>The well-known XKCD “Bobby Tables” comic uses a malicious name containing a command similar to:</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image17.png" style="width:1.70857in;height:0.41672in" /></p>
<ul>
<li><p>if an application directly combines user input with SQL text</p>
<ul>
<li><p>the input may be interpreted as executable SQL</p></li>
</ul></li>
<li><p>the correct defense is not merely removing suspicious words</p>
<ul>
<li><p>applications should use:</p>
<ul>
<li><p>parameterized queries</p></li>
<li><p>prepared statements</p></li>
<li><p>input validation</p></li>
<li><p>least-privilege database accounts</p></li>
<li><p>appropriate error handling</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>User input should never be inserted directly into executable SQL strings.</strong></p></td>
</tr>
<tr>
<td>Inserting Data</td>
<td colspan="2"><p>The INSERT statement adds new rows.</p>
<p><img src="generated_media\DATA715_week01_notes\media\image18.png" style="width:2.18773in;height:2.20456in" /></p>
<ul>
<li><p>the listed values correspond to the columns in the same order</p></li>
</ul>
<ul>
<li><p>an insertion must satisfy the table’s rules:</p>
<ul>
<li><p>column names must exist</p></li>
<li><p>values must use compatible data types</p></li>
<li><p>required columns must receive values</p></li>
<li><p>primary-key values must be unique</p></li>
<li><p>foreign-key relationships must be valid</p></li>
<li><p>check constraints must be satisfied</p></li>
</ul></li>
</ul>
<p><strong>It is good practice to list column names explicitly. This makes the statement clearer and less dependent on the physical order of columns.</strong></p></td>
</tr>
<tr>
<td>Deleting Rows</td>
<td colspan="2"><p><strong>The DELETE statement removes rows while preserving the table’s structure.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image19.png" style="width:3.57342in;height:0.63551in" /></p>
<ul>
<li><p>only rows satisfying the WHERE condition are removed</p></li>
<li><p>function names and date syntax differ across database platforms</p>
<ul>
<li><p>some systems use:</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image20.png" style="width:1.62523in;height:0.44798in" /></p></td>
</tr>
<tr>
<td>Importance of the WHERE Clause</td>
<td colspan="2"><p><strong>A DELETE statement without a WHERE clause removes every row:</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image21.png" style="width:2.13572in;height:0.46882in" /></p>
<ul>
<li><p>a filtered deletion is usually safer:</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image22.png" style="width:2.18781in;height:0.64592in" /></p>
<ul>
<li><p>before executing a destructive statement, the condition can be tested with SELECT:</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image23.png" style="width:2.17739in;height:0.9793in" /></p>
<p><strong>This confirms which rows will be affected.</strong></p></td>
</tr>
<tr>
<td>Updating Existing Data</td>
<td colspan="2"><p><strong>The UPDATE statement changes stored values.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image24.png" style="width:2.38575in;height:0.8647in" /></p>
<ul>
<li><p>this changes PROVIDER_NAME only for rows matching the condition</p></li>
</ul></td>
</tr>
<tr>
<td>Selecting Rows Precisely</td>
<td colspan="2"><p>Updates should use conditions that identify the intended rows as precisely as possible.</p>
<ul>
<li><p>preferred:</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image25.png" style="width:2.417in;height:0.84387in" /></p>
<ul>
<li><p>potentially unsafe:</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image26.png" style="width:2.54202in;height:0.83345in" /></p>
<ul>
<li><p>names are not necessarily unique</p>
<ul>
<li><p>the second statement could modify multiple unrelated providers who share the same surname</p></li>
</ul></li>
</ul>
<p><strong>Primary keys or other unique identifiers are generally safer for targeted changes.</strong></p></td>
</tr>
<tr>
<td>Updating Without a Filter</td>
<td colspan="2"><p><strong>An UPDATE statement without a WHERE clause modifies every row:</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image27.png" style="width:2.38575in;height:0.69801in" /></p>
<ul>
<li><p>this may be intentional, but it is often a serious error</p></li>
<li><p>before updating data:</p>
<ul>
<li><p>write the intended WHERE condition</p></li>
<li><p>test it with SELECT</p></li>
<li><p>confirm the expected row count</p></li>
<li><p>execute the update within a transaction when supported</p></li>
<li><p>validate the result</p></li>
<li><p>commit only after verification</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Truncating a Table</td>
<td><p><strong>The TRUNCATE TABLE statement removes all rows while preserving the table definition.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image28.png" style="width:2.37533in;height:0.43756in" /></p>
<ul>
<li><p>the table remains available, but it becomes empty</p></li>
<li><p>depending on the database system, truncation may also reset:</p>
<ul>
<li><p>identity counters</p></li>
<li><p>auto-increment sequences</p></li>
<li><p>storage allocations</p></li>
</ul></li>
</ul></td>
<td></td>
</tr>
<tr>
<td>DELETE, TRUNCATE, and DROP</td>
<td colspan="2"><table>
<colgroup>
<col style="width: 26%" />
<col style="width: 25%" />
<col style="width: 22%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Command</strong></th>
<th style="text-align: right;"><strong>Removes selected rows</strong></th>
<th style="text-align: right;"><strong>Removes all rows</strong></th>
<th style="text-align: right;"><strong>Preserves table structure</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>DELETE ... WHERE</strong></td>
<td style="text-align: right;">Yes</td>
<td style="text-align: right;">Only if all rows match</td>
<td style="text-align: right;">Yes</td>
</tr>
<tr>
<td><strong>DELETE without WHERE</strong></td>
<td style="text-align: right;">No selective filter</td>
<td style="text-align: right;">Yes</td>
<td style="text-align: right;">Yes</td>
</tr>
<tr>
<td><strong>TRUNCATE TABLE</strong></td>
<td style="text-align: right;">No</td>
<td style="text-align: right;">Yes</td>
<td style="text-align: right;">Yes</td>
</tr>
<tr>
<td><strong>DROP TABLE</strong></td>
<td style="text-align: right;">Not applicable</td>
<td style="text-align: right;">Yes</td>
<td style="text-align: right;">No</td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>DELETE</p>
<ul>
<li><p>can remove selected rows</p></li>
<li><p>supports a WHERE clause</p></li>
<li><p>usually records row-level changes</p></li>
<li><p>may trigger delete-related database logic</p></li>
<li><p>can be slower when removing every row from a large table</p></li>
</ul></li>
<li><p>TRUNCATE</p>
<ul>
<li><p>removes all rows</p></li>
<li><p>does not support row filtering</p></li>
<li><p>is generally faster than deleting rows individually</p></li>
<li><p>usually performs less row-level logging</p></li>
<li><p>may have stricter permission and foreign-key restrictions</p></li>
</ul></li>
<li><p>DROP</p>
<ul>
<li><p>removes the complete table</p></li>
<li><p>removes its structure and stored data</p></li>
<li><p>may break dependent database objects and applications</p></li>
</ul></li>
</ul>
<p><strong>Transaction and recovery behavior varies by database system. TRUNCATE and DROP should not be assumed to be reversible.</strong></p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>Safe Data-Modification Practices</td>
<td colspan="2"><p><strong>Before running UPDATE, DELETE, TRUNCATE, ALTER, or DROP:</strong></p>
<ul>
<li><p>confirm that the correct database is selected.</p></li>
<li><p>confirm the schema and table name.</p></li>
<li><p>inspect the affected rows with SELECT.</p></li>
<li><p>use primary keys or unique identifiers where possible.</p></li>
<li><p>check the expected number of affected rows.</p></li>
<li><p>identify dependent applications and database objects.</p></li>
<li><p>use transactions when the database supports them.</p></li>
<li><p>maintain current backups.</p></li>
<li><p>follow change-review and approval procedures.</p></li>
<li><p>grant users only the permissions required for their roles.</p></li>
</ul>
<p><strong>A typical controlled modification uses a transaction:</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image29.png" style="width:2.82562in;height:1.7574in" /></p>
<ul>
<li><p>if validation fails:</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image30.png" style="width:1.00014in;height:0.39589in" /></p>
<p><strong>Transaction syntax and support depend on the database platform and operation.</strong></p></td>
</tr>
<tr>
<td>Command Summary</td>
<td colspan="2"><table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Command</strong></th>
<th style="text-align: center;"><strong>Purpose</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>CREATE TABLE</strong></td>
<td>Create a new table</td>
</tr>
<tr>
<td><strong>ALTER TABLE</strong></td>
<td>Change a table’s structure</td>
</tr>
<tr>
<td><strong>DROP TABLE</strong></td>
<td>Remove a table and its contents</td>
</tr>
<tr>
<td><strong>INSERT</strong></td>
<td>Add new rows</td>
</tr>
<tr>
<td><strong>UPDATE</strong></td>
<td>Change values in existing rows</td>
</tr>
<tr>
<td><strong>DELETE</strong></td>
<td>Remove selected or all rows</td>
</tr>
<tr>
<td><strong>TRUNCATE TABLE</strong></td>
<td>Efficiently remove all rows while preserving the table</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td colspan="3">JOINs</td>
</tr>
<tr>
<td>Joining Tables with SQL</td>
<td colspan="2"><p><strong>A SQL join combines related data from two or more tables.</strong></p>
<ul>
<li><p>joins are fundamental to relational databases because normalized data is usually distributed across multiple tables</p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>a PATIENT table stores patient information</p></li>
<li><p>a VISIT table stores clinical visits</p></li>
<li><p>a PROVIDER table stores provider information</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>A join can combine these tables into one query result.</strong></p></td>
</tr>
<tr>
<td>Joins and Set Theory</td>
<td colspan="2"><p><strong>Joins are often introduced using set intersections.</strong></p>
<ul>
<li><p>suppose one set contains mammals and another contains pets</p>
<ul>
<li><p>the animals that belong to both sets might include:</p>
<ul>
<li><p>dogs</p></li>
<li><p>cats</p></li>
<li><p>guinea pigs</p></li>
</ul></li>
</ul></li>
<li><p>the overlap resembles an inner join because only matching members are retained</p>
<ul>
<li><p>however, SQL joins operate on rows and matching conditions</p></li>
<li><p>they are not exactly equivalent to mathematical set operations because:</p>
<ul>
<li><p>SQL tables may contain duplicate rows</p></li>
<li><p>one row may match multiple rows</p></li>
<li><p>SQL uses NULL to represent missing values</p></li>
<li><p>join cardinality depends on key relationships</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Join Keys</td>
<td colspan="2"><p><strong>Tables are usually connected through primary-key and foreign-key relationships.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image31.png" style="width:1.60439in;height:0.44798in" /></p></td>
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
<th>Foreign Key</th>
<th><p>A foreign key references a key in another table.</p>
<p><img src="generated_media\DATA715_week01_notes\media\image32.png" style="width:1.45854in;height:0.44798in" /></p>
<ul>
<li><p>the relationship can be expressed as:</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image33.png" style="width:2.93791in;height:0.43756in" /></p>
<ul>
<li><p>database documentation is important because it identifies:</p>
<ul>
<li><p>primary keys</p></li>
<li><p>foreign keys</p></li>
<li><p>table relationships</p></li>
<li><p>expected relationship cardinalities</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Table Aliases</td>
<td><p><strong>Aliases assign short names to tables within a query.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image34.png" style="width:1.54188in;height:0.48965in" /></p>
<ul>
<li><p>the alias P can then qualify columns:</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image35.png" style="width:1.38561in;height:0.37505in" /></p>
<ul>
<li><p>aliases are especially useful when:</p>
<ul>
<li><p>several tables contain columns with the same name</p></li>
<li><p>queries contain many joins</p></li>
<li><p>a table is joined to itself</p></li>
<li><p>fully qualified table names are long</p></li>
<li><p><img src="generated_media\DATA715_week01_notes\media\image36.png" style="width:1.8125in;height:1.01806in" />example:</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Two Ways to Write Joins</td>
<td><p><strong>SQL supports an older implicit syntax and a modern explicit syntax.</strong></p>
<ul>
<li><p>Implicit Join Syntax</p>
<ul>
<li><p>the older form lists tables in the FROM clause and places the join condition in WHERE</p></li>
</ul></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image37.png" style="width:2.58842in;height:1.3456in" /></p>
<ul>
<li><p>this form separates:</p>
<ul>
<li><p>ON:</p>
<ul>
<li><p>how tables are related</p></li>
</ul></li>
<li><p>WHERE:</p>
<ul>
<li><p>which joined rows should remain</p></li>
</ul></li>
</ul></li>
<li><p>explicit joins generally improve:</p>
<ul>
<li><p>readability</p></li>
<li><p>maintainability</p></li>
<li><p>error detection</p></li>
<li><p>support for outer joins</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Joining Multiple Tables</td>
<td><p>Additional tables can be connected by adding more join clauses.</p>
<p><img src="generated_media\DATA715_week01_notes\media\image38.png" style="width:2.38171in;height:1.62959in" /></p>
<ul>
<li><p>this query connects:</p>
<ul>
<li><p>patients to visits through PATIENT_ID</p></li>
<li><p>visits to providers through PROVIDER_ID</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>The <span class="math inline">$\textit{\textbf{(}}\mathbf{n - 1}\textit{\textbf{)}}$</span> Heuristic</td>
<td><p><strong>For a simple connected chain of</strong> <span class="math inline">$\textit{\textbf{(}}\mathbf{n}\textit{\textbf{)}}$</span> <strong>tables, at least</strong> <span class="math inline">$\textit{\textbf{(}}\mathbf{n - 1}\textit{\textbf{)}}$</span> <strong>join relationships are normally required.</strong></p>
<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"><strong>Tables</strong></th>
<th style="text-align: right;"><strong>Minimum connecting relationships</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: right;"><strong>2</strong></td>
<td style="text-align: right;">1</td>
</tr>
<tr>
<td style="text-align: right;"><strong>3</strong></td>
<td style="text-align: right;">2</td>
</tr>
<tr>
<td style="text-align: right;"><strong>4</strong></td>
<td style="text-align: right;">3</td>
</tr>
</tbody>
</table>
<ul>
<li><p>this is a useful check, but not a universal SQL rule</p></li>
<li><p>a query may require additional conditions when:</p>
<ul>
<li><p>tables use composite keys</p></li>
<li><p>several relationships exist between the same tables</p></li>
<li><p>date ranges or version columns participate in the join</p></li>
<li><p>the join graph contains multiple valid paths</p></li>
</ul></li>
</ul>
<p><strong>The actual requirement is that every table be connected correctly according to the data model.</strong></p></td>
</tr>
<tr>
<td>Join Cardinality</td>
<td><p><strong>The number of output rows depends on how many matches exist.</strong></p>
<ul>
<li><p>one-to-one</p>
<ul>
<li><p>each row matches no more than one row in the other table</p></li>
</ul></li>
<li><p>one-to-many</p>
<ul>
<li><p>one row may match several rows</p></li>
<li><p>for example:</p>
<ul>
<li><p>one patient may have several visits</p></li>
<li><p>the patient’s name will appear once for every matching visit</p></li>
</ul></li>
</ul></li>
<li><p>many-to-many</p>
<ul>
<li><p>several rows in each table may match several rows in the other table</p></li>
<li><p>this can produce a much larger result than either source table</p></li>
<li><p>many-to-many relationships are often represented through a junction table</p></li>
</ul></li>
<li><p>understanding cardinality helps distinguish:</p>
<ul>
<li><p>expected duplicate-looking rows</p></li>
<li><p>incorrect join conditions</p></li>
<li><p>unexpected row multiplication</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Inner Join</td>
<td><p><strong>An INNER JOIN retains only rows that satisfy the join condition.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image39.png" style="width:2.48372in;height:1.27734in" /></p>
<ul>
<li><p><strong>the result includes:</strong></p>
<ul>
<li><p><strong>patients with matching visits</strong></p></li>
<li><p><strong>one row for each matching patient-visit combination</strong></p></li>
</ul></li>
<li><p><strong>the result excludes:</strong></p>
<ul>
<li><p><strong>patients without visits</strong></p></li>
<li><p><strong>visits without matching patients</strong></p></li>
</ul></li>
</ul>
<p>For a simple equality condition, reversing the order of the two tables does not normally change which matched combinations appear.</p></td>
</tr>
<tr>
<td>Left Join</td>
<td><p><strong>A LEFT JOIN, also called a left outer join, retains:</strong></p>
<ul>
<li><p>every row from the left table</p></li>
<li><p>matching rows from the right table</p></li>
<li><p>NULL values where no right-table match exists</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image40.png" style="width:2.29429in;height:1.21064in" /></p>
<ul>
<li><p>this query returns every patient</p>
<ul>
<li><p>patients without visits remain in the result</p></li>
<li><p>but their visit fields are NULL</p></li>
</ul></li>
<li><p>a left join is useful for questions such as:</p>
<ul>
<li><p>which patients have no visits?</p></li>
<li><p>which customers have never placed an order?</p></li>
<li><p>which employees have no assigned supervisor?</p></li>
<li><p>which products have no sales?</p></li>
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
<th>Finding Unmatched Rows</th>
<th><p>A left join can identify rows without a corresponding match.</p>
<p><img src="generated_media\DATA715_week01_notes\media\image41.png" style="width:2.36092in;height:1.45693in" /></p>
<ul>
<li><p>this pattern is called an anti-join</p></li>
<li><p>it returns patients who have no matching visit</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Right Join</td>
<td><p><strong>A RIGHT JOIN, or right outer join, retains every row from the right table.</strong></p>
<p><img src="generated_media\DATA715_week01_notes\media\image42.png" style="width:2.52327in;height:1.31401in" /></p>
<ul>
<li><p>This can produce the same result as:</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image43.png" style="width:2.36474in;height:1.20771in" /></p>
<ul>
<li><p>many developers primarily use left joins and reorder the tables when necessary</p>
<ul>
<li><p>this creates a consistent reading rule:</p>
<ul>
<li><p>preserve every row from the table written on the left</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>Right joins are valid, but not every database system supports them.</strong></p></td>
</tr>
<tr>
<td>Full Outer Join</td>
<td><p><strong>A FULL OUTER JOIN preserves:</strong></p>
<ul>
<li><p>every row from the left table</p></li>
<li><p>every row from the right table</p></li>
<li><p>combined rows where the join condition matches</p></li>
<li><p>NULL values on the missing side of unmatched rows</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image44.png" style="width:2.48836in;height:1.29828in" /></p>
<ul>
<li><p>this result contains:</p>
<ul>
<li><p>patients with visits</p></li>
<li><p>patients without visits</p></li>
<li><p>visits without matching patients</p></li>
</ul></li>
<li><p>full outer joins are useful for:</p>
<ul>
<li><p>comparing datasets</p></li>
<li><p>reconciling records</p></li>
<li><p>detecting missing relationships</p></li>
<li><p>identifying additions and removals between data versions</p></li>
</ul></li>
</ul>
<p><strong>Some database systems do not directly support FULL OUTER JOIN.</strong></p></td>
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
<th>Cartesian Product</th>
<th><p>A Cartesian product combines every row from one table with every row from another table.</p>
<ul>
<li><p>the explicit syntax is:</p></li>
</ul>
<p><img src="generated_media\DATA715_week01_notes\media\image45.png" style="width:1.71858in;height:0.77007in" /></p>
<ul>
<li><p>If the first table has <span class="math inline">$\textit{\textbf{(}}\mathbf{n}\textit{\textbf{)}}$</span> rows and the second has <span class="math inline">$\textit{\textbf{(}}\mathbf{m}\textit{\textbf{)}}$</span> rows, the result contains <span class="math inline"><strong>n</strong>  <strong>×</strong> <strong>m</strong></span> rows</p>
<ul>
<li><p>for example:</p></li>
</ul></li>
</ul>
<p><span class="math display"><strong>5</strong><strong>,</strong> <strong>000</strong><strong>,</strong> <strong>000</strong>  <strong>×</strong> <strong>45</strong><strong>,</strong> <strong>000</strong><strong>,</strong> <strong>00</strong> <strong>=</strong> <strong>225</strong><strong>,</strong> <strong>000</strong><strong>,</strong> <strong>000</strong><strong>,</strong> <strong>000</strong><strong>,</strong> <strong>000</strong></span></p>
<ul>
<li><p>that is 225 trillion row combinations!</p></li>
</ul>
<p>A Cartesian product can occur accidentally when using implicit join syntax without a join condition:</p>
<p><img src="generated_media\DATA715_week01_notes\media\image46.png" style="width:1.75024in;height:0.77094in" /></p>
<ul>
<li><p>it can also occur when a table is added to a query but never connected to the other tables</p></li>
<li><p>possible consequences include:</p>
<ul>
<li><p>extremely large result sets</p></li>
<li><p>long-running queries</p></li>
<li><p>excessive memory consumption</p></li>
<li><p>high CPU and storage use</p></li>
<li><p>database instability</p></li>
<li><p>unexpected cloud costs</p></li>
</ul></li>
</ul>
<ul>
<li><p>across join is not inherently incorrect</p></li>
<li><p>it is useful when every possible combination is intentionally required.</p></li>
</ul>
<p>The danger is producing one unintentionally.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Self-Joins</td>
<td><p><strong>A self-join joins a table to another logical instance of itself.</strong></p>
<ul>
<li><p>this is useful when rows in a table refer to other rows in the same table</p></li>
<li><p>consider an employee table:</p></li>
</ul>
<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Column</strong></th>
<th style="text-align: center;"><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EMPLOYEE_ID</strong></td>
<td>Unique employee identifier</td>
</tr>
<tr>
<td><strong>EMPLOYEE_NAME</strong></td>
<td>Employee’s name</td>
</tr>
<tr>
<td><strong>MANAGER_ID</strong></td>
<td>Identifier of the employee’s manager</td>
</tr>
<tr>
<td colspan="2"><ul>
<li><p>managers are also employees</p>
<ul>
<li><p>so both employees and managers appear in the same table</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td colspan="2">Introduction to OMOP</td>
</tr>
<tr>
<td>What Is OMOP?</td>
<td><p><strong>OMOP is a healthcare Common Data Model (CDM).</strong></p>
<ul>
<li><p>a common data model defines a shared way for different organizations to structure their data</p>
<ul>
<li><p>UNC and Duke can store healthcare data using OMOP</p></li>
<li><p>researchers at both institutions can then use similar queries and analytical code</p></li>
</ul></li>
</ul>
<p><strong>Main Benefit.</strong></p>
<ul>
<li><p>different healthcare institutions can represent similar information in a standardized structure</p></li>
<li><p>this makes:</p>
<ul>
<li><p>data sharing easier</p></li>
<li><p>multi-institution research easier</p></li>
<li><p>analytical code more reusable</p></li>
<li><p>and healthcare data more consistent</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Understanding the Database Diagram</td>
<td><p><strong>A database diagram shows:</strong></p>
<ul>
<li><p>which tables exist</p></li>
<li><p>how those tables connect</p></li>
</ul>
<p><strong>Some diagrams also show:</strong></p>
<ul>
<li><p>attributes</p></li>
<li><p>primary keys</p></li>
<li><p>foreign keys</p></li>
<li><p>detailed table relationships</p></li>
</ul>
<p><strong>The OMOP diagram introduced here is intentionally high-level.</strong></p></td>
</tr>
<tr>
<td>Core OMOP Structure</td>
<td><p><strong>Two tables form the foundation of much of the model:</strong></p>
<p><strong>PERSON.</strong></p>
<ul>
<li><p>stores information about patients</p></li>
<li><p>each patient should have:</p>
<ul>
<li><p>one unique record</p></li>
<li><p>identified by a unique person identifier</p></li>
</ul></li>
<li><p>the person table can also connect to information about:</p>
<ul>
<li><p>locations</p></li>
<li><p>healthcare providers</p></li>
<li><p>care sites</p></li>
</ul></li>
</ul>
<p><strong>VISIT_OCCURRENCE.</strong></p>
<ul>
<li><p>the VISIT_OCCURRENCE table stores information about healthcare visits or encounters</p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>emergency department visits</p></li>
<li><p>hospital admissions</p></li>
<li><p>outpatient appointments</p></li>
<li><p>eye examinations</p></li>
<li><p>other encounters with the healthcare system</p></li>
</ul></li>
</ul></li>
<li><p>One patient can have many visits</p>
<ul>
<li><p>therefore:</p>
<ul>
<li><p>person_id may appear many times</p></li>
<li><p>while visit_occurrence_id uniquely identifies each visit</p></li>
</ul></li>
</ul></li>
</ul>
<ul>
<li><p>each visit can produce many additional healthcare records</p></li>
</ul>
<p><strong>CONDITION_OCCURRENCE.</strong></p>
<ul>
<li><p>the CONDITION_OCCURRENCE table stores diagnoses and medical conditions</p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>diseases</p></li>
<li><p>medical conditions</p></li>
<li><p>diagnoses associated with routine well visits</p></li>
</ul></li>
<li><p>a patient can have many diagnoses</p></li>
<li><p>a single visit can also contain multiple diagnoses</p>
<ul>
<li><p>therefore:</p>
<ul>
<li><p>diagnoses are not unique by patient or by visit</p></li>
</ul></li>
</ul></li>
</ul></li>
</ul>
<p><strong>DRUG_EXPOSURE.</strong></p>
<ul>
<li><p>the DRUG_EXPOSURE table stores information about medications</p>
<ul>
<li><p>it may contain:</p>
<ul>
<li><p>prescriptions written during care</p></li>
<li><p>medications currently being taken</p></li>
<li><p>medication history reported by the patient</p></li>
</ul></li>
</ul></li>
<li><p>a single medication may have many different codes</p>
<ul>
<li><p>this can happen because drugs differ by:</p>
<ul>
<li><p>formulation</p></li>
<li><p>dosage</p></li>
<li><p>combination</p></li>
<li><p>product</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>PROCEDURE_OCCURRENCE.</strong></p>
<ul>
<li><p>the PROCEDURE_OCCURRENCE table stores medical procedures</p></li>
<li><p>procedures are not limited to surgery</p>
<ul>
<li><p>they may include:</p>
<ul>
<li><p>surgery</p></li>
<li><p>injections</p></li>
<li><p>infusions</p></li>
<li><p>ultrasounds</p></li>
<li><p>other clinical procedures</p></li>
</ul></li>
</ul></li>
<li><p>different versions of the same general procedure can receive different standardized identifiers</p></li>
</ul>
<p><strong>MEASUREMENT.</strong></p>
<ul>
<li><p>the MEASUREMENT table stores clinical measurements</p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>blood pressure</p></li>
<li><p>laboratory results</p></li>
<li><p>body temperature</p></li>
<li><p>weight</p></li>
<li><p>height</p></li>
</ul></li>
</ul></li>
<li><p>measurements usually require three pieces of information:</p>
<ul>
<li><p>what was measured</p></li>
<li><p>the measured value</p></li>
<li><p>the unit</p></li>
</ul></li>
<li><p>for example:</p>
<ul>
<li><p><strong>measurement</strong>: body temperature</p></li>
<li><p><strong>value</strong>: 103</p></li>
<li><p><strong>unit</strong>: degrees Fahrenheit</p></li>
</ul></li>
<li><p>knowing only that a temperature was measured is not enough</p>
<ul>
<li><p>the actual value and unit are needed for analysis</p></li>
</ul></li>
</ul>
<p><strong>OBSERVATION.</strong></p>
<ul>
<li><p>the OBSERVATION table stores information that does not fit naturally into the other OMOP tables</p></li>
<li><p>the lecture describes it as something of a “junk bucket”</p></li>
<li><p>examples may include:</p>
<ul>
<li><p>medical history</p></li>
<li><p>family history</p></li>
<li><p>social factors</p></li>
<li><p>numerical values</p></li>
<li><p>text strings</p></li>
</ul></li>
</ul>
<p><strong>The table is intentionally flexible because it may need to store many unrelated types of information.</strong></p></td>
</tr>
<tr>
<td>OMOP Uses Codes Instead of Human Reeadble Text</td>
<td><p><strong>A major feature of OMOP is its heavy use of coded values and identifiers.</strong></p>
<ul>
<li><p>instead of storing:</p>
<ul>
<li><p>female</p></li>
</ul></li>
<li><p>the database might store:</p>
<ul>
<li><p>8532</p></li>
</ul></li>
<li><p>instead of storing:</p>
<ul>
<li><p>endometriosis</p></li>
</ul></li>
<li><p>the database might store</p>
<ul>
<li><p>a numerical concept ID</p></li>
</ul></li>
</ul>
<p><strong>The meaning of these codes is retrieved through lookup tables and standardized vocabularies.</strong></p>
<ul>
<li><p>this is common in well-structured databases</p></li>
<li><p>core tables often contain compact identifiers rather than long human-readable labels</p></li>
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
<th>Why Use Codes?</th>
<th><p>Healthcare contains enormous numbers of:</p>
<ul>
<li><p>diagnoses</p></li>
<li><p>medications</p></li>
<li><p>procedures</p></li>
<li><p>measurement types</p></li>
<li><p>variations of each</p></li>
</ul>
<p>Using standardized identifiers helps keep the database:</p>
<ul>
<li><p>organized</p></li>
<li><p>consistent</p></li>
<li><p>searchable</p></li>
<li><p>interoperable</p></li>
</ul>
<p>Lookup tables provide the human-readable meaning of those identifiers.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Patient Data Accumulates Over Time</td>
<td><p><strong>The lecture uses a hypothetical patient to show how healthcare data develops across a timeline.</strong></p>
<ul>
<li><p>the patient experiences:</p>
<ul>
<li><p>an initial complaint of dysmenorrhea</p></li>
<li><p>missed work</p></li>
<li><p>medications</p></li>
<li><p>clinical visits</p></li>
<li><p>examinations</p></li>
<li><p>an ultrasound</p></li>
<li><p>diagnosis of an ovarian cyst</p></li>
<li><p>severe pain and hospitalization</p></li>
<li><p>diagnosis of endometriosis</p></li>
</ul></li>
<li><p>each event creates additional data that can be stored in OMOP</p></li>
</ul>
<p><strong>These records may later support both patient care and research.</strong></p></td>
</tr>
<tr>
<td>Why Collect All This Data?</td>
<td><p><strong>Healthcare data supports two major purposes.</strong></p>
<p><strong>CLINICAL CARE.</strong></p>
<ul>
<li><p>historical data allows healthcare providers to understand:</p>
<ul>
<li><p>what has happened to the patient</p></li>
<li><p>previous diagnoses</p></li>
<li><p>previous treatments</p></li>
<li><p>medications</p></li>
<li><p>procedures</p></li>
<li><p>other relevant medical history</p></li>
</ul></li>
<li><p>this information can improve future care</p></li>
</ul>
<p><strong>RESEARCH AND OPERATIONS.</strong></p>
<ul>
<li><p>healthcare data can also support:</p>
<ul>
<li><p>clinical research</p></li>
<li><p>hospital planning</p></li>
<li><p>staffing decisions</p></li>
<li><p>treatment research</p></li>
<li><p>analysis of diseases and outcomes</p></li>
</ul></li>
<li><p>historical de-identified records could be used to study the treatment of ovarian cysts or endometriosis</p></li>
</ul>
<p><strong>IMPORTANT DATABASE RELATIONSHIPS.</strong></p>
<ul>
<li><p>a patient:</p>
<ul>
<li><p>can have many visits</p></li>
<li><p>may interact with the healthcare system many times</p></li>
<li><p>can have many diagnoses</p></li>
<li><p>may develop many conditions over time</p></li>
</ul></li>
<li><p>one visit:</p>
<ul>
<li><p>can have many diagnoses</p></li>
<li><p>can have many procedures</p></li>
<li><p>can have many measurements</p></li>
<li><p>several procedures may occur</p></li>
<li><p>many clinical measurements may be collected</p></li>
<li><p>several conditions may be recorded</p></li>
</ul></li>
<li><p>codes :</p>
<ul>
<li><p>are translated into meaningful clinical concepts using:</p>
<ul>
<li><p>lookup tables</p></li>
<li><p>standardized vocabularies</p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>As tables are connected, the amount of available data can grow rapidly.</strong></p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>OMOP Resources</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>The OMOP data model is managed by the OHDSI Consortium. OHDSI has a ton of great resources and online documentation that you may find useful, including:</p>
<ul>
<li><p><a href="https://ohdsi.github.io/TheBookOfOhdsi/">Book of OHDSI</a></p>
<ul>
<li><p>part textbook on how OMOP works</p></li>
<li><p>part documentation of the OMOP data model</p></li>
<li><p>if you like to learn through reading, this is a great way to get started with using and understanding OMOP</p></li>
</ul></li>
<li><p><a href="https://academy.ehden.eu/">EHDEN Academy</a></p>
<ul>
<li><p>offers a number of detailed video lectures covering how to use OMOP</p></li>
<li><p>you can practice many of the exercises from these lessons in our class database</p></li>
</ul></li>
<li><p><a href="https://ohdsi.github.io/CommonDataModel/cdm53.html">OMOP documentation</a></p>
<ul>
<li><p>is a useful reference that defines each field across all OMOP tables</p></li>
</ul></li>
<li><p><a href="https://athena.ohdsi.org/search-terms/start">ATHENA</a></p>
<ul>
<li><p>is an online tool where you can browse, search, and filter all the medical terminology concepts used in OMOP</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td></td>
</tr>
</tbody>
</table>
