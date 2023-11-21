---
layout: archive
title: "Album"
permalink: /album/
---

## My Photo Album

{% for photo in site._photos %}
  [![{{ photo.name }}]({{ site.baseurl }}{{ photo.url }})]({{ site.baseurl }}{{ photo.url }})
{% endfor %}
