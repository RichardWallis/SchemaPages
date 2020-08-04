<!DOCTYPE html>
<html lang="en">
<!-- Generated from EnumerationValuePage.tpl -->
<head>
    <title>{{ term.label }} - {{ sitename }}</title>
</head>
<body>
    {% set TERMTYPE = "Enumeration Value" %}
    {% include 'PageHeader.tpl' with context %}
    <div>
        A member of the <a href="{{href_prefix}}{{ term.enumerationParent }}.html">{{ term.enumerationParent }}</a> enumeration type.
    </div>
</body>
</html>
