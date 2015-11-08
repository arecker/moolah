angular.module('moolah')

    .controller('moolahSummaryController', ['$scope', 'SummaryService', function($scope, SummaryService) {
        var self = this,
            reloadSummary = function() {
                SummaryService.get().success(function(d) {
                    self.summary = d;
                });
            };

        self.summary = {};
        reloadSummary();

        $scope.api.reload = reloadSummary;
    }])

    .directive('moolahSummary', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'moolahSummaryController',
            controllerAs: 'summaryCtrl',
            templateUrl: toStatic('app/directives/moolah-summary.html'),
            scope: {
                api: '=?'
            }
        };
    }]);
