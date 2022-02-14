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
  var mouseX = e.clientX;
  var mouseY = e.clientY;
  console.log("mouseClick registered at ", mouseX, mouseY);
  ctx.fillStyle = "red";
  ctx.fillRect(mouseX, mouseY, 100, 200);
}

document.addEventListener('click', drawRect);
