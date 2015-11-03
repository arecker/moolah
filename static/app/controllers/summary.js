/*globals angular */
angular.module('moolah')

    .controller('SummaryController', function() {
        var self = this;

        self.click = function() {
            alert('clicked');
        };
    });
