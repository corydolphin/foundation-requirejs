module.exports = (grunt) ->
  grunt.initConfig
    pkg: grunt.file.readJSON("package.json")
    jsTempDir: ".tmp/js"
    buildDir: ".build"
    srcDir: "src/"
    styleSrcDir: "<%= srcDir %>/styles"
    scriptsSrcDir: "<%= srcDir %>/scripts"
    configDir : "boilerflask/config"

# Compile our sass using compass.
    sass:
      options:
        includePaths: ["bower_components/foundation/scss"]

      dist:
        files:
          "<%= buildDir %>/css/app.css": "<%= styleSrcDir %>/app.scss"

# Compile our coffeescript to javascript, in the jsTempDir
    coffee:
      glob_to_multiple:
        options:
          bare: true

        expand: true
        flatten: true
        cwd: "<%= scriptsSrcDir %>"
        src: ["*.coffee"]
        dest: "<%= jsTempDir %>"
        ext: ".js"

# Use requirejs to manage dependencies in the compiled js files.
    requirejs:
      options:
        baseUrl: "<%= jsTempDir %>"
        mainConfigFile: "<%= jsTempDir %>/build.js"
        out: "<%= buildDir %>/js/app.js"

      dev:
        options:
          optimize: "none"

    uglify:
      options:
        mangle: true
        banner: "/*! <%= pkg.title || pkg.name %> - v<%= pkg.version + \"\\n\" %>" + "* <%= grunt.template.today(\"yyyy-mm-dd\") + \"\\n\" %>" + "* <%= pkg.homepage + \"\\n\" %>" + "* Copyright (c) <%= grunt.template.today(\"yyyy\") %> - <%= pkg.title %> */ <%= \"\\n\" %>"

      js:
        src: "<%=buildDir %>/js/app.js"
        dest: "<%=buildDir %>/js/app.min.js"

    cssmin:
      css:
        src: "<%= buildDir %>/css/app.css"
        dest: "<%= buildDir %>/css/app.min.css"

# Cleans the buildDir 
    clean:
      build:
        src:"<%= buildDir %>"

# Add hash of the files for revisions
    filerev:
      options:
        encoding: "utf8"
        algorithm: "md5"
        length: 8

      scripts:
        src: "<%=buildDir %>/js/app.min.js"
        dest: "<%=buildDir %>/js/"

      styles:
        src: "<%=buildDir %>/css/app.min.css"
        dest: "<%=buildDir %>/css/"

# Writes the transformation of assets from unversioned to versioned form, i.e.
# app.min.css -> app.min.550d9252.css. Useful for dynamic templating
    filerev_assets:
      assets:
        options:
          dest: 'assets.json'
          cwd: '.build/'
          prefix: 'static/'
          prettyPrint:true

    s3:
      options:
        key: ""
        secret: ""
        bucket: ""
        access: "public-read"
        gzip: true
        gzipExclude: [".png", ".woff", ".jpg"]
        maxOperations: 10
        headers:
          "Cache-Control": "public, max-age=31367678"
          "Origin": "*"
          "Vary": "Origin"
          "Access-Control-Allow-Origin": "*"

      assets:
        upload: [
            src: "<%= buildDir  %>/css/app.min.*.css"
            dest: "css/"
          ,
            src: "<%=buildDir %>/js/app.min.*.js"
            dest: "js/"
        ]


    watch:
      grunt:
        files: ["Gruntfile.js"]

      src:
        files: "<%= srcDir %>"
        tasks: ["build"]

    bgShell:
        _defaults:
          bg: true

        watch:
          cmd: "grunt watch"

        runPython:
          cmd: "python manage.py server"
          bg: false


  grunt.loadNpmTasks 'grunt-filerev-assets' 
  grunt.loadNpmTasks 'grunt-contrib-uglify'
  grunt.loadNpmTasks "grunt-contrib-requirejs"
  grunt.loadNpmTasks "grunt-contrib-cssmin"
  grunt.loadNpmTasks "grunt-sass"
  grunt.loadNpmTasks "grunt-contrib-watch"
  grunt.loadNpmTasks "grunt-contrib-coffee"
  grunt.loadNpmTasks "grunt-filerev"
  grunt.loadNpmTasks "grunt-s3"
  grunt.loadNpmTasks "grunt-contrib-clean"



  grunt.registerTask "build", ["sass", "coffee", "requirejs:dev"]
  grunt.registerTask "rev", ["filerev", "filerev_assets"]
  grunt.registerTask "production", ["clean","build", "uglify", "cssmin", "rev", "s3:assets"]
  grunt.registerTask "default", ["build", "bgShell"]