/**
* CommentController
* @namespace crowdsource.forum.comment.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.forum.comment.controllers')
    .controller('CommentController', CommentController);

  CommentController.$inject = ['$location', '$scope', 'Authentication', 'Comment', 'Topic', 'Category', '$routeParams', '$mdToast'];

  /**
  * @namespace CommentController
  */
	function CommentController($location, $scope, Authentication, Comment, Topic, Category, $routeParams, $mdToast) {
		var userAccount = Authentication.getAuthenticatedAccount();
		if (!userAccount) {
			$location.path('/login');
			return;
		}

    var self = this;
		self.topic={};
		Topic.getTopic($routeParams.param).then(function(topicData){
			self.topic=topicData[0];
      Category.getCategory(self.topic.category).then(function (CategoryData){
        self.topic.category = CategoryData[0];
        if(self.topic.category.parent){
          Category.getCategory(self.topic.category.parent).then(function (CategoryData){
            self.topic.category.parent = CategoryData[0];
          });
        }

      });
      Comment.getComments($routeParams.param).then(function (commentsData) {
  			self.topic.comments = commentsData[0];
  		});
		});






    self.newcomment = {};
		self.addComment = function(){
      self.newcomment.topic =  self.topic.id;
			Comment.addComment(self.newcomment).then(function(commentData){
				$mdToast.show(
						$mdToast.simple()
						.content('New comment added')
						.hideDelay(3000)
				);
				self.topic.comments.push(commentData[0]);
				self.newcomment = {
					topic: self.topic.id
				};
			});
		}


  }
})();
