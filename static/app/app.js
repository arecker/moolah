angular.module('moolah', ['ngRoute', 'ngResource'])
    .config(['$httpProvider', '$routeProvider', 'STATIC_URL', function($httpProvider, $routeProvider, STATIC_URL) {

        var toStatic = function(i) {
            // no services in app.config :(
            return '{}{}'.format(STATIC_URL, i);
        };

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $routeProvider
            .when('/', {
                templateUrl: toStatic('app/views/today.html'),
                controller: 'TodayController',
                controllerAs: 'controller'
            });
    }]);
