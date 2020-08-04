<!DOCTYPE html>
<html lang="en">
<!-- Generated from DataType.tpl -->
<head>
    <title>{{ term.label }} - {{ sitename }}</title>
</head>
<body>
    {% set TERMTYPE = "Data Type" %}
    {% include 'PageHeader.tpl' with context %}
    <div>
        {% for prop in term.properties %}
        {% if loop.first %}<h2>Specific Properties</h2>{% endif %}<a href="{{href_prefix}}{{prop}}.html">{{ prop }}</a>{% if not loop.last %}, {% endif %}{% endfor %}
    </div>
    <div>
        <h2>Expected Type For</h2>
        {% for type in term.expectedTypeFor %}
        <a href="{{href_prefix}}{{type}}.html">{{ type }}</a>{% if not loop.last %}, {% endif %}{% endfor %}
    </div>
    <div>
        {% for sub in term.subs %}
        {% if loop.first %}<h2>More Specific DataTypes</h2>{% endif %}<a href="{{href_prefix}}{{sub}}.html">{{ sub }}</a>{% if not loop.last %}, {% endif %}{% endfor %}
    </div>
</body>
</html>
