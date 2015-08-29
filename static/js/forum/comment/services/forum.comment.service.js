/**
* Category
* @namespace crowdsource.forum.comment.services
*/
(function () {
	'use strict';

	angular
	.module('crowdsource.forum.comment.services')
	.factory('Comment', Comment);

	Comment.$inject = ['$cookies', '$http', '$q', '$location', 'HttpService'];

	/**
	* @namespace Comment
	* @returns {Factory}
	*/

	function Comment($cookies, $http, $q, $location, HttpService) {
		var Comment = {
			getComments: getComments,
			getAllComments: getAllComments,
			addComment: addComment
		};

		return Comment;

		function getComments(t_id) {

			var settings = {
				url: '/forum/topic/rest/'+t_id+'/comments/',
				method: 'GET'
			};
			// return HttpService.doRequest(settings);
			return $http(settings);
		}

		function getAllComments() {

			var settings = {
				url: '/forum/comment/rest/',
				method: 'GET'
			};
			// return HttpService.doRequest(settings);
			return $http(settings);
		}

		function addComment(comment) {

			var settings = {
				url: '/forum/comment/rest/',
				method: 'POST',
				data: {
					topic: comment.topic,
					comment: comment.comment,
					comment_html: comment.comment_html
				}
			};
			return HttpService.doRequest(settings);
		}
	}

})();
