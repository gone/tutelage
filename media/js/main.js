require({
    paths: {
        "text": "require/text",
        "cs": "require/cs",
        "handlebars" : "lib/handlebars-1.0.0.beta.6",
        "_": "lib/underscore-min",
        "jquery": "require/require-jquery",
        "bootstrap": "lib/bootstrap",
        "colorbox": "lib/jquery.colorbox-min",
        "chosen": "lib/chosen.jquery.min",
        "liveValidation": "lib/jquery.validationEngine",
        "liveValidationEn": "lib/jquery.validationEngine-en",
        "popcorn": "lib/popcorn-complete",
        "formset":'lib/jquery.formset',
    },
    shim: {
        _: {
            exports: "_"
        },
        bootstrap: {
            deps: ['jquery']
        },
        colorbox: {
            deps: ['jquery']
        },
        chosen: {
            deps: ['jquery']
        },
        liveValidation: {
            deps: ['jquery', "liveValidationEn"]
        },
        popcorn: {
            exports: "Popcorn",
            deps: ['jquery']
        },
        formset: {
            deps: ['jquery']
        },
        fileupload: {
            deps: ['jquery']
        }
    },
        urlArgs: "bust=" +  (new Date()).getTime(),
},
        ["jquery", "_", "bootstrap", "colorbox", "chosen", "cs!main", "cs!validation", "formset", "cs!lessons"], function($, Em, _){
            $(function(){
                if (typeof pagelogic !== "undefined") pagelogic()
            });
        });
