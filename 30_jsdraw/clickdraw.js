var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var mode = "rect";

var toggleMode = (e) => {
  console.log("toggling...");
  if (mode == "rect") {
    return;
  }
  return;
}

var drawRect = function(e) {
  var mouseX = e.offsetX;
  var mouseY = e.offsetY;
  console.log("mouseClick registered at ", mouseX, mouseY);
  console.log("offsetX,y ", e.offsetX, e.offsetY);
  ctx.fillStyle = "red";
  ctx.fillRect(mouseX, mouseY, 100, 200);
}

document.addEventListener('click', drawRect);
