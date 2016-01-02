/// @file controllers.js
/// @brief AngularJS controllers

angular.module('NFZQVControllers', [])
    .controller('statusController', [ '$scope', '$http', function($scope, $http) {
        var states = ['ready', 'working'];
        var actualState = 0;
        $scope.now = "ok";

        this.state = {
                'provider' : 0,
                'providersection' : 0,
                'provision' : 0,
                'record': 0,
                'now' : 'ready'
        };


        this.refresh = function() {

            this.toggleStatus();

            this.state.provider = get_count('provider');
            this.state.providersection = get_count('providersection');
            this.state.provision = get_count('provision');
            this.state.record = get_count('record');

            window.alert(get_count('record'));

            this.toggleStatus();
        };


        var get_count = function(what) {
            stateptr = this.state;

            $http.get('/api/' + what + '/?format=json').success(function(data) {
                window.alert(what + ' finished' + stateptr);
                $scope[what] = data['count'];
            }).error(function() {window.alert(what + 'failed');});

        };

        $scope.now = states[0];
        this.toggleStatus = function() {
            actualState = 1 - actualState;
            this.state.now = states[actualState];
        };

    }]);
