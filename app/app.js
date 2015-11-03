/*global angular*/
angular.module('moolah', ['ngRoute'])
    .constant('STATIC_URL', '/static/')
    .config(function($routeProvider, STATIC_URL) {
        var toStatic = function(i) {
            return '{}{}'.format(STATIC_URL, i);
        };

        $routeProvider
            .when('/', {
                templateUrl: toStatic('views/summary.html'),
                controller: 'SummaryController',
                controllerAs: 'controller'
            })

            .when('/today', {
                templateUrl: toStatic('views/today.html'),
                controller: 'TodayController',
                controllerAs: 'controller'
            });
    });
