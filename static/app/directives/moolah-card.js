angular.module('moolah')
    .directive('moolahCard', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            templateUrl: toStatic('app/directives/moolah-card.html'),
            transclude: true,
            scope: {
                cardTitle: '=?'
            }
        };
    }]);
