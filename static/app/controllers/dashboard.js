angular.module('moolah')
    .controller('DashboardController', [function() {
        var self = this;

        self.newTransaction = {};
        self.summaryApi = {};
        self.todaysTransApi = {};

        self.goGoGadgetReloadEverything = function() {
            self.todaysTransApi.reload();
            self.summaryApi.reload();
        };

    }]);
