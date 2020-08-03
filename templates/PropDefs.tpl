{% if term.properties|length > 0 %}{% set propstodisplay = True %}{% endif %}
{% for t in term.termStack %}
	  {% if t.properties|length > 0 %}{% set propstodisplay = True %}{% endif %}
{% endfor %}
{% if propstodisplay %}
	<table class="definition-table">
	    <thead>
	      <tr><th>Property</th><th>Expected Type</th><th>Description</th></tr>
	  </thead>
	  {% set rowfor = term %}{% include 'PropRow.tpl' with context %}
	  {% for t in term.termStack %}
	      {% set rowfor = t %}{% include 'PropRow.tpl' with context %}
	  {% endfor %}
	 </table>
{% endif %}
