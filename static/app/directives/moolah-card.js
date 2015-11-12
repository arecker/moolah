angular.module('moolah')

    .controller('moolahCardController', [function() {
        var self = this;
        self.showAdd = true;

        self.formToggleClick = function() {
            if (self.formToggle) {
                self.formToggle();
            }
            self.showAdd = !self.showAdd;
        };
    }])

    .directive('moolahCard', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            templateUrl: toStatic('app/directives/moolah-card.html'),
            transclude: true,
            controller: 'moolahCardController',
            controllerAs: 'cardCtrl',
            bindToController: true,
            scope: {
                cardTitle: '=?',
                formToggle: '=?'
            }
        };
    }]);
