/**
* TopicController
* @namespace crowdsource.forum.topic.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.forum.topic.controllers')
    .controller('TopicController', TopicController);

  TopicController.$inject = ['$location', '$scope', 'Authentication', 'Topic', '$routeParams'];

  /**
  * @namespace TopicController
  */
  function TopicController($location, $scope, Authentication, Topic, $routeParams) {
    var self = this;
		self.category_id = $routeParams.param;
		console.log(self.category_id);
		var userAccount = Authentication.getAuthenticatedAccount();
		if (!userAccount) {
			$location.path('/login');
			return;
		}
		self.topics=[];
    // Topic.getTopics(self.category_id).then(function (topicsData) {
    //   self.topics = topicsData.data;
    //   console.log(self.topics);
    // });

		Topic.getAllTopics().then(function (topicsData) {
      self.topics = topicsData.data;
      console.log(self.topics);
    });

  }
})();
