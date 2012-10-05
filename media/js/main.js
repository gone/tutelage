require({
    paths: {
        "text": "require/text",
        "cs": "require/cs",
        "ember": "lib/ember-1.0.pre",
        "handlebars" : "lib/handlebars-1.0.0.beta.6",
        "_": "lib/underscore-min",
        "jquery": "require/require-jquery",
        "bootstrap": "lib/bootstrap",
        "colorbox": "lib/jquery.colorbox-min",
    },
    shim:{
        ember: {
            exports: "Ember",
            deps: ['jquery', 'handlebars']
        },
        _: {
            exports: "_",
        },
        bootstrap: {
            deps: ['jquery']
        },
        colorbox: {
            deps: ['jquery']
        }
    },
        urlArgs: "bust=" +  (new Date()).getTime(),
},
        ["jquery", "ember", "_", "bootstrap", "colorbox", "cs!main"], function($, Em, _){
            $(function(){
            });
        });
