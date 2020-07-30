<!DOCTYPE html>
<html lang="en">
<!-- Generated from TypePage.tpl -->
<head>
    <title>{{ term.label }} - {{ sitename }}</title>
</head>
<body>
    {% set TERMTYPE = "Type" %}
    {% include 'PageHeader.tpl' with context %}
    <div><h2>Specific Properties</h2>
        {% for prop in term.properties %}<a href="{{href_prefix}}{{prop}}">{{ prop }}</a>{% if not loop.last %}, {% endif %}{% endfor %}
    </div>
    <div><h2>All Available Properties</h2>
        {% for prop in term.allProperties %}<a href="{{href_prefix}}">{{ prop }}</a>{% if not loop.last %}, {% endif %}{% endfor %}
    </div>
    <div>
        {% for type in term.expectedTypeFor %}
        {% if not loop.first %}<h2>Expected Type For</h2>{% endif %}<a href="{{href_prefix}}{{type}}">{{ type }}</a>{% if not loop.last %}, {% endif %}{% endfor %}
    </div>
</body>
</html>
