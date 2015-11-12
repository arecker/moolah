angular.module('moolah')

    .controller('rateBreakdownReportController', ['ReportService', function(ReportService) {
        var self = this;

        self.cardTitle = 'Rate breakdown';

        ReportService.rateBreakdown().success(function(d) {
            self.data = d.data;
            self.labels = d.labels;
        });
    }])

    .directive('rateBreakdownReport', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'rateBreakdownReportController',
            controllerAs: 'reportCtrl',
            templateUrl: toStatic('app/directives/rate-breakdown-report.html'),
            bindToController: true,
            scope: {}
        };
    }]);
