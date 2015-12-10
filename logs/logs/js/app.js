angular

.module('app', ['chart.js','ui.bootstrap'])


.controller('MainController',MainController)

.controller('PieController',PieController)

.controller('BarController',BarController)

.service('Charts',Charts);


function Charts(){
	this.user = true;
	this.mime = true;
	this.profiles = true;
	this.Status = true;
	this.filter = true;

	this.setUser = function(data) {
		this.user = data;
	}
	this.setMime = function(data) {
		this.mime = data;
	}
	this.setProfile = function(data) {
		this.profiles = data;
	}
	this.setStatus = function(data) {
		this.Status = data;
	}
	this.setFilter = function(data) {
		this.filter = data;
	}


}

function BarController($scope,Charts,$http){


	//TO PARSE JSON FILES

	$scope.labels = [];
	$scope.data = [];
	$scope.labels1 = [];
	$scope.data1 = [];
	$scope.labels2 = [];
	$scope.data2 = [];
	$scope.labels3 = [];
	$scope.data3 = [];
	$scope.labels4 = [];
	$scope.data4 = [];
	$scope.test = [];

	$scope.series = ["2010","2011","2012"];


	 $http.get("../logs/js/userdata.json")
	 .success(function(data){
	 	for (response in data.xdata) {
	 		$scope.labels.push(data.xdata[response]);
	 	}
	 	for (response in data.ydata) {
	 		$scope.test.push(data.ydata[response]);
	 	}

	 	//TO USE MULTIDIMENSTIONAL ARRAY WE NEED TO PUSH OUR DATA FIRST ON BLANK ARRAY..THN PUSH THAT BLANK ARRAY ON DATA

	 	$scope.data.push($scope.test);
	 	$scope.data.push($scope.test);
	 	$scope.data.push($scope.test);
	 	$scope.test = [];

	 	for (response in data.mimedatax) {
	 		$scope.labels1.push(data.mimedatax[response]);
	 	}
	 	for (response in data.mimedatay) {
	 		$scope.test.push(data.mimedatay[response]);
	 	}
	 	$scope.data1.push($scope.test);
	 	$scope.data1.push($scope.test);
	 	$scope.data1.push($scope.test);
	 	$scope.test = [];

	 	for (response in data.profiledatax) {
	 		$scope.labels2.push(data.profiledatax[response]);
	 	}
	 	for (response in data.profiledatay) {
	 		$scope.test.push(data.profiledatay[response]);
	 	}
	 	$scope.data2.push($scope.test);
	 	$scope.data2.push($scope.test);
	 	$scope.data2.push($scope.test);
	 	$scope.test = [];

	 	for (response in data.profiledatax) {
	 		$scope.labels3.push(data.statusdatax[response]);
	 	}
	 	for (response in data.profiledatay) {
	 		$scope.test.push(data.statusdatay[response]);
	 	}
	 	$scope.data3.push($scope.test);
	 	$scope.data3.push($scope.test);
	 	$scope.data3.push($scope.test);
	 	$scope.test = [];

	 	for (response in data.filterdatax) {
	 		$scope.labels4.push(data.filterdatax[response]);
	 	}
	 	for (response in data.filterdatay) {
	 		$scope.test.push(data.filterdatay[response]);
	 	}
	 	$scope.data4.push($scope.test);
	 	$scope.data4.push($scope.test);
	 	$scope.data4.push($scope.test);
	 	$scope.test = [];

	 }).error(function(error){

	 });

	 //TO SHOW-HIDE VALUES OF CHARTS

     $scope.$watch(function(){return Charts.user},function (newVal,oldVal,scope){
     	$scope.user = newVal;
     })
      $scope.$watch(function(){return Charts.mime},function (newVal,oldVal,scope){
     	$scope.mime = newVal;
     })
      $scope.$watch(function(){return Charts.profiles},function (newVal,oldVal,scope){
     	$scope.profiles = newVal;
     })
      $scope.$watch(function(){return Charts.Status},function (newVal,oldVal,scope){
     	$scope.Status = newVal;
     })
      $scope.$watch(function(){return Charts.filter},function (newVal,oldVal,scope){
     	$scope.filter = newVal;
     })



}

function PieController($scope,Charts,$http) {

	//TO PARSE JSON FILES

	$scope.labels = [];
	$scope.data = [];
	$scope.labels1 = [];
	$scope.data1 = [];
	$scope.labels2 = [];
	$scope.data2 = [];
	$scope.labels3 = [];
	$scope.data3 = [];
	$scope.labels4 = [];
	$scope.data4 = [];


	 $http.get("../logs/js/userdata.json")
	 .success(function(data){
	 	for (response in data.xdata) {
	 		$scope.labels.push(data.xdata[response]);
	 	}
	 	for (response in data.ydata) {
	 		$scope.data.push(data.ydata[response]);
	 	}

	 	for (response in data.mimedatax) {
	 		$scope.labels1.push(data.mimedatax[response]);
	 	}
	 	for (response in data.mimedatay) {
	 		$scope.data1.push(data.mimedatay[response]);
	 	}

	 	for (response in data.profiledatax) {
	 		$scope.labels2.push(data.profiledatax[response]);
	 	}
	 	for (response in data.profiledatay) {
	 		$scope.data2.push(data.profiledatay[response]);
	 	}

	 	for (response in data.profiledatax) {
	 		$scope.labels3.push(data.statusdatax[response]);
	 	}
	 	for (response in data.profiledatay) {
	 		$scope.data3.push(data.statusdatay[response]);
	 	}
	 	for (response in data.filterdatax) {
	 		$scope.labels4.push(data.filterdatax[response]);
	 	}
	 	for (response in data.filterdatay) {
	 		$scope.data4.push(data.filterdatay[response]);
	 	}


	 }).error(function(error){

	 });


	 //TO SHOW-HIDE VALUES OF CHARTS

     $scope.$watch(function(){return Charts.user},function (newVal,oldVal,scope){
     	$scope.user = newVal;
     })
      $scope.$watch(function(){return Charts.mime},function (newVal,oldVal,scope){
     	$scope.mime = newVal;
     })
      $scope.$watch(function(){return Charts.profiles},function (newVal,oldVal,scope){
     	$scope.profiles = newVal;
     })
      $scope.$watch(function(){return Charts.Status},function (newVal,oldVal,scope){
     	$scope.Status = newVal;
     })
      $scope.$watch(function(){return Charts.filter},function (newVal,oldVal,scope){
     	$scope.filter = newVal;
     })
}



function MainController($scope,Charts,$http) {


	//TO PARSE JSON FILES

	$scope.labels = [];
	$scope.data = [];
	$scope.labels1 = [];
	$scope.data1 = [];
	$scope.labels2 = [];
	$scope.data2 = [];
	$scope.labels3 = [];
	$scope.data3 = [];
	$scope.labels4 = [];
	$scope.data4 = [];
	$scope.test = [];

	$scope.series = ["2010","2011","2012"];


	 $http.get("/home/pallav/log filtering 3.0A/js")
	 .success(function(data){
	 	for (response in data.xdata) {
	 		$scope.labels.push(data.xdata[response]);
	 	}
	 	for (response in data.ydata) {
	 		$scope.test.push(data.ydata[response]);
	 	}

	 	//TO USE MULTIDIMENSTIONAL ARRAY WE NEED TO PUSH OUR DATA FIRST ON BLANK ARRAY..THN PUSH THAT BLANK ARRAY ON DATA

	 	$scope.data.push($scope.test);
	 	$scope.data.push($scope.test);
	 	$scope.data.push($scope.test);
	 	$scope.test = [];

	 	for (response in data.mimedatax) {
	 		$scope.labels1.push(data.mimedatax[response]);
	 	}
	 	for (response in data.mimedatay) {
	 		$scope.test.push(data.mimedatay[response]);
	 	}
	 	$scope.data1.push($scope.test);
	 	$scope.data1.push($scope.test);
	 	$scope.data1.push($scope.test);
	 	$scope.test = [];

	 	for (response in data.profiledatax) {
	 		$scope.labels2.push(data.profiledatax[response]);
	 	}
	 	for (response in data.profiledatay) {
	 		$scope.test.push(data.profiledatay[response]);
	 	}
	 	$scope.data2.push($scope.test);
	 	$scope.data2.push($scope.test);
	 	$scope.data2.push($scope.test);
	 	$scope.test = [];

	 	for (response in data.profiledatax) {
	 		$scope.labels3.push(data.statusdatax[response]);
	 	}
	 	for (response in data.profiledatay) {
	 		$scope.test.push(data.statusdatay[response]);
	 	}
	 	$scope.data3.push($scope.test);
	 	$scope.data3.push($scope.test);
	 	$scope.data3.push($scope.test);
	 	$scope.test = [];

	 	for (response in data.filterdatax) {
	 		$scope.labels4.push(data.filterdatax[response]);
	 	}
	 	for (response in data.filterdatay) {
	 		$scope.test.push(data.filterdatay[response]);
	 	}
	 	$scope.data4.push($scope.test);
	 	$scope.data4.push($scope.test);
	 	$scope.data4.push($scope.test);
	 	$scope.test = [];

	 }).error(function(error){

	 });

	 //TO SHOW-HIDE VALUES OF CHARTS

     $scope.$watch(function(){return Charts.user},function (newVal,oldVal,scope){
     	$scope.user = newVal;
     })
      $scope.$watch(function(){return Charts.mime},function (newVal,oldVal,scope){
     	$scope.mime = newVal;
     })
      $scope.$watch(function(){return Charts.profiles},function (newVal,oldVal,scope){
     	$scope.profiles = newVal;
     })
      $scope.$watch(function(){return Charts.Status},function (newVal,oldVal,scope){
     	$scope.Status = newVal;
     })
      $scope.$watch(function(){return Charts.filter},function (newVal,oldVal,scope){
     	$scope.filter = newVal;
     })

	
	//TO SET ALL CHECKBOX CHECKED

	$scope.user = true;
	$scope.mime = true;
	$scope.profiles = true;
	$scope.Status = true;
	$scope.filter = true;

	//STATIC LINE CHARTS VALUES

	

	$scope.$watch('user',function (newVal,oldVal,scope){
		Charts.setUser(newVal);
	});
	$scope.$watch('mime',function (newVal,oldVal,scope){
		Charts.setMime(newVal);
	});
	$scope.$watch('profiles',function (newVal,oldVal,scope){
		Charts.setProfile(newVal);
	});
	$scope.$watch('Status',function (newVal,oldVal,scope){
		Charts.setStatus(newVal);
	});
	$scope.$watch('filter',function (newVal,oldVal,scope){
		Charts.setFilter(newVal);
	});

}