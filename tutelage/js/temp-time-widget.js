/*
Dependencies:
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
  <script type="text/javascript" src="http://popcornjs.org/code/dist/popcorn-complete.js"></script>

Links:
  http://jsfiddle.net/popcornjs/qQ672/
  http://popcornjs.org/popcorn-docs/players/
  http://flowplayer.org/tools/rangeinput/
*/

var TempTimeTick;
function TempTime(pDivID, pTimers)
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
  var appendDisplay = function(pContainer) {
    var result = {};
    result.display = appendDiv(pContainer,     "display");
    result.icon    = appendDiv(result.display, "icon");
    result.prompt  = appendDiv(result.display, "prompt");
    result.details = appendDiv(result.display, "details");
    return result;
  }
  var appendDisplayMultiple = function(pContainer, pQuantity) {
    var result = new Array();
    for (var i = 0; i < pQuantity; i++) {
      result[i] = {};
      result[i].display = appendDiv(pContainer,     "display_" + i);
      result[i].display.toggleClass("display");
      result[i].icon    = appendDiv(result[i].display, "icon_" + i);
      result[i].icon.toggleClass("icon", true);
      result[i].prompt  = appendDiv(result[i].display, "prompt_"  + i);
      result[i].prompt.toggleClass("prompt", true);
      result[i].details = appendDiv(result[i].display, "details_" + i);
      result[i].details.toggleClass("details", true);
    }
    return result;
  }
  var setText = function(pContainer, pText) {
    pContainer.html(pText);
  }
  var HMStoS  = function(pH, pM, pS) {
    return pS + pM * 60 + pH * 60 * 60;
  }
  var leadingZero = function(pValue, pNone) {
    if (pNone) {
      return "--";
    }
    if (pValue < 10) {
      return "0" + pValue;
    }
    return "" + pValue;
  }
  var timeDisplay = function(pS) {
    var sign;
    var d    = Math.floor((Math.abs(pS) / (60 * 60 * 24)));
    var h    = Math.floor((Math.abs(pS) / (60 * 60)) % 24);
    var m    = Math.floor((Math.abs(pS) / 60) % 60);
    var s    = Math.floor(Math.abs(pS) % 60);

    if (pS < 0) {
      sign = "over by ";
    } else {
      sign = "";
    }
    if ((60 * 60 * 24) <= Math.abs(pS)) {
      d = d + "d, ";
    } else {
      d = "";
    }
    h = leadingZero(h, Math.abs(pS) < (60 * 60));
    m = leadingZero(m, Math.abs(pS) < 60);
    s = leadingZero(s, pS == 0);
    return sign + d + h + ":" + m + ":" + s;
  }
  var BaseModel = function(pClass, pPrompt, pDetails) {
    var result = {};
    // class setter / getter
    result.class = function(pClass) {
      this._class = pClass;
      return this;
    }
    // icon setter / getter
    result.icon = function(pIcon) {
      this._icon = pIcon;
      return this;
    }
    result.getIcon = function() {
      return this._icon;
    }
    // prompt setter / getter
    result.prompt = function(pPrompt) {
      this._prompt = pPrompt;
      return this;
    }
    result.getPrompt = function() {
      return this._prompt;
    }
    // details setter / getter
    result.details = function(pDetails) {
      this._details = pDetails;
      return this;
    }
    result.getDetails = function() {
      return this._details;
    }
    // initialization
    result.init = function(pClass, pIcon, pPrompt, pDetails) {
      return this.class(pClass).icon(pIcon).prompt(pPrompt).details(pDetails);
    }
    // display
    result._display  = function(pDisplay) {
      pDisplay.display.toggleClass(this._class, true);
      setText(pDisplay.icon,    '<img src="' + this._icon + '" alt=""></img>');
      setText(pDisplay.prompt,  this._prompt);
      setText(pDisplay.details, this._details);
      return this;
    }
    result.display   = result._display;
    return result;
  }
  var TempModel = function() {
    var result      = BaseModel();
    // set temperature
    result.temperature = function(pC, pF) {
      var text = pC + "&deg; C / " + pF + "&deg; F";
      return this.details(text);
    }
    result.celsius     = function(pC) {
      var f = Math.floor(pC * (9/5) + 32);
      return this.temperature(pC, f);
    }
    result.fahrenheit  = function(pF) {
      var c = Math.floor((pF - 32) * (5/9));
      return this.temperature(c, pF);
    }
    result.clear = function() {
      return this.init("default", "./img/icon_oven.png", "Temperature", "").temperature("N/A", "N/A");
    }
    result.resetDisplay = function(pDisplay) {
      pDisplay.display.toggleClass(this._class, false);
      return this.clear().display(pDisplay);
    }
    result.clear();
    return result;
  }
  var TimeModel = function() {
    var result     = BaseModel();
    result.seconds = 0;
    result.active  = false;
    // timer control
    result.on  = function(pSeconds) {
      this.active  = true;
      this.seconds = pSeconds;
      return this;
    }
    result.off = function(pReset) {
      this.active = false;
      if (pReset) {
        this.seconds = 0;
      }
      return this;
    }
    result.start = function(pH, pM, pS)
    {
      return this.on(HMStoS(pH, pM, pS));
    }
    result.stop = function()
    {
      return this.off(true);
    }
    result.pause = function()
    {
      return this.off(false);
    }
    result.resume = function()
    {
      if (0 < this.seconds) {
        this.active = true;
      }
      return this;
    }
    result.clear = function() {
      this.init("default", "./img/icon_chicken.png", "Timer", "").stop();
    }
    result.complete = function() {
      if (this.seconds < 0) {
        this.clear();
      }
      return this;
    }
    // display
    result.displayClasses = function(pDisplay) {
      pDisplay.display.toggleClass("on",  this.active);
      pDisplay.display.toggleClass("off", !this.active);
      pDisplay.display.toggleClass("positive", 0 < this.seconds);
      pDisplay.display.toggleClass("negative", this.seconds < 0);
      pDisplay.display.toggleClass("zero",     0 == this.seconds);
      return this;
    }
    result.mainDisplay = function(pDisplay) {
      this.details(timeDisplay(this.seconds));
      this._display(pDisplay);
      return this.displayClasses(pDisplay);
    }
    result.subDisplay = function(pDisplay) {
      if (this.seconds < 0) {
        this.details("Over");
      } else {
        this.details(timeDisplay(this.seconds));
      }
      this._display(pDisplay);
      setText(pDisplay.prompt, "");
      return this.displayClasses(pDisplay);
    }
    result.display = function(pDisplay, pIsMainDisplay) {
      if (pIsMainDisplay) {
        this.mainDisplay(pDisplay);
      } else {
        this.subDisplay(pDisplay);
      }
      return this;
    }
    result.tick = function(pDisplay, pIsMainDisplay) {
      if (this.active) {
        this.seconds -= 1;
        this.display(pDisplay, pIsMainDisplay);
      }
    }
    result.clear();
    return result;
  }
  var TempTimeModel = function() {
    var result   = {};
    result.temp  = TempModel();
    result.time  = TimeModel();
    result.main  = false;
    result.tick  = function(pDisplay) {
      this.time.tick(pDisplay, this.main);
      return this;
    }
    result.display = function(pTempDisplay, pTimeDisplay) {
      if (this.main) {
        this.temp.display(pTempDisplay);
      }
      this.time.display(pTimeDisplay, this.main);
      return this;
    }
    result.reset = function() {
      this.temp.clear();
      this.time.clear();
    }
    return result;
  }

  // get containing div
  var container = $("#" + pDivID);

  // create temp-time widget
  var temp_time_widget			= appendDiv(container,		"temp_time_widget");
    var temp_widget			= appendDiv(temp_time_widget,	"temp_widget");
      var temp_display			= appendDisplay(temp_widget);
    var time_widget			= appendDiv(temp_time_widget,	"time_widget");
      var time_display			= appendDisplay(time_widget);
      var time_control			= appendDiv(time_widget,	"time_control");
        var time_pause			= appendButton(time_control,		"time_pause",		"Pause");
        var time_resume			= appendButton(time_control,		"time_resume",		"Resume");
        var time_complete		= appendButton(time_control,		"time_complete",	"Complete");
      var time_sub			= appendDiv(time_widget,	"time_sub");
        var time_sub_display		= appendDisplayMultiple(time_sub, pTimers);
      var time_sub_control		= appendDiv(time_widget,	"time_sub_control");
        var time_pause_all		= appendButton(time_sub_control,	"time_pause_all",	"Pause All");
        var time_resume_all		= appendButton(time_sub_control,	"time_resume_all",	"Resume All");
        var time_complete_all		= appendButton(time_sub_control,	"time_complete_all",	"Complete All");

  // prepare temp-time controller and timers
  var result   = {};
  result.main  = TempTimeModel();
    result.main.main = true;
  result.sub   = new Array();
  for (var i = 0; i < pTimers; i++) {
    result.sub[i] = TempTimeModel();
  }

  result.redraw = function() {
    this.main.display(temp_display, time_display);
    if (this.main.time.seconds < 1 && !this.main.time.active) {
      this.main.temp.resetDisplay(temp_display);
    }
    for (var i = 0; i < pTimers; i++) {
      result.sub[i].display(temp_display, time_sub_display[i]);
    }
    return this;
  }
  result.clear = function() {
    this.main.reset();
    for (var i = 0; i < pTimers; i++) {
      result.sub[i].reset();
    }
    return this.redraw();
  }
  result._eventMain = function(pEvent) {
    this.main.time[pEvent]();
    return this;
  }
  result._eventAll  = function(pEvent) {
    this.main.time[pEvent]();
    for (var i = 0; i < pTimers; i++) {
      result.sub[i].time[pEvent]();
    }
    return this;
  }
  result.pauseMain  = function() {
    return this._eventMain("pause").redraw();
  }
  result.resumeMain = function() {
    return this._eventMain("resume").redraw();
  }
  result.completeMain = function() {
    return this._eventMain("complete").redraw();
  }
  result.pauseAll  = function() {
    return this._eventAll("pause").redraw();
  }
  result.resumeAll = function() {
    return this._eventAll("resume").redraw();
  }
  result.completeAll = function() {
    return this._eventAll("complete").redraw();
  }

  // add events to buttons
  time_pause.click(function() { result.pauseMain(); });
  time_resume.click(function() { result.resumeMain(); });
  time_complete.click(function() { result.completeMain(); });
  time_pause_all.click(function() { result.pauseAll(); });
  time_resume_all.click(function() { result.resumeAll(); });
  time_complete_all.click(function() { result.completeAll(); });

  // swap timers
  result.swapTimers = function(pSub) {
    var temp       = this.main;
    this.main      = this.sub[pSub];
    this.sub[pSub] = temp;
    this.main.main = true;
    this.sub[pSub].main = false;
    this.redraw();
  }
  result.getSwap = function(pSub) {
    return function() { result.swapTimers(pSub); };
  }
  for (var i = 0; i < pTimers; i++) {
    time_sub_display[i].display.click( result.getSwap(i) );
  }

  // clear values and start timers
  result.clear();
  result._tick = function() {
    this.main.tick(time_display);
    for (var i = 0; i < pTimers; i++) {
      result.sub[i].tick(time_sub_display[i]);
    }
    return this;
  }
  TempTimeTick = function() {
    result._tick();
    setTimeout("TempTimeTick()", 1000) 
  }
  TempTimeTick();

  // return temp-time controller
  return result;
}

