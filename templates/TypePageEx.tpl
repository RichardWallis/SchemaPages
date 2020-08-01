<!DOCTYPE html>
<html lang="en">
<!-- Generated from TypePage.tpl -->
<head>
    <title>{{ term.label }} - {{ sitename }}</title>
</head>
<body>
    {% set TERMTYPE = "Type" %}
    {% include 'PageHeader.tpl' with context %}
    <div id="mainContent">
    {% include 'InfoBlock.tpl' with context %}
    {% include 'PropDefs.tpl' with context %}
    </div> <!-- mainContent -->
</body>
</html>
