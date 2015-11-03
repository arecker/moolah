angular.module('moolah')
    .factory('toStatic', function(STATIC_URL) {
        return function(i) {
            return '{}{}'.format(STATIC_URL, i);
        };
    });
