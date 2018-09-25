/**
 * Created by yang on 18-7-11.
 */
$('#traffic_table').bootstrapTable({
    url: '/trafficdata',
    method: 'get',
    striped: false,
    cache: false,
    sortable: false,
    pageNumber: 1,
    pageSize: 15,
    pageList: [10, 25, 50, 100],
    sidePagination: 'client',
    pagination: true,
    search: true,
    showColumns: true,
    showRefresh: false,
    smartDisplay: false,
    contentType: "application/x-www-form-urlencoded",
    clickToSelect: true,
    locale: 'zh-CN',
    columns: [{
        field: 'id',
        title: 'ID', align: "center", valign: "middle", sortable: "true"
    }, {
        field: 'srcip',
        title: 'Src-ip', align: "center", valign: "middle", sortable: "true", clickToSelect: "true"
    }, {
        field: 'srcport',
        title: 'Src-port', align: "center", valign: "middle", sortable: "true", clickToSelect: "true"
    }, {
        field: 'destip',
        title: 'Dest-ip', align: "center", valign: "middle", sortable: "true", clickToSelect: "true"
    }, {
        field: 'destport',
        title: 'Dest-port', align: "center", valign: "middle", sortable: "true", clickToSelect: "true"
    }, {
        field: 'time',
        title: 'Time', align: "center", valign: "middle", sortable: "true"
    }],
    // data: datas
})

$('#traffic_table').on('click-row.bs.table', function (event, row, element, field) {
    console.log("row:" + row +" field:" + field)
    if (field != "id" || field != "time") {
        console.log(row[field]);
    }
})

$('#flow_a').click(function () {
    var opt = {
        url: '/trafficdata',
    };
    $('#traffic_table').bootstrapTable('refresh', opt);
    $('ul li a').removeClass("active");
    $(this).addClass("active");
    console.log("offical click")
});

setInterval(function () {
    queryTraffic()
},5000);

function queryTraffic() {
    // $("#traffic_table").bootstrapTable('removeAll');
    var opt = {
        url: '/trafficdata',
    };
    $('#traffic_table').bootstrapTable('refresh', opt);
};
