angular.module('moolah')

    .controller('rateBreakdownReportController', ['ReportService', function(ReportService) {
        var self = this;

        self.cardTitle = 'Rate breakdown';

        self.options = {
            pointDot : false,
            pointHitDetectionRadius: 0,
            scaleShowVerticalLines: false,
            scaleFontSize: 0,
            tooltipTemplate: function(obj) {
                var label = '{} days ago'.format(obj.label),
                    value;

                if (obj.value < 0) {
                    value = '-${}'.format(obj.value);
                } else {
                    value = '${}'.format(obj.value);
                }

                return '{} : {}'.format(label, value);
            }
        };

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
