// draws active video onto canvas
// code taken from http://html5doctor.com/video-canvas-magic/
// Tab Atkins Jnr., 2010

	document.addEventListener('DOMContentLoaded', function(){
    var v = document.getElementById('video');
    var canvas = document.getElementById('c');
    var context = canvas.getContext('2d');

    var cw = Math.floor(canvas.clientWidth /* / 100 */);
    var ch = Math.floor(canvas.clientHeight /* / 100 */);
    canvas.width = cw;
    canvas.height = ch;

    v.addEventListener('play', function(){
        draw(this,context,cw,ch);
    },false);

},false);

function draw(v,c,w,h) {
    if(v.paused || v.ended) return false;
    c.drawImage(v,0,0,w,h);
    setTimeout(draw,20,v,c,w,h);
}

