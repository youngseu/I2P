/**
 * Created by yang on 18-4-13.
 */
// var ctx = document.getElementById("myChart");
// var myChart = new Chart(ctx, {
//     type: 'line',
//     data: {
//         labels: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
//         datasets: [{
//             data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
//             lineTension: 0,
//             backgroundColor: 'transparent',
//             borderColor: '#007bff',
//             borderWidth: 4,
//             pointBackgroundColor: '#007bff'
//         }]
//     },
//     options: {
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: false
//                 }
//             }]
//         },
//         legend: {
//             display: false,
//         }
//     }
// });
// var datas = [];
// for (var i = 0; i < 30; i++) {
//     datas[i] = {"name": "1" + i + "1", "age": "1：" + i + "1", "sex": "1" + i}
// }
$('#site_table').bootstrapTable({
    url: '/alldata',
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
        field: 'site',
        title: 'Site', align: "center", valign: "middle", sortable: "true", clickToSelect: "true"
    }, {
        field: 'site32',
        title: 'Site32', align: "center", valign: "middle", sortable: "true", clickToSelect: "true"
    }, {
        field: 'time',
        title: 'Time', align: "center", valign: "middle", sortable: "true"
    }],
    // data: datas
})

$('#site_table').on('click-row.bs.table', function (event, row, element, field) {
    console.log("row:" + row +" field:" + field)
    if (field != "id" || field != "time") {
        console.log(row[field]);
    }
})

$('#official_a').click(function () {
    var opt = {
        url: '/officialdata',
    };
    $('#site_table').bootstrapTable('refresh', opt);
    $('ul li a').removeClass("active");
    $(this).addClass("active");
    console.log("offical click")
});

$('#search_a').click(function () {
    var opt = {
        url: '/searchdata',
    };
    $('#site_table').bootstrapTable('refresh', opt);
    $('ul li a').removeClass("active");
    $(this).addClass("active");
    console.log("search click")
});

$('#floodfill_a').click(function () {
    var opt = {
        url: '/floodfilldata',
    };
    $('#site_table').bootstrapTable('refresh', opt);
    $('ul li a').removeClass("active");
    $(this).addClass("active");
    console.log("floodfill click")
});

$('#extend_a').click(function () {
    var opt = {
        url: '/extendata',
    };
    $('#site_table').bootstrapTable('refresh', opt);
    $('ul li a').removeClass("active");
    $(this).addClass("active");
    console.log("extend click")
});

$('#all_a').click(function () {
    var opt = {
        url: '/alldata',
    };
    $('#site_table').bootstrapTable('refresh', opt);
    $('ul li a').removeClass("active");
    $(this).addClass("active");
    console.log("all_a click")
});

$('#online_a').click(function () {
    var opt = {
        url: '/onlinedata',
    };
    $('#site_table').bootstrapTable('refresh', opt);
    $('ul li a').removeClass("active");
    $(this).addClass("active");
    console.log("online_a click")
});