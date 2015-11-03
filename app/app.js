/*global angular*/
angular.module('moolah', ['ngRoute'])
    .constant('STATIC_URL', '/static/')
    .config(function($routeProvider, STATIC_URL) {
        $routeProvider
            .when('/', {
                templateUrl: '{}{}'.format(STATIC_URL, 'views/summary.html'),
                controller: 'SummaryController',
                controllerAs: 'controller'
            });
    });
