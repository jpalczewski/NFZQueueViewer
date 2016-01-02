/// @file controllers.js
/// @brief AngularJS controllers

angular.module('NFZQVControllers', [])
    .controller('statusController', [ '$scope', function($scope) {
        var states = ['tak', 'nie'];
        var actualState = 1;
        $scope.now = "ok";




        this.refresh = function() {
            var providers = 0;
            var provisions = 0;
            var providesections = 0;




        };

        $scope.now = states[0];
        this.toggleStatus = function() {
            actualState = 1 - actualState;
            $scope.now = states[1 - actualState];
        };

    }]);
