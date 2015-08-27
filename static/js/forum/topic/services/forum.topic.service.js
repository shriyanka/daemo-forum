/**
* topic
* @namespace crowdsource.forum.topic.services
*/
(function () {
	'use strict';

	angular
	.module('crowdsource.forum.topic.services')
	.factory('topic', topic);

	topic.$inject = ['$cookies', '$http', '$q', '$location', 'HttpService'];

	/**
	* @namespace topic
	* @returns {Factory}
	*/

	function topic($cookies, $http, $q, $location, HttpService) {
		var topic = {
			getCategories: getCategories,
			addtopic: addtopic
		};

		return topic;

		function getCategories() {

			var settings = {
				url: '/forum/topic/rest/',
				method: 'GET'
			};
			// return HttpService.doRequest(settings);
			return $http(settings);
		}

		function addtopic(topic) {

			var settings = {
				url: '/forum/topic/REST/',
				method: 'POST',
				data: {
					category : topic.category,
					title : topic.title
				}
			};
			return HttpService.doRequest(settings);
		}
	}

})();
