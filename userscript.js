// ==UserScript==
// @name       Nike+ GPX-linker
// @namespace  http://ankkatalo.net/nplus2gpx
// @version    0.1
// @description  Adds button to nikeplus run detail page that uploads the track data to be parsed into gpx 
// @match      https://secure-nikeplus.nike.com/plus/activity/running/*/detail/*
// @copyright  2014+, Jussi Niskanen
// @require  http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js
// @grant    GM_addStyle
// ==/UserScript==

$(window).load(function(){ 
    $("body").append ( '                \
    <div id="sendnpd" onclick="$(\'#thedata\').attr(\'value\', JSON.stringify(window.np.baked_data)); $(\'#sendnpdform\').submit()"> \
        <form id="sendnpdform" action="YOUR SERVICE URL HERE" method="POST" target="_blank"> \
            <input id="thedata" name="thedata" type="hidden" value="imthedata"> \
        </form> \
        <span id="sendnpdtxt">Create GPX</span> \
    </div> \
' );
    
    GM_addStyle ( " \
    #sendnpd { \
        color: white; \
        background-color: black; \
        position: fixed; \
        left: 20px; \
        top: 100px; \
        width: 100px; \
        height: 60px; \
        cursor: pointer; \
        cursor: hand; \
        z-index:1000; /* overkills ftw */ \
        border-radius: 10px; \
    } \
\
    #sendnpdtxt { \
        position: relative; \
        left: 10px; \
        top: 20px; \
        font-weight: bold; \
    } \
" );
})

