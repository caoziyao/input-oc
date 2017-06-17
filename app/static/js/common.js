/**
 * Created by working on 2017/6/16.
 */

(function(){



})()

var log = console.log.bind(console);

var e = function (element) {
    var ele = document.querySelector(element)
    return ele
}

// var addListener = function (element, callback) {
//     element.addEventListener
// }
//

var ajax = function(request) {
    /*
    request 是一个 object, 有如下属性
        method, 请求的方法, string
        url, 请求的路径, string
        data, 请求发送的数据, 如果是 GET 方法则没这个值, string
        callback, 响应回调, function
    */
    var r = new XMLHttpRequest()
    r.open(request.method, request.url, true)
    if (request.contentType !== undefined) {
        r.setRequestHeader('Content-Type', request.contentType)
    }
    r.onreadystatechange = function(event) {
        if(r.readyState === 4) {
            request.callback(r.response)
        }
    }
    if (request.method === 'GET') {
        r.send()
    } else {
        console.log('requestdata', request.data)
        r.send(request.data)
    }
}


// var appendHtml = (element, html) => element.insertAdjacentHTML('beforeend', html)
