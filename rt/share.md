---
layout: page
title: Local File Sharing
permalink: /share
---

<div style="display: block; text-align: center; background-color: #f5ecc0">
<hr>
<p id="shared-page"></p>

<script>
    function isSiteOnline(url) {
        // try to load favicon
        var timer = setTimeout(function(){
            // timeout after 5 seconds
            return false;
        },5000)

        var img = document.createElement("img");
        img.onload = function() {
            clearTimeout(timer);
            return true;
        }

        img.onerror = function() {
            clearTimeout(timer);
            return false;
        }

        img.src = url;
    }

    var share_url = "http://localhost:8000"

    if (isSiteOnline(share_url) == true) {
        document.getElementById("shared-page").innerHTML = '<iframe src=share_url></iframe>';
    }
    else {
            document.getElementById("shared-page").innerHTML = '<iframe width="560" height="315" src="https://www.youtube.com/embed/oAPjTHA19Kw" frameborder="0" allowfullscreen></iframe>';
    }

</script>
<hr>
</div>
