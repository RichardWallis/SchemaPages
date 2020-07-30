<!-- Header start from PageHeader.tpl -->
<div id="container">
	<div id="intro">
		<div id="pageHeader">
			<div class="wrapper">
				<div id="sitename">
				<h1>
					<a href="/">{{ sitename }}</a>
				</h1>
			</div>
		</div>
	</div>
</div>
<div id="selectionbar">
	<div class="wrapper">
		<ul>
	        {% if menu_sel == "Documentation" %}
	        <li class="activelink">
	        {% else %}
	        <li>
	        {% endif %}
				<a href="{{ docsdir }}documents.html">Documentation</a>
			</li>
	        {% if menu_sel == "Schemas" %}
	        <li class="activelink">
	        {% else %}
	        <li>
	        {% endif %}
				<a href="{{ docsdir }}schemas.html">Schemas</a>
			</li>
			<li>
	        {% if home_page == "True" %}
				<a href="{{ docsdir }}about.html">About</a>
	        {% else %}
				<a href="{{ homedir }}/">Home</a>
	        {% endif %}
			</li>
		</ul>
	</div>
</div>
    <h1>{{ term.label }}</h1>
    <h3>A Schema.org {{ TERMTYPE }}</h3>
    {% if term.pending %}<strong>Note:</strong> <span style="color: ff0000;">This term is pending in the vocabulary.</span>{% endif %}
    <div class="breadcrumbs>"
    {% for breadcrumb in term.breadcrumbs %}
        {% for crumb in breadcrumb %} {%if loop.length > 1 %}{% if not loop.first %}-> {% endif %}{{ crumb }}{% endif %}{% endfor %}
        <br/>
    {% endfor %}
    </div>
    <div class="description">{{term.comment|safe}}</div>


<!-- Header end from PageHeader.tpl -->
