let screen = "";

function press(value){
  screen = screen + value
  document.getElementById("display").innerHTML = screen;
};

function run(){
  screen = eval(screen);
  document.getElementById("display").innerHTML = screen;
};

function erase(){
   screen = "";
   document.getElementById("display").innerHTML = screen;
};

erase()