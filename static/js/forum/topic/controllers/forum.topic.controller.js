/**
* WorkerProfileController
* @namespace crowdsource.forum.topic.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.forum.topic.controllers')
    .controller('TopicController', TopicController);

  TopicController.$inject = ['$location', '$scope', 'Authentication', 'Topic'];

  /**
  * @namespace topicController
  */
  function TopicController($location, $scope, Authentication, Topic) {
    var self = this;
		var userAccount = Authentication.getAuthenticatedAccount();
		if (!userAccount) {
			$location.path('/login');
			return;
		}
		self.topics=[];
    Topic.getTopics().then(function (topicsData) {
      self.topics = topicsData.data;
      console.log(self.topics);
    });


  }
})();
