angular.module('moolah')

    .controller('moolahTodaysTransactionsController', ['TransactionService', function(TransactionService) {
        var self = this;
        self.api = self.api || {};
        self.resource = TransactionService;
        self.afterSave = self.afterSave || angular.noop;
        self.getQueryFilter = function() {
            return {
                date: moment()
            };
        };
        self.cardTitle = 'Today\'s Transactions';
    }])

    .directive('moolahTodaysTransactions', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'moolahTodaysTransactionsController',
            controllerAs: 'todaysTransCtrl',
            templateUrl: toStatic('app/directives/moolah-todays-transactions.html'),
            bindToController: true,
            scope: {
                api: '=?',
                afterSave: '=?'
            }
        };
    }]);
