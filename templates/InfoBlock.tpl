<div id="infoblock">
    <h1>{{ term.label }}</h1>
    <h3>A Schema.org {{ TERMTYPE }}</h3>
    <div><em>Canonical URI: {{term.uri}}</em><br/></div>
    {% if term.pending %}<strong>Note:</strong> <span style="color: ff0000;">This term is pending in the vocabulary.</span><br/>{% endif %}
    <br/>
    <div class="superPaths>"
    {% for superPath in term.superPaths %}
        {% for super in superPath %} {%if loop.length > 1 %}{% if not loop.first %}-> {% endif %}{{ super }}{% endif %}{% endfor %}
        <br/>
    {% endfor %}
    </div>
    <br/>
    <div class="description">{{term.comment|safe}}</div>
</div> <!-- infoblock -->

