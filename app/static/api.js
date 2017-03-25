/**
 * Created by cczy on 2017/3/24.
 */


/*
 ajax 函数
*/
var ajax = function (method, path, data, responseCallback) {
    var r = new XMLHttpRequest();
    // 设置请求方法和请求地址
    r.open(method, path, true);
    // 设置发送的数据的格式为 application/json
    // 这个不是必须的
    r.setRequestHeader('Content-Type', 'application/json');
    // r.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    // 注册响应函数
    r.onreadystatechange = function() {
        if(r.readyState === 4) {
            // log('r', r);
            // r.response 存的就是服务器发过来的放在 HTTP BODY 中的数据
            responseCallback(r.response)
        }
    }
    // 把数据转换为 json 格式字符串
    data = JSON.stringify(data);
    // 发送请求
    r.send(data);
};


// zhihu API
var apiZhihuSearch = function(callback) {
    var path = '/api/zhihu/search';
    ajax('GET', path, '', callback)
};

// login API
var apiLogin = function (data, callback) {
    var path = '/ajax/login';
    ajax('POST', path, data, callback)
};

// login API
var apiRegister = function (data, callback) {
    var path = '/ajax/register';
    ajax('POST', path, data, callback)
};