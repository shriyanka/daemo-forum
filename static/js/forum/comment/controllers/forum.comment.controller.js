/**
* CommentController
* @namespace crowdsource.forum.comment.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.forum.comment.controllers')
    .controller('CommentController', CommentController);

  CommentController.$inject = ['$location', '$scope', 'Authentication', 'Comment','$routeParams'];

  /**
  * @namespace commentController
  */
  function CommentController($location, $scope, Authentication, Comment, $routeParams) {
    var self = this;
		self.topic_id = $routeParams.param;
		var userAccount = Authentication.getAuthenticatedAccount();
		if (!userAccount) {
			$location.path('/login');
			return;
		}
		self.comments=[];
    Comment.getAllComments().then(function (commentsData) {
      self.comments = commentsData.data;
      console.log(self.comments);
    });

		// Comment.getComments(self.topic_id).then(function (commentsData) {
		// 	self.comments = commentsData.data;
		// 	console.log(self.comments);
		// });


  }
})();
