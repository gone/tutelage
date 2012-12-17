require(
    ["./common",], function(common){
        require(["jquery", "jqueryui", "_", "bootstrap", "colorbox", "chosen", "formset", "cs!main", "cs!validation", "cs!lessons", 'handlebars', "cs!rating"], function($, _){
            $(function(){
                if (typeof pagelogic !== "undefined") {
                    pagelogic()
                }
            });
        })
    });
