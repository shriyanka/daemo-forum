/**
* Category
* @namespace crowdsource.forum.category.services
*/
(function () {
	'use strict';

	angular
	.module('crowdsource.forum.category.services')
	.factory('Category', Category);

	Category.$inject = ['$cookies', '$http', '$q', '$location', 'HttpService'];

	/**
	* @namespace Category
	* @returns {Factory}
	*/

	function Category($cookies, $http, $q, $location, HttpService) {
		var Category = {
			getCategories: getCategories,
			addCategory: addCategory
		};

		return Category;

		function getCategories() {

			var settings = {
				url: '/forum/category/rest/',
				method: 'GET'
			};
			// return HttpService.doRequest(settings);
			return $http(settings);
		}

		function addCategory(category) {

			var settings = {
				url: '/forum/Category/REST/',
				method: 'POST',
				data: {
					parent : category.parent,
					title : category.title,
					description : category.description
				}
			};
			return HttpService.doRequest(settings);
		}
	}

})();
