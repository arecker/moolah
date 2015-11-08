angular.module('moolah', ['ngRoute', 'ngResource'])
    .config(['$httpProvider', '$routeProvider', '$resourceProvider', 'STATIC_URL', function($httpProvider, $routeProvider, $resourceProvider, STATIC_URL) {

        var toStatic = function(i) {
            // no services in app.config :(
            return '{}{}'.format(STATIC_URL, i);
        };

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $resourceProvider.defaults.stripTrailingSlashes = false;

        $routeProvider
            .when('/', {
                templateUrl: toStatic('app/views/dashboard.html'),
                controller: 'DashboardController',
                controllerAs: 'dashboardCtrl'
            });
    }]);
