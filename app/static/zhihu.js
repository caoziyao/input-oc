/**
 * Created by cczy on 2017/3/23.
 */


var bindEventSearch = function () {
    // 搜索按钮
    var btnSearch = e('#id-button-search');

    // 回调函数
    var search = function(d) {
        log('search', d);


    };

    // 搜索按钮绑定事件
    btnSearch.addEventListener('click', function () {
        apiZhihuSearch(search)
    })

};


var __main = function () {
    bindEventSearch();
};


__main();