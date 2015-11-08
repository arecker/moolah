angular.module('moolah')

    .controller('moolahSummaryController', ['SummaryService', function(SummaryService) {
        var self = this;

        self.summary = {};
        self.api.reload = function() {
            SummaryService.get().success(function(d) {
                self.summary = d;
            });
        };

        self.api.reload();
    }])

    .directive('moolahSummary', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'moolahSummaryController',
            controllerAs: 'summaryCtrl',
            templateUrl: toStatic('app/directives/moolah-summary.html'),
            bindToController: true,
            scope: {
                api: '=?'
            }
        };
    }]);
