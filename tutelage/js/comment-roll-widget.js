/*
Dependencies:
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
*/

function CommentRoll(pDivID)
{
  // utility functions
  var appendDiv = function(pContainer, pClass) {
    pContainer.append('<div class="' + pClass + '"></div> ');
    return pContainer.find('.' + pClass);
  }
  var appendButton = function(pContainer, pClass, pText) {
    pContainer.append('<button type="button" class="' + pClass + '">' + pText + '</button>');
    return pContainer.find('.' + pClass);
  }

  // get containing div
  var container = $("#" + pDivID);

  // create widget
  var comment_roll_widget	= appendDiv(container,			"comment_roll_widget");
    var comment_display		= appendDiv(comment_roll_widget,	"comment_display");
    var comment_control		= appendDiv(comment_roll_widget,	"comment_control");
        var comment_next_button	= appendButton(comment_control,		"comment_next_button",	"Next");

  // prepare comment controller
  var result      = {};
  result._pause   = false;
  result._display = comment_display;

  result.addComment	= function(pUser, pDate, pComment) {
    var commentHTML =
      '<ul>\n' +
      '  <li class="user"><a href="http://m.youtube.com/profile?user=' + pUser + '&feature=all_comments">' + pUser + '</a></li>\n' +
      '  <li class="date">' + pDate + '</li>\n' +
      '  <li class="comment">' + pComment + '</li>\n' +
      '</ul>\n';
    this._display.prepend(commentHTML);
  }
  result.nextComment	= function() {
    var nextComment = result._display.find('ul:last-child');
    result._display.prepend(nextComment);
  }
  comment_next_button.click(result.nextComment);

 // return temp-time controller
  return result;
}

/*
var CommentRollTick;

  // clear values and start timers
  result.tempTimeClear();
  result._tick = function() {
    if (!result._timerPauseAll) {
      this._timerMain.tick();
      this._timerSubA.tick();
      this._timerSubB.tick();
      this._timerSubC.tick();
      this._timerSubD.tick();
    }
  }
  TempTimeTick = function() {
    result._tick();
    setTimeout("TempTimeTick()", 1000) 
  }
  TempTimeTick();

*/
