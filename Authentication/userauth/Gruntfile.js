module.exports = function(grunt) {

    grunt.initConfig({
        less: {
            development: {
                options: {
                    paths: ['static/less']
                },
                files: {
                    'static/css/userauth.css': 'static/less/userauth.less',
                    'static/css/login.register.css': 'static/less/login.register.less',
                }
            }
        },

        watch: {
            styles: {
                files: ['static/less/**/*.less'],
                tasks: ['less']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['less', 'watch']);

};

