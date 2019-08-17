$(document).ready(function () {
    console.log("main.js");

// -----------------------------Upload Summary.html---------------
    if (window.location.pathname === "/dashboard/") {


        $('#summary_table').DataTable({
            "pagingType": "full_numbers",
            "lengthMenu": [[15, 30, 50, -1], [15, 30, 50, "All"]],
            responsive: true,
            language: {
                search: "_INPUT_",
                searchPlaceholder: "Search records",
            }
            // make zone region city column "visible": false and "searchable": true
            // this column should contain search term for eg. "zone" should be there in column.
            // by doing so one can search all zone/region/city by typing zone as search term.
        });
    }
}