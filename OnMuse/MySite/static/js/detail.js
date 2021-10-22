$(function(){
    //--------------------------------------------------------------------------------
    // マウスホイールで横スクロール処理
    //--------------------------------------------------------------------------------
    // スクロール後の位置
    var moving;
    // スクロール後の位置+余韻の距離
    var aftermov;
    // 余韻の距離
    var after = 200;
    // 1スクロールの移動距離
    var speed = 30;
    // アニメーション
    var animation = 'easeOutCirc';
    // アニメーションスピード
    var anm_speed = 500;
    $('.horizontal-scroll').mousewheel(function(event, mov) {
    // スクロール後の位置の算出
    var moving = $(this).scrollLeft() - mov * speed;
    // スクロールする
    $(this).scrollLeft(moving);
        // 余韻の計算
        if (mov < 0) {
        // 下にスクロールしたとき
        aftermov =  moving + after;
        } else {
        // 上にスクロールしたとき
        aftermov =  moving - after;
        }
        // 余韻アニメーション
        $(this).stop().animate({scrollLeft: aftermov}, anm_speed, animation);
        // 縦スクロールさせない
        return false;
    });
});