<!DOCTYPE html>
<html lang="en">
<!-- Generated from PropertyPage.tpl -->
<head>
    <title>{{ term.label }} - {{ sitename }}</title>
</head>
<body>
    {% set TERMTYPE = "Property" %}
    {% include 'PageHeader.tpl' with context %}
    <div><h2>Expected Types</h2>
        {% for type in term.rangeIncludes %}<a href="{{href_prefix}}{{type}}">{{ type }}</a>{% if not loop.last %}, {% endif %}{% endfor %}
    </div>
    <div><h2>Used on Types</h2>
        {% for type in term.domainIncludes %}<a href="{{href_prefix}}{{type}}">{{ type }}</a>{% if not loop.last %}, {% endif %}{% endfor %}
    </div>
</body>
</html>
