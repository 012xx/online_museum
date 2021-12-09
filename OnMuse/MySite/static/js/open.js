// ドラッグ&ドロップエリアの取得
var fileArea = document.getElementById("dropArea");
// input[type=file]の取得
// var fileInput = document.getElementById("uploadFile");
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
// fileInput.addEventListener(
//   "change",
//   function (e) {
//     var file = e.target.files[0];
//     console.log('success!')

//     if (typeof e.target.files[0] !== "undefined") {
//       // ファイルが正常に受け取れた際の処理
//       const imageWidth = e.target.files[0].width
//       if(imageWidth > 500) {
//         // 
//       }
//     } else {
//       // ファイルが受け取れなかった際の処理
//     }
//   },
//   false
// );
/*画像サイズ判定*/
// var element = document.getElementById( "#uploadFile" );

/* var intervalId = setInterval( function () {

	if (element.complete) {
		var width = element.naturalWidth ;
		var height = element.naturalHeight ;
		clearInterval(intervalId) ;
	}
}, 500 ) ; */

/*画像プレビュー*/
const fileInputRef = document.querySelector("#uploadFile");
fileInputRef.addEventListener("change", (e) => {
    console.log('success!')

  // 画像の一枚目
  // const file = e.target.files.item(0);

  //for文
  for (let num = 0; num < e.target.files.length; num++) {
  const file = e.target.files.item(num);
  const image = new Image();
  image.src = URL.createObjectURL(file);
  image.onload = () => {
    if (image.naturalWidth < 500 && image.naturalHeight < 500) {
      fileInputRef.value = "";
      return;
    }
    
    loadImage(
      file, // ロード前の画像を渡す
      (loadedImage) => { // callback ロードが終わった後に実行する関数を渡す
        document.getElementById('preview').innerHTML += '<img src="' + loadedImage + '">';
      }
    )
  }
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
function click_cb(){
	//チェックカウント用変数
	var check_count = 0;
	// 箇所チェック数カウント
	$("tag").each(function(){
		var parent_checkbox = $(this).children("input[type='checkbox']");
		if(parent_checkbox.prop('checked')){
			check_count = check_count+1;
		}
	});
	// 0個のとき（チェックがすべて外れたとき）
	if(check_count == 0){
		$("tag").each(function(){
			$(this).find(".locked").removeClass("locked");
		});
	// 3個以上の時（チェック可能上限数）
	}else if(check_count > 3){
		$("tag").each(function(){
			// チェックされていないチェックボックスをロックする
			if(!$(this).children("input[type='checkbox']").prop('checked')){
				$(this).children("input[type='checkbox']").prop('disabled',true);
				$(this).addClass("locked");
			}
		});
	}else{
		$("tag").each(function(){
			// チェックされていないチェックボックスを選択可能にする
			if(!$(this).children("input[type='checkbox']").prop('checked')){
				$(this).children("input[type='checkbox']").prop('disabled',false);
				$(this).removeClass("locked");
			}
		});
	}
	return false;
}
let outer = document.getElementById('outer');

let colorBack = document.getElementById('colorBack');
colorBack.value = "#278c72";
colorBack.addEventListener('change', function(){
  outer.style.background = this.value;
});

let colorFore = document.getElementById('colorFore');
colorFore.value = "#ffffff";
colorFore.addEventListener('change', function(){
  outer.style.color = this.value;
});