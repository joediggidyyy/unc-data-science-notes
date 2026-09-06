> Markdown version for convenient browsing. Original files:
> - PDF: [DATA715_week02_notes.pdf](../DATA715_week02_notes.pdf)
> - DOCX: [DATA715_week02_notes.docx](DATA715_week02_notes.docx)

---

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 2%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Create a Local Database from Scratch</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Overview</td>
<td colspan="2" style="text-align: right;"><em>5 Sept 2026</em></td>
</tr>
<tr>
<td colspan="4"><ul>
<li><p>install and create a database</p></li>
<li><p>create tables in a database</p></li>
<li><p>load data into a database</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Platform Update</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><p>For this module, remember:</p>
<ul>
<li><p>treat references to PostgreSQL or Postgres as references to MariaDB, unless SQLite is explicitly specified</p></li>
<li><p>treat references to pgAdmin as references to DBeaver</p></li>
<li><p>use MariaDB as the default database platform</p></li>
<li><p>use SQLite only when an activity specifically instructs you to do so</p></li>
<li><p>do not install PostgreSQL or pgAdmin for this module</p></li>
</ul>
<p><img src="generated_media\DATA715_week02_notes\media\image1.jpeg" style="width:4.57465in;height:2.57461in" /></p>
<p>ChatGPT 5.6 Sol</p></td>
</tr>
</tbody>
</table>

**
**

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">MariaDB Server Setup Links</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p>local guide:</p>
<p><a href="../resources/DATA715_CoursePreparation.pdf">notes\Fall_2026\DATA715\resources/DATA715_CoursePreparation.pdf</a></p></td>
</tr>
<tr>
<td colspan="2">Installing MariaDB Server Guide</td>
</tr>
<tr>
<td colspan="2"><a href="https://mariadb.com/docs/server/mariadb-quickstart-guides/installing-mariadb-server-guide">https://mariadb.com/docs/server/mariadb-quickstart-guides/installing-mariadb-server-guide</a></td>
</tr>
<tr>
<td colspan="2">Connecting to MariaDB Guide</td>
</tr>
<tr>
<td colspan="2"><a href="https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-connecting-guide">https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-connecting-guide</a></td>
</tr>
<tr>
<td colspan="2">CREATE TABLE Guide</td>
</tr>
<tr>
<td colspan="2"><a href="https://mariadb.com/docs/server/server-usage/tables/create-table">https://mariadb.com/docs/server/server-usage/tables/create-table</a></td>
</tr>
<tr>
<td colspan="2">Data Types Guide</td>
</tr>
<tr>
<td colspan="2"><a href="https://mariadb.com/docs/server/reference/data-types">https://mariadb.com/docs/server/reference/data-types</a></td>
</tr>
<tr>
<td colspan="2">String Data Types Guide</td>
</tr>
<tr>
<td colspan="2"><a href="https://mariadb.com/docs/server/reference/data-types/string-data-types">https://mariadb.com/docs/server/reference/data-types/string-data-types</a></td>
</tr>
<tr>
<td></td>
<td style="text-align: right;"></td>
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
<td colspan="3">Importing Data [MariaDB]</td>
</tr>
<tr>
<td>Importing Data</td>
<td colspan="2"><p><strong>Importing data means moving information from an external source into one or more database tables.</strong></p>
<ul>
<li><p>there is no single correct way to import data</p></li>
<li><p>the best method depends on:</p>
<ul>
<li><p>file format</p></li>
<li><p>amount of data</p></li>
<li><p>database location</p></li>
<li><p>available software</p></li>
<li><p>whether the import must be repeated</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Data Sources</td>
<td colspan="2"><p><strong>Data may come from many sources.</strong></p>
<ul>
<li><p>CSV or tab-delimited text files</p></li>
<li><p>Excel workbooks</p></li>
<li><p>SQL scripts and database backups</p></li>
<li><p>another database</p></li>
<li><p>web services and APIs</p></li>
<li><p>Python or other application code</p></li>
<li><p>manually written <span class="math inline"><em>I</em><em>N</em><em>S</em><em>E</em><em>R</em><em>T</em></span> statements</p></li>
</ul></td>
</tr>
<tr>
<td>Common Import Methods</td>
<td colspan="2"><p><strong>DBeaver Data Import.</strong></p>
<ul>
<li><p>DBeaver provides a visual import wizard for</p>
<ul>
<li><p>CSV</p></li>
<li><p>Excel</p></li>
<li><p>other supported file formats</p></li>
</ul></li>
<li><p>the wizard can be used to:</p>
<ul>
<li><p>select a source file</p></li>
<li><p>map source fields to table columns</p></li>
<li><p>configure file settings</p></li>
<li><p>review the import before loading the data</p></li>
</ul></li>
</ul>
<p><strong>DBeaver Data Import Guide:</strong></p>
<ul>
<li><p><a href="https://dbeaver.com/docs/dbeaver/Data-import/">https://dbeaver.com/docs/dbeaver/Data-import/</a></p></li>
<li><p>the guide covers:</p>
<ul>
<li><p>selecting a destination table</p></li>
<li><p>choosing the source file and format</p></li>
<li><p>configuring:</p>
<ul>
<li><p>delimiters</p></li>
<li><p>headers</p></li>
<li><p>quotes</p></li>
<li><p>encoding</p></li>
<li><p><span class="math inline"><em>N</em><em>U</em><em>L</em><em>L</em></span> values</p></li>
</ul></li>
<li><p>mapping source fields to destination columns</p></li>
<li><p>reviewing and executing the import</p></li>
</ul></li>
</ul>
<p><strong>DBeaver is often the easiest method for learning, exploring unfamiliar data, or performing a one-time import.</strong></p></td>
</tr>
<tr>
<td>MariaDB Import Tools And SQL Commands</td>
<td colspan="2"><p><strong>MariaDB provides commands and utilities for importing data directly into the database.</strong></p>
<ul>
<li><p>these methods are useful for:</p>
<ul>
<li><p>larger files</p></li>
<li><p>repeatable processes</p></li>
<li><p>automation</p></li>
<li><p>situations where a graphical interface is unavailable</p></li>
</ul></li>
</ul>
<p><strong>MariaDB Importing Data Guide:</strong></p>
<ul>
<li><p><a href="https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-importing-data-guide">https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-importing-data-guide</a></p></li>
<li><p>common methods include:</p>
<ul>
<li><p><span class="math inline"><em>L</em><em>O</em><em>A</em><em>D</em> <em>D</em><em>A</em><em>T</em><em>A</em> <em>I</em><em>N</em><em>F</em><em>I</em><em>L</em><em>E</em></span></p></li>
<li><p><span class="math inline"><em>L</em><em>O</em><em>A</em><em>D</em> <em>D</em><em>A</em><em>T</em><em>A</em> <em>L</em><em>O</em><em>C</em><em>A</em><em>L</em> <em>I</em><em>N</em><em>F</em><em>I</em><em>L</em><em>E</em></span></p></li>
<li><p>mariadb-import command-line utility</p></li>
<li><p>SQL scripts containing <span class="math inline"><em>C</em><em>R</em><em>E</em><em>A</em><em>T</em><em>E</em> <em>T</em><em>A</em><em>B</em><em>L</em><em>E</em></span> and <span class="math inline"><em>I</em><em>N</em><em>S</em><em>E</em><em>R</em><em>T</em></span> statements</p></li>
<li><p>database backup and restore tools</p></li>
<li><p>custom programs written in Python or another language</p></li>
</ul></li>
</ul>
<p><strong>Before Importing Data.</strong></p>
<ul>
<li><p>before starting an import:</p>
<ul>
<li><p>inspect both the source data and destination table</p></li>
<li><p>check:</p>
<ul>
<li><p>column names and order</p></li>
<li><p>data types</p></li>
<li><p>required and optional columns</p></li>
<li><p>primary and foreign keys</p></li>
<li><p>date and time formats</p></li>
<li><p>character encoding</p></li>
<li><p>field delimiters</p></li>
<li><p>quoted values</p></li>
<li><p>empty values and NULL values</p></li>
<li><p>duplicate records</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Import Validation</td>
<td colspan="2"><p><strong>A successful import does not always mean the data was imported correctly.</strong></p>
<ul>
<li><p>after the import, validate the results by:</p>
<ul>
<li><p>checking row counts</p></li>
<li><p>reviewing sample records</p></li>
<li><p>looking for unexpected <span class="math inline"><em>N</em><em>U</em><em>L</em><em>L</em></span> values</p></li>
<li><p>confirming that values were placed in the correct columns</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Choosing An Import Method</td>
<td colspan="2"><p><strong>Use DBeaver when you want a guided visual process or are completing a small, one-time import.</strong></p>
<ul>
<li><p>use MariaDB commands or utilities when:</p>
<ul>
<li><p>working with larger files</p></li>
<li><p>automating a repeatable process</p></li>
<li><p>learning how database imports operate outside a graphical tool</p></li>
</ul></li>
</ul>
<p><strong>Importing data involves more than loading a file.</strong></p>
<ul>
<li><p>it also requires:</p>
<ul>
<li><p>understanding the source</p></li>
<li><p>preparing the destination</p></li>
<li><p>selecting appropriate settings</p></li>
<li><p>handling errors</p></li>
<li><p>validating the final results</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="3">Creating Tables to Hold Data</td>
</tr>
<tr>
<td>Creating A Table</td>
<td colspan="2"><p><strong>Creating a table manually is useful for understanding how table definitions work before using more automated methods.</strong></p>
<ul>
<li><p><span class="math inline"><em>C</em><em>R</em><em>E</em><em>A</em><em>T</em><em>E</em> <em>T</em><em>A</em><em>B</em><em>L</em><em>E</em></span> syntax is very similar across SQL databases</p>
<ul>
<li><p>the same general structure appears in:</p>
<ul>
<li><p>PostgreSQL</p></li>
<li><p>Oracle</p></li>
<li><p>MySQL</p></li>
<li><p>other database systems</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Planning The Table</td>
<td colspan="2"><p><strong>Before creating a table, inspect the data that will be stored in it.</strong></p>
<ul>
<li><p>the table design should reflect:</p>
<ul>
<li><p>number of columns</p></li>
<li><p>type of data in each column</p></li>
<li><p>appropriate column names</p></li>
<li><p>required constraints</p></li>
<li><p>which columns make each row unique</p></li>
</ul></li>
</ul>
<p><strong>The example uses EPA vehicle data stored in a CSV file.</strong></p>
<ul>
<li><p>the file contains:</p>
<ul>
<li><p>column headers</p></li>
<li><p>comma-separated values</p></li>
<li><p>character data</p></li>
<li><p>integer data</p></li>
<li><p>floating-point numeric data</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Column Naming</td>
<td colspan="2"><p><strong>Source file column names may not always be valid or desirable database column names.</strong></p>
<ul>
<li><p>problems may include:</p>
<ul>
<li><p>white space</p></li>
<li><p>inconsistent naming conventions</p></li>
<li><p>camel case</p></li>
<li><p>names that do not follow the chosen database style</p></li>
</ul></li>
</ul>
<p><strong>Consistency is the most important naming principle.</strong></p></td>
</tr>
<tr>
<td>CREATE TABLE Structure</td>
<td colspan="2"><p><strong>A table definition begins with:</strong></p>
<p><span class="math display"><em>C</em><em>R</em><em>E</em><em>A</em><em>T</em><em>E</em> <em>T</em><em>A</em><em>B</em><em>L</em><em>E</em> <em>t</em><em>a</em><em>b</em><em>l</em><em>e</em>_<em>n</em><em>a</em><em>m</em><em>e</em> (</span></p>
<p><span class="math display">…<em>c</em><em>o</em><em>l</em><em>u</em><em>m</em><em>n</em> <em>d</em><em>e</em><em>f</em><em>i</em><em>n</em><em>i</em><em>t</em><em>i</em><em>o</em><em>n</em><em>s</em>…)</span></p>
<ul>
<li><p>the column definitions are placed inside parentheses</p></li>
</ul>
<ul>
<li><p>each column definition normally contains:</p>
<ul>
<li><p>column name</p></li>
<li><p>data type</p></li>
<li><p>optional constraints</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Character Data</td>
<td colspan="2"><p><strong>Character varying fields are useful when text values have different lengths.</strong></p>
<ul>
<li><p>example:</p></li>
</ul>
<p><span class="math display"><em>m</em><em>a</em><em>n</em><em>u</em><em>f</em><em>a</em><em>c</em><em>t</em><em>u</em><em>r</em><em>e</em><em>r</em> <em>V</em><em>A</em><em>R</em><em>C</em><em>H</em><em>A</em><em>R</em>(50) <em>N</em><em>O</em><em>T</em> <em>N</em><em>U</em><em>L</em><em>L</em></span></p>
<ul>
<li><p><span class="math inline"><em>V</em><em>A</em><em>R</em><em>C</em><em>H</em><em>A</em><em>R</em>(50) </span></p>
<ul>
<li><p>allows values up to 50 characters</p></li>
</ul></li>
<li><p><span class="math inline"><em>N</em><em>O</em><em>T</em> <em>N</em><em>U</em><em>L</em><em>L</em> </span></p>
<ul>
<li><p>means every row must contain a value for that column</p></li>
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
<th>Integer Data</th>
<th><p>Integer data is appropriate for whole-number values.</p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>model year</p></li>
<li><p>production count</p>
<ul>
<li><p>should also be an integer because fractional vehicles are not meaningful</p></li>
</ul></li>
</ul></li>
</ul>
<p>Years can also be stored as integers.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>NOT NULL</td>
<td><p><span class="math inline"><strong>N</strong><strong>O</strong><strong>T</strong> <strong>N</strong><strong>U</strong><strong>L</strong><strong>L</strong></span> <strong>prevents a column from containing a</strong> <span class="math inline"><strong>N</strong><strong>U</strong><strong>L</strong><strong>L</strong></span> <strong>value.</strong></p>
<ul>
<li><p>use <span class="math inline"><em>N</em><em>O</em><em>T</em> <em>N</em><em>U</em><em>L</em><em>L</em></span> when a value must exist for every row</p></li>
<li><p>example required fields include:</p>
<ul>
<li><p>manufacturer</p></li>
<li><p>model year</p></li>
<li><p>regulatory class</p></li>
<li><p>vehicle type</p></li>
</ul></li>
</ul>
<p><strong>Do not apply</strong> <span class="math inline"><strong>N</strong><strong>O</strong><strong>T</strong> <strong>N</strong><strong>U</strong><strong>L</strong><strong>L</strong></span> <strong>when missing values should be allowed.</strong></p></td>
</tr>
<tr>
<td>Numeric Data</td>
<td><p><strong>Numeric data is used when values contain decimal places.</strong></p>
<ul>
<li><p>the <span class="math inline"><em>N</em><em>U</em><em>M</em><em>E</em><em>R</em><em>I</em><em>C</em></span> type can define both precision and scale</p>
<ul>
<li><p>precision:</p>
<ul>
<li><p>maximum total number of digits</p></li>
</ul></li>
<li><p>scale:</p>
<ul>
<li><p>maximum number of digits after the decimal point</p></li>
</ul></li>
<li><p>Example:</p></li>
</ul></li>
</ul>
<p><span class="math display"><em>N</em><em>U</em><em>M</em><em>E</em><em>R</em><em>I</em><em>C</em>(8, 5)</span></p>
<ul>
<li><p>allows up to 8 total digits</p></li>
<li><p>allows up to 5 digits after the decimal point</p></li>
</ul>
<p><strong>Different Precision And Scale.</strong></p>
<ul>
<li><p>different numeric columns may require different precision and scale values</p></li>
<li><p>examples from the vehicle data include:</p>
<ul>
<li><p>miles per gallon</p></li>
<li><p>vehicle weight</p></li>
<li><p>horsepower</p></li>
</ul></li>
<li><p>example definitions:</p></li>
</ul>
<p><span class="math display"><em>N</em><em>U</em><em>M</em><em>E</em><em>R</em><em>I</em><em>C</em>(7, 3)</span></p>
<ul>
<li><p>maximum of 7 total digits</p></li>
<li><p>3 digits after the decimal point</p></li>
</ul>
<p><span class="math display"><em>N</em><em>U</em><em>M</em><em>E</em><em>R</em><em>I</em><em>C</em>(8, 3)</span></p>
<ul>
<li><p>maximum of 8 total digits</p></li>
<li><p>3 digits after the decimal point</p></li>
</ul>
<p><strong>Allowing</strong> <span class="math inline"><strong>N</strong><strong>U</strong><strong>L</strong><strong>L</strong></span> <strong>Values.</strong></p>
<ul>
<li><p>some numeric values may not always be available</p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>a vehicle may not yet have a calculated city miles-per-gallon value</p></li>
<li><p>leaving out <span class="math inline"><em>N</em><em>O</em><em>T</em> <em>N</em><em>U</em><em>L</em><em>L</em></span> allows the row to be stored even when that value is missing</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Separating Column Definitions</td>
<td><p><strong>Each column definition is separated by a comma.</strong></p>
<ul>
<li><p>forgetting a comma is a common source of <span class="math inline"><em>C</em><em>R</em><em>E</em><em>A</em><em>T</em><em>E</em> <em>T</em><em>A</em><em>B</em><em>L</em><em>E</em></span> syntax errors</p></li>
</ul></td>
</tr>
<tr>
<td>Primary Keys</td>
<td><p><strong>A primary key uniquely identifies each row in a table.</strong></p>
<ul>
<li><p>a primary key can be defined when the table is created</p>
<ul>
<li><p>it can also be added later</p></li>
</ul></li>
</ul>
<p><strong>The example uses a compound primary key.</strong></p>
<ul>
<li><p>a compound primary key uses more than one column to uniquely identify a row</p></li>
<li><p>the example primary key contains:</p>
<ul>
<li><p>manufacturer</p></li>
<li><p>model year</p></li>
<li><p>regulatory class</p></li>
<li><p>vehicle type</p></li>
</ul></li>
</ul>
<p><strong>Example structure:</strong></p>
<p><span class="math display"><em>P</em><em>R</em><em>I</em><em>M</em><em>A</em><em>R</em><em>Y</em> <em>K</em><em>E</em><em>Y</em> (</span></p>
<blockquote>
<p><span class="math display"><em>m</em><em>a</em><em>n</em><em>u</em><em>f</em><em>a</em><em>c</em><em>t</em><em>u</em><em>r</em><em>e</em><em>r</em>, </span></p>
</blockquote>
<p><span class="math display">                  <em>m</em><em>o</em><em>d</em><em>e</em><em>l</em><sub><em>y</em><em>e</em><em>a</em><em>r</em></sub>, </span></p>
<blockquote>
<p><span class="math display">  <em>r</em><em>e</em><em>g</em><em>u</em><em>l</em><em>a</em><em>t</em><em>o</em><em>r</em><em>y</em><sub><em>c</em><em>l</em><em>a</em><em>s</em><em>s</em></sub>, </span></p>
</blockquote>
<p><span class="math display">                        <em>v</em><em>e</em><em>h</em><em>i</em><em>c</em><em>l</em><em>e</em>_<em>t</em><em>y</em><em>p</em><em>e</em>)</span></p></td>
</tr>
<tr>
<td>Finishing The Statement</td>
<td><p><strong>The</strong> <span class="math inline"><strong>C</strong><strong>R</strong><strong>E</strong><strong>A</strong><strong>T</strong><strong>E</strong> <strong>T</strong><strong>A</strong><strong>B</strong><strong>L</strong><strong>E</strong></span> <strong>statement ends with:</strong></p>
<blockquote>
<p>)</p>
</blockquote>
<ul>
<li><p>followed by a semicolon</p></li>
</ul></td>
</tr>
<tr>
<td>Creating The Table</td>
<td><p><strong>After the statement is executed successfully, the table may not immediately appear in the database interface.</strong></p>
<ul>
<li><p>refresh the tables list to display the newly created table</p></li>
</ul></td>
</tr>
<tr>
<td>Table Naming</td>
<td><p>PostgreSQL has an important behavior involving uppercase letters in table names.</p>
<ul>
<li><p>using uppercase letters:</p>
<ul>
<li><p>can require the table name to be enclosed in double quotes in later queries</p></li>
</ul></li>
<li><p>this creates unnecessary complexity</p></li>
<li><p>recommended PostgreSQL practice:</p>
<ul>
<li><p>use lowercase table names</p></li>
<li><p>avoid uppercase characters</p></li>
<li><p>use underscores to separate words</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Data Types</td>
<td><p>Choosing the correct data type may be difficult when first creating tables.</p>
<ul>
<li><p>PostgreSQL supports many different data types</p></li>
<li><p>common types include:</p>
<ul>
<li><p><span class="math inline"><em>I</em><em>N</em><em>T</em><em>E</em><em>G</em><em>E</em><em>R</em></span></p></li>
<li><p><span class="math inline"><em>N</em><em>U</em><em>M</em><em>E</em><em>R</em><em>I</em><em>C</em></span></p></li>
<li><p><span class="math inline"><em>V</em><em>A</em><em>R</em><em>C</em><em>H</em><em>A</em><em>R</em></span></p></li>
<li><p><span class="math inline"><em>C</em><em>H</em><em>A</em><em>R</em><em>A</em><em>C</em><em>T</em><em>E</em><em>R</em></span></p></li>
</ul></li>
<li><p>PostgreSQL also supports more specialized types such as:</p>
<ul>
<li><p>JSON</p></li>
<li><p>currency-specific data types</p></li>
</ul></li>
<li><p>the PostgreSQL documentation:</p>
<ul>
<li><p>provides the complete set of supported data types.</p></li>
</ul></li>
</ul>
<p><strong>With experience, choosing appropriate data types becomes easier.</strong></p></td>
</tr>
<tr>
<td colspan="2">Importing Data into Created Tables</td>
</tr>
<tr>
<td>Before Importing Data</td>
<td><p><strong>Before importing data, inspect the source file carefully.</strong></p>
<ul>
<li><p>databases expect incoming values to match the structure and data types defined in the destination table</p>
<ul>
<li><p>unexpected values can cause an import to fail</p></li>
</ul></li>
<li><p>check the source data for:</p>
<ul>
<li><p>column names</p></li>
<li><p>column order</p></li>
<li><p>data types</p></li>
<li><p>missing values</p></li>
<li><p>unexpected text</p></li>
<li><p>date formats</p></li>
<li><p>duplicate records</p></li>
<li><p>values that do not match the destination table</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Importing With DBeaver</td>
<td><p><strong>DBeaver provides a guided interface for importing data into MariaDB tables.</strong></p>
<ul>
<li><p>the general process is:</p>
<ul>
<li><p>select the destination table</p></li>
<li><p>right-click the table</p></li>
<li><p>choose Import Data</p></li>
<li><p>select the source format</p></li>
<li><p>choose the source file</p></li>
<li><p>configure the import settings</p></li>
<li><p>map source columns to destination columns</p></li>
<li><p>review the settings</p></li>
<li><p>run the import</p></li>
</ul></li>
</ul>
<p><strong>For CSV imports, DBeaver supports settings for:</strong></p>
<ul>
<li><p>delimiters</p></li>
<li><p>headers</p></li>
<li><p>quotes</p></li>
<li><p>escape characters</p></li>
<li><p><span class="math inline"><em>N</em><em>U</em><em>L</em><em>L</em></span> values</p></li>
<li><p>encoding</p></li>
<li><p>date formats</p></li>
</ul></td>
</tr>
<tr>
<td>Selecting The Source File</td>
<td><p><strong>Choose the file containing the data to be imported.</strong></p>
<ul>
<li><p>common formats include:</p>
<ul>
<li><p>CSV</p></li>
<li><p>tab-delimited text</p></li>
<li><p>other formats supported by DBeaver</p></li>
</ul></li>
</ul>
<p><strong>The source file should be compatible with the structure of the destination table.</strong></p></td>
</tr>
<tr>
<td>Header Row</td>
<td><p><strong>A header row contains the names of the columns.</strong></p>
<ul>
<li><p>if the source file has a header:</p>
<ul>
<li><p>configure DBeaver to use the first row as column names</p></li>
</ul></li>
<li><p>if the source file does not have a header:</p>
<ul>
<li><p>configure the import so the first row is treated as data</p></li>
</ul></li>
</ul>
<p><strong>Incorrect header settings can cause a data row to be skipped or column names to be imported as data.</strong></p></td>
</tr>
<tr>
<td>Delimiter</td>
<td><p><strong>The delimiter identifies where one field ends and the next begins.</strong></p>
<ul>
<li><p>common delimiters include:</p>
<ul>
<li><p>comma</p></li>
<li><p>tab</p></li>
<li><p>pipe</p></li>
</ul></li>
<li><p>CSV files normally use a comma</p></li>
</ul>
<p><strong>The configured delimiter must match the source file.</strong></p></td>
</tr>
<tr>
<td>Quoted Values</td>
<td><p><strong>Text values may be surrounded by quotation marks.</strong></p>
<ul>
<li><p>quotes allow a value containing characters such as commas to be treated as a single field</p>
<ul>
<li><p>example:</p>
<ul>
<li><p>"Charlotte, NC"</p></li>
</ul></li>
<li><p>without quotes, the comma could incorrectly be interpreted as a field delimiter</p></li>
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
<th>Escape Character</th>
<th><p>An escape character allows special characters to appear inside a value without being interpreted as part of the file structure.</p>
<ul>
<li><p>this is useful when text contains quotation marks or other characters that would otherwise have special meaning</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>NULL Values</td>
<td><p><strong>The import process must distinguish between:</strong></p>
<ul>
<li><p><span class="math inline"><em>N</em><em>U</em><em>L</em><em>L</em></span></p></li>
<li><p>an empty string</p></li>
<li><p>a literal text value</p></li>
</ul>
<p><strong>DBeaver allows a specific value to be configured as the NULL marker and can also convert empty strings to NULL when needed.</strong></p></td>
</tr>
<tr>
<td>Column Mapping</td>
<td><p><strong>Map each source column to the appropriate MariaDB table column.</strong></p>
<ul>
<li><p>check that:</p>
<ul>
<li><p>column names correspond correctly</p></li>
<li><p>column order is correct</p></li>
<li><p>source values are compatible with destination data types</p></li>
<li><p>required destination columns receive values</p></li>
</ul></li>
</ul>
<p><strong>A successful mapping does not guarantee that every value is valid.</strong></p>
<ul>
<li><p>the actual data must still conform to the table definition</p></li>
</ul></td>
</tr>
<tr>
<td>Import Failure</td>
<td><p><strong>An import may fail when a source value cannot be converted to the destination column's data type.</strong></p>
<ul>
<li><p>for example:</p>
<ul>
<li><p><span class="math inline"><em>m</em><em>o</em><em>d</em><em>e</em><em>l</em>_<em>y</em><em>e</em><em>a</em><em>r</em> </span></p></li>
<li><p>is defined as <span class="math inline"><em>I</em><em>N</em><em>T</em><em>E</em><em>G</em><em>E</em><em>R</em></span></p></li>
</ul></li>
<li><p>but the source contains:</p>
<ul>
<li><p><span class="math inline"><em>p</em><em>r</em><em>e</em><em>l</em><em>i</em><em>m</em> 2022</span></p></li>
</ul></li>
</ul>
<p><strong>MariaDB cannot store the entire string</strong> <span class="math inline"><strong>p</strong><strong>r</strong><strong>e</strong><strong>l</strong><strong>i</strong><strong>m</strong> <strong>2022</strong></span> <strong>as an integer.</strong></p>
<ul>
<li><p>the source data or table design must therefore be corrected before the import can succeed</p></li>
</ul></td>
</tr>
<tr>
<td>Investigating The Error</td>
<td><p><strong>When an import fails, identify:</strong></p>
<ul>
<li><p>which column caused the error</p></li>
<li><p>which value caused the error</p></li>
<li><p>what data type the destination column expects</p></li>
<li><p>whether the source contains a recurring pattern</p></li>
</ul>
<p><strong>In the EPA vehicle example, the source contains preliminary 2022 values.</strong></p>
<ul>
<li><p>the text prelim communicates useful information</p></li>
<li><p>simply deleting it would make the value compatible with INTEGER but would also discard information</p></li>
</ul></td>
</tr>
<tr>
<td>Preserving Information During Cleaning</td>
<td><p><strong>Instead of deleting meaningful information, separate it into another field.</strong></p>
<ul>
<li><p>the original value:</p>
<ul>
<li><p><span class="math inline"><em>p</em><em>r</em><em>e</em><em>l</em><em>i</em><em>m</em> 2022</span></p></li>
</ul></li>
<li><p>can be represented as:</p>
<ul>
<li><p><span class="math inline"><em>m</em><em>o</em><em>d</em><em>e</em><em>l</em>_<em>y</em><em>e</em><em>a</em><em>r</em> = 2022</span></p></li>
<li><p><span class="math inline"><em>p</em><em>r</em><em>e</em><em>l</em><em>i</em><em>m</em> = <em>y</em></span></p></li>
</ul></li>
</ul>
<p><strong>This preserves the preliminary status while keeping</strong> <span class="math inline"><strong>m</strong><strong>o</strong><strong>d</strong><strong>e</strong><strong>l</strong><strong>_</strong><strong>y</strong><strong>e</strong><strong>a</strong><strong>r</strong></span> <strong>compatible with an integer data type.</strong></p></td>
</tr>
<tr>
<td>Adding A Preliminary Column</td>
<td><p><strong>Add a new column to the MariaDB table before importing the cleaned file.</strong></p>
<ul>
<li><p>Example:</p></li>
</ul>
<p><span class="math display"><em>A</em><em>L</em><em>T</em><em>E</em><em>R</em> <em>T</em><em>A</em><em>B</em><em>L</em><em>E</em> <em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em></span></p>
<p><span class="math display"><em>A</em><em>D</em><em>D</em> <em>C</em><em>O</em><em>L</em><em>U</em><em>M</em><em>N</em> <em>p</em><em>r</em><em>e</em><em>l</em><em>i</em><em>m</em> <em>C</em><em>H</em><em>A</em><em>R</em>(1);</span></p>
<p><strong>MariaDB supports adding columns to an existing table with ALTER TABLE and ADD COLUMN.</strong></p>
<ul>
<li><p>the field only needs to store:</p></li>
</ul>
<blockquote>
<p><span class="math inline"><em>y</em></span> or <span class="math inline"><em>n</em></span></p>
</blockquote>
<ul>
<li><p>so <span class="math inline"><em>C</em><em>H</em><em>A</em><em>R</em>(1)</span> is sufficient</p></li>
</ul></td>
</tr>
<tr>
<td>Cleaning The Source Data</td>
<td><p><strong>Create a prelim field in the source file.</strong></p>
<ul>
<li><p>for each row:</p>
<ul>
<li><p>set prelim to <span class="math inline"><em>y</em></span> when the model year is preliminary</p></li>
<li><p>set prelim to <span class="math inline"><em>n</em></span> otherwise</p></li>
<li><p>then replace:</p>
<ul>
<li><p><span class="math inline"><em>p</em><em>r</em><em>e</em><em>l</em><em>i</em><em>m</em> 2022</span></p></li>
</ul></li>
<li><p>with:</p>
<ul>
<li><p><span class="math inline">2022</span></p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>The resulting data keeps both pieces of information in fields with appropriate data types.</strong></p></td>
</tr>
<tr>
<td>Saving The Cleaned Data</td>
<td><p><strong>Save the cleaned dataset as a new file.</strong></p>
<ul>
<li><p>this preserves the original source data</p></li>
<li><p>the cleaned file can then be used for the database import</p></li>
</ul></td>
</tr>
<tr>
<td>Retrying The DBeaver Import</td>
<td><p><strong>Run the import again using the cleaned source file.</strong></p>
<ul>
<li><p>check the column mapping</p>
<ul>
<li><p>the file now contains the additional prelim column</p></li>
</ul></li>
<li><p>map:</p>
<ul>
<li><p><span class="math inline"><em>m</em><em>o</em><em>d</em><em>e</em><em>l</em>_<em>y</em><em>e</em><em>a</em><em>r</em></span> to <span class="math inline"><em>m</em><em>o</em><em>d</em><em>e</em><em>l</em>_<em>y</em><em>e</em><em>a</em><em>r</em></span></p></li>
<li><p><span class="math inline"><em>p</em><em>r</em><em>e</em><em>l</em><em>i</em><em>m</em></span> to <span class="math inline"><em>p</em><em>r</em><em>e</em><em>l</em><em>i</em><em>m</em></span></p></li>
</ul></li>
<li><p>then review the remaining mappings and execute the import</p></li>
</ul></td>
</tr>
<tr>
<td>Validating The Import</td>
<td><p><strong>A completed import should always be validated.</strong></p>
<ul>
<li><p>example:</p>
<ul>
<li><p><span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em> *</span></p></li>
<li><p><span class="math inline"><em>F</em><em>R</em><em>O</em><em>M</em> <em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em>;</span></p></li>
</ul></li>
<li><p>check that:</p>
<ul>
<li><p>rows were imported</p></li>
<li><p><span class="math inline"><em>m</em><em>o</em><em>d</em><em>e</em><em>l</em>_<em>y</em><em>e</em><em>a</em><em>r</em></span> contains valid integer values</p></li>
<li><p>prelim contains the expected <span class="math inline"><em>y</em></span> or <span class="math inline"><em>n</em></span> values</p></li>
<li><p>columns contain the correct source data</p></li>
<li><p>unexpected <span class="math inline"><em>N</em><em>U</em><em>L</em><em>L</em></span> values were not introduced</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Checking Row Counts</td>
<td><p><strong>Compare the number of imported rows with the expected number of source records.</strong></p>
<ul>
<li><p>example:</p>
<ul>
<li><p><span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em> <em>C</em><em>O</em><em>U</em><em>N</em><em>T</em>(*)</span></p></li>
<li><p><span class="math inline"><em>F</em><em>R</em><em>O</em><em>M</em> <em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em>;</span></p></li>
</ul></li>
<li><p>a matching row count is useful evidence that the import completed correctly</p></li>
<li><p>it does not by itself prove that every value was imported correctly</p></li>
</ul></td>
</tr>
<tr>
<td>Importing With MariaDB SQL</td>
<td><p><strong>MariaDB also provides</strong> <span class="math inline"><strong>L</strong><strong>O</strong><strong>A</strong><strong>D</strong> <strong>D</strong><strong>A</strong><strong>T</strong><strong>A</strong> <strong>I</strong><strong>N</strong><strong>F</strong><strong>I</strong><strong>L</strong><strong>E</strong></span> <strong>for importing data directly from text files.</strong></p>
<ul>
<li><p>this is useful when:</p>
<ul>
<li><p>working with larger files</p></li>
<li><p>creating repeatable import processes</p></li>
<li><p>automating data loading</p></li>
<li><p>working without a graphical interface</p></li>
</ul></li>
</ul>
<p><strong>MariaDB documents</strong> <span class="math inline"><strong>L</strong><strong>O</strong><strong>A</strong><strong>D</strong> <strong>D</strong><strong>A</strong><strong>T</strong><strong>A</strong> <strong>I</strong><strong>N</strong><strong>F</strong><strong>I</strong><strong>L</strong><strong>E</strong></span> <strong>as its high-speed SQL mechanism for loading rows from text files into a table.</strong></p>
<ul>
<li><p>Basic <span class="math inline"><em>L</em><em>O</em><em>A</em><em>D</em> <em>D</em><em>A</em><em>T</em><em>A</em> <em>I</em><em>N</em><em>F</em><em>I</em><em>L</em><em>E</em></span></p></li>
<li><p>A basic import has the form:</p>
<ul>
<li><p><span class="math inline"><em>L</em><em>O</em><em>A</em><em>D</em> <em>D</em><em>A</em><em>T</em><em>A</em> <em>I</em><em>N</em><em>F</em><em>I</em><em>L</em><em>E</em> ′/<em>p</em><em>a</em><em>t</em><em>h</em>/<em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em>.<em>c</em><em>s</em><em>v</em>′</span></p></li>
<li><p><span class="math inline"><em>I</em><em>N</em><em>T</em><em>O</em> <em>T</em><em>A</em><em>B</em><em>L</em><em>E</em> <em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em>;</span></p></li>
</ul></li>
</ul>
<p><strong>The file must be accessible in the environment expected by the MariaDB server.</strong></p>
<ul>
<li><p><span class="math inline"><em>L</em><em>O</em><em>A</em><em>D</em> <em>D</em><em>A</em><em>T</em><em>A</em> <em>L</em><em>O</em><em>C</em><em>A</em><em>L</em> <em>I</em><em>N</em><em>F</em><em>I</em><em>L</em><em>E</em></span></p>
<ul>
<li><p>reads the file from the client side rather than requiring the MariaDB server to access the file directly</p></li>
<li><p>example:</p>
<ul>
<li><p><span class="math inline"><em>L</em><em>O</em><em>A</em><em>D</em> <em>D</em><em>A</em><em>T</em><em>A</em> <em>L</em><em>O</em><em>C</em><em>A</em><em>L</em> <em>I</em><em>N</em><em>F</em><em>I</em><em>L</em><em>E</em> ′/<em>p</em><em>a</em><em>t</em><em>h</em>/<em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em>.<em>c</em><em>s</em><em>v</em>′</span></p></li>
<li><p><span class="math inline"><em>I</em><em>N</em><em>T</em><em>O</em> <em>T</em><em>A</em><em>B</em><em>L</em><em>E</em> <em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em>;</span></p></li>
</ul></li>
</ul></li>
<li><p>whether <span class="math inline"><em>L</em><em>O</em><em>C</em><em>A</em><em>L</em></span> imports are available depends on the MariaDB and client configuration</p></li>
</ul></td>
</tr>
<tr>
<td>Importing A CSV File With SQL</td>
<td><p><strong>A CSV import can define the delimiter, quote character, and header behavior.</strong></p>
<ul>
<li><p>Example:</p>
<ul>
<li><p><span class="math inline"><em>L</em><em>O</em><em>A</em><em>D</em> <em>D</em><em>A</em><em>T</em><em>A</em> <em>L</em><em>O</em><em>C</em><em>A</em><em>L</em> <em>I</em><em>N</em><em>F</em><em>I</em><em>L</em><em>E</em> ′/<em>p</em><em>a</em><em>t</em><em>h</em>/<em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em>.<em>c</em><em>s</em><em>v</em>′</span></p></li>
<li><p><span class="math inline"><em>I</em><em>N</em><em>T</em><em>O</em> <em>T</em><em>A</em><em>B</em><em>L</em><em>E</em> <em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em></span></p></li>
<li><p><span class="math inline"><em>F</em><em>I</em><em>E</em><em>L</em><em>D</em><em>S</em> <em>T</em><em>E</em><em>R</em><em>M</em><em>I</em><em>N</em><em>A</em><em>T</em><em>E</em><em>D</em> <em>B</em><em>Y</em> ′, ′</span></p></li>
<li><p><span class="math inline">$ENCLOSED\ BY\ '"'$</span></p></li>
<li><p><span class="math inline"><em>L</em><em>I</em><em>N</em><em>E</em><em>S</em> <em>T</em><em>E</em><em>R</em><em>M</em><em>I</em><em>N</em><em>A</em><em>T</em><em>E</em><em>D</em> <em>B</em><em>Y</em> ′ ∖ <em>n</em>′</span></p></li>
<li><p><span class="math inline"><em>I</em><em>G</em><em>N</em><em>O</em><em>R</em><em>E</em> 1 <em>L</em><em>I</em><em>N</em><em>E</em><em>S</em>;</span></p></li>
</ul></li>
<li><p><span class="math inline"><em>F</em><em>I</em><em>E</em><em>L</em><em>D</em><em>S</em> <em>T</em><em>E</em><em>R</em><em>M</em><em>I</em><em>N</em><em>A</em><em>T</em><em>E</em><em>D</em> <em>B</em><em>Y</em> </span></p>
<ul>
<li><p>identifies the column delimiter</p></li>
</ul></li>
<li><p><span class="math inline"><em>E</em><em>N</em><em>C</em><em>L</em><em>O</em><em>S</em><em>E</em><em>D</em> <em>B</em><em>Y</em> </span></p>
<ul>
<li><p>identifies the character surrounding quoted values</p></li>
</ul></li>
<li><p><span class="math inline"><em>L</em><em>I</em><em>N</em><em>E</em><em>S</em> <em>T</em><em>E</em><em>R</em><em>M</em><em>I</em><em>N</em><em>A</em><em>T</em><em>E</em><em>D</em> <em>B</em><em>Y</em> </span></p>
<ul>
<li><p>identifies how records are separated</p></li>
</ul></li>
<li><p><span class="math inline"><em>I</em><em>G</em><em>N</em><em>O</em><em>R</em><em>E</em> 1 <em>L</em><em>I</em><em>N</em><em>E</em><em>S</em> </span></p>
<ul>
<li><p>skips the header row</p></li>
</ul></li>
</ul>
<p><strong>MariaDB</strong> <span class="math inline"><strong>L</strong><strong>O</strong><strong>A</strong><strong>D</strong> <strong>D</strong><strong>A</strong><strong>T</strong><strong>A</strong></span> <strong>supports control over field formatting, line formatting, and column mapping during bulk imports.</strong></p></td>
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
<th>Choosing An Import Method</th>
<th><p>Use DBeaver when you want:</p>
<ul>
<li><p>a guided visual process</p></li>
<li><p>interactive column mapping</p></li>
<li><p>easy inspection of import settings</p></li>
<li><p>a small or one-time import</p></li>
</ul>
<p>use <span class="math inline"><strong>L</strong><strong>O</strong><strong>A</strong><strong>D</strong> <strong>D</strong><strong>A</strong><strong>T</strong><strong>A</strong> <strong>I</strong><strong>N</strong><strong>F</strong><strong>I</strong><strong>L</strong><strong>E</strong></span> or <span class="math inline"><strong>L</strong><strong>O</strong><strong>A</strong><strong>D</strong> <strong>D</strong><strong>A</strong><strong>T</strong><strong>A</strong> <strong>L</strong><strong>O</strong><strong>C</strong><strong>A</strong><strong>L</strong> <strong>I</strong><strong>N</strong><strong>F</strong><strong>I</strong><strong>L</strong><strong>E</strong></span> when you want:</p>
<ul>
<li><p>repeatable SQL</p></li>
<li><p>automation</p></li>
<li><p>larger bulk imports</p></li>
<li><p>a process that does not depend on a graphical interface</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Key Import Principle</td>
<td><p><strong>Importing data is not simply moving a file into a database.</strong></p>
<ul>
<li><p>it requires:</p>
<ul>
<li><p>inspecting the source</p></li>
<li><p>understanding the destination schema</p></li>
<li><p>matching data types</p></li>
<li><p>preserving meaningful information during cleaning</p></li>
<li><p>mapping fields correctly</p></li>
<li><p>handling import errors</p></li>
<li><p>validating the final result</p></li>
</ul></li>
</ul>
<p><strong>A failed import often identifies a mismatch between the structure of the source data and the structure expected by the database.</strong></p></td>
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
<th colspan="2">Testing That Data Are Correctly Loaded</th>
</tr>
</thead>
<tbody>
<tr>
<td>Why Validate Imported Data</td>
<td><p><strong>A successful import does not guarantee that the data was loaded correctly.</strong></p>
<ul>
<li><p>a process:</p>
<ul>
<li><p>can complete without errors</p></li>
<li><p>while still producing unexpected results</p></li>
</ul></li>
<li><p>never assume that an import worked simply because MariaDB or DBeaver reported success</p></li>
</ul></td>
</tr>
<tr>
<td>Check The Expected Row Count</td>
<td><p><strong>The first validation step is to determine how many rows should exist in the destination table.</strong></p>
<ul>
<li><p>the EPA source file contains <span class="math inline">5, 281</span> total rows</p>
<ul>
<li><p>one row is the header</p></li>
<li><p>the expected number of data rows is therefore:</p>
<ul>
<li><p><span class="math inline">5, 280</span></p></li>
</ul></li>
</ul></li>
</ul>
<p><strong>Count Rows In MariaDB.</strong></p>
<ul>
<li><p>Use COUNT(*) to determine how many rows were imported</p>
<ul>
<li><p><span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em> <em>C</em><em>O</em><em>U</em><em>N</em><em>T</em>(*)</span></p></li>
<li><p><span class="math inline"><em>F</em><em>R</em><em>O</em><em>M</em> <em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em>;</span></p></li>
<li><p>expected result:</p>
<ul>
<li><p><span class="math inline">5, 280</span></p></li>
</ul></li>
</ul></li>
<li><p>matching the expected row count:</p>
<ul>
<li><p>confirms that the expected number of records was loaded</p></li>
<li><p>it does not prove that every value was loaded correctly</p></li>
</ul></li>
</ul>
<p><strong>DBeaver Row Count.</strong></p>
<ul>
<li><p>DBeaver also displays the number of rows returned by a query</p></li>
<li><p>running:</p>
<ul>
<li><p><span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em> *</span></p></li>
<li><p><span class="math inline"><em>F</em><em>R</em><em>O</em><em>M</em> <em>e</em><em>p</em><em>a</em>_<em>c</em><em>a</em><em>r</em><em>s</em>;</span></p></li>
<li><p>can provide a quick visual confirmation of the number of retrieved rows</p></li>
<li><p>COUNT(*) is still preferable when the row count itself is the validation target</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Visually Inspect The Imported Data</td>
<td><p><strong>Visual inspection is an important part of quality assurance.</strong></p>
<ul>
<li><p>review sample rows and examine each column for values that appear inconsistent with the intended data type</p>
<ul>
<li><p>look for problems such as:</p>
<ul>
<li><p>decimal values being truncated</p></li>
<li><p>unexpected <span class="math inline"><em>N</em><em>U</em><em>L</em><em>L</em></span> values</p></li>
<li><p>text stored in the wrong column</p></li>
<li><p>incorrectly parsed dates</p></li>
<li><p>values shifted between columns</p></li>
<li><p>unexpected categories</p></li>
<li><p>missing records</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Check Numeric Precision</td>
<td><p>Numeric columns should retain the precision expected from the source data.</p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>a value containing decimal places:</p>
<ul>
<li><p>should not lose those decimal places because the destination column was accidentally defined as <span class="math inline"><em>I</em><em>N</em><em>T</em><em>E</em><em>G</em><em>E</em><em>R</em></span></p></li>
</ul></li>
<li><p>compare representative source values with their imported MariaDB values</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Compare Source And Destination Queries</td>
<td><p><strong>When transferring data from one database to another, run equivalent queries against both databases.</strong></p>
<ul>
<li><p>compare the results</p>
<ul>
<li><p>useful comparisons include:</p>
<ul>
<li><p>row counts</p></li>
<li><p>minimum and maximum values</p></li>
<li><p>category counts</p></li>
<li><p>aggregates</p></li>
<li><p>specific record lookups</p></li>
</ul></li>
<li><p>different results may indicate that the data was:</p>
<ul>
<li><p>transformed</p></li>
<li><p>omitted</p></li>
<li><p>duplicated</p></li>
<li><p>incorrectly loaded</p></li>
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
<th>Referential Integrity</th>
<th><p>Referential integrity describes whether relationships between tables remain valid.</p>
<ul>
<li><p>if one table references a record in another table:</p>
<ul>
<li><p>the referenced record should exist when the database design requires it</p></li>
<li><p>for example:</p>
<ul>
<li><p><span class="math inline"><em>C</em><em>O</em><em>N</em><em>D</em><em>I</em><em>T</em><em>I</em><em>O</em><em>N</em>_<em>O</em><em>C</em><em>C</em><em>U</em><em>R</em><em>R</em><em>E</em><em>N</em><em>C</em><em>E</em></span>:</p>
<ul>
<li><p>references <span class="math inline"><em>P</em><em>E</em><em>R</em><em>S</em><em>O</em><em>N</em></span> through <span class="math inline"><em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em>_<em>i</em><em>d</em></span></p></li>
</ul></li>
</ul></li>
<li><p>a diagnosis should correspond to an existing patient</p></li>
<li><p>a patient does not necessarily need to have a diagnosis</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Checking For Diagnoses Without Patients</td>
<td><p><strong>A LEFT JOIN can be used to identify condition records that do not have a matching patient.</strong></p>
<ul>
<li><p><span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em> <em>C</em><em>O</em><em>U</em><em>N</em><em>T</em>(*)</span></p></li>
<li><p><span class="math inline"><em>F</em><em>R</em><em>O</em><em>M</em> <em>c</em><em>o</em><em>n</em><em>d</em><em>i</em><em>t</em><em>i</em><em>o</em><em>n</em>_<em>o</em><em>c</em><em>c</em><em>u</em><em>r</em><em>r</em><em>e</em><em>n</em><em>c</em><em>e</em> <em>c</em></span></p></li>
<li><p><span class="math inline"><em>L</em><em>E</em><em>F</em><em>T</em> <em>J</em><em>O</em><em>I</em><em>N</em> <em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em> <em>p</em></span></p></li>
<li><p><span class="math inline"><em>O</em><em>N</em> <em>c</em>.<em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em>_<em>i</em><em>d</em> = <em>p</em>.<em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em>_<em>i</em><em>d</em></span></p></li>
<li><p><span class="math inline"><em>W</em><em>H</em><em>E</em><em>R</em><em>E</em> <em>p</em>.<em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em>_<em>i</em><em>d</em> <em>I</em><em>S</em> <em>N</em><em>U</em><em>L</em><em>L</em>;</span></p>
<ul>
<li><p>expected result:</p>
<ul>
<li><p>0</p></li>
</ul></li>
<li><p>a result of zero:</p>
<ul>
<li><p>means that every <span class="math inline"><em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em>_<em>i</em><em>d</em></span> in <span class="math inline"><em>C</em><em>O</em><em>N</em><em>D</em><em>I</em><em>T</em><em>I</em><em>O</em><em>N</em>_<em>O</em><em>C</em><em>C</em><em>U</em><em>R</em><em>R</em><em>E</em><em>N</em><em>C</em><em>E</em></span> also exists in <span class="math inline"><em>P</em><em>E</em><em>R</em><em>S</em><em>O</em><em>N</em></span></p></li>
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
<th>Why Use A LEFT JOIN</th>
<th><p>The goal is to preserve every row from CONDITION_OCCURRENCE.</p>
<ul>
<li><p>the <span class="math inline"><em>L</em><em>E</em><em>F</em><em>T</em> <em>J</em><em>O</em><em>I</em><em>N</em></span>:</p>
<ul>
<li><p>keeps all condition records even when there is no matching <span class="math inline"><em>P</em><em>E</em><em>R</em><em>S</em><em>O</em><em>N</em></span> record</p></li>
</ul></li>
<li><p><span class="math inline"><em>W</em><em>H</em><em>E</em><em>R</em><em>E</em> <em>p</em>.<em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em>_<em>i</em><em>d</em> <em>I</em><em>S</em> <em>N</em><em>U</em><em>L</em><em>L</em>:</span></p>
<ul>
<li><p>isolates the unmatched records</p></li>
</ul></li>
</ul>
<p>This is equivalent to the PostgreSQL example that used a RIGHT JOIN with the table order reversed.</p>
<ul>
<li><p>using <span class="math inline"><em>L</em><em>E</em><em>F</em><em>T</em> <em>J</em><em>O</em><em>I</em><em>N</em></span> often makes the validation logic easier to read</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Checking The Opposite Relationship</td>
<td><p><strong>The relationship can also be checked in the opposite direction.</strong></p>
<ul>
<li><p><span class="math inline"><em>S</em><em>E</em><em>L</em><em>E</em><em>C</em><em>T</em> <em>C</em><em>O</em><em>U</em><em>N</em><em>T</em>(*)</span></p></li>
<li><p><span class="math inline"><em>F</em><em>R</em><em>O</em><em>M</em> <em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em> <em>p</em></span></p></li>
<li><p><span class="math inline"><em>L</em><em>E</em><em>F</em><em>T</em> <em>J</em><em>O</em><em>I</em><em>N</em> <em>c</em><em>o</em><em>n</em><em>d</em><em>i</em><em>t</em><em>i</em><em>o</em><em>n</em>_<em>o</em><em>c</em><em>c</em><em>u</em><em>r</em><em>r</em><em>e</em><em>n</em><em>c</em><em>e</em> <em>c</em></span></p></li>
<li><p><span class="math inline"><em>O</em><em>N</em> <em>p</em>.<em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em>_<em>i</em><em>d</em> = <em>c</em>.<em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em>_<em>i</em><em>d</em></span></p></li>
<li><p><span class="math inline"><em>W</em><em>H</em><em>E</em><em>R</em><em>E</em> <em>c</em>.<em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em>_<em>i</em><em>d</em> <em>I</em><em>S</em> <em>N</em><em>U</em><em>L</em><em>L</em>;</span></p>
<ul>
<li><p>this identifies:</p>
<ul>
<li><p>patients who do not have a matching diagnosis</p></li>
<li><p>in this example, that is acceptable.</p></li>
</ul></li>
<li><p>patients may exist without any diagnosis records</p></li>
<li><p>whether unmatched records are acceptable depends on the business rules for the database</p></li>
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
<th>Business Rules</th>
<th><p>Daabase validation should also reflect the rules of the specific dataset.</p>
<ul>
<li><p>technical integrity alone does not guarantee that the data makes sense</p></li>
<li><p>examples of healthcare business-rule checks include:</p>
<ul>
<li><p>patient counts should not unexpectedly decrease</p></li>
<li><p>patient ages should remain within plausible ranges</p></li>
<li><p>expected demographic categories should not suddenly disappear</p></li>
<li><p>record counts should remain within reasonable ranges</p></li>
<li><p>required relationships should remain valid</p></li>
</ul></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr>
<td>Descriptive Validation</td>
<td><p><strong>Simple descriptive queries can reveal errors that row counts do not detect.</strong></p>
<ul>
<li><p>use frequency distributions to examine whether categorical data contains the expected mix of values</p>
<ul>
<li><p>examples include:</p>
<ul>
<li><p>race</p></li>
<li><p>ethnicity</p></li>
<li><p>sex</p></li>
<li><p>visit type</p></li>
<li><p>diagnosis category</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Why Use A LEFT JOIN</td>
<td><p><strong>A LEFT JOIN preserves all records from PERSON.</strong></p>
<ul>
<li><p>if a <span class="math inline"><em>r</em><em>a</em><em>c</em><em>e</em>_<em>c</em><em>o</em><em>n</em><em>c</em><em>e</em><em>p</em><em>t</em>_<em>i</em><em>d</em></span> does not have a corresponding record in CONCEPT, the patient still appears in the result</p>
<ul>
<li><p>the concept name will appear as <span class="math inline"><em>N</em><em>U</em><em>L</em><em>L</em></span></p></li>
<li><p>this makes broken or missing concept mappings easier to detect</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>NULL Values</td>
<td><p><strong>A</strong> <span class="math inline"><strong>N</strong><strong>U</strong><strong>L</strong><strong>L</strong></span> <strong>category is not automatically an error.</strong></p>
<ul>
<li><p>whether <span class="math inline"><em>N</em><em>U</em><em>L</em><em>L</em></span> values are acceptable depends on the business rules and meaning of the data</p>
<ul>
<li><p>for example:</p>
<ul>
<li><p>missing race data may be acceptable in a particular dataset</p></li>
<li><p>a sudden increase in missing values may still indicate a data-loading problem</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td>Validation Is More Than Error Checking</td>
<td><p><strong>Data validation should combine several types of checks.</strong></p>
<ul>
<li><p>row-count validation</p></li>
<li><p>visual inspection</p></li>
<li><p>data-type validation</p></li>
<li><p>referential-integrity checks</p></li>
<li><p>business-rule checks</p></li>
<li><p>descriptive queries</p></li>
<li><p>source-to-destination comparisons</p></li>
</ul>
<p><strong>Key Validation Principle.</strong></p>
<ul>
<li><p>never assume that imported data is correct because the import completed successfully</p></li>
<li><p>validation should confirm both structural correctness and logical correctness</p>
<ul>
<li><p>check that:</p>
<ul>
<li><p>the expected number of rows exists</p></li>
<li><p>values appear in the correct columns</p></li>
<li><p>data types preserved the intended values</p></li>
<li><p>table relationships remain valid</p></li>
<li><p>expected categories are present</p></li>
<li><p>business rules are satisfied</p></li>
<li><p>query results are consistent with the source data</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>
