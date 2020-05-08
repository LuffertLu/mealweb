var copy="mealweb";
function getCurrentDate()
{
var t = new Date();//获取当前时间
var year = t.getFullYear();//获取当前时间年份
var month = t.getMonth();//获取当前时间月份
var day = t.getDate();//获取当前时间日
var week = t.getDay();//获取当前时间星期
var arr = new Array ("星期一","星期二","星期三","星期四","星期五","星期六","星期日",);
//上行是为规划星期的输出
//下3行分别获得当前时间的时 分 秒 
var hour = t.getHours();
var minute = t.getMinutes();
var second = t.getSeconds();
var nowTime = year+"/"+month+"/"+day+" "+arr[week]+" "+hour+((minute<10)?":0":":")+minute+((second<10)?":0":":")
+second+((hour>12)?".pm":".am");
document.write(nowTime);
}
/*
* 根据固定宽高的盒子，让图片自由居中显示的方法
* 盒子长200px，宽145px
*/
// $(".imgNeedChange")为通过jq获取到的图片数组,对单个图片进行处理时去掉for循环即可
function imgDispose() {
  for(var i = 0; i < $(".imgNeedChange").length; i++) {
    document.getElementsByClassName('imgNeedChange')[i].onload = function(e) {
      e.stopPropagation();
      if(this.width / this.height > (200 / 145)) {
        $(this).css({
          "top": "0",
          "left": -(this.width / this.height * 145 - 200) / 2 + "px",
          "height": "145px",
          "width": "auto"
        });
      } 
      else {
        $(this).css({
          "left": "0",
          "top": -(this.height / this.width * 200 - 145) / 2 + "px",
          "width": "200px",
          "height": "auto"
        });
      }
    }
  }
}


(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 56)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 56
  });

})(jQuery); 

