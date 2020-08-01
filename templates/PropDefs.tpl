<table class="definition-table">
        <thead>
  <tr><th>Property</th><th>Expected Type</th><th>Description</th>               
  </tr>
  </thead>
  {% set rowfor = term %}
  {% include 'PropRow.tpl' with context %}
  {% for t in term.termStack %}
      {% set rowfor = t %}
      {% include 'PropRow.tpl' with context %}
  {% endfor %}
 </table>
