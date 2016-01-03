/// @file controllers.js
/// @brief AngularJS controllers

angular.module('NFZQVControllers', [])
    .controller('statusController', [ '$scope', '$http','$interval','$timeout', function($scope, $http,$interval,$timeout) {
        var states = ['ready', 'working'];
        var actualState = 0;
        $scope.now = "ok";
        this.minisemaphore = 0;
        this.semDOWN = function() {
            //$timeout(function() {
            $scope.status.minisemaphore++;
            if($scope.status.minisemaphore==1) $scope.status.state.now = states[1];
            //}, 0);
        };

            this.semUP = function() {
                $timeout(function() {
                    $scope.status.minisemaphore--;
                    if($scope.status.minisemaphore==0) $scope.status.state.now = states[0];
                }, 0);
            };
        this.state = {
                'provider' : 0,
                'providersection' : 0,
                'provision' : 0,
                'record': 0,
                'now' : 'ready'
        };



        var refresh = function() {
            get_count('provider');
            get_count('providersection');
            get_count('provision');
            get_count('record');
        };
        $interval(refresh, 30000);

        var get_count = function(what) {
            $scope.status.semDOWN();

            $http.get('/api/' + what + '/?format=json').success(function(data) {
                    $timeout(function(){$scope.status.state[what] = parseInt(data['count']);$scope.status.semUP();}, 0);
    }).error(function(rejection) {
        console.log(rejection);
        window.alert(what + 'failed');
    });

}; // controler end


    }])
.controller('commandController', [ '$scope', '$http','$interval','$timeout','filterFilter', function($scope, $http,$interval,$timeout,$filterFilter) {
    $scope.deps = [
        { name: '01',    selected: false },
        { name: '02',   selected: false },
        { name: '03',     selected: false },
        { name: '05', selected: false },
        { name: '06', selected: false },
        { name: '07', selected: false },
        { name: '08', selected: false },
        { name: '09', selected: false },
        { name: '10', selected: false },
        { name: '11', selected: false },
        { name: '12', selected: false },
        { name: '13', selected: false },
        { name: '14', selected: false },
        { name: '15', selected: false },
        { name: '16', selected: false },
];

    $scope.selected = [];

    $scope.selectedDeps = function selectedDeps() {
    return filterFilter($scope.deps, { selected: true })
  };

  $scope.$watch('deps|filter:{selected:true}', function (nv) {
  $scope.selected = nv.map(function (dep) {
    return dep.name;
  });
}, true);

$scope.block = false;

$scope.semUP = function() {
    $timeout(function(){
        $scope.state = "Waiting...";
        block = true;
    }, 0);
};
$scope.semDOWN = function() {
    $timeout(function(){
        $scope.state = "Ready!";
        block = false;
    }, 0);
};
$scope.flush = function() {
    if($scope.block)
    {
        window.alert("You can't - another request is in process.");
        return;
    }
    $http.get('/api/flush/').success(function(data) {
        $scope.semDOWN;
        console.log(data);
    }).error(function(reject) {});
}
$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
$scope.update = function() {
    if($scope.block)
    {
        window.alert("You can't - another request is in process.");
        return;
    }

    $http.post('/api/update/', {'departments':$scope.selected}).success(function(data) {
        $scope.semDOWN;
        console.log(data);
    }).error(function(reject) {console.log(reject);});
}

}]).controller();
