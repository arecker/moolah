angular.module('moolah')

    .controller('moolahTodaysTransactionsController', ['TransactionService', function(TransactionService) {
        var self = this;

        self.showForm = false;
        self.newTransaction = {};
        self.afterSave = self.afterSave || angular.noop;
        self.api = self.api || {};

        self.formToggle = function() {
            self.showForm = !self.showForm;
        };

        self.submit = function() {
            TransactionService.save(self.newTransaction, function() {
                self.afterSave();
                self.newTransaction = {};
            });
        };

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
                api: '=?',
                afterSave: '=?'
            }
        };
    }]);
