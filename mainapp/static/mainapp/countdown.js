var timeleft = 60;

var startTime = 0;
var currentTime = 0;

function convertSeconds(s) {
  var min = floor(s / 60);
  var sec = s % 60;
  return nf(min, 2) + ':' + nf(sec, 2);
}
function reDirect() {
              window.location="../result";
           }


function setup() {
  noCanvas();
  startTime = millis();

  var timer = select('#timer');
  timer.html(convertSeconds(timeleft - currentTime));

  var interval = setInterval(timeIt, 1000);

  function timeIt() {
    currentTime = floor((millis() - startTime) / 1000);
    timer.html(convertSeconds(timeleft - currentTime));
    if (currentTime == timeleft) {
      clearInterval(interval);
      reDirect();
    }
    if((timeleft-currentTime)<10){
      document.getElementById("timer").style="color:red;"
    }
  }

}
