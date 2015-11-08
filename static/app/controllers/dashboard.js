angular.module('moolah')
    .controller('DashboardController', ['TransactionService', function(TransactionService) {
        var self = this,

            refreshTransactions = function() {
                self.transactions = TransactionService.query({
                    date: moment()
                });
            };


        refreshTransactions();
        self.newTransaction = {};
        self.summaryApi = {};

        self.addTransaction = function() {
            TransactionService.save(self.newTransaction, function() {
                self.newTransaction = {};
                refreshTransactions();
                self.summaryApi.reload();
            });
        };

    }]);
