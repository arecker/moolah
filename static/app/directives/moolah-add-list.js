angular.module('moolah')

    .controller('moolahAddListController', [function() {
        var self = this,

            refreshTotal = function() {
                if (self.collection.length === 0) return;
                self.total = self.collection.map(function(o) {
                    return o.amount;
                }).reduce(function(p, c) {
                    return Number(p) + Number(c);
                });

                self.totalIsPositive = self.total > 0;
            };

        self.api = self.api || {};
        self.afterSave = self.afterSave || angular.noop;
        self.getQueryFilter = self.getQueryFilter || angular.noop;

        self.showForm = false;
        self.newObj = {};

        self.formToggle = function() {
            self.showForm = !self.showForm;
        };

        self.submit = function() {
            self.resource.save(self.newObj, function() {
                self.afterSave();
                self.newObj = {};
                self.api.reload();
            });
        };

        self.api.reload = function() {
            self.resource.query(self.getQueryFilter())
                .$promise.then(function(d) {
                    self.collection = d;
                    refreshTotal();
                });
        };

        self.api.reload();
    }])

    .directive('moolahAddList', ['toStatic', function(toStatic) {
        return {
            restrict: 'E',
            controller: 'moolahAddListController',
            controllerAs: 'addListCtrl',
            templateUrl: toStatic('app/directives/moolah-add-list.html'),
            bindToController: true,
            scope: {
                api: '=?',
                resource: '=',
                getQueryFilter: '=?',
                afterSave: '=?',
                cardTitle: '=?'
            }
        };
    }]);
