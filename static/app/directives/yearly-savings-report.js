angular.module('moolah')

    .controller('yearlySavingsReportController', ['ReportService', function(ReportService) {
        var self = this;

        self.cardTitle = 'Yearly savings over time';

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

        ReportService.yearlySavingDaily().success(function(d) {
            self.data = d.data;
            self.labels = d.labels;
            self.series = d.series;
        });
    }])

    .directive('yearlySavingsReport', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'yearlySavingsReportController',
            controllerAs: 'reportCtrl',
            templateUrl: toStatic('app/directives/yearly-savings-report.html'),
            bindToController: true,
            scope: {}
        };
    }]);
