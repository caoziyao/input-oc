/**
 * Created by cczy on 2017/3/23.
 */

// 这个函数的参数是一个选择器(和 CSS 选择器一样)
// 选择器语法和 CSS 选择器一样, 现在只用 3 个基础选择
// 元素选择器
var e = function (slect) {
    return document.querySelector(slect)
};


var log = function () {
    console.log.apply('console', arguments)
};