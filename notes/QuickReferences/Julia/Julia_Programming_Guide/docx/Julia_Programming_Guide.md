> Markdown version for convenient browsing. Original files:
> - PDF: [Julia_Programming_Guide.pdf](../Julia_Programming_Guide.pdf)
> - DOCX: [Julia_Programming_Guide.docx](Julia_Programming_Guide.docx)

---

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 9%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: left;"><strong>Julia Programming Language</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>Julia combines high-level expressive syntax with high-performance execution, making it particularly well-suited for scientific computing, data science, numerical analysis, and systems-level research workflows.</strong></p>
<p><strong>***created by Jeff Bezanson, Stefan Karpinski, Viral B. Shah, and Alan Edelman</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td><strong>Print</strong></td>
<td colspan="2" style="text-align: left;"><p><strong>print to screen:</strong></p>
<blockquote>
<p><strong>println("Hello, world!")</strong></p>
</blockquote></td>
</tr>
<tr>
<td><strong>Markdown</strong></td>
<td colspan="2"><p><strong>markdown: used in julia to write text in Pluto notebooks by use ‘ md””” ‘ string inside Pluto cell</strong></p>
<blockquote>
<p><strong>md"""</strong></p>
<p><strong>This text is in **bold** and _italic_.</strong></p>
<p><strong>"""</strong></p>
</blockquote>
<p><strong>Ctrl+M</strong></p>
<p><strong>keyboard shortcut:</strong></p></td>
</tr>
<tr>
<td><strong>Image in Markdown</strong></td>
<td colspan="2"><p><strong>method 1: access online image</strong></p>
<p><strong>target url: <a href="https://i.imgur.com/qHCI8RS.png">https://i.imgur.com/qHCI8RS.png</a></strong></p>
<blockquote>
<p><strong>md"""</strong></p>
<p><strong>![Description of the image](<a href="https://i.imgur.com/qHCI8RS.png">https://i.imgur.com/qHCI8RS.png</a>)</strong></p>
<p><strong>"""</strong></p>
</blockquote>
<p><strong>method 2: local image</strong></p>
<p><strong>for a local image to render in the notebook, the image has to be packaged and stored in the same or child directory with the notebook</strong></p>
<p><strong>target image: ./image.png</strong></p>
<blockquote>
<p><strong>using PlutoUI</strong></p>
<p><strong>PlutoUI.LocalResource(".</strong>/images/image.png<strong>")</strong></p>
</blockquote></td>
</tr>
<tr>
<td><strong>Control Flow</strong></td>
<td colspan="2"><p><strong>if statements: conditional evaluation</strong></p>
<blockquote>
<p><strong>if x &lt; y</strong></p>
<p><strong>println("x is smaller")</strong></p>
<p><strong>else</strong></p>
<p><strong>println("y is smaller")</strong></p>
<p><strong>end</strong></p>
</blockquote>
<p><strong>for loop: range-restricted iteration</strong></p>
<blockquote>
<p><strong>for i in 1:5</strong></p>
<p><strong>println(i)</strong></p>
<p><strong>end</strong></p>
</blockquote>
<p><strong>while loop: conditional iteration</strong></p>
<blockquote>
<p><strong>n = 0</strong></p>
<p><strong>while n &lt; 3</strong></p>
<p><strong>n += 1</strong></p>
<p><strong>end</strong></p>
</blockquote></td>
</tr>
<tr>
<td><strong>Data Structures</strong></td>
<td colspan="2"><p><strong>arrays:</strong></p>
<p><strong>push!</strong></p>
<p><strong>inserts items into a mutable collection by changing the existing collection instead of creatin a new one</strong></p>
<blockquote>
<p><strong>arr = [1, 2, 3]</strong></p>
<p><strong>push!(arr, 4)</strong></p>
</blockquote>
<p><strong>dict:</strong></p>
<p><strong>phonebook = Dict("Alice"=&gt;"1234", "Bob"=&gt;"5678")</strong></p>
<p><strong>type definition:</strong></p>
<blockquote>
<p><strong>struct Point</strong></p>
<p><strong>x::Float64</strong></p>
<p><strong>y::Float64</strong></p>
<p><strong>end</strong></p>
</blockquote></td>
</tr>
<tr>
<td><strong>Collection Manipulation</strong></td>
<td colspan="2"><p><strong>list comprehensions</strong></p>
<blockquote>
<p><strong>squares = [i^2 for i in 1:10]</strong></p>
</blockquote>
<p><strong>higher-order function</strong></p>
<blockquote>
<p><strong>apply_twice(f, x) = f(f(x))</strong></p>
</blockquote>
<p><strong>map / filter</strong></p>
<blockquote>
<p><strong>evens = filter(x -&gt; x % 2 == 0, 1:10)</strong></p>
</blockquote></td>
</tr>
<tr>
<td><strong>Multiple Dispatch</strong></td>
<td colspan="2"><p><strong>core Julia design feature: the specific implementation of a function is chosen at runtime based on the data types of all of its arguments</strong></p>
<blockquote>
<p><strong>f(x::Int) = "integer"</strong></p>
<p><strong>f(x::String) = "string"</strong></p>
</blockquote>
<p><strong>this allows generic functions to have many specialized behaviors for different combinations of input types</strong></p>
<p><strong>method on type: defines a function using ‘ :: ‘ notation</strong></p>
<blockquote>
<p><strong>distance(a::Point, b::Point) =</strong></p>
<p><strong>sqrt((a.x-b.x)^2 + (a.y-b.y)^2)</strong></p>
</blockquote>
<p><span class="math display">$$\sqrt{\left( \mathbf{x}_{\mathbf{1}}\mathbf{-}\mathbf{x}_{\mathbf{2}} \right)^{\mathbf{2}}\mathbf{+}\left( \mathbf{y}_{\mathbf{1}}\mathbf{-}\mathbf{y}_{\mathbf{2}} \right)^{\mathbf{2}}}$$</span></p>
<p><strong>Euclidean Distance Formula in Julia</strong></p>
<p><strong>Julia chooses which method to implement based on number of arguments</strong></p>
<p><strong>generic function with dispatch</strong></p>
<blockquote>
<p><strong>area(x::Number, y::Number) = x*y</strong></p>
<p><strong>area(x::AbstractVector) = sum(x)</strong></p>
</blockquote></td>
</tr>
<tr>
<td><strong>Tuple Unpacking</strong></td>
<td colspan="2"><p><strong>comma delineated dual assignment</strong></p>
<blockquote>
<p><strong>a, b = 1, 2</strong></p>
</blockquote>
<p><strong>equates to,</strong></p>
<blockquote>
<p><strong>a = 1, b = 2</strong></p>
</blockquote></td>
</tr>
<tr>
<td><p><strong>Interactivity UI Elements:</strong></p>
<p><strong>Sliders</strong></p></td>
<td colspan="2"><p><strong>@bing with PlutoUI</strong></p>
<p><strong>create interactive UI elements</strong></p>
<blockquote>
<p><strong>using PlutoUI</strong></p>
<p><strong>@bind apples Slider(</strong>5:50<strong>)</strong></p>
<p><strong>apples</strong></p>
<p><strong>repeat(“”, apples)</strong></p>
</blockquote>
<p><strong>output:</strong></p>
<p><strong>the @bind command creates the slider with a range(5:50)</strong></p>
<p><img src="generated_media\Julia_Programming_Guide\media\image1.png" style="width:2.43211in;height:0.5524in" /></p>
<p><strong>adjusting the slider adjust the number of apples displayed</strong></p>
<p><strong>“”</strong></p></td>
</tr>
<tr>
<td><strong>Plots</strong></td>
<td colspan="2"><p><strong>there are several plotting libraries available</strong></p>
<p><strong>examples: Makie.jl, PlutoPlotly.jl, Gadify.jl, Plots.jl</strong></p>
<p><strong>Plots.jl</strong></p>
<blockquote>
<p><strong>using Plots</strong></p>
<p><strong>plot([4,5,8,2,3,1,0])</strong></p>
<p><img src="generated_media\Julia_Programming_Guide\media\image2.png" style="width:2.38483in;height:1.62199in" /></p>
</blockquote>
<p><strong>result</strong></p>
<p><strong>combining multiple plot calls in a single cell</strong></p>
<blockquote>
<p><strong>data = rand(100)::Vector{Float64}</strong></p>
<p><strong>let</strong></p>
</blockquote>
<p><strong>A let block creates a local scope, allowing you to use mutable operations like plot! and !hline to modify an existing plot to build a single complex object.</strong></p>
<blockquote>
<p><strong>plot(data)</strong></p>
<p><strong># use the ! exclamation mark to modify the previous plot</strong></p>
<p><strong>scatter!(data)</strong></p>
<p><strong># add a horizontal line</strong></p>
<p><strong>mean = sum(data) / length(data)</strong></p>
<p><strong>hline!([mean]; label="Average value")</strong></p>
<p><strong>end</strong></p>
</blockquote>
<p><img src="generated_media\Julia_Programming_Guide\media\image3.png" style="width:2.28855in;height:1.50443in" /></p>
<p><strong>result</strong></p></td>
</tr>
<tr>
<td><p><strong>LaTeX</strong></p>
<p><strong>note: the legacy</strong></p>
<p><strong>LaTeX syntax:</strong></p>
<p><strong>$\frac{1}{2 \pi}$</strong></p>
<p><strong>is deprecated</strong></p>
<p><strong>.</strong></p></td>
<td colspan="2"><p><strong>Pluto has built-in LaTeX support for math equations for use inside markdown</strong></p>
<p><strong>notice double back-tics</strong></p>
<p><strong>method 1: inline math</strong></p>
<blockquote>
<p><strong>md”””</strong></p>
<p><strong>inline equation: ``\frac{1}{2 \pi}``.</strong></p>
<p><strong>”””</strong></p>
<p><em>inline equation:</em> <span class="math inline">$\frac{\mathbf{1}}{\mathbf{2}\mathbf{\pi}}$</span></p>
</blockquote>
<p><strong>inline</strong></p>
<p><strong>result</strong></p>
<p><strong>method 2: block math</strong></p>
<blockquote>
<p><strong>md"""</strong></p>
<p><strong>block equation:</strong></p>
</blockquote>
<p><em>block equation:</em></p>
<p><span class="math display">$$\frac{\mathbf{1}}{\mathbf{2}\mathbf{\pi}}$$</span></p>
<blockquote>
<p><strong>```math</strong></p>
<p><strong>\frac{1}{2 \pi}</strong></p>
<p><strong>```</strong></p>
<p><strong>"""</strong></p>
</blockquote>
<p><strong>block</strong></p>
<p><strong>result</strong></p></td>
</tr>
<tr>
<td><strong>Links</strong></td>
<td colspan="2"><p><strong>the ‘#’ character can be used to link to specific sections in a Pluto notebook:</strong></p>
<blockquote>
<p><strong>global variables: #variable_name</strong></p>
<p><strong>function definitions: #function_name</strong></p>
<p><strong>markdown headers: #header-text</strong></p>
</blockquote>
<p><strong>inside the notebook:</strong></p>
<blockquote>
<p><strong>md"""</strong></p>
<p><strong>Take a look at [the fruits variable](#fruits).</strong></p>
<p><strong>"""</strong></p>
</blockquote>
<p><strong>displayed text</strong></p>
<p><strong>link name</strong></p></td>
</tr>
</tbody>
</table>

*
*

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>References</strong></td>
<td><p><strong>Julia. (n.d.) Tutorials Point <a href="https://www.tutorialspoint.com/julia/julia_tutorial.pdf">https://www.tutorialspoint.com/julia/julia_tutorial.pdf</a></strong></p>
<p><strong><em>Julia Documentation · The Julia Language</em>. (n.d.). <a href="https://docs.julialang.org/en/v1/">https://docs.julialang.org/en/v1/</a></strong></p>
<p><strong><em>Linking</em>. (n.d.). <a href="https://plutojl.org/en/docs/linking/">https://plutojl.org/en/docs/linking/</a></strong></p>
<p><strong><em>Markdown</em>. (n.d.). <a href="https://plutojl.org/en/docs/markdown/">https://plutojl.org/en/docs/markdown/</a></strong></p>
<p><strong>Wikipedia contributors. (2026, February 11). <em>Julia (programming language)</em>. Wikipedia. <a href="https://en.wikipedia.org/wiki/Julia_(programming_language)">https://en.wikipedia.org/wiki/Julia_(programming_language)</a></strong></p></td>
</tr>
<tr>
<td colspan="2"></td>
</tr>
</tbody>
</table>
