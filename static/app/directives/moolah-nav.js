angular.module('moolah')

    .controller('moolahNavController', ['$location', 'LOGOUT_URL', 'USER_NAME', function($location, LOGOUT_URL, USER_NAME) {
        var self = this;

        self.logoutUrl = LOGOUT_URL;
        self.userName = USER_NAME;

        self.isActive = function(path) {
            return $location.path() === path;
        };
    }])

    .directive('moolahNav', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'moolahNavController',
            controllerAs: 'navController',
            templateUrl: toStatic('app/directives/moolah-nav.html')
        };
    }]);
