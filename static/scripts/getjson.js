

$(document).ready(function(){
    console.log()
    vaxlist=JSON.stringify($(".data-src").text());
    table = $(".datatable").DataTable({
        columns: [
            { data: 'name' },
            { data: 'position' },
            { data: 'salary' },
            { data: 'office' }
        ],
        data: vaxlist["data"],
        dom: '<"top"f>rt<"d-flex justify-content-between" lip><"float-left">P<"clear">',
        scrollY:"200px",
        scrollX:true,
        scorllCollapse: true,
        stateSave: true,
        paging: false,
        searching: false,
        searchPanes:{
            layout: 'columns-2'
        },
        lengthMenu: [
            [3, 5, 10, 25, 50, 100, -1],
            [3, 5, 10, 25, 50, 100, 'Crash']
        ],
        columnDefs: [
            {
                
                searchPanes: {
                    header: 'lol'
                },
                targets: [2]
            },
            {
                searchPanes: {
                    show: true
                },
                targets: [8]
            },
            {
                
                searchPanes: {
                    threshold: 0.9,
                    columns: [1,2,3,4,5,6,7,8]
                },
                targets: [1,2,3,4,5,6,7,8]
            }
        ],
        select: {
            style: 'os',
            selector: 'td:first-child'
        },
        order: [[1, 'asc']]
    })
    
});
