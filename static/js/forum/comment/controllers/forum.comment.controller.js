/**
* CommentController
* @namespace crowdsource.forum.comment.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.forum.comment.controllers')
    .controller('CommentController', CommentController);

  CommentController.$inject = ['$location', '$scope', 'Authentication', 'Comment'];

  /**
  * @namespace commentController
  */
  function CommentController($location, $scope, Authentication, Comment) {
    var self = this;
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


  }
})();
