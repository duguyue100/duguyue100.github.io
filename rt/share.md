---
layout: page
title: Local File Sharing
permalink: /share
---

<div style="display: block; text-align: center; background-color: #f5ecc0">
<hr>
<p id="shared-page"></p>

<script>
    function isSiteOnline(url,callback) {
        // try to load favicon
        var timer = setTimeout(function(){
            // timeout after 5 seconds
            callback(false);
        },5000)

        var img = document.createElement("img");
        img.onload = function() {
            clearTimeout(timer);
            callback(true);
        }

        img.onerror = function() {
            clearTimeout(timer);
            callback(false);
        }

        img.src = url;
    }

    share_url = "http://localhost:8000"

    isSiteOnline(share_url,function(found){
        if(found) {
            document.getElementById("shared-page").innerHTML = '<iframe src=share_url></iframe>';
        }
        else {
            document.getElementById("shared-page").innerHTML = '<iframe width="560" height="315" src="https://www.youtube.com/embed/oAPjTHA19Kw" frameborder="0" allowfullscreen></iframe>';
        }
    })
</script>
<hr>
</div>
