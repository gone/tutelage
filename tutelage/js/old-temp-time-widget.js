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
function TempTime(pDivID)
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
  var setText = function(pContainer, pText) {
    pContainer.html(pText);
  }
  var CtoF    = function(pC) {
    return pC * (9/5) + 32;
  }
  var FtoC    = function(pF) {
    return (pF - 32) * (5/9);
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
  var Timer = function(pDisplay) {
    var result = {};
    result.display = pDisplay;
    result.active  = false;
    result.pause   = false;
    result.seconds = 0;
    result.redraw  = function() {
      setText(this.display, timeDisplay(this.seconds));
      this.display.toggleClass("on",  this.active);
      this.display.toggleClass("off", !this.active);
      this.display.toggleClass("positive", 0 < this.seconds);
      this.display.toggleClass("negative", this.seconds < 0);
      this.display.toggleClass("zero",     0 == this.seconds);
    }
    result.tick = function() {
      if (this.active && !this.pause) {
        this.seconds -= 1;
        this.redraw();
      }
    }
    return result;
  }

  // get containing div
  var container = $("#" + pDivID);

  // create temp-time widget
  var temp_time_widget			= appendDiv(container,		"temp_time_widget");
    var temp_widget			= appendDiv(temp_time_widget,	"temp_widget");
      var temp_message			= appendDiv(temp_widget,	"temp_message");
      var temp_display			= appendDiv(temp_widget,	"temp_display");
        var temp_celsius_display	= appendDiv(temp_display,	"temp_celsius_display");
        var temp_fahrenheit_display	= appendDiv(temp_display,	"temp_fahrenheit_display");
    var time_widget			= appendDiv(temp_time_widget,	"time_widget");
      var time_message			= appendDiv(time_widget,	"time_message");
      var time_display			= appendDiv(time_widget,	"time_display");
        var main_display		= appendDiv(time_display,	"main_display");
        var sub_display			= appendDiv(time_display,	"sub_display");
          var display_a			= appendDiv(sub_display,	"display_a");
          var display_b			= appendDiv(sub_display,	"display_b");
          var display_c			= appendDiv(sub_display,	"display_c");
          var display_d			= appendDiv(sub_display,	"display_d");
      var time_control			= appendDiv(time_widget,	"time_control");
        var time_pause			= appendButton(time_control,	"time_pause",		"Pause");
        var time_resume			= appendButton(time_control,	"time_resume",		"Resume");
        var time_pause_all		= appendButton(time_control,	"time_pause_all",	"Pause All");
        var time_resume_all		= appendButton(time_control,	"time_resume_all",	"Resume All");
        var time_complete		= appendButton(time_control,	"time_complete",	"Complete");
    var temp_time_message		= appendDiv(temp_time_widget,	"temp_time_message");

  // prepare temp-time controller and timers
  var result   = {};
  result._timerPauseAll = false;
  result._timerMain     = Timer(main_display);
  result._timerSubA     = Timer(display_a);
  result._timerSubB     = Timer(display_b);
  result._timerSubC     = Timer(display_c);
  result._timerSubD     = Timer(display_d);
  result._timerOn       = function(pTimer, pSeconds) {
    pTimer.active  = true;
    pTimer.seconds = pSeconds;
    pTimer.redraw();
  }
  result._timerOff      = function(pTimer, pReset) {
    pTimer.active  = false;
    if (pReset) {
      pTimer.seconds = 0;
      pTimer.redraw();
    }
  }
  result._timerComplete = function(pTimer) {
    if (pTimer.seconds < 0) {
      this._timerOff(pTimer, true);
    }
  }

  // temperature control
  result.tempMessage	= function(pValue) { setText(temp_message, pValue); return this; };
  result.temp		= function(pC, pF) {
    setText(temp_celsius_display,    pC.toFixed(0) + " Celsius");
    setText(temp_fahrenheit_display, pF.toFixed(0) + " Fahrenheit");
    return this;
  };
  result.tempCelsius	= function(pC) { return this.temp(pC, CtoF(pC)); };
  result.tempFahrenheit	= function(pF) { return this.temp(FtoC(pF), pF); };
  result.tempClear	= function() {
    this.tempMessage("Temperature");
    setText(temp_celsius_display,    "N/A Celsius");
    setText(temp_fahrenheit_display, "N/A Fahrenheit");
    return this;
  };

  // timer control
  result.timeMessage    = function(pValue) { setText(time_message, pValue); return this; };
  result.timeMainStart  = function(pH, pM, pS) { this._timerOn(this._timerMain, HMStoS(pH, pM, pS)); return this; };
  result.timeSubAStart  = function(pH, pM, pS) { this._timerOn(this._timerSubA, HMStoS(pH, pM, pS)); return this; };
  result.timeSubBStart  = function(pH, pM, pS) { this._timerOn(this._timerSubB, HMStoS(pH, pM, pS)); return this; };
  result.timeSubCStart  = function(pH, pM, pS) { this._timerOn(this._timerSubC, HMStoS(pH, pM, pS)); return this; };
  result.timeSubDStart  = function(pH, pM, pS) { this._timerOn(this._timerSubD, HMStoS(pH, pM, pS)); return this; };
  result.timeMainStop   = function(pReset) { this._timerOff(this._timerMain, pReset); return this; };
  result.timeSubAStop   = function(pReset) { this._timerOff(this._timerSubA, pReset); return this; };
  result.timeSubBStop   = function(pReset) { this._timerOff(this._timerSubB, pReset); return this; };
  result.timeSubCStop   = function(pReset) { this._timerOff(this._timerSubC, pReset); return this; };
  result.timeSubDStop   = function(pReset) { this._timerOff(this._timerSubD, pReset); return this; };
  result.timeMainResume = function() { this._timerMain.active = true; return this; };
  result.timeSubAResume = function() { this._timerSubA.active = true; return this; };
  result.timeSubBResume = function() { this._timerSubB.active = true; return this; };
  result.timeSubCResume = function() { this._timerSubC.active = true; return this; };
  result.timeSubDResume = function() { this._timerSubD.active = true; return this; };
  result.timeClear      = function() {
    this.timeMessage("Timer");
    this.timeMainStop(true);
    this.timeSubAStop(true);
    this.timeSubBStop(true);
    this.timeSubCStop(true);
    this.timeSubDStop(true);
    return this;
  }
  result.timePauseMain  = function() {
    this._timerMain.pause = true;
  }
  result.timeResumeMain = function() {
    this._timerMain.pause = false;
  }
  result.timePauseAll  = function() {
    this._timerPauseAll = true;
  }
  result.timeResumeAll = function() {
    this._timerPauseAll = false;
  }
  result.timeCompleteAll = function() {
    this._timerComplete(this._timerMain);
    this._timerComplete(this._timerSubA);
    this._timerComplete(this._timerSubB);
    this._timerComplete(this._timerSubC);
    this._timerComplete(this._timerSubD);
  }

  // temp time control
  result.tempTimeMessage = function(pValue) { setText(temp_time_message, pValue); return this; };
  result.tempTimeClear   = function() {
    this.tempTimeMessage("...");
    this.tempClear();
    this.timeClear();
    return this;
  };

  // add events to buttons
  time_pause.click(function() { result.timeMainStop(false); });
  time_resume.click(function() { result.timeMainResume(); });
  time_pause_all.click(function() { result.timePauseAll(); });
  time_resume_all.click(function() { result.timeResumeAll(); });
  time_complete.click(function() { result.timeCompleteAll(); });

  // swap timers
  var swapTimers = function(pA, pB) {
    var temp_display   = result[pA].display;
    result[pA].display = result[pB].display;
    result[pB].display = temp_display;
    var temp_timer = result[pA];
    result[pA]     = result[pB];
    result[pB]     = temp_timer;
    result[pA].redraw();
    result[pB].redraw();
  }
  display_a.click(function() { swapTimers("_timerSubA", "_timerMain"); });
  display_b.click(function() { swapTimers("_timerSubB", "_timerMain"); });
  display_c.click(function() { swapTimers("_timerSubC", "_timerMain"); });
  display_d.click(function() { swapTimers("_timerSubD", "_timerMain"); });

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

  // return temp-time controller
  return result;
}

