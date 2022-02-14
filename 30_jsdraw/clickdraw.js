var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var mode = "rect";

var toggleMode = (e) => {
  console.log("toggling..." + mode);
  if (mode == "rect") {
    mode = "circle";
  }else{
    mode = "rect";
  }
}

var drawRect = function(e) {
  var mouseX = e.offsetX;
  var mouseY = e.offsetY;
  console.log("mouseClick registered at ", mouseX, mouseY);
  ctx.fillStyle = "red";
  ctx.fillRect(mouseX, mouseY, 100, 200);
}

var drawCircle = function(e){
  var mouseX = e.offsetX;
  var mouseY = e.offsetY;
  console.log("mouseClick registered at ", mouseX, mouseY);
  ctx.fillStyle = "red";
  ctx.beginPath();
  ctx.arc(mouseX, mouseY, 50, 0, 2*Math.PI);
  ctx.fill();
}

var draw = function(e){
  if (mode == "rect"){
    drawRect(e);
  }else{
    drawCircle(e);
  }
}

var wipeCanvas = function(){
  ctx.clearRect(0,0,c.clientHeight,c.clientWidth);
}

var clearB = document.getElementById("buttonClear");
clearB.addEventListener('click',wipeCanvas);

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener('click', toggleMode);

c.addEventListener('click', draw);
