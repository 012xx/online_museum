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

var _URL = window.URL || window.webkitURL;
$(`#uploadFile`).change(function (e) {
  var file, img;
  if ((file = this.files[0])) {
      img = new Image();
      img.onload = function () {
        if(this.width > 499 && this.height > 499){
          // ファイルが正常に受け取れた際の処理
        }else{
          alert('画像サイズが小さいです');
        console.log(this.width);
        }
        };
        img.src = _URL.createObjectURL(file);
        }
    });

/*画像プレビュー*/
const fileInputRef = document.querySelector("#uploadFile");
fileInputRef.addEventListener("change", (e) => {
  // 画像の一枚目
  // const file = e.target.files.item(0);

  //for文
  for (let num = 0; num < e.target.files.length; num++) {
  const file = e.target.files.item(num);
  loadImage(
    file, // ロード前の画像を渡す
    (loadedImage) => { // callback ロードが終わった後に実行する関数を渡す
      document.getElementById('preview').innerHTML += '<img src="' + loadedImage + '">';
    }
  )
}

})

const loadImage = (file, callback) => {
  const reader = new FileReader();

  //  ロードします。時間かかります。
  reader.readAsDataURL(file);

  // ロード終わったときに実行される関数
  reader.onload = () => {
    // ロードが終わった後の画像
    const loadedImage = reader.result;
    callback(loadedImage);
  }
}