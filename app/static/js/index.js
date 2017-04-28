/**
 * Created by working on 2017/4/27.
 */

var _main = function () {

    // left-menu 按钮
    $('#btnAddTags').click(function () {
        var obj = $(this);
        var val = $('.left-menu__input input').val();
        var ul = $('.left-menu__tag ul');
        if(val === ''){
           // alert('输入为空')
            return
        }

        var form = {
            type: 'tag',
            data: val
        }

        $.post("/ajax/add/tag", {
            data: JSON.stringify(form)
        }, function (data) {
            var jsons = jQuery.parseJSON(data);
            if (jsons.result == 1) {
                if (jsons.status == 1) {

                    var tagId = jsons.data.tagId;

                    var html = `<li class="left-menu__li" data-id="${tagId}"> ${val}
                        <div class="left-menu__li__text">
                            <a href="#">update</a><a href="#">delete</a>
                        </div>
                    </li>`;


                   ul.append(html);
                } else {
                    alert(jsons.msg);
                }
            } else {
                alert(jsons.msg)
            }
        });

    });

    // 激活 tags
    $('.left-menu__tag').delegate('.left-menu__li', 'click',function () {
        var obj = $(this);
        var siblings = obj.siblings();
        siblings.each(function () {
            var sibObj = $(this);
            sibObj.removeClass('left-menu__li--active');  // 去除背景颜色
        })
        obj.addClass('left-menu__li--active')  // 添加背景颜色


        // 选择 note
        var tagId = obj.attr('data-id');
        if(tagId === undefined){
            // return
            tagId = 0
        }
        var ul = $('.min-menu__title')
        var li = $('.min-menu__li:not(".all")');    // 选择非第一个
        li.remove();

        var form = {
            tagId: tagId
        }


        $.post("/ajax/select/notes", {
            data: JSON.stringify(form)
        }, function (data) {
            var jsons = jQuery.parseJSON(data);
            if (jsons.result == 1) {
                if (jsons.status == 1) {
                    var data = jsons.data;
                    for(var i=0; i<data.length; i++){
                        var tagId = data[i].tagId;
                        var noteId = data[i].noteId;
                        var note = data[i].content;
                        var html = `
                                <li class="min-menu__li"  tag-id="${tagId}" note-id="${noteId}">
                                <a class="min-menu__li_title" href="#">${note}</a>
                                    <div class="min-menu__li__text">
                                        <a href="#">update</a><a href="#">delete</a>
                                    </div>
                                </li>
                        `
                        ul.append(html);

                    }


                } else {
                    alert(jsons.msg);
                }
            } else {
                alert(jsons.msg)
            }
        });


    })


    // min-menu add
    $('#btnAddNote').click(function () {
        var obj = $(this);
        var ul = $('.min-menu__title');
        var val = $('.min-menu__search input').val();
        var tag = $('.left-menu__tag').find('li.left-menu__li--active');

        if(tag.length <1 ){
            alert('未选择 tag ')
            return;
        }

        var tagId = tag.attr('data-id');

        var form = {
            type: 'tag',
            content: val,
            tagId: parseInt(tagId)
        }

        $.post("/ajax/add/note", {
            data: JSON.stringify(form)
        }, function (data) {
            var jsons = jQuery.parseJSON(data);
            if (jsons.result == 1) {
                if (jsons.status == 1) {
                    var noteId = jsons.data.noteId;
                    var html = `
                            <li class="min-menu__li"  tag-id="${tagId}" note-id="${noteId}">
                                <a class="min-menu__li_title" href="#">${val}</a>
                                <div class="min-menu__li__text">
                                    <a href="#">update</a><a href="#">delete</a>
                                </div>
                            </li>
                    `
                    ul.append(html);
                } else {
                    alert(jsons.msg);
                }
            } else {
                alert(jsons.msg)
            }
        });



    })

    // 激活 note
    $('.min-menu__note').delegate('.min-menu__li', 'click',function () {
        var obj = $(this);
        var siblings = obj.siblings();
        siblings.each(function () {
            var sibObj = $(this);
            sibObj.removeClass('min-menu__li--active');  // 去除背景颜色
        })
        obj.addClass('min-menu__li--active')  // 添加背景颜色

        var content = $('.right-menu__view');
        var title = obj.find('.min-menu__li_title').text()

        if(title === undefined){
            title = 'Title'
        }

        $('.right-menu__title').text(title)


        var form = {
            'noteId': obj.attr('note-id')
        }

        $.post("/ajax/add/content", {
            data: JSON.stringify(form)
        }, function (data) {
            var jsons = jQuery.parseJSON(data);
            var msg = jsons.data.content;
            if (jsons.result == 1) {
                if (jsons.status == 1) {

                    content.val(msg)
                } else {
                    alert(jsons.msg);
                }
            } else {
                alert(jsons.msg)
            }
        });

    })


    // 保存按钮
    $('#btnSave').click(function () {
        var obj = $(this);
        var ul = $('.min-menu__title');
        var val = $('.min-menu__search input').val();
        var note = $('li.min-menu__li--active');

        if(note.length <1 ){
            alert('未选择 note ')
            return;
        }
        var tagId = note.attr('tag-id')
        var noteId = note.attr('note-id')
        var title = note.find('.min-menu__li_title').text()
        if(noteId === undefined){
            return;
        }
        var content = $('.right-menu__view').val()

        var form = {
            tagId: tagId,
            noteId: noteId,
            content: content,
        }

        $.post("/ajax/note/save", {
            data: JSON.stringify(form)
        }, function (data) {
            var jsons = jQuery.parseJSON(data);
            if (jsons.result == 1) {
                if (jsons.status == 1) {
                    // nothing happen
                    alert('保存成功');
                } else {
                    alert(jsons.msg);
                }
            } else {
                alert(jsons.msg)
            }
        });
    })


}


$(document).ready(function () {
    _main()
})