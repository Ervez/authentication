module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        less: {
            development: {
                files: {
                    'userauth/static/css/userauth.main.css': 'userauth/static/less/userauth.main.less'
                }
            }
        },
        cssmin: {
            target: {
                files: {
                    'userauth/static/css/userauth.main.css': ['userauth/static/css/userauth.main.less']
                }
            }
        },
        watch: {
            styles: {
                files: ['static/less/*.less'],
                tasks: ['less', 'cssmin'],
                options: {
                    spawn: false,
                }
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('default', ['watch']);
};