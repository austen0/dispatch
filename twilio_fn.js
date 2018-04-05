exports.handler = function(context, event, callback) {
  var error_log = '';
  var success_log = '';

  var jsdom = require('jsdom');
  const { JSDOM } = jsdom;
  const { window } = new JSDOM('<html></html>');
  var $ = require('jquery')(window);

  $.ajax({
    url: context.JSONBIN_URL,
    type: 'PUT',
    contentType: 'application/json',
    headers: {
      'secret-key': context.JSONBIN_KEY
    },
    data: JSON.stringify({ message: "words" }),
    success: (data) => {
      console.log(data);
      success_log = data;
    },
    error: (err) => {
      console.log(err.responseJSON);
      error_log = err.responseJSON;
    }
  });

  callback(error_log, success_log);
};
