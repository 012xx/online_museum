// ドラッグ&ドロップエリアの取得
var fileArea = document.getElementById("dropArea");
// input[type=file]の取得
var fileInput = document.getElementById("uploadFile");
// ドラッグオーバー時の処理
fileArea.addEventListener("dragover", function (e) {
  e.preventDefault();
  fileArea.classList.add("dragover");
});

// ドラッグアウト時の処理
fileArea.addEventListener("dragleave", function (e) {
  e.preventDefault();
  fileArea.classList.remove("dragover");
});

// ドロップ時の処理
fileArea.addEventListener("drop", function (e) {
  e.preventDefault();
  fileArea.classList.remove("dragover");
  // ドロップしたファイルの取得
  var files = e.dataTransfer.files;
  // 取得したファイルをinput[type=file]へ
  fileInput.files = files;
  if (typeof files[0] !== "undefined") {
    //ファイルが正常に受け取れた際の処理
  } else {
    //ファイルが受け取れなかった際の処理
  }
});

// input[type=file]に変更があれば実行
fileInput.addEventListener(
  "change",
  function (e) {
    var file = e.target.files[0];

    if (typeof e.target.files[0] !== "undefined") {
      // ファイルが正常に受け取れた際の処理
    } else {
      // ファイルが受け取れなかった際の処理
    }
  },
  false
);
/*1028*/ 
var fileArea = document.getElementById('dragDropArea');
var fileInput = document.getElementById('fileInput');
fileArea.addEventListener('dragover', function(evt){
  evt.preventDefault();
  fileArea.classList.add('dragover');
});
fileArea.addEventListener('dragleave', function(evt){
    evt.preventDefault();
    fileArea.classList.remove('dragover');
});
fileArea.addEventListener('drop', function(evt){
    evt.preventDefault();
    fileArea.classList.remove('dragenter');
    var files = evt.dataTransfer.files;
    console.log("DRAG & DROP");
    console.table(files);
    fileInput.files = files;
    photoPreview('onChenge',files[0]);
});
function photoPreview(event, f = null) {
  var file = f;
  if(file === null){
      file = event.target.files[0];
  }
  var reader = new FileReader();
  var preview = document.getElementById("previewArea");
  var previewImage = document.getElementById("previewImage");

  if(previewImage != null) {
    preview.removeChild(previewImage);
  }
  reader.onload = function(event) {
    var img = document.createElement("img");
    img.setAttribute("src", reader.result);
    img.setAttribute("id", "previewImage");
    preview.appendChild(img);
  };

  reader.readAsDataURL(file);
}
