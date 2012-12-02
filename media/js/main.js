require(
    ["./common",], function(common){
        require(["jquery", "_", "bootstrap", "colorbox", "chosen", "formset", "cs!main", "cs!validation", "cs!lessons", "cs!rating"], function($, _){
            $(function(){
                if (typeof pagelogic !== "undefined") {
                    pagelogic()
                }
            });


        })
    });
