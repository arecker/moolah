angular.module('moolah')

    .controller('moolahFunMoneyController', ['PurchaseService', function(PurchaseService) {
        var self = this;

        self.afterSave = self.afterSave || angular.noop;
        self.api = self.api || {};

        self.newPurchase = {};

        self.formToggle = function() {
            self.showForm = !self.showForm;
        };

        self.submit = function() {
            PurchaseService.save(self.newPurchase, function() {
                self.afterSave();
                self.newPurchase = {};
            });
        };

        self.api.reload = function() {
            PurchaseService.query(function(data){
                self.purchases = data;
            });
        };

        self.api.reload();
    }])

    .directive('moolahFunMoney', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'moolahFunMoneyController',
            controllerAs: 'funMoneyCtrl',
            templateUrl: toStatic('app/directives/moolah-fun-money.html'),
            bindToController: true,
            scope: {
                api: '=?',
                afterSave: '=?'
            }
        };
    }]);
