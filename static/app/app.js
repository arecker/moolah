angular.module('moolah', ['ngRoute', 'ngResource'])
    .config(['$routeProvider', 'STATIC_URL', function($routeProvider, STATIC_URL) {

        var toStatic = function(i) {
            // no services in app.config :(
            return '{}{}'.format(STATIC_URL, i);
        };

        $routeProvider
            .when('/', {
                templateUrl: toStatic('app/views/summary.html'),
                controller: 'SummaryController',
                controllerAs: 'controller'
            })

            .when('/today', {
                templateUrl: toStatic('app/views/today.html'),
                controller: 'TodayController',
                controllerAs: 'controller'
            });
    }]);
