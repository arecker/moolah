angular.module('moolah')

    .controller('moolahTodaysTransactionsController', ['TransactionService', function(TransactionService) {
        var self = this;

        self.api.reload = function() {
            self.transactions = TransactionService.query({
                date: moment()
            });
        };

        self.api.reload();

    }])

    .directive('moolahTodaysTransactions', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'moolahTodaysTransactionsController',
            controllerAs: 'todaysTransCtrl',
            templateUrl: toStatic('app/directives/moolah-todays-transactions.html'),
            bindToController: true,
            scope: {
                api: '=?'
            }
        };
    }]);
