module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    jsBuildDir: ".tmp",
    sass: {
      options: {
        includePaths: ['bower_components/foundation/scss']
      },
      dist: {
        files: {
          'css/app.css': 'scss/app.scss'
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
          baseUrl: ".tmp/js",
          mainConfigFile: ".tmp/js/build.js",
          out: ".build/optimized.js",
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
        cwd: 'cs',
        src: ['*.coffee'],
        dest: '<%= jsBuildDir %>/js',
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