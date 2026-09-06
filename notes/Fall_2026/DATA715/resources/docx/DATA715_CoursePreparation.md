> Markdown version for convenient browsing. Original files:
> - PDF: [DATA715_CoursePreparation.pdf](../DATA715_CoursePreparation.pdf)
> - DOCX: [DATA715_CoursePreparation.docx](DATA715_CoursePreparation.docx)

---

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 4%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Course Preparation</th>
<th></th>
<th style="text-align: right;"></th>
<th style="text-align: right;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Requirements</td>
<td colspan="2" style="text-align: right;"><em>13 Aug 2026</em></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>DBeaver</p></li>
<li><p>Java 21 or higher</p></li>
<li><p>OpenJDK 23.0</p>
<ol type="1">
<li><p><a href="https://dbeaver.io/download/">https://dbeaver.io/download/</a></p></li>
</ol></li>
<li><p>Campus VPN: Cisco Secure Client</p>
<ol type="1">
<li><p><a href="https://tdx.unc.edu/TDClient/33/Portal/KB/ArticleDet?ID=30">https://tdx.unc.edu/TDClient/33/Portal/KB/ArticleDet?ID=30</a></p></li>
<li><p>You need VPN to access</p>
<ol type="i">
<li><p>GitLab Services</p></li>
<li><p>F5 Load Balancer</p></li>
<li><p>Grouper</p></li>
</ol></li>
</ol></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Connect to a new MySQL Database</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><p><img src="generated_media\DATA715_CoursePreparation\media\image1.png" style="width:0.28125in;height:0.26067in" />You must be connected to the Campus VPN, or on EDUROAM to connect</p>
<ul>
<li><p>Click the icon to create a new connection OR</p></li>
<li><p>From the Menu click Database &gt; New Database Connection OR</p></li>
<li><p>Ctrl + Shift + N (Cmd + Shift + N on Mac)</p></li>
<li><p>Choose MySQL from the database driver list</p></li>
<li><p>Settings:</p>
<ol type="1">
<li><p>Server Host: db2.ils.unc.edu</p></li>
<li><p>Port: 3306</p></li>
<li><p>Database: db2_onyen (example db1_aml14)</p></li>
<li><p>Username: db2_onyen (example db1_aml14)</p></li>
<li><p>Password: Emailed to each student (be sure not to copy trailing spaces)</p></li>
<li><p>Click: ‘Save password’ &gt; ‘Test Connection’ &gt; ‘OK’ &gt; ‘Finish’</p></li>
</ol></li>
</ul></td>
</tr>
<tr>
<td>Screenshots</td>
<td colspan="4" style="text-align: center;"><p><img src="generated_media\DATA715_CoursePreparation\media\image2.png" style="width:4.89236in;height:4.91736in" /></p>
<p><img src="generated_media\DATA715_CoursePreparation\media\image3.png" style="width:3.41736in;height:3.47153in" /></p>
<p>be sure to enable public key retrieval</p>
<p><img src="generated_media\DATA715_CoursePreparation\media\image4.png" style="width:4.69167in;height:2.35417in" /></p></td>
</tr>
<tr>
<td colspan="4">Getting Connected: Connect to Sakila.db</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>Downloads</p>
<ul>
<li><p>saklia.db</p>
<ul>
<li><p><a href="https://www.timestored.com/data/sample/sakila.db">https://www.timestored.com/data/sample/sakila.db</a></p></li>
</ul></li>
<li><p>duckdb-demo.duckdb</p>
<ul>
<li><p><a href="https://www.timestored.com/sqlnotebook/files/duckdb-demo.duckdb">https://www.timestored.com/sqlnotebook/files/duckdb-demo.duckdb</a></p></li>
</ul></li>
<li><p>Open DBeaver</p></li>
<li><p>Create a New Database Connection</p>
<ul>
<li><p>Choose SQLite</p></li>
</ul></li>
<li><p>Connect by: Host</p></li>
<li><p>Path: Location of downloaded sakila.db e.g. C:\Downloads\sakila.db</p></li>
<li><p>Click: ‘Test Connection’ &gt; ‘OK’ &gt; ‘Finish’</p></li>
<li><p>View Database Connection in the navigation pane</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="4">Write Your First SQL Query in DBeaver</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="5"><ul>
<li><p>Open a New SQL Editor Tab</p></li>
<li><p>You have several ways to open a new SQL editor tab in DBeaver:</p>
<ul>
<li><p>Click the SQL Editor icon in the main toolbar</p></li>
<li><p>go to SQL Editor &gt; New SQL Script</p></li>
<li><p>press F3</p></li>
</ul></li>
<li><p>Type: SELECT * FROM actor;</p></li>
<li><p>Execute the Query</p>
<ul>
<li><p>Click the Execute SQL Statement button (▶️) in the toolbar</p></li>
<li><p>Or go to SQL Editor &gt; Execute SQL Statement</p></li>
<li><p>Or go to SQL Editor &gt; Execute SQL Statement</p></li>
</ul></li>
<li><p>View your results</p>
<ul>
<li><p>If your query runs successfully and you see a results grid showing data from the actor table, congratulations! You're all set and ready for Introduction to Databases section of the course..</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td colspan="5"></td>
</tr>
</tbody>
</table>
