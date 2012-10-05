({
    appDir: ".",
    baseUrl: ".",
    dir: "../webapp-build",
    //Comment out the optimize line if you want
    //the code minified by UglifyJS.
    optimize: "none",
    //optimize: "closure",
    CompilerOptions: "",
    findNestedDependencies: true,
    paths: {
        "text": "require/text",
        "cs": "require/cs",
        "ember": "lib/ember-1.0.pre.min",
        "handlebars" : "lib/handlebars-1.0.0.beta.6",
        "_": "lib/underscore-min",
        "jquery": "require/require-jquery",
    },
    shim:{
        ember: {
            exports: "Ember"
        },
        _: {
            exports: "_",
        }

    },
    modules: [
        {
            name: "main",
        }
    ]
})
