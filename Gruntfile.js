module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    jsTempDir: ".tmp/js",
    buildDir : ".build",
    srcDir : "src/",
    styleSrcDir: "<%= srcDir %>/styles",
    scriptsSrcDir: "<%= srcDir %>/scripts",
    sass: {
      options: {
        includePaths: ['bower_components/foundation/scss']
      },
      dist: {
        files: {
          '<%= buildDir %>/css/app.css': '<%= styleSrcDir %>/app.scss'
        }        
      }
    },

    watch: {
      grunt: { files: ['Gruntfile.js'] },
      sass: {
        files: '<%= srcDir %>',
        tasks: ['build']
      }
    },
    requirejs: {
        options: {
          baseUrl: "<%= jsTempDir %>",
          mainConfigFile: "<%= jsTempDir %>/build.js",
          out: "<%= buildDir %>/js/app.js",
        },
        dev: {
          options:{
            optimize:"none"
          }
        },
        production:{
          options:{
            optimize:"uglify2"            
          }
        }
    },
    coffee: {
      glob_to_multiple: {
        options:{
          bare:true
        },
        expand: true,
        flatten: true,
        cwd: '<%= scriptsSrcDir %>',
        src: ['*.coffee'],
        dest: '<%= jsTempDir %>',
        ext: '.js'
      }
    },

  });

  grunt.loadNpmTasks('grunt-contrib-requirejs');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-coffee');

  grunt.registerTask('build', ['sass', 'coffee', 'requirejs:dev']);
  grunt.registerTask('default', ['build','watch']);
}