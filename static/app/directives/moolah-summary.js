angular.module('moolah')

    .controller('moolahSummaryController', ['ReportService', function(ReportService) {
        var self = this;

        self.api = self.api || {};
        self.summary = {};
        self.api.reload = function() {
            ReportService.summary().success(function(d) {
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
