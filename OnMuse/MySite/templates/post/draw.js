import "../../static/css/draw.css";
const canvas = document.querySelector("#draw-area");
const context = canvas.getContext("2d");

canvas.addEventListener("mousemove", event => {
  draw(event.layerX, event.layerY);
});
canvas.addEventListener("touchmove", event => {
  draw(event.layerX, event.layerY);
});
//パソコンでクリックしてる間だけ描けるようにした機能
canvas.addEventListener("mousedown", () => {
  context.beginPath();
  isDrag = true;
});
canvas.addEventListener("mouseup", () => {
  context.closePath();
  isDrag = false;
});
//スマホで描けるようにする機能
canvas.addEventListener("touchstart", () => {
  context.beginPath();
  isDrag = true;
});
canvas.addEventListener("touchend", () => {
  context.closePath();
  isDrag = false;
});
//お絵かきするところをきれいにする機能
const clearButton = document.querySelector("#clear-button");
clearButton.addEventListener("click", () => {
  context.clearRect(0, 0, canvas.width, canvas.height);
});
//ペンの色を変える機能
const colorRed = document.querySelector("#color-red");
colorRed.addEventListener("click", () => {
  context.strokeStyle = "red";
});
const colorBlue = document.querySelector("#color-blue");
colorBlue.addEventListener("click", () => {
  context.strokeStyle = "blue";
});
const colorGreen = document.querySelector("#color-green");
colorGreen.addEventListener("click", () => {
  context.strokeStyle = "green";
});
const colorBlack = document.querySelector("#color-black");
colorBlack.addEventListener("click", () => {
  context.strokeStyle = "black";
});
//消しゴムの機能
const eraser = document.querySelector("#eraser");
eraser.addEventListener("click", () => {
  context.strokeStyle = "white";
});
//ぺんの太さを変える機能
const penSS = document.querySelector("#pen-ss");
penSS.addEventListener("click", () => {
  context.lineWidth = 1;
});
const penS = document.querySelector("#pen-s");
penS.addEventListener("click", () => {
  context.lineWidth = 5;
});
const penM = document.querySelector("#pen-m");
penM.addEventListener("click", () => {
  context.lineWidth = 10;
});
const penL = document.querySelector("#pen-l");
penL.addEventListener("click", () => {
  context.lineWidth = 15;
});
const penLL = document.querySelector("#pen-ll");
penLL.addEventListener("click", () => {
  context.lineWidth = 20;
});

let isDrag = false;
//線をかく機能
function draw(x, y) {
  if (!isDrag) {
    return;
  }
  context.lineTo(x, y);
  context.stroke();
}