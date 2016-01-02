/// @file services.js
/// @brief AngularJS services, AJAX communication with the server

angular.module('NFZQVServices', [])
    .service('djconn', //current information from zsm server
             function($http) {
                 this.baseURL = client_server_prefix; //the prefix defined in version.js

                 this.getProviders = function(page, callback) {
                     return $http.get(this.baseURL + '/provider/?format=json&page=' + page).success(callback);
				 };

                 this.getProviderSections = function(page, callback) {
                     return $http.get(this.baseURL + '/providersection/?format=json&page=' + page).success(callback);
                  };

                  this.getProvisions = function(page, callback) {
                    return $http.get(this.baseURL + '/provision/?format=json&page=' + page).success(callback);
                  };

                  this.getRecords = function(page, callback) {
                    return $http.get(this.baseURL + '/record/?format=json&page=' + page).success(callback);
                  };

			 })
	.service('srvCommands', //commands
			 function($http) {
                 this.baseURL = client_server_prefix + '/ajax/calcpy/'; //the prefix is defined in version.js

                 this.getCppCommands = function(callback) {
                     return $http.get(this.baseURL + 'getCommands').success(callback);
                 };
				 this.startCommand = function(callback) {
					 return $http.get(this.baseURL + 'startCommand').success(callback);
				 };
             });
