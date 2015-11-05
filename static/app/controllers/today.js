angular.module('moolah')
    .controller('TodayController', ['TransactionService', function(TransactionService) {
        var self = this;
        self.transactions = TransactionService.query({
            date: moment()
        });
    }]);
