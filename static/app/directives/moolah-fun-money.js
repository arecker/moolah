angular.module('moolah')

    .controller('moolahFunMoneyController', ['PurchaseService', function(PurchaseService) {
        var self = this;
        self.api = self.api || {};
        self.resource = PurchaseService;
        self.afterSave = self.afterSave || angular.noop;
        self.cardTitle = 'Fun Money';
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
