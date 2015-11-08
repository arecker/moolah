angular.module('moolah')
    .controller('DashboardController', ['TransactionService', function(TransactionService) {
        var self = this;

        self.newTransaction = {};
        self.summaryApi = {};
        self.todaysTransApi = {};

        self.goGoGadgetReloadEverything = function() {
            self.todaysTransApi.reload();
            self.summaryApi.reload();
        };

        self.addTransaction = function() {
            TransactionService.save(self.newTransaction, function() {
                self.newTransaction = {};
                self.todaysTransApi.reload();
                self.summaryApi.reload();
            });
        };

    }]);
