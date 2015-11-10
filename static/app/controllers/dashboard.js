angular.module('moolah')
    .controller('DashboardController', [function() {
        var self = this;

        self.newTransaction = {};
        self.summaryApi = {};
        self.todaysTransApi = {};
        self.funMoneyApi = {};

        self.goGoGadgetReloadEverything = function() {
            self.todaysTransApi.reload();
            self.summaryApi.reload();
        };

        self.reloadFunMoney = function() {
            self.funMoneyApi.reload();
            self.summaryApi.reload();
        };

    }]);
