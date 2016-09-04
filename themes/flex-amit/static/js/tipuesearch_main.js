'use strict';

$(document).ready(function() {
    $('#tipue_search_input').tipuesearch({
        'show': 10,
        'mode': 'json',
        'showURL': false,
        'descriptiveWords': 25,
        'highlightEveryTerm': true,
        'contentLocation': '/tipuesearch_content.json'
    });
});
