/*global angular*/
angular.module('moolah')

    .controller('moolahNavController', function($location) {
        var self = this;

        self.isActive = function(path) {
            return $location.path() === path;
        };
    })

    .directive('moolahNav', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'moolahNavController',
            controllerAs: 'navController',
            templateUrl: toStatic('directives/moolah-nav.html')
        };
    }]);
