// 要素の取得
const loveMe = document.querySelector('.loveMe')
const times = document.querySelector('#times')

// クリックイベントの登録
loveMe.addEventListener('click', (e) => {

})
// クリック時間の制御
// いいね数をカウント
let timesClicked = 0
 
// クリックイベントの登録
 
// ハートの作成
const createHeart = (e) => {
...
 
  // いいね数を増加して挿入
  times.innerHTML = ++timesClicked
}
