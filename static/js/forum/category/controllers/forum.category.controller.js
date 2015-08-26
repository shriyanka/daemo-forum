/**
* WorkerProfileController
* @namespace crowdsource.forum.category.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.forum.category.controllers')
    .controller('CategoryController', CategoryController);

  CategoryController.$inject = ['$location', '$scope', 'Authentication', 'Category'];

  /**
  * @namespace CategoryController
  */
  function CategoryController($location, $scope, Authentication, Category) {
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


  }
})();
