/**
* WorkerProfileController
* @namespace crowdsource.forum.category.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.forum.category.controllers')
    .controller('CategoryController', CategoryController);


  angular
    .module('crowdsource.forum.category.controllers')
    .controller('AddCategoryController', AddCategoryController);

  CategoryController.$inject = ['$location', '$scope', 'Authentication', 'Category', '$mdDialog'];
  AddCategoryController.$inject = ['$location', '$scope', 'Authentication', 'Category', '$mdDialog'];

  /**
  * @namespace CategoryController
  */
  function CategoryController($location, $scope, Authentication, Category, $mdDialog) {
    var self = this;
		var userAccount = Authentication.getAuthenticatedAccount();
		if (!userAccount) {
			$location.path('/login');
			return;
		}
		self.categories=[];
    Category.getCategories().then(function (categoriesData) {
      self.categories = categoriesData.data;
      console.log(self.categories);
    });

    self.add = function(ev) {
      console.log("clcked on add");
    $mdDialog.show({
      controller: AddCategoryController,
      templateUrl: '/static/templates/forum/newCategory.html',
      // parent: angular.element(document.body),
      targetEvent: ev,
      clickOutsideToClose:true
    })
    .then(function(answer) {
      console.log('You said the information was "' + answer + '".');
    }, function() {
      console.log('You cancelled the dialog.');
    });
  };



  }

  function AddCategoryController($location, $scope, Authentication, Category,   $mdDialog){
    $scope.hide = function() {
      $mdDialog.hide();
    };
    $scope.cancel = function() {
      $mdDialog.cancel();
    };
    $scope.answer = function(answer) {
      $mdDialog.hide(answer);
    };
  }
})();
