angular.module('moolah')
    .controller('TodayController', ['TransactionService', 'SummaryService', function(TransactionService, SummaryService) {
        var self = this,

            refreshTransactions = function() {
                self.transactions = TransactionService.query({
                    date: moment()
                });
            },

            refreshSummary = function() {
                SummaryService.get().success(function(d) {
                    self.summary = d;
                });
            };


        refreshTransactions();
        refreshSummary();
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
