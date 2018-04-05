exports.handler = function(context, event, callback) {
  var request = require('request');
  var log_error = ''

  request(
    {
      method: 'PUT',
      url: context.JSONBIN_URL,
      headers: {
        'content-type': 'application/json',
        'secret-key': context.JSONBIN_KEY
      },
      body: JSON.stringify({"message": "words"})
    },
    function (error, response, body) {
      log_error = error;
    }
  );

  callback(log_error, 'success');
};
