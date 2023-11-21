---
layout: archive
title: "Album"
permalink: /album/
#author_profile: true
---

## My Photo Album

{% for photo in site.static_files %}
  {% if photo.path contains 'photos' %}
    ![{{ photo.name }}]({{ photo.path | relative_url }})
    {{ photo.path }}  <!-- 调试信息 -->
    {{ photo.name }}  <!-- 调试信息 -->
  {% endif %}
{% endfor %}

