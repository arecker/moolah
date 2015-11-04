/*globals angular */
angular.module('moolah')
    .controller('TodayController', function(TransactionService) {
        var self = this;
        self.transactions = TransactionService.query({
            date: moment(Date.now())
        });
    });
