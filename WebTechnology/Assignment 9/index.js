var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope) {
	$scope.result = '';

	$scope.updateResult = function(key) {
		$scope.result = $scope.result + key;
	};

	$scope.calculate = function() {
		try {
			$scope.result = eval($scope.result);
		} catch (e) {
			$scope.result = 'Error';
		}
	};

	$scope.clear = function() {
		$scope.result = '';
	};
});