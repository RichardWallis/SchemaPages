.html<!DOCTYPE html>
<html lang="en">
<!-- Generated from TypePage.tpl -->
<head>
    <title>{{ term.label }} - {{ sitename }}</title>
</head>
<body>
    {% set TERMTYPE = "Type" %}
    {% include 'PageHeader.tpl' with context %}
    <div><h2>Specific Properties</h2>
        {% for prop in term.properties %}<a href="{{href_prefix}}{{prop}}.html">{{ prop }}</a>{% if not loop.last %}, {% endif %}{% endfor %}
    </div>
    <div>
        {% for type in term.expectedTypeFor %}
        {% if loop.first %}<h2>Expected Type For</h2>{% endif %}<a href="{{href_prefix}}{{type}}">{{ type }}</a>{% if not loop.last %}, {% endif %}{% endfor %}
    </div>
</body>
</html>
