/*global angular*/
angular.module('moolah', ['ngRoute'])
    .constant('STATIC_URL', '/static/')
    .config(function($routeProvider, STATIC_URL) {
        var toStatic = function(i) {
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
    });
