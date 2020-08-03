{% for sub in SUBSLIST %}
    {% if loop.first %}
     <br/><b><a  id="subtypes" title="Link: #subtypes" href="#subtypes" class="clickableAnchor" >More specific Types</a></b><ul>
    {% endif %}
	<li> <a href="{{href_prefix}}{{sub}}.html">{{sub}}</a> </li>
    {% if loop.last %}
     </ul>
    {% endif %}
{% endfor %}
