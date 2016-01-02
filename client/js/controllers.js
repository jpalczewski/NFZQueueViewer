/// @file controllers.js
/// @brief AngularJS controllers

angular.module('NFZQVControllers', [])
    .controller('statusController', [ '$scope', '$http','$interval','$timeout', function($scope, $http,$interval,$timeout) {
        var states = ['ready', 'working'];
        var actualState = 0;
        $scope.now = "ok";
        this.minisemaphore = 0;

        this.state = {
                'provider' : 0,
                'providersection' : 0,
                'provision' : 0,
                'record': 0,
                'now' : 'ready'
        };



        this.refresh = function() {

             get_count('provider');
            get_count('providersection');
            get_count('provision');
            get_count('record');


        };


        var get_count = function(what) {
            $scope.status.semDOWN();

            $http.get('/api/' + what + '/?format=json').success(function(data) {
                    $timeout(function(){$scope.status.state[what] = parseInt(data['count']);$scope.status.semUP();}, 0);
    }).error(function() {window.alert(what + 'failed');});

        };

        $interval(function() {$scope.status.refresh();}, 5000);

        this.semDOWN = function() {
            //$timeout(function() {
                this.minisemaphore++;
                if(this.minisemaphore==1) this.state.now = states[1];
            //}, 0);
        }

        this.semUP = function() {
            //$timeout(function() {
                this.minisemaphore--;
                if(this.minisemaphore==0) this.state.now = states[0];
            //}, 0);
        }

    }]);
