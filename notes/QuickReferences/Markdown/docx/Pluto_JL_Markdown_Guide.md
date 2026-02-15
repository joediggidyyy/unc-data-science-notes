---
generated_at_utc: 2026-02-15T09:37:49+00:00
generated_from: notes/QuickReferences/Markdown/docx/Pluto_JL_Markdown_Guide.docx
generator: tools/convert_assets_to_markdown.py
engine: pandoc
---
> Markdown version for convenient browsing. Original files:
> - PDF: [Pluto_JL_Markdown_Guide.pdf](../Pluto_JL_Markdown_Guide.pdf)
> - DOCX: [Pluto_JL_Markdown_Guide.docx](Pluto_JL_Markdown_Guide.docx)

---

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 33%" />
<col style="width: 0%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: left;"><strong>Markdown Formatting</strong></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: left;"><p><strong>This guide documents Markdown features that render correctly in Pluto.jl using md""" ... """ blocks. All examples are Markdown-native and safe for assignments and assessments`</strong></p>
<p><strong>***Use triple-quoted strings for all multi-line markdown in Pluto</strong></p></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;"><strong>1. Basic Text Formatting</strong></td>
<td colspan="3" style="text-align: center;"><p><strong>headings</strong></p>
<ul>
<li><p># H1</p></li>
<li><p>## H2</p></li>
<li><p>### H3</p></li>
<li><p>#### H4</p></li>
</ul></td>
<td style="text-align: center;"><p><strong>text</strong> <strong>decorations</strong></p>
<ul>
<li><p>**<strong>bold</strong>**</p></li>
<li><p>*<em>italic</em>*</p></li>
<li><p>_<em>italic</em>_</p></li>
<li><p>`inline code`</p></li>
</ul></td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><p><strong>strikethrough</strong></p>
<p>begin</p>
<p>using CommonMark</p>
<p>p() = enable!(Parser(), StrikethroughRule())</p>
<p>cm”””</p>
<p>&lt;del&gt;<del>this text is strikethrough using HTML</del>&lt;/del&gt;</p>
<p>&lt;s&gt;<del>this is also strikethrough</del>&lt;/s&gt;</p>
<p>”””p</p>
<p>end</p></td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;"><strong>2. Lists</strong></td>
<td colspan="3" style="text-align: center;"><p><strong>bullet lists</strong></p>
<p>- Item 1<br />
- Item 2<br />
- Sub-item<br />
- Sub-sub-item</p></td>
<td rowspan="2" style="text-align: center;"><p><strong>numbered lists</strong></p>
<p>1. First<br />
2. Second<br />
3. Third</p></td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><p><strong>task lists</strong></p>
<p>- [x] Completed<br />
- [ ] Not completed</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>3. Blockquotes and Horizontal Rules</strong></td>
<td colspan="4" style="text-align: left;">&gt; <em>This is a blockquote</em><br />
&gt;&gt; <em>Nested quote</em><br />
--- horizontal line</td>
</tr>
<tr>
<td style="text-align: left;"><strong>4. Code Blocks</strong></td>
<td colspan="2" style="text-align: center;"><p>julia</p>
<p>```julia<br />
f(x) = x^2<br />
f(3)<br />
```</p></td>
<td colspan="2" style="text-align: center;"><p>python</p>
<p>```python<br />
print("hello")<br />
```</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>5.Links and Images</strong></td>
<td colspan="4" style="text-align: left;"><p>[Pluto Website](<a href="https://plutojl.org">https://plutojl.org</a>)</p>
<p>![Alt text](<em>image_url_here</em>)</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>6. Tables</strong></td>
<td colspan="2" style="text-align: left;">| Variable | Meaning | Value |<br />
|----------|---------|-------|<br />
| x | input | 10 |<br />
| f(x) | output | 100 |</td>
<td colspan="2" style="text-align: center;"><p><em>alignment</em></p>
<p>| Left | Center | Right |<br />
|:-----|:------:|------:|<br />
| a | b | c |</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>7. Pluto Julia Interpolation</strong></td>
<td colspan="4" style="text-align: left;"><blockquote>
<p>for: x = 10</p>
<p>md"""<br />
The computed value is **$(x^2)**.<br />
"""</p>
<p>renders as:</p>
</blockquote>
<p><span class="math display"><em>T</em><em>h</em><em>e</em> <em>c</em><em>o</em><em>m</em><em>p</em><em>u</em><em>t</em><em>e</em><em>d</em> <em>v</em><em>a</em><em>l</em><em>u</em><em>e</em> <em>i</em><em>s</em> <strong>100</strong></span></p></td>
</tr>
<tr>
<td rowspan="3" style="text-align: left;"><strong>8. LaTeX Math</strong></td>
<td colspan="4" style="text-align: center;"><p><em>inline equation</em></p>
<p>$E = mc^2$</p>
<blockquote>
<p>renders as:</p>
</blockquote>
<p><span class="math display"><em>E</em> = <em>m</em><em>c</em><sup>2</sup></span></p></td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><p><em>block equation</em></p>
<blockquote>
<p>```math</p>
<p>\frac{1}{2 \pi}</p>
<p>```</p>
<p>renders as:</p>
</blockquote>
<p><span class="math display">$$\frac{1}{2\pi\ }$$</span></p>
<p><em>aligned equation</em></p>
<blockquote>
<p>md"""</p>
<p>```math</p>
<p>\begin{aligned}</p>
<p>E &amp;= mc^2 \\</p>
<p>F &amp;= ma \\</p>
<p>PV &amp;= nRT</p>
<p>\end{aligned}</p>
<p>```</p>
<p>”””</p>
<p>renders as:</p>
</blockquote>
<p><span class="math display"><em>E</em> = <em>m</em><em>c</em><sup>2</sup></span></p>
<p><span class="math display"><em>F</em> = <em>m</em><em>a</em></span></p>
<p><span class="math display"><em>P</em><em>V</em> = <em>n</em><em>R</em><em>T</em></span></p></td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><p><em>integral</em></p>
<blockquote>
<p>here is the Gaussian integral:</p>
</blockquote>
<p>`` \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi} ``</p>
<blockquote>
<p>renders as:</p>
</blockquote>
<p><span class="math display">$$\int_{- \infty}^{\infty}{e^{- x^{2}}dx} = \sqrt{\pi}``$$</span></p></td>
</tr>
</tbody>
</table>

*
*

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr>
<th><strong>9. Greek Letters</strong></th>
<th style="text-align: center;"><p>example</p>
<p>$\alpha$</p>
<p>$\beta$</p>
<p><span class="math display"><strong>.</strong></span></p>
<p><span class="math display"><strong>.</strong></span></p>
<p><span class="math display"><strong>.</strong></span></p>
<p>$\omega$</p></th>
<th style="text-align: center;"><p>renders as</p>
<p><span class="math display"><strong>α</strong></span></p>
<p><span class="math display"><strong>β</strong></span></p>
<p><span class="math display"><strong>.</strong></span></p>
<p><span class="math display"><strong>.</strong></span></p>
<p><span class="math display"><strong>.</strong></span></p>
<p><span class="math display"><strong>ω</strong></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>10. Best Practices</strong></td>
<td colspan="2"><ul>
<li><p>use <strong>consistent</strong> <strong>heading</strong> hierarchy</p></li>
<li><p>keep <strong>paragraphs</strong> <strong>short</strong> (3–5 lines)</p></li>
<li><p><strong>limit</strong> list <strong>nesting</strong> depth</p></li>
<li><p><strong>avoid</strong> <strong>HTML</strong> styling inside md""" <strong>blocks</strong></p></li>
<li><p>use <strong>fenced</strong> <strong>code</strong> <strong>blocks</strong> for all code</p></li>
<li><p>keep <strong>math</strong> in <strong>display</strong> <strong>blocks</strong> for clarity</p></li>
</ul></td>
</tr>
</tbody>
</table>
