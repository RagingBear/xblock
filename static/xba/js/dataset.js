$(function () {
    // rich text
    var richEditors = [];
    $.each($('.rich-text'), function (index, obj) {
        const editor = new window.wangEditor(obj);
        editor.create();
        richEditors.push(editor);
    });

    $(".dataset-detail").hide();

    $(".op-edit").click(function () {
        $(".btn-back").show();
        $(".dataset-detail").show();
        $(".dataset-list").hide();
        console.log("op click");
    });

    $(".btn-back").click(function () {
        $(".btn-back").hide();
        $(".dataset-list").show();
        $(".dataset-detail").hide();
        console.log("back click");
    });

    $('#tbl').bootstrapTable({
        // 翻页配置
        sidePagination: "server",
        url: '/api/log/access',
        method: 'GET',
        pageNumber: 1,
        pageSize: 10,
        pagination: true,
        pageList: [10, 25, 50, 100],
        queryParams: function (params) {
            return {
                limit: params.limit,
                offset: params.offset,
            }
        },

        // 样式和工具栏配置
        search: true,
        toolbar: '#toolbar',
        striped: true,
        clickToSelect: true,

        // 表单数据配置
        columns: [
            {
                field: 'state',
                checkbox: true,
                align: 'center',
                valign: 'middle'
            }, {
                title: 'ID',
                field: 'id',
                align: 'center',
                valign: 'middle',
            }, {
                title: 'ip',
                field: 'ip',
                align: 'center',
                valign: 'middle',
            }, {
                title: 'path',
                field: 'path',
                align: 'center',
                valign: 'middle',
            }, {
                title: 'referer',
                field: 'referer',
                align: 'center',
                valign: 'middle',
            }, {
                title: 'time',
                field: 'time',
                align: 'center',
                valign: 'middle',
            }, {
                field: 'operate',
                title: 'operate',
                align: 'center',
                clickToSelect: false,
                events: {
                    'click .op-delete': function (e, value, row, index) {
                        $.ajax({
                            url: '/api/log/access',
                            method: 'delete',
                            data: {id: row.id},
                        })
                    }
                },
                formatter: function (value, row, index) {
                    return [
                        '<a class="op-delete" href="javascript:void(0)" title="Remove">',
                        '<i class="glyphicon glyphicon-trash"></i>',
                        '</a>'
                    ].join('')
                },
            }
        ],
    });

});