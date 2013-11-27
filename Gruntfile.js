module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    jsTempDir: ".tmp/js",
    buildDir : ".build",
    sass: {
      options: {
        includePaths: ['bower_components/foundation/scss']
      },
      dist: {
        files: {
          '<%= buildDir %>/css/app.css': 'scss/app.scss'
        }        
      }
    },

    watch: {
      grunt: { files: ['Gruntfile.js'] },
      sass: {
        files: 'scss/**/*.scss',
        tasks: ['sass']
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
            optimize:"closure"            
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
        cwd: 'cs',
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