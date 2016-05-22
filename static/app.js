(function(angular, jQuery, undefined) {
    if (!String.prototype.format) {
	String.prototype.format = function () {
	    var i = 0, args = arguments;
	    return this.replace(/{}/g, function () {
		return typeof args[i] != 'undefined' ? args[i++] : '';
	    });
	};
    }

    jQuery(document).ready(function() {
	$.material.init();
    });

    angular.module('moolah', ['ngRoute', 'ngResource'])

	.config(['$httpProvider', '$routeProvider', '$resourceProvider', 'STATIC_URL',
		 function($httpProvider, $routeProvider, $resourceProvider, STATIC_URL) {

		     var toStatic = function(i) {
			 return '{}{}'.format(STATIC_URL, i);
		     };

		     $httpProvider.defaults.xsrfCookieName = 'csrftoken';
		     $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
		     $resourceProvider.defaults.stripTrailingSlashes = false;

		     $routeProvider
			 .when('/', {
			     templateUrl: toStatic('views/dashboard.html'),
			     controller: 'DashboardController',
			     controllerAs: 'dashboardCtrl'
			 });
		 }])

	.factory('toStatic', ['STATIC_URL', function(STATIC_URL) {
	    return function(i) {
		return '{}{}'.format(STATIC_URL, i);
	    };
	}])

	.controller('moolahNavController', ['$location', 'LOGOUT_URL', 'USER_NAME', function($location, LOGOUT_URL, USER_NAME) {
	    var self = this;

	    self.logoutUrl = LOGOUT_URL;
	    self.userName = USER_NAME;

	    self.isActive = function(path) {
		return $location.path() === path;
	    };

	}]).directive('moolahNav', ['toStatic', function(toStatic) {
	    return {
		restrict: 'E',
		controller: 'moolahNavController',
		controllerAs: 'navController',
		templateUrl: toStatic('views/nav.html')
	    };
	}])

	.controller('DashboardController', [function() {

	}]);

}(angular, jQuery));
