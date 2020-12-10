$(function () {

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
        cache: false,
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
                events: function (e, value, row, index) {
                    $.ajax({
                        url: '/api/log/access',
                        method: 'delete',
                        data: {id: row.id},
                        complete: function (req, status) {
                            $('#tbl').bootstrapTable('remove', {
                                field: 'id',
                                values: [row.id]
                            })
                        }
                    });
                },
                formatter: function (value, row, index) {
                    return [
                        '<a class="op-delete" href="javascript:void(0)" title="Like">',
                        '<i class="glyphicon glyphicon-trash"></i>',
                        '</a>  ',
                    ].join('')
                }
            }
        ],
    });

    $('#remove').click(function () {
        let selectedItems = $('#tbl').bootstrapTable('getSelections')
        if (selectedItems.length == 0) window.alert('no item selected');
        for (let i = 0; i < selectedItems.length; i++) {
            $.ajax({
                url: '/api/log/access',
                method: 'delete',
                data: {id: selectedItems[i].id},
                complete: function (req, status) {
                    $('#tbl').bootstrapTable('remove', {
                        field: 'id',
                        values: [selectedItems[i].id]
                    })
                }
            });
        }
    });
});