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

	.factory('Transaction', ['$resource', 'API_URL', function($resource, API_URL) {
	    return $resource('{}transactions/:id'.format(API_URL));
	}])

	.factory('Purchase', ['$resource', 'API_URL', function($resource, API_URL) {
	    return $resource('{}purchases/:id'.format(API_URL));
	}])

	.factory('PurchaseBalance', ['$http', 'API_URL', function($http, API_URL) {
	    return function() {
		return $http.get('{}purchases/total/'.format(API_URL));
	    };
	}])

	.factory('SummaryReport', ['$http', 'API_URL', function($http, API_URL) {
	    return function() {
		return $http.get('{}reports/summary/'.format(API_URL));
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

	.controller('DashboardController', ['Purchase', 'PurchaseBalance', 'Transaction', 'SummaryReport', function(Purchase, PurchaseBalance, Transaction, SummaryReport) {

	    var self = this;

	    self.reloadTransactions = function() {
		Transaction.query().$promise.then(function(d) {
		    self.todaysTransactions = d;
		    var values = d.map(function(i) { return i.amount; });
		    self.todaysTransactionsTotal = values.reduce(function(a, b) {
			return Number(a) + Number(b);
		    }, 0);

		    self.totalIsPositive = self.todaysTransactionsTotal > 0;
		});
	    };

	    self.reloadPurchases = function() {
		Purchase.query().$promise.then(function(d) {
		    self.purchases = d;
		});
		PurchaseBalance().then(function(d) {
		    self.purchaseBalance = d.data.balance;
		    self.balanceIsPositive = self.purchaseBalance > 0;
		});
	    };

	    self.reloadSummary = function() {
		SummaryReport().then(function(d) {
		    self.summary = d.data;
		});
	    };

	    self.submitTransaction = function() {
		Transaction.save(self.newTransaction, function() {
		    self.newTransaction = {};
		    self.reloadTransactions();
		    self.reloadSummary();
		});
	    };

	    self.submitPurchase = function() {
		Purchase.save(self.newPurchase, function() {
		    self.newPurchase = {};
		    self.reloadPurchases();
		});
	    };

	    self.reloadTransactions();
	    self.reloadSummary();
	    self.reloadPurchases();

	}]);

}(angular, jQuery));
