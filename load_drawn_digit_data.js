
var path = 'C:/Users/k21pa/dev/PersonalProject/PERSONAL_PROJECT_FINAL_PRODUCT/FINAL_PRODUCT_USERDRAWN';

// var equation_size = window.prompt("How long is your equation? ");
var equation_size = 3;


function draw_guidelines(){
  var guidelines = equation_size - 1;
  for(var i = 1;i<=guidelines;i++){
    strokeWeight(1);
    console.log(width,height);
    line((i*width/equation_size), 0, (i*width/equation_size), height);
  }
}


function setup(){
  let c = createCanvas(600,200);
  background(255);
  draw_guidelines();

  var PredictButton = select('#Predict');
  PredictButton.mousePressed(function() {
    for(var i = 1;i<equation_size;i++){
      saveCanvas(c,'Userdrawn_' + i + '_Number.jpg');
      if(i%2 == 0){
        index = (i/2);
        saveCanvas(c,'Userdrawn_'+ index + '_Operator.jpg');
      }
    }
  });
  var ClearButton = select('#Clear');
    ClearButton.mousePressed(function() {
    background(255);
    draw_guidelines();
  });
}

function draw() {
  strokeWeight(20);
  stroke(0);
  if (mouseIsPressed) {
    line(pmouseX, pmouseY, mouseX, mouseY);
  }
}
