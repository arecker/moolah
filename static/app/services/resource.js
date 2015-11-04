angular.module('moolah')
    .factory('TransactionService', function($resource) {
        return $resource('/api/transactions/');
    });
