{% for prop in rowfor.properties %}
    {% if loop.first %}
        <tr class="supertype">
             <th class="supertype-name" colspan="3">Properties from <a   href="{{href_prefix}}{{rowfor.id}}">{{rowfor.id}}</a></th>
  
        </tr>
    {% endif %}
    
{% endfor %}
