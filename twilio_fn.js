exports.handler = function(context, event, callback) {
  var paste = require('better-pastebin');
  paste.setDevKey(context.PASTEBIN_API_KEY);
  paste.login(
    context.PASTEBIN_USERNAME,
    context.PASTEBIN_PASSWORD,
    function(success, data) {
      if(!success) {
        console.log('Login Failed (' + data + ')');
        return false;
      }

      paste.create({
        contents: event.body,
        privacy: '2'
      },  function(success, data) {
        if(!success) {
          console.log('Create Failed (' + data + ')');
        } else {
          console.log('Paste created (' + data + ')');
        }
      });
  });

  callback();
};
