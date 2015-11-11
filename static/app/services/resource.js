angular.module('moolah')
    .factory('TransactionService', ['$resource', 'API_URL', function($resource, API_URL) {
        return $resource('{}transactions/:id'.format(API_URL));
    }])

    .factory('ReportService', ['$http', 'REPORT_URLS', function($http, REPORT_URLS) {
        var buildGet = function(key) {
            return $http.get(REPORT_URLS[key]);
        };

        return {
            summary: function() {
                return buildGet('summary');
            },
            dailyTransactionReport: function() {
                return buildGet('dailyTransaction');
            }
        };
    }])

    .factory('SummaryService', ['$http', 'API_URL', function($http, API_URL) {
        return {
            get: function() {
                return $http.get('{}{}'.format(API_URL, 'summary/'));
            }
        };
    }])

    .factory('PurchaseService', ['$resource', 'API_URL', function($resource, API_URL) {
        return $resource('{}purchases/:id'.format(API_URL));
    }]);
