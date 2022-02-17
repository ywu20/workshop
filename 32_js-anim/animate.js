// Team Trig :: Yuqing Wu, Hebe Huang
// SoftDev pd2
// K32: More Moving Parts
// 2022-02-17


//access canvas and buttons via DOM
var c = document.getElementById('playground');
var dotButton = document.getElementById('buttonCircle');
var stopButton = document.getElementById('buttonStop');
var movieButton = document.getElementById('buttonMovie');

//prepare to interact with canvas in 2D
var ctx = c.getContext('2d');

//set fill color to team color
ctx.fillStyle = "skyblue";

var requestID, requestID2;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.clientWidth , c.clientHeight);
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
  /*
    ...to
    Wipe the canvas,
    Repaint the circle,
    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()
   */
  clear(); //wipe canvas
  stopIt(requestID); //to propagate your animations, you must pop off existing frames from the stack
            //cancelAnimationFrame first to make sure there is one animation frame running
  console.log("drawDot invoked...")
  //start drawing circle from the center
  var mouseX = c.clientWidth / 2;
  var mouseY = c.clientHeight / 2;
  console.log("mouseClick registered at ", mouseX, mouseY);

  //repaint circle
  ctx.strokeStyle = "black";
  ctx.beginPath();
  ctx.arc(mouseX, mouseY, radius, 0, 2*Math.PI);
  ctx.fill();
  ctx.stroke();

  //circle shouldn't be drawn outside of the bounds of the canvas
  //circle will start getting smaller when it hits the edges
  if (radius == Math.min(c.clientWidth, c.clientHeight) / 2) {
    growing = false;
  }
  //circle will get bigger if it is at its smallest
  if (radius == 0) {
    growing = true;
  }

  if (growing) {
    radius++;
  } else {
    radius--;
  }

  requestID = window.requestAnimationFrame(drawDot); //and provide a callback to continue animating
};


//var stopIt = function() {
var stopIt = (requestID) => {
  /*
    ...to
    Stop the animation
    You will need
    window.cancelAnimationFrame()
  */
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);
};

var drawDVD = () => {
  stopIt(requestID2);
  console.log("draw DVD ...");
  var myImage = new Image(10, 20);
  myImage.src = 'logo_dvd.jpg';
  var dx = 0;
  var dy = 0;
  ctx.drawImage(myImage, dx,dy);
  requestID2 = window.requestAnimationFrame(drawDVD);
}

dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
movieButton.addEventListener("click", drawDVD);
