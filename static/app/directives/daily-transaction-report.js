angular.module('moolah')

    .controller('dailyTransactionreportController', ['ReportService', function(ReportService) {
        var self = this;

        self.cardTitle = 'This Week';

        ReportService.dailyTransactionReport().success(function(d) {
            self.data = d.data;
            self.labels = d.labels;
            self.series = d.series;
        });
    }])

    .directive('dailyTransactionReport', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'dailyTransactionreportController',
            controllerAs: 'reportCtrl',
            templateUrl: toStatic('app/directives/daily-transaction-report.html'),
            bindToController: true,
            scope: {}
        };
    }]);
