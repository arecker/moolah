/*globals angular */
angular.module('moolah')
    .controller('TodayController', function() {
        var self = this;

        self.clicky = function() {
            alert('clicked the today button');
        };
    });
