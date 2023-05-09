---
layout: archive
title: "Album"
permalink: /album/
#author_profile: true
---

<div class="album">
  {% for photo in site.static_files %}
    {% if photo.path contains 'photos/' %}
      <div class="photo">
        <a href="{{ zhe }}{{/photos}}" target="_blank">
          <img src="{{ zhe }}{{ /photos}}" alt="{{ IMG_0102.JPG}}">
        </a>
      </div>
    {% endif %}
  {% endfor %}
</div>

