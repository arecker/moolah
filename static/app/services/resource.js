angular.module('moolah')
    .factory('TransactionService', ['$resource', 'API_URL', function($resource, API_URL) {
        return $resource('{}transactions/'.format(API_URL));
    }]);
